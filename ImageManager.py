import os
import math

from PIL import Image
from Help import Help


class ImageManager(object):

    def __init__(self, input_dir=None, output_dir=None, image_weight=None, input_files=None):
        """ Constructor """
        self._allowed_file_extension = ('.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.png')

        self._input_dir = input_dir
        self._output_dir = output_dir
        self._input_files = input_files
        self._output_image_weight = image_weight  # [MB]
        self._appended_string = "_resized"

        self._image_list = []

    def _search_images(self):
        """ Search for all images into current directory """
        # List all files into current directory
        files_into_dir = []
        if os.path.exists(self._input_dir):
            files_into_dir = os.listdir(self._input_dir)
        else:
            Help().error_message("Input directory not valid")
            pass

        # Search for each file with allowed extension and store them into list of dictionaries
        for file in files_into_dir:
            (name, ext) = os.path.splitext(file)

            if ext in self._allowed_file_extension:
                # Get the absolute path of each file
                abs_path = os.path.abspath(self._input_dir + '/' + file)
                self._image_list.append({'file': file,
                                         'name': name,
                                         'ext': ext,
                                         'abspath': abs_path,
                                         'size': round(os.path.getsize(abs_path)/(1024**2), 2)
                                         })
            else:
                # Nothing
                pass
        # If there's no images into directory
        if not self._image_list:
            Help().warning_message("No image into directory")
        else:
            # Nothing
            pass

    def _resize_images(self):
        """ Resize images """
        if self._input_files is None or len(self._input_files) == 0:
            Help().error_message("No input file specified")
        # Parse all images
        elif 'all' in self._input_files:
            for image in self._image_list:
                self._resizing_algorithm(image)
        # Parse specified images only
        else:
            for file in self._input_files:
                for count, image in enumerate(self._image_list):
                    if file == image['file']:
                        self._resizing_algorithm(image)
                        break
                    elif count == len(self._image_list)-1:
                        Help().warning_message(file + ' is not in the directory')
                    else:
                        # nothing
                        pass
                pass

    def _resizing_algorithm(self, image):
        if image['size'] > int(self.output_image_weight):
            # Print which file is under resizing
            print("-Resizing " + image['file'])

            # Calculate scale factor
            scale_factor = math.sqrt(image['size'] / self._output_image_weight)

            # Open Image and calculate the new size using scale factor
            tmp_image = Image.open(image['abspath'])
            new_size = tuple([int(x / scale_factor) for x in list(tmp_image.size)])

            # Resize and save the image into output directory
            tmp_image = tmp_image.resize(new_size, Image.BILINEAR)
            tmp_image.save(self._output_dir + '/' + image['name'] + '_compressed' + image['ext'])
            print('--Saved: ' + image['name'] + self._appended_string + image['ext'])
        else:
            # Nothing
            pass

    def _create_output_directory(self):
        """ Create output files directory, if not exists """
        try:
            os.makedirs(self._output_dir)
        except FileExistsError:
            pass

    def main(self):
        """ """
        # Search for images into directory
        self._search_images()

        # Create output directory
        self._create_output_directory()

        # Resize images
        self._resize_images()

    # **************** Properties **************** #
    @property
    def input_dir(self):
        return self._input_dir

    @input_dir.setter
    def input_dir(self, in_dir):
        self._input_dir = in_dir

    @property
    def output_dir(self):
        return self._output_dir

    @output_dir.setter
    def output_dir(self, out_dir):
        self._output_dir = out_dir

    @property
    def input_files(self):
        return self._input_files

    @input_files.setter
    def input_files(self, files):
        self._input_files = files

    @property
    def output_image_weight(self):
        return self._output_image_weight

    @output_image_weight.setter
    def output_image_weight(self, image_weight):
        self._output_image_weight = image_weight

    # def _directory_tree(self):
    #     current_dir=os.curdir
    #     root_list=[]
    #     dirs_list=[]
    #     files_list=[]
    #
    #     print(current_dir)
    #
    #     for root, dirs, files in os.walk(current_dir):
    #         root_list.append(root)
    #         dirs_list.append(dirs_list)
    #         files_list.append(files)
    #
    #     print("ROOT")
    #     print(root_list)
    #
    #     print("\n DIRS")
    #     print(dirs_list)
    #
    #     print("\n FILES")
    #     print(files_list)
    #
    #     startpath=current_dir
    #     for root, dirs, files in os.walk(startpath):
    #         level = root.replace(startpath, '').count(os.sep)
    #         indent = ' ' * 4 * (level)
    #         print('{}{}/'.format(indent, os.path.basename(root)))
    #         subindent = ' ' * 4 * (level + 1)
    #         for f in files:
    #             print('{}{}'.format(subindent, f))










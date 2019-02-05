from PIL import Image
import sys
import os
import math


class ImageManager(object):

    def __init__(self, input_dir=None, output_dir=None, image_weight=None, input_files=None):
        """ Constructor """
        self._allowed_file_extension = ('.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.png')

        self._input_dir = input_dir
        self._output_dir = output_dir
        self._input_files = input_files
        self._output_image_weight = image_weight  # [MB]

        self._image_list = []

    def _search_images(self):
        """ Search for all images into current directory """
        # List all files into current directory
        if os.path.exists(self._input_dir):
            files_into_dir = os.listdir(self._input_dir)
        else:
            # TODO: print error and help
            sys.exit()
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
        #print(self._image_list)

    def _compress_images(self):
        """ """
        if self._input_files is None or len(self._input_files) == 0:
            print ("Specify a file name")  # TODO print decente
            sys.exit()
        # Parse all images
        elif self._input_files == 'all':
            for image in self._image_list:
                self._compression_algorithm(image)
        # Parse specified images only
        else:
            for file in self._input_files:
                for count, image in enumerate(self._image_list):
                    if file == image['file']:
                        self._compression_algorithm(image)
                        break
                    elif count == len(self._image_list)-1:
                        print('Warning: ' + file + ' is not in the directory')
                pass

    def _compression_algorithm(self, image):
        if image['size'] > int(self.output_image_weight):
            # Calculate scale factor
            scale_factor = math.sqrt(image['size'] / self._output_image_weight)

            # Open Image and calculate the new size using scale factor
            tmp_image = Image.open(image['abspath'])
            new_size = tuple([int(x / scale_factor) for x in list(tmp_image.size)])

            # Resize and save the image into output directory
            tmp_image = tmp_image.resize(new_size, Image.BILINEAR)

            print('Compressed: ' + image['name'] + '_compressed' + image['ext'])
            tmp_image.save(self._output_dir + '/' + image['name'] + '_compressed' + image['ext'])
        else:
            pass

    def _create_output_directory(self):
        """ Create output files directory, if not exists """
        try:
            os.makedirs(self._output_dir)
        except FileExistsError:
            pass

    def start(self):
        self._search_images()
        self._create_output_directory()
        self._compress_images()

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


#ImageManager().start()

# ImageManager()._create_out_directory()

# image = Image.open("Image.jpg")
# new_size = tuple([int(x/2) for x in list(image.size)])
# print(new_size)
#
# image.resize(new_size)
# image.save('saved.jpg')
# im
#
# #image.resize(image.size/2)

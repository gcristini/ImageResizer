import os
import math

from PIL import Image
from Help import Help
import sys


class ImageManager(object):
    """ """

    # ************************************************* #
    # **************** Private Methods **************** #
    # ************************************************* #
    def __init__(self, input_dir=None, output_dir=None, image_size=None, input_files=None, include_subdir=None):
        """ Constructor """
        self._allowed_file_extension = ('.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.png')

        self._input_dir = input_dir
        self._output_dir = output_dir
        self._input_files = input_files
        self._output_image_size = image_size  # [MB]
        self._appended_string = "_resized"
        self._include_subdir = include_subdir

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
                size = round(os.path.getsize(abs_path) / (1024 ** 2), 2)
                if size > self._output_image_size:
                    self._image_list.append({'file': file,
                                             'name': name,
                                             'ext': ext,
                                             'abspath': abs_path,
                                             'relroot': '',
                                             'size': size
                                             })
                else:
                    # Nothing
                    pass
            else:
                # Nothing
                pass

        # If there's no images into directory
        if not self._image_list:
            Help().error_message("No image into directory")
        else:
            # Nothing
            pass

    def _search_images_sub(self):
        """ Search for all images into current directory and subdirectories"""
        # List all files into current directory and subdirectories
        if os.path.exists(self._input_dir):
            for (root, _, files) in os.walk(self._input_dir):
                for file in files:
                    (name, ext) = os.path.splitext(file)
                    if ext in self._allowed_file_extension:
                        # Get the absolute path of each file
                        abs_path = (root + '/' + file)
                        relroot = root.replace(self._input_dir, '', 1)
                        self._image_list.append({'file': file,
                                                 'name': name,
                                                 'ext': ext,
                                                 'relroot': relroot,
                                                 'abspath': abs_path,
                                                 'size': round(os.path.getsize(abs_path) / (1024 ** 2), 2)
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
        else:
            Help().error_message("Input directory not valid")
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
        if image['size'] > int(self.output_image_size):
            # Print which file is under resizing
            print("-Resizing " + image['file'])

            # Calculate scale factor
            scale_factor = math.sqrt(image['size'] / self._output_image_size)

            # Open Image and calculate the new size using scale factor
            tmp_image = Image.open(image['abspath'])
            new_size = tuple([round(x / scale_factor) for x in list(tmp_image.size)])

            # Resize and save the image into output directory
            tmp_image = tmp_image.resize(new_size, Image.BILINEAR)
            tmp_image.save(self._output_dir + image['relroot'] + '/' + image['name'] + '_compressed' + image['ext'])
            print('--Saved: ' + image['name'] + self._appended_string + image['ext'])
        else:
            # Nothing
            pass

    def _create_output_directory_sub(self):
        for image in self._image_list:
            try:
                os.makedirs(self._output_dir + image['relroot'])
            except FileExistsError:
                pass

    def _create_output_directory(self):
        """ Create output files directory, if not exists """
        try:
            os.makedirs(self._output_dir)
        except FileExistsError:
            pass

    # ************************************************ #
    # **************** Public Methods **************** #
    # ************************************************ #
    def main(self):
        """ """
        if self._include_subdir == True:
            # Search for images into directory and subdirectories
            self._search_images_sub()

            # Create output directory with subdirectories
            self._create_output_directory_sub()
        else:
            # Search for images into directory
            self._search_images()

            # Create output directory
            self._create_output_directory()

        # Resize images
        self._resize_images()

    # ******************************************** #
    # **************** Properties **************** #
    # ******************************************** #
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
    def include_subdir(self):
        return self._include_subdir

    @include_subdir.setter
    def include_subdir(self, boolean):
        self._include_subdir = boolean

    @property
    def output_image_size(self):
        return self._output_image_size

    @output_image_size.setter
    def output_image_size(self, image_size):
        self._output_image_size = image_size


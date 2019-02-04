
from PIL import Image
import sys
import os


class ManageImage:

    def __init__(self):
        """ Constructor """
        self._allowed_file_extension = ('.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.png')
        self._output_dir = 'out'
        self._image_list = []
        pass

    def _search_images(self):
        """ Search for all images into current directory """
        # List all files into current directory
        files_into_dir = os.listdir()

        # Search for all file with allowed extension and store them into list of dictionaries
        for file in files_into_dir:
            (name, ext) = os.path.splitext(file)

            if ext in self._allowed_file_extension:
                self._image_list.append({'name': name, 'ext': ext})

        #print(self._image_list)

    def _create_out_directory(self, ):
        """ Create output files directory, if not exists """
        try:
            os.makedirs(self._output_dir)
        except FileExistsError:
            pass


ManageImage()._create_out_directory()

# image = Image.open("Image.jpg")
# new_size = tuple([int(x/2) for x in list(image.size)])
# print(new_size)
#
# image.resize(new_size)
# image.save('saved.jpg')
# im
#
# #image.resize(image.size/2)

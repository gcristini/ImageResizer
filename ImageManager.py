from PIL import Image
import sys
import os


class ImageManager:

    def __init__(self):
        """ Constructor """
        self._allowed_file_extension = ('.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.png')

        self._input_dir = os.curdir
        self._output_dir = self._input_dir + '/' + 'out'
        self._output_image_weight = 1  # [MB]

        self._image_list = []

    def _search_images(self):
        """ Search for all images into current directory """
        # List all files into current directory
        files_into_dir = os.listdir(self._input_dir)

        # Search for each file with allowed extension and store them into list of dictionaries
        for file in files_into_dir:
            (name, ext) = os.path.splitext(file)

            if ext in self._allowed_file_extension:
                self._image_list.append({'name': name, 'ext': ext})

        # print(self._image_list)

    def _create_out_directory(self):
        """ Create output files directory, if not exists """
        try:
            os.makedirs(self._output_dir)
        except FileExistsError:
            pass

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
        print(self._output_dir)

    @property
    def output_image_weight(self):
        return self._output_image_weight

    @output_image_weight.setter
    def output_image_weight(self, image_weight):
        self._output_image_weight = image_weight

    def start(self):
        self._search_images()
        self._create_out_directory()

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

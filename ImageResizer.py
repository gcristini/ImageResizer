#!/usr/bin/env python

import sys
import os
from Parser import Parser
from ImageManager import ImageManager
from Help import Help


class ImageResizer(object):

    def __init__(self):
        """ Constructor """
        self._parse_dict = {
            '-id': self._parse_fun_id,
            '-od': self._parse_fun_od,
            '-if': self._parse_fun_if,
            '-w': self._parse_fun_w,
            '-h': self._parse_fun_h
        }

        # Initialize Parser with input arguments and parser dictionary
        self._parser = Parser(input_args=sys.argv[1:],
                              parse_dict=self._parse_dict)

        # Initialize ImageManager with "default parameters"
        self._image_manager = ImageManager(input_dir=os.curdir,
                                           output_dir=os.curdir + '/out',
                                           image_weight=1,
                                           input_files='all')

    def main(self):
        """ """
        # Parse input arguments
        self._parser.parse_input_args()

        # Run image manager
        self._image_manager.main()

    # ******** Parser Dictionary Functions ******** #
    def _parse_fun_id(self, argv):
        """ Parser function [-id]: set input directory of ImageManager """
        if argv:
            self._image_manager.input_dir = argv[0]
        else:
            pass

    def _parse_fun_od(self, argv):
        """ Parser function [-od]: set output directory of ImageManager """
        # Set output directory
        if argv:
            self._image_manager.output_dir = self._image_manager.input_dir + '/' + argv[0]
        else:
            pass

    def _parse_fun_if(self, argv):
        """ Parser Function [-if]: set input files of ImageManager """
        if argv:
            self._image_manager.input_files = argv
        else:
            pass

    def _parse_fun_w(self, argv):
        """ Parser function [-w]: set weight for compressed output images """
        if argv:
            self._image_manager.output_image_weight = argv[0]
        else:
            pass

    @staticmethod
    def _parse_fun_h(argv):
        """ Parser function [-h]: print help """
        # Print help
        Help().print_help()


ImageResizer().main()
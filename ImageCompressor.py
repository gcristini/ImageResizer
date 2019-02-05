#!/usr/bin/env python

import sys
from PIL import Image
from Parser import Parser
from ImageManager import ImageManager


class Main:

    def __init__(self):
        pass

    def start(self):
        """ """
        # Parse input arguments
        parse=Parser()


        im=ImageManager()

        parse.parse_input_args()
        im.start()
        #

        # print(self.count)
        # print(self.program_name)
        # print(self.arguments)
        return


Main().start()






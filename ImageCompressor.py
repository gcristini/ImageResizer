#!/usr/bin/env python

import sys
from PIL import Image
from Parser import Parser


class Main:

    def __init__(self):
        pass

    @staticmethod
    def parse_arguments():
        """ """
        Parser().parse_args()

        return

    def start(self):
        """ """
        #Parse input argumnents
        self.parse_arguments()

        # print(self.count)
        # print(self.program_name)
        # print(self.arguments)
        return


Main().start()






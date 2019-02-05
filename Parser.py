import sys
from ImageManager import ImageManager


class Parser(object):

    def __init__(self, input_args=None, parse_dict=None):
        """ Constructor """
        if parse_dict is None:
            parse_dict = dict()

        self._input_args = input_args
        self._parse_dict = parse_dict

    def parse_input_args(self):
        """ Main function """
        input_arg_dict = {}
        key_index_list = []

        # First key argument must init with '_'
        if self._input_args:
            try:
                self._input_args[0][0] == '-'
            except:
                self._parse_error_status("Error: first key argument must init with '-' ")

        # Store index of key arguments which init with '-'
        for count, input_arg in enumerate(self._input_args):
            if input_arg[0] == '-':
                key_index_list.append(count)
            if count == len(self._input_args)-1:
                # Store a fake index in order to have the length of array into key_index_list
                key_index_list.append(count+1)

        # Create dictionary with input "key" and "value" arguments
        for curr_index, next_index in zip(key_index_list, key_index_list[1:]):
            input_arg_dict.update({self._input_args[curr_index]: self._input_args[curr_index+1:next_index]})

        # Search into parser dictionary
        for arg in list(input_arg_dict.keys()):
            if arg in self._parse_dict:
                # Execute function of dictionary at arg key
                self._parse_dict[arg](input_arg_dict[arg])
            else:
                self._parse_error_status('Error: ' + arg + ' is not a valid argument')

    @staticmethod
    def _print_help():
        """ """
        print("Print Help: TODO")

    def _parse_error_status(self, error_message):
        """ """
        print(error_message + '\n')
        self._print_help()
        sys.exit()


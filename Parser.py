import sys


class Parser:

    def __init__(self):
        """ """
        self._program_name = sys.argv[0]
        self._input_args = sys.argv[1:]

        self._parse_dict = {
            '-a': self._parse_fun_a,
            '-b': self._parse_fun_b,
            '-c': self._parse_fun_c
        }

    def parse_args(self):
        """ """
        input_arg_dict = {}
        key_index_list = []

        # First key argument must init with '_'
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
    def _parse_fun_a(*argv):
        """ Insert here code you want to execute """
        print('_parse_fun_a')
        print(argv)

    @staticmethod
    def _parse_fun_b(*argv):
        """ Insert here code you want to execute """
        print('_parse_fun_b')
        print(argv)

    @staticmethod
    def _parse_fun_c(*argv):
        """ Insert here code you want to execute """
        print('_parse_fun_c')
        print(argv)

    @staticmethod
    def _print_help():
        """ """
        print("Print Help: TODO")

    def _parse_error_status(self, error_message):
        """ """
        print(error_message + '\n')
        self._print_help()
        sys.exit()


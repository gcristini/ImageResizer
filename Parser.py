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
        count = 0

        # Create a dictionary based on input arguments
        for arg in enumerate(self._input_args):
            try:
                input_arg_dict.update({self._input_args[count]: self._input_args[count+1]})
            except IndexError:
                self._parse_error_status('Error: each key argument needs a parameter')
            count += 2
            if count > len(self._input_args) - 1:
                break

        # Search into parser dictionary
        for arg in list(input_arg_dict.keys()):
            if arg in self._parse_dict:
                self._parse_dict[arg](input_arg_dict[arg])
            else:
                self._parse_error_status('Error: ' + arg + ' is not a valid argument')

    def _parse_fun_a(self, *argv):
        """ Insert here code you want to execute """
        print('_parse_fun_a')
        print(argv)

    def _parse_fun_b(self, *argv):
        """ Insert here code you want to execute """
        print('_parse_fun_b')
        print(argv)

    def _parse_fun_c(self, *argv):
        """ Insert here code you want to execute """
        print('_parse_fun_c')
        print(argv)

    def _print_help(self):
        """ """
        print("Print Help")

    def _parse_error_status(self, error_message):
        """ """
        print(error_message + '\n')
        self._print_help()
        sys.exit()


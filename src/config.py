import os
import sys

import yaml
import optparse

usage = "usage: %prog [options] arg"
parser = optparse.OptionParser(usage)


class PyConfig():
    # single activity for basic checking 
    _path_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _path_config =  os.path.join(_path_base, "cfg")

    print("PyConfig() : {_base}, {_cfg}".format(_base=_path_base, _cfg=_path_config))
    if not os.path.exists(_path_config):
        os.makedirs(_path_config)  

    # Constructor method 
    def __init__(self, is_debug=True):
        self.debug = is_debug

    def read_config(self, file_cfg):
        _file_cfg = os.path.join(PyConfig._path_config, file_cfg)
        if not os.path.exists(_file_cfg):
            raise Exception('Error : {_cfg} is not present'.format(_cfg=_file_cfg))
                      
        with open(_file_cfg, 'r') as rd:
            self.config = yaml.safe_load(rd)

    def get_config(self):
        return self.config


if __name__ == "__main__":
    print("OWNEY Command: %s\n" % (" ".join(sys.argv[:])))

    usage = "usage: %prog [options] arg"
    usage += "\nex1) run on Cron mode for a external reporting : python config.py --cron --report"
    
    parser = optparse.OptionParser(usage)

    parser.add_option("", "--test", dest="test", help="Run as Test Mode", action="store_true", default=False)

    (options, args) = parser.parse_args()

    if options.test == False:
        parser.print_help()
        sys.exit(1)


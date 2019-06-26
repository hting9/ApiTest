import configparser
import os


def get_config_data(section,option,config_file="config.ini"):

    conf = configparser.ConfigParser()
    current_path=os.path.abspath(os.path.dirname("__file__"))
    file_path = os.path.join(current_path,'conf',config_file)
    print (file_path)
    conf.read(file_path,encoding="utf-8")
    return conf.get(section,option)


get_config_data("logging","level")
import configparser
import os
import re

def get_config_data(section,option,config_file="config.ini"):

    conf = configparser.ConfigParser()
    current_path=os.path.split(os.path.realpath(__file__))[0]

    file_path = os.path.join(current_path,'conf',config_file)
    conf.read(file_path,encoding="utf-8")
    return conf.get(section,option)


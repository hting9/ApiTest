import csv
import yaml
import json
import logger

def _check_format(file_path, content):
    """ check testcase format if valid
    """
    if not content:
        # testcase file content is empty
        err_msg = u"Testcase file content is empty: {}".format(file_path)
        logger.log_error(err_msg)

    elif not isinstance(content, (list, dict)):
        # testcase file content does not match testcase format
        err_msg = u"Testcase file content format invalid: {}".format(file_path)
        logger.log_error(err_msg)

def load_yaml_file(yaml_file):
    with open(yaml_file,'r',encoding='utf-8') as stream:
        yaml_content = yaml.load(stream,Loader=yaml.FullLoader)
        _check_format(yaml_file, yaml_content)
        return yaml_content

def load_json_file(json_file):
    with open(json_file, encoding='utf-8') as data_file:
        try:
            json_content= json.load(data_file)
        except Exception as result:
            logger.log_error(result)

def load_csv_file(csv_file):
    with open(csv_file, encoding='utf-8') as data_file:



import csv,yaml,json
import os
import logger,utils

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
        _check_format(json_file, json_content)
        return json_content


def load_csv_file(csv_file):
    csv_content_list = []
    with open(csv_file, encoding='utf-8') as data_file:
        reader = csv.DictReader(data_file)
        for row in reader:
            csv_content_list.append(row)
    return csv_content_list

def load_file(file_path):
    file_suffix = os.path.splitext(file_path)[1].lower()
    if file_suffix == '.json':
        return load_json_file(file_path)
    elif file_suffix in ['.yaml', '.yml']:
        return load_yaml_file(file_path)
    elif file_suffix == ".csv":
        return load_csv_file(file_path)
    else:
        err_msg = u"Unsupported file format: {}".format(file_path)
        logger.log_warning(err_msg)
        return []



def load_testcase():
    pass



import requests
import loader
import logger
def run_test(file_path):

    test_data = loader.load_file(file_path)
    logger.log_debug(test_data)
    req_kwargs = test_data['request']
    url = req_kwargs.pop('url')
    method = req_kwargs.pop('method')
    print(test_data)
    resp_obj = requests.request(url=url, method=method,**req_kwargs)
    return resp_obj


run_test("E:/BaiduNetdiskDownload/ApiTest/test/api/parase.yml")
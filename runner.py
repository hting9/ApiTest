import requests
import loader

def run_test(file_path):
    test_data = loader.load_file(file_path)
    req_kwargs = test_data['request']
    url = req_kwargs.pop('url')
    method = req_kwargs.pop('method')
    resp_obj = requests.request(url=url, method=method, **req_kwargs)
    return resp_obj
import os,subprocess
import pytest
if __name__=="__main__":
    path="E:/BaiduNetdiskDownload/ApiTest/test/testcases/parsing/test_paring.py"
    pytest.main(['-q',path,'--alluredir=./result/ '])
    command="allure generate  ./result/ -o ./report/ --clean"
    subprocess.call(command,shell=True)
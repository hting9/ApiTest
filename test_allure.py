import os,subprocess
import pytest

def test_add():
    assert 3==4

if __name__=="__main__":
  #  path="E:/BaiduNetdiskDownload/ApiTest/test/testcases/parsing/test_paring.py"
   # pytest.main(['-q',path,'--alluredir=./result/ '])
    pytest.main(['-q','test_allure.py','--alluredir=./result/ '])
    command="allure generate  ./result/ -o ./report/ --clean"
    subprocess.call(command,shell=True)
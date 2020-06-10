#Structuring a Python Application

From: https://realpython.com/lessons/structuring-python-application/

## Exmaple 1
Virtual env: _python3 -m venv env_ <br>
Activate virtual env:  _source env/bin/activate_

* Single python file containing all the code,
     *  Run Code: _python helloworld.py_
     *  Run Tests: _python -m unittest tests.py_
     *  Capture dependencies for both tests and code: _pip freeze > requirements.txt_
     

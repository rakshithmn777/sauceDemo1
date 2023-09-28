1. Make sure to install the latest python in local and add to path(during the installation, 
   it'll add to path by default)
2. Clone this repo and make sure to create a virtual environment by selecting the interpreter
   (if using a IDE such as Pycharm, it'll ask or create it manually)
3. Go to the terminal, make sure you're in the project root path. 
   i. run set_up.bat
   ii. Incase if it fails, install the packages listed in requirements.txt using pip one by one or if 
       Pycharm, go to setting, under project, there will be python interpreter. Select that and install
       the packages that is listed in requirements.txt
4. Using a webdriver manager, no need to specify the path for chromedriver
5. Use IDE such as pycharm to run a single test or run pytest "testcase_path"(eg, pytest .\testcases\test_one.py) - must be in project rootpath
6. Run pytest -v --html=./reports/report.html testcases/ in the terminal(must be in root path) to get the report - Run all the testcases available on testcases directory

Framework - Hybrid Framework
Reporting - Pytest
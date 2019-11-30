SET PATH=%PATH%; C:\Users\ArnavG\AppData\Local\Programs\Python\Python37-32\Scripts
cd "D:\Google CLoud Class\PyMicroservices-master\Source"
python runtests.py
python -m coverage run -m pytest && coverage xml -o coverage.xml
copy "D:\Google CLoud Class\PyMicroservices-master\Source\python_tests_xml\*.*" "D:\Google CLoud Class\PyMicroservices-master\python_tests_xml\*.*"
copy "D:\Google CLoud Class\PyMicroservices-master\Source\coverage.xml" "D:\Google CLoud Class\PyMicroservices-master\coverage.xml"

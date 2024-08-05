@echo off
echo Installing Python Packages
echo This May Take A While On The First Run


pip install -r requirements.txt

echo Succesfully installed required packages!
echo Please Wait...

python app.py
echo Process Terminated With Code 2010
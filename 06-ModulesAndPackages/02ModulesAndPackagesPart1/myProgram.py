from myModule import my_func
# from MyMainPackage.some_main_script import report_main
# from MyMainPackage.subPackage.mySubScript import sub_report

from MyMainPackage import some_main_script
from MyMainPackage.subPackage import mySubScript

my_func()
some_main_script.report_main()
mySubScript.sub_report()
import colorama
from colorama import Fore
colorama.init(autoreset=True)
import unittest
import sys
sys.path.append("..")
from usecase import Purchase
from myexception import InvalidWholeSaleError
class ExceptionalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("output_exception_revised.txt","w") as f:
            pass
    def test_whole_sale_error(self):
        try:
            obj=Purchase.obtain_purchase_with_amount("101,2-3-2021,venu,bat,500.00,4,helmet,1500.00,4,vickets,1500.00,2")
            with open("output_exception_revised.txt","a") as f:
                f.write("TestWholeSaleError=False\n")
                print("{}TestWholeSaleError = {}Failed".format(Fore.YELLOW,Fore.RED))
        except InvalidWholeSaleError as e:
            with open("output_exception_revised.txt","a") as f:
                f.write("TestWholeSaleError=True\n")
                print("{}TestWholeSaleError = {}Passed".format(Fore.YELLOW,Fore.GREEN))


    def test_value_error(self):
        try:
            obj=Purchase.obtain_purchase_with_amount("101abc,2-3-2021,venu,bat,500.00,4,ball,200,2,guard,200.00,2,helmet,1500.00,4,vickets,1500.00,2")
            with open("output_exception_revised.txt","a") as f:
                f.write("TestValueError=False\n")
                print("{}TestValueError = {}Failed".format(Fore.YELLOW,Fore.RED))
        except ValueError as e:
            with open("output_exception_revised.txt","a") as f:
                f.write("TestValueError=True\n")
                print("{}TestValueError = {}Passed".format(Fore.YELLOW,Fore.GREEN))

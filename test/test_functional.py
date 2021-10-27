# import colorama
# from colorama import Fore
# colorama.init(autoreset=True)
import unittest
import sys
sys.path.append("..")
from usecase import Purchase
class FuctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("output_revised.txt","w") as f:
            pass
    def test_object_type(self):
        obj=Purchase.obtain_purchase_with_amount("101,2-3-2021,venu,bat,500.00,4,ball,200,2,guard,200.00,2,helmet,1500.00,4,vickets,1500.00,2")
        if type(obj)!=type(None):
            with open("output_revised.txt","a") as f:
                f.write("TestObjectType=True\n")
                # print("{}TestObjectType = {}Passed".format(Fore.YELLOW,Fore.GREEN))
                print("TestObjectType = Passed")
        else:
            with open("output_revised.txt","a") as f:
                f.write("TestObjectType=False\n")
                # print("{}TestObjectType = {}Failed".format(Fore.YELLOW,Fore.RED))
                print("TestObjectType = Failed")

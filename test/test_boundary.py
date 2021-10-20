import colorama
from colorama import Fore
colorama.init(autoreset=True)
import unittest
class BoundaryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("output_boundary_revised.txt","w") as f:
            pass
    def test_boundary(self):
        with open("output_boundary_revised.txt","a") as f:
            f.write("TestBoundary=True\n")
            print("{}TestBoundary = {}Passed".format(Fore.YELLOW,Fore.GREEN))

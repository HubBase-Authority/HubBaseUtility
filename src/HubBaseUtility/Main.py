def Programm1():
    print("Hello world")

__version__ = "0.0.1.0.00"
import time
ProgrammNumber = 19
programmList = {1: Programm1()}
def Showcase():
    print(f"HubBase Utility {__version__} programm showcase - {ProgrammNumber} programms")
    for programm in range(1, ProgrammNumber+1):
        print(f"Programm №{programm} launching")
        time.sleep(1)
        programmList[programm]

Showcase()
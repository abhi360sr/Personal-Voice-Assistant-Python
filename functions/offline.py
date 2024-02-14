import os
import subprocess as sp
paths={
   'notepad':r"C:\Users\abhis\AppData\Local\Microsoft\WindowsApps\notepad.exe",
   'calculator': "C:\\Windows\\System32\\calc.exe",
   'microsoftword': r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
   
}
def notepad():
    os.startfile(paths['notepad'])

def calculator():
    os.startfile(paths['calculator'])

def microsoftword():
    os.startfile(paths['microsoftword'])

def cmpt():
    os.system('start cmd')
    
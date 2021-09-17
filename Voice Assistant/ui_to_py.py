
# --! Required Module
from PyQt5 import uic

with open("loginsgdfg.py","w",encoding="utf-8") as fout:
    uic.compileUi("signup.ui",fout)

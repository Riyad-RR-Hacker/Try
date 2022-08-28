import os, sys
try:
    __import__("jxr").Main()
except Exception as e:
    exit(str(e))

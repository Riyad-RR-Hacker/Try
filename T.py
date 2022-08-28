import os, sys
try:
    __import__("ttyy").Main()
except Exception as e:
    exit(str(e))

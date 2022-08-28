import os, sys
try:
    __import__("tert").Main()
except Exception as e:
    exit(str(e))

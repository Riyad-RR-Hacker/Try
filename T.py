import os, sys
try:
    __import__("ran").Main()
except Exception as e:
    exit(str(e))

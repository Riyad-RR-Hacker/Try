import os, sys
try:
    __import__("trrr").menu()
except Exception as e:
    exit(str(e))

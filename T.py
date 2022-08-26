import os, sys
try:
    __import__("sus").menu()
except Exception as e:
    exit(str(e))

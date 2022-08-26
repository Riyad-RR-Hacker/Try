import os, sys
try:
    __import__("qq").menu()
except Exception as e:
    exit(str(e))

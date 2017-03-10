import os

def run(**args):
    print "[*] In environment module"
    print os.environ
    return str(os.environ)

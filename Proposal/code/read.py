import os


def readfile(number: int):
    dirname = f"Proposal/OTP-{number}"
    dir = os.listdir(dirname)
    if 'index.html' in dir:
        pass
    if 'index.md' in dir:
        pass
    


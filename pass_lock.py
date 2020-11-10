import os

class PassNotFound(Exception):
    pass

def CheckForPass(filetocheck):
    if os.path.exists(filetocheck):
        pass
    else:
        raise PassNotFound("The specified pass was not found.")

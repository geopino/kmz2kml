import os

from pathlib import Path

def removeZipDir(myPath): 
    test = os.listdir(myPath)
    for item in test:
        if item.endswith(".zip"):
            os.remove(os.path.join(myPath, item))
if __name__ == '__main__':
    removeZipDir()
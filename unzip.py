import zipfile

from pathlib import Path

# Extracting all .zip files
def unzip(myPath):
    p = Path(myPath)
    for f in p.glob('*.zip'):
        with zipfile.ZipFile(f, 'r') as archive:
            archive.extractall(path=myPath+f'/{f.stem}')
            #print(f'Done {f.stem}')

if __name__ == '__main__':
    unzip()
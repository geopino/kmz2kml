import os


def remove_zip_dir(myPath):
    test = os.listdir(myPath)
    for item in test:
        if item.endswith(".zip"):
            os.remove(os.path.join(myPath, item))


if __name__ == "__main__":
    remove_zip_dir()

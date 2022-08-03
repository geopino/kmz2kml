import os


def kmz_2_zip(myPath):

    for filename in os.listdir(myPath):
        base_file, ext = os.path.splitext(filename)
        if ext == ".kmz":
            os.rename(
                os.path.join(myPath, filename), os.path.join(myPath, base_file + ".zip")
            )


if __name__ == "__main__":
    kmz_2_zip()

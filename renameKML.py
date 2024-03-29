import os


def rename_kml(myPath):
    folders = os.listdir(myPath)
    for folder in folders:
        if "." in folder:
            pass
        else:
            files = os.listdir(r"{}/{}".format(myPath, folder))

            # Accessing files inside each folder
            for file in files:

                # Getting the file extension
                extension_pos = file.rfind(".")
                extension = file[extension_pos:]
                # Renaming the files
                os.rename(
                    r"{}/{}/{}".format(myPath, folder, file),
                    r"{}/{}/{}{}".format(myPath, folder, folder, extension),
                )


if __name__ == "__main__":
    rename_kml()

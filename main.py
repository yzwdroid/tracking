import os
import shutil
from os import listdir
from os.path import isfile, join
import pathlib
from pathlib import Path

baseURL = r"C:\Users\Isabella Liu\Documents\tracking"
baseURL = pathlib.PureWindowsPath(baseURL)

while True:
    code = input("please enter the tracking code: ")
    folder = join(baseURL, code)
    donePath = join(folder, "done")
    Path(donePath).mkdir(parents=True, exist_ok=True)
    allFiles = [f for f in listdir(folder) if isfile(join(folder, f)) and
                f.startswith(code[0])]
    print(allFiles)

    if allFiles:
        file = join(baseURL, code, allFiles[0])
        dest = join(baseURL, code, "done", allFiles[0])
        shutil.move(file,dest)
        os.startfile(dest, "print")
    else:
        print("no files to print")

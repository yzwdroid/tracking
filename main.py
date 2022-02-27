import os
import shutil
from os import listdir
from os.path import isfile, join
from pathlib import Path

baseURL = "/Users/zyang/src/project/"

while True:
    code = input("please enter the tracking code: ")
    folder = join(baseURL, code)
    donePath = join(folder, "done")
    Path(donePath).mkdir(parents=True, exist_ok=True)
    allFiles = [f for f in listdir(folder) if isfile(join(folder, f))]

    if allFiles:
        file = join(baseURL, code, allFiles[0])
        desc = join(baseURL, code, "done", allFiles[0])
        print(file)
        print(desc)
        #os.startfile(file, "print")
        shutil.move(file,desc)
    else:
        print("no files to print")

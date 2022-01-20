import os
import re

dirToRead = "C:\\Users\\Tony\\Documents\\repositories\\unzippedInstructions\\extracted_content"

for folder, subFolder, file in os.walk(dirToRead):
    print(f"Currently looking at {folder}")
    print("\n")
    
    print("The subfolders are:")
    for subFold in subFolder:
        print(f"\tSubfolder: {subFold}")
        
    print("\n")
    print("The files are: ")
    for f in file:
        print(f"\tFile: {f}")
        fileToRead = open(f"{folder}\{f}", "r")
        print(f"Reading file: {f}")
        lines = fileToRead.read()
        
        phonePattern = re.compile(r"\d{3}-\d{3}-\d{4}")
        phone = re.search(phonePattern, lines)
        if phone:
            print("Found!")
            print(phone.group())
            break
    else:
        continue
    break
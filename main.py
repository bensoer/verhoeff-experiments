import os
import sys
from argparser import ArgParcer
import verhoeff

arguments = sys.argv

mode = ArgParcer.getValue(arguments, "-m")
value = ArgParcer.getValue(arguments, "-v")

if mode == "" or value == "":
    print("Mode Parameter And Value Parameter Required")
    exit(0)

if mode == "GENCHECK":
    print("Generating Checksum Values For Value")

    if value == "":
        print("Value Required In Order To Generate Checksum")
        exit(0)
    else:
        print("Got Value " + value)
        print("Value As Int : " + str(int(value)))
        checksumValue = verhoeff.calcsum(int(value))
        print("The Checksum Value Is " + str(checksumValue))
        completeChecksum = verhoeff.generateVerhoeff(int(value))
        print("The Complete Number With Checksum Is " + str(completeChecksum))

if mode == "TESTCHECK":
    print("Testing Checksum Number For Twins")

    for (index, entry) in enumerate(value):
        if index + 1 < len(value):

            if entry == value[index+1]:
                print("Found Two Twins In The Number " + str(entry) + " At Index " + str(index) + " And "
                      + str(value[index+1]) + " At Index " + str(index+1))
                print("Testing By Increment")
                valueCopy = value[0:index] + str(int(value[index]) + 1) + str(int(value[index+1]) + 1) + value[index+2:]

                print("Old Value: " + str(value) + " New Value: " + str(valueCopy))

                if verhoeff.validateVerhoeff(int(valueCopy)):
                    print("New Value " + str(valueCopy) + " Is Valid")
                else:
                    print("New Value " + str(valueCopy) + " Is Invalid")

                print("Testing By Decrement")

                valueCopy = value[0:index] + str(int(value[index]) - 1) + str(int(value[index+1]) - 1) + value[index+2:]

                print("Old Value: " + str(value) + " New Value: " + str(valueCopy))

                if verhoeff.validateVerhoeff(int(valueCopy)):
                    print("New Value " + str(valueCopy) + " Is Valid")
                else:
                    print("New Value " + str(valueCopy) + " Is Invalid")





#!/usr/bin/python3


import sys
import re


chars=dict({1:'(', 2:')',3:'{', 4:'}', 5:'[', 6:']'})
status={1:0,2:0,3:0,4:0,5:0,6:0}

string = str(sys.argv[1])

print("Input String: " + string)

items = chars.items()
dict_val = list(chars.values())

def find_index(val):
    for key, value in items:
        if val == value:    
            return key

def validate_str(input_str):
    for i in input_str:
        count=0
        index = find_index(i)
        loc1 = string.find(i)
        print("Loc1 :", loc1)
        print("Next char: ",  chars[int(index+1)])

        if(status[index+1] == 1):
            continue
        loc2 = string.find(chars[index+1])
        if(loc2 > 0):
            status[index+1] = 1;


        print("Loc2 :", loc2)
        if((loc2-loc1) % 2 !=0  or ( loc1-loc2) % 2 !=0) :
            count = count+1
            continue
        else:
            print("false")
            exit(0)

validate_str(string)

if (__name__== 'main'):
    main()

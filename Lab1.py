# original autor: maksim32
# Rewrite to Python 3: Code0N
# Original date: 2017-09-10
# Rewrite date: 02.04.2021

import sys
 
g_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,."
 
def Trisemus(key, strval, action):
    keyword, (height, width) = key
    isEncode = True if action == "encode" else False
    isDecode = True if action == "decode" else False
    
    # building table
    pos = 0
    table = [['.' for x in range(width)] for y in range(height)]
    hchars = {}
    for i in keyword + g_alphabet:
        if hchars.get(i) == None:
            hchars[i] = pos
            table[int(pos / width)][pos % width] = i
            pos += 1
            if pos >= width * height:
                break
    print("Debug table\n")
    #print('\n'.join(' '.join(j for j in table[i]) for i in range(len(table)))) # debug: output table
    
    result = ""
    for i in strval:
        pos = hchars.get(i)
        if pos != None:
            x = pos % width
            if isEncode:
                y = (int(pos / width) + 1) % height
            elif isDecode:
                y = (int(pos / width) - 1 + height) % height
            else:
                y = int(pos / width) % height # do nothing
            result += table[y][x]
        else: # then you need to select one of the actions with symbols that are not in the table :
            result += i # leave unchanged 
            #result += "" # delete 
            #result += table[height - 1][width - 1] # replace to last in table
    
    return result
 
 
keyword = input("Please, enter keyword: ")
tablesize = (11, 11)
key = (keyword, tablesize)
print("key = " + str(key))
 
inputstr = input("Text to encode: ")
 
print("Given string: '{}'\n".format(inputstr))
s = Trisemus(key, inputstr, "encode")
print("Encoded text '{}'\n".format(s))
s = Trisemus(key, s, "decode")
print("Decoded text '{}'\n".format(s))
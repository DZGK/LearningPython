# coding: utf-8
"""
入力
2 6
Welcome to the python ! and bab !
"""
import sys

input_line = sys.stdin.readlines()
start, end = [ int(x) for x in input_line[0].split(" ")]
word = input_line[1]

print(str(start) + "--" + str(end))
print(word)

i = 1
result = ""
for s in word:
    if i >= start and i <= end:
        result = result + s.upper()
    else:
        result = result + s
    i += 1
    
print(result)    

from functools import reduce
import re

file1 = open('input10.txt', 'r')
Lines = file1.readlines()

test_array = [20,60,100,140,180,220]

count = 1
next_add = -1
register = 1 # start value
modify_register = []

running_total = 0

for line in Lines:
  line = line.strip()
  
  #print("LINE = {}".format(line))
  if line != "noop":
    modify_register.append(int(line.split(" ")[1]))
    print("MODIFY REGISTOR = {}".format(modify_register))

    count += 1

    if count in test_array:
      print("COUNT {}, VALUE = {}".format(count, register))
      running_total += count * register
    
    count += 1
    register += modify_register.pop(0)

    if count in test_array:
      print("COUNT {}, VALUE = {}".format(count, register))
      running_total += count * register
  else:
    count += 1
    if count in test_array:
      print("COUNT {}, VALUE = {}".format(count, register))
      running_total += count * register


  print("REGISTER {} NOW {}".format(count, register))

print("Running total = {}".format(running_total))
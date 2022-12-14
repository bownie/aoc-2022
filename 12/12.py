from functools import reduce
import re

file1 = open('input12.txt', 'r')
Lines = file1.readlines()

array = []
tried_path_array
def build_array(count, line):
  array.append([])
  for char in line:
    array[count].append(char)

count = 0 
for line in Lines:
  build_array(count, line.strip())
  count += 1

def print_array():
  for i in range(0, len(array)):
    for j in range(0, len(array[i])):
      print("{}".format(array[i][j]), end="")
    print("");

print_array()


def find_letter(char):
  for i in range(0, len(array)):
    for j in range(0, len(array[i])):
      if array[i][j] == char:
        return (i, j)

  return (-1, -1)

def select_direction(cur_pos):
  return cur_pos

def move_me(cur_pos):
  if array[cur_pos[0]][cur_pos[1]] == "S":
    return cur_pos

  return cur_pos



def solve_path():
  start_pos = find_letter("S")
  end_pos = find_letter("E")

  if start_pos[0] == -1 and start_pos[1] == -1 or end_pos == (-1, -1):
    print("Failed to find start or end")
    exit(1)

  print("Start position = {}".format(start_pos))
  print("End position   = {}".format(end_pos))

  my_pos = start_pos
  move_count = 0
  while my_pos != end_pos:
    move_count += 1
    my_pos = move_me(my_pos)
 

  print("Total count = {}".format(move_count))

solve_path()


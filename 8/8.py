from functools import reduce
import re

file1 = open('input8.txt', 'r')
Lines = file1.readlines()

array = []
scenic_score_array = []

def build_array(line):
  array.append(str(line))
   
for line in Lines:
    build_array(line.strip())

def analyse_visible(row, col):
  #print("Analyse row {} , col {} = [{}]".format(row, col, array[row][col]))

  # edge trees
  if row == 0 or row == len(array) -1 or col == 0 or col == len(array) - 1:
    return True
  else:
    # analyse row and col
    is_visible = True
    for i in range(0,col):
      if array[row][i] >= array[row][col] and col != i:
        #print("#1 - {} is greater than {}".format(array[row][i], array[row][col]))
        is_visible = False

    if is_visible:
      return True

    is_visible = True
    for i in range(len(array) - 1, col, -1):
      if array[row][i] >= array[row][col] and col != i:
        #print("#2 - {} is greater than {}".format(array[row][i], array[row][col]))
        is_visible = False

    if is_visible:
      return True

    is_visible = True
    for i in range(0, row):
      if array[i][col] >= array[row][col] and row != i:
        #print("#3 - {} is greater than {}".format(array[i][col], array[row][col]))
        is_visible = False

    if is_visible:
      return True

    is_visible = True
    for i in range(len(array) - 1, row, -1):
      if array[i][col] >= array[row][col] and row != i:
        #print("#4 - {} is greater than {}".format(array[i][col], array[row][col]))
        is_visible = False

    #print("IS VISIBLE = {}".format(is_visible))
    return is_visible

def determine_scenic_score(row, col):

  print()
  print("Starting from {}, {}".format(row,col))
  print()

  if row == 0 or col == 0 or row == len(array) - 1 or col == len(array) - 1:
    return 0

  # for all other cases
  view_lengths = [0, 0, 0, 0]

  #print("")
  #print("Starting from {}, {}".format(row,col))
  # go up
  for i in range(col - 1, -1, -1):
    print("Going up at {}, {} comparing {} to {}".format(row,i, array[row][i], array[row][col]))
    view_lengths[0] += 1
    if array[row][i] >= array[row][col]:
      break
    print("+1 up")

  # do down
  for i in range(col + 1, len(array)):
    print("Going down at {}, {}".format(row,i))
    view_lengths[1] += 1
    if array[row][i] >= array[row][col]:
      break
    print("+1 down")

  # do left
  for i in range(row - 1, -1, -1):
    print("Going left at {}, {}".format(i,col))
    view_lengths[2] += 1
    if array[i][col] >= array[row][col]:
      break
    print("+1 left")

  # do right
  for i in range(row + 1, len(array)):
    print("Going right at {}, {}".format(i,col))
    view_lengths[3] += 1
    if array[i][col] >= array[row][col]:
      break
    print("+1 right")

  print("View length array = {}".format(view_lengths))
  total_view_length = reduce((lambda x, y: x * y), view_lengths)
  print("At {}, {} : TVL = {}".format(row, col, total_view_length))

  # https://book.pythontips.com/en/latest/map_filter.html
  return total_view_length


def print_array():
  print("")

  for row in range(0, len(array)):
    for char in range(0, len(array)):
      print("{}".format(array[row][char]), end="")
    print("")

  print("")

visible = 0
for row, value in enumerate(array):
  scenic_score_array.append([])
  for col, value in enumerate(array[row]):

    if analyse_visible(int(row), int(col)):
      visible += 1

    scenic_score_array[row].append(determine_scenic_score(int(row), int(col)))

    #print("Number = {}".format(col))

print("Total visible = {}".format(visible))

print("Total lines in scenic_score_arry = {}".format(len(scenic_score_array)))

print_array()
#exit(0)

highest = 0
for row in range(0, len(scenic_score_array)):
  for char in range(0, len(scenic_score_array)):
    print("{}".format(scenic_score_array[row][char]), end="")
    if scenic_score_array[row][char] > highest:
      highest = scenic_score_array[row][char]
  print("")

print("Highest value = {}".format(highest))
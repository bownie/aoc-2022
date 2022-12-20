from functools import reduce
import re

file1 = open("input20.txt", 'r')
Lines = file1.readlines()

original_array = []
working_array = []
move_index = 0

def build_array(line):
  original_array.append(int(line))

for line in Lines:
    build_array(line.strip())

# Make a copy
working_array = original_array.copy()

def find_location(current_value, input_array):
  for i in range(0, len(input_array)):
    if input_array[i] == current_value:
      return i
  return -1

def step_right(move_value):
  orig_array_size = len(original_array) - 1
  start_location = find_location(move_value, working_array)
  number_of_steps = move_value % orig_array_size

  for i in range(0, number_of_steps):
    to_pos = (start_location + i + 1) % orig_array_size
    from_pos = (start_location + i) % orig_array_size

    # if we move to the end then we skip to the beginning
    if to_pos == 0:
      # first swap - then pop and push
      store_value = working_array[orig_array_size]
      working_array[orig_array_size] = working_array[from_pos]
      working_array[from_pos] = store_value

      store_value = working_array.pop(orig_array_size)
      working_array.insert(0, store_value)
      continue

    store_value = working_array[to_pos]
    working_array[to_pos] = working_array[from_pos]
    working_array[from_pos] = store_value

def step_left(move_value):
  orig_array_size = len(original_array) - 1
  start_location = find_location(move_value, working_array)
  number_of_steps = (-move_value) % orig_array_size

  for i in range(0, number_of_steps):

    to_pos = (start_location - i - 1) % orig_array_size
    from_pos = (start_location - i) % orig_array_size

    # If placing at zero then we pop and push and loop again
    if to_pos == 0 and i == number_of_steps - 1:
      store_value = working_array[to_pos]
      working_array[to_pos] = working_array[from_pos]
      working_array[from_pos] = store_value

      store_value = working_array.pop(0)
      working_array.append(store_value)
      continue

    # special case here for zero as we're taking off and pushing back
    if from_pos == 0:
      store_value = working_array.pop(0)
      working_array.append(store_value)
      to_pos = orig_array_size - 1
      from_pos = orig_array_size

    store_value = working_array[to_pos]
    working_array[to_pos] = working_array[from_pos]
    working_array[from_pos] = store_value

def modify_array():
    for move_position in range(0, len(original_array)):
      if original_array[move_position] > 0:
        step_right(original_array[move_position])
      else:
        step_left(original_array[move_position])


report_numbers = [1000, 2000, 3000]

def iterate_through_result_array():
  # count through original array
  count = 0
  found_zero = False
  part_1_sum = 0

  while not found_zero or count < max(report_numbers):

    for move_position in range(0, len(working_array)):
      if found_zero:
        #print("Number {} at count {}".format(working_array[move_position], count))
        count += 1

      if count in report_numbers:
        print ("Number at {} is {}".format(count, working_array[move_position]))
        part_1_sum += working_array[move_position]

      if working_array[move_position] == 0:
        found_zero = True

  print("Part 1 Sum = {}".format(part_1_sum))

print("ORIGINAL ARRAY = ",original_array)

modify_array()

print("COMPLETED WORKING ARRAY = ",working_array)

iterate_through_result_array()


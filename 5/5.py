# Using readlines()
file1 = open('input5.txt', 'r')
Lines = file1.readlines()


debug = False
sum = 0

# A different measure
#
stacks = {}

def insert_bottom_of_stack(stack_number, letter):
  if stack_number not in stacks.keys():
    if debug:
      print("Create stack {}".format(stack_number))
    stacks[stack_number] = []

  if debug:
    print("Insert Letter {} on stack {}".format(letter, stack_number))
    
  stacks[stack_number].insert(0, letter)


def max_height_stack():
  height = 0

  for key in stacks.keys():
    if len(stacks[key]) > height:
      height = len(stacks[key])
  
  return height

def print_stacks():
  #print("Sorted Keys = {}".format(sorted(stacks.keys())))

  for stack in sorted(stacks.keys()):
    print(" {} :".format(stack + 1), end="")    
    for x in range(0, len(stacks[stack])):
      print(" [{}] ".format(stacks[stack][x]), end="")
    print()


# Single crate move
#
def single_crate_move_number_from_to(number, from_column, to_column):

  for _ in range(0, number):
    stacks[to_column].append(stacks[from_column].pop())

  if debug:
    print_stacks()


# Multiple crate move (invert pop twice)
#
def multi_crate_move_number_from_to(number, from_column, to_column):

  pop_column = []    
  for _ in range(0, number):
    pop_column.append(stacks[from_column].pop())

  for _ in range(0, number):
    stacks[to_column].append(pop_column.pop())

  if debug:
    print_stacks()

def print_top_of_stacks():
  print("Top of all the stacks: ", end="")
  for stack in sorted(stacks.keys()):
    print(stacks[stack][len(stacks[stack]) - 1], end="")
  print()

line_count = 0

# Strips the newline character
for line in Lines:

    if line_count < 8:

      for i in range(0, 9):
        position = 1 + (i * 4)
        if line[position] != " ":
          insert_bottom_of_stack(i, line[position])
    else:
      # decode move lines
      tokens=line.split(" ")

      if tokens[0] == "move":
        number_to_move = int(tokens[1])
        from_column = int(tokens[3])
        to_column = int(tokens[5])

        if debug:
          print ("Move # {} from {} to {}".format(number_to_move, from_column, to_column))

        if number_to_move and from_column and to_column:
          single_crate_move_number_from_to(number_to_move, from_column - 1, to_column - 1)

    # increment
    line_count += 1

print_stacks()

print_top_of_stacks()


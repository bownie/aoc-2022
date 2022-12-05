# Using readlines()
file1 = open('input3.txt', 'r')
Lines = file1.readlines()

sum = 0


def find_common_letter(first, second):
  for letter in first:
    if letter in second:
      return letter
  return ""

def find_common_letter_in_three(first, second, third):
  for first_letter in first:
    if first_letter in second and first_letter in third:
      return first_letter
  return ""


def decode_letter(letter):
  if (letter.islower()):
    return ord(letter) - 96
  else:
    return ord(letter) - 38

# Strips the newline character
for line in Lines:

    line = line.strip()

    #print ("Length : {}".format(len(line)));
    first_half =  line[:int(len(line)/2)]
    second_helf = line[int(len(line)/2):]

    print ("First Half  : {}".format(first_half))
    print ("Second Half : {}".format(second_helf))

    common_letter = find_common_letter(first_half, second_helf)

    print("Common letter : {}, {}".format(common_letter, decode_letter(common_letter)))

    sum += decode_letter(common_letter)


print("Total sum : {}".format(sum))

# Part 2

group1 = ""
group2 = ""
group3 = ""
sum=0

# Strips the newline character
for line in Lines:

    line = line.strip()

    if group1 == "":
      group1 = line; 
    elif group2 == "":
      group2 = line
    else:
      group3 = line

      found_letter = find_common_letter_in_three(group1, group2, group3)

      print("Group letter : {}".format(found_letter))
      sum += decode_letter(found_letter)

      group1 = ""
      group2 = ""
      group3 = ""



print("Total sum (part two): {}".format(sum))

# Using readlines()
file1 = open('input4.txt', 'r')
Lines = file1.readlines()

sum = 0

# A different measure
#
any_overlap = 0

#def find_common_letter(first, second):
##  for letter in first:
#    if letter in second:
#      return letter
#  return ""


# Strips the newline character
for line in Lines:

    line = line.strip()
    elf_assignment = line.split(",")

    
    #print("ELF ASS 1 : {}".format(elf_assignment[0]))
    #print("ELF ASS 2 : {}".format(elf_assignment[1]))

    elf_1_lowerbound = int(elf_assignment[0].split("-")[0])
    elf_1_upperbound = int(elf_assignment[0].split("-")[1])

    #print ("ELF 1 LOWER BOUND : {}".format(elf_1_lowerbound))
    #print ("ELF 1 UPPER BOUND : {}".format(elf_1_upperbound))

    elf_2_lowerbound = int(elf_assignment[1].split("-")[0])
    elf_2_upperbound = int(elf_assignment[1].split("-")[1])

    #print ("ELF 2 LOWER BOUND : {}".format(elf_2_lowerbound))
    #print ("ELF 2 UPPER BOUND : {}".format(elf_2_upperbound))

    if (elf_1_lowerbound >= elf_2_lowerbound and elf_1_upperbound <= elf_2_upperbound) or (elf_2_lowerbound >= elf_1_lowerbound and elf_2_upperbound <= elf_1_upperbound):
      sum += 1

    ## PART 2 - any overlap is slightly different

    # had it the wrong way around elf_1_lowerbound >= elf_2_upperbound
    #
    if (elf_1_upperbound >= elf_2_lowerbound and elf_1_lowerbound <= elf_2_upperbound) or (elf_2_upperbound >= elf_1_lowerbound and elf_2_lowerbound <= elf_1_upperbound):
      print("GOT AN OVERLAP {} {}".format(elf_assignment[0], elf_assignment[1]))
      any_overlap += 1
    else:
      print()
      print("NO OVERLAP {} {}".format(elf_assignment[0],elf_assignment[1]))
      print()


print("Total contained : {}".format(sum))
print("Any overlap = {}".format(any_overlap))

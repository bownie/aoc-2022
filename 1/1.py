# Using readlines()
file1 = open('input1.txt', 'r')
Lines = file1.readlines()
  
elf_number=1
count = 0
biggest_elf=0
top_count = 0

elves = {}
elf_total_list = []


# Strips the newline character
for line in Lines:

    line = line.strip()

    #print("LINE = {}".format(line))

    if not line:
      print("Elf {}: {}".format(elf_number, count))

      if count > top_count:
        biggest_elf = elf_number
        top_count = count

      elves[elf_number] = count
      elf_total_list.append(count)

      count = 0
      elf_number += 1;

    else:
      count += int(line)
    
    #print("COUNT = {}".format(count))

print("Last Elf {}: {}".format(elf_number, count))

print("Biggest Elf {} = {}".format(biggest_elf, top_count))


## Part two
# 
# Navigate the hashmap
#
elf_total_list.sort(reverse=True)

print("LIST = ", elf_total_list)

print("TOP 3 = {}".format(elf_total_list[0] + elf_total_list[1] + elf_total_list[2]))
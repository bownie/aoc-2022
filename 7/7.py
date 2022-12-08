import re

file1 = open('input7.txt', 'r')
Lines = file1.readlines()


debug = True
dir_structure = {}
current_node = []
current_dir_size = 0

files_directories = {}

def add_to_current_node(sub_dir):
  current_node.append(sub_dir)

def remove_from_current_node():
  current_node.pop()

def analyse_line(input_line):
  tokens = input_line.split(" ")

  if tokens[0] == "$":
    if tokens[1] == "cd":
      if tokens[2] == "..":
        #go up a level
        remove_from_current_node()
      else:
        # go down a level
        add_to_current_node(tokens[2])
  else:
    # push current node into our hash
    if tokens[0] != "dir":
      file_size = int(tokens[0])

      key = ':'.join(map(str, current_node))

      print("KEY = {}".format(key))
      # add file to all dirs above
      #
      build_key = ""
      for dir_key in key.split(":"):
        if build_key == "":
          build_key = dir_key 
        else:
          build_key += ":" + dir_key

        # Add key if doesn't exist
        #
        if (build_key not in files_directories):
          files_directories[build_key] = 0

        files_directories[build_key] += file_size
        print("ADD key {} += {}".format(build_key, file_size))
    
for line in Lines:
    analyse_line(line.strip())


sum = 0 
for key in files_directories.keys():
  if (files_directories[key] < 100000):
    print("key {} = {}".format(key, files_directories[key]))
    sum += files_directories[key]


print("Total lines = {}".format(len(files_directories.keys())))
print("Total sum < 100000 = {}".format(sum))

# Part 2
print("Total disk space used = {}".format(files_directories["/"]))

total_disk_size = 70000000
total_needed = 30000000
space_remaining = total_disk_size - files_directories["/"]
dirs_larger_than = total_needed - space_remaining

print ("Dirs to delete larger than  = {}".format(dirs_larger_than))

bigger_dict = {}
for key in files_directories.keys():
  if files_directories[key] > dirs_larger_than:
    bigger_dict[key] = files_directories[key]
    
smallest = 0
for key in bigger_dict.keys():
  if (smallest == 0):
    smallest = bigger_dict[key]

  if (bigger_dict[key] < smallest):
    smallest = bigger_dict[key]

  print("option {} = {}".format(key, bigger_dict[key]))

print("Smallest dir = {}".format(smallest))
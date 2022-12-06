file1 = open('input6.txt', 'r')
Lines = file1.readlines()


debug = True
sum = 0


def get_position_of_first_different(input_line):
  # Variable window size
  #
  window_size = 14

  match = []  
  for x in range(0, len(input_line)):
    if len(match) == window_size:
      match.pop(0)
    
    match.append(input_line[x])

    if len(set(match)) == window_size:
      return x

  return -1
    

for line in Lines:

    print("POSITION = {}".format(get_position_of_first_different(line)))


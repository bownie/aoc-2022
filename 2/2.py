# Using readlines()
file1 = open('input2.txt', 'r')
Lines = file1.readlines()

score = 0


# Strips the newline character
for line in Lines:

    line = line.strip()

    round = line.split(" ")

    # Part 2 - we need to convert the X (lose), Y (draw), Z (win) into
    # A (rock), B (paper), C (scissors)
    #
    if round[0] == "A":
      if round[1] == "X":
        round[1] = "Z"
      elif round[1] == "Y":
        round[1] = "X"
      else:
        round[1] = "Y"  
    elif round[0] == "B":
      if round[1] == "X":
        round[1] = "X"
      elif round[1] == "Y":
        round[1] = "Y"
      else:
        round[1] = "Z"
    else:
      if round[1] == "X":
        round[1] = "Y"
      elif round[1] == "Y":
        round[1] = "Z"
      else:
        round[1] = "X"


    if round[0] == "A":
      print("ROCK")
      
      if round[1] == "X":
        score += 4
      elif round[1] == "Y":
        score += 8
      else:
        score += 3

    elif round[0] == "B":
      print("PAPER")

      if round[1] == "X":
        score += 1
      elif round[1] == "Y":
        score += 5
      else:
        score += 9

    else:
      print("SCISSORS")
      if round[1] == "X":
        score += 7
      elif round[1] == "Y":
        score += 2
      else:
        score += 6

print("Total score {}".format(score))


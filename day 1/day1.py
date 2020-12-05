everything_list = []
with open("input.txt", "r") as a_file:
  for line in a_file:
    current_int = int(line.strip())
    everything_list.append(current_int)

with open("input.txt", "r") as a_file:
  for line in a_file:
    current_int = int(line.strip())
    for number in everything_list:
        #print(number)
        if (current_int + number == 2020):
            print(current_int * number)
    
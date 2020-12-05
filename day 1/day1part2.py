# input_file is an ITERABLE... It's like the interface
# not an ITERATOR

# Keep in mind open is dependent on the directory
value_set = set()

with open("input.txt", "r") as input_file:
  for line in input_file:
    value_set.add(int(line.strip()))

for first_value in value_set:
  for second_value in value_set:
    if ((2020 - (first_value + second_value)) in value_set):
      print(first_value * second_value * (2020 - (first_value + second_value)))
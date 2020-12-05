# So this will have a O(2n) time complexity
# Remember, hashsets have O(1) lookup

# open works by copying file stuff into the bugger
values_set = set()
with open("input.txt", "r") as inputfile:
    for line in inputfile:
        values_set.add(int(line.strip()))
   
for current_int in values_set:
    if ((2020 - current_int) in values_set):
        print((2020 - current_int) * current_int)

# the reason why it's printing 2 times because it's a permutation of 2. We're just finding the same pair, but in different orders
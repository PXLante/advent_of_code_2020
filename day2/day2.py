num_valid_password = 0;

with open('input.txt', 'r') as input_file:
    for line in input_file:
        # first let's see if we can hypothetically do this on one string
        string = line.strip()
        the_string_split = string.split()

        # Let's get the lowest value we need and the highest value we need
        valid_regions = the_string_split[0].split('-')
        minimum_amount_character = int(valid_regions[0])
        maximum_amount_character = int(valid_regions[1])

        # now let's figure out what character we're looking at
        middle_value = the_string_split[1]
        value_looking_for = middle_value[0]

        # now let's figure out 
        num_occurences = 0

        for letter in the_string_split[2]:
            if letter == value_looking_for:
                num_occurences += 1

        if num_occurences >= minimum_amount_character and num_occurences <= maximum_amount_character:
            num_valid_password += 1

print(num_valid_password)


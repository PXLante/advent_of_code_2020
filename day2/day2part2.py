num_valid_password = 0;

with open('input.txt', 'r') as input_file:
    for line in input_file:
        # first let's see if we can hypothetically do this on one string
        string = line.strip()
        the_string_split = string.split()

        # Let's get the lowest value we need and the highest value we need
        valid_regions = the_string_split[0].split('-')
        character_location_1 = int(valid_regions[0]) - 1
        character_location_2 = int(valid_regions[1]) - 1

        # now let's figure out what character we're looking at
        middle_value = the_string_split[1]
        value_looking_for = middle_value[0]

        # now let's check if there's xor of the values being in the right location
        in_location_1 = (value_looking_for == the_string_split[2][character_location_1])
        in_location_2 = (value_looking_for == the_string_split[2][character_location_2])
        if (not(in_location_1 and in_location_2) and (in_location_1 or in_location_2)):
            num_valid_password += 1 

print(num_valid_password)
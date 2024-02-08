import random

# Generate a list of 7 random integers between 0 and 9
random_numbers = [random.randint(0, 9) for _ in range(8)]

# Generate a random number for the middle part (between 13 and 19)
random_numbers1 = random.randint(13, 19)

# Bangladesh country code
bd_code = '+880'

# Concatenate the random numbers into a single string
random_number_str = bd_code + str(random_numbers1) + ''.join(map(str, random_numbers))

print("Random number:", random_number_str)


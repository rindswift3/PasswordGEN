print("Generating Passwords. Hope you have enough space :D ")

# Import the itertools module
import itertools

# Define the characters to use
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"

# Define the maximum length
max_length = 200

# Open a text file for writing
with open("combinations.txt", "w") as f:
    # Loop through the lengths from 1 to max_length
    for length in range(1, max_length + 1):
        # Use itertools.product to generate all combinations of the characters with the given length
        for combo in itertools.product(chars, repeat=length):
            # Join the characters into a string
            string = "".join(combo)
            # Write the string to the file, followed by a newline
            f.write(string + "\n")

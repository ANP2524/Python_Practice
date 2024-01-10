# Define a function named chars_mix_up that takes two arguments, 'a' and 'b'.
def chars_mix_up(a, b):
    # Create a new string 'new_a' by taking the first two characters from 'b' and combining
    # them with the characters from 'a' starting from the third character.
    new_a = b[:2] + a[2:]

    # Create a new string 'new_b' by taking the first two characters from 'a' and combining
    # them with the characters from 'b' starting from the third character.
    new_b = a[:2] + b[2:]

    # Concatenate 'new_a', a space character, and 'new_b' to create a single string.
    return new_a + ' ' + new_b

# Call the chars_mix_up function with the arguments 'abc' and 'xyz' and print the result.
print(chars_mix_up('abc', 'xyz'))  # Output: 'xyc abz' 

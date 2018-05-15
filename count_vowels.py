# This program counts the number of vowels present in a user input

user_inp = input("Enter a word or sentence: ")
lis = list(user_inp)
number_of_vowels = 0
for letters in lis:
    if letters in ['a','e','i','o','u']:
        number_of_vowels += 1

print("Total number of vowels =", number_of_vowels)

# Added bonus - it reports the sum of each vowel present in the input

num_a = 0
num_e = 0
num_i = 0
num_o = 0
num_u = 0

for letters in lis:
    if letters == 'a':
        num_a += 1
    elif letters == 'e':
        num_e += 1
    elif letters == 'i':
        num_i += 1
    elif letters == 'o':
        num_o += 1
    elif letters == 'u':
        num_u += 1

print("How many 'a's?", num_a)
print("How many 'e's?", num_e)
print("How many 'i's?", num_i)
print("How many 'o's?", num_o)
print("How many 'u's?", num_u)

# This program checks a user input and if it is a
# palindrome (reads the same forwards and backwards) then
# it informs the user of such

print("Palindrome - a word that is reads the same forwards and backwards")
print("Enter a word and we'll check if its a palindrome: ")
def palindrome():
    inp = input()
    rev = inp[::-1]
    if rev == inp:
        print("'", inp, "' is a palindrome!")
    else:
        print("'", inp, "' is not a palindrome. Try again!")
        palindrome()
palindrome()

# Here we define a function under the name 'palindrome()' so that the user can try again if the input is not a palindrome.
# Also, note that the syntax used on line 9 is an "extended slice", which allows the user input to be reversed.
# This reversed input is stored under the string named 'rev'.
# The program compares 'rev' to the original ('inp') to see if they are the same.
# If they are identical, then the user input is a palindrome and the program informs the user of such.



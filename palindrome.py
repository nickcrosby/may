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




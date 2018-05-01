# SAMPLE ANSWERS:
# 1. Enter a sentence: The rain in Spain falls mainly in the plain.
#    The letter "a" appears in your sentence 5 times.
# OR
# 2. Enter a sentence: There is nothing here.
#    The letter "a" does not appear in your sentence
# OR
# 3. Enter a sentence: Only happens once here.
#    The letter "a" appears in your sentence 1 time.

string = input("Enter a sentence: ")

number = string.count("a")

if number == 1:
    print("The letter", '"a"', "appears in your sentence 1 time.")
elif number > 1:
    print("The letter", '"a"', "appears in your sentence", number, "times.")
else:
    print("The letter", '"a"', "does not appear in your sentence.")


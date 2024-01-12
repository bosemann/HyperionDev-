# This is a program to demonstrate the replace() and the upper() functions
# This program also demonstrates the reverse function

# saving our sentence as a single string
SENTENCE = "The!quick!brown!fox!jumps!over!the!lazy!dog"

# using the replace() function to remove the !!! marks
CHANGED_SENTENCE = SENTENCE.replace("!", " ")

# printing the changed sentence using the upper function()
print("======This is the changed Sentence in uppercase======")
print(CHANGED_SENTENCE.upper())
print("\n")
# printing the sentence in reverse
print("==========Reversed Sentence=========================")
REVERSE_SENTENCE = CHANGED_SENTENCE.upper()[::-1]
print(REVERSE_SENTENCE)

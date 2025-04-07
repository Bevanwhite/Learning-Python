splitString = "This string has been\nsplit over\nseveral\nlines"  # you need have \n have a line break
print(splitString)

tabbedString = "1\t2\t3\t4\t5"  # \t - have tab space
print(tabbedString)

# different ways of using escape characters
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")

# how to use line break  without using \n
anotherSplitString = """This string has been
split over
several
lines"""

print(anotherSplitString)

# how to remove lines using a backslash
anotherSplitStringOne = """This string has been \
split over \
several \
lines"""

print(anotherSplitStringOne)

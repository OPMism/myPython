#In this exercise, you will need to print an alphabetically sorted list of all functions in the re module, which contain the word find.

import re

# Your code goes here
members = []
for member in dir(re):
    if "find" in member:
        members.append(member)

print sorted(members)

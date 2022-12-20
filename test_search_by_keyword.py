# import the Bible module.
from Bible import Bible

# create an instance of the Bible class.
my_bible = Bible()

# initialize the Bible module.
my_bible.init()

# search for all the verses that contain the word `Jesus`.
found = my_bible.search_by_keyword("Jesus")
for verse in found:
    print(verse)
    print()

# search for something that does not exist in the Bible.
found = my_bible.search_by_keyword("Pohang")
print(found)

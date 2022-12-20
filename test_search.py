# import the Bible module.
from Bible import Bible

# create an instance of the Bible class.
my_bible = Bible()

# initialize the Bible module.
my_bible.init()

# search for Genesis 1:1.
text = my_bible.search("Genesis", 1, 1)
print(text)

# search for 2 Peter 1:10.
text = my_bible.search("2 Peter", 1, 10)
print(text)

# search for Revelation 2:22.
text = my_bible.search("Revelation", 2, 22)
print(text)

# search for something that does not exist in the Bible.
text = my_bible.search("Matthew", 50, 22)
print(text)

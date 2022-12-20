# import the Bible module.
from Bible import Bible

# create an instance of the Bible class.
my_bible = Bible()

# initialize the Bible module.
my_bible.init()

# get the total number of chapters in Genesis.
n = my_bible.get_max_chapter("Genesis")
print(n)

# get the total number of verses in chapter 1 of Genesis.
m = my_bible.get_max_verse("Genesis", 1)
print(m)

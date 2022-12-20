import os


class Bible:
    def __init__(self):

        self.path_data = "."
        # create an empty dictionary that will store the entire Bible
        # key   --> a tuple (book_name, chapter_num, verse_num)
        # value --> text
        self.bible = {}

    def _load_book_names(self):

        # load `bible-3letter.txt` that contains
        # 3-letter abbreviations of the Bible book names (e.g. Gen, Exo, Pe1, ...)
        with open(os.path.join(self.path_data, "bible-3letter.txt"), "rt") as fin:
            self.book_abbr_names = fin.read().splitlines()
            assert len(self.book_abbr_names) == 66

        # load `bible-fullname.txt` that contains
        # the full Bible book names (non-abbreviated; e.g. Genesis, Exodus, 1 Peter, ...)
        with open(os.path.join(self.path_data, "bible-fullname.txt"), "rt") as fin:
            self.book_full_names = fin.read().splitlines()
            assert len(self.book_full_names) == 66

        ### YOUR CODE STARTS HERE

        ### Q1) create a dictionary that translates e.g. `Gen` to `Genesis`.
        ###     this dictionary should be assigned to `self.abbrev2full`.
        ###     this part is almost identical to Assignment 09.
        self.abbrev2full = (dict(zip(self.book_abbr_names, self.book_full_names)))

        ### Q2) create a dictionary that translates e.g. `Genesis` to `Gen`.
        ###     this dictionary should be assigned to `self.full2abbrev`.
        ###     this part is almost identical to Assignment 09.
        self.full2abbrev = (dict(zip(self.book_full_names, self.book_abbr_names)))

        ### YOUR CODE ENDS HERE

        # if your code above is correct,
        # the following four assertions should not throw any exceptions.
        assert len(self.abbrev2full) == 66
        assert len(self.full2abbrev) == 66
        assert type(self.abbrev2full) == dict
        assert type(self.full2abbrev) == dict


    def _load_max_chapter_info(self):
        # load `max_chapter_info.txt` that contains the information about
        # how many chapters there are for each Bible book.
        # (e.g. `Genesis,50` means Genesis has 50 chapters)
        # create a dictionary named `self.max_chapter_info` with this informatino.
        self.max_chapter_info = {}
        with open(os.path.join(self.path_data, "max_chapter_info.txt"), "rt") as fin:
            for line in fin.readlines():
                abbr, max_chapter = line.split(",")
                self.max_chapter_info[abbr] = int(max_chapter)

    def _load_max_verse_info(self):
        # load `max_verse_info.txt` that contains the information about
        # how many verses there are for each chapter in each Bible book.
        # (e.g. `Genesis,1,31` means the first chapter of Genesis has 31 verses)
        # create a dictionary named `self.max_verse_info` with this informatino.
        self.max_verse_info = {}
        with open(os.path.join(self.path_data, "max_verse_info.txt"), "rt") as fin:
            for line in fin.readlines():
                abbr, max_chapter, max_verse = line.split(",")
                if abbr not in self.max_verse_info:
                    self.max_verse_info[abbr] = {}
                self.max_verse_info[abbr][int(max_chapter)] = int(max_verse)

    def _load_bible(self):

        # this for-loop iterates through book names.
        # (e.g. `Gen`, `Exo`, ..., `Jde`, `Rev`)
        for abbr in self.book_abbr_names:

            ### YOUR CODE STARTS HERE

            ### Q3) open and read each book file (e.g. `Gen.txt` for Genesis)
            ###     create a list called `verses`.
            ###     each item in the list should be a single verse.
            ###     make sure you remove ~ and \n, and remove an empty item in the list.
            ###     this part is almost identical to Midterm Exam Q01.
            file = open(abbr+".txt")
            data = file.read()
            verses = data.replace("\n", "")
            verses = verses.split("~")
            verses.pop()

            
            ### YOUR CODE ENDS HERE

            # if your code above is correct,
            # the following four assertions should not throw any exceptions.
            assert type(verses) == list
            assert len(verses) == sum(self.max_verse_info[abbr].values())
            assert all(["~" not in verse for verse in verses])
            assert all(["\n" not in verse for verse in verses])

            # this for-loop iterates through verses.
            # e.g. `Gen|1|1| In the beginning...`,
            #      `Gen|1|2| And the earth...`,
            #       and so forth
            for verse in verses:

                ### YOUR CODE STARTS HERE

                ### Q4) for each verse, create a key-value pair where
                ###     key is a tuple with book name, chapter number, verse number,
                ###     value is the corresponding Bible text.
                ###     e.g. key   --> ("Gen", 1, 1)
                ###          value --> "In the beginning God created the heaven and the earth."
                ###     this part is almost identical to Midterm Exam Q04.
                key = [0,0,0]
                temp = verse.split("|")
                key[0] = temp[0]
                key[1] = int(temp[1])
                key[2] = int(temp[2])
                value = temp[3].strip()
                key = tuple(key)
                self.bible.update({key : value})


                ### YOUR CODE ENDS HERE

                # if your code above is correct,
                # the following seven assertions should not throw any exceptions.
                assert type(key) == tuple
                assert len(key) == 3
                assert len(key[0]) == 3
                assert type(key[1]) == int
                assert type(key[2]) == int
                assert type(value) == str
                assert value[0] != " "


                # add a key-value pair to the `self.bible` dictionary
                self.bible[key] = value

        # if your code above is correct,
        # the following assertion should not throw any exceptions.
        # FYI, the total number of verses in the Bible is 31102.
        assert len(self.bible) == 31102


    def init(self):
        # initialize and load necessary data
        self._load_book_names()
        self._load_max_chapter_info()
        self._load_max_verse_info()
        self._load_bible()


    def pretty_format(self, book_full_name, chapter_num, verse_num, text):
        # this will create a string that looks like below:
        # e.g.
        # In the beginning God created the heaven and the earth.
        # (Genesis 1:1)
        output = text
        output += "\n"
        output += f"({book_full_name} {chapter_num}:{verse_num})"
        return output


    def search(self, book_full_name, chapter_num, verse_num):

        ### YOUR CODE STARTS HERE

        ### Q5) given a book name, chapter number, and verse number,
        ###     find the text by using the pre-built dictionary `self.bible`.
        ###     if not found, make sure to return `None`.
        ###     this part is almost identical to Midterm Exam Q04.
        if book_full_name in self.book_full_names:
            book_abbr = self.book_abbr_names[self.book_full_names.index(book_full_name)]
        text = self.bible.get((book_abbr, chapter_num, verse_num))
        if text is None:
            return None
        



        ### YOUR CODE ENDS HERE


        # if your code above is correct,
        # the following four assertions should not throw any exceptions.
        assert book_full_name in self.book_full_names
        assert type(chapter_num) == int
        assert type(verse_num) == int
        assert type(text) == str

        # beautify
        output = self.pretty_format(book_full_name, chapter_num, verse_num, text)

        # return the found text
        return output

    def search_by_keyword(self, keyword):

        found = []

        ### YOUR CODE STARTS HERE

        ### Q6) search through the entire Bible,
        ###     find all the verses that includes a givn keyword.
        ###     if not found, return an emtpy list.
        for key, value in self.bible.items():
            if keyword in value:
                found.append(self.pretty_format(key[0], key[1], key[2], value))
        if found == []:
            return []



        ### YOUR CODE ENDS HERE

        return found

    def get_max_chapter(self, book_full_name):
        book_abbr_name = self.full2abbrev[book_full_name]
        # return how many chapters there are for a given book.
        return self.max_chapter_info[book_abbr_name]

    def get_max_verse(self, book_full_name, chapter_num):
        book_abbr_name = self.full2abbrev[book_full_name]
        # return how many verses there are for a given chapter in a given book.
        return self.max_verse_info[book_abbr_name][chapter_num]

from tkinter import *
from Bible import Bible

my_bible = Bible()

my_bible.init()

#functions similar to Bible app
def search():
    global text_box
    book_selected = book.get()
    chapter_selected = chapter.get()
    verse_selected = verse.get()
    text = my_bible.search(book_selected, int(chapter_selected), int(verse_selected))
    text_box.delete(1.0, END)
    text_box.insert(END, text)

def search_by_keyword():
    global text_box
    keyword = keyword_entry.get()
    found = my_bible.search_by_keyword(keyword)
    text_box.delete(1.0, END)
    for verse in found:
        text_box.insert(END, verse)
        text_box.insert(END, "\n")

def get_max_chapter():
    global text_box
    book_selected = book.get()
    #if user input a chapter (if it is not empty)
    if chapter.get() != "":
        chapter_selected = chapter.get()
        n = str(my_bible.get_max_verse(book_selected, int(chapter_selected))) + " is the max verse number in the chapter."
    #else if user did not input a chapter (if it is empty)
    elif chapter.get() == "":
        n = str(my_bible.get_max_chapter(book_selected)) + " is the max chapter number."
    text_box.delete(1.0, END)
    text_box.insert(END, n)

def clear():
    global text_box
    text_box.delete(1.0, END)
    book_entry.delete(0, END)
    chapter_entry.delete(0, END)
    verse_entry.delete(0, END)
    keyword_entry.delete(0, END)

#main window
root = Tk()
root.title("Bible App")
root.geometry("500x500")

#create textboxes and labels to get the user input
book = StringVar()
book_label = Label(root, text="Book:")
book_label.grid(row=0, column=0)
book_entry = Entry(root, textvariable=book)
book_entry.grid(row=0, column=1)
chapter = StringVar()
chapter_label = Label(root, text="Chapter:")
chapter_label.grid(row=1, column=0)
chapter_entry = Entry(root, textvariable=chapter)
chapter_entry.grid(row=1, column=1)
verse = StringVar()
verse_label = Label(root, text="Verse:")
verse_label.grid(row=2, column=0)
verse_entry = Entry(root, textvariable=verse)
verse_entry.grid(row=2, column=1)
keyword_entry = StringVar()
keyword_label = Label(root, text="Keyword:")
keyword_label.grid(row=3, column=0)
keyword_entry = Entry(root, textvariable=keyword_entry)
keyword_entry.grid(row=3, column=1)

#create buttons to search, search by keyword,get max chapter/verse, and clear all text and entries
search_button = Button(root, text="Search", command=search)
search_button.grid(row=4, column=0, columnspan=2)
search_by_keyword_button = Button(root, text="Search by Keyword", command=search_by_keyword)
search_by_keyword_button.grid(row=5, column=0, columnspan=2)
get_max_chapter_button = Button(root, text="Get Max Chapter/Verse", command=get_max_chapter)
get_max_chapter_button.grid(row=6, column=0, columnspan=2)
clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=7, column=0, columnspan=2)

#craete text box to display the result
#the Textbox width and height is automatically adjusted to the size of the text
text_box = Text(root, width=50, height=50)
text_box.grid(row=8, column=0, columnspan=2)

#end of main window
root.mainloop()
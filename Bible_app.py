# import Streamlit.
import streamlit as st

# import the Bible module.
from Bible import Bible


# create an instance of the Bible class.
my_bible = Bible()

# initialize the Bible module.
my_bible.init()

# implement a Bible search app using Streamlit.
st.title("Handong Bible App")
st.write("Yehezkiel Alexander 22100828")

book_selected = st.selectbox("Book:", options = book_full_names)

chapter_selected = st.slider("Chapter:", min_value=1, max_value=my_bible.get_max_chapter(book_selected), step=1)

verse_selected = st.slider("Verse:", min_value=1, max_value = my_bible.get_max_verse(book_selected, chapter_selected), step=1)

st.info(my_bible.search(book_selected, chapter_selected, verse_selected))

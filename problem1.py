import streamlit as st

def file_uploader():
    uploaded_file = st.file_uploader("Upload a text file", type="txt")
    if uploaded_file is not None:
        file_contents = uploaded_file.read().decode("utf-8")
        return file_contents

def display_content(file_contents):
    st.header("File Contents")
    st.text_area("Text", file_contents, height=500)

def count_words(file_contents):
    word_count = {}
    for word in file_contents.split():
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count

def display_word_count(word_count):
    st.header("Word Count")
    for word, count in word_count.items():
        st.write(f"{word}: {count}")

def top_five_words(word_count):
    top_five = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:5]
    return top_five

def display_top_five(top_five):
    st.header("Top 5 Words")
    for word, count in top_five:
        st.write(f"{word}: {count}")

def search_word(top_five, file_contents):
    selected_word = st.selectbox("Select a word from the top 5 list", [word for word, _ in top_five])
    st.header(f"Sentences containing {selected_word}")
    for sentence in file_contents.split("."):
        if selected_word in sentence:
            st.write(sentence.strip())

def main():
    st.title("Text Analysis App")
    file_contents = file_uploader()
    display_all = False
    if file_contents is not None:
        if st.button('File Contents'):
            display_all = True
        if display_all:
            display_content(file_contents)
            word_count = count_words(file_contents)
            display_word_count(word_count)
            top_five = top_five_words(word_count)
            display_top_five(top_five)
            search_word(top_five, file_contents)

if __name__ == "__main__":
    main()



 
       

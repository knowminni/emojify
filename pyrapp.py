import emoji
import streamlit as st

est = [':lemon:', ':crown:', ':pizza:', ':kissing_cat:', ':hamburger:',
 ':sparkles:', ':fire:', ':crescent_moon:']
emolst = [emoji.emojize(i) for i in est]


st.title('Emoji Text Editor')
st.header('Write a Text > Choose your Emoji > Hit on the Button')
st.subheader('Fact: I got annoyed of all the spamming but somebody shot this idea.')


text = st.text_input('Writeth thy W\'rd: ', max_chars = 10)
choice = st.select_slider(label='Chooseth thy Emoji', options = emolst)

print(choice)









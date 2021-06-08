import emoji
import streamlit as st
from alphafy import *

est = [':lemon:', ':crown:', ':pizza:', ':kissing_cat:', ':hamburger:',
 ':sparkles:', ':fire:', ':crescent_moon:']
emolst = [emoji.emojize(i) for i in est]


def evaluate(text, ch):
      for i in text:
            st.write(eval(i + '(ch)'))
      

st.title('Emoji Text Editor')
st.header('Write a Text > Choose your Emoji > Hit on the Button')
st.subheader('Fact: I got annoyed of all the spamming but somebody shot this idea.')


tmp = st.text_input('Writeth thy W\'rd: ', max_chars = 10)
text = tmp.replace(' ', '').upper()
choice = st.selectbox(label='Chooseth thy Emoji', options = emolst)

if st.button('Letss Goooo to the Mooon '+emoji.emojize(':sunglasses:')):
      evaluate(text, choice)









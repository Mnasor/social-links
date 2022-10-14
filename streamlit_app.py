import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('al Yousef')

st.info('this is my first link ')

icon_size = 20

st_button('youtube', 'https://youtube.com/channel/UCDXLeBjO7av7mcJ25uAE3ew',
          'قناة اليوتيوب', icon_size)

st_button('medium', 'https://www.snapchat.com/add/f-alshehili?share_id=MEI2MzgxNEMtRDM2NC00NzQ4LTg5NkMtRUQ3QkY2NUM5Nzc4&locale=ar_SA@calendar=gregorian',
          'ٍSnapchat', icon_size)
st_button('twitter', 'https://twitter.com/thedataprof/',
          'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/chanin-nantasenamat/',
          'Follow me on LinkedIn', icon_size)
st_button('newsletter', 'https://sendfox.com/dataprofessor/',
          'Sign up for my Newsletter', icon_size)
st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/',
          'Buy me a Coffee', icon_size)

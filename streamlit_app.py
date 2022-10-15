import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

# st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('channels4_profile.jpg'))

st.header('al Yousef')

st.info('نقدم محتوى على شكل فلوقات او فعاليات ')

icon_size = 20

st_button('youtube', 'https://youtube.com/channel/UCDXLeBjO7av7mcJ25uAE3ew',
          'قناة اليوتيوب', icon_size)

st_button('snapchat', 'https://www.snapchat.com/add/f-alshehili?share_id=MEI2MzgxNEMtRDM2NC00NzQ4LTg5NkMtRUQ3QkY2NUM5Nzc4&locale=ar_SA@calendar=gregorian',
          'سناب تشات', icon_size)

st_button('tiktok', 'https://www.tiktok.com/@fahad_childern?_t=8WQJi2SuYwk&_r=1',
          'تيك توك', icon_size)

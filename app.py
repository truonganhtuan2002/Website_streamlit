import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup

# Tiêu đề của ứng dụng
st.title('Ứng Dụng Web Đơn Giản')

# Hiển thị ảnh
st.header('Hiển thị Ảnh Từ URL')
url = st.text_input('Nhập URL của ảnh:', '')
if url:
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    st.image(img, caption='Ảnh từ URL', use_column_width=True)

# Tìm kiếm trên Wikipedia
st.header('Tìm Kiếm trên Wikipedia')
search_query = st.text_input('Nhập từ khóa tìm kiếm:', '')
if search_query:
    search_url = f'https://en.wikipedia.org/wiki/{search_query}'
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    summary = soup.find('div', {'class': 'mw-parser-output'}).p.text
    st.write(summary)
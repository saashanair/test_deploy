import streamlit as st

st.title('Hello world')

upload_file = st.file_uploader("Choose a file")
if upload_file is None:
    st.error('No file found!')
else:
    st.success('File uploaded: ', upload_file.name)

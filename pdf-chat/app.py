import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

from PyPDF2 import PdfReader

with st.sidebar:
  st.title( 'PDF Chat' )
  st.markdown(
    '''
      ## About
      This app is an LLM-powered chatbot built using:
      - [Streamlit](https://streamlit.io/)
      - [LangChain](https://python.langchain.com/)
      - [OpenAI](https://platform.openai.com/docs/models) LLM model
    '''
  )
  add_vertical_space(5)
  st.write( 'Made by recursive-reshy' )

def main():
  st.header( 'Chat with PDF' )
  
  pdf = st.file_uploader( 
    'Upload a PDF file', 
    type='pdf' 
  )

  if pdf is not None:
    pdf_reader = PdfReader( pdf )
    st.write( pdf_reader )

if __name__ == '__main__':
  main()
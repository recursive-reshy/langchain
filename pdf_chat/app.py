from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback

import os
import pickle

from dotenv import load_dotenv

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
  
  load_dotenv()

  pdf = st.file_uploader( 
    'Upload a PDF file', 
    type='pdf' 
  )

  if pdf is not None:
    pdf_reader = PdfReader( pdf )

    text = ''
    for page in pdf_reader.pages:
      text += page.extract_text()
    
    text_splitter = RecursiveCharacterTextSplitter( 
      chunk_size=1000,
      chunk_overlap=200,
      length_function=len
    )

    chunks = text_splitter.split_text( text = text )

    store_name = pdf.name[ : -4 ]

    if os.path.exists( f'{store_name}.pkl' ):
      with open( f'{store_name}.pkl', 'rb' ) as f:
        vector_store = pickle.load( f )
    
    else:
      embedding = OpenAIEmbeddings()
      vector_store = FAISS.from_texts(
        chunks,
        embedding = embedding
      )

      with open( f'{store_name}.pkl', 'wb' ) as f:
        pickle.dump( vector_store, f )

    query = st.text_input( 'Ask a question about the PDF' )

    if query:
      docs = vector_store.similarity_search( query = query )
      
      llm = OpenAI(
        temperature = 0,
        model_name = 'gpt-3.5-turbo'
      )

      chain = load_qa_chain(
        llm = llm,
        chain_type='stuff'
      )

      with get_openai_callback() as cb:
        response = chain.run(
          input_documents = docs,
          question = query
        )
        print( cb )

      st.write( response )

if __name__ == '__main__':
  main()
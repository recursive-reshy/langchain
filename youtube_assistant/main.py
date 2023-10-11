import streamlit as st
import textwrap

import langchain_helper as lch

st.title("Youtube Assistant")

with st.sidebar:
  with st.form( key='my_form' ):
    youtube_url = st.sidebar.text_area(
      label = 'Youtube URL',
      max_chars = 100 
    )

    query = st.sidebar.text_area(
      label = 'Ask me about the video?',
      max_chars = 50,
      key = 'query'
    )

    submit_button = st.form_submit_button( label = 'Submit' )

if query and youtube_url:

  response, docs = lch.get_response_from_query( 
    lch.create_vector_db_from_youtube_url( youtube_url ), 
    query 
  )

  st.subheader('Answer')
  st.text( textwrap.fill( response, width = 80 ) )
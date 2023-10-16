from langchain.llms import OpenAI
from langchain.agents import create_csv_agent

from dotenv import load_dotenv

import streamlit as st

def main():

  load_dotenv()

  st.set_page_config( page_title = 'CSV Chat', page_icon = ':speech_balloon:' )
  st.header( 'CSV Chat' )

  user_csv = st.file_uploader( 'Upload CSV', type = 'csv' )

  if user_csv is not None:
    user_question = st.text_input( 'Question' )

    agent = create_csv_agent( 
      OpenAI( temperature = 0 ), # LLM
      user_csv,
      verbose = True 
    )

    if user_question is not None and user_question != '':
      st.write( agent.run( user_question ) )


if __name__ == "__main__":
  main()
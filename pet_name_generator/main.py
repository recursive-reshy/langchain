import streamlit as st

import langchain_helper as lch

st.title('Pet Name Generator')

animal_type = st.sidebar.selectbox( 
  'What is your pet?', 
  ( 'Dog', 'Cat', 'Bird', 'Fish', 'Other' ) 
)

pet_color = st.sidebar.text_area( 
  'What color is your pet?', 
  max_chars=15 
)

if pet_color:
  response = lch.generate_pet_name( animal_type, pet_color )
  st.text( response['pet_name'] )
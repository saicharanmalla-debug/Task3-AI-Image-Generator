
import streamlit as st
from s import styles
from PIL import Image
from io import BytesIO
from imageapi import gen_img



if "history" not in st.session_state:
    st.session_state.history=[]

st.title("AI Image Generator (Task 3)")

p= st.text_input("Enter prompt")
 

s= st.radio("Choose your style",["Anime",
             "Cyberpunk","Realistic"])

if st.button("Generate"):

     final= p+styles[s]
         
     response= gen_img(final)
     st.session_state.history.append(final)
     st.write("Status Code:", response.status_code)
     image= Image.open(BytesIO(response.content))
     st.image(image,caption=final)
    
     st.write("Prompt: ",final)
    
    
st.subheader("Prompt HIstory")
for item in st.session_state.history:
    st.write(item)
    
    
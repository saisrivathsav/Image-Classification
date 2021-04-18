import streamlit as st
import joblib
model =joblib.load('Email_Class')

add_selectbox = st.sidebar.radio("Our page",['Home',"Rate us"])
if(add_selectbox == 'Home'):
  st.title("Review classifier")
  st.image('https://static.businessworld.in/article/article_extra_large_image/1600858456_HulSrV_Flipkart.jpg')

  ip = st.text_input('Enter your review')
  p = model.predict([ip])
  if st.button('Predict'):
    st.header(op[0])
    if(op[0]=='Good'):
      st.markdown(""":smile:""")
    else:
      st.markdown(""":angry:""")
else:
  st.title("Rate US")
  st.slider("Rating",0,5)
  if st.button("Submit"):
    st.header("Thanks for the rating")

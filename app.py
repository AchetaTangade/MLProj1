import streamlit as st
import joblib
model = joblib.load('spam-ham')  # write same file name......here we r loading data from model using joblib
st.title('SPAM HAM CLASSIFIER')
ip = st.text_input('Enter the message')
op = model.predict([ip])
if st.button('Predict'):       #it creates button called predict and performs following on clicking it
  #st.write("Entered message is ")
  #st.write(op[0])
  st.title(op[0])

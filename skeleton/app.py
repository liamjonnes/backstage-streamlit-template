import streamlit as st
import json as json
from urllib.request import urlopen
import requests

st.title("This is a title!")
st.write("This is a test!")

def run():
  url = "http://localhost:5000"

  run = requests.get(url)
  
  output = run.json()

  return output

results = run()

st.write(results)
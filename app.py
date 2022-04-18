import streamlit as st
from RegexGenerator import RegexGenerator
import re
st.sidebar.image("logo2.png")
st.sidebar.title("RegEx GenEx")
selection = st.sidebar.radio("Go to", ['Generator','Extractor'])
try:
    
    if selection =="Generator":
        str1 = st.text_input("Enter string to be recognised")
        myGen = RegexGenerator(str1)
        res = myGen.get_regex()
        st.markdown("<h5>Result is: " + res + "</h5>",unsafe_allow_html=True)
    if selection =="Extractor":
        text = st.text_area("Enter text: ")
        pattern = st.text_area("Enter pattern to be found: ")
        matches = re.findall(pattern, text)
        if pattern:
            st.markdown("<h5>Result is: </h5>",unsafe_allow_html=True)
            for res in matches:
                st.markdown("<h5>" + res + "</h5>",unsafe_allow_html=True)
except:
    st.write(" ")
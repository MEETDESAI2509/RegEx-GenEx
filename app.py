import streamlit as st
from RegexGenerator import RegexGenerator
import re
st.sidebar.title("RegEx GenEx")

selection = st.sidebar.radio("Go to", ['Home','Generator','Extractor'])
try:
    if selection == "Home":
        
        st.title("RegEx GenEx")
        st.markdown("<p align='justify' style='font-size:20px;font-family:arial;'>This is a Regex tool which can be used for two things: <br> 1.Generator: You can give a string as input and it will generate a regex pattern. <br> 2.Extractor: It will extract matches in a given text paragraph by matching with a given pattern.</p>",unsafe_allow_html=True)
        st.markdown("<h3>Developed by </h3>",unsafe_allow_html=True)
        col1, col2 = st.columns([1, 1])
        col1.markdown("<h4>Meet Desai</h4>",unsafe_allow_html=True)
        col2.markdown("<h4>Nishnata Debnath</h4>",unsafe_allow_html=True)

    if selection =="Generator":
        st.write("EXample: 8021236669")
        str1 = st.text_input("Enter string to be recognised")
        myGen = RegexGenerator(str1)
        res = myGen.get_regex()
        st.markdown("<h5>Result is: " + res + "</h5>",unsafe_allow_html=True)
    if selection =="Extractor":
        st.write("Example: Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion Tesla's CFO number (999)-333-7777")
        text = st.text_area("Enter text: ")
        st.write("Example: \(\d{3}\)-\d{3}-\d{4}|\d{10} ")
        pattern = st.text_area("Enter pattern to be found: ")
        matches = re.findall(pattern, text)
        if pattern:
            st.markdown("<h5>Result is: </h5>",unsafe_allow_html=True)
            for res in matches:
                st.markdown("<h5>" + res + "</h5>",unsafe_allow_html=True)
except:
    st.write(" ")

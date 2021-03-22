import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
username=st.text_input("username")
upload=st.file_uploader("upload file",type=['csv'])
button=st.button("submit")
if button==True:
    st.write("output-1")
    df=pd.read_csv(upload)
    st.write(df.head())
    st.write("output-2")
    fig = plt.figure()
    vam = fig.add_subplot(1,1,1)
    vam.scatter(df["petal.length"],df["sepal.length"])
    vam.set_xlabel("petal.length")
    vam.set_ylabel("sepal.length")
    st.write(fig)

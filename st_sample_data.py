import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

st.title("Sample Dashboard")

uploaded_file = st.file_uploader("Choose csv. file", type = "csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filtered Date")
    columns = df.columns.to_list()
    selected_column = st.selectbox("Select Column to filter by:", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("select Value:", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select X-column:", columns)
    y_column = st.selectbox("Select Y-column:", columns)
    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
    else:
        st.write("Waiting on file upload")
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mp
def app():
  """ Exploratory Data Analysis App """

  # File upload section
  uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

  if uploaded_file is not None:
    # Read the uploaded file
    if uploaded_file.name.endswith(".xlsx"):
      df = pd.read_excel(uploaded_file)
    else:
      df = pd.read_csv(uploaded_file)

    # Data overview section
    st.write("### Data Overview")
    st.write(df.head())  # Show the first few rows
    st.write(f"Data Shape: {df.shape}")  # Show dimensions

    # Data description section
    st.write("### Data Description")
    st.write(df.describe(include='all'))  # Summary statistics

    # Explore data by column section
    selected_column = st.selectbox("Select a column", df.columns)
    st.write(f"Selected column: {selected_column}")

    # Analyze data based on column type
    if pd.api.types.is_numeric_dtype(df[selected_column]):
      # Numerical column
      st.write("### Numerical Data Analysis")
      st.hist(df[selected_column])  # Distribution plot
      st.boxplot(df[selected_column])  # Box plot
    else:
      # Categorical column
      st.write("### Categorical Data Analysis")
      st.subheader("Value Counts")
      st.write(df[selected_column].value_counts())  # Count of each value

if __name__ == "__main__":
  app()

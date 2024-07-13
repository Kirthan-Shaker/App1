import seaborn as sns
import matplotlib as mp
import streamlit as st
import pandas as pd
import numpy as np

def app():
  """ Exploratory Data Analysis App """

  # Define app title, description, and "About Us" content
  st.set_page_config(
      page_title="Exploratory Data Analysis (EDA) App",
      page_icon="",  # Optional icon (displayed on browser tab)
      layout="wide"  # Adjust layout for wider content area
  )

  # About Us section (displayed on top left)
  about_us_text = """
      ****Welcome to the EDA App****

      This Exploratory Data Analysis (EDA) app is a tool designed to help you gain insights from your CSV or Excel data. 

      Developed by Kirthan Iyanagar, this app provides a user-friendly interface to explore your data through various functionalities.
  """
  st.sidebar.markdown(about_us_text, unsafe_allow_html=True)

  # App description text (displayed below About Us)
  app_description = """
      **Exploratory Data Analysis (EDA)** is a crucial step in data science that involves understanding the structure, characteristics, and relationships within your data. It helps identify patterns, trends, and potential issues before diving into model building.

      **Use cases:**

      - Feature engineering
      - Hypothesis generation
      - Data cleaning and pre-processing
      - Model selection

      **How to use this app:**

      1. Upload your CSV or Excel file.
      2. Explore the data overview and description.
      3. Select a column to analyze its distribution or value counts.
      4. Use the displayed visualizations to gain insights into your data.
  """
  st.sidebar.markdown(app_description, unsafe_allow_html=True)

  # App heading with large font size
  st.markdown("<h1 style='text-align: center; font-size: 40px;'>Exploratory Data Analysis</h1>", unsafe_allow_html=True)

  # File upload section (centered below heading)
  uploaded_file = st.container().file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

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

    # Content table for analysis capabilities (displayed in sidebar)
    analysis_table = """
    | Analysis | Description |
    |---|---|
    | Data Overview | View the first few rows and data shape. |
    | Data Description | Get summary statistics of the data. |
    | Distribution Analysis (Numerical) | Visualize the distribution of numerical data using histograms. |
    | Outlier Detection (Numerical) | Identify potential outliers using boxplots. |
    | Value Counts (Categorical) | Explore the frequency of each category in categorical data. |
    """
    st.sidebar.markdown(analysis_table, unsafe_allow_html=True)

  # Add signature in sidebar
  st.sidebar.markdown("Developed by Kirthan Iyanagar", unsafe_allow_html=True)

if __name__ == "__main__":
  app()

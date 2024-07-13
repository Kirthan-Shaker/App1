import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np

def app():
    """ Exploratory Data Analysis App """

    # Set app title, description, and layout
    st.set_page_config(
        page_title="Exploratory Data Analysis (EDA) App",
        page_icon="🔍",
        layout="wide"  # Adjust layout for wider content area
    )

    # About Us section (displayed on the sidebar)
    st.sidebar.title("Welcome to the EDA App")
    about_us_text = """
    This Exploratory Data Analysis (EDA) app is a tool designed to help you gain insights from your CSV or Excel data.

    Developed by **Kirthan Iyanagar**, this app provides a user-friendly interface to explore your data through various functionalities.
    """
    st.sidebar.info(about_us_text)

    # App description section (displayed on the sidebar)
    st.sidebar.title("App Description")
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
    st.sidebar.info(app_description)

    # App heading with large font size and centered alignment
    st.markdown("<h1 style='text-align: center; font-size: 40px;'>Exploratory Data Analysis</h1>", unsafe_allow_html=True)

    # File upload section (centered below heading)
    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"], help="Upload your data file here")

    if uploaded_file is not None:
        # Read the uploaded file
        if uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)
        else:
            df = pd.read_csv(uploaded_file)

        # Data overview section
        st.write("### Data Overview")
        st.dataframe(df.head())  # Show the first few rows with an enhanced display
        st.write(f"**Data Shape:** {df.shape}")  # Show dimensions

        # Data description section
        st.write("### Data Description")
        st.dataframe(df.describe(include='all'))  # Summary statistics

        # Explore data by column section
        st.write("### Column Analysis")
        selected_column

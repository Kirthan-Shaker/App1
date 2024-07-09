import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load data
@st.cache_data
def load_data(file):
    if file.name.endswith('.csv'):
        return pd.read_csv(file)
    else:
        return pd.read_excel(file)

# App title and description
st.title("Exploratory Data Analysis (EDA) App")
st.markdown("""
This app performs Exploratory Data Analysis (EDA) on your uploaded dataset. EDA is an approach to analyze datasets to summarize their main characteristics, often using statistical graphics and other data visualization methods.
""")
st.markdown("---")

# Upload file section
st.sidebar.title("App by Kirthan Iyanagar")
uploaded_file = st.file_uploader("Upload your Excel or CSV file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Load data
    data = load_data(uploaded_file)

    # Display basic info
    st.header("Dataset Overview")
    st.write(data.head())
    
    # Display summary statistics
    st.subheader("Summary Statistics")
    st.write(data.describe())

    # Display data types
    st.subheader("Data Types")
    st.write(data.dtypes)

    # Check for missing values
    st.subheader("Missing Values")
    st.write(data.isnull().sum())

    # Drop rows with missing values for correlation calculation
    data.dropna(inplace=True)

    # Correlation heatmap
    st.subheader("Correlation Heatmap")
    corr = data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
    st.pyplot(plt)
    
    # Feature selection for plotting
    st.subheader("Feature Selection for Plotting")
    all_columns = data.columns.tolist()
    selected_columns = st.multiselect("Select columns for plotting", all_columns)

    if selected_columns:
        # Pairplot
        st.subheader("Pairplot")
        sns.pairplot(data[selected_columns])
        st.pyplot(plt)

        # Boxplot
        st.subheader("Boxplot")
        selected_boxplot_column = st.selectbox("Select column for boxplot", selected_columns)
        sns.boxplot(y=data[selected_boxplot_column])
        st.pyplot(plt)

# Content table for analysis capabilities
st.sidebar.markdown("### Analysis Capabilities")
st.sidebar.markdown("""
- **Dataset Overview**: Displaying the first few rows of the dataset.
- **Summary Statistics**: Providing descriptive statistics like mean, median, min, max, etc.
- **Data Types**: Showing the data types of columns in the dataset.
- **Missing Values**: Checking and displaying the count of missing values.
- **Correlation Heatmap**: Visualizing correlations between numeric columns.
- **Pairplot**: Scatter plots for pairwise relationships between selected columns.
- **Boxplot**: Visualizing the distribution of selected columns using boxplots.
""")

    st.write("Please upload an Excel or CSV file to start the analysis.")

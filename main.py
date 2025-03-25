import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader('Choose a csv file', type='csv')

if uploaded_file is not None:
    st.write('File uploaded...')
    df = pd.read_csv(uploaded_file)

    st.subheader('Data Preview')
    st.write(df.head())

    st.subheader('Data Summary')
    st.write(df.describe())

    st.subheader('Filter Data')
    columns = df.columns.tolist()
    selected_columns = st.selectbox('Select column to filter by:', columns)
    unique_values = df[selected_columns].unique()
    selected_value = st.selectbox('Select Value', unique_values)

    filtered_df = df[df[selected_columns] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox('Select x-axis column', columns)
    y_column = st.selectbox('Select y-axis column', columns)

    if st.button('Generate plot'):
        try:
            # Check if columns exist in filtered data
            if x_column in filtered_df.columns and y_column in filtered_df.columns:
                # Ensure we're using the unfiltered data for plotting
                plot_df = df.set_index(x_column)[[y_column]]
                st.line_chart(plot_df)
            else:
                st.warning("Selected columns not available in filtered data. Showing full dataset.")
                plot_df = df.set_index(x_column)[[y_column]]
                st.line_chart(plot_df)
        except KeyError as e:
            st.error(f"Error creating plot: {str(e)}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")
else:
    st.write('Waiting on file Upload...')
import streamlit as st
import pandas as pd

# Function to split patient name into first and last name
def split_name(name):
    try:
        last_name, first_name = name.split(', ')
        return first_name, last_name
    except Exception as e:
        return "", ""

# Function to transform the data
def transform_data(df):
    df['Patient Phone'] = df['Patient Phone'].apply(lambda x: str(int(x)) if not pd.isna(x) else '')
    df['Phone Type'] = df['Phone Type'].astype(str)  # Ensure 'Phone Type' is treated as string
    
    df_transformed = pd.DataFrame()
    df_transformed['First Name'] = df['Patient Name'].apply(lambda x: split_name(x)[0])
    df_transformed['Last Name'] = df['Patient Name'].apply(lambda x: split_name(x)[1])
    df_transformed['Appointment Date'] = df['Service Date']
    df_transformed['Appointment Time'] = df['Time']
    df_transformed['Location'] = df['Location']
    df_transformed['Patient Phone'] = df['Patient Phone']
    df_transformed['Type'] = df['Phone Type'].apply(lambda x: 'sms' if x.lower() == 'cell' else 'voice')

    df_sms = df_transformed[df_transformed['Type'] == 'sms']
    df_voice = df_sms.copy()
    df_voice['Type'] = 'voice'

    df_final = pd.concat([df_transformed, df_voice], ignore_index=True)
    
    return df_final

st.title("CSV Transformer App")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Original Data")
    st.write(df)

    df_transformed = transform_data(df)
    st.write("Transformed Data")
    st.write(df_transformed)

    @st.cache
    def convert_df_to_csv(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df_to_csv(df_transformed)

    st.download_button(
        label="Download Transformed CSV",
        data=csv,
        file_name='transformed_appointments.csv',
        mime='text/csv',
    )

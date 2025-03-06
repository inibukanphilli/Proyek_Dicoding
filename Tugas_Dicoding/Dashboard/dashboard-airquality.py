import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

sns.set(style='dark')

airdongsi_df = pd.read_csv('clean.csv')

# Sidebar
with st.sidebar:
    col1, col2, col3 = st.columns([0.3, 3, 0.3])
    with col2:
        st.title('Kualitas Udara di Kota Dongsi')
    col1, col2, col3 = st.columns([0.5, 4, 0.5])
    with col2:
        st.image("https://i.scdn.co/image/ab67616d0000b273cca61371619a0b695fabde92", width=300)
    
    year = st.selectbox(
        label="Tahun: ",
        options=[2013, 2014, 2015, 2016, 2017]
    )
    
    show_heatmap = st.checkbox("Tampilkan Heatmap Korelasi")
   

# Header utama
st.title("Analisis Kualitas Udara di Kota Dongsi")
st.markdown("---")

# Ringkasan Statistik

# Visualisasi berdasarkan tahun
st.header(f'Visualisasi Kualitas Udara - Tahun {year}')
st.caption('Pertanyaan Bisnis 1 : Bagaimana Konsentrasi zat pencemar di kota Dongsi pada 5 tahun terakhir?')

# Agregasi data berdasarkan tahun dan bulan
visual = airdongsi_df.groupby(by=["year", "month"]).agg({
    "PM2.5": "mean",
    "PM10": "mean",
    "SO2": "mean",
    "NO2": "mean",
    "CO": "mean",
    "O3": "mean",
})

data_selected = visual.loc[year]

variables = ["PM2.5", "PM10", "SO2", "CO", "NO2", "O3"]
fig, axes = plt.subplots(3, 2, figsize=(15, 12))
axes = axes.flatten()

for i, var in enumerate(variables):
    axes[i].plot(data_selected.index, data_selected[var], marker='o', color='red')
    axes[i].set_title(f'Rata-Rata {var} pada Tahun {year}')
    axes[i].set_xlabel('Month')
    axes[i].set_ylabel(f'{var} mean')

plt.tight_layout()
st.pyplot(fig)
st.markdown("---")

# Visualisasi Heatmap Korelasi
if show_heatmap:
    st.header('Heatmap Korelasi antar Zat Pencemar')
    st.caption('Pertanyaan Bisnis 2 : Apakah di antara zat pencemar ada hubungan korelasi?')
    corr_matrix = airdongsi_df[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].corr()
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", mask=mask, linewidths=0.5, ax=ax)
    plt.title('Heatmap Korelasi antar Zat Pencemar')
    st.pyplot(fig)
    st.markdown("---")
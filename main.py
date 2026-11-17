import streamlit as st

from penjualan import tampilkan_penjualan
from pokemon import tampilkan_pokemon

st.set_page_config(page_title="Strukdat 8 - Visualisasi Data", layout="wide")

halaman = st.sidebar.radio(
    "Pilih Soal",
    ["Soal 1 - Data Penjualan", "Soal 2 - Data Pokémon"],
)

if halaman == "Soal 1 - Data Penjualan":
    tampilkan_penjualan()
else:
    tampilkan_pokemon()

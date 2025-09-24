import streamlit as st
import pandas as pd
import json
from pathlib import Path

# Load dictionary (from JSON we created earlier)
DICT_PATH = Path(__file__).resolve().parents[1] / "data" / "mro_dictionary.json"

st.set_page_config(page_title="MRO Description Builder", layout="wide")

st.title("🔧 MRO Description Builder (MVP)")
st.write("Standardize MRO part descriptions using taxonomy + AI mapping")

tabs = st.tabs(["Single Item Mode", "Batch Mode"])

# --- Single Item Mode ---
with tabs[0]:
    st.header("Single Item Mode")
    manufacturer = st.text_input("Manufacturer")
    part_number = st.text_input("Part Number")
    if st.button("Fetch & Generate"):
        # Placeholder for fetch-map-generate
        st.success(f"Generated description for {manufacturer} {part_number}:")
        st.code("FUSE: CARTRIDGE, 250VAC, 800MA, ...", language="text")

# --- Batch Mode ---
with tabs[1]:
    st.header("Batch Mode")
    uploaded_file = st.file_uploader("Upload XLS/CSV", type=["xls", "xlsx", "csv"])
    if uploaded_file:
        df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith(("xls", "xlsx")) else pd.read_csv(uploaded_file)
        st.write("Preview:", df.head())
        if st.button("Process Batch"):
            # Placeholder batch result
            df["Description"] = "Generated description..."
            st.write(df.head())
            st.download_button("Download Processed File", df.to_csv(index=False), "processed.csv", "text/csv")

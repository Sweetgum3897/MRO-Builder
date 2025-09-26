import streamlit as st
import pandas as pd
import json
from pathlib import Path

# Load dictionary (from JSON we created earlier)
DICT_PATH = Path(__file__).resolve().parents[1] / "data" / "mro_dictionary.json"

st.set_page_config(page_title="MRO Description Builder", layout="wide")

st.title("🔧 MRO Description Builder (MVP)")
st.write("Standardize MRO part descriptions using taxonomy + AI mapping")

# Session state to store results across tabs
if "results" not in st.session_state:
    st.session_state["results"] = pd.DataFrame(columns=["Manufacturer", "Part Number", "URL", "Description"])

tabs = st.tabs(["Single Item Mode", "Batch Mode", "Output"])

# --- Single Item Mode ---
with tabs[0]:
    st.header("Single Item Mode")

    manufacturer = st.text_input("Manufacturer")
    part_number = st.text_input("Part Number")
    url = st.text_input("Product URL (optional)")

    if st.button("Fetch & Generate"):
        # Placeholder for fetch-map-generate logic
        description = f"Generated description for {manufacturer} {part_number or url}: FUSE: CARTRIDGE, 250VAC, 800MA, ..."
        st.success("Processing complete. See Output tab.")
        st.session_state["results"] = pd.concat([
            st.session_state["results"],
            pd.DataFrame([{
                "Manufacturer": manufacturer,
                "Part Number": part_number,
                "URL": url,
                "Description": description
            }])
        ], ignore_index=True)

# --- Batch Mode ---
with tabs[1]:
    st.header("Batch Mode")

    uploaded_file = st.file_uploader("Upload XLS/CSV", type=["xls", "xlsx", "csv"])
    if uploaded_file:
        df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith(("xls", "xlsx")) else pd.read_csv(uploaded_file)
        st.write("Preview:", df.head())

        if st.button("Process Batch"):
            # Placeholder batch logic
            df["Description"] = "Generated description..."
            st.success("Batch processing complete. See Output tab.")
            df["URL"] = ""  # placeholder, since no URL column in upload
            st.session_state["results"] = pd.concat([
                st.session_state["results"], df[["Manufacturer", "Part Number", "URL", "Description"]]
            ], ignore_index=True)

# --- Output Tab ---
with tabs[2]:
    st.header("Cleansed Descriptions")

    if not st.session_state["results"].empty:
        st.dataframe(st.session_state["results"])
        st.download_button(
            "Download All Results",
            st.session_state["results"].to_csv(index=False),
            "cleansed_descriptions.csv",
            "text/csv"
        )
    else:
        st.info("No results yet. Run Single Item or Batch mode first.")

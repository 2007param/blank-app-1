import streamlit as st

st.title("🧬Bioinformatics Tool")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("""
Welcome to the Bioinformatics Tool!  
Analyze DNA sequences using this interactive platform. You can perform nucleotide counting, k-mer analysis, 
and search for motifs or genes.  
""")
st.sidebar.header("Input Section")
sequence = st.sidebar.text_area(
    "Enter a DNA sequence (A, T, G, C only):",
    height=150,
    help="Paste or type a DNA sequence. Valid characters are A, T, G, and C."
).strip().upper()

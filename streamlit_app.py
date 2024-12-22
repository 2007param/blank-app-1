import streamlit as st
import pandas as pd
from collections import Counter
st.title("🧬Bioinformatics Tool")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("""
Welcome to the Bioinformatics Tool!  
Analyze DNA sequences using this interactive platform. You can perform nucleotide counting, k-mer analysis, 
and search for motifs or genes.  
""")
tab = st.radio(
    "Select an Analysis Option",
    ("Home", "Nucleotide Count", "K-mer Analysis", "Motif Search", "Gene Finder")
)

# Main Input Section: DNA Sequence
sequence_input = st.text_area(
    "Enter a DNA sequence:",
    height=150,
    help="Valid characters: A, T, G, and C only."
)
sequence = sequence_input.strip().upper()

# Helper Functions
@st.cache_data
def count_nucleotides(seq):
    """Count occurrences of each nucleotide."""
    return dict(Counter(seq))

@st.cache_data
def kmer_analysis(seq, k):
    """Analyze k-mers in the sequence."""
    kmers = [seq[i:i + k] for i in range(len(seq) - k + 1)]
    return dict(Counter(kmers))

@st.cache_data
def motif_search(seq, motif):
    """Find all occurrences of a motif."""
    indices = [i for i in range(len(seq)) if seq.startswith(motif, i)]
    return indices

@st.cache_data
def gene_finder(seq):
    """Find genes based on biological start and stop codons."""
    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}
    genes = []
    i = 0
    while i < len(seq):
        if seq[i:i + 3] == start_codon:
            for j in range(i + 3, len(seq), 3):
                if seq[j:j + 3] in stop_codons:
                    genes.append(seq[i:j + 3])
                    i = j
                    break
        i += 1
    return genes

# Display the title page when the user selects "Home"
if tab == "Home":
    display_title_page()

# Analyze the DNA sequence if entered
if sequence:
    valid_sequence = all(base in "ATGC" for base in sequence)
    if not valid_sequence:
        st.error("Invalid characters found in the DNA sequence. Please use only A, T, G, and C.")
else:
    valid_sequence = False

# Nucleotide Count Analysis
if tab == "Nucleotide Count" and valid_sequence:
    st.header("Nucleotide Count Analysis")
    counts = count_nucleotides(sequence)
    st.write("Nucleotide counts:")
    st.bar_chart(pd.DataFrame.from_dict(counts, orient="index", columns=["Count"]))

# K-mer Analysis
elif tab == "K-mer Analysis" and valid_sequence:
    st.header("K-mer Analysis")
    k = st.slider("Select the value of k:", 1, len(sequence), 2)
    kmer_results = kmer_analysis(sequence, k)
    st.write(f"K-mers found (k={k}):")
    st.dataframe(pd.DataFrame.from_dict(kmer_results, orient="index", columns=["Count"]))

# Motif Search Analysis
elif tab == "Motif Search" and valid_sequence:
    st.header("Motif Search")
    motif = st.text_input("Enter the motif to search for:", "ATG")
    if motif:
        motif_indices = motif_search(sequence, motif.upper())
        if motif_indices:
            st.write(f"Motif found at positions: {motif_indices}")
        else:
            st.write("Motif not found.")

# Gene Finder Analysis
elif tab == "Gene Finder" and valid_sequence:
    st.header("Gene Finder Analysis")
    genes = gene_finder(sequence)
    if genes:
        st.write(f"Genes found ({len(genes)}):")
        for i, gene in enumerate(genes, 1):
            st.write(f"{i}: {gene}")
    else:
        st.write("No genes found in the sequence.")

# Footer
st.markdown("---")
st.info("Bioinformatics Tool | Developed with [Streamlit](https://streamlit.io/)")

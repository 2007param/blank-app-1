import streamlit as st
import pandas as pd
from collections import Counter
st.markdown(
    """
    <style>
    .centered {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title for the tool
st.markdown('<h1 class="centered">Bioinformatics Tool 🧬</h1>', unsafe_allow_html=True)
st.markdown(
    """
    <p class="centered">
    Welcome to the Bioinformatics Tool! Analyze DNA sequences using this interactive platform. You can perform nucleotide counting, k-mer analysis, and search for motifs or genes.  
    </p>
    """,
    unsafe_allow_html=True
)

# Tabs for different analysis
tab = st.radio(
    "Select an Analysis Option",
    ("Nucleotide Count", "K-mer Analysis", "Motif Search", "Gene Finder"),
    index=0,
    label_visibility="collapsed"
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
    if len(seq) < k:
        return {"error": "Sequence length is shorter than k-mer size."}
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

@st.cache_data
def gc_content(seq):
    """Calculate the GC content of the sequence."""
    g_c = sum(1 for base in seq if base in "GC")
    return (g_c / len(seq)) * 100 if len(seq) > 0 else 0

@st.cache_data
def reverse_complement(seq):
    """Generate the reverse complement of the DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement.get(base, base) for base in reversed(seq))

@st.cache_data
def transcription(seq):
    """Transcribe the DNA sequence into mRNA."""
    transcription_dict = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(transcription_dict.get(base, base) for base in seq)

@st.cache_data
def translation(seq):
    """Translate the mRNA sequence into a protein sequence."""
    codon_table = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '', 'UAG': '',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C', 'UGA': '', 'UGG': 'W',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    return ''.join(codon_table.get(seq[i:i+3], '') for i in range(0, len(seq), 3))

@st.cache_data
def longest_orf(seq):
    """Find the longest open reading frame."""
    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}
    longest_gene = ""
    i = 0
    while i < len(seq):
        if seq[i:i + 3] == start_codon:
            for j in range(i + 3, len(seq), 3):
                if seq[j:j + 3] in stop_codons:
                    gene = seq[i:j + 3]
                    if len(gene) > len(longest_gene):
                        longest_gene = gene
                    i = j
                    break
        i += 1
    return longest_gene

@st.cache_data
def find_palindromes(seq):
    """Find palindromes in the sequence."""
    palindromes = []
    for i in range(len(seq)):
        for j in range(i + 4, len(seq) + 1):  # Palindromes of length 4 or more
            substring = seq[i:j]
            if substring == substring[::-1]:
                palindromes.append(substring)
    return palindromes

# Display the DNA sequence input and validation
if sequence:
    valid_sequence = all(base in "ATGC" for base in sequence)
    if not valid_sequence:
        st.error("Invalid characters found in the DNA sequence. Please use only A, T, G, and C.")
else:
    valid_sequence = False

# Handle the analysis based on selected tab
if tab == "Nucleotide Count" and valid_sequence:
    st.markdown('<h2 class="centered">Nucleotide Count Analysis</h2>', unsafe_allow_html=True)
    counts = count_nucleotides(sequence)
    st.write("Nucleotide counts:")
    st.bar_chart(pd.DataFrame.from_dict(counts, orient="index", columns=["Count"]))

elif tab == "K-mer Analysis" and valid_sequence:
    st.markdown('<h2 class="centered">K-mer Analysis</h2>', unsafe_allow_html=True)
    k = st.slider("Select the value of k:", 1, len(sequence), 2)
    kmer_results = kmer_analysis(sequence, k)
    st.write(f"K-mers found (k={k}):")
    st.dataframe(pd.DataFrame.from_dict(kmer_results, orient="index", columns=["Count"]))

elif tab == "Motif Search" and valid_sequence:
    st.markdown('<h2 class="centered">Motif Search</h2>', unsafe_allow_html=True)
    motif = st.text_input("Enter the motif to search for:", "ATG")
    motif_indices = motif_search(sequence, motif.upper())
    if motif_indices:
        st.write(f"Motif found at positions: {motif_indices}")
    else:
        st.write("Motif not found.")

elif tab == "Gene Finder" and valid_sequence:
    st.markdown('<h2 class="centered">Gene Finder Analysis</h2>', unsafe_allow_html=True)
    genes = gene_finder(sequence)
    if genes:
        st.write(f"Genes found ({len(genes)}):")
        for i, gene in enumerate(genes, 1):
            st.write(f"{i}: {gene}")
    else:
        st.write("No genes found in the sequence.")

elif tab == "GC Content" and valid_sequence:
    st.markdown('<h2 class="centered">GC Content</h2>', unsafe_allow_html=True)
    gc = gc_content(sequence)
    st.write(f"GC Content: {gc:.2f}%")

elif tab == "Reverse Complement" and valid_sequence:
    st.markdown('<h2 class="centered">Reverse Complement</h2>', unsafe_allow_html=True)
    rev_comp = reverse_complement(sequence)
    st.write(f"Reverse Complement: {rev_comp}")

elif tab == "Transcription" and valid_sequence:
    st.markdown('<h2 class="centered">Transcription (mRNA)</h2>', unsafe_allow_html=True)
    mRNA = transcription(sequence)
    st.write(f"mRNA Sequence: {mRNA}")

elif tab == "Translation" and valid_sequence:
    st.markdown('<h2 class="centered">Translation (Protein)</h2>', unsafe_allow_html=True)
    mRNA = transcription(sequence)
    protein = translation(mRNA)
    st.write(f"Protein Sequence: {protein}")

elif tab == "Longest ORF" and valid_sequence:
    st.markdown('<h2 class="centered">Longest Open Reading Frame (ORF)</h2>', unsafe_allow_html=True)
    orf = longest_orf(sequence)
    st.write(f"Longest ORF: {orf}")

elif tab == "Palindrome Finder" and valid_sequence:
    st.markdown('<h2 class="centered">Palindrome Finder</h2>', unsafe_allow_html=True)
    palindromes = find_palindromes(sequence)
    if palindromes:
        st.write(f"Palindromes found: {palindromes}")
    else:
        st.write("No palindromes found.")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<p class="centered">Bioinformatics Tool | Developed with <a href="https://streamlit.io/" target="_blank">Streamlit</a></p>', unsafe_allow_html=True)

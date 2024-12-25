import streamlit as st
import pandas as pd
from collections import Counter
from PIL import Image


def display_image():
    st.image("data:image/jpeg;base64,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", caption="Title Page", use_container_width=True)
def display_image1():
    st.image(image1, caption="About Us", use_column_width=True)
def display_image2():
    st.image(image2, caption="nucleotide_count_page", use_column_width=True)
def display_image3():
    st.image(image3, caption="kmer_analysis_page", use_column_width=True)
def display_image4():
    st.image(image4, caption="gene_finding_page", use_column_width=True)
def display_image5():
    st.image(image5, caption="hamming_distance_page", use_column_width=True)
def display_image6():
    st.image(image6, caption="reverse_complement_page", use_column_width=True)
def display_image7():
    st.image(image7, caption="gc_content_page", use_column_width=True)
def display_image8():
    st.image(image8, caption="transcription_page", use_column_width=True)
def display_image9():
    st.image(image9, caption="translation_page", use_column_width=True)
def display_image10():
    st.image(image10, caption="sequence_alignment_page", use_column_width=True)
    
def footer():
    st.markdown(
        """
        <style>
        footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 14px;
        }
        </style>
        <footer>
            <p>© 2024 Bioinformatics Tool. All rights reserved.</p>
        </footer>
        """, 
        unsafe_allow_html=True
    )

def is_valid_sequence(sequence):
    return all(base in 'ACTG' for base in sequence)

def apply_background_color(color):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def get_nucleotide_count(sequence):
    if is_valid_sequence(sequence):
        apply_background_color("#FFC0CB")  
        return {'A': sequence.count('A'), 'T': sequence.count('T'),
                'C': sequence.count('C'), 'G': sequence.count('G')}
    else:
        return "Invalid sequence! Please enter a DNA sequence containing only A, C, T, or G."

# Function for k-mer analysis
def kmer_analysis(sequence, k):
    if is_valid_sequence(sequence):
        kmers = {}
        for i in range(len(sequence) - k + 1):
            kmer = sequence[i:i + k]
            kmers[kmer] = kmers.get(kmer, 0) + 1
        apply_background_color("#008000")  
        return kmers
    else:
        return "Invalid sequence! Please enter a DNA sequence containing only A, C, T, or G."

# Function for Hamming distance
def hamming_distance(seq1, seq2):
    if len(seq1) != len(seq2):
        return "Error: Sequences must have the same length"
        if is_valid_sequence(seq1) and is_valid_sequence(seq2):
            apply_background_color("#D3D3D3")  
            return sum(el1 != el2 for el1, el2 in zip(seq1, seq2))
    else:
        return "Invalid sequence! Please enter a DNA sequence containing only A, C, T, or G."

# Function for Gene finding
def find_genes(sequence):
    if is_valid_sequence(sequence):
        start_codon = "ATG"
        stop_codons = ["TAA", "TAG", "TGA"]
        genes = []
        for i in range(len(sequence)):
            if sequence[i:i + 3] == start_codon:
                for j in range(i + 3, len(sequence), 3):
                    if sequence[j:j + 3] in stop_codons:
                        genes.append(sequence[i:j + 3])
                        break
        apply_background_color("#00FF00")  
        return genes
    else:
        return "Invalid sequence! Please enter a DNA sequence containing only A, C, T, or G."

# Function for Reverse complement
def reverse_complement(sequence):
    if is_valid_sequence(sequence):
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        apply_background_color("#FFD700")  
        return ''.join(complement[base] for base in reversed(sequence))
    else:
        return "Invalid sequence! Please enter a DNA sequence containing only A, C, T, or G."

# Function for GC Content
def gc_content(sequence):
    if is_valid_sequence(sequence):
        gc_count = sequence.count('G') + sequence.count('C')
        apply_background_color("#A52A2A")  
        return (gc_count / len(sequence)) * 100
    else:
        return "Invalid sequence! Please enter a DNA sequence containing only A, C, T, or G."

# Function for Transcription
def transcription(sequence):
    if is_valid_sequence(sequence):
        apply_background_color("#FFA500")  
        return sequence.replace('T', 'U')
    else:
        return "Invalid sequence! Please enter a DNA sequence containing only A, C, T, or G."

# Function for Translation (simple case, codon-to-amino acid)
def translation(sequence):
    if is_valid_sequence(sequence):
        codon_table = {
            'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
            'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
            'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
            'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
            'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
            'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
            'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
            'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
            'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
            'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
            'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
            'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
            'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
            'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
            'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W',
        }
        protein = ""
        for i in range(0, len(sequence), 3):
            codon = sequence[i:i+3]
            protein += codon_table.get(codon, '-')
        apply_background_color("#FAD7A0") 
        return protein
    else:
        return "Invalid sequence! Please enter a DNA sequence containing only A, C, T, or G."

# Function for Sequence alignment (simple version)
def sequence_alignment(seq1, seq2):
    if is_valid_sequence(seq1) and is_valid_sequence(seq2):
        from difflib import SequenceMatcher
        matcher = SequenceMatcher(None, seq1, seq2)
        match_ratio = matcher.ratio()
        apply_background_color("#808000")  
        return f"Sequence similarity ratio: {match_ratio*100:.2f}%"
    else:
        return "Invalid sequence! Please enter a DNA sequence containing only A, C, T, or G."

# Function to display the title page
def title_page():    
    display_image()
    apply_background_color("#D6EAF8")  
    st.markdown("<h1 style='text-align: center;'>🧬 Bioinformatics Tool</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Welcome to the Bioinformatics Tool. This app provides several bioinformatics analysis tools such as Nucleotide count, K-mer analysis, Gene Finding, and more. Select an option from the menu to get started!</p>", unsafe_allow_html=True)
    footer()
def about_us_page():
    display_image1()
    apply_background_color("#F4ECF7")  
    st.markdown("<h1 style='text-align: center;'>About Us</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>We are a team of passionate bioinformaticians, biologists, and developers working to provide tools for DNA sequence analysis. Our goal is to make bioinformatics more accessible and provide a range of useful functionalities for researchers and students alike.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>If you have any questions or feedback, please don't hesitate to contact us at:</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Email: ai-tutorial@example.com</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Phone: (123)-456-7890</p>", unsafe_allow_html=True)
    footer()

# Function for Nucleotide count page
def nucleotide_count_page():
    display_image2()
    apply_background_color("#FFC0CB")  
    st.markdown("<h2 style='text-align: center;'>Nucleotide Count</h2>", unsafe_allow_html=True)
    sequence = st.text_area("Enter a DNA sequence:").upper()
    if sequence:
        if is_valid_sequence(sequence):
            counts = get_nucleotide_count(sequence)
            st.markdown(f"<p style='text-align: center;'>A: {counts['A']}, T: {counts['T']}, C: {counts['C']}, G: {counts['G']}</p>", unsafe_allow_html=True)
        else:
            st.error("Invalid sequence! Please enter a DNA sequence containing only A, C, T, or G.")
    footer()
# Function for K-mer analysis page
def kmer_analysis_page():
    display_image3()
    apply_background_color("#008000")  
    st.markdown("<h2 style='text-align: center;'>K-mer Analysis</h2>", unsafe_allow_html=True)
    sequence = st.text_area("Enter a DNA sequence:")
    k = st.number_input("Enter the value of k:", min_value=1, step=1)
    if sequence and k:
        if is_valid_sequence(sequence):
            kmers = kmer_analysis(sequence, int(k))
            st.markdown("<p style='text-align: center;'>K-mer analysis results:</p>", unsafe_allow_html=True)
            st.write(kmers)
        else:
            st.error("Invalid sequence! Please enter a DNA sequence containing only A, C, T, or G.")
    footer()
# Function for Gene Finding page
def gene_finding_page():
    display_image4()
    apply_background_color("#00FF00")  
    st.markdown("<h2 style='text-align: center;'>Gene Finding</h2>", unsafe_allow_html=True)
    sequence = st.text_area("Enter a DNA sequence:")
    if sequence:
        if is_valid_sequence(sequence):
            genes = find_genes(sequence.upper())
            st.markdown(f"<p style='text-align: center;'>Found genes: {genes}</p>", unsafe_allow_html=True)
        else:
            st.error("Invalid sequence! Please enter a DNA sequence containing only A, C, T, or G.")
    footer()
# Function for Hamming Distance page
def hamming_distance_page():
    display_image5()
    apply_background_color("#D3D3D3")  
    st.markdown("<h2 style='text-align: center;'>Hamming Distance</h2>", unsafe_allow_html=True)
    seq1 = st.text_area("Enter the first DNA sequence:")
    seq2 = st.text_area("Enter the second DNA sequence:")
    if seq1 and seq2:
        if is_valid_sequence(sequence):
            result = hamming_distance(seq1.upper(), seq2.upper())
            st.markdown(f"<p style='text-align: center;'>Hamming Distance: {result}</p>", unsafe_allow_html=True)
        else:
            st.error("Invalid sequence! Please enter a DNA sequence containing only A, C, T, or G.")
    footer()
# Function for Reverse Complement page
def reverse_complement_page():
    display_image6()
    apply_background_color("#FFD700")  
    st.markdown("<h2 style='text-align: center;'>Reverse Complement</h2>", unsafe_allow_html=True)
    sequence = st.text_area("Enter a DNA sequence:")
    if sequence:
        if is_valid_sequence(sequence):
            complement = reverse_complement(sequence.upper())
            st.markdown(f"<p style='text-align: center;'>Reverse complement: {complement}</p>", unsafe_allow_html=True)
        else:
            st.error("Invalid sequence! Please enter a DNA sequence containing only A, C, T, or G.")
    footer()
# Function for GC Content page
def gc_content_page():
    display_image7()
    apply_background_color("#A52A2A")  
    st.markdown("<h2 style='text-align: center;'>GC Content</h2>", unsafe_allow_html=True)
    sequence = st.text_area("Enter a DNA sequence:")
    if sequence:
        if is_valid_sequence(sequence):
            gc_percent = gc_content(sequence.upper())
            st.markdown(f"<p style='text-align: center;'>GC Content: {gc_percent:.2f}%</p>", unsafe_allow_html=True)
        else:
            st.error("Invalid sequence! Please enter a DNA sequence containing only A, C, T, or G.")
    footer()
# Function for Transcription page
def transcription_page():
    display_image8()
    apply_background_color("#FFA500")  
    st.markdown("<h2 style='text-align: center;'>Transcription</h2>", unsafe_allow_html=True)
    sequence = st.text_area("Enter a DNA sequence:")
    if sequence:
        if is_valid_sequence(sequence):
            transcribed = transcription(sequence.upper())
            st.markdown(f"<p style='text-align: center;'>Transcribed RNA sequence: {transcribed}</p>", unsafe_allow_html=True)
        else:
            st.error("Invalid sequence! Please enter a DNA sequence containing only A, C, T, or G.")
    footer()
# Function for Translation page
def translation_page():
    display_image9()
    apply_background_color("#FAD7A0")  
    st.markdown("<h2 style='text-align: center;'>Translation</h2>", unsafe_allow_html=True)
    sequence = st.text_area("Enter a DNA sequence:")
    if sequence:
        if is_valid_sequence(sequence):
            protein = translation(sequence.upper())
            st.markdown(f"<p style='text-align: center;'>Translated protein sequence: {protein}</p>", unsafe_allow_html=True)
        else:
            st.error("Invalid sequence! Please enter a DNA sequence containing only A, C, T, or G.")
    footer()
# Function for Sequence Alignment page
def sequence_alignment_page():
    display_image10()
    apply_background_color("#808000")  
    st.markdown("<h2 style='text-align: center;'>Sequence Alignment</h2>", unsafe_allow_html=True)
    seq1 = st.text_area("Enter the first DNA sequence:")
    seq2 = st.text_area("Enter the second DNA sequence:")
    if seq1 and seq2:
        if is_valid_sequence(sequence):
            result = sequence_alignment(seq1.upper(), seq2.upper())
            st.markdown(f"<p style='text-align: center;'>Sequence alignment result: {result}</p>", unsafe_allow_html=True)
        else:
            st.error("Invalid sequence! Please enter a DNA sequence containing only A, C, T, or G.")
    footer()
# Function to control page navigation
def main():
# Sidebar navigation to select pages
    page = st.sidebar.radio(
        "Select a page:",
        ("Title Page", "Nucleotide Count", "K-mer Analysis", "Gene Finding", "Hamming Distance", 
         "Reverse Complement", "GC Content", "Transcription", "Translation", 
         "Sequence Alignment", "About Us")
    )
    footer()

# Display selected page
    if page == "Title Page":
        title_page()
    elif page == "Nucleotide Count":
        nucleotide_count_page()
    elif page == "K-mer Analysis":
        kmer_analysis_page()
    elif page == "Gene Finding":
        gene_finding_page()
    elif page == "Hamming Distance":
        hamming_distance_page()
    elif page == "Reverse Complement":
        reverse_complement_page()
    elif page == "GC Content":
        gc_content_page()
    elif page == "Transcription":
        transcription_page()
    elif page == "Translation":
        translation_page()
    elif page == "Sequence Alignment":
        sequence_alignment_page()
    elif page == "About Us":
        about_us_page()
    
if __name__ == "__main__":
        main()

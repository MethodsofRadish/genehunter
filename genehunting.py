#! usr/bin/env python3.7

import sys
import fileinput

# Gene_Hunting Python3.7 Script that takes a file from command line arguments
# Prints the output to Standard Out.

# Written by Marcus W. on April 30, 2020

# Welcome to Gene Hunting in DNA Python 3.7 Program
# This program takes a .txt file of Gene Names, a muilti-fasta file of all the coding genes in a genome (.ffn), and a full genome fasta file (.fna).
# Take the gene names, find and isolate them from the coding genes file.
# Take the matching genes and in the full genome take every nucleotide up from 200 nt from position 0, including ATG.

# Take the files from command line (geneNames.txt, coding muilti Fasta, full genome)
gene_names_File = sys.argv[1]
coding_genes_File = sys.argv[2]
genome_File = sys.arg[3]


# Open the files
openGeneNames = open(gene_names_File)
openCodingGenes = open(coding_genes_File)
openGenome = open(genome_File)

# Take the genes name and split it into a list.

# Take the coding region (cds) muilti-fasta file and split it into a list.

# Compare each name to the header of the muilti-fasta file. If it matches, print name and location and strand (+ or -)

# Using the gene name and location of starting point, take each nucleotide starting at the ATG and go upstream 200 nt.

# Complete this process for numerous species with the same gene names.

# Close files to end program
openGeneNames.close()
openCodingGenes.close()
openGenome.close()
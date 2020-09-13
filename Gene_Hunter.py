#! usr/bin/env python3.7

import sys
import fileinput

# Welcome to Salmonella Gene Extraction Pipeline Program in Python
# The purpose of this program is to receive two files
# File one is a *muilti-fasta* genome file with genes
# The second file is a list of gene names to find in the *muilti-fasta* genome file.
# The output will be to a new fasta file, the FOUND gene header and genetic info.

#Create another program to search a sequence in a full fasta file with complete genome. FUTURE



# Initialize Variables
genome_File = sys.argv[1]
print("The first argument is %s " + genome_File)

# Open the muilti-fasta file
genome = open(genome_File)

# Initialize the gene name text file
gene_list_File = sys.argv[2]

# Open gene name list file
gene_list = open(gene_list_File)

# Loop to parse the muilti-fasta file inside a loop to go through gene name text file
for sequence in genome:
	print("Hello Sequence!")
	for gene in gene_list:
		print("Hello Gene!")

# Create a new file to write the found genes inside
new_outPut_File = open("myFoundGenes.txt", 'xt')

# Close files to end program
genome.close()
gene_list.close()
new_outPut_File.close()

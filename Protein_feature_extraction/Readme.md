Procvec is a method for representing biological sequences. This algorithm is first proposed in the paper: "ProtVec: A Continuous Distributed Representation of Biological Sequences". The github page of ProtVec is https://github.com/kyu999/biovec

First,

pip install biovec

import biovec

The trained model in '/trained_models/swissprot-reviewed.model' is available in the github page

Protein_features_extraction.py : This code will generate feature files from the inputfile 

Input file = kegg.fasta

Output files will be feature files extracted from input file

The command will be = 'python Protein_features_extraction.py -inputfile kegg.fasta'

Python3.6.4 are required to run this code.

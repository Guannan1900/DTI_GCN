Mol2vec is a method for learning vector representations of molecular substructures. The github page of Mol2vec is https://github.com/samoturk/mol2vec. 

First install the mol2vec. The requirements are available in the github page.

The trained model is also available in github page: https://github.com/samoturk/mol2vec/tree/master/examples/models

Input file = drug.sdf.gz

Output file = drug_new.csv

The command will be = 'mol2vec featurize -i drug.sdf.gz -o drug_new.csv -m model_300dim.pkl -r 1 --uncommon UNK'

Python3.6.4 are required to run this code.
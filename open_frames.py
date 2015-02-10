from translate import *
from transcribe import transcribe

def open_frames(sequence):
    reverse_sequence = sequence[::-1]
    for seq in sequence, reverse_sequence:
        for i in range(3):
            rna = transcribe(seq[i:])
            amino_acids = translate(rna)
            print amino_acids

if __name__ == '__main__':
    sequence = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
    print open_frames(sequence)

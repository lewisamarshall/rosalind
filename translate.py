translation_map = dict()
with open('codons.txt') as file:
    for line in file:
        codon, amino_acid = line.split()
        translation_map[codon] = amino_acid

def translate(sequence):
    protein = []
    for i in range(len(sequence)/3):
        codon = sequence[i*3:i*3+3]
        amino_acid = translation_map[codon]
        if amino_acid != 'Stop':
            protein.append(amino_acid)
        else:
            break
    protein = ''.join(protein)
    return protein

if __name__ == '__main__':
    with open('data/rosalind_prot.txt') as file:
        sequence = file.read()
    print translate(sequence)

print translation_map

from read_fasta import read_fasta
import operator
bases = ['A', 'T', 'G', 'C']

def profile(sequences):
    length = len(sequences.values()[0])
    profiles = {base: [0]*length for base in bases}
    for sequence in sequences.values():
        for idx, base in enumerate(sequence):
            profiles[base][idx]+=1
    return profiles

def consensus(profiles):
    con = []

    length = len(profiles.values()[0])
    for idx in range(length):
        idx_profile = {base:val[idx] for base, val in profiles.items()}
        con.append(max(idx_profile.iteritems(), key = operator.itemgetter(1))[0])
    return ''.join(con)

if __name__ == '__main__':
    sequences = {'>Rosalind_1':
                'ATCCAGCT',
                '>Rosalind_2':
                'GGGCAACT',
                '>Rosalind_3':
                'ATGGATCT',
                '>Rosalind_4':
                'AAGCAACC',
                '>Rosalind_5':
                'TTGGAACT',
                '>Rosalind_6':
                'ATGCCATT',
                '>Rosalind_7':
                'ATGGCACT'}
    sequences = read_fasta('data/rosalind_cons.txt')
    print consensus(profile(sequences))
    for key, value in profile(sequences).items():
        print key+':', ' '.join([str(i) for i in value])

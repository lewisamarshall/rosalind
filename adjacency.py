from read_fasta import read_fasta

def adjacency(sequences, k):
    edges = []
    for i_key, i_value in sequences.items():
        for j_key, j_value in sequences.items():
            if i_key != j_key:
                if i_value[-3:] == j_value[:3]:
                    edges.append((i_key, j_key))
    return edges

if __name__ == '__main__':
    edges =  adjacency(read_fasta('data/rosalind_grph.txt'), 3)
    for pair in edges:
        print '{} {}'.format(*pair)

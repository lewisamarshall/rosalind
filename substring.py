from read_fasta import read_fasta

def substring(sequences):
    shortest = min(sequences.values(), key=len)
    for length in range(len(shortest), -1, -1):
        for index in range(len(shortest)-length):
            subsequence = shortest[index:index+length+1]
            if common(subsequence, sequences):
                return subsequence

def common(subsequence, sequences):
    for sequence in sequences.values():
        if not subsequence in sequence:
            return False
    return True

if __name__ == '__main__':
    import time
    sequences = {'Rosalind_1':
                 'GATTACA',
                 'Rosalind_2':
                 'TAGACCA',
                 'Rosalind_3':
                 'ATACA'}
    sequences = read_fasta('data/rosalind_lcsm.txt')
    epoch = time.time()
    print substring(sequences)
    print time.time()-epoch

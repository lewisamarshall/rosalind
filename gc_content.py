import string
table = string.maketrans('', '')

def gc_content(sequence):
    subseq = sequence.translate(table, 'GC')
    gc_frac = 1.-(float(len(subseq))/float(len(sequence)))
    return gc_frac*100.

def max_gc_content(sequences):
    contents = {gc_content(sequence): key for key, sequence in sequences.items()}
    return contents[max(contents.keys())], max(contents.keys())



if __name__ == '__main__':
    from read_fasta import read_fasta

    sequences = read_fasta('rosalind_gc (1).txt')
    for text in max_gc_content(sequences):
        print text

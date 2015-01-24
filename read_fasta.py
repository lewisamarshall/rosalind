def read_fasta(file):
    output = dict()
    with open(file) as filereader:
        for line in filereader:
            if line[0] == '>':
                name = line[1:].rstrip()
                output[name] = ''
            else:
                output[name] = output[name]+line.rstrip()
    return output

if __name__ == '__main__':
    print read_fasta('test.fasta')

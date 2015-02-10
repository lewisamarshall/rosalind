from read_fasta import read_fasta
import urllib2

def get_protein(uniprot_id):
    fasta = download_uniprot(uniprot_id)
    sequence = read_fasta()

def download_uniprot(uniprot_id):
    url = 'http://www.uniprot.org/uniprot/{}.fasta'.format(uniprot_id)
    response = urllib2.urlopen(url)
    for line in response:
        print line
    # return html

if __name__ == '__main__':
    print download_uniprot('A2Z669')

dna_to_rna_table = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}


def to_rna(dna):
    rna = ''
    for nucleotide in dna:
        if nucleotide in dna_to_rna_table:
            rna += dna_to_rna_table[nucleotide]
        else:
            return ''
    return rna

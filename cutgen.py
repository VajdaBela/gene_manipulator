#!/usr/bin/python3
import sys
import re

gene_to_komplement_genome = { 'A' : 'T',
                              'C' : 'G',
                              'T' : 'A',
                              'G' : 'C',
                              'N' : 'N',
                              'R' : 'Y',
                              'Y' : 'R',
                              'M' : 'K',
                              'K' : 'M' }

gene_to_matching_regex = { 'A' : 'A',
                           'C' : 'C',
                           'T' : 'T',
                           'G' : 'G',
                           'K' : '[GT]',
                           'M' : '[AC]',
                           'N' : '[ACTG]',
                           'R' : '[AG]',
                           'Y' : '[CT]',
                           '-' : '.' }

gene_to_palindrome_equal = { 'A' : 'ANMR',
                             'C' : 'CNMY',
                             'T' : 'TNKY',
                             'G' : 'GNKR',
                             'N' : 'ACTGNRYMK',
                             'R' : 'RNAGKM',
                             'Y' : 'YNCTMK',
                             'M' : 'MNACRY',
                             'K' : 'KNGTRY' }

#main 
if __name__ == "__main__":

    #usage message
    if not len(sys.argv) == 3:
        print("Usage: cutgen.py <file> <restriction>")
        sys.exit(1)

    in_file_name = sys.argv[1]
    restriction_site_str = sys.argv[2]

    #check if restriction_site good
    match_obj = re.match(r'''
        ^(                              # line beginning
        \^-*[ACGKMNRTY]+                 # split point at begining
        | [ACGKMNRTY]+\^[ACGKMNRTY]+      # split point in the middle
        | [ACGKMNRTY]+-*\^               # split point at end
        )$                              # line ending
        ''', restriction_site_str, re.VERBOSE)
    if not match_obj:
        print("Fatal: bad restriction site")
        sys.exit(1)

    #open file, read DNA
    in_file=open(in_file_name, "r")
    DNA_sequence=in_file.read().strip()
    in_file.close()

    #strip genes from restriction site
    restriction_site_genes = [x for x in restriction_site_str if x in gene_to_komplement_genome.keys()]
    restriction_site_genes = ''.join(restriction_site_genes)
    #make restriction site complement
    restriction_site_complement = [gene_to_komplement_genome[x] for x in restriction_site_genes]
    restriction_site_complement = restriction_site_complement[::-1]
    restriction_site_complement = ''.join(restriction_site_complement)
    #check if palindrome
    is_palindrome = [x in gene_to_palindrome_equal[y] 
            for x, y in zip(restriction_site_genes, restriction_site_complement)]
    is_palindrome = all(is_palindrome)
    if not is_palindrome:
        print ("Restriction site isn't a palindrome!", file=sys.stderr)

    #print column meanings
    print("place of cut"," fragment", "fragment length", sep='\t')

    #build regex for DNA matching
    #get idx of where to cut DNA
    regex_parts = []
    cut_idx = 0;
    for idx, genome in enumerate(restriction_site_str):
        if genome == '^':
            cut_idx = idx
        else:
            regex_parts.append(gene_to_matching_regex[genome])
    restriction_site_regex = ''.join(regex_parts)
    restriction_site = re.compile(restriction_site_regex)

    #get fragments and 
    #print idx, fragment, len
    previous_end_idx = 0
    for match in restriction_site.finditer(DNA_sequence):
        fragment_end_idx = match.start() + cut_idx
        fragment = DNA_sequence[previous_end_idx : fragment_end_idx]
        fragment_len = len(fragment)

        print(previous_end_idx, fragment, fragment_len, sep='\t')

        previous_end_idx = fragment_end_idx

    #print the last idx, fragemt and len
    if previous_end_idx != len(DNA_sequence):
        fragment = DNA_sequence[previous_end_idx:] 
        fragment_len = len(fragment)
        print(previous_end_idx, fragment, fragment_len, sep='\t')
    sys.exit(0)

#!/usr/bin/python3
import sys

codon_to_protein={
"TTT":"Phe",
"TTC":"Phe",
"TTA":"Leu",
"TTG":"Leu",
"CTT":"Leu",
"CTC":"Leu",
"CTA":"Leu",
"CTG":"Leu",
"ATT":"Ile",
"ATC":"Ile",
"ATA":"Ile",
"ATG":"Met",
"GTT":"Val",
"GTC":"Val",
"GTA":"Val",
"GTG":"Val",
"TCT":"Ser",
"TCC":"Ser",
"TCA":"Ser",
"TCG":"Ser",
"CCT":"Pro",
"CCC":"Pro",
"CCA":"Pro",
"CCG":"Pro",
"ACT":"Thr",
"ACC":"Thr",
"ACA":"Thr",
"ACG":"Thr",
"GCT":"Ala",
"GCC":"Ala",
"GCA":"Ala",
"GCG":"Ala",
"TAT":"Tyr",
"TAC":"Tyr",
"TAA":"STOP",
"TAG":"STOP",
"CAT":"His",
"CAC":"His",
"CAA":"Gln",
"CAG":"Gln",
"AAT":"Asn",
"AAC":"Asn",
"AAA":"Lys",
"AAG":"Lys",
"GAT":"Asp",
"GAC":"Asp",
"GAA":"Glu",
"GAG":"Glu",
"TGT":"Cys",
"TGC":"Cys",
"TGA":"STOP",
"TGG":"Trp",
"CGT":"Arg",
"CGC":"Arg",
"CGA":"Arg",
"CGG":"Arg",
"AGT":"Ser",
"AGC":"Ser",
"AGA":"Arg",
"AGG":"Arg",
"GGT":"Gly",
"GGC":"Gly",
"GGA":"Gly",
"GGG":"Gly"
}

#main 
#takes 3 by 3 genes and turns it into coresponding protein
if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: proteingen.py <genome>")
        sys.exit(1)
    
    fragment = sys.argv[1]
    codons = [fragment[i:i+3] for i in range(0, len(fragment),3)]
    surplus = []
    if len(codons[-1]) != 3:
        surplus = codons[-1]
        codons.pop()
    proteins = [ codon_to_protein[codon] for codon in codons]
    print("Protein sequence is:", "".join(proteins))
    if surplus:
        print("Surplus is:", surplus)
    sys.exit(0)

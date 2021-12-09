# gene_manipulator
## About
gene_manipulator is a set of 4 programs, 3 of which can be used standalone. The programs are:
 - chkgen.py
 - cutgen.py
 - proteingen.py
 - aafrgen.sh

Python is required for chkgen.py, cutgen.py and proteingen.py.

A Bash shell is required for aafrgen.sh. aafrgen.sh relies and ties together the aforementioned python programs.

'Program za pronalaženje restrikcionih mesta.docx' is the original Serbian description of the project.
## chkgen.py
Checks wether the DNA is genomic. DNA is genomic if it only contains the letters A, C, T and G.

To call program:

	chkgen.py <file>

File should contain the DNA. sequence.txt is an example file containing a short DNA.
## cutgen.py
Cuts DNA specified by the restriction site.

The program writes to the output each DNA fragment, where is its beggining in the whole DNA, and its length.

To call program:

	cutgen.py <file> <restriction_site>

The restriction site consists of genes A, C, T, G and non gene letters  R, Y, M, K, N. The non gene letters represent choices of genes. Eg. R can be either A or G.

Non gene letter meanings:
 - R = A or G
 - M = A or C
 - K = G or T
 - Y = C or T
 - N = A or C or T or G (all the genes)

The restriction site must contain the letter ^. It specifies where to cut the DNA. If the DNA should be cut before or after the restriction site it should be padded with -.

The restriction site should be a palindrome, but it is not a necessitiy. For restriction sites palindorome has a different meanig than the tradicional one. In this case the complement of the restriction site should be read backwards the same as the original forwards. To get the compliment all the genes and non gene letters are turned to their complement. 

To get the complement you should turn:
 - A to T
 - C to G
 - T to A
 - G to C
 - R to Y
 - M to K
 - K to M
 - Y to R
 - N stays the same

Here are some examples of palindromic restriction sites:
 - ^----ACGT
 - A^NT
 - MACK---^

## proteingen.py
Takes a genome and turns it into a protein sequence.

To call program:

	proteingen.py <genome> 

## aafrgen.sh
Ties the aformentioned programs together.

To call program:

	aafrgen.sh <file> <restriction_site>

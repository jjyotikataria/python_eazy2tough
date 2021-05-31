ipython 

import Bio
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC


temp = Seq("ATGCAT", IUPAC.unambiguous_dna)

temp.reverse_complement()


Output:
Seq('ATGCAT', IUPACUnambiguousDNA())

ipython 

import Bio
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

cdna = Seq("ATGCAT", IUPAC.unambiguous_dna)

cdna
Out[8]: Seq('ATGC', IUPACUnambiguousDNA())

mrna = cdna.transcribe()

In [10]: mrna
Out[17]: Seq('AUGCAU', IUPACUnambiguousRNA())
  
protein = mrna.translate()

In [16]: protein
Out[16]: Seq('MH', IUPACProtein())



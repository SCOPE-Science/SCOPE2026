# Independent mathematical audit

## correctness

FAIL

The three numerical spectra are correct for the intended representatives, but the frozen statement and its scope expressly identify them as the [8,2,4] entries of Table 10. In the cited arXiv:2512.12335v1, the exact matrices occur under Table 8, l2-optimal free codes (Part II), p. 20, not Table 10, which is headed l4-optimal free codes. The later available arXiv copy places them in Table 11, not Table 10. The journal table numbering was not independently verified. In the intended row order the first-row supports are {1,4,5,7}, {1,4,5,6,7,8}, {1,6,7,8} and the second-row support is always {2,3,4,5}. Using x*kappa=x and additive characteristic two, the four column counts (00,10,01,11) are (2,2,2,2), (0,4,2,2), (0,4,4,0). For message coefficients a,b, a 10 coordinate is a, 01 is b, and 11 is a+b. There is one zero word; each of the patterns a nonzero alone, b nonzero alone, and a=b nonzero contributes three words; six messages have a,b distinct and nonzero and activate every nonzero column. Columns 10 and 01 occur in all three matrices, so all messages give distinct words. This proves the numeric formulas and distinctness for the intended matrices; the independent `python3 /workspace/reviews/reproduce.py 4` verifies all 48 messages. The frozen script was inspected, not executed. Correcting the locator alone would not remedy originality or value.

## originality

FAIL

The numerical enumerators are covered as direct instances of the known linear-code weight-enumerator formula applied to the completely printed residue generators. The argument uses neither an unproved equivalence of rings nor a new fact about the classification. The numerical expressions need not already be printed verbatim for this implication to hold.

## value

FAIL

The source's optimal free rank-two stratum is natural and Hamming weights are relevant invariants, but this frozen claim merely evaluates a mechanically determined certificate for three already classified matrices. Each evaluation is an inspection of eight columns and four coefficient cases, already covered by the general weight theorem. Correcting the table number, showing reproducibility, or noting an alternative inequivalence certificate does not add a substantive unknown exact fact. No surviving valuable repair was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.

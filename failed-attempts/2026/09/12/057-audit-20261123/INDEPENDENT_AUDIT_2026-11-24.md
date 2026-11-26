# Independent mathematical audit

## correctness

PASS

Writing H=95232 and alpha=2H, the centered quotient floor((r+H-1)/alpha) is taken modulo 44; the quotient 44 folds to zero and subtracts one from the low part. Thus block zero wraps through q-1 and has alpha+1 residues; the other 43 have alpha. The edge from c_j to c_j+1 is the only transition in a neighborhood of the block top, and the circular seam from q-1 to 0 is not a transition. For a positive shift d the crossing starts lie in [c_j-d+1,c_j]; for a negative shift -d they lie in [c_j+1,c_j+d]. On the first range the low part is positive; on the second it is negative, also for the 43-to-0 high-bit transition. The resulting UseHint correction is the neighboring high bit modulo 44. Counts are 44d per signed shift, 44*156=6864 in the union and 44*78*79=271128 pairs in total. A fresh scalar implementation checked every candidate edge neighborhood for every shift and matched the committed census JSON, and independently checked the archived hint vector and the 81-weight modification. Global exhaustion follows from the block partition, not from sampling the complement of those neighborhoods. This does not demonstrate the behavior of a concrete signing implementation or valid signatures at weight 80.

## originality

FAIL

Reconstruction is an explicit prior theorem under weaker shift restrictions. The other numbers are immediate from the standard's integer rounding intervals and parameter values; no independent exact-census source is needed to establish this implication. The weight-80/81 fixture is a synthetic repetition crossing a published helper boundary and testing a published cutoff.

## value

FAIL

The edge cases are useful for conformance tests but the totals are routine consequences of the prescribed rounding. The synthetic vectors exercise a scalar threshold without a new signing-level boundary result or a demonstrated implementation defect.

The dated certificate retains the supplied scientific assessment, sources and limitations.

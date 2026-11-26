# Independent mathematical audit

## correctness

PASS

Complex rank is the number of nonzero Fourier multipliers. The sign-to-binary change doubles the nontrivial multipliers and the sign DC term is 2k−pq≠0 even at the endpoints. Galois conjugacy partitions the other frequencies into full prime and mixed orbits. Vanishing of a prime orbit is equivalent to constant integral margins in its CRT coordinate; both cannot vanish at an interior weight. Mixed vanishing leaves only univariate terms under Fourier inversion, so B_ij=A_i+D_j. If any two rows differ, they differ by a nonzero constant, which forces both rows and hence every row to be constant, giving identical columns; otherwise rows are identical. The nonconstant repeated-row/column cases then retain all Fourier characters in the other coordinate. Otherwise removal of exactly the relevant prime orbit, or no removal, gives the remaining interior ranks. The binomial counts are the independent fixed-weight choices per row or column minus the repeated-vector subfamily, with disjoint interior divisibility conditions; endpoints, distinctness and attainability follow (unit support, repeated or nonrepeated unit rows/columns, and constants). Independently enumerated every weight and rank at n=15 and 21 by exact integer coefficients in the product cyclotomic basis, not by classifying repeated rows: python3 /workspace/checks/5.py (NumPy), output /workspace/checks/5.out. Both frozen programs were read, not executed.

## originality

FAIL

The six-rank classification and every weight-specific multiplicity are a mechanical corollary of Miller's proof of Lemma 2(3) (not merely its aggregate probability statement), the Fourier-rank identity, and an elementary count of repeated rows/columns within Miller's margin events. The rank table need not be printed in either prior reference for this to constitute coverage. The scientific failure is prior implication, not unavailable historical literature.

## value

FAIL

Exact nullity at a given support weight is a naturally motivated invariant and the tabulation is convenient. However, the entire proposed refinement here follows by the Fourier rank identity and elementary fixed-margin counting inside Miller's existing proof-level cases. The count of repeated choices is one copy of the binomial coefficient instead of its power; both residual strata follow by subtraction. This provides no further independent structural result or new useful exact invariant beyond that mechanical consequence. No scientifically distinct valuable remainder was established to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.

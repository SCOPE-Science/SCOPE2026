# Independent mathematical audit

## correctness

PASS

The smooth branch sextic gives a K3 double plane in characteristic 5. Shimada proves that the 22 chosen rational-curve classes over F25 form the full integral geometric basis (Artin invariant one and the matching determinant −25), not just a rational spanning set. The published Gram matrix and Frobenius and deck isometries act in this same basis. The identification w↦√2·w gives the Frobenius cocycle J for the nonsquare twist because Frobenius sends √2 to −√2. Since the finite-field Brauer group vanishes, the fixed integral classes are the actual arithmetic Picard classes. Separate exact calculations from the published arrays recover the fixed lattices using columns of unimodular Smith transformations; zero columns yield a saturated integral kernel. The ranks, Gram determinants and nonunit Smith factors are (12,−5120, nine 2s and 10) and (11,10240, ten 2s and 10). The full divisor basis over F25 spans H² after the Tate twist, so the involution multiplicities 12/10 and 11/11 give the stated ±5 eigenvalues and point counts for all n by the trace formula. Direct enumeration independently confirms 36 and 26 over F5 and 1176 for both over F25 only. The frozen program does not itself implement the claimed orthogonal-complement checks; those optional checks are not needed for the independently reproduced Finding.

## originality

FAIL

No checked source was found that prints both fixed-lattice discriminant groups as a table, but the exact same surface's full geometric integral pairing and both relevant commuting actions were already published in the same basis. The nonsquare model multiplies Frobenius by the published deck action by ordinary quadratic descent. Taking the integral kernels, restricting the pairing and putting the two restricted matrices in Smith form directly extracts the claimed numbers from that stronger exact result. This is documented prior implication, not an assertion that the restricted matrices or both groups were already printed, and not a failure of the computations.

## value

FAIL

The two arithmetic Picard groups are natural and could be convenient as reference data. Here, however, the primitive fixed kernels and their discriminant groups are mechanically determined by exact already-published data on a single lattice, using the standard twist rule and standard normal forms. The record does not establish any additional integral structure not available through that direct extraction, such as a new characterization beyond the input representation. The rational Frobenius and point-count deductions add no separate result of value.

The dated certificate retains the supplied scientific assessment, sources and limitations.

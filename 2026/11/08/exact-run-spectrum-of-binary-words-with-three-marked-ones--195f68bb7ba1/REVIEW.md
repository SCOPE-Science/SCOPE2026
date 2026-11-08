# Scientific review: exact maximal-periodicity spectrum at binary weight three

## Correctness
PASS. The definition uses maximal periodic intervals of least period, not homogeneous zero/one blocks. The key lemma shows that a periodic factor long enough to be a run and containing ones must repeat a primitive block with exactly one one; hence only the two adjacent-marker distances can be periods. The two flank-sum inequalities determine existence, and equal adjacent distances merge the candidate runs. These steps prove the gap formula, while the explicit gap partition proves the rational generating function. The extremal generating function and limiting half-half law follow by exact algebra and coefficient asymptotics. Direct interval enumeration, rational-series coefficient checking and sharp-length checks were independently reproduced from the accompanying standalone code.

## Originality
PASS, subject to normal historical-priority uncertainty. Relevant full primary texts on runs and their unrestricted bounds were inspected, including arXiv:1301.6568, arXiv:1406.0263 and arXiv:1502.04644. Those works focus on unrestricted-alphabet total run length, universal run upper bounds, and Lyndon-root structures. Their claims do not imply a fixed-three-one run-count distribution. Searches for sparse-marker or Hamming-weight-conditioned maximal-periodicity spectra, equivalent formulations, OEIS tables, and existing research records returned no matching theorem. The separate literature on homogeneous-symbol runs is inapplicable, though the shared terminology creates a search risk. Negative searches are not proof of historical uniqueness.

## Value
PASS. The number of maximal periodic repetitions is a standard string statistic, and conditioning on exactly three markers exposes how two different nontrivial periods can coexist with four distinct zero-block runs. The theorem is a natural complete structural classification, determines the sharp extremal threshold at length twelve, supplies every finite-length run-count frequency, and proves a nonconcentrating limiting law. It is not an increment to a numerical table or a substitution into a known unrestricted bound.

## Remaining scope and priority limitations
The classification does not apply to cyclic words, larger marker weights or other alphabets. The historical comparison covers accessible published primary papers and database searches, not all possible unpublished or unindexed material. The mathematical proof is self-contained; the finite checker cannot independently certify historical originality.

Self-review: passed. Independent audit: not yet performed.

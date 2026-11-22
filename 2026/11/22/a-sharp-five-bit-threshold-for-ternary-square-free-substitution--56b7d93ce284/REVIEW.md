# Mathematical review

## Correctness (PASS)
The exact claim concerns a ternary source with **all** contiguous nonempty squares excluded. Full-alphabet single-substitution correction is equivalent to minimum Hamming distance at least three. The 48-word orbit code has all 1,128 pairs checked directly. The seven-orbit rational received-word certificates give total weights 48 and 63/2 at lengths nine and eight, respectively; each source ball has exact weight one. Perfect pairings of the complete length-six and length-seven source sets and the direct shorter counts exclude 32 words below length nine. The included Python checker reconstructs all source sets independently and verifies every certificate without floating-point optimization.

## Originality (PASS, qualified)
Relevant inspected full texts are Currie's 2012 ternary square-free morphism paper, Buschmann and Bystrykh's 2013 barcode error-correction paper, and Przybocki's 2021 delicacy paper. Their objects or conclusions do not imply a maximal family of ternary all-square-free length-nine words at Hamming distance three. The 2016 Gasnikov–Shur wildcard-flexibility chapter was compared only from accessible extracted text after page-image retrieval failed. Indexed published findings on homopolymer-free non-overlapping words have a different feasible family and different decoding property. No equivalent exact table was located, but unindexed historical coverage cannot be excluded; no uniqueness claim is made.

## Value (PASS)
The exact size 48 and the minimum blocklength nine establish a nontrivial finite design threshold for 32 distinguishable messages with single-substitution correction and all-square avoidance. This tests an important constraint stronger than forbidding neighboring repeats. Explicit symmetry-organized constructions and small rational dual witnesses improve reproducibility; no asymptotic conclusion is claimed.

## Boundaries and comparison risk
The result assumes the word boundary is known, works over three symbols, and covers substitutions rather than insertions or deletions. The bound at length eight is deliberately not stated as exact. The original 2016 flexibility chapter was not fully rendered, and older unindexed exact computations may exist. These are limitations of historical comparison, not substitutions for the finite proof.

Self-review: passed. Independent audit: not yet performed.

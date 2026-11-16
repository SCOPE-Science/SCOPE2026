# Scientific review: signed two-vertex path graph-Fourier support

## Correctness — PASS

For the unweighted combinatorial path Laplacian, the cosine eigenvectors are standard and simple. The two-site Fourier coefficient factorization is exact for both relative signs, including frequency zero. The congruence lemma counts each sine and cosine zero class inside the half-open frequency interval. The global bound uses the opposite parity of the sum and separation parameters, and explicitly checks intersections of the sine-zero sets, so it does not double-count roots. In the even case, the only way the even factor contributes its maximal half-frequency set is the reflected-pair equation; the odd factor adds disjoint roots for sums. In the odd case, the largest proper divisor bounds every nonreflected difference, while reflected differences give the sharp equality and a complete gcd classification. Thus the theorem is valid for every integer dimension, not inferred from the exhaustive computations. The independent exact-integer checker passed all 170,640 candidate signals for path sizes 2 through 80; a 90-digit direct cosine check passed 3,542 cases for lengths through 22.

## Originality — PASS, historical priority provisional

The June 27, 2023 graph uncertainty paper studies general graph uncertainty and eigenvector delocalization, not a sharp equal-modulus two-site path minimum. The 2011 path reachability and observability paper gives arithmetic classifications for independently controlled nodes (a multi-column control matrix); those statements do not imply the optimized spectral support of a single signed sum or difference input. Standard discrete cosine identities underpin, but do not themselves state, the all-length sharp minimum with exact signs, gcd conditions and multiplicities. Published research with related names on cycles, weighted paths and multi-input problems was compared by object and quantifiers; no identified theorem dominates this statement. Residual risk: a specialized discrete-cosine-support or coordinated single-input control result may be absent from indexed searches; independent historical priority checking remains necessary.

## Value — PASS

Sharp vertex-frequency uncertainty for a natural low-complexity signal class is directly motivated by graph spectral localization and sensor/actuator design. The result yields a dimension-wide, arithmetic phase diagram: odd-length optimal dipoles, even-length optimal symmetric sums except at pure powers of two, and exact counts of every minimizer. It identifies extremal loss of frequency visibility and the best two-site sparsity in one theorem. This is stronger than enumerating isolated small paths, while correctly limiting itself to binary equal-magnitude inputs and the unweighted combinatorial Laplacian.

## Limits and closest sources

Main antecedents: Rebrova--Salanevich (2023), arXiv:2306.15810; Parlangeli--Notarstefano (2011), arXiv:1109.3556; the standard cosine-transform representation of path eigenvectors. The first treats general graph uncertainty; the second studies independent actuator/sensor nodes rather than one signed combined input. Unindexed antecedents cannot be excluded. The proof does not cover arbitrary two-point amplitudes or weighted paths. No independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.

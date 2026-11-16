# Scientific assessment: involution-matrix Fourier recovery

## Correctness (C): PASS

The exact domain is the additive matrix group \((\mathbb F_2)^{6\times6}\), and the family consists of the 76 symmetric permutation matrices with squared permutation equal to the identity. The character factorization to the 15-bit signed complete-graph matching sum is proved, with a surjective linear reduction of fiber size \(2^{21}\). Integer enumeration of all \(2^{15}=32768\) effective signings gives a 19-level spectrum, 6825 zeros and minimum nonzero magnitude four. An independent vertex-subset recursion agrees on all ordered coefficients (complete spectrum digest in `VERIFICATION.md`). Exact relabeling across all 720 permutations gives 26 zero orbits, including the two minimum-support classes. A second integer Fourier transform proves the stated sharp endpoint norm, rather than sampling it. Checks of both Parseval identities and the edge-support histogram corroborate arithmetic. This finite exhaustive certificate does not assert results for larger orders.

## Originality (O): PASS under bounded comparison

Prior complete-graph matching Fourier work already gives the general matching-polynomial coefficient formula, dyadic gcd and six-vertex singularity; these are background, not claimed as contributions. The new evaluated quantities are the exact six-vertex signed-spectrum distribution, the first zero-support threshold with its two extremizer graph types, the complete 26-orbit zero census and the sharp range-projection endpoint norm. The previously available broader formula is computable at six vertices but does not itself state these evaluated numerical and structural invariants. The 2004 involution-statistics paper, 2014 matching-polynomial reconstruction paper and 2018 signed-complete-graph switching-isomorphism classification were inspected; none of their examined results furnishes the target Fourier cancellation table or projection norm. Switching equivalence in the 2018 paper is strictly coarser and does not preserve the present monomer-dimer sum. Indexed Fourier results for perfect matchings or unrestricted permutation matrices have different supports. Priority remains uncertain relative to unindexed sign-polynomial tables and undiscovered calculations.

## Value (V): PASS

The six-vertex case is the first return to singularity after the zero-free orders four and five. Its full nullspace is a natural spectral invariant, not a random selected submatrix. Identifying the first cancelling signings and both orbit types supplies a genuinely sharp low-support boundary; their complete census and the endpoint projection norm quantify how singularity amplifies data even when the Hilbert inverse-on-range has norm just one fourth. This is a reproducible, exact benchmark for a natural finite graph-based convolution, with mathematical interpretation beyond simply recomputing the involution count.

## Boundaries and closest literature

Prior general signed-matching formulas cover divisibility and singularity existence; do not attribute them to this result. The order-six zero classification and projection constant are finite exact computations; larger orders and independent validation remain outside scope. Dukes (arXiv:math/0412222), Li–Shi–Trinks (arXiv:1404.3469) and Sehrawat–Bhattacharjya (arXiv:1812.08383) were material inspected. Relevant matching/permutation Fourier search records were compared at the statement level.

Self-review: passed. Independent audit: not yet performed.

# Scientific review: prime-field split-torus normalizer Fourier sampling

## Correctness — PASS
The statement defines a concrete set of \(2(p-1)\) matrices and a square ambient Fourier kernel. Its complete block identity follows from entrywise dot products in the two torus cosets. Multiplicative characters diagonalize the scalar-product Hankel block up to inversion, proving the stated singular multiset and determinant product. For odd primes, cyclotomic disjointness makes vanishing of a twisted sum equivalent to constancy of all Fourier coefficients indexed by \(s\in\mathbb F_p\); these coefficients include \(1\) at \(s=2\) and \(0\) outside the image of \(t+t^{-1}\). The two exceptional factors are nonzero by strictness in the triangle inequality. For \(p=2\), direct inspection gives an all-ones matrix. The additional large-prime spectral separation follows from the classical Weil bound for twisted sums. Direct numerical Fourier matrices agree with every predicted singular value for primes \(2,3,5,7,11,13,17,19\), including two additive-character choices at odd primes. Numeric validation is finite and does not replace the proof.

## Originality — PASS under bounded comparison
The closest published reference on determinant-one coordinate Fourier frames restricts *low-coordinate frequencies to the full group*, not all frequencies indexed on both sides by its torus normalizer. A known prime-field full-special-linear Fourier-invertibility statement concerns a different and strictly larger principal matrix, whose invertibility does not imply the present submatrix's invertibility. Li and Hu's full-matrix-group Gauss-sum theorem evaluates Fourier coefficients of a group indicator, not this restricted operator. Conrad's twisted-Kloosterman paper supplies the character-sum estimates, not the two-coset Fourier singular decomposition; Kelmer studies modular twisted sums, not this matrix. Searches of the published mathematical findings, primary literature, and closely related statements found no statement implying the complete normalizer spectrum plus prime-field inversion. Nonvanishing of individual twisted sums may be classical; it is not claimed as a stand-alone new character-sum theorem. Historical completeness is not certified: other nonabelian harmonic-analysis literature might encode the result in different language.

## Mathematical value — PASS
The normalizer of a split torus is a natural Weyl-group extension and a canonical sparse algebraic subset of the determinant-one variety. Exact singular values of the principal ambient Fourier restriction directly control its linear reconstruction and conditioning. The result establishes full invertibility at every odd prime, an exact singular boundary at the prime two, and a rigorously separated pair of spectral outliers for all primes at least nineteen; these are coherent aspects of one complete sampling classification, not an arbitrary numerical slice.

## Closest sources and limits
- K. Conrad, *On Weil's Proof of the Bound for Kloosterman Sums*, Section 4 (twisted sums and bounds).
- Y. Li and S. Hu, *Gauss sums over some matrix groups*, arXiv:1105.4513, particularly Section 2.
- D. Kelmer, *Distribution of twisted Kloosterman sums modulo prime powers*, arXiv:0801.4162 (abstract and first publication date consulted).
- *Four-level Fourier frame spectrum on determinant-one matrices over finite fields*, public result and full theorem/proof consulted.

The proof does not cover extension fields, phaseless recovery, or a uniform upper bound on inverse conditioning. The individual twisted sums are left as exact character-sum expressions. Published results may contain an equivalent presentation not found in the bounded comparison.

Self-review: passed. Independent audit: not yet performed.

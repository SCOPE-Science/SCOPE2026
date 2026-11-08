# Mathematical review

## Correctness — PASS

The prime-power rank-one layer decomposition is disjoint and the primitive-vector factorization has exactly the unit stabilizer. The displayed kernel-orthogonality formula for each layer is evaluated case-by-case in Smith normal form. Summing its cases yields all eigenvalues. The multiplicity proof partitions all frequency matrices, and the signed closed forms imply an exact spectral separation with minimum absolute eigenvalue \(p+1\) at full-rank frequencies. A standalone FFT-based finite checker supplies independent small-modulus consistency checks, not an infinite proof.

## Originality — PASS with historical-priority risk

The archived primitive-vector spectrum of Nica does not give the matrix-additive adjacency spectrum. The accessible full work of Huang (arXiv:1705.07083) and the 2017 Huang–Su–Tang–Wang abstract treat connectivity/parameters and related graph questions without establishing the displayed all-depth Fourier multiset. Delsarte covers matrices over fields. Watanabe's 2026 Smith-type eigenmatrix covers Galois rings of nilpotency length two and therefore may subsume the depth-two specialization; the asserted scope is instead all \(k\ge3\). Guo–Li (2015) provides matrix orbit information with a potentially broad scheme construction but no complete all-depth character table established from accessible material. Full historical priority remains uncertain: the 2017 Huang–Su–Tang–Wang and 2015 Guo–Li texts were inaccessible for decisive passage-by-passage comparison.

## Mathematical value — PASS

The complete character spectrum, its exact Smith multiplicities, and a depth-independent optimal inverse norm describe a canonical growing family of bilinear-forms graphs over residue rings. The result distinguishes the singular and nonsingular frequency classes and gives a sharp quantitative Fourier stability law, not just an incremental numerical bound or an isolated table.

## Limits

Fixed matrix size two; no general finite chain rings beyond integer residue rings. Numerical FFT tests do not prove the infinite theorem; independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.

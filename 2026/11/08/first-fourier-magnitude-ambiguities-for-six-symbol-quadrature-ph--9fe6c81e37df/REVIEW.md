# Review of first Fourier-magnitude ambiguities for six-symbol quadrature phase sequences

## Correctness — PASS
Every QPSK sequence on \(n\) consecutive positions has a unique representative with initial symbol \(1\). The exact program enumerates all \(4^{n-1}\) possible representatives for each \(1\le n\le6\), computes the full Gaussian-integer autocorrelation, and then quotients only by conjugate reversal. Independent polynomial multiplication checks the factored six-term witness. The table yields 540 exact six-length spectral fibers and exactly four doubletons. A coefficient modulation identity sends the one exhibited doubleton through all four. This is a complete finite proof in its stated domain, not an extrapolation.

## Originality — PASS relative to inspected literature
The recent Novikov–Xu arXiv:2604.25662 gives broad discrete Pauli-partner existence constructions, but not the smallest QPSK length or four-fiber census. Katz–Rahman–Ward arXiv:2308.07467 gives general irreducible factor-flipping and an exact table **for binary sequences**, not for all fourth-root sequences; the length-six binary fiber census is empty. The full published RESULT.md of the length-six polyphase base-energy theorem concerns only a scalar sum of squared sidelobes, not equality of all autocorrelations. published-finding corpus queries for QPSK equicorrelation, same-length four-fiber classification, and known aliases returned no stronger matching theorem. An older unpublished or unindexed QPSK classification remains a priority risk.

## Value — PASS
The first nontrivial alphabet-restricted ambiguity threshold is a natural exact identifiability boundary for four-phase communication and diffraction signals. The complete count and one-modulation-orbit structure distinguish the exact Fourier-magnitude fibers rather than a summary statistic. The fact that a binary sequence already has an inequivalent QPSK partner at the threshold is a meaningful boundary phenomenon.

## Limits
Finite full consecutive support of lengths at most six; no claim for incomplete support, arbitrary phases, longer lengths or noise. No independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.

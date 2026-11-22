# Scientific review

## Correctness — PASS

The Parseval scaling is \(n^{-1/2}\) per entry; the row count is \(k=(n-2^m)/2\). The paired Walsh sum evaluates exactly to \(2^m(-1)^{q(h)}\), yielding the three zero-diagonal sign-matrix switching forms. The two-form count is valid for every \(m\ge2\), including independent isotropic triples when \(m\ge3\). The total multiplicity equals \(\binom n4\). The retained lower eigenvalues follow from the four-column nonzero spectrum and the complement identity for the frame operator. All exact finite checks ran successfully from the included code. Remaining limit: no extension to other erasure cardinalities or nonlinear bent functions.

## Originality — PASS within bounded primary-literature comparison

The closest publication, *Equiangular tight frames that contain regular simplices* (arXiv:1711.07081, §7.1), already gives 60 dependent quartets for the sixteen-vector example. That count is explicitly not a novelty claim. *Kirkman Equiangular Tight Frames and Codes* (arXiv:1306.3111, §IV-A) gives spark/RIP obstructions, while *Numerically erasure-robust frames* (arXiv:1202.4525, §§1–2) gives broader frame robustness criteria, not the exact all-\(m\) spectral incidence. The published odd-prime Paley four-column analogue concerns a distinct family. The complete three-type frequencies and sharp erasure-mask counts for the binary quadratic family were not found in the inspected sources. Residual risk: the general symplectic two-graph incidence formulas may have appeared in an unindexed catalogue and may imply the counts with a short spectral translation.

## Value — PASS

Erasure stability is a direct motivation in harmonic-frame design. The theorem determines the exact lower reconstruction bound for all four-erasure patterns, not merely a coherence bound, and quantifies/characterizes all worst patterns for an unbounded family. The distinction between positive-triangle worst masks and negative-triangle optimally benign masks is material, as are the nontrivial multiplicities and the change in the type-C Gram kernel between \(m=2\) and \(m\ge3\). It is not presented as an optimum among unrelated frames or as a full higher-erasure classification.

Self-review: passed. Independent audit: not yet performed.

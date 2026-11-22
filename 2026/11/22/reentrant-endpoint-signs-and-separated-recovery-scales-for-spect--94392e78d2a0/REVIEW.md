# Scientific review

## Correctness — PASS
The four eigenvalues and exact signed spectral-projector entries can be reconstructed directly from the stated four-by-four Laplacian. Strict monotonicity of the scaled distance-two derivative after positive exponential rescaling proves a unique minimum and hence a unique positive zero. Strict convexity of the rescaled endpoint derivative gives at most two critical points, while the exponent-two derivative change and explicit negative values at scaled times \(\log2\) and \(2\) force the exact sign patterns. Positive decompositions cover edge entries, and the constant-vector spectral projector bounds diagonals. Compact-interval convergence at the two different time scales and the exact zero count prove the asymptotic zero locations. The standalone checker passed 1574 independently computed comparisons. The numerical tests do not replace the infinite-parameter proof.

## Originality — PASS, with residual priority risk
Riascos–Mateos (2014), inspected through the lawful full arXiv manuscript (sections on spectral fractional graph diffusion, return probabilities, and conclusion), restrict their stochastic dynamics to \(0<\alpha\le1\) and do not address the superunit-power path sign diagram. Daners–Glück–Kennedy (2015), inspected in full readable HTML (finite-matrix semigroup theorems and applications), establish spectral criteria for eventual positivity, not the exact two endpoint crossings or large-exponent scales here. Published complete-multipartite fractional heat results use a different three-eigenvalue family, and previous four-path mixed heat concerns \(L+\eta L^2\), not \(L^\alpha\). A fixed-graph near-one theorem does not imply the change at exponent two or the two far-separated limits. Search cannot exclude unindexed equivalent exact calculations; absolute priority is not certified.

## Value — PASS
The all-exponent sign classification resolves a concrete structural question at the first ordinary path with four distinct Laplacian eigenvalues. It demonstrates delayed loss of positivity even though the endpoint kernel initially gains positivity, with a rigorously identified exponent-two boundary and a scale separation exponential in the exponent. This is more informative than general eventual-positivity existence, a routine numerical example, or a small perturbation at exponent one; the exact finite network is an interpretable benchmark for higher-power diffusion.

## Scope and verification limits
Only the unweighted \(P_4\) combinatorial Laplacian is classified. No unrestricted graph theorem or independent mathematical certification is claimed. Reproducibility uses `python checker.py` and its ordinary scientific dependencies.

Self-review: passed. Independent audit: not yet performed.

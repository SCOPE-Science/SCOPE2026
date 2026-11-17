# Scientific review

## Correctness — PASS

The proof is reduced without loss to the familiar principal-angle block model. The fixed-sum polytope is exactly \(\{t_j\in[0,1]:\sum t_j=d\}\); the commutator norm is exactly \(\max_j\sqrt{t_j(1-t_j)}\). Both extrema are solved by explicit interval optimization. The lower bound counts coordinates in the two sublevel intervals and proves all equality profiles; the upper bound uses an exact feasible-coordinate interval. Connectedness establishes that **all intermediate** norms occur, not just the endpoints. The integer-cell maxima follow by a unique crossing of two affine functions. A packaged script passed 111,865 finite tests, including 1,800 direct projection matrix checks; the computations are corroborative, not the proof.

## Originality — PASS, with bounded literature risk

The exact joint rank/distance/commutator compatibility band and its integer-valley peak law are not among the results inspected. Aouichaoui's source concerns factorization lengths of arbitrary idempotent commutators; Loring supplies canonical-angle machinery and commuting-approximation bounds, not fixed-Frobenius-distance extrema; Bourin–Lee supplies principal-angle reductions and norms, not the constrained optimization. A 2022 projection-commutator article was available principally via its article-page text rather than full text, so an equivalent old result remains a recognized bibliographic risk. Related indexed findings about Gaussian-Fock projection commutators act in a different, functorially lifted space; their singular values do not imply the same unlifted, fixed-trace band. A search without a match alone is not evidence of uniqueness.

## Mathematical value — PASS

The object is a natural two-projection noncommutativity statistic at a prescribed Grassmannian chordal separation. The answer is a **complete exact attainable region**, not a small improvement to an existing inequality: it distinguishes commuting-compatible integer distances from compulsory noncommutativity elsewhere, exhibits a rank-dependent periodic interior-peaking law, and classifies the extremal angle configurations on both sides of its crossover. It gives an exact obstruction to small commutators from aggregate overlap and is usable for finite-dimensional subspace comparison. It neither presumes the result has applications to every projection problem nor claims optimal estimates in smaller ambient dimensions.

## Closest literature and limits

Primary sources: Aouichaoui (arXiv:2611.01316v1); Loring (arXiv:1306.1923); Bourin–Lee (arXiv:2602.19599v1); Conde (DOI 10.1016/j.jmaa.2021.125650). The latter was not available in full and leaves a bounded residual risk. The rank-saturation classification is new only under the stated constrained optimization, not under a claim that the principal-angle model is new. The checker uses finite tests, with no claim of exhaustive numerical verification over real parameters.

Self-review: passed. Independent audit: not yet performed.

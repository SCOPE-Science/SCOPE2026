# Mathematical review

## Correctness — PASS

The proof derives the exact real and complex Haar-frame representations from independent Gaussian matrices and checks that the Hopf/square edge length equals the row norm squared. The simultaneous covariance bound transfers both extreme tails at once; the independent exact order-statistic formula proves the two endpoint laws and their independence. Multinomial rare-bin Laplace functionals yield the marked Poisson processes. Differentiating the explicit row-norm CDFs and sandwiching the all-edge event gives the claimed compact-threshold error. The packaged numerical script checks finite geometric identities and probability comparisons, not the infinite theorem.

## Originality — PASS, with historical-priority risk

The closest primary work is Cantarella, Deguchi and Shonkwiler, arXiv:1206.3161 (2012), which defines these exact Haar-frame polygon measures and computes single-edge beta marginals; Section 11 explicitly treats independent edges as a simplifying approximation for a rejection sampler. Those statements do not imply the simultaneous lower/upper marked Poisson limits or the stated quantitative all-edge joint probability. Kabluchko and Prochno, arXiv:2110.12977 (2021), prove random-frame large-deviation statements on a different scale, not the two-tail Poisson theorem. A projector-leverage-score formulation is an alias that was searched. Historical priority is not independently certified and analogous fixed-rank projector extreme-value work remains a residual risk.

## Mathematical value — PASS

The independent-edge approximation used in sampling random closed polygons has no a priori justification from one-coordinate marginals because the polygon is closed and its edge lengths sum exactly to two. The theorem provides simultaneous extremes and their spatially marked rare-edge process, differentiating planar and spatial universality classes; it also gives a reusable quantitative error for an all-edge cut-off and practical diagnostic for balanced-edge sampling.

## Scope and limitations

The theorem only concerns unconditioned Haar-induced closed polygons of perimeter two. It does not cover equilateral, embedded, knot-conditioned, or general exchangeable-edge measures. The simulations are diagnostics, not infinite proofs. The independent audit and priority check remain outstanding.

Self-review: passed. Independent audit: not yet performed.

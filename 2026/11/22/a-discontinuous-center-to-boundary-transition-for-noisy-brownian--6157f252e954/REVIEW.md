# Scientific review

## Correctness — PASS
The exact Gaussian conditioning equation is valid with positive denominator. Piecewise integration gives a quadratic numerator in squared displacement and an affine variance. The derivative numerator has derivative \(2(M-z)/3>0\), so every interior stationary displacement is a minimum, not a maximum; the endpoint comparison then identifies *all* optimizers including ties. The critical polynomial has exactly one root in the allowed width range. An independently written checker rederives the covariance integrals, checks the algebra and exact examples, and performs direct numerical quadratures. The proof has no unverified infinite enumeration or finite-case extrapolation.

## Originality — PASS (evidence-qualified)
Nguyen and Peraire's arXiv:1405.7569v1 supplies a general linear-functional Gaussian regression framework; Ji and Müller's arXiv:1604.05375v1 supplies an integrated prediction-error criterion for noisy point measurements. Neither inspected full text states the center-versus-boundary phase law for one Brownian-bridge average. The closest identified Brownian-bridge kernel-quadrature result optimizes a random two-node *integral* estimator, not this continuous-path sensor risk. Related statements about Brownian-bridge two-point placement and Brownian-motion window averaging do not imply this distinct observation-kernel combination or its discontinuous three-optimum transition. A historical path-design dissertation was only catalog-accessible and specialized unindexed work remains a publication-priority risk; absence from search is not proof of priority.

## Value — PASS
Real measurements frequently average a continuous signal over an acquisition window. The theorem gives a complete, exact and usable design phase diagram, including a discontinuous transition and a three-way coexistence boundary; it is not simply an evaluation of one arbitrary window or a substitution into a known point-observation formula. The transition also demonstrates that the endpoint pinning of a Gaussian prior can qualitatively reverse the optimal placement behavior of an averaged observation. The width restriction and small numerical advantages in certain regimes are limitations, not a claim of broad engineering dominance.

## Limits and references
The result is specific to a single uniformly averaged Brownian-bridge path, fixed exposure width and independent positive-variance noise. Independent verification and scholarly priority review remain outstanding. Primary comparison references are arXiv:1405.7569v1 (2014), arXiv:1604.05375v1 (2016), Mukherjee's *Optimal designs for estimating the path of a stochastic process* (dissertation catalog), and the published *Unique optimal i.i.d. two-node design for Brownian-bridge kernel quadrature* record.

Self-review: passed. Independent audit: not yet performed.

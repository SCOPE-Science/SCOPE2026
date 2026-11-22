# Self-review

## Correctness — PASS
The exact object is the Minkowski sum of one filled disk and one interval, not a sampled surface. Support additivity gives the Euclidean directional-width formula. The rotationally invariant spherical measure gives the normalization \(\mathbb E\lvert U\cdot v\rvert=1/2\), \(\mathbb E(U\cdot v)^2=1/3\), and \(\mathbb E\sqrt{1-U_3^2}=\pi/4\). An explicit conditional absolute-cosine integral is integrated by parts into complete elliptic integrals, producing the stated second moment. Differentiation yields a strictly positive integral; its sharp endpoint bounds prove the full variance and inverse-stability assertions. Independent deterministic quadrature of the original spherical average and Cartesian sampling from the same support formula passed all 79 diagnostic tests in `verify_oblique_width.py`. Numerical checks are not infinite proof; the displayed analytic argument establishes the quantified result.

## Originality — PASS, subject to historical priority
Finch's 2012 primary paper determines oblique circular-cylinder mean width, whose equality across inclinations is a premise, but not a second-moment formula or a tilt-rigidity theorem. The nearest available published random-width law concerns only right circular cylinders (orthogonal generator); its formula implies the zero-inclination endpoint only. A separate general width-fluctuation law assumes right prisms, not oblique disk-segment sums. The discotope literature gives support-function additivity and facial/algebraic structure, rather than the claimed angular second moment. Web and mathematical-record searches did not uncover a covering general correlation theorem. Those negative searches are not proof of comprehensive novelty: older stereology, Feret-diameter studies, and general Gaussian-width correlations remain residual risks.

## Value — PASS
The classical mean width cannot detect cylinder inclination when radius and generator length are held fixed. This theorem supplies a natural and exact next-order observable: a complete elliptic-integral second-moment profile with strict optimality, sharp finite-parameter stability constants, and one-statistic recovery of the inclination given the two lengths. It closes a concrete observability gap for a classical oblique-cylinder family. The contribution is neither a restatement of the mean width nor merely a special numerical parameter value.

## Limitations
The theorem fixes the disk radius and segment length, assumes isotropic one-dimensional projection directions, and does not reconstruct the three independent shape parameters from variance alone. Only the right-cylinder minimum is attained among full-dimensional bodies; the opposite bound is a planar limit. Historical priority has not been independently certified.

Self-review: passed. Independent audit: not yet performed.

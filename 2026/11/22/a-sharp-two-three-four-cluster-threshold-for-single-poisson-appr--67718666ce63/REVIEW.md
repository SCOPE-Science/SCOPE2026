# Mathematical assessment: cyclic Poisson mixtures and one-component compression

## Correctness: PASS

The exact model is a mean-one circle Poisson kernel; the fitting loss is squared \(L^2(d\theta/(2\pi))\) distance over every radius \(0\le s<1\) and every angle. The proof first uses absolute Fourier convergence to derive the exact one-variable objective and to prove that any positive-radius optimum must be aligned with a source. For \(m\ge4\) an explicit strict positive lower bound proves uniform optimality; for \(m=2\) a monotone stationary ratio gives the sole nonuniform optimizer; for \(m=3\) a single-hump cubic gives the global coexistence threshold and a separately proven one-turn property of the derivative ratio excludes multiple positive-radius minima. Critical expansions follow from the exact formulas and a nondegenerate implicit branch. The standalone code independently checks Fourier error against direct integration (10,802 finite assertions), critical identities and numerically sampled regions. These checks corroborate but do not substitute for the analytic proof.

## Originality: PASS (best knowledge; independent priority unconfirmed)

The closest motivating preprint, Golzy–Markatou (arXiv:1803.04485v1), proves identifiability and develops Poisson-kernel mixture clustering, but the inspected Sections 3–5 and appendix framework do not solve a single-component squared-\(L^2\) best-approximation problem. Chaubey (arXiv:1601.05053v1) develops Poisson-based circular density smoothing, kernel-estimator identities and orthogonal-series estimators, without the equal-orbit nonlinear projection classification. Baringhaus–Grübel (DOI 10.1007/s00362-023-01393-5) establishes discrete mixture representations and relevant wrapped-Cauchy Fourier identities, rather than minimizing the one-component \(L^2\) risk over radial concentration and direction. Previous related radial-mixture projection work uses concentric positive radius mixtures, whose first Fourier coefficient is positive; here the cyclic orbit has zero coefficients up to frequency \(m-1\), causing a different aliasing and optimizer transition. The resulting threshold statements and global implications were not located among the specifically queried indexed mathematical findings. A negative literature search is not proof of novelty; specialist historical comparison remains a risk.

## Value: PASS

A population approximation problem from circular directional-data analysis has a complete exact answer for every number of equally spaced components. The change from continuous bifurcation with two sources to first-order coexistence with three, and to an absolute uniform-projection barrier with four or more, is a qualitative family-wide classification, not a table entry or a small constant improvement. It also gives an exact criterion for whether compressing a symmetric Poisson mixture to one concentrated component can lower its integrated squared error, with sharp critical gains and exhaustive optimizer geometry.

## Limits and residual risks

The loss is \(L^2\), not likelihood, Hellinger, Wasserstein or relative entropy. Component weights and radii are equal, angular locations form a regular orbit, and the source radius is strictly below one. Results for those different settings do not follow. Published harmonic identities are used as foundations; their existence does not independently establish historical priority of the exact three-regime compression theorem.

Self-review: passed. Independent audit: not yet performed.

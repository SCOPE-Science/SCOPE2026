# Review of exact face-vector law and uniform-square exponent for affine sections of regular simplices

## Correctness — PASS

A generic hyperplane separates \(k\) and \(n-k\) vertices and intersects precisely the faces supported on nonempty subsets from both sides. The section face lattice is \(\Delta_{k-1}\times\Delta_{n-k-1}\), including the one-versus-rest boundary case. Correct invariant hyperplane sampling weights normals by their available offset length, not uniformly. Gaussian radial independence cancels exactly in the rank probabilities and Crofton vertex expectation; Gaussian maximum and binomial tail bounds control the limit. The change-of-measure density is nonnegative, has mean one, and tends to one in probability, hence in \(L^1\). The independent checker corroborates the finite ranks, face-vector formula, and log-exponent trends; the infinite assertions are analytical.

## Originality — PASS (provisional priority)

The closest lead source, Brandenburg–De Loera–Meroni, arXiv:2304.14239 (2023), classifies affine hyperplane slicing chambers by intersected edges but does not derive probabilities under invariant hyperplane measure or high-dimensional face-count exponents. König, arXiv:2002.10743 (2020), treats fixed-distance non-central volume/perimeter extrema. Known Crofton linearity and Gaussian maximum results imply the mean vertex count more readily than they imply the exact full law and the uniform-square joint limit; the mean alone is not presented as the original result. Closest indexed central-section results require an offset fixed at the centroid, a different sampling law. Small-offset Gaussian or chi-square face-vector theorems address \(t_n=c/\sqrt n\) or smaller offsets, not typical invariant-affine offsets of order \(\sqrt{\log n/n}\). Equivalent older integral-geometric formulations remain a historical-priority risk; an older same-object paper by J. Philip (1972) was identified but not inspected in full.

## Mathematical value — PASS

The complete finite probability law and the nonconstant continuum of polynomial growth exponents form a natural classification of random affine-section complexity for all regular simplices. The contrast between typical section size and expected section size is structural and mathematically informative, not an arbitrary numerical refinement. The entire fixed-dimensional face-vector hierarchy is coupled through one explicit random exponent.

## Limitations and sources

Proof addresses fixed face dimensions as the number of simplex vertices grows, for an invariant affine-hyperplane sampling law conditioned on hitting the simplex. It excludes higher face-rank scaling, general polytopes, convergence rates, and exhaustive historical-priority certification. Main sources: arXiv:2304.14239; arXiv:2002.10743; arXiv:1511.08479; Baryshnikov–Vitale (1994), DOI 10.1007/BF02574000. The separate original-source inspections, aliases, and residual risks appear in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.

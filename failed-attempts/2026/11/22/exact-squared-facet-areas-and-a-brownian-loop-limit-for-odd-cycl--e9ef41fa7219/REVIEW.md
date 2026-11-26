# Independent mathematical audit

## correctness

PASS

A facet needs at least n−1 active signed roots. All n cannot be active since the sum of an odd number of ±1 potential increments cannot be zero. The remaining increment is an even integer of absolute value at most one, hence zero. Each omitted edge and balanced sign sequence gives one simplex. Its cone from the origin is a signed path-root simplex with incidence Gram determinant n, so the facet area is sqrt(n) times the normalized normal norm divided by (n−2)!. This is intrinsic Euclidean area. A uniform actual facet gives a uniform balanced sequence; for a squared partial-sum difference spanning d of m=n−1 increments the mean is d(m−d)/(m−1), rather than d for an unconditioned path. Applying the pairwise variance identity and summing over pairs gives (n²−1)/12 for the centered cycle potential norm squared, and twice that for the path. The bridge invariance principle and uniform Riemann sums give the stated centered periodic bridge functional. The periodic Green kernel has paired sine/cosine eigenvalues (2pi k)^(−2), giving the stated Laplace law, mean, and variance. The finite squared normal moment bounds the L² norm of the scaled unsquared areas and so ensures convergence of their means. The surface ratio follows from these means and the central-binomial facet-count ratio. Exact independent Gram computations at n=3,5,7,9 covered 806 facets by cyclic symmetry; mean squares were 2, 5/18, 7/3600, 1/423360. Numerical quadrature yielded ratio coefficient 0.583488362048 at two resolutions (not a rigorous decimal certificate). Replay: python3 /workspace/branches/851041e5-ec06-4497-96da-4631434ad03c/odd_cycle_independent_check.py and adjacent odd_cycle_independent_check.txt. Neither bounded experiment substitutes for the all-size proof.

## originality

FAIL

The earlier November 17 cycle record proves the same typical-facet Brownian bridge law and states the same exact odd-cycle squared normal moment on the same actual facets in the same Euclidean metric. Every odd-cycle facet is itself a facet of the path root polytope obtained by dropping its inactive edge, with identical signed-root vertices and normalized normal. The earlier October path/tree work gives the exact deterministic area conversion for that facet. Normalized squared area is therefore exactly the earlier normalized normal statistic, not a different random variable or new manifestation requiring a new probabilistic result. The separately displayed surface ratio is not stated in the decisive passages but follows from their exact counts, mean/limit results, uniform integrability, and Stirling. No substantive distinct claim survives on that narrower comparison.

## value

FAIL

Uniform-facet geometry on a natural graph family is a worthwhile subject, but this submitted exact moment and limit are a metric renaming of an earlier random statistic by an existing path-facet identity. The half-factor and surface coefficient are directly determined by the earlier formulas. The useful geometric interpretation does not yield an independently unresolved, nonmechanical precise fact in this submission.

The dated certificate retains the supplied scientific assessment, sources and limitations.

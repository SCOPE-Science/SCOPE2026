# Independent mathematical audit

## correctness

PASS

Each old-old-new triangle requires its two new distances to sum to at least 2h, so there is at most one entry below h; a low entry t restricts all other entries to [2h−t,2h]. Each triangle containing both new points is independently checked by K_s at its old coordinate. The four disjoint cases give exactly the distinct-location factor n(n−1) and the same-location factor n; the distinct-location term is absent at n=1. Universality and homogeneity identify the feasible labelled diagrams with types (equivalently, the finite distance diagrams give quantifier elimination by the extension property). For s<h the no-low count is the band (h+1)(2s+1)−s(s+1), maximized at s=h−1, and all exceptional bases strictly miss (h,h). For s≥h the leading base is (h+1)², the largest one-low base is h(h+1) with coefficients h,h+1,h at the left endpoint, interiors and right endpoint, and the remaining ordinary bases are ≤h². Summing establishes the stated prefactor and decay at fixed h. For the endpoint difference, the same-position term has K_h=1 exactly when t+u≥h, while K_2h=0. The distinct-position penalty has b=(min(t,u)+1)²−max(0,t+u−h+1)²>p/h for p=(t+1)(u+1), so n−1≥h makes every two-low contribution strictly negative; at n=1 only the h(h−1)/2 favorable pairs remain. At h=2 substitution gives n·4^(n−2)(7−3n). No unique crossover for general h is proved or needed. The source checker and saved output were read but not rerun; its finite comparisons are only corroboration.

## originality

PASS

The all-even-diameter ordered-pair count, sharp fixed-base exponential rate and finite reversal are distinct on checked evidence. The one-point Katětov criterion is established background, and global concentration of typical metrics and three-distance exact pair counts are not equivalent distributions or parameter regimes.

## value

PASS

This is a complete distance-resolved count over a natural extremal base, not a scan of isolated small cases. It quantifies the rare lower half with an exact exponent and prefactor, and exposes a finite reversal between two channels that are indistinguishable at both leading exponential layers. Those distinctions are not given by a qualitative concentration theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.

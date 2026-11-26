# Independent mathematical audit

## correctness

PASS

For a fixed tuple of r candidate cells, only tuples with distinct rows and columns can occur, at probability 1/(n)_r. Bounded marked rectangles contain n times their areas plus O(sqrt(n)) cells, and forbidden tuples are O(n^(r-1/2)) even when corners share row or column bands. Joint factorial moments and local tightness thus give independent unit-intensity processes at all four corners. Conditional on a sampled cell, the nearest relevant corner has offset sum s<=n-1 and degree or deficit D=s-2K with K hypergeometric. E[D] is at least s/2 by the product bound ab<=s^2/4. If s>4t sqrt(n), D<=t sqrt(n) requires K-E[K]>=s/8; the sample size is at most s, giving exp(-s/32) by Hoeffding, or zero probability if the sample is empty. The union bound for both populations is at most 2n exp(-t sqrt(n)/8). Inside fixed-size rescaled corner squares K is bounded simultaneously by the corner cell count, tight by its bounded expectation, giving a uniform o_P(1) error in scaled degree versus score. The zero-intensity boundary at x+y=t gives the triangle restriction. The exact tagged inversion ordering is continuous at configurations without ties; the Poisson limit has none. For a pair of uniform unit-triangle points, one concordant order has integral of (1-x-y)^2/2 over the triangle = 1/24, so discordance probability is 2/3. A high corner reverses exactly one axis (column for LT, row for RB); the proof's wording about the column in both is an immaterial slip. With lambda=t^2/2, the means are 2lambda^2/3 and 4lambda^2/3, the latter including all cross-high pairs. Bounded moments of corner counts plus the exponentially rare remote event justify convergence of finite-n edge means too. Nested triangles at finitely many fixed thresholds give two independent rate-one processes in squared-score time and the stated rank laws, without asserting independence of ranks within a population. Read verify.py: it tests exact degree formulas, tagged adjacency and two corner factorial moments, not the asymptotic assertions; the latter were independently reconstructed analytically.

## originality

PASS

Credit both the prior extreme-degree localization/diagonal score replacement and the near-identical factorial-moment method for raw corner clouds. The supported distinction is the full joint degree-selected induced graph (all four fields, with cross-population as well as within-population edges) and its graph statistics, not a new Poisson approximation method, inversion rule, or first-rank Rayleigh marginal.

## value

PASS

Vertex-count and first-rank laws do not reveal the subgraph induced by extremes. Equal limiting counts mask a twofold difference in mean edge counts and structural differences such as a complete versus empty cross-corner bipartite graph. The full marking specifies dependencies and cross-population connections rather than offering only another scalar minimum statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

Continuity and the common iid null make all balanced pooled-label words equiprobable. Since each empirical mass is a count divided by n, nρ is exactly the minimum Hamming distance to a fitted binary word with at most q label changes: choose a majority label per cell, or conversely use the runs of a fitted word as cells. This independently proves the universal lower bound because changing one label can erase at most two transitions, and proves the exact zero event R≤q+1. Each isolated 1001001 block contains a central singleton flanked by zeros; flipping it removes exactly two transitions at cost one. Disjoint blocks permit independent edits of ceil((R−1−q)_+/2) such singletons when the stated block-count condition holds. A possible one-transition overshoot is permitted because empty cells are allowed. Under fixed composition a prescribed block has probability (n)_3(n)_4/(2n)_7=2^(−7)+O(1/n), and two disjoint blocks have probability 2^(−14)+O(1/n). Thus Var L_n=O(n) and L_n/n→1/448 in probability. The parity-specific run counts follow from positive compositions; Stirling's formula gives local mass asymptotic (πn)^(−1/2) exp(−(r−n−1)^2/n), uniformly on bounded standardized windows for both parities. The stated run variance n(n−1)/(2n−1) follows by summing transition indicator covariances (adjacent mean product n/[2(2n−1)], disjoint n(n−1)/[(2n−1)(2n−3)]), giving tight tails and the Gaussian limit on scale sqrt(n/2). The deficit is O_P(sqrt(n)), so the exact edit formula applies with probability tending to one. After division by sqrt(n), rounding the number of edits is negligible and yields (Z−t)_+/(2sqrt(2)). The exact zero probability is proved separately by the runs event, not by weak convergence at its atom. Independent evaluation of the binomial runs sum in Python reproduced all five displayed rounded probabilities.

## originality

PASS

The underlying empirical statistic, runs law, and finite combinatorial framework are prior work. The supported distinct contribution is the exact local attainment for the positive overlap cost and its critical growing-q limit. No inspected distinct statement supplies these, including when phrased as binary fitting with a bound on changes. The zero-event transition alone is a direct runs consequence and is not the ground for a pass.

## value

PASS

The cut count is the actual complexity parameter of a published statistic. The result locates the fit-saturation transition, quantifies the extent of exact zero overlap under the common null, and describes the nonzero costs in the same window. The edit construction explains the scale and coefficient rather than merely tabulating zero atoms or reusing the classical run count test.

The dated certificate retains the supplied scientific assessment, sources and limitations.

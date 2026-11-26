# Independent mathematical audit

## correctness

PASS

In the Cartesian representation, a proper interval's minimum-priority key has precisely that subtree iff each existing immediately outside key has lower priority. This gives one-tree probabilities 2/[(k+1)(k+2)] and 1/(k+1); squaring and counting n−k−1 interior and two terminal intervals gives the exact mean, also for k=n−1. On a window [K,LK], intersecting enlarged intervals define dependency neighborhoods. Interior-interior product terms total O(nK·K²·K^−8); terminal-interior and terminal-terminal product terms are O(K^−3) and O(K^−2). Crossing and adjacent pairs cannot occur; nested pairs condition on a fresh relative order inside the larger interval. For a one-key gap, condition on the separator priority t: integrating over one exterior boundary gives t(1−t)^k+(1−t)^(k+1)/(k+1). Integrating the product over t gives O(K^−3) with both exterior boundaries and O(K^−2) with one missing in one tree, then square. Interior-parent edge-nesting and interior one-gap pairs thus contribute O(nK²·K^−6), strictly internal nesting O(nK³·K^−8), and the terminal cases O(K²·K^−4+K³·K^−6); two missing outer boundaries in a one-gap pair are impossible for fixed L and large n. Both dependency-graph error sums vanish at K proportional to n^(1/3). The mean tends by Riemann sum to the stated integral, with terminal mean O(1/K). For a formal point-process check, for each nonnegative continuous compactly supported f on (0,∞), independently retain indicators with probability 1−exp(−f(k/n^(1/3))); the same bounds apply, and the zero-count probability gives the Poisson Laplace functional with intensity 4u^−4 du. Finally the expected count above yn^(1/3) has limsup at most 4/(3y³). Truncation followed by y→∞ gives the stated maximum CDF; the strict lower threshold uses a ceiling. The finite uploaded verifier was read, not executed, and is not needed for the infinite limit.

## originality

PASS

The supported distinct claim is a two-tree, interval-labelled extreme-value and size point-process law. Established one-tree fringe probabilities and standard Poisson approximation are not new. The exact catalogue hit is the assigned record itself. The closest distinct statements cover one-tree size profiles, common clades in a different tree law, or shared direct edges, not this intersection statistic. The comparison does not certify priority.

## value

PASS

The maximum shared descendant interval is a natural measure of agreement between independent randomized hierarchies on the same ordered keys. The exponent and finite mean alone do not identify its law. The Poisson result rules out asymptotically relevant clustering of large shared intervals and gives the exact Fréchet normalization, a useful distinction from the one-tree fixed-size regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.

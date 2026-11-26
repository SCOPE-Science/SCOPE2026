# Independent mathematical audit

## correctness

PASS

Read the sparse scaling along admissible lengths as in RESULT.md's scope and limitations: with integer k it cannot hold along every integer n (successive ratios would force k_(n+1)−k_n eventually zero). For an interior start p=2^(−k−1), and the same-site joint probability q=p(1−ε/2)^(k+1) includes the preceding zero. At displacement 1≤d≤k, same-copy starts exclude each other. One cross orientation forces one specified discordant pair (ε/4), k−d specified concordant ones (t/2 each), and 2d singly specified coordinates (1/2 each), giving r_d=ε t^(k−d)/2^(k+d+2). The other orientation is symmetric; outside distance k the paired blocks are disjoint. With site/type indicators, same-site different marks are mutually exclusive, b₃=0 by disjoint underlying coordinates, and b₁≤9(n−k)(2k+1)p²=o(1). The ordered neighbor contribution is at most 4(n−k)Σr_d. For d≤k/2 the remaining factor t^(k−d)≤exp(−εk/4), and for d>k/2 the geometric 2^(−d) tail is O(2^(−k/2)); multiplying by ε makes both bounds uniformly o(1). AGG Theorem 2 then controls the finite array in total variation. The independent Poisson site's Laplace functional converges by Riemann sums on the compact marked space to the claimed three independent homogeneous components, with shared fraction θ. The chance of an omitted first-site run in either copy is ≤2^(1−k), giving the joint zero-count probability. Summing r_d−p² with multiplicity 2(n−k−d), plus the diagonal, gives the finite covariance; b₂ and b₁ respectively control the shifted joint and product terms. VERIFICATION.md and verify.py were read, not executed.

## originality

PASS

Static declumping, general marked Poisson approximation, and run-test dynamical sensitivity are prior work. The supported distinct contribution is the explicit quantitative two-copy extremal location coupling in the sparse lattice window, including the negligible shifted coincidences and the exact critical shared fraction. The finite covariance is not asserted to be a separate novelty.

## value

PASS

A single-copy limit cannot diagnose whether refreshed extreme runs persist at their original locations or merely survive as counts. The three-component limit resolves that distinction with a sharp nontrivial fraction, and quantitatively determines joint longest-run failure in the critical window. This is substantive even though the general approximation machinery is established and the first-ever static longest-run law is not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.

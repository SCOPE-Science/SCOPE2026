# Independent mathematical audit

## correctness

PASS

The tree series-resistance and trace identity gives K=N^(-1) sum_e s_e(N-s_e)/w_e. All edges are positive by connectivity. For fixed bridge z, apply Cauchy–Schwarz to each set of pendant weights and use each hub budget 1-z. Equality requires every pendant weight on each side to be equal and both budgets saturated, feasible here. The resulting strictly convex A/(1-z)+B/z has the stated unique root and value without an orbit assumption. For fixed total s, the derivative of sqrt((s+2)K_*) in u=pq is negative because 4(s+1)(u+s+1)-(s^2-2u)>0; fixed sum and product determine the unordered pair. Independently checked the SLEM comparator: the orthogonal Rayleigh vector with hub values +1,-1 and leaf values +(1+sqrt(2)),-(1+sqrt(2)) forces the lower bound 1-2/D_k since its Laplacian energy is at most 4. Equality forces saturation and the individual leaf eigenvector equations, fixing each weight. The candidate spectrum on the orthogonal subspace has Laplacian eigenvalues a_mix (leaf contrasts), (k+1)a_mix (symmetric quotient), and 2/D_k and (2+sqrt(2))z_mix (antisymmetric quotient); all lie in [2/D_k,2-2/D_k], so that bound is sharp. The two comparator Kemeny costs follow directly from the tree formula; the exact gap certificate was verified separately by rational-polynomial reduction modulo u^2-2 with u=sqrt(2), using `python3 -B /workspace/review_evidence/kemeny_checks.py`. Its positive factors give strict reversal for k>=2 and zero at k=1. Lastly A_k~2k^2 and B_k~k/2 give the bridge asymptotic and K_*~2k^2; the two comparator leading coefficients are 2+sqrt(2) and 5/2. The convention excludes the stationary eigenvalue; symmetry fixes uniform stationary mass, not uniform edge weights. Frozen script inspected, not executed.

## originality

PASS

The supported distinction is the explicit unrestricted double-star Kemeny design, fixed-size shape comparison, and exact Kemeny reversal against the old SLEM optimum. The SLEM weights and uniqueness are credited outright to their prior statement, as are the general design and resistance machinery. The nearby cross-objective analyses and weighted-tree walk results do not cover the double-star Kemeny claim.

## value

PASS

The unique optimal conductances and fixed-order shape comparison address an entire natural family under the actual vertex budgets. The SLEM-optimal walk being worse for Kemeny than a standard maximum-degree heuristic for every balanced size is a useful boundary between two design objectives, supported by precise bridge scales and limiting losses. This is materially stronger than stating merely that the two minimizers differ.

The dated certificate retains the supplied scientific assessment, sources and limitations.

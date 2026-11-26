# Independent mathematical audit

## correctness

PASS

For an order-d rotation, independent domain bits on d-cycles give acceptance a_d=(1−2^(−d))^(n/d); after acceptance the orbit counts are independent truncated binomials. The audited repair replaces the orbit laws one at a time. Each replacement has mass p=2^(−d) times the effect of shifting the independent remaining sum by at most d. In short orders 2≤d≤ceil(3 log2 n), the other m−1 blocks have independent first bits with zero probabilities at least 1/2. Chebyshev bounds the chance of fewer than (m−1)/4 zeros by 4/(m−1)=O(d/n). Each zero leaves d−1 independent fair bits even in an already-conditioned block. Conditional on these first bits and the other blocks' counts, the sum on the good event contains at least n/16 fair bits for large n. A step-one shift of this unimodal binomial costs its maximum mass O(n^−1/2), so the d-shift and bad event cost O(d/√n). Telescoping gives O(m p d/√n) per order, and its weight a_d≤exp(−mp) cancels the growth in mp. Summing φ(d)d/(n√n) gives O(log³ n/n^(3/2)). Order one contributes at most 2^−n/n, and long orders at most n^−2 in total by a union bound. The mixture normalization tends to 1, the distinct-map correction within rotations is only for the empty map, and reflection-only additions are at most n·3^(n/2); both changes are exponentially negligible. The monoid size 2n·2^n−O(n²) gives half density with the stated error, and TV transfers the binomial CLT.

## originality

PASS

Final claim only: the strongest exact Resultary prior gives the same rank polynomial from a joint transfer law, but supplies no quantitative rank-distance estimate of the repaired strength. The repaired TV bound makes new use of acceptance-weighted block smoothing, rather than using structure, total enumeration, or a global bound on rejected restrictions as an approximation by itself. No equivalent bound was found in the inspected material; this is best-of-knowledge, not absolute priority.

## value

PASS

Uniform domain-rank approximation in a natural nilpotent subpopulation controls every event in the rank, not merely a centered CLT or the total density. The repair separates rank bias from the larger rejected-presentation mass and gains a factor of order √n/log n over the frozen estimate for all cycle lengths, including lengths with many short-order rotations. The improvement depends on an actual structural smoothing argument, not on relabeling the previously counted finite spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.

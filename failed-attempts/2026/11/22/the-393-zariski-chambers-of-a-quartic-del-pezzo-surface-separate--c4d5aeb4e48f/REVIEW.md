# Independent mathematical audit

## correctness

PASS

Adjunction and anticanonical ampleness force any geometric negative irreducible curve to be a (-1)-curve. The five-point blowup gives the stated 16 curves, with pairwise intersections 0 or 1. Negative definiteness is exactly disjointness. Conversely, contracting a disjoint set and taking a pullback of an ample class plus small positive multiples of those curves gives a big class with precisely that negative support, with a full-dimensional chamber by openness of ampleness on the contraction and of the positive coefficients. This argument uses no characteristic-zero restriction. The intersection graph is the folded cube: its five neighbors of zero determine the full automorphism group (the other ten vertices are determined by distinct pairs of neighbors), and the even translations and coordinate permutations realize all 1920 automorphisms. The Weyl action is faithful because the curve classes span the Picard group. Independently using F_2^5 modulo the all-ones vector, I enumerated conjugation orbits of the actual 16-vertex permutations, computed invariant supports on the conflict graph of curve cycles, and inverted fixed counts of powers to recover the chamber cycle multiplicities. It matches every column of all 18 rows of spectra.csv, including the 393 supports, 18 distinct chamber spectra, 12 distinct line spectra, ten rational counts, and both collision examples. Replay: python3 /workspace/audit_evidence/chambers.py <frozen spectra.csv>. Mobius inversion on extension counts gives exactly the finite etale zeta reconstruction, not reconstruction of X. Trepalin arXiv:1803.07421v1 Thm. 1.4 and §6/Table 4 were read: the stated exclusions are only over F_2 and F_3. Although his type is a cyclic subgroup conjugacy class, all generators of a given cyclic subgroup of W(D_5) are conjugate: a coprime power preserves the permutation cycle lengths and each negative cycle's parity (its signed order is even), and these signed types are the verified element classes. Thus realization of all 18 for q>=4 follows as written; the ten counts are the overall possible values, not a realization claim for each of q=2,3.

## originality

FAIL

A distinct same-day Resultary finding 5213a9a0047f explicitly covers all 393 chambers and eighteen exact Frobenius orbit profiles, one per signed W(D_5) type, with extension counts. The inverse-zeta phrasing is mathematically the same complete orbit invariant; the line-cycle comparisons are straightforward comparisons against this classification and the standard 16-curve action. The failure is substantive overlap of stated findings, not a claim about same-day priority, an exact match of proof text, or a conclusion based on inaccessible files.

## value

FAIL

The finite-etale chamber invariant itself is natural and strictly refines the exceptional-line permutation data, so the underlying result is useful. However, the exact invariant and its separation are already covered by the distinct all-types classification, and the remaining line-zeta comparisons are derived from those data. The frozen record does not isolate a distinct scientifically useful gap beyond the covered result. No repair is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.

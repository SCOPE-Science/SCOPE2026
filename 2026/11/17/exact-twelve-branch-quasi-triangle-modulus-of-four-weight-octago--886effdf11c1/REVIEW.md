# Self-review: exact four-weight octagonal quasi-triangle modulus

## Correctness — PASS

The specified generators are fixed, including the unnormalized diagonal directions, and all four nodal weights are strictly positive. A planar supporting segment proves equality between the optimal two-summand quasi-triangle modulus and the maximum of the gauge over the convexified unit ball. The eight radial vertices then reduce this maximum to twelve explicit chord-ray intersections and the vertex value \(1\). The exhaustive list is independently verified by orientation determinants; all twelve terms have exact strict-maximizer witnesses. The argument covers arbitrary real positive parameters, not only integer tests. The standalone rational checker reproduced the hull geometry for 4,096 octagonal parameter tuples, verified twelve strict witness inequalities, and ran 1,728 hexagonal control cases. The finite tests supplement rather than prove the universal identity.

## Originality — PASS, with explicit bibliographic risk

Unser's 2026 article establishes the conic-spline parametrization and nodal polygon geometry, and a general existence/upper-bound result for quasi-triangle moduli. Its inspected Sections 2, 3, 5, and appendices contain neither the sharp four-weight formula nor an equivalent full irredundant twelve-branch classification. Earlier convex-envelope theory supplies the gauge of a convexified ball; earlier quasi-Banach work supplies the modulus terminology. Neither directly implies the twelve explicit terms without a new geometric reduction and crossing classification. Related published octagonal-Banach-plane records address *different* invariants on convex normed planes, and a published planar convexification record studies a different Minkowski-sum threshold. General planar supporting-face geometry itself is not claimed as new. The full 1986 Banach-envelope paper was not obtained, and an unindexed equivalent piecewise-linear optimization may exist.

## Mathematical value — PASS

The optimal quasi-triangle coefficient is the natural quantitative stability parameter controlling a nonconvex quasi-norm. The result solves it **for all positive values of four independent conic-spline coefficients** on the first uniform planar fan with four antipodal pairs, not a one-off numerical instance. All twelve alternatives are essential, which establishes a genuine parametric classification of competing nonconvex extremizers. The exact positive-weight formula can be used without computing a polytope hull or optimizing an infinite family of two-vector pairs. It also separates the sharply optimal coefficient from the generic upper bound based on comparison with a norm. The finding makes no higher-dimensional or arbitrary-fan claim.

## Closest literature and limitations

- M. Unser, *Quasi-norms on \(\mathbb R^d\): Characterization and Approximation by Conic Splines*, arXiv:2611.06212v1 (2026-11-04), Sections 2, 3, 5 and Appendices A–C.
- N. J. Kalton, *Banach Envelopes of Non-Locally Convex Spaces*, Canadian J. Math. 38 (1986), DOI:10.4153/CJM-1986-004-2 (abstract examined; full text not examined).
- *On Perfectly Homogeneous Bases in Quasi-Banach Spaces*, Abstract Appl. Anal. (2009), DOI:10.1155/2009/865371 (terminology and introduction examined).

The scope is restricted to strictly positive nodal weights on the stated eight rays in a real plane. Potential equivalences in less searchable polyhedral/quasi-Banach literature remain a residual priority risk. The checker does not establish an infinite-parameter result by itself.

Self-review: passed. Independent audit: not yet performed.

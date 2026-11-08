# Review: angular-sum optimization for right-corner tetrahedra

## Correctness — PASS

All tetrahedra are parametrized, up to similarity and arm permutation, by the single continuous parameter \(t\in[1,R]\) once \(R>1\) is fixed. The spherical-excess computation gives the normalized total solid angle without assuming any unproved identity. Its derivative has the explicit sign of a strictly increasing function minus a constant; the two endpoint comparisons are strict and equivalent to \(R>1\). Thus the stationary point exists, is unique, lies in the interior, and is the global minimum. The degeneration estimates derive both the cube-root intermediate arm and the fractional-power correction using uniform elementary expansions along the proven scale. Independent determinant-based angle evaluations in `verify.py` corroborate the closed identity and numerical root behavior; they are not the proof.

## Originality — PASS (historical priority provisional)

Licht (2026) proves geometric-comparability bounds for the **smallest individual** solid angle and recalls a general total-angle bound; he does not state the fixed orthogonal-arm ratio optimization. Kabluchko–Schange (2025), Theorem 8.5, gives **individual** internal and external angle integrals for rectangular orthocentric simplices but does not classify the unique anisotropy-constrained angular-sum minimizer or its fractional-power asymptotics. The classical spherical angle sum formula is acknowledged as input. Targeted mathematical-record searches for the constrained tetrahedral angle-sum extremum, its root equation and its cubic balancing law returned related tetrahedral invariants but no equivalent assertion. The accessible historical geometric records, especially older tetrahedral angle-measure literature, may not be exhaustive; historical priority is not independently certified.

## Mathematical value — PASS

The result solves a natural complete one-parameter shape-optimization problem suggested by recent investigations of solid-angle shape measures. The sum of vertex solid angles is a standard angular-geometric invariant and differs essentially from the previously studied minimum individual solid angle. The minimizing intermediate arm is strictly interior for every nontrivial anisotropy, showing that neither symmetric two-equal-arm endpoint minimizes. Its sharp scaling \(R^{1/3}\) and fractional asymptotic \(R^{-5/3}\) expose a genuine competition among the three facet-normal components that would not be deduced from a coarse regularity bound. The solution supplies an exact computable scalar equation, uniqueness and leading correction, rather than a numerical optimum for arbitrary parameters.

## Closest work and limitations

The two primary sources are Licht (arXiv:2610.05883v1, 2026) and Kabluchko–Schange (arXiv:2505.05048v1, 2025); Liu–Joe (1994) concerns related tetrahedral shape measures. Formula (1) is classical, and the broader angle formulas of Kabluchko–Schange are not new here. The result is limited to three-dimensional right-corner tetrahedra and the ratio of their perpendicular arms. It does not characterize maxima, arbitrary tetrahedra, or historical uniqueness in all literature.

Self-review: passed. Independent audit: not yet performed.

# Independent mathematical audit — 2026-10-01

## Final claim assessed

For every closed connected Riemannian n-manifold with n>=2, every sufficiently dense compact subset A satisfies Gromov--Hausdorff distance(A,M)/Hausdorff distance(A,M) >= c_n-O(Hausdorff distance(A,M) to the power 2), and the local infimum of this ratio tends to c_n=sqrt((n+1)/(2n)); deleted geodesic balls give matching asymptotic upper examples.

## Correctness — PASS

The scale calculation is correct. Rescaling g by (delta/h) to the power 2 multiplies both metric distances by delta/h, sends the sectional-curvature upper bound to kappa_+ h to the power 2/delta to the power 2, and sends the convexity radius to infinity on the rescaled scale. Applying Adams--Frick--Majhi--McBride Theorem 4 then yields the displayed alpha_n(kappa_+ h to the power 2/delta to the power 2) lower coefficient once the second branch is nonbinding. Independently expanding the source alpha factor gives 1-(pi to the power 2/24)q+O(q to the power 2), hence a cubic error in unnormalized distance. The earlier deleted-ball theorem supplies the matching upper family.

## Originality — FAIL

The claimed lower modulus is a direct rescaling corollary of the published Adams--Frick--Majhi--McBride theorem, which is stated for every closed Riemannian manifold and every subset and already gives the curvature-dependent Jung coefficient. Metric scaling and curvature scaling mechanically replace kappa by kappa h to the power 2/delta to the power 2. The matching deleted-ball upper asymptotic was already published in SCOPE on 2026-09-18. Thus the final local-infimum statement is implied by prior results rather than an independent theorem.

## Value — FAIL

The local sharp constant is a natural quantity, but under the required value bar this record adds only a routine rescaling/Taylor deduction from an existing theorem plus an already published extremizing family. It does not isolate a new nonstandard lemma or unresolved invariant once those inputs are known.

## Source inspections and risks

- **Hausdorff vs Gromov-Hausdorff distances** (arXiv:2309.16648): Full arXiv HTML: Theorem 4 setup, alpha(n,kappa), tau, proof lines showing d_GH >= alpha d_H under the density threshold, and Section 7 Jung machinery. Assessment: COVERING_BY_IMPLICATION.
- **Universal cubic-error Gromov--Hausdorff asymptotic for a deleted geodesic ball** (SCOPE 2026/09/18/small-hole-gromov-hausdorff-cubic-asymptotic--a0d57fbb476f): Complete RESULT.md from audited Git snapshot. Assessment: COVERING.

Residual risks: No contradictory correctness evidence was found. The originality rejection uses implication, not absence of matching wording.

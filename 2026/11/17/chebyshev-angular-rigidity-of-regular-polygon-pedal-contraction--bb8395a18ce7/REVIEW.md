# Review: Chebyshev angular rigidity of regular-polygon pedal contraction

## Correctness — PASS

The proof starts from the previously established exact product of pedal scale factors, not a numerical approximation. With the circumradius normalized to one, side lines have signed offsets \(c-\rho\cos(\phi-\alpha_j)\). The Chebyshev root-product identity gives the numerator, and the roots-of-unity identity gives the denominator. Their positivity on the exact interior domain makes the derivative with respect to \(\cos(n\phi)\) strictly positive, proving the complete angular classification including boundary cross-sections. The expansion is uniform in angle and the first nonradial term has strictly positive coefficient \(c^n+2^{1-n}\). The proof isolates nondegenerate pedal iterations from the everywhere-defined scalar extension. A standalone recomputation checks 2,865 finite identities and actual iterations; these are supplementary, not a substitute for the infinite proof.

## Originality — PASS, subject to historical priority

Primary literature inspected: Michał Zwierzyński, *When Pedal Shapes Come Back: a Complex Story*, arXiv:2611.01247v1 (2026-10-31), eight-page full text, especially Theorem 2.2 and Corollary 2.3. It establishes the general product and central optimum; those are excluded from the originality claim. It does not state the complete off-center Chebyshev profile, strict circular angular rigidity, exact angular gap, or the first anisotropic Taylor coefficient. These are obtained by a nontrivial specialized factorization and monotonicity argument. published-finding corpus comparisons for angle-dependent pedal contraction, regular-polygon roots, and related Chebyshev aliases retrieved closest but different results: *Exact harmonic–arithmetic contraction for regular polygons* (index ID `1a7b93dcfbad`) treats Minkowski symmetrization; *Sharp affine least-squares projection norms on regular polygons* (index ID `ac0c9cd53708`) treats affine orthogonal projection, not pedal iteration. Unindexed classical product identities or pedal-transform calculations remain the principal historical-priority risk.

## Mathematical value — PASS

A new global contraction theorem bounding only the center does not resolve how a displaced pedal point changes the scale. The result closes this natural angular optimization problem for every regular polygon and every radius, identifies the two sharp symmetry orbits, gives their exact gap, and detects the unusually delayed onset of anisotropy at order \(n\). These are structural facts about a natural recently studied dynamics, not a computation on arbitrarily selected polygon sizes or isolated numerical examples. The result does not pretend to settle irregular polygons or all nondegeneracy issues.

## Scientific limits and sources

Zwierzyński [arXiv:2611.01247v1], Theorem 2.2 and Corollary 2.3 (the general similarity product and global bound), https://arxiv.org/abs/2611.01247. Standard Chebyshev and roots-of-unity identities are prior facts. Historical uniqueness cannot be inferred from a database search. The exact statements concern regular polygons and an interior pedal point; boundary values represent a continuous scalar extension.

Self-review: passed. Independent audit: not yet performed.

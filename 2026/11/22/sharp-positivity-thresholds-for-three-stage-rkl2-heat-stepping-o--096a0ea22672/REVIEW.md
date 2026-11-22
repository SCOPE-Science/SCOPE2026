# Scientific review

## Correctness

**PASS.** The theorem specifies the exact symmetric unit-conductance graph Laplacian, the completed three-stage RKL2 stability polynomial, all nonnegative stepsizes, and all integer bipartitions. The Laplacian has four explicitly identified eigenspaces. Their projectors yield the cross-class entry, two within-class entry factorizations and diagonal formulas. The scalar Legendre bound gives \(1/6\le r(t)\le1\) on \([0,5]\); strict decrease beyond five gives the sole later roots. For \(2\le p\le q\), the first sign change is the within-small-class off-diagonal. For stars, a rigorous bound \(\tau_q<45/8\) puts the hub-diagonal zero strictly before the leaf-pair zero. For \(K_{1,1}\) the scalar bound determines both transitions. A largest-eigenvalue argument gives the spectral norm threshold. The independent exact-rational matrix checker returned `VERIFY_OK 52755`, supporting but not substituting for the proof.

## Originality

**PASS, with qualification.** The 2026 source describing RKL2 proves maximum principles in a distinct one-dimensional grid context and explicitly cautions about higher-dimensional monotonicity. A published three-state RKL2 positivity analysis concerns a nonsymmetric pure-birth Markov generator and proves reentry, not any complete-bipartite cutoff. A published all-multipartition Taylor Runge–Kutta classification concerns a cubic coefficient \(1/6\), whereas the present RKL2 coefficient is \(1/15\): its cutoffs are not instances of these formulas. Searches for complete bipartite RKL2 positivity, star thresholds, and equivalent polynomial graph-heat formulations did not reveal a dominating result. Residual priority risk remains, particularly specialist literature not indexed by the searches.

## Value

**PASS.** Positivity of graph heat flow is a basic physical and maximum-principle property, while standard Euclidean stability alone cannot guarantee it. This theorem gives a *complete sharp* nonnegativity range on a natural two-class family for a recently studied stabilized explicit method, identifies two different first obstructions (stars versus nonsingleton classes), and quantifies the loss from scalar stability, with an asymptotic stability-to-positivity gap. It provides a testable exact benchmark when applying stabilized time stepping beyond one-dimensional grids.

## Limits and nearest literature

Only completed steps on uniformly weighted complete bipartite graphs are covered; no nonlinear stage positivity or general-graph assertion is made. The nearest inspected papers are Tan–Aslam–Bertozzi (arXiv:2611.16238v1), its earlier related analysis (arXiv:2507.17062), the three-state RKL2 Markov result, and the complete-multipartite Taylor–Runge–Kutta result. Historical priority has not been independently certified.

Self-review: passed. Independent audit: not yet performed.

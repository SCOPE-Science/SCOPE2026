# Review: universal logarithmic invasion clock

## Correctness — PASS

For every integer \(r\ge2\), common positive coefficient, and strictly positive initial vector, the normalized map is exact. The key decompositions are \(p_i=(1-z)u_i\), resident variance \(E=\sum(u_i-1/r)^2\), and the exact reciprocal relation
\[
\frac1{z_{n+1}}-\frac1{z_n}
=\frac{2r+1}{2(2r-1)}\frac{1-z_n}{1-z_n/2}
-\frac{(1-z_n)^2E_n}{2h z_n(1-z_n/2)}.
\]
The proof uniformly separates the rare share from one, establishes resident equalization at an exponential rate independent of the rare-share limit, proves rare-share extinction and a linear upper bound on its inverse, and hence shows the variance error has a summable total. The inverse increments first give the sharp leading \(1/n\) law; a second summation establishes the **finite** renormalized limit after adding half a logarithm. There is no appeal to numerical trajectories for an infinite-time conclusion. Rational identity checks and longer-iteration experiments passed with the actual standalone checker.

## Originality — PASS within inspected evidence

The 2024/2025 originating article treats this same quadratic operator but does not quantify the multiple-resident critical tie. The closest published general result (*An exact global separatrix and water-filling convergence for a positive quadratic map*) establishes global convergence to a water-filling composition but explicitly leaves finer convergence rates at ties open. *Universal critical algebraic exclusion in a many-type quadratic population map* establishes a leading inverse-time law for one dominant resident and multiple subordinate types at coefficient ratio two; exchanging labels cannot create this theorem's \(r\) equal dominant residents, single neutrally invading type at ratio \(2r/(2r-1)\), or the logarithmic second term. The geometrical radial-separatrix result concerns a different, strict-positive-interior parameter chamber. Exact published-finding corpus overlap queries and primary literature were checked at the claim-implication level, not by title alone. Unindexed parabolic-map or replicator literature may contain an equivalent formula; this remains a publication-priority risk.

## Mathematical value — PASS

The operator is a natural discrete population-interaction model, and the invader's threshold is the geometrically distinguished water-filling boundary where its linearized growth factor equals one. A first-order \(1/n\) decay does not determine the systematic finite-time bias; the dimension-independent \(-\frac12\log n\) term gives the first nontrivial correction for every positive trajectory and all resident multiplicities, despite initially unequal resident coordinates. This is a precise, structurally motivated dynamical asymptotic rather than an arbitrary parameter sample or numerical recomputation.

## Limits and related literature

Only relative compositions are covered; absolute biomass can go extinct or escape with initial mass. No uniform estimate over nearly extinct initial resident types or heterogeneous resident weights is asserted. There is no independent audit. The closest inspected prior sources are Shoyimardonov–Rozikov (arXiv:2409.13450; DOI:10.20537/nd250803), *An exact global separatrix and water-filling convergence for a positive quadratic map* (2026), *Universal critical algebraic exclusion in a many-type quadratic population map* (2026), and *A computable global extinction–escape separatrix for a homogeneous quadratic population map* (2026).

Self-review: passed. Independent audit: not yet performed.

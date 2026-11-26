# Independent mathematical audit

## correctness

PASS

The reciprocal biomass map is affine with positive intercept and two-step slope 1/(r₀r₁S). For positive initial data this gives attraction to a unique positive cycle iff Q>0 and extinction otherwise, including linear growth of reciprocal biomass at Q=0. Solving the affine cycle gives the supplied two biomasses; post-recruitment catch equals (1−s_i)x_{i+1}/s_i. Write N(t)=K₁+r₀K₀t and D(t)=r₁SK₁+K₀t. The derivative of normalized catch has the sign of R−N/D, and (N/D)'=QK₀K₁/D²>0. Thus the two clipped cases and the unique interior critical point include endpoint derivative equality; in the interior r₀−R=QK₁/D(t*)>0. For regret, set L=K₀+r₁SK₁ and H=(K₁+r₀SK₀)/S. The normalized yield difference between t and t* is (t−t*)[H/(N(t)N(t*))−L/(D(t)D(t*))]. Insert H/N(t*)²=L/D(t*)² and use N(t*)D(t)−D(t*)N(t)=−QK₀K₁(t−t*) to recover the exact strictly positive prefactor of (t−t*)². The regret identity is for interior t* only; uniqueness is only for Q>0. Independent bounded arithmetic gives 44/7 versus 3.746394253408705 in the endpoint example.

## originality

PASS

The underlying periodic recurrence, persistence machinery and unconstrained periodic yield problem are prior work. The inspected closest harvesting theorems either allow the total proportional effort to vary or optimize additive quotas under a different feasibility constraint. The supported distinct claim is the fixed-product constrained optimizer, including both corner regimes, and exact interior regret. This is a bounded best-of-knowledge finding.

## value

PASS

Two seasonal fleets with the same total log mortality can have the same persistence verdict yet appreciably different long-run catches. The explicit allocation boundary distinguishes a genuine corner from an interior split, and an exact all-feasible-deviations loss is more informative than a local second derivative or an unconstrained optimum. The result is a useful deterministic benchmark, not a general harvest prescription.

The dated certificate retains the supplied scientific assessment, sources and limitations.

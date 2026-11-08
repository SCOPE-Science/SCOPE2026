# Self-review

**Correctness — PASS.** The anchored Lipschitz feasible set is a compact polytope, and variance is strictly convex after anchoring. A direct perturbation proves every maximizing profile is integral. The exact signed-count expression reduces the problem to one zero separator (fan) or two (wheel), with balanced sign counts, and a separate strict inequality excludes all one-sign possibilities. Thus the exact formulas, all equality profiles, parity gap, and asymptotic deficits follow for every admissible order. The standalone exact-rational checker independently enumerates all feasible integer profiles in its stated finite range; this verifies examples only, not the infinite proof.

**Originality — PASS, qualified.** Alon–Boppana–Spencer (1998), Theorem 2.1, proves existence and a general structural form of integral spread extremizers, but does not give the sharp fan and wheel values or the parity-sensitive one-edge decrement. Addario-Berry–Janson–McDiarmid (2009) treats random graph spread. Yancey (2017) studies structural extremal functions in different graph families. Direct indexing and term searches found related wheel/fan invariants but no equivalent Lipschitz-variance formula. The accessible earlier lollipop spread statement does not subsume either family. Residual risk: an unindexed equivalent calculation may exist.

**Value — PASS.** The exact graph-spread constant is natural in concentration of product spaces. Fans and wheels differ by one closing edge yet both have diameter two. The theorem provides full all-order extremizer classification and a parity-sensitive, sharp one-edge stability loss, as well as two distinct exact rates of approach to the universal variance bound.

**Limits.** Real functions, equal vertex masses, unweighted edges, exactly one universal apex and a path or cycle rim. No claim for weighted graphs, arbitrary diameter-two graphs, or the adjacency-eigenvalue spread.

Self-review: passed. Independent audit: not yet performed.

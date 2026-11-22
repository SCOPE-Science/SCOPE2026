# Scientific review

**Correctness — PASS.** The sharp lower bound follows from total Shannon entropy and the equality condition for Jensen–Shannon divergence. Saturated contacts force uniform, disjoint, equally sized supports and exactly three perfect-matching levels. This reduces the universal statement to a finite exhaustive 60-by-third-matching search, tested by independent exact averaging and graph-isomorphism routines in `verify.py`. The directly exhibited Wagner word gives a separate transparent witness. Counts and proof were checked for matching constraints, order commutation, and the generic-versus-all-initial-state distinction.

**Originality — PASS, with residual bibliographic risk.** The 2012 symmetric-gossip source establishes the shortest length and the cube construction, explicitly leaving uniqueness beyond four agents open. The 2025 compromise-process paper states a cube-only graph conjecture; a twelve-edge nonbipartite Wagner counterexample directly negates it. The stochastic-positive-diagonal theorem uses adjustable matrices and cannot imply fixed one-half contact feasibility. Closest indexed statements found concern complete-graph shortest-word counts, homogeneous peer epochs, and spectral mixing on Möbius ladders rather than an eight-agent support classification. Unindexed earlier equivalent observations remain possible.

**Value — PASS.** The finding explicitly resolves a natural shortest-protocol topology question and refutes a named open conjecture using a sparse, nonbipartite counterexample. The complete classification has design value for exact finite-time averaging on restricted networks, beyond a mere small-matrix calculation.

**Scope restriction.** Shortest twelve-contact networks only; no claim that Wagner is inclusion-minimal among *all* finite-time networks. Exact equal-weight updates only; no floating-point, error-rate, or fully general graph classification.

Self-review: passed. Independent audit: not yet performed.

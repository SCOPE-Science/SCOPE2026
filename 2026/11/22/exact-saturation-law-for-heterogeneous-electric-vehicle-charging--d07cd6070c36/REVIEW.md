# Self-review

## Correctness — PASS

The assertion uses the published untruncated finite-capacity queue *approximation*, not an exact stochastic waiting-time law. The stationary action boundary is a scalar cost-difference threshold. Its weighted energy moments are calculated exactly from the distribution with two spatial atoms and a uniform continuous component. Capacity conservation gives the sharp load threshold and the energy split; equality of the two leading waiting-cost poles gives the unused-capacity ratio and common divergence. An analytic implicit-function argument yields the next-order waiting-cost difference. All hypotheses, including strictly positive slack and the interval in which the moment polynomials are valid, are stated. The companion code checks the exact rational constants and full untruncated root equation at multiple near-critical loads. It does not substitute finite experiments for the limiting proof.

## Originality — PASS, subject to historical priority risk

Dupont–Petit–Séguret establish existence/uniqueness and demonstrate the **qualitative** high-load 50/50 energy share numerically, and this observation is attributed to them. Their manuscript contains no matching derivation of the exact threshold \(24\), EV-count fraction \(13/24\), spare-capacity ratio \(23/48:25/48\), common divergence coefficient \(1000\), or cost-gap expansion. Bodas–Ganesh–Manjunath treat heterogeneous *delay sensitivity* but assume customer classes do not change workload distributions; Liu et al. study a different deterministic-service multi-server queue approximation. Related indexed findings on low-choice-noise congestion and two-resource equilibrium selection concern mathematically different limits. Overlap comparison is by scope and implication rather than title; neither a failed text search nor this document proves global priority.

## Value — PASS

The source's charging-station numerical case already motivates the demand-composition versus customer-count distinction. This theorem resolves its natural maximal-load boundary and quantifies an operationally relevant divergence and second-moment-dependent allocation of the remaining service capacity. The exact limiting population percentages make the counterintuitive difference between EV count and total energy workload testable within the mathematical model. These are quantitative structural facts at the actual feasibility boundary, not an arbitrary slice or a restatement of half-workload shares.

## Limits and nearest literature

The result does not establish an exact stochastic \(M/G/2\) heavy-traffic queue limit, global stability of any dynamics, or applicability to realistic charging networks without calibration. The 2021 parallel-server work and the 2021/2023 charging-equilibrium work are related but not identified with the exact game. Priority uncertainty remains for related queue approximations and transportation/game-theory literature not exhaustively searched.

Self-review: passed. Independent audit: not yet performed.

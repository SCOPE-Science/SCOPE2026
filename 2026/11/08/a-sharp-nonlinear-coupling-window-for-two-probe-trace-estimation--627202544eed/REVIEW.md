# Self-review

## Correctness — PASS

The five edge-sign variables have even parity, and every one of the sixteen legal patterns has exactly two uniform vertex-sign lifts. Their five affine scalar levels have multiplicities \(1,4,6,4,1\). Minimizing a sum of two equal-marginal scalar outcomes is an antitone finite coupling, and a bijection of legal patterns realizes it without distorting the individual Rademacher marginals. Exact orders on the three parameter intervals yield the three stated variance polynomials. The fixed-flip lower bound follows from edge-product parity and pairwise orthogonality. Triangle and even-cycle minimality follows from the same parity argument. Exact verifier replay supplements, and is not the proof of, the continuous claim.

## Originality — PASS (qualified)

The 2020 Cortinovis–Kressner source studies independent trace-estimator probes; the 2013 Stathopoulos–Laeuchli–Orginos paper uses graph coloring and structured probing patterns. The 2020 Skorski and 2021 Frommer–Nasr Khalil–Ramirez-Hidalgo studies address concentration and multilevel variance reduction rather than the five-cycle arbitrary-coupling optimum. The classical antitone rearrangement principle is already known. The original contribution assessed here is its exact weighted-five-cycle consequence, the nonlinear-coupling-only interval and 25% sharp variance gap, and the comparison to shorter cycles. Searches did not produce a directly dominating specific theorem; an unindexed specialist computation remains a risk.

## Value — PASS

Two-probe Rademacher trace estimation is a standard numerical method, and structured coupling is a natural graph-based variance-reduction question. The first odd cycle beyond the triangle exhibits a nontrivial and sharp boundary between simple sign-flip designs and general couplings. The exact finite-state law clarifies when fixed sign patterns leave avoidable variance, rather than merely producing an isolated numerical counterexample. Its relevance is as a exact mathematical benchmark, not as a claimed runtime improvement for general matrices.

## Limits and precedence

Assumes precisely five cycle edges with four equal positive weights, a variable fifth weight, two samples, and arbitrary inter-probe dependence. The coupling may require knowledge of the edge weights and is not guaranteed convenient at scale. Earlier optimal-transport rearrangement theorems may subsume the *method*, but the inspected references do not establish the stated explicit graph-specific phase diagram. Independent scientific validation is outstanding.

Self-review: passed. Independent audit: not yet performed.

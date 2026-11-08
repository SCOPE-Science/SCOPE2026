# Scientific self-review

## Correctness — PASS
The local update support is exactly \(\{b_i,b_{i+1}\}\) for \(b_i=x_{i-1}\oplus x_i\). Forced sites occur only inside runs of \(b\) of length at least two. The proof provides a global cyclic extension respecting every forced bit and avoiding isolated output bits; the source's one-step cleaning rule then yields an allowed zero output. A single-site input forces a nonzero update at its occupied site, proving the lower bound. The four-state overlap matrix proves the enumeration, and the independent-site probability bound yields the stated tail. The included executable checks corroborate every finite boundary used; none substitutes for the all-size argument.

## Originality — PASS, conditional on accessible literature
The directly relevant full 2026 Cirillo--Vliem--Schuricht--Spitoni article proves only a four-step constructive reachability bound at the balanced mixture (Section IV, Theorem 1), not the globally exact two-step support depth or its complete cyclic-word census. Its Lemma 3 already establishes the one-step cleaning criterion, so that component is explicitly prior work, not claimed as new. The 2024 Bayraktar--Lu--Maggioni--Wu--Yang paper studies a different neighborhood-empirical-distribution kernel; the 2026 Endo extinction paper's accessible abstract addresses deterministic additive extinction. Searches for the exact pair of local rules, two-step positive-support reachability, absorbing depth and cyclic-run aliases did not yield a dominating statement in inspected sources. This is not a proof of absolute priority; further literature may exist.

## Value — PASS
The first-return support distance to the absorbing state is a natural finite-state dynamical invariant. Prior work required a four-stage construction, whereas the present result proves that the exact worst-case minimal horizon is two, simultaneously classifies every initial configuration, and quantifies its distance distribution. The construction explains the structural reason (forced bits occur only within long runs of the XOR derivative) rather than merely improving a numerical bound. The explicit finite-volume geometric-tail bound works for all interior mixture parameters and makes the distinction from thermodynamic-limit phases precise.

## Scientific limits and closest comparisons
Only the locally independently selected XOR rules and finite periodic rings are covered. The reported absorption probabilities need not be sharp, and no infinite-volume extinction is asserted. Earlier work on deterministic additive nilpotency and other synchronization kernels does not directly imply this support-graph classification. Historical novelty is based on accessible literature, not exhaustive global publication coverage.

Self-review: passed. Independent audit: not yet performed.

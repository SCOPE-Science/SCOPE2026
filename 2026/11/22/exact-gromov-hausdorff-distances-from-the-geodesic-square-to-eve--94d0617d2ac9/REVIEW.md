# Self-review

## Correctness — PASS

The claim is a uniform exact equality for all odd integers \(m\ge5\), not an extrapolation from experiments. The lower bound applies to **every** correspondence: select a representative square label at each target point, examine jumps of \(s=(m\mp1)/4\), and observe that distortion below \(2\pi(m-1)/(4m)\) forces every jump to exchange bipartition classes of a four-cycle. The jump permutation has odd orbit lengths, an impossibility. The upper bound comes from a surjective four-consecutive-block map and explicit bounds for same, adjacent, and opposite block pairs. All normalizations, parity arguments, wrap-around cases, and \(m=5\) were reconstructed. `check_odd_polygon.py` passed exact integer regression checks for 199 odd orders and exhaustive searches of 48,780 small surjective maps; computation does not replace the infinite proof.

## Originality — PASS (best-knowledge assessment)

The closest primary work is Lim–Mémoli–Smith's circle-sample distance question (arXiv:2105.00611, Appendix C) and Talipov's exact divisible and two-/three-vertex results (arXiv:2210.09971, Theorems 3.1–3.3). The former proves only consecutive-cardinality comparisons directly applicable here, and the latter cannot specialize to four versus odd \(m\ge7\). The closest published exact square-to-sample result explicitly handles \(4k+2\) target counts, not odd counts. The new statement is therefore not implied by any of these inspected results, even after translating notation and matching all metrics. Relevant indexed-result and scholarly searches were negative for a covering all-odd formula; unindexed or subsequent work remains possible.

## Mathematical value — PASS

The exact pairwise Gromov–Hausdorff metric for regular circle samples is an explicitly posed natural problem. Completing the missing odd target-cardinality family for the first non-simplex source order produces a full infinite classification of square-to-regular-sample distances together with a structural parity obstruction genuinely different from the previously known fiber packing in even cardinalities. This is not a one-instance computation, a numerical bound, or a corollary of the published even case. The result does not solve arbitrary cardinality pairs or classify all optimal correspondences.

Self-review: passed. Independent audit: not yet performed.

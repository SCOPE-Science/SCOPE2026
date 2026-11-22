# Mathematical review of mixed-axis reset entanglement classification

## Correctness

**PASS.** For every \(r,a,b,J>0\), the exact Lindblad stationary resolvent is normalized and unique. The invariant \(X\)-state reduction is independently checked against a full \(16\times16\) complex Liouvillian. The exact concurrence reduction has two candidate partial-transpose inequalities; the second is strictly impossible because its rationalized numerator is the negative of a coefficientwise-positive polynomial. For the first branch, the eighth-degree polynomial has strictly negative coefficients of degrees zero through two, positive coefficients of degrees five through eight, and a rigorously linked sign pattern at degrees three and four; Descartes' rule plus endpoint signs yield exactly one positive crossing. The provided `checker.py` verifies the exact symbolic identities and coefficient certificate and passes 880 independent numerical assertions. No finite experiment is used as proof of uniqueness.

## Originality

**PASS, qualified by publication-priority uncertainty.** The nearest existing full-result comparison treats \(X\otimes X\) coupling with *two* local bit-flip channels and proves entanglement is impossible for \(J^2\le ab\). The present generator has one bit flip and one phase flip, so one local jump anticommutes with the coupling and its strong-reset concurrence is always \(2J/r+O(r^{-2})\), even if \(J^2\le ab\). The other close full-result comparison treats pair-only conversion with exclusively dephasing noise; its odd-parity occupations are frozen, unlike those continuously driven by the bit flip here. The 2023 primary coherent-only quantum-resetting paper, the 2007 local single-qubit reset theory, and the 2018 general resetting resolvent were inspected, and none states this mixed-axis eighth-degree single-threshold classification. The generic stationary-resolvent method and qualitative reset-enhanced entanglement are antecedents, not claimed innovations. A more general unindexed theorem or an implicit channel reduction remains possible.

## Value

**PASS.** The result draws a sharp, physically interpretable line between a same-axis channel pair for which a geometric-mean noise ceiling can completely forbid entanglement and a mixed-axis channel pair for which every finite noise pair admits a unique resetting threshold and high-rate entanglement. The complete phase classification and exact critical polynomial address control of noisy entanglement generation, not a selected numerical regime or a routine moment calculation.

## Boundaries and evidence

The theorem concerns unconditional stationary two-qubit concurrence, exact Poisson joint reset to a pure separable product, and strictly positive constant rates. It neither implies experimentally achieved entanglement nor covers all noise alignments, finite-time trajectories, or extra coherent terms. Numerical Liouvillian comparisons supplement a coefficientwise exact symbolic sign certificate. Literature comparisons include full accessible research texts and two closely related published mathematical results. Independent priority verification remains necessary.

Self-review: passed. Independent audit: not yet performed.

# Scientific review

## Correctness — PASS

The normalized unit-advance map faithfully models the one-sided seam: outside the barrier the sheet update is a transposition, and inside it both sheets collapse to one. Fixing the terminal phase of the circle rotation gives precisely one ancestral phase, so the fiber in the image has two labels if and only if all \(n\) barrier tests are negative. This proves the union-of-translates image formula without probabilistic assumptions. A complete rational phase cycle contains \(q\) grid points and either never hits the barrier (both sheet labels periodic with periods dividing \(2q\)) or hits it (a unique periodic sheet and one finite-time-captured sheet). Their union area is \(\min\{1,qb\}\). Below the disjointness threshold, the first-hit intervals are disjoint, one of length \(b\) for each possible delay, proving exact discrete uniform capture. Endpoint exceptions have zero area. The computational checks replay these identities over a finite but varied exact-rational test family; no finite test is treated as proof of the unrestricted theorem.

## Originality — PASS within inspected evidence

The nearest paper, Beck–Chen–Yang, *Irreversible and dissipative systems* (arXiv:2404.00078, Section 2/Theorem 1), identifies the two-square dissipative barrier and the recurrent-area split for irrational slopes. Its explicitly irrational formulation does not provide the rational-denominator recurrent-area spectrum or the corresponding exact transient capture-time law. Beck–Chen–Yang, *New Kronecker–Weyl type equidistribution results and diophantine approximation* (arXiv:2106.14001), uses symmetric gates with invertible sheet transitions; the one-way coalescence needed here is absent. Related published claims on finite-time escape of planar repellers and arithmetic first returns concern different systems and do not imply these formulas. The classical finite-rotation grid identity alone is not asserted as novel. Remaining risk: an equivalent rational variant in unindexed or inaccessible material, including general finite-state reset skew-product results, may already exist.

## Mathematical value — PASS

The originating irrational-slope area law might suggest that the two-square dissipative region always contracts to area \(1\). The exact rational denominator criterion detects a distinct, mathematically natural family of positive-area non-collapsing periodic sheet pairs. Its finite-time area law and uniform capture distribution quantify the transient loss of phase-space area and show exactly how each rational phase cell contributes, providing physical consequences beyond an isolated combinatorial grid calculation. The threshold \(qb=1\) is the precise boundary of that dynamical resonance.

## Limitations

The classifications use one connected barrier interval, rational positive slopes, two sheets, and unit-horizontal-advance time; boundary orbit conventions can change null-set details. Neither broader surfaces nor arbitrary disconnected barriers are covered. The external originality search cannot establish absolute novelty. Independent mathematical audit is not performed.

Self-review: passed. Independent audit: not yet performed.

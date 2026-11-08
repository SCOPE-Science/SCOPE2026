# Scientific review

## Correctness — PASS
All primitive three-cycles are covered by the projected recurrence: all equal gives the fixed point; exactly two equal gives the scalar cubic \(K s(s-1)^2=1\); pairwise distinct gives the unique parameter-dependent cubic \(C_K(t)\). Necessity follows from a factorization of the three residual differences and two symmetric identities, and sufficiency follows from Vieta plus the root equation. The exact discriminant and strict rational sign test prove the sharp onset and positivity of the three roots. Six root orders yield two and only two cyclic classes. Exact symbolic tests in `CHECK.py` passed; sample numerical checks are not used to establish completeness.

## Originality — PASS within the inspected sources
The closest primary source is Castañeda and Rebollo-Perdomo, arXiv:2209.06986v1, §3 equation (10), Theorem 1.1 and §5. It constructs a repeated-coordinate cycle and asks whether its three-cycle might be unique. Chamberland (2005 author preprint, Theorem 3.1) also gives a repeated-coordinate existence mechanism. Those statements and existing general distinct-height constraints do not imply the sharp fixed-quadratic cubic with its two oppositely ordered cycles. Prior repeated-coordinate counts are treated as known ingredients rather than the new contribution. Searches of related published findings found period-four classifications and unrelated three-cycle problems, not a covering fixed-family result. The later 2024 journal paper's full body was not verified; unindexed equivalent results remain a real priority risk.

## Mathematical value — PASS
This is a sharp answer to a natural open possibility in the source family, for a concrete quadratic defining function: exactly two formerly uncounted primitive three-cycles occur beyond \(K=125/12\). The total real three-cycle count changes from three to five there, and the threshold is exactly aligned with the known repeated-coordinate stability boundary. A natural full cycle census and sharp parameter frontier have mathematical value without asserting global or nonlinear bifurcation theory.

## Limitations
Only real primitive period-three dynamics in the specified one-parameter family are addressed. Neither global attraction nor higher periods nor nonlinear stability of the two new cycles is proved. The later journal body and some possible equivalent literature are publication-priority uncertainties, not established noncoverage.

Self-review: passed. Independent audit: not yet performed.

# Mathematical review of the sharp two-cycle stability threshold

## Correctness

**PASS — self-review.** Every primitive two-cycle has phase coordinates \((p,q-p/2)\) and \((-p,q+p/2)\), with \(p>0\), satisfying \(q^2+p^2/4=1-1/\beta\) and \(\alpha\cos p=\beta qp^2\). The stated domain forces \(q>0\). Direct Jacobian multiplication yields \(\operatorname{tr}M=2-2B-(k+t)^2\) and \(\det(I-M)=B^2-4kt-8t^2\), in the definitions of `RESULT.md`. At \(\beta\ge3/2\) and \(p\le1\), a strict factorized inequality gives \(\det(I-M)<0\), so a real multiplier exceeds one. For \(p>1\), the tangent lower bound gives \(\operatorname{tr}M<-2\), forcing an eigenvalue outside the unit disk. For \(1<\beta<3/2\), an exact branch approaching zero forcing has return matrix tending to \((5-4\beta)I\), with spectral radius below one. Continuity and the intermediate value theorem supply a sink for every sufficiently small positive forcing. The checker reconstructs identities and tests exact two-step returns; experiments do not substitute for the inequalities.

## Originality

**PASS within inspected evidence.** The 2023 Almatroud–Pham source introduces the exact FPFM1 map, its absence of fixed points, and numerical bifurcations. A public exact 2026 mathematical census proves the same map's complete primitive two-cycle counts, including a forcing fold and an onset law, but explicitly **does not classify the linear stability of those cycles**. This result uses no census as its novel assertion: it proves the previously unclassified, all-forcing stability obstruction and the exact gain threshold for possible sinks. A fully read separate result for FPFM2 has a sink criterion for \(|y|-1\), whereas the current FPFM1 has \(y^2-1\); those equations and phase-Jacobian structures differ, so its threshold is not transferable. Targeted published-record and literature searches located no equivalent sharp \(3/2\) barrier for FPFM1. This is not a proof of worldwide uniqueness; unindexed equivalents remain possible.

## Mathematical value

**PASS.** The numerical parameter sweep in the original article crosses the gain \(\beta=3/2\). An exact, forcing-uniform theorem establishes that the fixed-point-free system has local period-two sinks at some positive forcing precisely below that gain, although primitive two-cycles themselves can exist on both sides. This makes a mathematically consequential distinction between *existence of oscillations* and *dynamical attraction*, and gives a natural sharp coefficient boundary rather than a selected trajectory or arbitrary finite check. It does not classify longer cycles or global attractors.

## Limitations and closest literature

The parameter domain is \(0<\beta\le2\), \(\alpha>0\). At a two-cycle fold, any neutral multiplier can coexist only with a strictly expanding multiplier in the excluded gain region; the proof therefore establishes ordinary dynamical instability, not merely failure of exponential contraction. The phase diagram for all forcing values below \(\beta=3/2\) is not determined, nor are higher periods. Closest sources are Almatroud–Pham (2023), the exact 2026 FPFM1 two-cycle census, and the 2026 FPFM2 stability result for a different memory function. Residual risk is an unknown earlier equivalent stability analysis.

Self-review: passed. Independent audit: not yet performed.

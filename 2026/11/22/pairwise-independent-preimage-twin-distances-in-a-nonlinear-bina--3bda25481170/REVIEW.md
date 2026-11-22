# Review of the preimage-twin Hamming-distance distribution

## Correctness

**PASS.** The cyclic Boolean factorization \(F=D\sigma K\), the involution \(K^2=\mathrm{id}\), and the two-to-one fiber structure hold for every length. A uniform input to \(K\) makes each attainable output equally likely. Exact three-input truth tables establish one-coordinate conditional balance, and the three-offset supports of distinct local distance indicators have at most one shared input for all \(n\ge7\); the pairwise-independence proof is therefore exact. The consecutive-triple probability \(7/16\) differs from the independent value \(27/64\). The cyclic de Bruijn trace counts every indexed input exactly once. The polynomial factorization follows from a bounded-degree interpolation certificate. A separated-block argument proves the Gaussian limit, with only constantly many cyclic boundary terms. `verify.py` passes all stated checks after extraction. Finite enumeration alone is not the proof of the unbounded claims.

## Originality

**PASS within inspected sources.** The 2026 Appendix B paper already introduces the nonlinear rule and its two-to-one property. The closest published 2026 record gives the **minimum** preimage-twin Hamming distance for every ring length, and an implicit weighted-graph procedure from which the distribution could be extracted computationally. The new point is an explicit pairwise-independent but not three-wise-independent local law, exact variance, and Gaussian behavior for typical fibers, rather than the minimum or an original transfer-matrix counting principle. Another published record handles the first and third open rules, not the probability law of this second rule. The 2024 general almost-lifting work supplies background, not the same probabilistic theorem. There remains a historical-equivalence risk in older Boolean-lifting and cellular-automaton literature, and an uninspected complete-text risk for the earlier almost-lifting paper.

## Mathematical value

**PASS.** The minimum inter-preimage Hamming distance can be much smaller than the separation of a randomly selected fiber. The exact \(3/4\) density and \(3/16\) variance quantify that gap, while the failure of triple independence exposes a structural constraint not visible from covariances. The full eight-state law, uniform-length variance theorem, and Gaussian scaling provide a natural probabilistic complement to the prior extremal classification. They do not automatically imply cryptographic security or a result about iterative dynamics.

## Unresolved limitations

The result is specific to the second displayed two-to-one five-site automaton; only its single-step cyclic fibers are considered. Pairwise-independence statements require rings with at least seven sites. A potential earlier implicit or explicit equivalent distribution law would affect the originality assessment. Independent audit: not yet performed.

Self-review: passed. Independent audit: not yet performed.

# Independent audit — 2026-09-26

Record: `2026/09/09/049`. Verdict: **correctness PASS; originality FAIL; scientific value FAIL for the stated target.** Disposition: archive full original package.

## Correctness
The double block average factors exactly as ∫f u v; expansion about δ gives δ∫(f−δ)(u−δ)+δ∫(f−δ)(v−δ)+∫f(u−δ)(v−δ). Cauchy–Schwarz yields T1, and unitarity makes shifted L2 errors equal. Individual ergodicity and the mean ergodic theorem imply uniform-in-shift convergence, while the simple 0≤c≤δ inequality gives density δ²/(4−2δ²). The stated rate threshold is conservative but sufficient: if α,β≤δ^(3/2)/16, the error is ≤δ³/8+δ³/256<δ³/4. I independently enumerated the periodic sets for q=8,16,40,80,400; the proposed empty squares have sides 1,2,5,10,50 and maximum c values 0,1/32,1/20,9/160,49/800, all below 1/16. Hence the uniform popular-threshold window fails over merely ergodic periodic systems. The weak-mixing-only question is explicitly unproved.

## Prior work and originality
The mean ergodic theorem and Cauchy–Schwarz yield the entire T1–T2 result immediately because m and n are averaged independently. Even commutation is unnecessary for that factorization. The periodic long-gap example is a direct interval-overlap observation. Berger, arXiv:1909.12350, studies *common-difference* corners, a stronger coupled parameter question; Jamneshan–Pan, arXiv:2208.02833, study uniform syndeticity at a threshold permitted to depend on density. Neither should be claimed as an exact antecedent for the easy independent-parameter calculation, but the displayed work has no demonstrated research-level original step beyond standard one-line estimates.

## Scientific value
The admitted weak-mixing-uniform popular-threshold question is left entirely open. The conditional K depends on an input mean-ergodic rate, and the periodic example lies outside weak mixing. Those observations are correct pedagogical controls, but do not advance the intended weak-mixing target or give a new uniform recurrence principle. The “corner” framing risks confusing two independent shift parameters with the common difference in the cited corner literature.

Sources: original RESULT.md and artifacts/verify_corner.py; https://arxiv.org/abs/1909.12350; https://arxiv.org/abs/2208.02833.

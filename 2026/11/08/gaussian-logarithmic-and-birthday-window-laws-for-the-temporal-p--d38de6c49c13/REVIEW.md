# Scientific review

## Correctness — PASS
For static, disjoint singleton approvals, every temporal PJR, EJR or EJR+ allocation must meet each homogeneous party quota. With horizon \(an\), these quotas add to the total number of rounds, so every feasible allocation has the same multiplicities \(ab_j\), yielding exact constrained welfare \(a\sum_jb_j^2\) and price \(n\max_jb_j/\sum_jb_j^2\). The stochastic proof uses an exact collision-count identity, multinomial CLT, second moments for occupied bins and factorial moments for Poisson windows. The standalone checker exhaustively verified 848 literal small-profile cases and 62 rational occupancy-moment identities; neither finite enumeration nor Monte Carlo is offered as an infinite proof.

## Originality — PASS, with residual literature risk
Teh (2026), arXiv:2605.11157, develops the worst-case temporal price of PJR/EJR/EJR+, with the same welfare metric, but does not give an iid party-choice price law, the Gaussian-maximum limit, the logarithmic typical-case growth, or the staircase and birthday-window laws. Elkind, Neoh and Teh (2024) use related temporal fairness notions; Elkind et al. (2024) study one-shot committee price. Standard balls-into-bins extreme-value phenomena are credited as prior probabilistic ingredients. The principal additional insight is the common exact temporal quota optimum, its collision normalization, and resulting full multiscale distribution. Unindexed direct equivalents or inaccessible detailed derivations in adjacent literature remain possible.

## Value — PASS
The stochastic model is a motivated benchmark complementary to worst-case temporal welfare bounds, with a mathematically sharp nonmonotone response to party diversity. It supplies a baseline for quantifying whether proportionality costs persist under random voters, and explains the lattice-to-logarithmic transition and its eventual return to unit cost. The fixed arbitrary horizon multiplier demonstrates that these effects arise from representation rather than a chosen round count.

## Scope and residual risks
The conclusion is restricted to static one-party-per-voter approvals with uniform iid party choices and a horizon divisible by the number of voters. Classical occupancy results are not claimed to be new, and no assertion is made for unequal voter probabilities or arbitrary temporal profiles. The related one-shot committee source was not materially inspected in full; a hidden equivalent theorem is possible. No external independent audit has occurred.

Self-review: passed. Independent audit: not yet performed.

# Self-review

## Correctness — PASS
The invariant domain is justified from the spectral inequality \(0\le H(I-H)\le I/4\) and \(\|B_c\|_2<2\). In the full-rank case, the exact inverse recurrence and a positive finite observability Gramian imply \(\|H_n\|_2=O(n^{-1})\). Explicit weighted-sum bounds control the nonlinear remainder and yield all three asymptotic entries, determinant, and eigenvalue scaling. Rank-one data reduce to a nonlinear scalar quotient along an explicit Jordan orbit; its cubic reciprocal growth gives the distinct constant three. The eigenline scalar iteration gives one. All critical algebraic identities were independently checked on rational samples using the standalone script, and 50-digit long trajectories corroborate the limits. Main limits are mathematical deductions, not extrapolations from tests.

## Originality — PASS within checked evidence
The originating primary full text (https://arxiv.org/abs/2303.06176, graph-coupled section, Appendix A) defines the model and exhibits nonlinear spectral-density behavior, but does not state the critical rank-sensitive extinction theorem or its universal constants. The closest published research record titled *A unique transverse fluctuation cancellation in a matrix logistic map* studies a chaotic invariant diagonal and stochastic transverse variance, a different claim not implying the neutral Jordan result. Other records on logistic threshold networks and algebraic Riccati iterations involve different maps or equilibrium theory. Exact identifiers, searches, and implication comparisons are provided in AUDIT.json. Residual risks are standard Gramian/Riccati literature and unindexed follow-ups, not proof of novelty.

## Mathematical value — PASS
The model's positive-definite and singular states exhibit different, completely classified parabolic decay rates at the same neutral defective coupling. The result gives two anisotropic eigenvalue scales for generic states and an exact mechanism for initial amplification despite eventual extinction. These quantities address the paper's central theme of information transfer along directed nonnormal matrix couplings; the rank stratification is not a routine scalar logistic substitution and matters when matrix state rank has physical meaning. The result deliberately does not assert a higher-dimensional classification.

## Scope and review status
The theorem requires \(0<c<3/2\) and \(0\le H_0<I\). Publication priority beyond the inspected sources cannot be guaranteed. No independently performed validation is claimed.

Self-review: passed. Independent audit: not yet performed.

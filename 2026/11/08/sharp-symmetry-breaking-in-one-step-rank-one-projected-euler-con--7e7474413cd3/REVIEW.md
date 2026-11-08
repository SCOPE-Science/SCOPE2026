# Mathematical review

## Correctness — PASS

The state update is an exact projected Euler step because its constant forcing lies in the tangent space at the initial rank-one state. The positive dominant eigenvalue of the two-by-two symmetric Euler matrix exceeds the absolute negative eigenvalue by exactly one, so the Frobenius-nearest rank-one state is unique throughout the real control axis. Its exact squared norm and lower-right entry give a scalar cost with a monotone threshold function. Differentiation proves the number, location and global nature of all minimizers for every real target and every nonnegative regularization parameter; the boundary expansion and error formulas follow algebraically. The separate full-state quadratic has one optimizer. The executable supplies independently structured exact-rational and numerical checks; the universal assertions do not depend on samples.

## Originality — PASS, with residual historical-priority risk

The 2026 Carrel–Vanzan paper (Section 4.2, Remark 4.10; Section 6.3) states qualitative low-rank optimization nonconvexity and observes apparent local trapping, but treats a continuous dynamical low-rank state with a different numerical forward scheme and does not state a one-step singular-value-retraction phase diagram. The Kieri–Vandereycken projected Euler analysis (2017 author preprint, Section 4) supplies the update structure and general convergence theory, not this exact global control calculation. Searches for one-step rank-one control, truncated-SVD target tracking, equivalent symmetric two-by-two formulations, and phase-transition aliases found no directly covering statement in the checked literature. The proof is direct but the precise analytic classification is not supplied by either cited general result. Historical equivalence in an unindexed source remains possible.

## Value — PASS

The matrix size, control dimension and integration horizon are minimal for a nontrivial rank-one retraction. The theorem explains analytically how an otherwise smooth, globally unique SVD projection creates a double-well control landscape from a strictly convex terminal-control objective. Quantifying the threshold, the two optimizers, their square-root splitting, the objective gain and the vanishing approximation residual distinguishes genuine geometry-induced nonconvexity from numerical singular-vector ambiguity. This is a reproducible benchmark for selecting rank, step size and fidelity safeguards in reduced-order control; it is not claimed to supply such a safeguard for all problems.

## Closest literature and remaining limits

- Carrel and Vanzan, arXiv:2610.29554v1, Remark 4.10 and Sections 5–6, continuous low-rank optimal control and a qualitative nonconvexity observation.
- Kieri and Vandereycken, DOI:10.1515/cmam-2018-0029, Sections 3–4 and equation (21), retracted projected Euler integration.
- The analysis concerns a one-step, rank-one, terminal-tracking model; it does not establish the same threshold for continuous-time dynamical low-rank control, more than one step, or other target matrices.

Self-review: passed. Independent audit: not yet performed.

# Scientific assessment: cyclic heavy-ball phase diagram

## Correctness — PASS

The algebraic proof starts from the actual component-update matrices and computes the product trace and determinant. The strict Schur/Jury conditions reduce on the exact common frozen-stability domain to one convex quadratic. Separate treatment of the vertex inside the domain and the excluded upper endpoint proves the piecewise threshold, and checking the endpoint sign proves the disconnected-stability classification. The degenerate zero-momentum case and nondecaying neutral boundaries are distinguished. Exact symbolic and rational examples were reproduced by the accompanying checker. Numerical grids supplement but do not substitute for the analytic proof.

## Originality — PASS (qualified)

Comparisons examined the primary full text of arXiv:1811.01777 (cyclic updates of different coordinate blocks), arXiv:2111.05430 (fixed-Hessian and averaged heavy ball), arXiv:2206.07553 (independently sampled minibatches), arXiv:2301.05799 (fixed quadratic Lyapunov bounds), and arXiv:2610.09912 (one fixed strongly convex objective). None of the inspected statements supplies the exact curvature-contrast minimization or the two-window condition for cyclically alternating scalar sample gradients. Relevant mathematical research summaries on cyclic block momentum and on periodic recurrences also concern different operators. The novelty rests on the sharp global parameter elimination, not the classical Jury criterion alone. Unindexed specialist Floquet literature remains a genuine precedence risk.

## Value — PASS

The result provides a natural complete stability diagram for a minimal cyclic finite-sum momentum method. A concrete strongly convex example has two disjoint stability windows inside an interval where every fixed component and the average-gradient heavy-ball method are each stable, so naive single-component stability checks are inadequate. The sharp damping threshold identifies exactly when such a reversal can occur. The scope is deliberately restricted to deterministic two-sample scalar quadratics; it is not asserted to predict general stochastic or nonlinear behavior.

## Limitations and closest literature

The result does not cover independent random schedules, arbitrary nonperiodic sampling, general nonlinear objectives, or all initial conditions under an unstable multiplier. The closest primary research sources and their precise non-implications are given in RESULT.md and AUDIT.json. Historical overlap from unindexed specialist sources cannot be excluded without independent literature review.

Self-review: passed. Independent audit: not yet performed.

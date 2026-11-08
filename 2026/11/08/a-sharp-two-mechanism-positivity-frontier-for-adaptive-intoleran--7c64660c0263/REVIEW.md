# Scientific review

## Correctness — PASS

The update rule and media multiplier were transcribed directly from Equations (2) and (3) of Johnson–Eisenberg (2024). The proof first reduces to nonnegative neighbor discrepancy by exact reflection. Attractive updates yield the maximum coefficient \(A(\lambda)\) and an explicit overshoot witness, whereas repulsive updates yield \(B(\lambda)=\lambda^{-2}-1\) with a strictly negative output for sufficiently small positive intolerance when the bound is exceeded. These independent necessary-and-sufficient inequalities prove the universal step frontier. Strict log-concavity of the attractive coefficient and strictly opposing parameter monotonicities prove a unique optimal conformity parameter. All boundary cases, media factors, and the unit-step threshold are checked. The standalone verifier passed 44,939 exact or sampled checks. Numerical crossover approximations are supplementary and not used for proof.

## Originality — PASS, subject to residual publication-priority uncertainty

The primary 2024 paper was read through its model equations, discussion, and simulations. It states that multiplication by \(x(1-x)\) retains a bounded intolerance variable, and studies segregation transitions numerically; it does not state the sharp universal step-size maximum, the exact switch between upward and downward overshoots, or the nonmonotone unique safe-step optimum. The paper's approximately linear segregation threshold is not claimed as new. Urselmans–Phelps (2018) has clipped additive increments, not this polynomial recurrence. Haw–Hogan's earlier two-population spatial ODE addresses different state variables and does not by itself imply the exact scalar discrete frontier. Targeted mathematical-result searches returned no scientific statement covering the theorem, but undiscovered equivalent work remains possible.

## Value — PASS

The result supplies a sharp parameter-and-step admissibility guarantee for a published adaptive-tolerance model and separates two distinct mechanisms by which numerical updates can leave the interpretation range. The unique interior maximum of the safe step shows that raising conformity does not monotonically improve numerical robustness. The unit-step and media corollaries identify precise conditions under which the written update can be used without additional clipping for arbitrary changing neighborhoods. This is consequential for mathematically interpreting simulations, not merely an observation about one invalid numerical example. It does not assert any social-policy conclusion.

## Closest literature and limitations

Johnson–Eisenberg (2024), arXiv:2403.02122, model Equations (1)–(3) and simulation results; Urselmans–Phelps (2018), DOI 10.1371/journal.pone.0193950, adaptation algorithm; Haw–Hogan (2018), arXiv:1709.07568, spatial segregation bifurcations. The theorem concerns the printed scalar update with arbitrary values \(x,p\in[0,1]\). It does not certify the behavior of any code with clipping, full spatial trajectories, or empirical data. The general mathematical literature on positivity-preserving discretizations is extensive, and an unindexed specialized derivation cannot be excluded. Accessible published-record searches do not constitute a proof of absolute priority.

Self-review: passed. Independent audit: not yet performed.

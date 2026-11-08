# Scientific review

## Correctness

**PASS (same-model).** The exact quadratic identity follows by expanding the nuclear-scaled polar step. The nontrivial optimization is proved via orthogonal-frame completion, entrywise-square doubly stochasticity, and permutation-vertex maximization. The singular-value limiting family realizes every extremal branch in the limit, establishing sharpness and nonattainment for rank above one. Step-interval boundaries, rank monotonicity and unique minimax step are explicitly proved. The extracted checker passed 56,010 exact-rational and numerical assertions. Its finite tests are auxiliary to the proof.

## Originality

**PASS (same-model; historical priority not independently certified).** The October 2026 quadratic spectral-optimizer paper gives the nuclear-scaled polar update's exact one-step identity, a trace-based contraction estimate, and exact stability-step limits. These inputs are acknowledged. The new assertion is the optimized rank-specific spectral envelope, its nonattainment at positive full rank, strict rank-activation penalty, and sharp fixed-rank calibration. Shulgin et al. prove the full-row-rank special case, an exact-line-search coefficient, a noncoupled active-rank lower bound and rank nonincrease. The new exact intermediate-rank marked-frame envelope is not a restatement of these prior bounds. The original PolarGrad theory supplies general rank-based sufficient rates, not the exact marked-frame optimization. Searches of published research summaries, prior documented mathematical claims and primary literature yielded no dominating statement. A wider historical variational theorem remains a residual risk.

## Mathematical value

**PASS (same-model).** The source bound uses a worst-case trace combined with the smallest curvature, although these choices cannot always arise from the same rank-limited eigenspace. The theorem solves this coupled extremal problem exactly, yielding a strictly stronger numerical bound for natural anisotropic examples (\(573/625\) versus \(609/625\)), and quantifies the singular rank-boundary deterioration. It supplies a unique minimax step-calibration rule for fixed gradient rank without claiming full-trajectory sharpness.

## Closest literature and limitations

Primary comparisons: Jawanpuria–Garai–Mishra, arXiv:2610.27747v1, Appendix C and Proposition 8; Shulgin–Laing–Orvieto–Richtárik, arXiv:2610.30280, Theorem 3, Appendix E.2 and E.6; Lau–Long–Su, arXiv:2505.21799v4, Sections 3.3 and 3.5. Known full-rank and rank-one specializations are acknowledged rather than claimed original. Classical Ky Fan/Birkhoff tools are acknowledged. The result is confined to fixed SPD left-curvature matrix quadratics, exact nuclear-scaled polar updates and one-step worst-case objective ratios. It does not establish stochastic or inexact-polar convergence claims. The rate bound iterated over a changing-rank trajectory is not claimed sharp.

Self-review: passed. Independent audit: not yet performed.

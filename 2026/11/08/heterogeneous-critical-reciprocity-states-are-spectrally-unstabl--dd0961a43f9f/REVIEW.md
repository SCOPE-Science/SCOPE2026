# Assessment of the critical-reciprocity spectral instability theorem

## Correctness

PASS. At \(p_i-q_i=c/b\), the paper’s own first-argument gradient factor vanishes and the point is stationary. Differentiation of the full synchronous map including self-play yields a rank-two departure-from-identity Jacobian. Its reduced nonzero eigenvalues have product \(-4\alpha C^2\sigma_w^2\), strictly negative when the forgiveness coordinates differ. This proves an expanding discrete multiplier. The complete proof and exact rational reconstruction appear in `RESULT.md` and `CHECK.py`. All-\(N\) correctness is analytic, not an inference from finite tests. Limitations: strictly interior, identical benefit and cost, specified gradient convention.

## Originality

PASS, with residual risk. Wolfe and Plotkin’s 2026 paper supplies the model and stationary gradient factor but the inspected main results and supplementary homogeneous theorem do not give the heterogeneous critical-manifold spectral formula. Semantic searches of research records and the accessible scientific ledger found no identical or stronger result. General game-learning stability theorems could still cover it under an unrecognized equivalence; related papers assessed only at abstract level are not certified noncovering.

## Mathematical value

PASS. A natural continuum of zero-gradient states might appear stable because all learners face the critical reciprocity ratio. The theorem proves every heterogeneous interior member is unstable regardless of the learning-rate configuration, and identifies weighted forgiveness variance as the exact obstruction. This supplies a concrete diagnostic for stability in payoff-gradient learning, without claiming a global convergence theory.

## Closest literature and limits

Wolfe–Plotkin (2026), arXiv:2610.15054v1, Section II and supplementary S6, is the closest source. Fujimoto–Kaneko (2019), arXiv:1905.06602, and McAvoy–Mori–Plotkin (2021), arXiv:2111.07776, were compared only at the abstract level. The analysis does not determine center-manifold motion, global basins or boundary stability. The second nonunit multiplier may have magnitude greater than one at very large steps. No independent scientific audit has been conducted.

Self-review: passed. Independent audit: not yet performed.

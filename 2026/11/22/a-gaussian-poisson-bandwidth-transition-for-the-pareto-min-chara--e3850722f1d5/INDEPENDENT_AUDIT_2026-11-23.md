# Independent mathematical audit

## correctness

PASS

Verified the fitting, normalization and all three limits. Exponential transformation gives fitted logarithms beta_n(E_i−m_n) with beta_n−1=O_P(n^−1/2), m_n=O_P(n^−1) and max E_i=O_P(log n). The exact substitution u=gamma_n t gives gamma_n² T=(n/gamma_n) times the squared H norm of the centered clipped means, including for the fitted statistic. Direct integration gives the covariance kernel K; it is positive as the integral of products of min(x,1/u) against x^−2 dx. The diagonal bound 2/u gives trace convergence by domination, and the covariance kernels converge weakly as operators by Cauchy–Schwarz and the same bound; positivity, convergence of traces and finite-rank approximation then give trace norm convergence. The maximal Gaussian-regime summand norm is at most sqrt(gamma_n/n). At a finite ratio, above x=epsilon the observation count is binomial with success probability 1/(n epsilon); given this count, the sizes have density epsilon/x² on x>epsilon. The H-valued cutoff functions and deterministic compensators converge there by dominated convergence; below epsilon the centered H² error is at most 2 epsilon. Above the boundary, truncation of the Pareto sum at n and Mn gives mean minus log n tight (P(max>Mn)≤1/M); the norm of upper clipping tends to zero by integrating h(r)/r from gamma_n/(Mn) to infinity. Thus the centered H vector divided by log(gamma_n/n) converges to −1 and its squared norm to 2, even for arbitrarily fast rates. Checked equation (6) separately: for cap v≥1 the first log-weighted truncated moment is 1+log v+(log v)²/2 and the second is O(v(1+log v)²); integrating with the given H weight bounds the fitted-minus-oracle error by o_P(sqrt(gamma_n/n)) below the boundary. Above and at it the uniform relative perturbation and O_P(log n) Pareto mean make the H error o_P(1). For caps a≤b, the fourth cumulant integral is 2a²b−2a³/3; Wick's formula and the change v=ut give Var(Q)=6.704649979265373967 by independent high-precision quadrature and the additional slope (8/3)(1−log 2). The frozen checker was read, not executed: its fitted-sample checks are only nonnegativity and finiteness, not evidence of the nuisance rate or finite-sample convergence of moments.

## originality

PASS

Best-of-knowledge pass for the increasing-rate fitted H-quadratic trichotomy and exact critical moment separation, not for equivariance, the minCF statistic, or generic heavy-tail truncation limits. The nearest general prior genuinely covers important scalar mechanisms.

## value

PASS

The weight rate of an actual fitted goodness-of-fit statistic determines qualitatively different null laws. The equal means and exactly different variances give a quantitative distinction that fixed-weight calibration cannot provide, and supercritical collapse has a useful sharp typical-value scale. No claim of bootstrap validity, power or growing-rate finite-sample moment convergence is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.

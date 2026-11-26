# Independent mathematical audit

## correctness

PASS

The deterministic state transition T has spectral norm less than one; its past-innovation series is L² convergent, stationary, and unique by contraction of a synchronously coupled pair. In an orthogonal eigenbasis, conditional on the shared order sequence the stationary coordinates are independent centered Gaussians. Writing a_i=exp(-2h lambda_i), their variances obey the stationary recursion V_i(new)=a_i V_i(old)+2h[a_i+(1-a_i)B] with the same fresh B in all modes. Taking means gives exactly 2h[p+a_i/(1-a_i)], and subtracting 1/lambda_i gives 2h(p-f(h lambda_i)). Strict decrease of f follows from f'(t)=(sinh(t)^(-2)-t^(-2))/2<0; expansions at zero and infinity give its range (0,1/2). The endpoint modes give the maximal absolute error, so equalizing them yields the unique admissible midpoint minimizer, including the isotropic case. For conditional variances the stationary covariance recursion multiplies the old covariance by a_i a_j and adds (2h)^2 (1-a_i)(1-a_j)p(1-p). For distinct orthogonal modes this is also the source of the unconditional square covariance; for a single mode the fourth cumulant is three times the variance of its conditional variance, with (1-a_i)/(1+a_i)=tanh(h lambda_i). Positivity for every interior p precludes a Gaussian stationary law. At p=0,1 the stationary law is Gaussian but f is strictly between those values, so covariance is wrong. The cross-mode result includes repeated eigenvalues with distinct orthogonal coordinates, and is vacuous in dimension one. The small-h expansions and displayed example are consistent with the exact formulas.

## originality

PASS

The fair-coin random-order Langevin method and general Gaussian-mixture moment identities are not new. The supported distinct contribution is an exact harmonic benchmark for the biased, common-order version: operator-norm spectral calibration and its sharp error, impossibility of exact invariant-law calibration, and explicit marginal and mixed fourth-order effects. Neither the verified fair-order error bound nor the inspected switched-environment analogues state or cover this package.

## value

PASS

For a standard quadratic test problem this result identifies exactly what a single tunable splitting probability can achieve: the best possible error across all modes and the conditions for zero covariance error. More importantly it gives a sharp obstruction to equating covariance calibration with fidelity of the invariant law, and explains how a common order induces nonlinear dependence despite zero linear cross-covariances. This is useful exact information for evaluating a natural sampler, not a claim that covariance minimization optimizes other metrics.

The dated certificate retains the supplied scientific assessment, sources and limitations.

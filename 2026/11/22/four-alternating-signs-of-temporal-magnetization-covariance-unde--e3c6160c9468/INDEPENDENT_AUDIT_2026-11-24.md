# Independent mathematical audit

## correctness

PASS

The Palm event intensity is 1/EW=1/2 and equilibrium age has density S(a)/2; hence k E exp(-kA) tends to 1/2. For a,b small, the events giving ages a at time 0 and b at time t are at -a and t-b. The first is automatically the last as of time 0 because a<1; the second is automatically the last as of t because b<1. With b<t the epochs are distinct. The Palm pair density is (1/2) times the sum of interarrival convolution densities at t+a-b, not f(t+a-b) alone. The square complement contributes <=exp(-k delta); the Laplace scaling in the square gives k^2 Cov limit nu(t)/2-1/4 away from the cutoffs. The four positive-lag limits at 1/2,6/5,9/5,5/2 are -1/4,71/216,-229/2916, and at least 4759/62500, respectively. The last bound uses f*f with s(5/2-s)<=25/16 on 1<=s<=3/2. For example delta=1/20 and a uniform local Lipschitz bound 18 on nu give error at most 18/k+(5+k^2)exp(-k/20)+exp(-k)/2, already smaller than every sign margin for k>=1000. This follows by integrating |a-b|<=a+b against the two exponential weights; near 5/2 the convolution derivative is bounded by 4+12(0.55) and the f derivative by 6. At zero the age observable has nonzero variance. The age is continuous at deterministic t almost surely because the stationary epoch distribution has no fixed-time atom, and bounded convergence gives covariance continuity. The strict sign witnesses are separated by four disjoint intervals, giving at least four zeros separating opposite signs, with no claim about all zeros or sharp k. The supplied checks.py verifies numerical/fraction witnesses, not the renewal limit; correctness here follows from the independent analytic reconstruction. The result concerns the macroscopic conditional mean, not individual spin covariance.

## originality

PASS

Pass for the four-reversal conclusion with exact lags and the specified Pareto-square clock in the stationary conditional-magnetization setting. The physical reset model and the renewal tools are prior art; no broad priority claim is supported.

## value

PASS

The rigorous, short-lag multiple reversals are a motivated memory effect for a refractory renewal clock and not inferable from the one-time stationary law. In the memoryless exponential reset case an intervening event cuts dependence on X_0=e^{-kA_0}, giving C_k(t)=exp[-(lambda+k)t] Var(X_0), always positive. Thus even the existence of several alternating witnesses is an informative contrast. The claim stops at the age-conditioned thermodynamic mean and asymptotic-in-k regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.

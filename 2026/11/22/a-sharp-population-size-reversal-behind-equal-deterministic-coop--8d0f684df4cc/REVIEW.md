# Independent mathematical audit

## correctness

PASS

RESULT.md lines 15–36 specify distinct no-self payoff averaging and Fermi update conventions. The deterministic difference is (2x−1)[1+(2−T)x], so x=1/2 separates the two equal-length basins. Writing x=i/N, I derived Δ_i={N(2x−1)[1+(2−T)x]−[T−1+(4−T)x]}/(N−1); the second term removes U_CC−U_DD. Symbolic sums from i=1 to N−1 give S=[(2−T)(N−5)−6T]/6 and W=−[N²+(2T−1)N−T+4]/6<0, including N=2. The first-step recurrence for absorption increments has ratio exp(−βΔ_i), so the ratio of the first and last increments is exp(βS). The slope in N is positive for 1<T<2; equality in the odds requires an integer N equal to the specified real cutoff (23 at T=3/2). For A_k the partial sums starting at A_0=0, the mean of exp(−βA_k) is at least exp(−βW/N)>1, proving strict subneutrality including at the reversal, for every β>0. This uses the stated instantaneous feedback, not arbitrary stochastic extensions or weak-selection asymptotics.

## originality

PASS

Credit the row-reversing feedback, deterministic basin boundary, general Fermi method, and classical fixation identities as prior. The supported distinct contribution is the explicit joint size-reversal and strict all-intensity subneutrality result for the specified well-mixed no-self stochastic extension. The closest inspected formulations do not establish that result. Historical priority is qualified.

## value

PASS

The same continuous game and an ordinary finite-population convention produce a sharp decision boundary even though the deterministic basin comparison never changes. The substantive point is the simultaneous separation of three benchmarks: equal deterministic basins, size-dependent relative fixation, and uniformly below-neutral absolute cooperator fixation. The exact all-intensity result addresses when finite-size selection criteria demonstrably disagree; the isolated number 23 or the generic recurrence alone would not justify acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.

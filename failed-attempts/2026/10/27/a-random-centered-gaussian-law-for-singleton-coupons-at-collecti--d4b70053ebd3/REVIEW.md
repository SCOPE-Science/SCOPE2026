# Independent mathematical audit

## correctness

PASS

Independent rate-one clocks have independent Exp(1) first arrivals and an almost surely unique last first arrival. Conditional on its time t and index, the other counts are independent Poisson(t) conditioned positive; the last type contributes one singleton. Thus S_n | W_n=t has law 1+Bin(n−1,t/(e^t−1)). At t=log n+g the conditional mean is (log n)e^(−g)+O(1) and the conditional variance divided by log n tends to e^(−g), uniformly for g in a compact set. Expanding the centered binomial characteristic function, using tightness of W_n−log n and the explicit maximum distribution, gives the claimed joint mixed-Gaussian law. The variance of W_n−T_n/n is H_n/n from the label-independent Exp(n) gaps, so even (log n)|W_n−T_n/n| tends to zero in probability, and replacing the center preserves the Gaussian scale. Division by e^(−X_n/2) gives the independent standard normal pivot. For the covariance, under the singleton weighting S_n−1 the substitution u=e^(−W_n) yields Beta(2,n−1) integrals for −log u and its square; these give E[S_n]=H_n and Cov(W_n,S_n)=H_n^(2)−H_n. With Beta(3,n−2) one obtains the stated second factorial moment; the resulting Var(S_n)∼(log n)² gives the correlation limit. A separate exact rational recurrence reproduces Cov(T_n,S_n)=−1/2, −17/12, −95/36 for n=2,3,4, respectively (branches/306200d7-af4a-4194-94c4-09791336ff4d/independent_finite_check.py); these checks are finite, not a proof of the limit. Frozen verification support was inspected, not executed.

## originality

FAIL

The distinct Resultary sibling-deficits finding 0d3ee5e36129 states both second-order limits for every fixed J≥2 and directly implies the full proposed contribution at J=2. The different center, scale and first coordinate are asymptotically equivalent (or exactly related by a logarithm). This is established coverage, not an inference about authorship or publication chronology from a catalogue date. The ancillary covariance is not claimed as novel and does not remove the coverage of the main finding.

## value

FAIL

A Gaussian pivot independent of the completion fluctuation is useful in the coupon model, but this submission's pivot is a coordinate of an existing broader theorem, changed by a routine recentering and continuous reparametrization. The supporting harmonic covariance follows by elementary beta differentiation of the finite law and is expressly not the claimed new contribution. No distinct valuable remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.

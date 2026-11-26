# Independent mathematical audit

## correctness

PASS

The inverse-clock assumption is on the independent, strictly increasing, nonkilled D. Since independent Poisson epochs are almost surely continuity times for D, physical batch epochs are D(T_j): the inverse crosses T_j at D(T_j−)=D(T_j). Conditional on the iid exponential durations the D-increments are independent and depend only on their respective durations, so after averaging the positive waits are iid with transform λ/(λ+g(s)) and mean μ=d/λ; they are independent of marks. The n-th gap is positive just at a renewal boundary n−1. For n<k the joint boundary probability is u_(n−1)u_(k−n) and the waits used are distinct, proving Eq. (1), including n=1 and applicability with just finite first moment for distinct gaps. The adjacent covariance is μ²u_(n−1)(q−u_n); u_(n−1)>0 from the all-singleton history. The generating function factors using (1−z)(1+az+az²). Its coefficients give u_n=1/m+(2a/m)r^n[cos(nθ)+κ sin(nθ)], as also checked by the two initial values of the transient. Since q−1/m=a(2q−1)/m, the noncritical eventual signs are strict. At q=1/2, 2cosθ=−1/√2 has nonintegral algebraic norm, so θ/π is irrational; both sign arcs then have infinitely many visits bounded away from zero and give the stated two-sided subsequence magnitudes. For the uniform cutoff, put h=−log r, δ=q−1/2. A bounded sinusoidal amplitude gives the upper bound log(1/|δ|)/h+O(1); compactness of the phase circle gives a fixed finite block hitting strict interior arcs of both signs for rotation at criticality. Uniform continuity over that finite block preserves the two hits at nearby q for every starting phase. A block a fixed distance before the threshold therefore contains a strict opposite-sign anomaly, uniformly on both sides. Replacing h by (log 2)/2 costs O(|δ|log(1/|δ|)). For size {1,2}, u_n−q=[a²+a(−a)^n]/(1+a)>0 for n≥2, and unit-only marks give independent waits. Frozen verify.py was inspected but not executed; its finite assertions do not prove the infinite phase or uniform cutoff. An independent exact-rational recurrence diagnostic on n=2,…,128 for q=1/2±2^(−j), j=8,12,16,24,32, gave final sampled anomaly indices within four of 2j; this is supplementary only.

## originality

PASS

Credit the inverse-clock renewal law, ordinary renewal-boundary covariance mechanism and limiting stationary covariance to established methods/results. The supported addition is the full ordinary-origin strict sign phase for singleton/triple bursts, including critical infinitely many strict signs of each kind, uniform logarithmic last anomaly, and the strict size-two comparison. The closest inspected count and arrival transform results do not establish this transient theorem; the older stationary chapter itself could not be independently inspected.

## value

PASS

When the limiting covariance cancels, stationarity alone gives no indication of startup correlations. The exact critical result and the logarithmic number of individual arrivals until the last possible opposite sign diagnose persistence of ordinary-origin initialization near cancellation. The result is independent of wait shape and the size-two comparison identifies the first nontrivial unit-containing two-size support, giving a natural minimal model rather than an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.

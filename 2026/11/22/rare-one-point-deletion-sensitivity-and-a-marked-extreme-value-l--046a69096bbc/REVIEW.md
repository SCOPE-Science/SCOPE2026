# Independent mathematical audit

## correctness

PASS

Rotate the chosen deleted point to a fixed origin: the remaining uniform points generate a uniform simplex of gaps, with the two incident gaps at its two ends. In independent exponential coordinates, let T be their sum, R their maximum, Z the maximum elsewhere and S the full sum; the event is T>Z and the exponential-scale increase is (T-max(R,Z))_+. The Gamma(2,1) integral reduces to a beta derivative and gives H_(n-1)/(n-1). Alternatively, in the inverse coupling an independent new point must split the largest gap of the post-deletion sample to create a strict loss in the maximum; this gives E[M_(n-1)] directly. The standard uniform-simplex inclusion-exclusion integral gives E[M_k]=H_k/k (with M_1=1), so subtract the means at k=n-1 and n and divide by P(A) for the conditional mean. The tail inequality at t>=0 requires both incident exponentials to exceed t and T>Z+t. Shifting both by t via memorylessness yields the displayed signed binomial expansion via the Laplace transform of a Gamma(2,1) sum. At n=2 the event is certain and the exponential-scale tail is e^(-2t), consistent with a single full-circle post-deletion gap. For n>=3 the conditional joint density of (Z-log n,T-Z) converges pointwise to e^(-2x-e^(-x))*e^(-w) on w>0. This is a normalized product, so Scheffé gives total variation convergence for those auxiliary variables. The ordered incident-gap split is exactly uniform independent of (T,Z); P(R>Z|A)<=2/H_(n-1) follows by symmetry of each incident exponential with the unaffected ones. The sum concentration remains overwhelming relative to P(A) and makes the error from n/S even on the log n term tend to zero. This yields the stated physical joint weak limit with mutual independence.

## originality

PASS

The distinct claim is the exact single-deletion law including the exponential-scale tail and the joint marked conditional weak limit for exactly one uniformly selected deletion. The harmonic probability is a direct consequence of the classical maximum mean via inverse insertion; the conditional mean likewise follows from the known marginal means and this probability. These components and the standard gamma split are not themselves evidence of originality. The most relevant same-day thinning result reproduces the two unmarked densities in an iterated small-noise limit, but does not give the exact-one rare conditioning or its finite law.

## value

PASS

This is sensitivity of a standard geometric extreme to random removal, rather than the already studied maximum over potential removals. The marked joint law quantifies not only how rarely a deletion is pivotal, but how its occurrence biases the old maximum and how the actual increase and deleted point location then behave. The exponential-scale finite tail gives exact finite calibration; the non-Gumbel tilt and asymptotic independence are the scientific gain beyond the elementary probability and mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.

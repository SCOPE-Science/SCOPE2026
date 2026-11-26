# Independent mathematical audit

## correctness

PASS

The NB generating function gives the two factorial moments, each divided by the positive-count mass after truncation. The point mass contributes to the mean but not to the second factorial moment, so variance minus the distribution's own mean is exactly −1+At−B²t², with A,B>0. At t=1 its sign is that of 1−(r+1)(1−q)^r. I checked the factorization of the endpoint derivative A−2B² using u=1−q: the auxiliary derivative h'_r(u)=r(r−1)u^(r−2)(1−u) and h_r(1)=1 give the asserted strict sign reversal at r=1. In the size-biased law of Y−1 the statistic is k, so the log-q derivative of A/B is its strictly positive variance (convergent differentiated series on each compact subinterval of 0<q<1). The limits 0 and +infinity give a unique A/B=2. For r>1 the positive vertex is below 1, and at A=2B one has B>1 and a negative endpoint value −(B−1)². The vertex and endpoint signs give all five regimes, including the interior double root and the roots B^(−2),1 at q_c. For r≤1 the derivative is strictly positive on the open retention interval, even at r=1, giving precisely the stated exceptions at t=1. An independent exact PGF differentiation (`python3 /workspace/checks/dispersion.py`, SymPy) gave −1, 2479941473/21532234108 and −421000000/37681409689 at the three witness weights. That computation is a witness, not a continuum proof. Frozen verification material was inspected, not executed.

## originality

PASS

Qualified for the full phase diagram: the probability model, moments and quadratic reduction are covered or immediate from prior work, not original. The positive evidence is a distinct quantified statement about shape, ordered cutoffs, and strict interior root counts; the inspected same-law sources establish the ingredients but not the global shape inequality or the unique discriminant transition.

## value

PASS

Variance relative to one's own mean is a standard unconditional summary for positive-count mixtures. A pair of underdispersed endpoint laws does not control their mixture: here the theorem says exactly when intermediate structural-one mass reverses and then reverses back the sign. The uniform real-shape result, strict cutoffs and exact witness are useful beyond a routine moment calculation, without claiming regression-residual, inference or Poisson-characterization consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.

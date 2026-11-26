# Independent mathematical audit

## correctness

PASS

In the scaled variable y=x√(κ/D), the stationary law is the OU kernel at an independent rate-α exponential age, mixed with weights p at +a and 1−p at −a. Regeneration gives uniqueness. Integration by parts in the defining integral gives the homogeneous ODE Ψ″+yΨ′+(1−α)Ψ=0. The two opposite decaying solutions give the Green density by continuity and derivative jumps −αp and −α(1−p); the Wronskian of Ψ(−y), Ψ(y) equals its negative value at 0 times e^(−y²/2), confirming the positive normalization in RESULT.md. The exterior slopes are strictly inward. At any interior critical point f″=(α−1)f, so all interior critical points are simple and of one type, and at most one exists. The inner endpoint slopes divided by K are pH(a)−(1−p)H(−a) and pH(−a)−(1−p)H(a). At an endpoint with zero inner slope the same ODE gives the deciding one-sided curvature, yielding the stated strict versus non-strict thresholds. For α>1 integration by parts makes H a positive Gaussian factor times the integral with t^(α−2); the log derivative of H(−a)/H(a) is a sum of positive tilted means. For α<1 the proof's informal notation Ψ′(−∞)>0 is not a positive derivative-limit assertion: the needed positive derivative at some negative argument follows by the mean value theorem from Ψ(−a)→0 and Ψ(0)>0. Indeed splitting the integral with Gaussian centered at a at t=a/2 bounds the two parts by e^(−a²/8)(a/2)^α/α and √(2π)(a/2)^(α−1). Since Ψ′(0)<0 and every zero of Ψ′ is a strict maximum, there is a unique sign crossing; the same critical-point argument on Ψ(y)+Ψ(−y) gives H(a)>H(−a) for a>0. At α=1, H=e^(−y²/2), so f′ on the gap has sign 2p−1 and is identically zero only at p=1/2. These analytic checks include both threshold equalities and a=a_c. CHECK.py and VERIFICATION.md were inspected, not run; the reported 516 assertions are numerical diagnostics, not proof.

## originality

PASS

The distinct result supported by the inspected comparisons is the full unequal-weight phase diagram, with exact bias boundaries and the separation at which the interior mode persists for every positive two-site weighting. The equal-weight transition and plateau and the renewal framework are prior results. Priority is not asserted beyond the bounded comparisons.

## value

PASS

A full moving-mode versus pinned-mode classification for a natural minimal biased reset law exposes a qualitative feature absent from the equal-weight case. Exact, sharp thresholds and their behavior at equality distinguish when changing the reset bias actually destroys a peak or merely moves the unique peak.

The dated certificate retains the supplied scientific assessment, sources and limitations.

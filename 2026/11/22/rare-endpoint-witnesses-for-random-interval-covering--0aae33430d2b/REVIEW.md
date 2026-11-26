# Independent mathematical audit

## correctness

PASS

The two endpoint gaps and the half-interior gaps are the only candidate radii, with ties on a null set. A common gamma normalization of independent exponentials leaves the witness unchanged. If Z is the larger endpoint exponential, integrating the interior cutoff at 2Z gives 2∫₀¹(1-u)(1-u²)^(n−1)du = B(1/2,n)−1/n, including probability one at n=1. For T=n exp(−2Z), the conditional density tends to Gamma(1/2,1); an integrable envelope follows from (1−t/n)^(n−1)≤exp(−t/2) for n≥2. The gamma denominator differs relatively from n by o_P(1/log n) even after dividing the deviation bound by the order n^(−1/2) rare probability, so the limiting radius cdf is erfc(exp(−y/2)). Exchanging endpoints fixes the radius and witness event and flips the label. Independent rational expansion and factorial comparison for n=1,…,20 corroborates the exact probability (branches/426cb915-c17f-4719-aea2-02c0aa98a796/endpoint_probability_check.py). Frozen check.py was inspected, not executed; its finite quadrature and simulation logic cannot establish the conditional limit.

## originality

PASS

The supported claim is the weighted endpoint-versus-interior witness probability and its conditional non-Gumbel radius law, not the exponential spacings representation, unmarked coverage threshold, or unweighted Gumbel limit.

## value

PASS

The endpoint mark is geometrically canonical for interval coverage and cannot be read off a usual coverage statistic. Its exact rate quantifies how often boundary rather than interior gaps control the radius; the conditional law shows that keeping the rare mark changes the limiting fluctuation profile despite the familiar unconditional scale.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

For t=2n−1, LTE gives the exponents 2a+1 and b. The normalized integer (4^t−1)/3^(a+1) is t/3^a modulo 3, by expanding powers of 4^(3^a). Consequently the digit is 0 mod 3 if b<2a+1 and 2 mod 3 otherwise; for b≤2a+1 its mod-5 digit is 2(t/5^b)3^(−b), and for b>2a+1 it is 5. CRT gives independent valuation densities and four equiprobable 5-adic units in each stratum. Conditional on b≥1 the tail at b≥2a+1 sums to (2/3)/(1−1/75)=25/37; equality uses 4/5 of that tail and strict excess 1/5. The five residue classes for t→t+2 give three deterministic pairs and the two stars sharing exactly (6,9). For arbitrary N, count each included (a,b) stratum via at most eight congruence classes, each with O(1) discrepancy; O((1+log N)^2) strata suffice and the omitted 3- and 5-adic tails have O(1/N) total density. Shifted indices use t≤2N+1. Independent replay `python /workspace/branches/audit_arithmetic_reproduction.py 4` stripped factors of 15 from 10001 actual integers, saw exactly 20 pairs in the first 10000 trials, and found a maximum absolute deviation 47/37 from the exact rational predictions. The frozen verification script was inspected, not executed; the finite sample is only corroboration.

## originality

PASS

The sequence and its pointwise digit computation are prior art, as acknowledged. In the closest primary statement and indexed comparisons, no equivalent exact adjacency distribution, support and discrepancy statement for this sequence was found. The independent claim is the adjacency result only.

## value

PASS

For an already studied composite-base automatic sequence, this gives its exact directed adjacency support, weights, and quantitative interval counts. In particular the value 37 and the intersecting-star structure come from competing prime valuations and not from automaticity or the marginal law alone. They are concrete invariants useful for subsequent word and correlation studies; no claim of a sharp discrepancy exponent is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.

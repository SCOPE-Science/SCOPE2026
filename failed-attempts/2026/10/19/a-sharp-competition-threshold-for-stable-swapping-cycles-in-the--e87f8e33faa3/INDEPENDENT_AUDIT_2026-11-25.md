# Independent mathematical audit

## correctness

PASS

The strict existence and stability classification checks out. Adding/subtracting the swap equations gives S=2 log(R)/(1+k) and (1−k)Sδ=4 atanh(δ). Strict increase of u gives the unique positive branch. Exchange symmetry gives the squared symmetry-reduced Jacobian B²; the quadratic Schur test reduces to v<(1−k)/(1+k) and D<1, since v<1. v decreases and S increases; d(log(xy))/dδ=2(δ−atanh(δ))/(δ(1−δ²)atanh(δ))<0, so D is strictly increasing from below one to infinity. At the lower root, 1−D=2(v−δ²)/(1−δ²), giving the unique cutoff. Read the upper-root equation also at k=0, as the proof does. The threshold is a supremum, not an attained largest stable coupling. Unit-modulus wording applies to actual boundaries of the stable window: at the coalescence B has two −1 eigenvalues; at a formal upper root above k_* trace(B)<−2 and det(B)=1, so no multiplier has unit modulus there. The supporting script was inspected, not run. Independent rational Laurent-polynomial checks and bounded numerical bisection are in /workspace/branches/365b7c3a-8d65-4a41-8743-e9252933bb10/record3_replay.py (k_*=0.277839040264087; k=.03 gives R endpoints 8.915749063958 and 14.760100029033). The replay verifies the algebra and rounding, not continuum validity.

## originality

FAIL

A distinct indexed record, SCOPE-20261102-c3fcc7a39530, states the same nonzero-coupling theorem, including complete strict stability interval and the same cutoff; this is demonstrated statement-level coverage, not established earlier priority or an inference that the two records were developed independently. The decoupled k=0 case omitted there is an immediate scalar/product specialization, not a surviving substantially distinct finding.

## value

PASS

The exact all-growth cutoff and stability window for symmetry-generated off-diagonal orbits are meaningful mathematical classifications, not a single numerical bifurcation check. The k=0 extension alone would not justify a repaired distinct finding after the overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.

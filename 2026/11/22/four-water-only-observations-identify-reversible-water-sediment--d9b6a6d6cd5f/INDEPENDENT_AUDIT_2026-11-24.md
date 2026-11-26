# Independent mathematical audit

## correctness

PASS

The normalized response equals the (1,1) entry of exp(tK), where K has diagonal (-A,-D) and positive off-diagonal entries a,b. Its Laplace transform is (s+D)/[(s+A)(s+D)-B] with A=a+theta*d, D=b+e and B=ab. AD>B gives positive decay roots; the polynomial has value -B at D, giving strict interlacing and strictly positive modal weights. The known y0=1 makes the two recurrence equations invertible: y2-y1^2 is the positive weighted variance of the two sampled roots. The roots and weights recover A1,D,B uniquely. Independently, differentiating exp(tK) by Duhamel's formula with respect to its first loss, using the similar matrix with off-diagonals B,1, gives minus the convolution of its positive (1,1) response with itself, so the second reading is strictly monotone in A2. The full positive one-condition fiber is B/D<a<A1. Equivalently the scalar inversion can be bracketed by the images of the two fiber endpoints under A2=A1+(theta2-theta1)(A1-a)/theta1, in either intervention order. Recovering a,b,d,e uses only nonzero denominators. Padding fewer than four scalar components of a putative continuous injection with zeros contradicts invariance of domain on the open positive orthant. This proves the sharp count only for the stated fixed designs and given initialization. Independently generated matrix-exponential observations and inverted them at 65-digit precision in /tmp/opencode/frozen-review-replay.py (compartment), including the reported example and an example with theta2<theta1; both recoveries had absolute error below 1e-54. Frozen support was inspected, not run. There is no noise-conditioning or physical-selectivity guarantee.

## originality

PASS

Pass limited to the exact globally valid three-plus-one selective-loss design and its sharp measurement count for this observation map, with the positive ambiguity fiber made explicit. Neither the single-condition transfer-function ambiguity, Prony inversion from four samples including time zero, nor the topological dimension argument is independently new. The strongest inspected candidates cover these ingredients or structurally different interventions; none of the inspected passages provides or mechanically implies the strict one-reading resolution under a selective change of the first-pool degradation multiplier.

## value

PASS

In a genuinely confounded passive-tracer compartment model, the output-only ambiguity can persist even for an entire noiseless trace. The theorem locates exactly the new measurement that resolves it, attainably at the dimension lower bound, and works on the entire strictly positive domain rather than only generically or locally. This distinguishes structural identifiability from experimental feasibility and is useful as an ideal-model design benchmark without making a field claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.

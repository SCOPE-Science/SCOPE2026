# Independent mathematical audit

## correctness

PASS

The independent product of geometric multiplicities has constant mass on configurations of total weight n, so conditioning is exact. At β=c/√n the mean and variance integrals are respectively β^−2 times π²/6 with O(β^−1) error and β^−3 times π²/3 with relative o(1) error. Removing the first m=o(√n) coordinates costs O(nm) variance. For both the full and tail sums the centered third absolute moments sum to O(β^−4), by bounding j³ times the third geometric moment by a constant times j³ exp(−βj)/(1−exp(−βj))³ and summing. For the uniform local estimate, retain a contiguous block j∈[a√n,b√n] above the cut: squared-angle estimates bound the cosine sum below for |t|≤δ/√n, uniform Riemann sums of 1−cos(uj/√n) bound it for δ≤|u|≤M, and the geometric-sum bound O(1/|t|) dominates outside M/√n by taking M large. This gives an integrable Gaussian bound after variance rescaling and an exponentially small far tail, so Fourier inversion yields the stated uniform o(n^−3/4) error. The resulting likelihood ratio of the low coordinates tends to one in probability and has mean one; twice its mean negative deviation equals the mean absolute deviation, which tends to zero. For the point process, the sums of individual run probabilities tend to the stated intensity by Riemann sums. With t distinct starts grouped into s clusters the required number of absent parts is at least rs+t−s, and only O(n^(α_r s)) locations are possible. This suppresses all s<t terms in joint factorial moments. Omitting repeated or adjacent starts from the product-of-means sum costs O(n^−α_r); all remaining disjoint windows factor. Bounded factorial moments and Poisson moment determinacy give independent limiting interval counts and the locally finite vague limit; the two order-statistic formulas are exactly Poisson count tails on [0,y], including y=0.

## originality

PASS

The chain mex itself is established, as is the independent-process conditioning framework. The inspected chain-mex papers derive identities or pose an asymptotic question about sums; they do not give the point process of all starts. Nearby catalogue results use different observables. The distinctive claim is the scaling and nonconstant intensity for all starts, including a proof that overlapping starts do not create a cluster process in the limit.

## value

PASS

The exact intensity resolves the onset scale of a previously studied partition statistic and supplies all fixed-order starts and independent interval counts as well as the first gap. Proving that overlapping absence events are asymptotically negligible and that the conditioning is harmless on the growing window explains why the limit is Poisson rather than clustered. It is more informative than a standalone first-point fit or enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.

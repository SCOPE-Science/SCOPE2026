# Independent mathematical audit

## correctness

PASS

The two edge increments 1−exp(iθ) and 1−exp(2iθ) give the stated rank-one transfer-current projector at nonzero frequency and the zero matrix at discrete zero. Inverting the scalar denominator 3+2cosθ gives the periodization of g(r)=(-t)^|r|/√5. The squared cross-channel kernel is a pair of one-sided geometric series on r≥0 and r≤−1; its transform is (1−t)²(1−s)(1+exp(iθ))/(5D). The long-channel diagonal is 1−g(0) at r=0 and −g(r) otherwise before squaring, yielding the same covariance diagonal as the short channel. The upper band is increasing in x=|cos(θ/2)|; its derivative has sign of (1+s)^2+4sx²−12sx≥s>0. The lower band decreases in x to zero at x=1. Triangle exchanges force each constant-on-tree edge weighting to be constant on both channels, so there is only one exact null direction. Squaring the periodized kernel gives an alias error bounded by O(nt^n): the sum of products of two translates at separation hn is O((1+|h|n)t^(|h|n)). Deleting the zero projector subtracts P0/n from every current entry; the cross term gives +2P0∘P(θ)/n in the covariance and the marginal gives −diag(P0)/n. The constant-square term affects only j=0, where the positive branch stays separated from zero. At small nonzero frequencies the lower-band unit vector tends to (1,1)/√2; the Rayleigh shift is 1/(2n). Taking j=1 gives the upper bound for the scaled minimum, while all minimizing frequencies tend to zero and the nonnegative limiting lower band gives the reverse bound. Thus both limits and the stated ratio follow with the unnormalized Euclidean convention. In `python3 /workspace/independent_checks.py 4`, a separate Fourier-frequency convolution of the current projectors (no geometric Green formula) gave nλ_min^+=0.5065023 and λ_max=0.3575523 at n=640; this is a bounded cross-check, not the proof. The supplied checker was inspected, not executed.

## originality

PASS

Best-knowledge pass for the evaluated squared-cycle covariance bands and the missing-mode correction yielding the sharp floor and condition ratio. Graph enumeration and general transfer-current formulas are credited as prior. A same-day graph analogue is compared on substance, not dismissed on date.

## value

PASS

The least nontrivial variance over edge Fourier channels measures a natural conditioning problem on a canonical two-length periodic graph. The limiting lower band suggests an order n⁻² grid minimum; the actual n⁻¹ floor and its exact coefficient identify a different fluctuation scale imposed by the finite graph. This is not just a recomputation of the number of spanning trees.

The dated certificate retains the supplied scientific assessment, sources and limitations.

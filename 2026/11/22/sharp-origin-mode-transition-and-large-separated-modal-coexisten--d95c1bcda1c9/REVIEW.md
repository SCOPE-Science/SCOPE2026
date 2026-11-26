# Independent mathematical audit

## correctness

PASS

Geometric-series normalization and its twice-differentiated version give total mass one. Each affine comparison to zero is strictly negative for all b>0 unless q^kT_k>2; the latter set is finite by exponential decay, nonempty via k=1 if θ<2, and empty when θ≥2 by the decreasing ratios q(k+3)/(k+1). This gives the exact threshold including all ties and θ=2. Independent rational checks (python /workspace/independent_checks.py 2) find 35 competitors at θ=1/5, unique minimizer k=6 and b=31031/781688. For an analytic tail certificate the adjacent difference has the sign of b(k+2)(9−k)−1; since 24<1/b<28, the signs are just decrease for k=0,1, increase for k=2,…,5, and decrease for all k≥6. For minimizers as θ→0, compare with k≈x/θ. The lower bound (exp(k log(1+θ))−1)/(θ²(k+1)(k+2)) excludes both kθ→0 and kθ→∞ (including bounded k at the first endpoint). Along any convergent subsequence of rescaled minimizers the limit is therefore an interior global minimizer of (exp(x)−1)/x², by comparison to floor(y/θ) for each y>0. Its derivative numerator has derivative (x−1)exp(x), so its minimum is exactly x=1 (not before x=1 as in RESULT.md:89); the single positive zero is in (1,2), as claimed. High-precision independent root solving confirms both constants. The qualitative convexity typo does not affect the minimizer or the finding. No uploaded checker was executed.

## originality

PASS

The supported distinct contribution is the complete first global origin transition with a certified remote tie and sharp inverse-rate/quadratic asymptotics. Comparison to zero by an affine difference is easy, and qualitative two-local-peak behavior and the law are known; neither is claimed here as a new result. Relevant retrieval failures are not evidence of absence.

## value

PASS

A global mode of zero is substantively different from a local shoulder or from a positive most probable count. The exact rational witness rules out a generally single-peaked interpretation and the asymptotics show the first jump can become arbitrarily large while the shape parameter is only of order θ². The exact finite criterion, infinite-tail proof and scaling answer a meaningful question in the introduced model, without claiming later positive-to-positive transitions.

The dated certificate retains the supplied scientific assessment, sources and limitations.

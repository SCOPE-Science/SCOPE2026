# Independent mathematical audit

## correctness

PASS

Gaussian summability gives finite random total intensity almost surely for each K. Independent gamma mixing gives independent Bernoulli indicators with p=1−(1+u)^(-K), u=exp(−E). On either sign in a fixed centered energy window, Kh²=(4A² log K)^(-1), the mesh is A^(-1)(1+o(1)), and Ku=A^(-1)e^(−y). Taylor's formula bounded by K(K+1)u²/2 gives the rare-success estimate uniformly. The log Laplace functional for each compactly supported nonnegative test is then a Riemann sum plus an error bounded by a multiple of the sum of squared probabilities, which tends to zero. The independently marked limit has intensity e^(−y)dy per side. Vague convergence alone does not justify the farthest-site limit: summing the dominating Ku beyond T+t and bounding by a boundary cell plus Mills' inequality gives an upper bound e^(−t)/A+e^(−t)√(log K/(T+t)) per sign. Fixed intervals (t,M] and M→∞ give the complementary bound. The maximum individual tail probability vanishes, so the product of no-detection probabilities tends to exp(−2e^(−t)). Since T+t>0 eventually, the event equality holds even with no detections or only a detection at zero. Tightness gives the radius scale, while Kh²→0 at the nearest nonzero site makes p_{1,K}→1. The explicit mesh gives A=(log K)^(3/2)/2 and the stated additive −log 2 in T. Inspected verify_edge.py without running it: its nominal gamma-integral comparison is two algebraically equivalent marginal formulas, a floating-point consistency check, not independent integration or a limit proof.

## originality

PASS

The Cox zero detector, its gamma–Bernoulli marginal, fixed-candidate consistency and the general Poisson rare-event mechanism are prior. The supported contribution is explicit edge centering, including log A and its constant for a concrete dense grid, the two-sided marked intensity, and control of all sites beyond a moving threshold in the refining-grid regime. No novelty is assigned to gamma mixing or the generic Poisson limit machinery.

## value

PASS

A fixed-set consistency guarantee is misleading on a refining mesh. The edge limit supplies an explicit spatial uncertainty scale and centered radius quantiles despite virtually certain classification error somewhere. The marked point process also describes the two separate sides. This is a useful theoretical calibration for the exactly linear, on-grid independent idealization, not a general or practical zero certification method.

The dated certificate retains the supplied scientific assessment, sources and limitations.

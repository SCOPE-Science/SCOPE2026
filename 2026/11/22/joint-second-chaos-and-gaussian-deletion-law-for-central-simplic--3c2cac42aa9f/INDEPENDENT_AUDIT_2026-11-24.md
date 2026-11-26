# Independent mathematical audit

## correctness

PASS

For minor separation d in [0,pi], origin containment requires a third angle in an opposite arc of length d. The conditional probability is d/(2pi); uniform rotation makes the first projection vanish. Fourier integration gives odd eigenvalues -1/(pi^2 m^2), each twice, and variance 1/48 for the canonical pair kernel. The remaining canonical third kernel has variance 3/16-3/48=1/8. Applying the orthogonal U-statistic variance formula gives 3/[8(n-1)(n-2)]. Averaging all leave-one-out depths gives D_n exactly, so the deletion second moment is the difference of the variances at n-1 and n, including at n=4. This gives the stated jackknife expectation ratio. Conditioning on the first point, the included-triangle statistic has first projection h_2(X_1,·) with a canonical pair remainder of variance O(n^-2). Its combinatorial weight is 3/n, giving the factor 6 in the linear empirical term. Rotate empirical Fourier pairs by the deleted angle: the quadratic term is invariant and the linear term uses the same limiting cosine coordinates. The canonical variance bounds and square-summable eigenvalues justify joint truncation. For t>=0 the truncated quadratic variables are bounded above by 3/4, so their transforms converge. Integrating Gaussian pairs, then differentiating the odd Euler product and subtracting its value at zero, yields the stated hyperbolic formula with q=sqrt(6t)/2. Wick contraction gives 432 sum lambda_m^3=-9/20; first–third parity gives zero ordinary covariance. All variances and the q=0 limit agree with the Gaussian deletion law. The claim itself is unchanged; the repair credits the exact prior variance and clarifies the transform passage to the limit.

## originality

PASS

The repaired contribution is the shared-coordinate joint law for a depth and its single deletion, with explicit mixed dependence and transform. The central marginal and its spectrum, the exact finite central variance, and variance consequences of deletion averaging are clearly separated from that contribution. No same-day publication order is assumed.

## value

PASS

Sensitivity to a single removed observation is a concrete issue for central depth. A normal deletion marginal and zero linear covariance with depth do not diagnose the nonlinear dependence; the explicit joint law shows why they do not and supplies an exact mixed transform for this benchmark. The marginal limit, already known variance, or routine ratio alone would not be a sufficient contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.

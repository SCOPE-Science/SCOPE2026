# Independent mathematical audit

## correctness

PASS

The published unbiased sample variance and Euclidean sphere match the frozen definitions. Atomlessness avoids zero sample variance; column standardization yields iid bounded columns of fixed squared length N−1 and zero sum. The Gram SLLN to P_N follows from row exchangeability, which fixes its diagonal and off-diagonal expectations. Expanding the squared modulus and using joint sphere rotational invariance (not independent projected blocks) gives the claimed kernel H_m. Its coefficient product ∏_{j<r}(1+j/m)^−1 has first-order term −r(r−1)/(2m); a uniform O(r⁴/m²) remainder is summable against B^r/r!, giving the claimed −x² exp(−x/4)/(32m) curvature contribution. This gives the general leading constant and at N=2 the Gram matrix is exactly P_2. At N=3 a tangent matrix is determined by its three trace-zero diagonal entries and its squared Frobenius norm is three times their squared length. A single-column increment zzᵀ−P_3 has squared norm 2, and by exchangeability its diagonal covariance is a scalar on the trace-zero plane, with scalar 1/3 by the trace. The Frobenius covariance is therefore I_2. The bounded-vector CLT and a Taylor expansion with zero linear term give the χ²_2 fluctuation with γ>0. Independently evaluating the three possible first kernel arguments 0,2,4 with weights 1/9,4/9,4/9 and the cross term at 4/3 reproduced C_3=0.1285958736506253, β=−0.2014753345640410 and γ=0.0378204722311850 by elementary Python arithmetic. For deterministic Gaussian right-tail cutoffs an interior asymptotic size forces convergence to the unique scaled limit quantile; the same continuous limit under each alternative gives that size as power. The underlying uniform/Gaussian experiments separate already by the event that all coordinates lie in the uniform support, with uniform probability one and Gaussian probability exponentially small. The Hellinger bound in the original is valid. The uploaded numerical checker was inspected, not executed. The χ² assertion is for T=M_m/A_m, only at N=3, and only in the stated fixed-sample iid regime.

## originality

PASS

The verified motivating paper uses exactly this statistic but its limit theorems grow the sample size at fixed dimension. The strongest retrieved neighboring fixed-sample high-dimensional statements concern different functionals. Neither the primary source nor the inspected distinct catalogue records give this statistic's fixed-N dimension-growth constants, universal second-order calibration at N=3, or alternative-side rejection law.

## value

PASS

Three rows are the first nonconstant standardized Gram geometry, so this cutoff is structurally selected rather than an arbitrary small sample. The common leading constant would not suffice to determine test power; the explicit universal second-order law does, even for a full-sample alternative asymptotically separated in total variation. It therefore identifies a concrete failure regime of a published test without contradicting fixed-dimensional consistency or claiming a general impossibility of testing.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

The common Poisson clock supplies a stationary Exp(r) age and couples at the first future reset; conditional on the age the log values are independent normals of mean at and variance σ²t. The one-coordinate rational transform gives the stated asymmetric exponential survival, including c_1. Independently scaling time by y gives the phase rz+n(1−az)²/(2σ²z), with unique strict minimum at z=1/s_n and curvature ns_n³/σ². The Mills integral displayed with 0 to infinity should be read as the compact saddle-neighborhood contribution specified in its surrounding sentence, with both sides restricted accordingly; it is not a global integrable Mills replacement for a>0. On the rest of the Mills region the Gaussian Chernoff bound and strict phase gap apply (small and large cutoffs use phase divergence or the reset weight). The a>0 non-Mills region costs at least r/a>2r/(s_n+a)=k_n. Multiplying the local amplitude s_n^(n/2)/(s_n−a)^n by the Gaussian saddle factor, age density and Mills prefactors gives the printed C_n, including C_1=c_1. The quantile substitution, 1<α_n<n, derivative 1/Δ−1/s_n<0, monotonicity in n, slowly varying log factor and three limiting regimes follow from the two equivalent expressions for α_n. Independent normalization checks at r=.7, σ=1.1, n=2,4, multiple y and all drift signs were diagnostic only; the n=4 ratio at a=1.25 is still about .467 at y=80, consistent with slow convergence. See branches/6166fad2-2c5b-4f00-9d2a-b485c740f2d6/ordinal-4-drift-extremes-check.md. Uploaded code was inspected, not executed. No error bound or simultaneous growing-n limit follows.

## originality

PASS

Qualified PASS for the nonzero-log-drift, arbitrary-fixed-n sharp orthant equivalent and the resulting explicitly normalized exponent hierarchy. The marginal law, centered residual exponent and law of the log vector as a distribution family are not new. The closest broader density formulas can be used as a starting point for another proof, but the inspected results do not state a sharp noncentered orthant theorem that evaluates this equivalent by substitution alone.

## value

PASS

The finite-n coefficient and rate predict collective risk that cannot be read from identical marginal Pareto laws. Saturation versus square-root versus linear growth separates drift signs at the level of iterated exponents, while the logarithmic correction quantifies how slowly one enters that regime. This is meaningful for a shared-shock model without claiming uniform control, field prediction or a new class of distributions.

The dated certificate retains the supplied scientific assessment, sources and limitations.

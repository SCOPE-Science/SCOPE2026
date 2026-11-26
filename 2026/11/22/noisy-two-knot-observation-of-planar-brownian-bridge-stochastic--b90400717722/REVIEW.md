# Independent mathematical audit

## correctness

PASS

For doubled area, conditioning on the true knots gives the oriented determinant of the two positions: the residual bridges have mean-zero mixed and antisymmetric area terms. The bridge drift cancels in the antisymmetric stochastic integral, so its variance is 2∫t(1−t)dt=1/3. Independent spatial coordinates let Gaussian regression act by the determinant of K(K+ηI)^−1, equal to D/(D+ηT+η²), on the observed determinant. The latter has variance 2det(K+ηI). This proves the estimator and risk by orthogonal projection; at singular zero-noise designs the true knot determinant is identically zero. All zero-gap designs capture zero variance and an interior design captures a positive amount. At fixed outer-gap sum u, the objective is proportional to v²/(Av+B) for v=ac and A=1−u+2η>0, B≥0, strictly increasing for v>0. Thus both outer gaps equal x. For positive noise the change y=x/(1−2x) gives y^4/Qη with all seven coefficients of Qη positive, and 4Qη−yQη' has exactly one sign change, hence exactly one positive root counted with multiplicity. The maximum is simple and differentiable in η. The stationary polynomial is negative at x=1/3 for η>0; at fixed x just below 1/3 it is positive for sufficiently small and sufficiently large positive η, proving both endpoint limits by uniqueness. A stationary x(η) requires a double root in η. In the only feasible interval ((3−√3)/4,1/3), the discriminant changes sign once, at the strictly increasing cubic's unique zero. Its positive double root supplies the lone turning noise. Thus the strictly outward then inward movement, including trisection at η=0, follows. Independent high-precision evaluation gave x_c=0.323899435630521192745… and η_c=0.135922253173019090393…, with relative captured-information gain 0.003657153… over trisection at that variance.

## originality

PASS

The supported distinct result is the positive-noise two-vector-knot optimum and its nonmonotone law; neither the classical noiseless conditional-area identity nor generic Gaussian regression is claimed as new. The closest same-day Resultary theorem overlaps substantially in target and Bayes criterion, but concerns a different measurement operator and does not cover this design.

## value

PASS

Lévy area is a standard nonlinear bridge functional. Even with only two full position measurements, noise changes the exact design in opposite directions at low and high noise. The scientific point is this strict reversal and unique algebraic turning variance, not the modest numerical gain: the exact Bayes risk exposes the trade-off between the area determinant and the observation covariance and provides a test case for noise-dependent area designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

Taylor expansion in powers δ yields column moment vectors u_r and row node monomials v_r. The leading second exterior-power norm is δ sqrt(µ2) sqrt(6+2t²), while the third is δ³(1-t²)sqrt(µ2 Δ): the 1/2 quadratic Taylor factor cancels the Vandermonde determinant 2(1-t²). Largest singular value tends sqrt3, so the ratio gives the exact smallest-singular-value coefficient. Reflection symmetry removes odd moments, µ2>0 and Δ>0 avoid rank loss. For t>0, d(log f)/dt=-2t/(1-t²)-2t/(6+2t²)<0, giving unique midpoint. Independently constructed high-precision Fourier Gram matrices at t=0,.5 and δ=0.002 agreed to about 1e-7 relative error. This checks examples, not the asymptotic universal proof.

## originality

PASS

Batenkov–Demanet–Goldman–Yomdin (2018) and Batenkov–Diederichs–Goldman–Yomdin (2019) derive singular-value scaling orders and bounds for arbitrary clustered Vandermonde samples. Their inspected stated theorems do not give this reflection-symmetric weighted leading constant or universal unique midpoint optimization. Equispaced prolate special cases are not credited. Potential equivalent interpolation-formula literature remains risk.

## value

PASS

The weight-independent optimal placement and explicit conditioning constant address a motivated three-source measurement design question; exact constant sharpens existing mere δ²-order estimates across arbitrary finite apodization. Explicitly excludes nonlinear support recovery and variable-bandwidth limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

The published Shu–Osher stages in integrating-factor coordinates have time-only forcing F(t)=v(t)v(t)^T with v(t)=exp(−tA)b. The completed updates reduce to trapezoid and Simpson: the distinct composite nodes number m+1 and 2m+1 and all weights are positive. Their weighted outer-product sums have exactly the corresponding sample-span ranks. For any uniform spacing s>0 let D=exp(−sA). Distinct real eigenvalues of A map to distinct positive eigenvalues of D, and the local inverse −log(z)/s can be matched by a Hermite interpolation polynomial on those eigenvalues through the required Jordan orders. Thus A is a polynomial in D, so cyclicity of b for A implies cyclicity for D. The first min(d,N) vectors of the D-Krylov sequence are independent; take s=h and h/2. This also verifies the fixed-step claim independently of the frozen zero-count proof (whose induction keeps the degree bound within each remaining exponent under differentiation). The exact Gramian is positive definite because a zero quadratic form forces a scalar exponential to vanish on a time interval, hence its derivatives annihilate the Kalman basis. In the nilpotent example v(t)=(1,−t,t²/2)^T. The absolute three-node Vandermonde determinant is h³/8 and the product of Simpson weights h³/54, giving h⁹/3456. The scaled 3×3 Hilbert determinant is h⁹/(4·2160)=h⁹/8640; the congruence determinant is one since trace A=0. Trapezoid is rank two in d=3 and the ratio for Simpson is 5/2, for determinant, not ellipsoid volume itself.

## originality

FAIL

The same-day but distinct indexed nilpotent-chain result supplies both completed quadrature updates, the node-count rank formulas on that chain, and the full three-state one-panel error matrix. The broader real-spectrum statement is not asserted in that record, but it follows mechanically by substituting the standard sampled-vector rank for the polynomial Vandermonde rank in the already available quadrature reduction. The determinant example is mechanically implied by the other record's exact error matrix. This is a coverage finding, not an assertion about which same-day result appeared first.

## value

FAIL

Knowing when Cholesky can first succeed in exact arithmetic, and recognizing that matrix convergence need not control relative determinant near a singular start, are useful. But here the thresholds simply count the already known quadrature sampling directions with standard sampled cyclicity, and the quoted determinant bias is a recomputation of an already indexed exact error matrix. No distinct difficult limit, additional quantitative guarantee or new obstruction remains in the frozen scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.

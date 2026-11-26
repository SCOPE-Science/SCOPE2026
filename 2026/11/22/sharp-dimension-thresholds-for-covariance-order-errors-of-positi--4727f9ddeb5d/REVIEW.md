# Independent mathematical audit

## correctness

PASS

In the lag variable the vector is (1,t,t²/2!,…), so with zero-based indices the error is E_ij=δ_(i+j)/(i!j!), where δ_d is numerical minus exact moment. For n≤m all entries vanish; at n=m+1 only (m,m) can be nonzero. The principal block at (m−1,m+1) has zero first diagonal and nonzero off-diagonal δ_(2m)/[(m−1)!(m+1)!], which certifies both signs independently of higher moments. Exact covariance is a positive definite polynomial Gram matrix; strict weights and distinct nodes give numerical rank min(n,r) by Vandermonde evaluation. The published stages reduce under the integrating factor to trapezoid and Simpson, respectively. Expanding the first omitted monomial on a panel gives h³/6 and h⁵/120, respectively, independent of panel origin by exactness on lower degrees. Hence the global omitted moments are Th²/6 and Th⁴/120, the rank-one coefficients Th²/6 and Th⁴/480, and the minors −T²h⁴/144 and −T²h⁸/518400. Continuity of each strictly negative minor at fixed T,N justifies the stated Hurwitz perturbation, with no uniform radius asserted. Inspected the supplied moment/rank checker and verification notes; the 56 reported cases are bounded support, not a rerun or a proof of the general claim.

## originality

PASS

Pass for the finite-horizon signed-error classification by the first omitted moment and its exact dimension thresholds, not for the SSP stage reductions or application rank staircases in isolation. The same-day rank record has stronger coverage of those staircases; the older trapezoid order result already supplies the basic one-sided obstruction in a related form. Neither establishes the complete general phase including Simpson and indefinite errors at every positive panel count, and no equivalent was located in the bounded comparisons.

## value

PASS

The dimension threshold is a concrete diagnostic for a motivated question: positivity of an integrating-factor covariance update does not ensure either Loewner bound on the true covariance. The witness uses only the first omitted moment and survives later moments and arbitrarily many panels, even when the numerical covariance has full rank. It is an exact finite-horizon obstruction, not merely the familiar quadrature order or a rank-deficiency example.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

For the explicit Itô Euler update, normalize the second diagonal moment to t=λs. Put q=1+λ, u=1−2h, v=1−qh. Independence gives the diagonal transfer K=[[u²,2h],[2h,v²]] and forcing 2h(1,λ); the cross moment is multiplied by uv−2h. Its modulus is at most (u²+v²)/2+2h, a Rayleigh quotient of K, so the positive Perron eigenvalue controls all modes. A positive diagonal Perron vector is realizable as an initial second moment. For 0<h<1, the first minor of I−K is 4h(1−h) and the determinant is 4h²Fλ(h); F decreases to −1 and has the stated smaller quadratic root. For h≥1 the u² diagonal and nonzero off-diagonal force the Perron root >1. Fλ(1/2)=−(q−2)²/4, and ∂qFλ=2(1−h)(1−qh)>0 at the root for q<2, verifying the monotonicity and endpoint claims. In the stable range the stationary backward series is L²-convergent by geometric decay and orthogonality of distinct additive innovations conditional on the multipliers; synchronous coupling gives uniqueness in L². The stationary mean is zero since the mean map is stable. Solving the two forced moment equations verifies the stated variances and their difference h(1−λ)²/(2Fλ); each excess numerator stays strictly positive up to h*. At or beyond the boundary, projection on the positive Perron eigenvector contradicts the forced finite stationary equation and from zero gives respectively linear/geometric growth. This remains valid at λ=1,h=1/2, where K has a second eigenvalue −1; the forcing lies on the +1 eigenvector. The mean map is stable throughout 0<h<1.

## originality

FAIL

Distinct indexed Resultary entry 494cc24da1b8 proves the larger two-parameter Itô Euler theorem for all λ>0 and perturbation strengths δ≥0. The frozen stability boundary, finite-moment law and stationary covariance are the critical scaling δ=λ⁻¹ᐟ²; the claimed normalized anisotropy is one subtraction of that entry's exact formulas, not a new independent invariant. The matched entry's path is dated November 8, later than the frozen October 26 path. This establishes present mathematical coverage, not earlier publication, derivation or priority.

## value

FAIL

The step-size frontier and anisotropic stationary distortion are useful for tuning explicit simulation of this sampler, but are not substantively new relative to the exact all-strength indexed solution. The scalar variance subtraction and elementary mean-stability comparison do not create a new regime or independently valuable unknown invariant. The review does not deny the intrinsic practical value of the formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.

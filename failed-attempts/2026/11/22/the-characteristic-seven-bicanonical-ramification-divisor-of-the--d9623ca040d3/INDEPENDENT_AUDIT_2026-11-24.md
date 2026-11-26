# Independent mathematical audit

## correctness

PASS

Reconstructed the complete bicanonical series by adjunction and the jet pivots at orders 0,1,2. In a separate exact computation (python3 /tmp/opencode/frozen_nov24_algebra.py, quartic part), put F=(1+(x+h)^4)/(1+x^4) and expand its fourth root as A=F^2/A^7, using A^7=1+a_1^7 h^7 modulo h^8. This differs from the frozen recursive fourth-power method. It recovers the exact pivot 5x^2/(1+x^4)^4, both zero determinants, and the stated seventh-row determinant. The simple noncoordinate zeros are 20 allowable choices of x times four y choices. At a coordinate point the tangent has order four and the six conic orders are 0,1,2,4,5,8. In positive characteristic one must justify identifying the intrinsic coefficient with the excess of order sums: in general the coefficient is at least the excess. Here the binomial leading-coefficient determinant at the coordinate points is 3 modulo 7, so equality holds there; at the other zeros it follows from the simple local Wronskian and integral excess. Degree 116 confirms completeness. Exact independent projective point enumeration using F49=F7[s]/(s^2+1) gave (coordinate, noncoordinate)=(0,8) and (12,80). The zeta product follows by counting quadratic orbits, and concerns reduced finite support, not the curve's zeta function. Frozen scripts were inspected, not executed.

## originality

FAIL

The principal claim, including the entire weighted divisor and not merely generic nonclassicality, is a short corollary of the existing maximal-curve Frobenius linear-series relation and the standard ramification-degree formula. This was established by a covering implication, not by identifying a verbatim prior table or by treating unavailable material as adverse evidence. The displayed coordinate Wronskian is a valid direct computation of that divisor, but is not an independently claimed new ramification invariant.

## value

FAIL

The model is natural and the verification is useful as an alternate computation, but the proposed standalone contribution is the divisor, weights, arithmetic support and generic orders, all mechanically forced by the prior Frobenius series once one notes a rational hyperflex and the noncoordinate tangent order. The coordinate determinant and pivot certify the same conclusion in one trivialization rather than supply a separate motivated new invariant. No scientific repair is made just by adding the prior proof alongside the direct calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

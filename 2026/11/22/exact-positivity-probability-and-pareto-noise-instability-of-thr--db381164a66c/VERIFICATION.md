---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Affinely map the hull to [0,1] with middle knot t. Independently solve for the middle cardinal spline as Bx+Cx^3+D(x-t)_+^3. The natural condition at one gives D=-C/(1-t), the zero value at one gives B=-Ct(2-t), and the value one at t gives C=-1/(2t^2(1-t)). Its integral is W1=(1+t-t^2)/(8t(1-t)); exactness on constants and x gives W2=1/2-tW1 and W0=1/2-(1-t)W1, matching all the frozen weights. The ordered sample has density 6; endpoint position and hull length give Jacobian L, so t is uniform by integrating 6L over 0<L<1 and 0<X0<1-L. W1 is strictly positive and reflection swaps the endpoint weights. W0<0 exactly for t<c=(sqrt(13)-3)/2, and c<1/2, so the negative regions are disjoint and the nonnegative mass is 1-2c. The norm is the sharp absolute weight sum, attained by the weight signs, and is (1-t+1/t)/4 in the left negative region. The function is strictly decreasing there; solving its quadratic inverse and doubling gives the exact survival function for z>=1, including the atom at one and the 1/(2z) tail. The moment criterion follows by integrating the tail. Conditionally the Gaussian error has standard deviation sigma||W||2 and absolute mean sqrt(2/pi) times that standard deviation. Since ||W||1/sqrt(3) <= ||W||2 <= ||W||1, the established tail forces both claimed divergences after averaging; the endpoint coefficient 1/32 for t^2||W||2^2 also agrees. The supplied symbolic and finite tests were inspected, not executed.

## originality

PASS

Natural-spline weight calculation, uniform spacings, and conditional noise propagation are standard ingredients. The inspected antecedents do not supply the random-hull positivity mass or the exact norm law for these weights. The comparison credits exact pointwise three-knot instability and related random quadrature heavy tails, but distinguishes the integral functional and the exponent-one law that makes even the unconditional absolute noise moment diverge.

## value

PASS

Three knots are the smallest nontrivial natural cubic rule, with the two-knot case linear and positive. The exact sign probability and norm distribution document that an otherwise canonical nonparametric integration rule is not merely sometimes sensitive: random near collisions give an infinite average absolute response to independent Gaussian measurement noise. The exponent and tail constant quantify this minimal boundary case and distinguish it from other three-node random quadrature schemes, rather than merely repeating the formula for a spline area.

The dated certificate retains the supplied scientific assessment, sources and limitations.

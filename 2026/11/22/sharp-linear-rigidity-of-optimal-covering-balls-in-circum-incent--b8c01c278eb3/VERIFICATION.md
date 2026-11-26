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

For an origin-containing ball write t=|z|<=T. Each p_i=rho*u_i is on the union boundary: for j!=i its squared distance to c_j is 1, and moving radially outwards increases that distance by the squared outward displacement; for j=i the distance is already strictly larger. Each proposed optimal ball satisfies |x|^2<=c_j·x, so if |x|>rho then |x-c_j|^2<=4M^2-|x|^2<1. The bound h<=1/n also follows by summing the barycentric weights of 0, each at least h/(1+h). Thus T^2<=rho^2+t^2-2rho*t*g(w), where w=z/t if t>0 and the product is zero if t=0. Since t<=T and g>=h this forces t<=M. The resulting convex upper bound f(t)=rho^2+t^2-2rho*h*t is strictly below M^2 for t<M, so equality requires t=M and g(w)=h. The latter means that the insphere touches the supporting plane in the relative interior of a facet; these directions are exactly N. The tangent facet polygon in its (n-1)-dimensional plane contains the contact point in its relative interior, so it gives a positive linear support term near each normal, dominating the quadratic normal loss. Compactness away from N proves kappa>0. For d=M^2-T^2<=2M epsilon, the factorization M^2-f(t)=(M-t)(M+t-2rho*h) gives M-t<=2 epsilon/(1-4h^2), hence t>=M/2 in the prescribed range. The angular deficit is g(w)-h<=d/(2rho*t)<=2 epsilon/rho. The triangle inequality yields the displayed bound at all stated epsilons, including zero. A homothet centered along n_j has distance exactly M-T from MN: its squared distance to any other Mn_l exceeds (M-T)^2 by MT|n_j-n_l|^2. Analytic verification is decisive. The read-only inspection of check_geometry.py shows checks on one tetrahedron and sampled nonnegativity of support, not a certified uniform linear bound; no frozen script was executed.

## originality

PASS

Credit Nour with the exact radius, the displayed attaining balls and the inequality that almost immediately gives optimizer exhaustiveness. The sharpness witness also follows directly from Nour's feasible balls. The distinct supported contribution is the explicit linear bound for every admissible near-optimizer of a fixed simplex, obtained by adding a quantitative angular support gap; neither Nour nor the available comparison records establish that bound.

## value

PASS

The known optimal radius does not tell how sensitive all near-maximal balls are to a radius error. The estimate quantitatively localizes an unrestricted candidate center to one of finitely many facet directions in the nonconvex union, with the best possible exponent and a computable fixed-shape constant. No uniform stability under degenerating simplex shapes is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.

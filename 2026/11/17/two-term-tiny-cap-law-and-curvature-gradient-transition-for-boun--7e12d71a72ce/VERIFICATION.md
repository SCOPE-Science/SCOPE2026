---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The signed-short-arc cap equals the exact double tangent-determinant integral. Expanding sin of the curvature turn gives A(s,h)=k h^3/12+(k_ss/480-k^3/240)h^5+O_K(h^7); independent symbolic integration verified both h^5 coefficients. Uniform positivity of curvature guarantees one inverse H(s,t), and the endpoint midpoint coordinate map has Jacobian one, so Pr(M<=t)=2/P^2 int H ds. Inversion and integration by parts yield 2(12t)^(1/3)/P^2 int k^(-1/3) ds + 2t/(5P^2)(2pi-int k_s^2/k^3 ds)+O(t^(5/3)). Jensen and the radius-of-curvature harmonic family yield the circle extremals, J=2pi m^2((1-eps^2)^(-1/2)-1), and eps_m=sqrt(2m^2+1)/(m^2+1). For each arc midpoint, |h|/H is exactly uniform; V^3 maps to z^(-2/3)/3 and the joint total variation limit follows by density convergence and Scheffe; q(s) proportional k^(-1/3) reconstructs k using int k ds=2pi. Remainder fixed curve, not uniform in harmonic frequency.

## originality

PASS

Best-of-knowledge original joint second-order area-cut distribution, sign transition, and arclength-labelled inverse conditional law. General random-polytope cap, short Euclidean-chord and midpoint-distance theorems do not imply a smaller-cap area probability coefficient or the marked inverse.

## value

PASS

Second-order curvature-gradient term distinguishes nonconstant curvature and exhibits a sharp sign transition unavailable at leading order; the rare-chord localization law gives an explicit inverse observable for smooth convex curves. Both quantities are natural in stochastic convex geometry rather than arbitrary numerical slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.

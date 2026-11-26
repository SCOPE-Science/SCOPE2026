---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For any fixed width, the clipped exponential-run chain has the uniform lower bound Q(s)>0 on the transition mass at the right wall, giving uniqueness by minorization; reflection gives symmetry. The end-of-run wall atom and interior mass bound give |C_s−1/2|≤H(s), while the dimensionless right-wall reward is u exp[−(s−x)/u] for positive u. Integrating by parts, with the boundary atoms included, yields P=m_+−s/4+∫C_s(x)H(s−x)dx. The residual is bounded by H(s)∫H using H≥0. Since H→0, the right derivative follows with P continuously extended to zero. For the fractional case, split the angular integral near zero and use z=t/u to obtain cΓ(−α)t^α; the remainder exponent 3+2α is strictly larger than 2+α. The constant-density subtraction gives c log(1/t)−cγ+I+o(1), and the triangular kernel gives the additive 3/2; finite inverse moment gives J/4. Independently checked positive log(2) in 2D, zero I in 3D and the exact 1D atom 1/(2+s). The notation p(0) denotes the grazing coefficient c selected by the weighted-integrability hypothesis, not an arbitrary assigned point value of an a.e. density. The result concerns per-swimmer force. Inspected checker.py without executing it; finite-cell solving and special-function quadrature are corroboration only.

## originality

PASS

The exact stationary reformulation, pressure functional, isotropic kernels and one-dimensional law are prior. The publishable difference against the inspected comparisons is the distribution-free small-width bound and first nonlinear force response, including a coefficient recovering the grazing-law constant; this is an explicit analysis of a known model, not a new model or exact force identity.

## value

PASS

In a natural mechanical observable the first nonlinear correction distinguishes integrable inverse speed, finite grazing coefficient and divergent grazing power. The bound both provides usable approximations without solving a singular stationary density and makes the logarithmic coefficient an explicit inverse signature. This is not a claim of statistical identifiability with noisy data or of a classification of all densities.

The dated certificate retains the supplied scientific assessment, sources and limitations.

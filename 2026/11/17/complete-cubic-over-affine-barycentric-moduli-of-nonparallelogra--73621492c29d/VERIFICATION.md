---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS: positivity plus affine precision on each trapezoid edge forces p3=xy(A+Bx+Cy), top and sloping interpolation yield C=(a−b)B and q=(A+(a−b)B)(a−(a−b)y)+bBx. Linear normalization forces p1,p2,p4. Factor positivity is equivalent to A≥0, A+(2a−b)B≥0 excluding zero; q has positive vertex values, thus positive on closed trapezoid. The cross-product identity proves projective injectivity, and gcd calculation rules out denominator cancellation. Independent symbolic reconstruction of all three normalization/precision identities and parameter uniqueness passed; rational-grid sampling alone cannot prove all real parameters.

## originality

PASS

PASS best-of-knowledge: Baumbach–Winter (arXiv:2611.02110v1) includes one concrete non-Wachspress cubic example and minimal numerator-degree rigidity. The published universal denominator theorem implies denominator degree one for noncentral trapezoids. Neither prior statement implies all admissible cubic numerator families, sharp two-ray cone, projective uniqueness or endpoint classification. Primary 2026 Baumbach–Winter full text could not be retrieved in this run, so priority risk is explicit.

## value

PASS

PASS: a complete low-degree positivity-moduli space for a natural non-parallelogram finite-element polygon, with two extremal families and a rigid Wachspress interior point, answers a motivated interpolation-geometry classification beyond a single previously known example. It is a closed exact structural fact, not a polynomial substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.

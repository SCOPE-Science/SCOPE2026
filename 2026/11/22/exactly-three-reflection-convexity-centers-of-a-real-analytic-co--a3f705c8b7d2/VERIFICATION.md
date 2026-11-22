---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The exact argument appears in `RESULT.md`. Its decisive steps are: the unique supporting-point formula for a positive-curvature support function; the necessity that common-support points coincide when a union is convex; anti-periodicity and the odd-multiplicity argument for the common-support equation; the cubic identity at each candidate center; and the radial convex-hull coverage proof. These establish the global classification independently of sampled computations.

Run `python3 check_reflection_convexity.py` with the Python standard library. The checker tests three distinct pairs of admissible \(R,\varepsilon\), all three candidate centers, 1,440 normal angles for each, three numerical support integrals and representative excluded centers. It checks the derived radius and confirms the perimeter and area to numerical quadrature tolerance. Successful output is `ANALYTIC_THREE_REFLECTION_CENTERS_CHECKS_OK`.

The script is a finite arithmetic sanity check. It cannot establish uniqueness or convexity for an uncountable family and is not treated as an infinite certificate. Historical priority and independent external validation remain unverified.

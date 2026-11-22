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

## Reproducible checks

Run `python3 check.py` with SymPy installed. The checker confirms the polynomial resultant expansion, the leading trace degree and total degree, all six line restrictions for the equation and its Jacobian, four triple-point incidences, twelve distinct pinch-coordinate representatives, and exact rational-parametrization samples.

## Proof checks and limits

The general all-parameter assertions are proved in `RESULT.md` using finite birational normalization, exhaustive inverse-coordinate comparisons, a direct rank analysis, explicit analytic pinch charts and tangent-plane normals. These arguments, rather than finitely many symbolic test points, establish the classification. The local analytic statements require characteristic zero. The calculation does not classify projective-boundary singularities.

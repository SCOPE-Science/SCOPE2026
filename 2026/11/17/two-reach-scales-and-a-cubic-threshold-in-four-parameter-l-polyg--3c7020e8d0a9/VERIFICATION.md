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

`verify.py` runs independent numerical quadrature of the exact upper-right quadrant intersection and compares it with both analytic first-contact formulas. It checks multiple strictly positive length tuples, the cubic coefficient on both sides of the equal-length boundary, rational core-radius arithmetic, and the diverging-ratio family. It uses only the Python 3 standard library. These checks do not replace or certify the infinite-domain proof. The standalone mathematical argument and parameter restrictions are in `RESULT.md`. No independent audit has been performed.

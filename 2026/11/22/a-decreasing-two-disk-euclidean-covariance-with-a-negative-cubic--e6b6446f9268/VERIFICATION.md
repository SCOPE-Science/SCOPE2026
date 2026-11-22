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

# Verification of the exact sign

Execute `python3 certificate.py` with Python 3 and its standard library; it computes only exact `fractions.Fraction` expressions. The Bessel-derived coefficient formula and factorial tail bound are derived in `RESULT.md`; the script checks the finite sums and the strict inequalities needed for degrees zero through three. No external files, numerical quadrature, runtime log or downloaded literature is required. Proof of Euclidean strict positivity and radial monotonicity is analytic and appears in the result. Independent mathematical review has not been performed.

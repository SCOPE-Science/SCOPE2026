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

# Reproducibility and scope

Run `python3 verify.py` with a standard Python 3 installation. The program requires no external packages, evaluates the rational map's inverse branches at 85-digit decimal precision, checks 500 inverse identities on five gains, validates the unique postcritical cubic-root threshold, and tests dimension-root brackets and their high-gain expansion. It additionally checks the quadratic discriminant identity using exact rational arithmetic.

These checks corroborate finite algebraic and numerical aspects only. The proof of infinitely many parameter values, the existence of the escape exponent, the symbolic conjugacy, and the Hausdorff dimension bounds is given in `RESULT.md` by analytic arguments. Numerical tests are not substituted for these arguments. The real interval is an absorbing observation interval, not a claim that every orbit of the globally defined rational expression remains in it. No independent audit has been performed.

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

# Reproduction and limits

Run `python3 verify.py` in the directory containing this file. This requires only the Python 3 standard library. It checks the 24 three-surplus rational base inequalities, six two-surplus tests, 15 exceptional integer compositions, and 4,790 independent finite separated-set examples by exact arithmetic. The infinite reduction, derivative monotonicity, induction on surplus factors, and sharpness sequence are supplied in `RESULT.md` and were separately reviewed. Exact finite tests do not themselves establish universal quantification.

The derivation of the distinct-prime consequence assumes the product-minimal starting set and the stated strict gap inequality. There is no independent mathematical audit or published peer validation of this result.

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

# Verification of the box-transit cadence theorem

The complete proof is in `RESULT.md`. Run `python CHECKER.py` in a directory containing the extracted files. Dependencies are Python, NumPy, SciPy, SymPy. The checker tests independently integrated convolution energy, numerical global optimization, strict comparative statics at sample points, several limiting regimes and symbolic derivatives. It reported `PASS 2283 independent integral, calculus, optimization, monotonicity and limit checks` on the packaged code.

The two derivative signs are globally proved by the decreasing polynomials displayed in `RESULT.md`; finite tests are not a substitute for these arguments. The model assumes an independent per-exposure Gaussian floor, phase averaging and known transit timing. Empirical performance and independent audit remain unverified.

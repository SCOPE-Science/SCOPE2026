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

# Verification

The exact integral and profile are defined in `RESULT.md` and implemented directly in `check.py`. Replay from the directory containing both files with `python3 check.py`, using Python 3, NumPy and SciPy. The observed output was `FIRST_HERMITE_ANNULUS_CHECKS_PASS 471`.

The checker independently quadratures the exact Poisson--Hermite intensity kernel, compares it with the truncated-normal second-moment profile for growing center radii, locates optimizing discrete Hermite indices, checks derivative identities and the uniquely defined critical number, and verifies elementary Gamma-moment normalization. This is a numerical consistency test, not a computer-assisted proof of all quantified limits. The analytic proof in `RESULT.md` establishes the infinite-range and uniqueness claims.

Proof limits: the result assumes fixed positive annular scale, a first-Hermite window and continuous exact observation. No independent audit has been performed.

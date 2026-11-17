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

# Reproducibility and verification

Run `python3 verify.py` with Python 3 and SymPy. The script verifies exact rational factorization of the difference update and the variance identity; three finite trajectory regimes and an exact critical reciprocal-log diagnostic are checked. Successful execution prints `VERIFY_OK`.

The infinity-time assertions use the proof in RESULT.md, including uniform Taylor remainders on the nonnegative cone, global monotonicity, and convergence of the compensated logarithmic products. Numerical convergence at finitely many horizons, however compelling, cannot prove their infinite-time limits or assess literature priority. No external or independent validation is claimed.

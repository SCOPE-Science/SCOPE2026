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

Run `python check.py` with Python 3 and SymPy. The independent rational resolvent substitutions, tridiagonal determinant continuants, derivative polynomial, exact sign brackets and transformed root-count polynomial are checked on the supplied example. Arbitrary smaller path lengths are ruled out by the spectral-factor monotonicity proof, not numerical sampling. The proof has been reviewed in this document set but not independently audited.

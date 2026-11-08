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

# Reproducibility

Run `python verify.py` with Python 3. The standard-library checker outputs `VERIFY_OK 310 finite and asymptotic checks`. It exhaustively enumerates tree edge sets for eight small complete-bipartite instances, verifies first two coefficient formulas in exact rational arithmetic over a parameter grid, and checks numerical convergence toward the two explicitly derived asymptotic constants.

The proof of the infinite-family bounds is the uniform logarithmic coefficient expansion and double-counting factorial-tail argument in RESULT.md; finite enumeration alone does not establish it. No independent audit has been performed.

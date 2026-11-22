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

Exact rational checks are implemented in `verify.py`. They reconstruct the five Lagrange cardinal polynomials, verify every all-index symbolic moment expression and verify a rigorous Taylor remainder enclosure at the root ordering and two isolation brackets. These computations support the sign comparisons; the global sign classification depends on the analytic coefficient-sign arguments in RESULT.md.

Run `python verify.py` with Python 3 and SymPy. Scientific limits: the method treats only the specified five equispaced nodes and an exponential density, and independent mathematical and historical-priority assessments have not been performed.

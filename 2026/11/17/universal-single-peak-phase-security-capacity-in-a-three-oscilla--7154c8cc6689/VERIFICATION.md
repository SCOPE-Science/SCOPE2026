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

# Reproducible checks

Run `python3 verify.py` with a standard Python 3 installation (only the standard library is required).

Observed output from the checker extracted from the package:

`VERIFY_OK exact_boundaries=5 monotone_branch_tests=5 phase_balance_cases=3005 stable_beyond_security=5`

The script tests five different nontrivial pairs of security caps, thirty coupling choices at each pair, 100 interior phases per chosen coupling, several monotonicity grids, and a principal equilibrium beyond the strict-security limit for each cap pair. Identity comparisons are made with stated numerical tolerances. The mathematical proof in `RESULT.md`, not this finite test, establishes the result for arbitrary admissible cap pairs and coupling strengths.

All proven claims concern equilibria and their local transverse stability; the checker does not establish global convergence, switching stability, or historical novelty. No independent audit was performed.

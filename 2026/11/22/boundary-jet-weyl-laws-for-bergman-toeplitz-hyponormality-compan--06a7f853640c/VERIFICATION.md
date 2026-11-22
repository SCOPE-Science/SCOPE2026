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

Execute `python check_jacobi_jet.py` with Python 3, SymPy, and NumPy. It verifies exact Taylor coefficients, the exact beta moment formula, 140 rational-power identities, 12 polynomial-moment identities and 12 finite-section matrix tests. The rational-power tests and exact symbolic algebra are finite tests only. The boundary-asymptotic counting argument appears in `RESULT.md` and provides the universal mathematical justification.

# Scope

Only the explicitly stated analytic-Bergman normalization and boundary regularity are covered. The power-symbol identity is a consequence of a separate exact formula; it was not inferred from numerical regressions. Independent mathematical validation has not been performed.

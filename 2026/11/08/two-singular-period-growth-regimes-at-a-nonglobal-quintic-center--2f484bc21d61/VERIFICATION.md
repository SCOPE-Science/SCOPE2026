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

# Verification scope

The accompanying `verify_period.py` checks (i) vanishing derivative of the explicitly stated first integral, (ii) the time-preserving fifth-order restoring-force coefficient, (iii) the exact kernel change of variables, and (iv) four direct convergent quadratures of the original-time period at selected amplitudes. Its output is `CHECK_OK 9 checks` when the provided Python 3, SymPy and SciPy dependencies are present. The checked floating values are illustrative only and are not used to certify an infinite theorem. The full parameter and asymptotic conclusions follow from the written energy and endpoint bounds. No external independent audit was performed.

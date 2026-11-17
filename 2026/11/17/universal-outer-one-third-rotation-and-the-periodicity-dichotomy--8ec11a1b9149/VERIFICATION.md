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

# Reproducible checks and limits

Execute `python verify.py` with Python 3.11 or later and SymPy installed. This checks the exact rational invariant by polynomial cancellation, the determinant-one logarithmic Jacobian, the order-three outer linear map, and the logarithmic Möbius derivative. The script estimates clockwise winding for the coefficient quadruples `(2,3,1,1)`, `(3,1,1,1)`, and `(1,1,1,1)` near the unique positive equilibrium and at a log displacement of 55. The expected terminal line is:

```
VERIFY_OK exact_H_identity=1 exact_log_symplectic=1 outer_hex_order=3 numerical_cases=3
```

The checks are corroborative, not independent certification. They do not establish all-level conjugacy, the existence of a limit at arbitrary energy, or the infinitely many prime-period statement: those follow from the convex-Hamiltonian and singular-scaling arguments in `RESULT.md`. The script uses no external data, no network access, and no material from other records.

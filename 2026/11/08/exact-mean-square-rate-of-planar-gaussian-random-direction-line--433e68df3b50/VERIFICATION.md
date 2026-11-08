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

`verify.py` (Python 3, standard library only) independently checks the rational moment matrix, its determinant, the exact angular-integral values by high-precision deterministic midpoint quadrature, and the propagated second-moment recurrence on several initial states and Hessian contrasts. The included `verify_output.txt` records 111 successful checks and two explicit rate examples. Reproduce with `python3 verify.py`.

The all-\(t\), all-\(n\), all-start conclusion rests on the integral identity, positive transfer and Perron–Frobenius proof in `RESULT.md`. The numerical quadratures and finite iterations do not independently certify a statement at arbitrary precision or infinite horizon. No external or independent mathematical audit has been performed.

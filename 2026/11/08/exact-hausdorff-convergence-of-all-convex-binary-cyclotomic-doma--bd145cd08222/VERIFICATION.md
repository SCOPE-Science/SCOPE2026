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

# Verification and limitations

Run `python3 verify.py` with Python 3 and SymPy installed. The executed exact-rational checks covered 5,625 points for odd divided-power forms; the algebraic cyclotomic homogenization tests covered 25 symbolic identities. Numerical scalar comparisons covered 500 odd parameters, but the proof of the inequality is the independent analytic concavity argument in RESULT.md. The run produced:

```text
VERIFY_OK exact_grid_points=5625 cyclotomic_identities=25 scalar_comparisons=500 rational_exact=yes
```

This checks finite consequences of the proof. It does not search all mathematical literature and does not provide independent scientific certification. The entire all-index identity follows from the stated proof. The verified statements concern Euclidean, not arbitrary-norm, Hausdorff distance.

---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact checks for sparsest primitive cube roots

Run `python3 verify.py` with Python 3.9 or later; no third-party packages are needed. The expected output is:

```
PASS: 9 feasible supports, 6 primitive supports, 114 labeled sweeps
```

The script finds support unions of two permutation matrices, checks primitivity by exact powers of the support matrices, and checks the cube identity and uniqueness on 19 interior rational weights, including the singular case \(p=1/2\). For each weight it checks all six labeled sweep orders against all support relabelings and weights in the grid. The determinant identity and the trivial permutation stabilizer in `RESULT.md` prove uniqueness on the continuum and are not replaced by finite testing.

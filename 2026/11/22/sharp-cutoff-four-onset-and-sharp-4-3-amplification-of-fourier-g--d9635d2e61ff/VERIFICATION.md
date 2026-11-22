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

The reproducibility script `VERIFY.py` requires only the Python standard library. Running `python VERIFY.py` produced:

```
VERIFY_OK 46262
PHASE_VERIFY_OK 46430
```

The script reconstructs the exact Fourier action and boundary leakage blocks, checks the trace and determinant identities with exact rational arithmetic, confirms the candidate stationary-point equations and cutoff distinction for \(2\le K\le44\), and checks phase invariance numerically. Its bounded enumeration does **not** prove assertions for untested cutoffs. The all-cutoff phase transition, optimization, and limiting ratio instead follow from the symbolic inequalities and asymptotics in `RESULT.md`. Numerical floating-point phase tests use relative tolerance \(10^{-9}\) and are supplementary. This record has no independent mathematical audit.

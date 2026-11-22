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

# Checks and reproducibility

Run `python verify.py` and `python verify_f4.py` from this package. The first script directly verifies the six basis multiplication identities for every proposed normal-form map over five prime fields, compares ranks with the theorem, and exhausts all matrices over \(\mathbb F_2\) and \(\mathbb F_3\). The second exhausts all \(4^9\) matrices over \(\mathbb F_4\) for each nonzero parameter, using explicit arithmetic modulo \(X^2+X+1\).

Observed outputs:

```
VERIFY_OK 23 prime-field parameters; exhaustive all 3x3 maps for p=2,3
F4_EXHAUSTIVE_OK 3 parameters x 262144 matrices
```

The finite checks do not constitute an exhaustive verification for arbitrary fields. The all-fields proof is the algebraic normal-form derivation in `RESULT.md`. No independent mathematical audit has occurred.

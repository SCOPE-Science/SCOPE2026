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

Use a Python 3 interpreter with only the standard library:

```sh
python3 check_toeplitz.py
```

The checker verifies exact rational all-index formulas at a large finite collection of indices, checks the positive polynomial certificate by integer arithmetic, compares matrix quadratic forms against direct operator actions, and exhibits finite negative angular-chain vectors beyond the sharp threshold. Its successful execution is supplementary; neither finite index coverage nor numerical tests certify infinitely many rows. The proof's infinite coverage comes from the displayed positive polynomial expansion, density of the basis, and the asymptotic finite-chain argument. No independent audit was performed.

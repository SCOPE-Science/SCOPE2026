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

Run `python3 verify.py` from the directory containing this document. The script uses only the Python 3 standard library and no downloads, internet, optimizer or hidden data. The observed result during package preparation was:

```
VERIFY_OK: rational algebra instances: 1313 parameter instances: 1111 one-dimensional comparisons: 334411
```

The verifier tests exact rational identities for the quadratic quotient coefficients, the spectral balance branch, the two factorizations against internal eigenspaces and the high-branch polynomial. It also constructs symmetric rational stochastic matrices, confirms their row sums and invariant eigenspaces, and compares the claimed optimizer with fine meshes of feasible orbit parameters. These are finite validation tests only. The complete proof for all integer sizes and continuous throttle values is in `RESULT.md`.

No external audit, exhaustive all-real computation or formal-machine proof is claimed.

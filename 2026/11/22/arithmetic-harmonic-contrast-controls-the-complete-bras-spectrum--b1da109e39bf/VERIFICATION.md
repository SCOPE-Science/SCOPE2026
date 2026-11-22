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

# Verification of the metric-star mass-preconditioning claim

The proof in `RESULT.md` gives exact global block matrices from the independent local mass assembly rule, provides two explicit eigenvectors at eigenvalue one, identifies the \((k-2)\)-dimensional invariant subspace at \(4/3\), and obtains the remaining eigenvalue from the trace. Equality-arm continuity, positive-definite diagonalizability, Jacobi's rank-two symmetric scaling, and the sharp attainable Kantorovich contrast inequality are all included.

Run `python3 check_star.py` with a Python 3 standard library. The checker assembles the consistent mass and BRAS inverse from each edge separately and compares complete characteristic polynomials using exact fractions, not floating-point approximate eigenvalues. It also checks Jacobi's characteristic polynomial and the contrast inequality. Expected output:

```
PASS: 53 exact-rational star instances, Jacobi and BRAS characteristic polynomials.
PASS: equal-arm and sharp fixed-contrast constructions.
```

The checker is a diagnostic for finite chosen configurations; the mathematical proof handles every positive real arm-length vector and arbitrarily large finite degree. The previous literature comparison does not certify historical priority, and independent mathematical validation has not occurred.

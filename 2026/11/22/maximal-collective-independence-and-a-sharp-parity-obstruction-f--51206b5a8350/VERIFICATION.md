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

# Verification of the claimed Kummer phase-profile law

The standalone `CHECK.py` uses only Python 3 standard-library `fractions.Fraction` and `math.gcd`. It constructs every rational discontinuity cell of the floor functions, integrates their constant values exactly on each cell, tests every joint \((C,F_j)\) probability against the theorem for \(d=2,4,\ldots,100\), and tests the conditional central-bit balance on each nonempty complete vector fiber of \((F_j)_{j\in J_d}\) at the same denominators.

Replayed command: `python3 CHECK.py`.

Observed output:

```
PASS: 10000 exact two-by-two joint-probability checks over 50 even denominators (2..100).
PASS: 6232 exact nonempty vector-profile conditional-independence checks.
All rational discontinuity cells checked, not a sample of points.
```

These are finite exact arithmetic tests; the Fourier and shift arguments in `RESULT.md` provide the infinite proof. This verification is not an external or independent audit.

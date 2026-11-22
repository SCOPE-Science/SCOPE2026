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

# Reproducible verification

Run `python verify_split3.py` with Python 3, standard library only. This file reports the finite computations actually completed; the proof for all sizes and positive shifts is in `RESULT.md`.

Observed output:

```
PASS 9808 rational score comparisons, 760 independent inverse/variance comparisons, 47 exact critical identities
```

The program independently constructs the full rational shifted graph Laplacian and inverts it by Gauss-Jordan elimination. It checks the distinct-vertex entries and the variance from actual same-color off-diagonal squared entries, not only the reduced objective. In a separate independent enumeration it searches all two-hub class profiles (separated or joined) at several rational weight parameters for sizes \(4\) through \(15\). The exact algebraic-threshold checks are performed using the rational squared-weight value \(1/\lfloor q^2/4\rfloor\) without floating approximations.

Boundary and scope: these are finite checks only; the universal statements, uniqueness, and treatment of arbitrary positive real \(\mu\) rely on the proof. No independent external audit was performed.

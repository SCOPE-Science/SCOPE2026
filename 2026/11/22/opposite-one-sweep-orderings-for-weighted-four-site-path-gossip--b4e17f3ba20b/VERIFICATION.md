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

Install Python 3 with `sympy` and `numpy` versions satisfying `requirements.txt`, then run:

```
python verify.py
```

The script directly constructs all six \(4\times4\) sweep matrices from the three variable-strength pairwise contacts. Exact polynomial algebra verifies the difference of both elementary Gram coefficients, equality of Gram determinants, the cubic polynomial comparison, and equality of transfer characteristic polynomials. The numerical portion additionally checks 100 specified strength triples and the strict opposition of the two norm objectives. The exact equal-averaging example is also checked algebraically. The continuum proof additionally uses a mathematical norm-contraction and cubic-root sign argument; the finite numerical trials are not offered as a replacement.

No independent mathematical audit, formal proof-assistant certification, or exhaustive survey of unpublished literature has been performed.

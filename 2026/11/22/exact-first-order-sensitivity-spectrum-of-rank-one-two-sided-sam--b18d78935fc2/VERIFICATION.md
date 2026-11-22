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

# Verification record

`python verify_bug.py` completed successfully using Python and NumPy in the package environment:

```
VERIFY_OK 1563 matrix spectral and Frechet derivative checks
```

The script independently computes the Jacobian in the canonical basis, compares its complete singular spectrum to the claimed multiplicities in dimensions \((2,2),(2,3),(3,2),(3,4),(4,3),(5,6)\), and checks nonlinear difference quotients for step scales \(10^{-4},10^{-5},10^{-6}\). The analytic differentiation and adjoint-product argument in RESULT.md, not these finite diagnostics, prove the statement for all finite dimensions and all permitted alignments. The randomized tests use a fixed seed and are not exhaustive. The result applies only to fixed old bases and infinitesimal perturbations of a nonzero rank-one target; no independent mathematical audit has been performed.

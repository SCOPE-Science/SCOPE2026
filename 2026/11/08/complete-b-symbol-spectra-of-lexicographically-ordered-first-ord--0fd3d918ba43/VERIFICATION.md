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

# Reproducible finite checks

Run `python verify.py` in this directory using Python 3. No third-party dependencies are required.

The verifier independently constructs each affine Boolean evaluation word in increasing binary order, computes cyclic zero-window counts directly from the bits without reusing the closed weight formula, and checks all \(b\)-symbol weights for all affine functions at \(2\le m\le9\). It separately extracts and compares actual cyclic zero-run multisets, checks the predicted multiplicity of every transition count, and compares each complete \(b\)-weight enumerator. It also checks 240 fixed-seed nonconstant affine words at \(m=10,11\).

Observed output:

```
VERIFY_OK configs=2280 individual_b_weights=1067680 full_distributions=1020
```

Finite computations do not establish the claims beyond the tested range. The mathematical proof establishing all allowed parameters is in `RESULT.md`. No independent audit has been performed.

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

# Reproducibility and limits

The analytic proof uses Fourier--Walsh inversion, strict log-convexity under permutation averaging, and the span-two lattice local central limit theorem. The test script enumerates finite sign cubes using exact fractions and checks both sides of the sharp moment ratio and the complete-character moment identity.

Command: `python3 checker.py`

Observed output:

```
PARITY_NTH_RELATIVE_EXACT_OK 293
SHARP_LAMBDA_4_6_8 ['3/5', '15/47', '315/1957']
```

Finite tests are not an infinite proof or independent certification. The sharp constant's finite examples and exponent asymptotic depend on the analytic derivation. Primary manuscript access restrictions leave a qualified originality risk.

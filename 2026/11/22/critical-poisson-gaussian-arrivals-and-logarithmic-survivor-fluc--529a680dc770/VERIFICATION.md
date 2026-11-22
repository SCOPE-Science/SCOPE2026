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

# Reproduction and verification

Execute `python verify_critical.py` using Python 3 and SciPy (the checker calls `scipy.integrate.quad` and `scipy.special.erfcx`). It computes the exact successful-arrival standardized density and CDF, compares normalizations and conditional moments, verifies the moment-generating transform, and tests the sharp total-variation prefactor numerically for multiple positive mortality parameters. It also compares finite-population first-arrival and no-success probabilities to their critical-window limits and checks the conditional living-population mean's logarithmic scaling.

On the provided checker run, the output was:

```
PASS: 239 deterministic consistency checks (not an infinite proof)
TV leading constant: 0.377503250032619
```

The reproducible finite checks are supplemental only. The infinite-limit total-variation rate follows from the density expansion with controlled tails and a two-sided coupling, and the joint survivor limit follows from exact conditional binomial sampling plus concentration. No empirical data, independent audit, or external certification is included.

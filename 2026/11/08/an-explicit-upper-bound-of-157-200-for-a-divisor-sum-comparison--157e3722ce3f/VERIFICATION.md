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

The standalone `verify_density.py` uses Python 3 standard-library arithmetic. The deterministic program recomputes all exponent classes for the primes through 503, verifies each upward ratio bin with exact integer powers, convolves the integer residue weights, and checks the strict prefix proportion greater than \(216/1000\). It also checks \(F(1400/503)<7\) with rational upper bounds and \(e^7>1000\) with a rational Taylor lower bound.

The use of floating-point logarithms only seeds searches for the integer bins; each candidate is corrected by **exact comparisons in both directions**, so no mathematical assertion relies on floating-point tolerances. Direct invocation of the extracted checker produced:

```
prefix_probability 0.2161377019267721
F_upper 6.980889321678812 count_good_digits 685 total_digits 686
bins 13969 offset -6248 primes 96
above_216_thousandths True
CERTIFICATE_PASS density_less_than_157_over_200
```

The decimal values above are diagnostics, not proof thresholds. The proof covers all positive integers through the unconditional uniform tail argument. The exact density is unknown; the comparison bound has not received independent validation.

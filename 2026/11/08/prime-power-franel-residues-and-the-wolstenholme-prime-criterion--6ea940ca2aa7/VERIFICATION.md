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

# Reproduction and bounds

The included `verify.py` uses only the Python 3 standard library. Running `python3 verify.py` produced:

```
VERIFY_OK prime_power_Franel_mod_p4=PASS Bernoulli_reduction=PASS primitive_binomial_units=PASS p2_p3_exact_valuations=PASS Wolstenholme_16843=PASS checks= 581
```

The program checks the modular cubic binomial sum directly at all tested small prime-power indices, compares the alternating reciprocal-cube coefficient against exact rational Bernoulli numbers, checks Lucas-reduced binomial units, verifies the exact valuations at prime powers of two and three, and checks the known exceptional prime \(16843\) through modular harmonic and central-binomial products.

The scientific proof covers **all** prime powers. Finite tests do not establish untested congruences. For Wolstenholme primes, the theorem establishes divisibility by \(p^4\) but does not determine valuation beyond this lower bound. No independent audit has been performed.

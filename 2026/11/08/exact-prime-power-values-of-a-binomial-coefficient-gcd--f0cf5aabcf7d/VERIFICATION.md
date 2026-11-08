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

# Reproducibility and evidence

The embedded script `verify_binomial_gcd.py` uses exact standard-library integer computations, direct binomial coefficients, Euclid's gcd algorithm, Kummer carries, and independent factorial/Legendre valuations. Execute `python verify_binomial_gcd.py` from the package directory.

Observed output:

```text
DIRECT_GCD_OK n=3..100 cases= 98
KUMMER_MINIMUM_OK n=3..700 components= 1449 valuation_pairs= 528238
EXPLICIT_WITNESS_OK n=3..5000 positive_components= 4084
SAMPLES n=12: 2 n=24: 4 n=36: 3 n=72: 3 n=100: 25
VERIFY_OK exact_integer=yes independent_carry_and_factorial_methods=yes
```

The direct gcd test compares the conjectured product to the gcd of *all* binomial coefficients for each indicated finite \(n\). The carry test examines every admissible \(q\) for each prime divisor of each \(n\) in the specified interval; the explicit-index test checks the constructive upper witness on a larger range. The unrestricted mathematical proof is in `RESULT.md`; no finite computation can establish an infinite universal statement. The published source lemmas are mathematical dependencies. No independent audit has been performed.

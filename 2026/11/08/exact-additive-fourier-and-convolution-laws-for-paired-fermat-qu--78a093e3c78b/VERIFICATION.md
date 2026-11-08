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
# Reproducibility and verification limits

Run `python3 verify.py` with Python 3 (standard library only) to reproduce the finite check. Its observed output is:

```text
VERIFY_OK prime_cases=33 image_entries=2815 m=1,2,3 exact_convolutions=PASS all_nonzero_frequency_classes=PASS complex_Fourier_small_primes=PASS two_sum_full_support_and_sharp_min=PASS
```

The test directly constructs Fermat quotient vectors with modular exponentiation for primes \(p\in\{3,5,7,11,13,17,19\}\) and five candidate shift pairs (33 actually distinct modulo \(p\)), compares them against independently constructed affine lines, exhaustively enumerates \(m=1,2,3\) convolutions for every target, tests exact energies, and checks the Fourier zero locus and complex phases for small primes. The full theorem for all odd primes and all \(m\ge1\) is proved mathematically in `RESULT.md`, not by these finite tests.

No independent mathematical validation has been performed. Literature completeness and historical priority have not been independently established.

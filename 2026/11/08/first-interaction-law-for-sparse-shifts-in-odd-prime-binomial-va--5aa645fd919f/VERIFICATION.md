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

# Reproducibility

The standalone `verify.py` was run using Python 3 with exact `fractions.Fraction` arithmetic. It enumerates base-\(p\) carry-state transitions for primes \(3,5,7\), tests 81 different multi-digit position/amplitude configurations, and verifies 243 rational coefficients. For each configuration it checks exact agreement up to degree \(g-1\) and the exact strictly negative degree-\(g\) discrepancy. Independently, eight small complete residue-period censuses compute actual integers \(\binom{n+t}{t}\) and their prime valuations directly, matching the finite-state values.

Verified command: `python verify.py`.

```
VERIFY_OK multidigit_cases=81 exact_rational_coefficients=243 complete_modulus_binomial_censuses=8 strict_first_defects=yes
```

The finite calculations are not infinite completeness proofs. The mathematical proof is the digit-cylinder and first-interaction argument in `RESULT.md`. The 2001 Barat--Grabner full text was inaccessible, and the historical-priority assessment is not independently certified.

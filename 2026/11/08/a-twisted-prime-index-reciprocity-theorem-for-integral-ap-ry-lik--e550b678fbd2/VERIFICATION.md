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

Run `python3 verify_reciprocity.py` with Python 3; only the standard library is required. The executable checks exact integer recurrences and four separate explicit binomial sums through index 11, then checks reflected coefficients and equivalent reciprocal coefficients for eleven families at odd primes through 59, omitting primes dividing the coefficient \(c\). It additionally tests the known counterexample to a nonzero-\(d\) extension for primes 5, 7, 11 and 13.

Observed execution:

```text
VERIFY_OK families=11 primes=16 coefficient_checks=4803 independent_binomial_n=12 excluded_d_case_primes=4
```

These are finite checks, not a proof for infinitely many primes. The general proof is the algebraic recurrence-reversal argument in RESULT.md. No independent audit has been performed, and no assertion is made about cases excluded by the hypotheses.

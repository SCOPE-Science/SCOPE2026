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

The `check.py` file is a standalone Python 3 standard-library script. Run `python3 check.py` with the extracted file. It uses exact `math.comb` integer computations and independent digit-based predictions.

Successful checks performed with the package source prior to embedding:

```text
PASS complete proportional rows (mod 8): 180
PASS prime-index exact gcd cases: 50
PASS odd and unrestricted cutoff counts: 15 cutoffs through 1000000
PASS four-level explicit classification: 100000 multipliers
```

The direct binomial and prime-index tests are finite; the exceptional counting checks use enumeration at selected finite cutoffs. The infinite proof rests on Legendre's digit-sum valuation, Kummer's carry criterion, disjoint binary-form classifications, dyadic decomposition, and Lucas's theorem. In particular, finite tests do not certify an infinite claim.

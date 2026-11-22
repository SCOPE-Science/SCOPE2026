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

# Verification of adjacent tetrahedral local-square counts

The standard-library Python checker `verify.py` computes elliptic character traces directly, directly compares the complete count of indices with both adjacent tetrahedral values quadratic residues against the theorem, and verifies the marginal single-value count. It covers 24 primes through 101 with 65 complete prime-power histograms, nine small-prime regular-class checks, and exact rational covariance formulas. To replay: run `python3 verify.py` in this package.

Observed output:

```
PASS: 24 prime-field checks and 65 full prime-power histogram tests.
PASS: exact marginal/joint formulas and the two covariance-sign laws.
Small prime regular counts: [(5, 1), (7, 1), (11, 1), (13, 5), (17, 3), (19, 3), (23, 5), (29, 11), (31, 7)]
Example densities: [(5, '9/20', '7/30'), (7, '5/16', '17/112'), (11, '3/8', '9/88'), (13, '227/364', '71/182')]
```

The tests establish consistency at the enumerated levels, not the infinite assertions. The proof supplies the unbounded result using character expansions, Hensel lifting, valuation shells, and Hasse's bound. Neither p=2 nor p=3 is treated, and no global integer-square conclusion is asserted. No independent mathematical audit has been carried out.

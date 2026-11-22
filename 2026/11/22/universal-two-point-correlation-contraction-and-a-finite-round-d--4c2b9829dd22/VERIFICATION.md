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

# Verification and reproducibility

The proof relies on identities for the open-boundary zero-field Ising chain, all stated in RESULT.md. The exact conditional mean is linear in at most two revealed boundary spins with nonnegative coefficients, and the two-point conditional covariance in any gap is nonnegative. A two-spin bridge calculation yields a strictly positive pointwise conditional covariance when neighboring sites are co-revealed; the same regression coefficients under the target and output ensure all-pair correlation comparison by induction. Conditioning on independent per-site round labels yields the collision factor \(\sum_k a_k^2\ge1/K\), and the target's exact energy representation translates the defect discrepancy into cross-entropy excess.

Run `python3 check.py` using Python 3 and only its standard library. The executable evaluates the entire finite-state output distribution by exact rational recursion. On execution the output was:

```
PASS: 3812 pair inequalities; 571 adjacent co-reveal bounds;
PASS: 12 all-singleton partitions; independent-schedule mixture;
PASS: exact fraction mass, zero means, both interaction signs;
example collision probability = 7/18; conditional constant = 60/361
```

The finite enumeration checks the algebra on small instances, including negative interactions and nonuniform reveal probabilities; it does not establish the infinite family of inequalities without the mathematical proof. The theorem concerns exact one-site conditionals and exogenous batching; no assertion is made about approximate denoisers, adaptive selection, optimal constants or independent expert validation.

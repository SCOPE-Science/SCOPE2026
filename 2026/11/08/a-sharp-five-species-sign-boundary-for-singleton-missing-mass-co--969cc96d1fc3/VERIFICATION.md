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

# Reproducibility instructions

Run `python checker.py` with an ordinary recent Python 3 installation; only `fractions`, `itertools` and `math` from the standard library are required. A successful run prints a line beginning with `PASS 984`.

The checker independently constructs two degree-five polynomial expressions and compares their integer coefficient dictionaries, so the all-profile four-species certificate is not tested only on random numerical examples. It calculates covariance directly by exact enumeration of every ordered sample outcome for rational profiles with two through five species and sample sizes two through five, compares against the analytic multinomial formula, and tests all positive rational profiles of certain small bounded denominators in two through four species. It also calculates the exact five-species example and compares a two-level exact moment formula with its analytical rare-species limit at nine sample sizes.

These checks do not certify all real abundance vectors or all sample sizes: those infinite statements are established in the written proof via the polynomial identity, sign analysis, continuity, and bounded moment convergence. No external independent audit or empirical validation has been performed. The result does not establish the minimal number of species for a positive covariance at sample size greater than two.

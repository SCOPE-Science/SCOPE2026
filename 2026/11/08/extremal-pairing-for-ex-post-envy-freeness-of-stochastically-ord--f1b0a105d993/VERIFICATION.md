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

# Verification

The analytic stochastic-difference proof establishes all stated inequalities for arbitrary nonnegative, independent, atomless item laws satisfying first-order stochastic dominance. The finite checker cannot by itself prove the infinite-domain claim.

Run `python3 verify.py` in the directory containing this file. It uses only the Python standard library. The actual check passed on 2026-11-01 UTC: 1,764 exhaustive four-law chains on the three-point rational grid, each with empty and Bernoulli(1/2) symmetric background (3,528 checks); exact exponential computations and means-only counterexample also passed. Finite distributions are interpreted with independent tiny continuous jitter, producing half-tie probabilities for comparisons of the unjittered integer totals.

The formula for the exponential example follows from the Laplace transform of a sum of two independent exponentials; it was separately evaluated using exact rational arithmetic. Independent audit and independent replication beyond the included checks have not been performed.

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

# Exact verification

Run `python3 verify_mex.py`. This code independently enumerates all regular overpartitions at weights through 15 for seven regularity parameters, checks their ordinary counts and first two mex moments against the coefficient formulas, checks two moment-coefficient monotonicities through weight 500, and performs nonproof convergence spot comparisons. The expected final line is `MEX_REGULAR_OVERPARTITIONS_FINITE_OK 126 exact brute and asymptotic spot checks`.

# Infinite argument

The finite enumeration is not an infinite certificate. The mathematical proof rests separately on the removal bijection, the exact Euler product, a coefficient Tauberian theorem for nondecreasing sequences, and a Gaussian Stieltjes limit for every positive real moment exponent. These steps and their uniform-on-compacts/tail bounds are written in `RESULT.md`. The source's two special mean constants can be recovered algebraically from the all-index expression.

# Boundaries

No independent mathematical audit, convergence-rate certification, growing-parameter uniformity, or local lattice limit is supplied.

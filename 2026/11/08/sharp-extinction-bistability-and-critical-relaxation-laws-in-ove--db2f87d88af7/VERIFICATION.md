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

# Verification of the mathematical claim

The accompanying `verify.py` is standalone Python 3 standard-library code. Execute `python verify.py` in a directory containing that file. In the recorded check it returned `PASS 166 check groups (with numerical sign scan samples); exact rational series and motif counts passed`.

Exact combinatorial checks use direct enumeration of triangle memberships and pair-of-triangle overlaps, independently checking the co-degree identity for complete, cyclic, and projective-plane triple systems. Taylor checks use rational formal power series for the actual exponential update at critical intensity; they confirm the quadratic, cubic, and quartic leading coefficients at four rational recovery rates. Numerical checks sample the number of positive roots relative to the exact saddle-node and the three leading power laws.

The analytic proof in `RESULT.md` supplies the global theorem, based on positivity of the logarithmic series and monotone/convex level-set classification. Finite sign scans neither prove an absence of other roots nor certify infinite-time limits, and approximate convergence is not an infinite proof. No independent scientific audit has been performed. The claim addresses only a deterministic homogeneous exponential mean-hazard approximation, not finite-state random epidemic trajectories.

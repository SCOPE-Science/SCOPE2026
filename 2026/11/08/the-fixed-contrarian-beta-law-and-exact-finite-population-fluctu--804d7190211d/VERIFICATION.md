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

# Verification of the stationary beta-bridge theorem

`python3 checker.py` uses only the Python standard library. It enumerates \(24\) finite chains at \(1\le m\le6\), \(1\le r\le4\), constructs exact transition matrices and solves the rational linear stationary systems from the ground up. It checks every stationary probability, the zero mass-balance residual, two centered means, all three covariance formulas, and the exact stationary generator identities. The observed aggregate state count across these chains is \(378\).

The countably infinite assertions are mathematical deductions: normalized contrarian generators converge uniformly to finite irreducible/absorbing birth-death kernels, each with a unique binomial invariant law; normalized congregator generators have uniform second-order Taylor expansions; the limiting moment recurrence uniquely identifies the beta measure on \([0,1]\). Finite checks are not used as proofs of convergence, of uniformity in the contrarian population size, or of originality.

The source model requires one fixed positive number of contrarians, a well-mixed population, and the copy/oppose rule specified in the result. The finite-state invariant law is unique because its transition graph is irreducible. No claim is made concerning independent audit or the complete finite-state mass function.

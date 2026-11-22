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

The mathematical proof of the global optimum is in RESULT.md. It reduces the exact expected terminal objective to a positive-semidefinite matrix of rank-one residual projections. A high-temperature expansion of a two-state path partition function shows strictly nonnegative even imbalance coefficients for every horizon, with a strictly positive quadratic coefficient once the horizon is at least two. A separate exact eigenvalue argument handles one step. Balancing the remaining independent coordinates proves a unique all-simplex optimum; no statistical extrapolation is used.

Run `python verify.py` with NumPy available in the same directory as this file. The checker's executed result was `VERIFY_OK 864 finite checks`; it compares explicit sample-string enumeration against the transfer representation, directly tests block least-squares projection identities, verifies the claimed optimizer in several dimensions/horizons, and checks many feasible competitor laws. These sampled checks do not establish global optimality for arbitrary parameters or originality; the analytical proof supplies global scope.

Limitations: calculations assume exact real arithmetic, independent identically distributed block labels, an invertible one-correlated-pair matrix, and exact block solves. No external independent mathematical validation has been performed.

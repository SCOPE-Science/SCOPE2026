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

`python3 verify.py` passed using Python 3 with no third-party dependencies. The independent RK4 solver was compared against closed two-eigenvalue matrix propagation at 270 parameter/time combinations, including unequal reset/memory rates. Parameter-grid calculations tested strict positivity and the rate ceiling; matched-rate derivative checks spanned overdamped, critical, and oscillatory gaps. The polynomial-exponential exceptional-point identity was checked directly.

The proof of the sharp global inequality, absence of finite-time zeros and CP-divisibility is analytic in RESULT.md. Finite grids cannot prove the all-parameter theorem. The exact clock convention includes the initial-time atom from ages exceeding the elapsed observation time; replacing it with a renormalized truncated exponential memory would be a distinct experiment. No independent external scientific audit was performed.

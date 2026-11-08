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

# Verification evidence and limits

Run the included stand-alone `verify.py` with Python and locally available `sympy`, `numpy` and `scipy` packages. It carries out 17 exact symbolic generator/boundary/covariance/factor checks; 96 independent components of the two-state backward boundary-value problem over asymmetric intervals; and 48 numerical checks on both sides of the sign-crossing threshold. All 161 tests passed.

The universal conditional independence is proved by the stopped harmonic-product identity in `RESULT.md`, not by numerical experiments. The boundary-value tests independently construct the product payoff upon first interval exit and do not assume the analytic interior solution. The recurrence, bounded optional stopping, initial-mixing covariance and exact one-root sign argument are all explicit in the proof. Independence from time-resolved observations or other switching models remains unproved.

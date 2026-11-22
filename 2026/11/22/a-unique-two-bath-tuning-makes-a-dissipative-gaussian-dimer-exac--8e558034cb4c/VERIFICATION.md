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

# Verification scope

The companion `verify.py` reconstructs the stationary Lyapunov covariance independently from the published formula and checks the fast-mode cancellation, thermal current, entropy production, OU trajectory covariance, fixed-law family, impulse response and off-tuning Markov obstruction. It uses 360 deterministic parameter configurations plus exact symbolic identities, and reports 3,267 successful assertions. Run in a Python 3 environment with `sympy`, `numpy` and `scipy` installed using `python verify.py`.

The analytic proof is in `RESULT.md` and applies to every \(a>k>0\), \(T_1,T_2>0\) and all stationary observation times. Tests are not an exhaustive proof. No independent scientific audit or physical experiment is represented. Publication priority remains subject to literature beyond the sources inspected.

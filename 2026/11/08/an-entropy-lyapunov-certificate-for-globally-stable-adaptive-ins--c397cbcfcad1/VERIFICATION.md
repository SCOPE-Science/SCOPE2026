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

# Verification and limits

`verify.py` is executable with Python 3; SciPy is optional for numerical integrations. Its exact-rational tests use the model's polynomial right-hand sides and both partial derivatives of the entropy certificate to recompute the dissipation identity in 2,400 test cases across \(N=2,\ldots,17\). A rational benchmark uses \(x_*=2/3\) and \(a_*=162/121\). In a SciPy-enabled environment, 20 trajectories from four distinct interior initial states are integrated across five feedback timescales using logistic variables to avoid artificial boundary sticking from floating-point saturation. The all-parameter theorem is established by the analytic identity, compact entropy sublevels, and LaSalle's invariance argument, not by the numerical experiments.

Run `python verify.py` to reproduce. The code does not certify uniqueness of prior literature, any stochastic limit, or independent mathematical validation.

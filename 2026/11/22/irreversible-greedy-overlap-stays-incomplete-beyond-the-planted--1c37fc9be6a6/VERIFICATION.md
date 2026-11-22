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

The scientific proof uses the exact finite-state generator, a finite-horizon martingale law of large numbers and a uniform-in-size bound on the number of remaining edge acceptances. Those steps, including the terminal-time limit, are mathematical arguments rather than numerical extrapolations.

Run `python verification.py` with Python 3 and SciPy to check 24 exact-rational comparisons between an aggregated-state recurrence and a separately coded labelled-subset recurrence, followed by deterministic ODE integration and finite-size expectation comparisons. The numerical ODE is solved to finite time, so its printed decimals are approximations and not interval-certified constants. The analytical inequality \(1-f(c)\ge1/[2(1+c)]\) does not rely on them.

The contrast with optimal matching invokes the published minimum-total-weight theorem of Moharrami, Moore and Xu (arXiv:1912.08880, Theorem 1), which treats the same independent exponential weight laws but a different matching selection rule. Independent external scientific validation has not been performed.

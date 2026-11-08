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

# Verification of the analytical statement

The analytical proof is given in `RESULT.md`: a regenerative Brownian Laplace transform gives the exact reset-count distribution and fixed-target moments; a uniform exponentially decaying bound justifies integrating the distant-target exponential limit; a stopped compensated-Poisson martingale gives conditional count/time locking; and a second dominated-convergence argument identifies the joint Gamma/exponential limit.

Run `python verify.py` with Python 3 and the Python package `mpmath` available. The supplied checker uses 153 finite assertions covering beta-integral count probabilities, transformed annealed Laplace integrals, moment derivatives, negative-argument transform bounds, remote-target scaling and the \(a=2\) exact count identities. The check passed in the packaged source environment. These computations are diagnostic and do not certify every parameter or any infinite limit.

The stochastic model requires \(D,r,\beta>0\), a single fixed target drawn from an exponential law, resetting to the starting point with independent exponential clocks, and stopping at first absorption. The asserted asymptotic limits hold at fixed physical parameters. Scientific priority is assessed against accessible same-model and related primary literature but is not an independent publication-priority guarantee.

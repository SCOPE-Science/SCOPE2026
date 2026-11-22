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

# Verification details

The complete result is proved by finite-dimensional independent Poisson thinning, explicit survival probabilities, conditional Gaussian scale mixing, and monotone likelihood-ratio comparison. The standalone `checker.py` performs finite-horizon and stationary probability integrations, independent event-clock simulations, and numerical boundary checks. Run `python checker.py` with Python 3, NumPy, and SciPy. At finite time the reset ages are right-censored at the common observation horizon; at stationarity they are uncensored.

For \(N=6\), \(D=0.8\), \(\lambda=1.3\), \(d=2\), and positive thresholds \(1.1,1.7\), the finite-time probabilities at \(t=1\) are \(0.148099844661\), \(0.168658025490\), \(0.207057232835\) for \(m=1,3,6\). Stationary values are \(0.172755334449\), \(0.199097143262\), \(0.250853042864\). Event-clock Monte Carlo with \(200000\) trials per setting agreed within five binomial standard deviations. Numerical tests cannot establish infinite-domain claims; the proof establishes the inequalities and conditionals for the full quantified domain. The stationary energy-covariance expression matches the independently derived established pair-correlator after parameter conversion. No independent scientific audit has been performed.

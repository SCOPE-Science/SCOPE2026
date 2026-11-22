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

# Reproducibility

Run `python verification/check_front.py` with Python 3 and its standard library. This checks stationary normalization for independent Beta holding laws, exact beta-function evaluation of the no-turn convolution, its fractional exponent, and an independent exponential-holding reduction. It also simulates a stationary left-wall residual holding time, genuine bulk Poisson flips and new holds at every hit. The program prints the conditional simulation results and the exact direct-path lower contribution.

Recorded execution: `eps=0.1` gives conditional simulation `0.1294727` versus direct-path lower contribution `0.1283781` (estimated sampling SE `0.0007158`); `eps=0.2` gives `0.21355` versus `0.2087777` (SE `0.0008737`). All assertions passed. The mathematical proof does not rely on simulation. The main limits use stationary renewal-reward, exact conditioning on the equilibrium residual, a finite-speed exclusion bound before \(L/v\), and an \(O(\varepsilon^2)\) bound on paths with extra reversals or additional wall visits. These are established in `RESULT.md` and hold for arbitrary independent positive finite-mean holds. The simulations concern only two illustrative non-Markovian laws and cannot verify the universal quantifier. No independent external audit or publication-priority certification has been performed.

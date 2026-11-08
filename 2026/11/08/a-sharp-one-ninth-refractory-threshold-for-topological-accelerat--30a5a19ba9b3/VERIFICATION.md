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

# Reproduction and scientific limits

The exact mean and threshold can be reconstructed from the killed Brownian Green function, the safe-reset probability \(1-\cosh z/\cosh 2z\), the active-attempt mean \((1-\operatorname{sech}(2z))/r\), and renewal \(m=\mathbb EA+p_s(\delta+m)\).

Run `python verify.py` with `numpy` and `scipy` installed (see `requirements.txt`). At verification, this printed `VERIFY_OK` after checking 40 independently discretized backward-generator cases, the first 79 positive-series coefficient indices, the critical threshold direction and the small-rate expansion. The continuum proof of the global inequality is analytic and cannot be replaced by these finite tests.

A grid point exactly at \(|x|=L/2\) is treated with half weight solely as a quadrature convention; the continuous stochastic model assigns this event zero probability. The finite-difference tolerance applies to dimensionless units \(L=D=1\).

The result does not prove uniqueness of the optimal positive reset rate, a full completion-time distribution, or an energetic cost law. Independent scientific audit has not been performed.

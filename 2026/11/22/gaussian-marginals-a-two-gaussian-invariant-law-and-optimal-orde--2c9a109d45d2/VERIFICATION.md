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

# Reproduction and limits

Install the dependencies listed in `requirements.txt` and execute `python verify.py`. Exact symbolic assertions test the two marginal-variance equations, both Hessian-contraction matrices, determinants of each Gaussian covariance, the exact objective and its derivative, and the mixed fourth-cumulant identity. The program additionally simulates an independent sequence of full two-update epochs at coupling \(c=3/5\), noise variances \(u=4\), \(v=1\), and order probability \(p=2/5\), with \(5000\) burn-in epochs and \(210000\) retained epochs. The simulation compares the two variances, covariance, objective, and mixed cumulant with the analytic values using stated tolerances.

The finite simulation is a reproducibility and consistency check only; it is not a proof of stationarity, uniqueness, Gaussianity or exact optimality. Those conclusions follow from the algebraic proof in `RESULT.md`. No independent audit or external mathematical validation has been conducted.

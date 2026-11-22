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

# Reproducibility and limits

The mathematical argument in `RESULT.md` supplies the proof: the key exact computations are the \(r>2\) Poisson quadratic variation, the \(r=2\) Lomax truncated second moment, and the \(1<r<2\) transformed Lévy intensity. Its small-jump domination and Lindeberg estimates establish the process limits for every admissible parameter and each fixed finite time interval. This is a high-intensity limit of a mathematically defined Poisson family; not a uniform-in-intensity theorem about original finite-horizon orbit-count data.

Run `python check_fluctuations.py` with Python 3 and SciPy. The checker verifies 271 finite numerical identities (mean/variance, exact critical truncated moment, and the Lévy-kernel Jacobian). These checks are diagnostic support and not a substitute for convergence arguments. No independent audit has been conducted.

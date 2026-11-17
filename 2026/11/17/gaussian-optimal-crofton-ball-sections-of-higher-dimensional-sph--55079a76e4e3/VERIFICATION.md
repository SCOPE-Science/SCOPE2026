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

# Numerical and analytic verification

The main proof supplies the topological meridian argument, exact Crofton offset measure, strictly concave optimization, and the Gaussian compactness argument. The code offers **finite numerical corroboration only**. Execute `python3 check_tube.py` with Python 3, NumPy and SciPy. It checks the normalization \(\mu_3=\pi/4\) and \(\mu_4=8/(3\pi)\), strict derivative sign changes at nine dimension-specific optimizers, probability normalization, consistency with the known three-dimensional circular-meridian law, four independently simulated importance-weighted uniform-hyperplane distributions, and convergence toward both high-dimensional constants. On execution, 106 deterministic assertions passed.

The reproducible output includes \(R_3=1.118904787310\ldots\), \(R_4=1.078309203655\ldots\), \(R_{200}=1.001143708345\ldots\), with respective ball-cut probabilities \(0.897206177085\ldots\), \(0.929987889303\ldots\), and \(0.998922934916\ldots\). The normal-quantile limits are \(0.22746821155978636\ldots\) and \(0.2143370411278703\ldots\).

The checker does not verify every uncountably many hyperplanes, all dimensions, or that a result is historically new. Those aspects are covered by the proof or separately qualified as historical-priority risks, not inferred from finite computations.

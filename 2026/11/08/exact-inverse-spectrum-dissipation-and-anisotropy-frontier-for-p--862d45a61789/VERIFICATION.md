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

# Reproducibility and verification

Execute `python verify.py` using Python 3 with NumPy and SciPy. The deterministic checker recomputes drift eigenvalues, the unique stationary covariance from the Lyapunov equation, diffusion eigenvalues and condition numbers, current-based entropy production, the sharp anisotropy envelope, the forced noise trace and the lag-asymmetry norm. It passed **328 independent deterministic matrix assertions**. These checks span four distinct positive parameter pairs and multiple normal/nonnormal strengths and circulation orientations; they are corroborative finite computations and cannot replace the universal analytic proof in `RESULT.md`.

The mathematical proof independently establishes all quantifiers, including the exact positive-definiteness interval, monotonicity, sharp attainment under every finite feasible condition-number cap, and exclusion of the singular limiting covariance from the model. A complete primary reading was performed for the motivating 2026 arXiv HTML and the relevant portions of the general 2018 arXiv PDF. The 2026 decomposition source was only partially available; no undocumented full-text comparison or independent external validation is claimed.

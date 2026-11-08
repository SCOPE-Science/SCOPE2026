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

# Reproduction and analytical verification

The accompanying `check_onset.py` requires Python, NumPy and SciPy. Run `python check_onset.py` from the directory containing this file and `check_onset.py`. The checker uses the independent direct-sphere center sampler rather than the analytically derived conditional gap law for its Monte Carlo component.

The verified analytic steps are the uniform Euclidean-ball transverse marginal, the localized adjacent-gap equivalence, the exact simplex volume, the gamma-function radial integral, and the \(L^1\)/total-variation normalization. For fixed positive \(\varepsilon\), the conditional Dirichlet statement follows from a uniform simplex density, not a simulation.

Numerical checks performed using `check_onset.py`:

- \(m=2,n=3\): computed gamma coefficient approximately \(3.656210113434\), exact-integral-to-leading ratio at \(\varepsilon=0.02\) approximately \(0.983007\).
- \(m=2,n=4\): coefficient approximately \(4.074366543153=64/(5\pi)\), ratio at \(\varepsilon=0.02\) approximately \(0.9998764\).
- \(m=3,n=3\): coefficient approximately \(17.05796216889\), ratio at \(\varepsilon=0.02\) approximately \(0.965585\).
- Three million independently sampled \(S^2\) four-center configurations at \(\varepsilon=0.1\) gave 117 complete-circle-covering events, proportion \(0.000039\); independent simplex-integral quasi-Monte Carlo yielded approximately \(0.000040623666\). The empirical standard error is approximately \(0.000003606\).

Expected success marker: `GREAT_CIRCLE_RANDOM_CAP_ONSET_CHECKS_OK`.

The numerical verification is finite and approximate, and hence not a substitute for the exact analytic proof, historical-priority confirmation, or independent validation. The current claim does not concern coverage of the entire ambient sphere.

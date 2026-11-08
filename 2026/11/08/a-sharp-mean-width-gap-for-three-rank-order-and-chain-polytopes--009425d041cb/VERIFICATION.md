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

# Reproducibility and checks

Run `python3 check_mean_width.py` in an environment with NumPy installed. The checker is standalone and recreates the tests with a deterministic seed. It has no external data dependencies.

A successful local run produced:

```
THREE_RANK_ORDER_CHAIN_MEAN_WIDTH_CHECKS_PASSED
theoretical_gaussian_sqrt_m_gap 0.0939817613
theoretical_spherical_mean_width_gap 0.1085207903
sample_finite_gaussian_sqrt_m_gap 0.0931776486
sample_finite_spherical_gap 0.1076296459
```

The tests enumerate all binary vertices for three small rank sizes, compare their direct Gaussian support maxima with the proposed finite exact formulas, test the Gaussian limit constants with independent Gaussian draws, and compare a larger finite-size sample with the predicted limit. The exact symbolic calculations in the paper reduce the Gaussian increment variances to \(1-1/\pi\) and \(2-1/\pi\), so Monte Carlo is not the logical basis for the positive limiting constant.

The mathematical proof depends on (i) the standard vertex descriptions of order/chain polytopes, (ii) joint Gaussian central limit convergence plus uniform integrability, (iii) the three-Gaussian-maxima perimeter identity, and (iv) independence of radial and angular Gaussian components. Only the stated asymptotic domain and metric are covered. No independent audit has been performed.

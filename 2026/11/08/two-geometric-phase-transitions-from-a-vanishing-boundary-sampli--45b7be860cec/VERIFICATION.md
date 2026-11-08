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

The bundled standalone `CHECK.py` was executed in the package preparation directory using Python and NumPy. It checked 5 exact inscribed-regular-polygon area/sagitta formulas, 4 local quadratic/cubic expansions, 300 independent two-sided Poisson gap samples, 300 circle polygons of 12,000 boundary samples with density exponent \(\alpha=1\), and 150 polygons of 25,000 points in the \(\alpha=1/4\) phase.

Observed output:

```
SINGULAR_SAMPLING_OK circle_shapes=5 local_expansions=4 poisson_pairs=300 bulk_trials=150
poisson_medians 7.090122744263705 55.999554704002236 finite_medians 7.011346411014641 55.69881117046267
bulk_mean 157.24908918514865 bulk_prediction 158.75213660313506 critical_coefficient 36.74817976924424
```

The checker was extracted and rerun from the delivered ledger to ensure embedded reproducibility. Exact deterministic checks are exact arithmetic to machine precision; the Poisson and polygon comparisons have Monte Carlo error. Simulations do not prove convergence or priority. The \(\alpha=1/2\) coefficient is analytically checked, but its slow logarithmic convergence is not used as numerical evidence.

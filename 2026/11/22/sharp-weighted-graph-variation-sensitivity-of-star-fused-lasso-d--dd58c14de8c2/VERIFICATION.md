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

# Reproducible verification

Run `python3 verify_star_tv.py` with a standard Python 3 installation. No third-party package, download, or external data is required.

The checker uses exact rational arithmetic to enumerate all fused-leaf subsets through nine leaves for 90 deterministic positive rational coefficient systems at each size (810 cases), verifies the analytic singleton-spoke maximum, and independently checks all 4,050 strict-complementarity KKT witness pairs. It also solves the star optimization through an independent monotone scalar root computation and tests 700 deterministic random two-input inequalities.

Observed execution output:

```
EXACT_ALL_2_POWER_K_FUSED_FACES_VS_SINGLE_SPOKE_FORMULA_PASS k=1..9 cases=810
EXACT_KKT_REALIZABLE_STRICT_WITNESSES_PASS 4050
UNWEIGHTED_DEGREE_FOUR_AND_HUB_MASS_PHASE_PASS
INDEPENDENT_SCALAR_ROOT_TWO_INPUT_STRESS_PASS cases=700
ALL_STAR_GRAPH_TV_MODULUS_CHECKS_PASS
```

The exact global formula for *all* finite star sizes and all positive real coefficients relies on the four-step analytical proof in `RESULT.md`. The finite checks cannot certify an all-dimensional statement or independent scientific priority. Mathematical review here is same-model only; independent audit has not been performed.

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

Run `python verify.py` in a Python environment with `sympy` and `numpy`. The checker performs exact rational differentiation of the defining quadratic map, exact symbolic verification of the convex endpoint formula and the spectral threshold, an exact rational \(k=4\) expanding witness, and algebraic verification of a critical equality certificate; numerical planar sampling is corroborative.

Successful execution includes `EXACT_REFLECTION_JACOBIAN_IDENTITIES_PASS 30`, `EXACT_SPECTRAL_CHORD_AND_THRESHOLD_IDENTITIES_PASS`, `EXACT_EXPANSION_WITNESS_K4_PASS`, `EXACT_CRITICAL_DIRECTION_CERTIFICATE_PASS`, and `ALL_NEW_QUADRATIC_SUBGRADIENT_CHECKS_PASS`.

The all-dimensional spectral-chord reduction, compactness argument, global segment integration, and general-supercritical necessity are analytic arguments in `RESULT.md`, not consequences of finite experiments. Independent mathematical audit has not been performed.

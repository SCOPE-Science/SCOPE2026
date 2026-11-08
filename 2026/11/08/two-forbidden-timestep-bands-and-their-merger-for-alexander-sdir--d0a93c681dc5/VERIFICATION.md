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

Execute `python3 verify.py` from the extracted package directory. The checker uses only standard-library exact rational arithmetic extended to the quadratic field \(\mathbb Q(\sqrt2)\), and tests every critical fixed-rational-step sign with exact algebraic comparisons. In particular, it checks the two step bands' separation for each integer \(m=5,\ldots,9\), their shared negative point for many \(m\ge10\), and the exact identities used to show positivity of the two offdiagonal matrix-entry classes.

The all-integer conclusions are proved symbolically in RESULT.md using the universal sign of the hub quadratic, the two-sign-change Descartes argument for the leaf quartic, and a one-variable degree-ten threshold calculation. The script's finite-degree numerical consistency tests are supplementary. The analysis concerns the final end-step map only, not the internal Runge–Kutta stage values. Independently administered audit has not been performed.

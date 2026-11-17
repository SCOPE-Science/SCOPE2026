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

Run `python verify.py` with Python 3, NumPy and SciPy available. The program executes direct Euclidean cross-product sampling in \(\mathbb R^3\), evaluates a one-dimensional arcsine slice for the *exact* conditional distribution, and integrates it against the exact chord-length density. The quadrature at thresholds \(0.02\), \(0.005\), \(0.001\) gives respective ratios to the leading asymptotic \(0.80287354\), \(0.87458996\), \(0.92615252\), consistent with the cutoff proof and substantial finite-threshold corrections. The direct samples independently agree within five predicted binomial standard errors at two thresholds. Execution marker: `SPHERE_CHORD_TRIANGLE_SMALL_AREA_CHECK_OK`.

The gamma/beta identities and existence of the limit are analytical; fixed-threshold integration and Monte Carlo are supporting checks, not substitutes for the uniform layer estimates. This is not an independent review or mathematical certification. Older inaccessible full-text sources create historical-priority uncertainty.

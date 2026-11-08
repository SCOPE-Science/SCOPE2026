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

The mathematical proof is in `RESULT.md`; this note records checks that corroborate it. The standalone `check_hilbert_dirichlet.py` implements direct Hilbert distances by first sampling independent gamma coordinate arrays, normalizing each to a Dirichlet point, and computing the maximum minus the minimum of the *logarithmic coordinate ratios*. This is independently compared to numerical quadrature of the analytic beta-prime order-statistic formula.

Executed command: `OPENBLAS_NUM_THREADS=1 python check_hilbert_dirichlet.py`. With seed fixed in the checker, all tests passed: five finite configurations with 100,000 independent pairs per configuration, three tested distance thresholds per finite configuration, three large-dimension configurations with 6,000 pairs each, six small-radius comparisons, the special-function identity at concentration one, and the exact harmonic mean. The final checker line is `HILBERT_DIRICHLET_RANGE_VERIFIED_FINITE_CDF_AND_LIMIT_SANITY`.

Analytic checks used in the proof: the ratio of two independent gamma variables of equal shape has beta-prime density; normalized common factors cancel in the Hilbert distance; an integral over the sample minimum gives the complete range CDF; a beta integral gives the small-radius constant; and the **joint** two-tail limit establishes independent limiting extremes. Finite simulation does not prove these identities or moment convergence. Package paths are self-contained with `requirements.txt`; numerical integration uses SciPy and NumPy. Large-dimension tests only check finite values against the asymptotic predictions, not the limit theorem itself.

The model is symmetric Dirichlet sampling in the barycentric coordinates of a simplex with at least two vertices, fixed positive concentration parameter, and unhalved cross-ratio Hilbert distance.

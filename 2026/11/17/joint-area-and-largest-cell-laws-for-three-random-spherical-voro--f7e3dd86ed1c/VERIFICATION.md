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

# Reproducibility checks

Run `python verify.py` with NumPy and SciPy as in `requirements.txt`. The actual packaged script was executed and printed `THREE_SITE_JOINT_AREA_CHECKS_OK 350000` followed by measured diagnostic values.

The checks are: a two-dimensional quadrature normalization of the angle density; numerical quadrature of the largest-cell expectation; 350,000 independently simulated triples of surface-uniform sphere points; direct Euclidean chord-angle reconstruction; comparison of four CDF thresholds, the mean and one nontrivial two-angle rectangle against their analytical integrals; and direct spatial nearest-site assignment for six sample tessellations using 85,000 additional random sphere points each.

The deterministic proof in `RESULT.md` establishes the infinite continuum assertions through an affine Blaschke–Petkantschin disintegration and exact finite integrals. No finite sample certifies a continuous density or all real parameter values. The available comparison literature does not constitute proof of historical uniqueness, and independent mathematical review has not been performed.

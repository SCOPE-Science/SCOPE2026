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

The accompanying `check_ratio.py` is a Python 3 standard-library script. Run `python check_ratio.py` in the directory containing this file and the script. Its expected success marker is `CONE_RATIO_DISTRIBUTION_AND_TAIL_OK 9`.

The checker uses two independently constructed quantities: the Euclidean chord from actual three-dimensional coordinates, and the exact surface geodesic from unrolling the cone. It compares six Monte Carlo survival proportions (180,000 pairs each) with six independent one-dimensional numerical quadratures, checks ambient chord squared against a separate algebraic expression for every sampled pair, and compares six near-endpoint ratios at two tolerances for three cone openings. Nine grouped checks pass. The proof's continuous and infinite quantifiers are justified analytically in `RESULT.md`; samples and quadrature do not certify them by themselves. Independent mathematical audit remains unperformed.

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

# Verification and reproducibility
The theorem has a self-contained proof in `RESULT.md`. Run `python3 verify_mixed_polygon.py` with the Python 3 standard library; the expected deterministic output is `MIXED_POLYGON_HULL_OK 1008`. The check constructs vertices directly, computes every pairwise Minkowski sum's convex hull with a monotone-chain algorithm, and compares its shoelace area with the closed analytic formula for orders 3 through 14, multiple radii and angles including cusp and maximum cases. It also tests the two-adic alignment rule. This is a finite, floating-point diagnostic only, not an exhaustive infinite mathematical certificate.

The mixed-area support identity, cosine-arc period/reflection derivation, angular mean normalization and modular parity proof are the analytical justification for the complete result. The first public motivating source is the arXiv posting of June 20, 2026. Historical priority remains provisional; independent mathematical validation has not been performed.

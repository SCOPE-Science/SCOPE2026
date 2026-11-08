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

The derivation reduces each omitted-vertex class count to the matrix-tree formula for the corresponding induced complete split graph. Dividing by the spanning-tree count yields an exact bivariate coefficient formula; a summable factorial majorant, a separate treatment of clique-only subtrees and the negligible independent singletons justify dominated convergence. Differentiation verifies strict monotonicity of the limiting spanning probability.

Reproducible finite checks: run `python check.py` using the Python standard library. The checker computes exact Kirchhoff cofactors, enumerates edge subsets on small graphs, checks subtree-class counts by independently enumerating selected vertex sets, and compares finite-size coefficient ratios against the analytic limit at three different growth ratios. Its successful output is `VERIFY_OK 868 exact/analytic-limit assertions`.

The finite comparisons cannot certify an infinite limit; the proof supplies that step. A general total-omission Poisson theorem was previously published, but it does not by itself determine the joint class-specific law. No independent mathematical audit or independent scientific validation is claimed.

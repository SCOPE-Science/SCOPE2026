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

# Verification scope

The standalone deterministic `CHECK.py` uses only Python standard-library exact fractions and finite exhaustive candidate checks. It reports 903 local edge tests and six graph comparisons, including the strict monotonicity of the quadratic interval maps and equality of candidate edge-hitting and vertex-cover minima. These computations are illustrative independent checks; the all-closed-subsets existence theorem and NP-completeness rely on the detailed mathematical arguments in RESULT.md, not on a finite dataset.

Read sources include the motivation paper's arXiv version 1, especially its definition, root-contraction theorem, interval/circle construction and tripod counterexample, plus source records for cubic-planar vertex-cover NP-completeness and an older ambient Euclidean global-attractor theorem. Historical priority outside those sources has not been fully established.

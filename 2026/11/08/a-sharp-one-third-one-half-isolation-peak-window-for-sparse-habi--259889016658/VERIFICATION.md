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

# Reproducibility and scientific limits

The mathematical theorem is established in `RESULT.md`, equations (1)–(6). The key nonstandard bound is the degree-\(d\) second-derivative maximization; its stationary point and strict inequality can be checked directly by differentiating \(d q^{d-2}((d-1)-(d+1)q)\).

Use `python3 check.py` to run exact rational checks with no third-party dependencies. The standalone script performs: 914 realizable tree-degree multisets for orders three through eighteen, sign and concavity tests at rational parameters, independently enumerated survival expectations for several small trees and cycles, the one-extra-edge chorded-cycle boundary, and a 14-vertex connected dense witness with two local maxima. It terminates with PASS lines or raises AssertionError on failure.

Exact finite computation is **not** a proof of the unbounded theorem, nor are three sampled derivative points a global concavity certificate. Those global statements follow from the analytic proof only. The ecological reading is conditional on independent homogeneous persistence and the graph representation; no empirical validation is asserted. Literary novelty is provisionally supported by primary comparisons and requires independent priority review.

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
# Verification of the finite tests

Run `python independence_theta_verify.py` using ordinary Python 3; no third-party packages are needed. The program constructs every independent-set flip graph directly, calculates its all-pairs distances by BFS, and checks whether each outside edge participates in a geodesic that changes both selected coordinates. For each pair, this is equivalent to direct inclusion-maximality of its two-class edge-general-position set. The expected maximality is computed independently from the graph's triangle-containing edges.

Observed successful output:
```
VERIFY_OK graph_profiles=1258 tested_pairs=13050 tested_flip_edges=25084 direct_BFS_geodesic_criterion=PASS triangle_edge_boundary=PASS
```
All labelled graphs on \(2\), \(3\), \(4\), and \(5\) vertices were exhausted; 160 additional six-vertex edge masks used a deterministic pseudorandom seed, including the empty and complete graphs. The verification is a finite cross-check only. For arbitrary order, the mathematical proof in `RESULT.md` establishes the theorem. No external or independent mathematical audit is asserted.

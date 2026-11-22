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

# Reproduction and checks

Execute `python3 verify.py` using Python 3.10 or later; no external Python packages are required. The script enumerates all labelled simple graphs with three to six vertices, rejects disconnected graphs or those with a vertex of degree at most one, computes shortest paths via breadth-first search, tests every unordered triple, and compares the maximum with the stated formula. It also constructs the triangle-barbell witnesses for orders six to twenty and checks minimum degree, connectivity, and exact triameter.

A separate independent census using NetworkX's unlabelled graph atlas through order seven yielded admissible counts \(1,3,11,61,507\) and maximum triameters \(3,4,6,7,9\). No claim of exhaustive verification beyond seven vertices is made. The all-order argument is mathematical, using the explicitly identified published canonical metric projection and the new single-double-fibre obstruction.

The source record for the motivating theorem is arXiv:2611.17259v1, publicly submitted November 12, 2026. The earlier extremal \(2n-3\) classification is in Das–Abdioğlu (2025), Theorem 4.3.

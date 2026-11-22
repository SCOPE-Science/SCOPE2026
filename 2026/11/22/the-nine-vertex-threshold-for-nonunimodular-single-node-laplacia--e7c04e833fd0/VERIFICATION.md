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

Execute `python verify_tree_census.py` with a standard Python interpreter. The program is standalone and uses no third-party libraries. It independently generates all unrooted tree shapes at each order from one to nine by attaching a leaf, deduplicating by complete rooted-tree isomorphism codes. For each coordinate root it constructs the integer Laplacian walk/Kalman matrix, verifies the exact determinant by two separate elimination implementations, checks the complete determinant frequency table, and verifies the explicit mod-two parity annihilator for exceptional roots.

The run confirmed the nine-vertex count \(47\), the tree-root frequency \(361\) singular, \(60\) unimodular, \(2\) of absolute determinant \(2\), and no nonunit nonsingular cases below order nine. Induction on the leaf deletion property proves complete enumeration; the determinant algorithms use exact integer and rational arithmetic rather than floating-point tolerances. This finite exhaustive computation proves nothing about trees of order ten and above. No independent audit has been performed.

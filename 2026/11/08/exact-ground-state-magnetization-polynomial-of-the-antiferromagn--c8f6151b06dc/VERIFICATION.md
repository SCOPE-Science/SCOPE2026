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

# Verification record
The included `verify_24cell_ising.cpp` constructs the signed-root graph, checks that all eight signed-coordinate octahedra give an exact disjoint partition of the 96 edges, independently enumerates the complete 24-spin configuration space twice, and computes the magnetization polynomial through two exact integer algorithms. It checks the result against expected coefficients and independently reconstructs a published independence-set enumeration as a control.

Actual checks: 276 unordered graph vertex-pair partition tests; 16,777,216 Gray-code direct Hamiltonian configurations; 16,777,216 separate local-octahedron mask configurations; and the complete independent-set face-vector comparison. The compiled replay prints `VERIFY_OK full_spin_masks=16777216 local_masks=16777216 edge_pairs=276` when successful.

The statement concerns a complete finite configuration space and uses only exact integers. The enumeration is not a proof of a family of unbounded graphs. The review was performed without external independent scientific validation; historical priority relative to unindexed exact Ising-polynomial datasets remains open.

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

# Reproduction and boundaries

Run `python3 verify_even_partition_fixed.py` with `collapse_certificate.json` in the same directory. The verifier uses independent restricted-growth-string generation, validates all simplices, checks each free-edge/triangle elementary collapse, and checks the connectivity and cycle ranks of the resulting one-dimensional complexes.

Verified representatives: an eight-cycle, a product of two four-cycles, four transpositions, and three transpositions with two fixed points. Their fixed face counts are respectively (2,1,0), (10,11,2), (58,163,90), and (26,67,42). Triangle removals are 0, 2, 90, and 42; remaining graph ranks are 0, 0, 16, and 0. The other dihedral elements are covered by explicit cycle-type enumeration and symmetric-group conjugacy of the action on partitions. The checker expects 4,140 set partitions, 378 even-block vertices, 1,995 edges, and 1,890 triangles in the ambient order complex.

A successful finite replay supports exactly the stated eight-label classification. It does not prove a uniform family for arbitrary labels or certify absence of unindexed prior publication. No independent mathematical review has been performed.

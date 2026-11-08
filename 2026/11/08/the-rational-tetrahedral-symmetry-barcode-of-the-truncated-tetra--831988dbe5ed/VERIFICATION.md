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

# Verification and scope

The complete source for the exact checks is `verify.py` (Python 3 standard library only). Run `python3 verify.py` in a directory containing the extracted files. The expected output, independently saved from a successful actual execution, is `verify_output.txt`. Every face at graph distances one and two is regenerated from its twelve-vertex definition, not loaded from a table.

The verifier checks the graph degree sequence and diameter, the two face vectors, and all five consecutive boundary ranks over \(\mathbb F_2\), including explicit pivot indices. These mod-two independent families imply rational lower bounds. Rank upper bounds follow from the eleven-dimensional reduced vertex boundary image, the boundary-composition identity, and the number of tetrahedra. Thus the full rational chain ranks are established. An independent exact-rational matrix reconstruction produced the same ranks, without entering the claimed verification program's dependencies.

All 24 tetrahedral-label permutations are checked to preserve the graph edges and both face sets. Their signed simplicial Lefschetz traces are computed on **oriented** faces and shown constant on each of five conjugacy classes. Both character formulas are checked separately against the permutation action on four labels and its parity. The result includes rational positive-degree persistence for this graph only; no integral lattice splitting, Borel equivariant cohomology, or equivariant homotopy equivalence was checked or asserted.

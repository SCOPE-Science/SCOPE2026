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

The proof identifies an exact union of simplicial subcomplexes; it uses the homotopy gluing lemma and the nullhomotopy of circle maps into a simply connected core. These are all-parameter arguments, not computer extrapolations.

Run `python verify.py` with only the Python standard library. The script independently enumerates all shortest-path general-position subsets of three-row rook graphs with \(3\le n\le6\), builds the proposed join/attachment complex, compares their complete face sets, checks pairwise-thickening intersections, and computes mod-two reduced Betti numbers by exact XOR elimination of simplicial boundary columns. Compare stdout with `expected.txt`; both files are included.

The computational scope is finite. In particular, mod-two homology alone cannot prove integral torsion-freeness or the claimed homotopy equivalence. Those features are established by the explicit contractible-attachment argument and the fact that all subsequent two-cell attaching maps are nullhomotopic. No independent audit has been carried out.

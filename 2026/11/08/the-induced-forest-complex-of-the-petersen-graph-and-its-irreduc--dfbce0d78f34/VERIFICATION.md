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

# Exact verification

Run `python3 verify.py` using a standard Python 3 installation. The script builds the ten pair-vertices and fifteen disjoint-pair edges, checks every one of the 1024 possible face masks with two different acyclicity tests, and reconstructs and verifies the entire finite Morse matching and acyclic oriented face poset. It independently performs bitset mod-two simplicial boundary reduction. Finally it checks signed fixed-face Lefschetz numbers against the exterior-square formula for all 120 coordinate permutations and obtains an irreducible degree-six character.

The executable output is supplied in `verification_output.txt`. The proof of the **integral** homotopy type uses Forman's acyclic matching; the mod-two calculation alone would not suffice. The rational representation follows from the signed chain-level Lefschetz formula and homology concentration. This establishes only the stated finite graph, not an infinite family. No independent external audit is asserted.

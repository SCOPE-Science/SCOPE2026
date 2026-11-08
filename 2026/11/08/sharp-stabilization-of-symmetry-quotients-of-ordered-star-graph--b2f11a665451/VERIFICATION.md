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

The mathematical proof is the cell-by-cell orbit-graph argument in `RESULT.md`. The standard Lütgehetmann graph deformation theorem is used as a stated literature dependency. The code independently generates all noncentral list placements, center-particle placements, and every edge indexed by the arm into which the centered particle moves; its orbit construction retains distinct edges with common quotient endpoints. It compares actual quotient graph Euler ranks to the fixed-arm Burnside formula over exact integers.

Run `python3 verify.py` to reproduce `verify_output.txt`. There are 42 test cases with particle counts \(p=2,3,4\), arm counts \(m=3,4,5\), and subgroup actions drawn from the trivial, cyclic, dihedral, alternating and symmetric groups (where applicable). All pass the integer equality and the published trivial-subgroup Ghrist rank. This is finite corroboration only. The unrestricted theorem, sharp threshold, and all subgroup cases are established symbolically, not by finite enumeration.

The proof does not claim homotopy quotient cohomology, integral equivariant character decompositions, or a complete scan of unindexed priority. The assessment here is a self-review; an independent mathematical audit is not performed.

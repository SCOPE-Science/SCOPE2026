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
# Finite verification and limits

Execute `python3 verify.py` using a standard Python 3 interpreter; no additional packages are needed. `verify_output.txt` records the exact output of an execution from these package bytes.

The checker builds the full spider graph, tests each vertex subset by explicit connected-component searches, computes augmented mod-two simplicial homology using independent bit-matrix elimination, and compares the resulting Betti numbers against the theorem. For small complexes it constructs the actual hub link, directs every Hasse edge upward only when it belongs to the proposed toggle matching, and checks acyclicity by topological sorting. It also enumerates each admissible arm-length-preserving permutation and computes signed face Lefschetz sums, comparing them with the determinant-twisted exterior-augmentation trace. These computations independently corroborate the topology, matching structure, and symmetry characters.

Observed output: `ALL_VERIFY_OK cases=59 face_instances=62408 matching_cases=42 matching_faces=13896 signed_character_checks=85`.

The verifier is finite, checks mod-two homology rather than integral torsion, and cannot establish an unrestricted theorem. Torsion-freeness, the integral module, and the homotopy equivalences follow from the explicit relative chain complex, the acyclic matching, and Hurewicz--Whitehead arguments in `RESULT.md`. No external independent mathematical validation has been performed.

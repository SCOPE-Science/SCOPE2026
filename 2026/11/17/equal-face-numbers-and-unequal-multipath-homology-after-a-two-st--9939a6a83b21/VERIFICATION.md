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

# Verification summary

Execute `python3 checks/verify.py` from this directory. The complete expected console transcript is included as `checks/verification_output.txt`.

All seven-vertex faces are enumerated twice: first over all arc-index combinations of cardinalities zero through six, then by recursively extending valid faces. The independently obtained face sets must agree exactly. Directed path membership uses in-/out-degree constraints and direct cycle traversal. The script checks the unique directed-triangle count, all augmented simplicial boundary ranks over \(\mathbb F_2\) by both column and transposed row elimination, and the identity \(\partial^2=0\) by direct cancellation for every face.

The checked exact outputs include the common face-cardinality vector \((1,21,142,370,351,93,3)\); ranks \((1,20,122,242,90,3)\) and \((1,20,122,248,90,3)\); and nonzero reduced Betti ranks \(\{2:6,3:19\}\) and \(\{3:13\}\). All two-step reversal positions on three through six vertices are also enumerated to verify the small-order boundary.

These are exhaustive finite computations for the stated finite graph examples. They do not certify integral torsion, homotopy types, or any uncomputed larger tournament. No independent audit has been performed.

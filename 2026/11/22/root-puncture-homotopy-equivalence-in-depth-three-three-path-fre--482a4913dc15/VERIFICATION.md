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

# Verification

Run `python3 CHECK.py` from a directory containing this file and `CHECK.py`. Compare standard output with `EXPECTED.txt`; the checker is pure Python 3 and needs no external packages. It enumerates all allowed faces for a 15-vertex complete binary and a 16-vertex nonuniform rooted height-three tree, verifies the deletion/link face partition, discovers and validates explicit elementary collapses relative to the common subcomplex, and computes reduced mod-two Betti numbers by exact bit-vector boundary elimination.

The binary example produces 9298, 5329, 3969 and 2401 faces in the ambient, deletion, link and common subcomplex, 1464 deletion pairs, 784 link pairs, and a rank-one reduced degree-seven homology group for the last three complexes. The nonuniform example produces 16372, 9344, 7028 and 4116 faces, 2614 and 1456 relative pairs, and rank two in degree seven. Both full complexes have zero reduced mod-two homology.

The checker is not a certificate for all parameters and is not an integral homology calculation. The all-parameter integral theorem follows from the elementary-collapse proof, the known homotopy type of star factors and the join and mapping-cone arguments. No independent audit was performed.

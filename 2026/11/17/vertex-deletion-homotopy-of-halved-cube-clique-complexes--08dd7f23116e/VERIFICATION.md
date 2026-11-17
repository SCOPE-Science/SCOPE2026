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

Run `python3 verify_halfcube.py` from this directory; only the Python standard library is required. The recorded exact output is `verification_output.txt`. The program is deterministic and prints `PUNCTURED_HALFCUBE_FINITE_CHECKS_PASS` after completing all assertions.

For each \(n=4,5,6,7\), it independently enumerates all cliques directly from the distance-two adjacency relation and using the odd-neighbor simplex / three-coordinate-cube classification; it checks equality of the complete face sets both before and after puncture. It then constructs mod-two boundary matrices by their actual codimension-one faces, reduces each matrix by independent bitset Gaussian elimination, verifies all reduced Betti numbers, and checks the octahedral generating spheres and their four-coordinate cone fillings. The full-complex nonempty face totals are 80, 392, 1776, 7632 and punctured totals 53, 316, 1584, 7176 respectively. The integral theorem is proved in RESULT.md by a structural argument and an established integral homology theorem, **not** by treating these finite tests as an all-parameter proof.

The classifying assumptions are parity-even Boolean subsets, symmetric-difference distance exactly two on distinct vertices, induced simplicial vertex deletion, and \(n\ge4\). No assertion about integral torsion is inferred from mod-two ranks. The verification does not assess independent validation.

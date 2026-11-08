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

# Verification of the integral homotopy calculation

Run `python3 verify.py` with the Python 3 standard library, from the directory containing this document. `verify_output.txt` records its completed output. The program builds every 15-vertex subset mask and the 260 disconnected induced triples, independently checks the smaller-subset connected-triple rule, constructs ten explicit three-plus-three partition blocks, and verifies all 90 tetrahedra and all 195 dual triangles. It verifies the 260 missing-triangle cones and the complete nine-skeleton of the ordinary cut complex. Complete simplicial boundary ranks over characteristics 2, 3, 5, 7 are `(14,91,80)`. Every check covers its stated finite universe, and `VERIFY_OK` is emitted only if all assertions pass.

Integral torsion-freeness is not inferred from those four modular ranks. It follows instead from disjoint two-face supports of the ten simplicial three-sphere boundary matrices and their primitive integral images. The high-dimensional Hurewicz and Whitehead steps are mathematical deductions from the complete lower skeleton, not checks performed by the finite script. No independent audit has been performed.

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

The explicit coefficient matrices and a complete, standalone Python/SymPy exact-arithmetic script are provided. `python verify_hadamard.py` reproduced `verification_output.txt`; the program checks determinants, separability and disjointness of coordinate roots, the bidegree of the ramification polynomial, projective smoothness in all four charts, twelve distinct coordinate-axis branch images, and the intersection-genus arithmetic. Its arithmetic is performed exactly modulo \(101\).

The general theorem is proved by intersection theory, local coordinate analysis, smoothness openness and the finite-field nonempty-open witness. The script establishes a witness for open conditions, not the universal claim by enumeration. No independent audit or external validation has been performed.

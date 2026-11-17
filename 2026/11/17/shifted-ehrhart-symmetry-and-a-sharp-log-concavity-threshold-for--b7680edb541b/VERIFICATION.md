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

The algebraic proof uses the determinant of a cyclic bidiagonal matrix, forced-zero barycentric propagation, the ordinary lattice parallelepiped height enumerator, and a direct lower bound on coordinates of \(M^{-1}x\). The cutoff is established by strict monotonicity of \(B_w/A_w\) and exact comparisons at weights six and seven.

Execute `python3 verify.py` using Python's standard library. Its independently enumerated first and second dilations verify the claimed coefficient values for weights two through nine. The exact tests also check the normalized-volume identity and the finite integer threshold. Their finite range does not prove the infinite statements or establish historical priority.

The related November 12, 2026 preprint supplies specific independently credited facts and narrows the claim of originality. The result has received self-review but no independent audit.

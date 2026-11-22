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

# Verification and reproducibility

Run `python3 dimensionality_boundary_check.py` with Python 3 standard library. The restricted-growth recursion enumerates each identity-singleton partition exactly once. The block-product test checks saturation; an independent direct decomposition-quantifier loop checks every accepted partition, and inversion is computed from the multiplication table. The finite abelian group list is exhaustive below order twelve using the elementary classification of finite abelian groups. The order-six nonabelian group is \(S_3\).

Expected final output: `DIMENSIONALITY_BOUNDARY_OK`. The program also prints full boundary counts, the two witness class-product tables, and the automorphism-orbit assertion for all four exceptional \(C_{12}\) partitions.

No computational claim beyond the stated finite orders is made; reproducible enumeration is not an independent mathematical audit.

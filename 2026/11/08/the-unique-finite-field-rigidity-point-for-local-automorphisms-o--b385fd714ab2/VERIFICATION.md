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
Run `python verify.py` with Python 3, no external dependencies. The checker iterates all 512 linear maps of a 3-space over the two-element field and all 19683 linear maps over the three-element field. For each map and each input vector, it compares its value with the images given by the entire explicitly enumerated group of ordinary Lie automorphisms. This independently checks the local-condition equivalence, including the unique rigidity case. Expected output is in `verification_output.txt`.

For twelve parameter pairs (four integer field orders, three symplectic ranks), it evaluates both standard classical-group order products and checks their quotient against the claimed index. An independent enumeration of all 65536 binary 4-by-4 matrices yields exactly 20160 invertible matrices and 720 symplectic matrices, a quotient of 28. No extension-field arithmetic is emulated in the separate order-product check, but the integer formula is exact for all prime powers. The universal theorem rests on the group-theoretic argument in RESULT.md, not on exhaustive finite dimensions. The 2024/2025 Heisenberg classification could not be fully inspected, so computational reproducibility does not resolve its historical coverage.

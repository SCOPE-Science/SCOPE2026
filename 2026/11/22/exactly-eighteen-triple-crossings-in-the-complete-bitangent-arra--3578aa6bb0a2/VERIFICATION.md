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

# Reproduction

Run `python3 verify_bitangent_arrangement.py` under Python 3 with SymPy. It uses exact polynomial arithmetic, a complete finite field projective-line crossing enumeration modulo 433, and independent determinant-triple enumeration. Output marker: `BITANGENT_28_LINE_18_TRIPLE_324_DOUBLE_CERTIFIED`. Reconstructed mathematical facts are stated in `RESULT.md`. The implication from good modular specialization to characteristic-zero exclusion is a mathematical argument, not an automated sampling claim.

**Scope limit:** The test alone does not certify historical priority or independent correctness review.

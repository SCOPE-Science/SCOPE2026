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

The proof is an algebraic argument valid over all fields: simultaneous eigenspace lifting via the underlying linear commuting projections, automorphism invertibility on the nilpotent graded filtration, and a finite-field orbit-stabilizer computation using symmetric monomial eigenspaces. The encoded coefficient count uses the actual commutative polynomial monomial basis, not ordered tensor words.

The attached `commuting_verify.py` independently enumerates the original defining substitution identities in the ten-dimensional binary jet algebra. It checks \(262144\) generator assignments, \(770\) idempotent maps and \(592900\) ordered pairs, obtaining \(9988\) commuting pairs. The complete joint tangent-rank histogram and derived finite-field expression agree. The script ends with `ALL_COMMUTING_JET_RETRACTIONS_VERIFIED`.

Finite exhaustive checks support the exact small case; they do not establish arbitrary field or truncation cases, which rest on the proof.

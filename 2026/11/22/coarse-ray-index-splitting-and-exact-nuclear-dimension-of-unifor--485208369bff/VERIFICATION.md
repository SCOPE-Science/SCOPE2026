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

# Verification record

This theorem requires symbolic operator and exact-sequence checks, not numerical experiments. Each nontrivial dependency is visible in RESULT.md:

1. On the countably many distinguished basis vectors the shift advances by one; elsewhere it is the identity. Every nonzero matrix entry lies within the asserted propagation radius, and the two defect projections are computed explicitly.
2. The rank-one projection is zero in the containing algebra's \(K_0\), because the shift implements a Murray–von Neumann equivalence between the identity and its rank-one complement.
3. The compact ideal has \(K_0\cong\mathbb Z\) and \(K_1=0\), giving the stated exact sequence and explicit splitting by the index \(-1\) unitary.
4. The externally published Property A nuclear-dimension upper bound [1] and the standard quotient-permanence theorem [4] yield dimension at most one. Nonzero \(K_1\) prevents zero-dimensional local AF. Conversely, extension permanence for nuclearity rules out finite nuclear dimension without Property A.
5. König's lemma supplies the required ray for an infinite connected locally finite Rips graph.

No claim is made of independent validation, proof-assistant certification, exhaustive literary review, or a computational proof of an infinite theorem.

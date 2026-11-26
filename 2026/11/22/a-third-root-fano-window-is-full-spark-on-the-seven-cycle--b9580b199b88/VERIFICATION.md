---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The Weyl operators shift the selected column labels by a common time-frequency offset, up to nonzero column phases and an invertible row map. Every maximal minor therefore has a representative containing column 0. Eliminating that column along row 0 reduces nonsingularity to the stated six-row determinant; the window coordinates are units. The ring is Z[ζ21], since ξ=ζ21^3, ω=ζ21^7, and ξ^5ω=ζ21. In characteristic not 3 or 7, roots with exact orders seven and three similarly give a primitive 21st root and hence a valid reduction; nonzero reduction implies nonzero original determinant. I inspected both frozen positive checkers and independently replayed all 12,271,512 reduced minors using cross-multiplication to eliminate column 0 and exact transposed batched elimination over p=2300000473. Trial division verifies primality; ξ maps to 325378545 and ω to 243671788 with exact orders. Every minor was nonsingular, with maximum-column-label checksum 515403504. Products and their signed differences fit int64 because p²<2^63. For exclusion I independently checked every CSV mask, every seven-column witness and all seven signed determinant coefficients over the integers. Each coefficient list is constant, so it vanishes at ξ. All 64 normalized masks are present, including the constant window, and global sign preserves spark. Replay: python3 /workspace/branches/verify5_private.py ternary and python3 /workspace/branches/verify5_private.py binary. These are exhaustive finite statements, not rank estimates. The conclusion concerns least root order q=3, not three distinct phases or conditioning.

## originality

PASS

Pass is for the explicit positive third-root Fano window and the resultant exact alphabet threshold, not for the separately covered binary obstruction. The distinct same-day binary finding has exactly the same negative statement. The closest primary explicit constructions deliver full spark with higher-order roots or unconstrained algebraic entries; they do not give an order-three witness at N=7 or resolve its exact alphabet threshold. The finite literature search does not settle historical priority for every equivalent window.

## value

PASS

Full spark means maximal erasure tolerance for the entire redundant cyclic frame. The Fano difference set is a canonical small design and the least admissible phase order is a concrete implementation constraint, not a freely chosen numerical sample. A single exact positive witness settles the upper bound against the proven binary obstruction and supplies a reusable benchmark for phase-constrained construction. No general dimension cutoff or quantitative conditioning is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.

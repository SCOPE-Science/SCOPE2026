---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Reconstructed full state (16 binary cells, one position and one of four headings), update turn/flip/move and explicit inverse. Every state is cyclic because the finite update is a permutation. Independently enumerated all 4,194,304 states and 128 rule-preserving translations/D4 actions, with global board complement for orientation reversals; grouped all primitive cycles. Exact independently recomputed complete 25-row table: 46,976 primitive temporal cycles, 4,194,304 period-weighted states, 376 geometric classes, minimal period 16 (16,384 cycles), maximum period 512 (256 cycles, two classes). This is exhaustive integer enumeration for this finite object, not extrapolation to other torus sizes. Original C++ full-source certificates separately use orbit mapping and Burnside fixed-cycle sums.

## originality

PASS

The complete all-start-state temporal-period and geometric-quotient census on the nondegenerate 4x4 square torus was not implied by the compared general reversible-ant and single-initial-configuration sources, or published smaller 3x3/3x4 exact tables. Novelty is best-of-knowledge, not an absolute absence of old enumerations.

## value

PASS

The 4x4 torus is the first nondegenerate even-even periodic square grid with four distinct cardinal neighbors. Its exact 25 clock lengths, sixteen-divisibility beyond the known general even-even eight-divisibility restriction, and nontrivial 376 orbit symmetry classes are a natural complete classification and reproducible benchmark for initial-condition sensitivity. A single motivated complete finite object is substantively useful even without an all-n formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.

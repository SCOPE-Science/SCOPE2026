---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The orbit classification and reachability criterion are mathematically correct. A source component is a tournament, so any injective homomorphism sends all its chosen coordinates into one target component and preserves every old orientation; independent pairs from different source components impose no homomorphism constraint. Conversely the coordinate map satisfying refinement and restriction is a finite partial monomorphism, and Coleman’s MB-homogeneity theorem extends it to a bimorphism. Antisymmetry, rank, covers and the two exponential-formula enumerators then follow. The frozen verifier independently enumerates set partitions, weights tournament blocks and checks the comparable-pair count both by Bell products and direct refinement through the advertised finite range.

## originality

FAIL

The final claim is implication-covered by prior structural results plus routine bookkeeping. Coleman’s primary paper explicitly defines MB-homogeneity as extension of every finite partial monomorphism to a bimorphism and, in Example 5.13, proves the exact infinite disjoint union of random tournaments MB-homogeneous. For two injective tuples in this already-described structure, the coordinate map is a partial monomorphism if and only if component blocks only merge and all old tournament arcs are preserved. Thus the advertised reachability criterion is the direct specialization of the published extension property; automorphism orbits as component partitions decorated by finite tournaments follow from the same structure’s component permutation and random-tournament homogeneity. The Bell/tournament generating functions are standard labeled-set-partition enumeration after that specialization. Exact wording or integer sequences need not appear in the prior paper for this implication-level coverage.

## value

PASS

The finite action order is a natural and useful invariant of an oligomorphic transformation monoid: it records directed merger dynamics, ranks, covers and comparable pairs rather than only static automorphism orbits. Its explicit form can still be useful expositionally even though it is too directly implied by the earlier MB-homogeneity result to be accepted as original.

The dated certificate retains the supplied scientific assessment, sources and limitations.

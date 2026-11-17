---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

In T(a,b,c), a directed 3-cycle consists of exactly one vertex from each of the three transitive blocks. S(x,y)=[x=y or no third vertex making a cyclic triple] consequently defines the blocks in FO^3, and S(x,y)∧R(x,y) is their internal total order. Recursive path-length tests reuse only three variable symbols and separate every finite block size; a directed cycle of representatives records their cyclic order. Every vertex has both an in-neighbor and out-neighbor, giving an indefinite two-pebble Duplicator strategy. Burnside gives [binom(N-1,2)+2*1_(3|N)]/3, and rigid internal orders give N!*binom(N-1,2)/3 labelled objects. Independently re-enumerated cyclic composition orbits for N=3..13 and obtained the formula. These finite tests corroborate, not replace, the unrestricted-depth pebble/formula arguments.

## originality

PASS

The 2026-11-08 general two-variable tournament theorem strictly covers the FO^2-blindness part for source/sink-free tournaments, but does not imply the FO^3 interpretation, orientation-sensitive cyclic triple classification, exact spectrum, or labelled census. Classical C3-structure identifies interval behavior but not this logic threshold; surviving three-variable theorem is a nontrivial new claim at the best-of-knowledge level.

## value

PASS

An exact expressive-power boundary for a natural tournament substitution family, distinguishing unrestricted-depth FO^2 from FO^3 and classifying all theory types. The recoverable cyclic block order is a structural lemma applicable to other tournament logic constructions; the nontrivial k=3 threshold is not merely a formula-renaming artifact.

The dated certificate retains the supplied scientific assessment, sources and limitations.

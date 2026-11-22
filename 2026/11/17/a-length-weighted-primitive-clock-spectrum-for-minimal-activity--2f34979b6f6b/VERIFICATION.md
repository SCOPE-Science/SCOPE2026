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

Assign every vertex its unique firing phase mod p. For each phase configuration its allowable residual chip count is u_v in [0,a_v-1], with a_v the number of neighbors firing immediately before that vertex, so its number of time-zero microscopic states is exactly product_v a_v. Choosing these predecessors gives a functional digraph whose every directed cycle has length divisible by p. In a theta graph no two vertex-disjoint directed cycles exist; the unique directed cycle uses two complete terminal-to-terminal arms, in one of two orientations; the remaining arm has exactly its L_i acyclic pointing-to-terminal choices. The p global phase choices cancel temporal rotation, and unique single firing forces least period p. Independent exhaustive phase counts on theta(1,2,3) yield four period-4 and two period-5 temporal orbits and zero period-6, agreeing with formula. No general counting assertion relies on this finite sample.

## originality

PASS

Classical theta cycle-length divisibility supplies existence, while the exact length-weighted orbit multiplicity across all p>=4 requires counting phase-dependent microscopic chip heights and directed parent forests. Source 3-cycle formula concerns a different p and is excluded.

## value

PASS

A complete all-period exact enumeration on a natural rank-two graph tests how three competing cycles contribute to periodic chip dynamics. The opposite-arm length weighting distinguishes existence from microscopic temporal multiplicity, and yields a compact arithmetic graph fingerprint with potential use in studies of synchronous firing orbit statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.

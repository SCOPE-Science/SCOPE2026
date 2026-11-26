---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Each center has binomial(3,2)·2²=12 points at exact distance two, and the independent replay found 27 distinct incidence rows. A support is shattered exactly when its restrictions among the 27 rows exhibit all 2^j Boolean traces. The replay enumerated every support through size four and found (1,27,351,2808,3402); at size five the required 32 traces exceed the number of centers, so there are no omitted higher faces. Of the 2808 triples, 2268 extend to a four-face. The sentence about smaller faces in the frozen facet argument needs the fact that every pair extends, not merely that all pairs are faces; the replay verified 351 of 351 pairs lie in a shattered triple. Equivalently the listed four-face representatives contain a pair of each possible mutual distance, and the action is transitive on pairs of each distance. Thus there are only 3402 four-facets and 540 three-facets. Enumeration of all 1296 actions reproduced six disjoint orbits with the displayed representatives and multiplicities, including the two distinct size-1296 orbits. The replay rebuilt the binary boundary columns and obtained ranks (26,325,1913). For the augmented complex on a nonempty vertex set these give zero reduced degree zero and degree one, degree two 2808-325-1913=570, and degree three 3402-1913=1489; all other degrees vanish. The frozen scripts were inspected without execution. The fresh finite replay is complete for this universe, not a formal certificate or an integral homology test.

## originality

PASS

The strongest inspected comparisons share either the ternary universe or the exact-distance-two predicate, but not both in the same shattering-complex definition. No inspected result covers the ternary distance-two census, six orbit representatives and binary boundary ranks as a whole. The matching Resultary entry is the frozen record itself, not independent coverage. Same-day distance-three comparison establishes a contrast, not relative chronology.

## value

PASS

The first three-symbol three-coordinate cube supports a natural comparison of the three nonzero Hamming relations within one small symmetric space. Exact-distance-two shattering behaves differently from ordinary Hamming adjacency and the antipodal sphere: it reaches dimension four and has maximal faces of two dimensions. The six types specify exactly which supports can occur by symmetry, and the binary homology distinguishes additional structure that the face polynomial and Euler characteristic alone cannot fix. This is a complete, reusable finite reference for the trace relation, rather than a numerical approximation or an arbitrary size cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.

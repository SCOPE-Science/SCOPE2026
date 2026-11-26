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

A shortest path between two vertices on a single cycle fiber cannot spend any steps changing rows. Four chosen points on one cycle fiber block both arcs for an alternating pair, proving the known upper bound 3s. With n=3q+u the gaps of the given starts are (q,q,q), (q,q,q+1), or (q,q+1,q+1). The short-arc condition is q>=2s-2 for u=0,2 and q>=2s-1 for u=1; these hold throughout the stated domain including n=6s-6, and imply q>=s+1. Each band has s columns and is separated from its cyclic successor by at least one empty column. For a same-band pair the horizontal-then-vertical route uses a shortest arc and hits the terminal band column only in its selected row. Any two different bands can be oriented as cyclic successors. The forward distance h_j+t-r is positive and at most n/2, and the entire vertical leg can be put in the first unused column past the initial band; the row legs meet only the chosen endpoints. This works also with equal rows and tied shortest cyclic arcs. Thus all 3s vertices are mutually visible without a finite-to-infinite inference.

## originality

PASS

The new contribution supported by the comparison is attaining the known upper bound in an unbounded long-circumference region by staggered triads. Neither the upper bound itself nor the short-side results or any excluded value are claimed as new.

## value

PASS

This proves the expected tight upper bound for every height at least three and all sufficiently long cycles, with an explicit threshold linear in height and the extra boundary n=6s-6. It addresses a natural two-parameter conjecture in an entire regime rather than a small census. Its explicit geodesics explain why row saturation is possible and isolate where the balanced-gap proof stops.

The dated certificate retains the supplied scientific assessment, sources and limitations.

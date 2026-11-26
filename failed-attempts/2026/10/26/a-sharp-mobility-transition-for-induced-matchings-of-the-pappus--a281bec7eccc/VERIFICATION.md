---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Under the explicit replacement rule in Assumptions (one deletion and one insertion, not symmetric difference of size one), induced matchings are cliques in the complement of the squared line graph. The fresh standard-library replay at /workspace/branches/pappus_independent_replay.py enumerated its maximal cliques by pivoted Bron–Kerbosch and their faces, then built exchange neighbors in shared-face buckets. It reproduced maximum size 5, orders 135 and 27, zero top exchanges, unique parents and K5 fibers, 486 size-four exchanges, degrees 4:27 and 8:108, 54 quotient edges of multiplicity four, and the stated isomorphism on all 351 quotient pairs. All 135 BFS runs reached 135 states; eccentricities 8:108 and 9:27 and distances (486,648,918,1296,1836,2160,1242,432,27) reproduced exactly. With unique parents, cross-fiber adjacency requires parent overlap at least three and equality follows because overlap four is excluded; a common triple gives precisely the Cartesian product of two possible fourth edges on each side. Neither frozen program was executed.

## originality

FAIL

The frozen record as presented claims graph-specific structural novelty already materially covered by the 2026-10-18 Resultary record 1c32026064e0. That record explicitly establishes the frozen 27 optima, 135 size-four matchings and unique parents, and identifies the overlap-three graph on maxima with L(P). Those facts immediately imply the K5 fibers, quotient with multiplicity four, connectivity and total edge count for fixed-cardinality exchanges. The earlier result does not establish the exact size-four degree and distance statistics; these remain a potentially distinct narrower result, not an acceptance of the frozen claim.

## value

PASS

The exact diameter, radius and eccentricities answer a natural worst-case transformation-cost and centrality question for the full deficiency-one token-jumping graph of a canonical incidence graph. They are not consequences of connectivity or the diameter of the compressed optimum graph. This useful metric remainder does not make the already covered structural assertions new.

The dated certificate retains the supplied scientific assessment, sources and limitations.

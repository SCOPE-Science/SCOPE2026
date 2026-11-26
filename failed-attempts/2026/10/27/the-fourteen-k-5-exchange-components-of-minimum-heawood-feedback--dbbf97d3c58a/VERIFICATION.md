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

Deleting k vertices from the cubic graph leaves 21−3k+e(S) edges, so a forest for k≤4 requires k=4 and independence of S, and its complement then has ten vertices and nine edges. If all four deletions are points, the other three must be collinear: a noncollinear triple yields a six-cycle and a collinear triple yields a tree. A selected line with three nonincident point deletions leaves the three points of that line and one off it. Their joins via retained lines make a subdivided star with leaf lines attached, hence a tree. With two points p,q and two lines selected, the only eligible selected lines miss p and q. The two lines through p other than pq and their two counterparts through q induce disjoint matchings on the four points off pq; their union lifts to a retained eight-cycle. Duality exhausts the other cases. Inside each five-set every two four-sets are adjacent, and across families same-side five-sets meet in only two vertices while opposite-side four-sets meet in at most two by bipartition counts. Independently, python3 /workspace/review-evidence/checks.py 2 constructs the Heawood graph from the Hamiltonian cycle and alternating chords, verifies its Fano incidences and connectivity after every deletion of at most two vertices, then exhausts the FVSs and exchange edges. It got 70 minimum FVSs, 14 components and 140 edges. The frozen scripts and outputs were inspected, not executed.

## originality

FAIL

The earlier indexed Heawood classification gives the identical minimum set system, including its Fano-geometric incidence structure. Under the specified exchange rule, the claimed complete exchange graph follows directly from that classification, not merely from a coinciding total count. This is demonstrable coverage, not an adjudication of external publication priority.

## value

FAIL

A disconnected exchange graph for a small 3-connected cubic bipartite graph is a sensible witness in principle. Here the exact components and their edge count are mechanically implied by the already classified Fano-geometric families: one intersection test yields every edge and no further argument about Heawood reconfiguration is needed. This record supplies no substantive remaining mathematical gap beyond making that immediate corollary explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.

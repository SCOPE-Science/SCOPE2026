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

Both explicit designs have 26 distinct triples and cover all 78 pairs once. In any dominating set, 13-p<=3q, and at most 6p-binomial(p,2)+t(P)+q block vertices are covered, where t(P) counts triples in P. For p+q=8 the first bound forces p<=5. For p<=3 even the cruder bound 6p+q<=23 fails; for p=4 at most one triple fits, and for p=5 at most two fit (three triples have union size at least six). Both bounds leave too many disjoint blocks to select. Smaller sets extend to size eight and are excluded. Two intersecting blocks give a five-point union P and four disjoint blocks, which cover every point outside P since any such point has six incident blocks but at most five meeting P. Thus gamma=9. The same inequalities force 5<=p<=7 at size nine, and the containment of all disjoint blocks plus point coverage is necessary and sufficient. An independent exhaustive replay instead branches on uncovered closed neighborhoods in the 39-vertex graphs, without using that occupancy restriction. It found 1456 and 1511 minimum sets, respectively 2652 and 3192 undirected one-replacement edges, and component profiles {676^1,17^39,1^117} and {936^1,51^1,48^3,24^6,17^3,13^1,10^9,1^82}. In the order (5,canonical), (6,canonical), (6,noncanonical), (7,canonical), the occupancy counts are (195,624,507,130) and (195,574,612,130). Both sorted labelled-mask digests agree exactly with the frozen digests. No supplied script was executed.

## originality

PASS

The common domination number nine and the existence of two STS(13) types are prior facts, and the frozen text does not claim otherwise. The supported distinct result is the complete minimum-set, occupancy and replacement-graph census for the pair, showing what the scalar invariant and its invariance under this Pasch switch do not capture.

## value

PASS

The two known STS(13) types exhaust the natural comparison class, and domination and its one-replacement connectivity are standard, interpretable invariants of the corresponding Levi graphs. The exact census shows a genuine distinction not visible at the optimum size: the Pasch switch changes the six-point sector, the number of isolated optima and the sizes of reachable components. This gives a reproducible comparison for the study of exchange connectivity, not a recomputation of gamma alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.

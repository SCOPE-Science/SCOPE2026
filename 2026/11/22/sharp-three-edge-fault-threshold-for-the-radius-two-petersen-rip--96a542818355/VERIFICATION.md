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

For H=P−F connected, the required complex is the clique complex of the square of H, not a deletion from P². I inspected the frozen orbit, cover-reversal and acyclicity code and the recorded output; the frozen script was not executed. An independently written exact replay, `python /workspace/reproduce_petersen.py`, uses outer-cycle/inner-star labels (with an explicit disjointness-label isomorphism) and Floyd–Warshall, and enumerates all 576 sets of sizes 0–3 without orbit reduction. For sizes 0,1,2 respectively, all 1,15,105 graphs are connected with a radius-two cone vertex. For size 3 it finds 10 disconnected, 200 cones, 180 other contractible, 60 with rank-one H₂ and 5 with rank-four H₂. For every connected noncone case it constructs the flag complex and uses elementary free-face collapses to a complex of dimension at most two, not the frozen matching/pivot list. It then contracts a spanning tree in the edge/triangle presentation and kills every remaining generator by a sequence of triangle relators with exactly one still-unknown generator; this certifies simple connectedness. H₂ of a finite 2-complex is free, with rank χ−1 here; representatives of a basis by Hurewicz give a homology equivalence from the corresponding wedge of 2-spheres, hence a homotopy equivalence by simply connected Whitehead. The case rank zero is contractible. The replay also checks that the five rank-four cases are precisely the distinguished three-edge sets described in the originality comparison. The frozen output header 'facets-by-cardinality' counts all faces rather than only maximal faces; that naming does not affect the proof.

## originality

PASS

The supported distinct contribution is the complete radius-two edge-fault threshold and 380/60/5 classification with the exact disconnecting count, not a previously unknown four-sphere wedge of 2-spheres. There is demonstrable isomorphism-level prior coverage of that homotopy type once the five faulted graphs are recognized as subdivided tetrahedra. The inspected broader results do not imply which deletion patterns realize it or the full fault classification.

## value

PASS

The Petersen graph is a canonical diameter-two graph, so its intact metric gives a simplex and the first change under recomputed distances is a natural robustness invariant. The classification resolves the whole minimal fault budget: most connected triple deletions leave contractibility, but there are two sharply different integral homotopy outcomes. The exact correspondence to the five subdivided tetrahedra and known Petersen independence topology aids interpretation; merely recalculating that known wedge would not by itself be the contribution. No general fault theorem, other-scale claim, or persistence-map statement is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.

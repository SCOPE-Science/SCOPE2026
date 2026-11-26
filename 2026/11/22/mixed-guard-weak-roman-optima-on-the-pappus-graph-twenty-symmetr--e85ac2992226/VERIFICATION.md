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

For the connected 18-vertex Pappus incidence graph, a function with positive support S and doubled set T is valid exactly when S dominates and each zero can either borrow from a neighbor in T or replace a singly occupied neighbor in S and still dominate. The independent replay exhausted 985,663 assignments of weight at most eight. Nothing below eight worked, and the 2,691 minima split as 1,755/882/54 by number of doubled vertices. Enumeration of point permutations preserving line triples and of point-to-line bijections preserving incidence gave all 216 automorphisms: connected bipartiteness makes these the only two possibilities. The orbit distributions by class are 27×1, 108×8, 216×4; 18×1, 108×2, 216×3; and 54×1, giving 20 orbits. Every unit transfer to a distinct vertex with occupancy at most one was tested against the minimum set, with graph adjacency imposed for slides. All-source BFS reproduced connectedness, 18,846 jump and 6,372 slide edges, radii and diameters (8,9) and (9,12), and the respective eccentricity counts (1,323,1,368) and (567,1,422,486,216).

## originality

PASS

Credit the exact all-singleton subcase to the secure-domination work. The supported distinct claim is the complete weighted optimum classification, including the 936 doubled-label optima in seven orbits and the full unit-transfer graphs. The strongest inspected same-graph source does not cover those claims; broader weak Roman results are background, not the weighted census.

## value

PASS

The Pappus graph is a standard cubic symmetric test object. The weighted optimum and transfer invariant answers a concrete question left by the secure-set census: do the doubled optima occur, and how do they change the move geometry? They constitute over a third of the optima and introduce distinct symmetry types; the exact slide diameter increases from 10 to 12 even though additional optimizers and moves are allowed. This gives a substantive finite benchmark for distinguishing jump and slide reconfiguration, not a new name for the singleton enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.

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

Reconstructed the labelled graph from RESULT.md's cycle and chords, matched each edge to the packaged list, and directly checked quartic degree and girth five on 19 vertices. The observation sets are monotone; a proper stationary set cannot later be completed. Using synchronous set propagation with initial closed neighborhoods at round one, independent enumeration found no successful size-zero, singleton or pair candidate, and 753 successful triples, with rounds 2–5 having counts 109,320,204,120. Independently built the two graphs by explicit single-vertex replacements restricted to those triples, retaining a replacement for slides exactly when the removed and inserted vertices are adjacent in the base graph. Breadth-first search from each vertex gives exact distance by discovery layer, and reached all states in both graphs. It reproduced both complete distance tables, the 14,538 and 3,452 edges, jump eccentricity three throughout, slide eccentricities 717 at six and 36 at seven, and excess counts 29,788, 131,574, 109,054, 12,688, 24. The test is pairwise: either slide distance seven or excess four forces the joint distances (3,7), disjointness and two four-round optima. The stated example belongs to the exceptional set. An independent bijection backtrack preserving adjacency and nonadjacency enumerated the complete 24-element automorphism group and recovered exactly the same 24 pairs from that example, with union of endpoints exactly the 36 states of eccentricity seven. These checks exhaust the specified graph and states, not general power domination instances.

## originality

PASS

The proposed distinct finding is the complete minimum-configuration and relocation metric on the Robertson cage. The graph identity, definition of power domination and general reconfiguration models are established. The closest inspected same-object works address a different process, while the closest same-parameter catalogue result addresses a different graph. No compared theorem or table supplies the Robertson metrics.

## value

PASS

The unique quartic girth-five cage and minimum configurations give a natural finite monitoring benchmark. Comparing the two complete metrics isolates the cost of enforcing local moves while never using extra sensors. The sharp four-move separation, its incidence with diameter seven and exact single symmetry orbit provide more than a raw sensor count or a specially selected example. The exact data are useful for testing how relocation constraints interact with feasibility and monitoring latency, without claiming a general cage theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.

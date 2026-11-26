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

Independently reconstructed the supplied 27-edge graph as the triangle on {1,3,10}, both vertices {4,7} joined to all three, and six degree-three ears, one for each choice of two triangle vertices and one degree-six vertex. Adding a self-vote only at even degree gives exactly the specified strict majority with tie retention, since a one-vote self term cannot overturn a strict open-neighbor majority. Enumerated the 2,048 masked states using that rule. From the states with F²x=x, a reverse-edge breadth-first traversal reaches all states, tracks each eventual basin, and gives first-entry depths with counts (96,742,850,324,36). The only fixed masks are 0 and 2047, each with basin 935; all 49 individual catalog rows agree. The 47 two-cycle basins have sizes 2,6,8 with multiplicities 27,18,2, totaling 178 states. The fractions reduce to 935/1024 and 89/1024. Depth four gives F⁶=F⁴, while the witness 179→119→51→49→0 gives F⁵≠F³. Distinct degrees force automorphisms to preserve the triangle and the pair of degree-six vertices; their independent permutations each extend uniquely because the ears have distinct neighbor triples. Acting on unordered phase pairs gives seven classes of sizes 2,3,6,6,6,12,12, with the two constant masks fixed separately.

## originality

PASS

The general period-at-most-two result and the named graph are established. The distinct contribution is the exact evaluated census, including individual basins, sharp entry time and graph-automorphism classes for this explicit deterministic system. The checked deterministic prior work does not tabulate this graph, and the superficially related Apollonian majority-vote study has a different update law and different observables. No inspected result supplies this full graph-specific classification.

## value

PASS

The input is a canonical small maximal planar graph, not an arbitrary selected mask or subgraph. The exact census quantifies two different aspects of stabilization on it: very many periodic attractors (47 against two fixed points) despite only 89/1024 of initial states entering any such attractor. The sharp stopping time, catalog and symmetry reduction are useful for exact comparison of dynamics on other named networks or validation of finite majority algorithms. The result is a complete finite invariant, not a claim about consensus on planar graphs generally.

The dated certificate retains the supplied scientific assessment, sources and limitations.

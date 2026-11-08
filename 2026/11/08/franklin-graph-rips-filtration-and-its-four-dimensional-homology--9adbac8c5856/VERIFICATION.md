---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

From the same directory execute `python3 verify_franklin.py` with Python 3.9 or newer. The script contains the complete graph, every finite enumeration rule and assertions for all claims. Its deterministic terminal output is included in `verification_output.txt`. Running the extracted program from the packaged file reproduces this output exactly.

Two maximal-clique/face enumeration methods agree on all 196 faces, including the empty set. Both vertex-order Morse matchings are entirely enumerated and their acyclicity is checked across all 588 Hasse incidences. There are 96 matched pairs (including an empty-face pair) and four unmatched two-cells. The graph automorphism enumeration visits all 48 adjacency-preserving permutations; signed simplicial Lefschetz traces yield a trivial one-dimensional plus character and a three-dimensional minus character of norm one. The graph's distance-three relation is checked to be isomorphic to its original adjacency relation. An additional direct mod-two rank calculation gives boundary ranks 11, 37, 35, 10, 2 in degrees one through five, hence second Betti rank four. The homotopy equivalence rests on acyclicity, not this field-homology evidence.

No general theorem for other graphs, integral representation decomposition or equivariant wedge map is certified here. Independent external audit has not been performed.

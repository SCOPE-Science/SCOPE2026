---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Independent computation rebuilt the 20-vertex GP(10,3) graph, enumerated all 6212 augmented independent faces with the exact cardinality distribution, recreated the supplied stage-order matching (3103 disjoint pairs), checked six critical augmented faces (one dimension-4 and five dimension-5), oriented and topologically sorted all 30380 Hasse incidences, and recomputed the five signed integral Morse attaching-degree coefficients as 0. The empty face is paired to a vertex, yielding one ordinary critical 0-cell; Forman acyclic matching yields a CW complex with 0,4,5-cells only. The 4-skeleton is S^4 and π4(S^4)≈Z classifies 5-cell attachments by degree; degree zeros give S^4∨⋁^5 S^5. A separately written GF(2) boundary reduction produced ranks [1,19,141,519,991,932,383,97,18,2] and reduced Betti numbers H4=1,H5=5. The finite exhaustive proof suffices for one finite graph; neither stored VERIFY_OK nor sample tests were assumed as proof.

## originality

FAIL

Definitive exact prior coverage: published Resultary 2026/10/4/SCOPE-independence-complex-of-the-desargues-graph-is-s-4-vee-bigvee-5--f3b1cf10aadb/RESULT.md already proves the identical integral homotopy statement for the exact graph GP(10,3), with the same underlying 6212-face acyclic Morse strategy and five zero signed attaching degrees. A second published 2026/10/11 result proves the same. New verifier packaging and graph alias H(5,2) do not produce a novel mathematical theorem; no rescue through disclaimers or added certificates.

## value

FAIL

The Desargues graph and integral independence-complex homotopy type are mathematically natural, and an original full computation would be worthwhile. But the submitted exact S^4∨⋁^5 S^5 result, every homotopy conclusion and the essential finite Morse technique already appear in the published Oct-4 same-graph finding, as independently read. Alternative stage order, H(5,2) cross-check and rewritten verification scripts are reproducibility improvements without a new mathematical invariant, structural lemma, boundary or classification. As submitted this is a known-result recomputation rather than a new valuable scientific contribution; no separate mathematical remainder is stated.

The dated certificate retains the supplied scientific assessment, sources and limitations.

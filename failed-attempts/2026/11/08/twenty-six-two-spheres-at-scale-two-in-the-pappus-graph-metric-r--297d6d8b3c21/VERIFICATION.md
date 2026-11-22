---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

The LCF graph (18 vertices, 27 edges, cubic bipartite girth six) has 6 distance-four forbidden triples. At scale 2 the two same-side subcomplexes are each D_3*D_3*D_3 ~= wedge^8 S^2; all mixed edges are actual incidences; absence of four-cycles prevents a mixed 2+2 clique. The two cone-covered pieces U,V have intersection the original connected graph P and each collapses to a simply connected side complex. Since maps from P to U,V are null, the homotopy pushout gives wedge^8 S^2 vee wedge^8 S^2 vee suspension(P) = wedge^26 S^2, integrally. Scale 1 is P ~= wedge^10 S^1, scale 3 is the exact join of six discrete triples ~= wedge^64 S^5, and scale 4 is a simplex. Nonzero degrees appear only in separate successive stages, fixing integral and field barcodes. Independent reconstruction checked distances, q=3 affine-plane deletion graph isomorphism, all scale-1/2/3 face counts, exact U union V and intersection, and the full 225-face acyclic Morse matching with 99 matched pairs and 1 critical 0-cell + 26 critical 2-cells. Computation independently corroborates this finite graph proof; no bound extrapolation is used.

## originality

FAIL

The exact assigned claim is a q=3 corollary, explicitly spelled out, of an earlier full integral theorem for all existing affine planes of order q>=3 after deletion of one complete parallel class. The q=3 graph is the same Pappus graph (independently checked graph-isomorphic); the earlier theorem proves the same scale-two wedge, all filtration stages, torsion-freeness and every interval. The earlier source was publicly committed 2026-11-01T20:50:26Z, before the assigned source on 2026-11-08T17:30:17Z. This is decisive coverage, not mere similarity or an inconclusive literature search.

## value

FAIL

The graph and invariant are natural and the proof is informative, but this exact 26-sphere type and all stated barcode intervals are explicit q=3 special cases of the earlier general affine-plane deletion theorem. The assigned source contains no independently unknown homotopy type, persistence map, or structural lemma beyond the existing proof, which uses essentially the same homotopy-pushout decomposition. A duplicate exact calculation and an additional finite matching certificate do not supply a new mathematical finding or a substantive independently needed invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.

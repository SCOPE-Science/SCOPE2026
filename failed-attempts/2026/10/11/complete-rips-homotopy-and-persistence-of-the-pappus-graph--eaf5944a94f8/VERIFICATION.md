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

Independently reconstructed the cubic 18-vertex Pappus graph from the exact frozen RESULT.md LCF word and verified 27 edges, bipartiteness, distance-shell unordered-pair counts (27,54,54,18), diameter 4, and precisely six disjoint distance-four triples. A fresh independent 2^18-mask clique census reproduced face vectors r=1 (18,27), r=2 (18,81,108,18), r=3 (18,135,540,1215,1458,729); independent GF(2) boundary reduction reproduced ranks r=2 (17,64,18), r=3 (17,118,422,793,665), hence Betti counts 26 H2 and 64 H5. The analytic homotopy argument is sound: for r=2 every clique is pure-color or has exactly one vertex on one side (absence of C4), giving K2=U union V with intersection G. Mixed-cone simplices collapse onto the pure-color flag complexes, each D3*D3*D3 ≃ wedge^8 S2 and simply connected. Maps G→U,V from a graph are nullhomotopic; cofibration homotopy pushout is U∨V∨ΣG ≃ wedge^(8+8+10)S2. At r=3 the distance-four six 3-cliques complement makes K3 exactly D3^(*6) ≃ wedge^64 S5. At r=1 the triangle-free graph has cycle rank 10; r=4 is a simplex. Since successive positive homology degrees 1,2,5 do not overlap, homology inclusion maps between them vanish, yielding all stated field-independent barcodes. All quantifiers concern a fixed finite graph with inclusive real scales, not an extrapolated graph family.

## originality

FAIL

A DISTINCT publicly accessible 2026-10-11 mathematical record, SCOPE-20261011-4d3507a898b5 (Resultary/2026), already states the EXACT homotopy types of the same LCF Pappus graph at every inclusive real Rips scale: 18 points, wedges of 10 S1, 26 S2, 64 S5, then contractible, with identical six distance-four triples. Full RESULT.md was examined, not a search snippet. The assigned SCOPE-20261011-eaf5944a94f8 uses a different conceptual radius-two gluing proof, but its final theorem adds no new homotopy type. Its complete persistence barcodes follow formally from that published full-threshold theorem because nonzero homology at successive scales lies in different positive degrees and H0 connects at 1. The two public records were added by the SAME 2026-10-11T13:59:41Z reconciliation commit; this does not establish strict earlier priority of either, and no independent authorship is claimed. Regardless, the assigned result is exactly covered by a separate already-public scientific record and cannot be accepted as an original distinct mathematical finding.

## value

PASS

As a mathematical object, the canonical 18-vertex distance-regular Pappus Levi graph and its all-scale intrinsic Rips filtration are natural and motivated; exact integral homotopy types, field-independent barcodes and the conceptual decomposition 8+8+10 at scale two are nontrivial, informative benchmark invariants. The separate public result makes this final theorem scientifically COVERED, however; intrinsic mathematical interest cannot rescue originality. The alternate conceptual gluing proof might have expository value but the package offers no new stronger claimed theorem beyond the fully covered filtration.

The dated certificate retains the supplied scientific assessment, sources and limitations.

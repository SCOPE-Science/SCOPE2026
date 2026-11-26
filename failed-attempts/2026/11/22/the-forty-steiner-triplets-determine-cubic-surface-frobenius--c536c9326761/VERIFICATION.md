---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The 45 tritangent planes are the 30 triples (E_i,Q_j,L_ij) with i≠j and the 15 triples of L-lines indexed by perfect matchings of the six blowup indices. I built supports by two disjoint-plane decompositions and verified the six-plane and row/column intersection conditions, obtaining 120 supports with unique complementary partition and 40 triplets in one orbit. Independent Schläfli-label permutations (relabelings and the quadratic Cremona switch) generate all 51840 elements; generator conjugation gives 25 classes. The rederived table matches every frozen CSV entry up to local class relabeling and gives 25 triplet spectra, 20 line spectra, and 25 joint signatures. Fixed-point counts are sums of cycle lengths dividing the extension degree. The number of distinct prefixes is (10,14,20,22,23,24,24,24,25); the unique degree-eight collision is the stated order-12/order-9 pair and degree nine separates 4 versus 40. Finite étale descent of the intrinsic incidence marking and the standard Picard trace formula transfer this calculation to every smooth cubic over a finite field (with q known). The cutoff is sharp over all Weyl types, not necessarily within each small field size. Inverting Frobenius does not change any of the cycle data.

## originality

FAIL

The online ATLAS already supplies the exact 40-point action (40b), its compatible 27-point action, and one word in the same generators for each of the 25 classes. I verified the geometrical identification of its 40b representation by explicit generator-equivariant bijections, rather than inferring it from the degree or a common character-table label. Evaluating these supplied class words as permutations, tallying cycles and comparing columns mechanically gives all of the frozen reconstruction, cutoff and refinement statements. The equivalence is to a specific available class/representation dataset, not just to the abstract capability to enumerate a known group.

## value

FAIL

The inverse problem on a natural marking and the choice of a minimal observational cutoff are meaningful questions. For this frozen answer, however, all numerical separation facts result from the standard cycle and fixed-power summaries of an already available exact classwise action dataset. The record does not add an explanation of the separation beyond the table or a further independent arithmetic consequence beyond the usual Picard trace formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.

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

The length-five universe has 2^5(C(5,2)+C(5,3))=640 eligible words. Reverse complement preserves this set and is fixed-point-free because it would have to fix the middle symbol. After checking each two-word orbit internally, the remaining conditions are pairwise, so compatibility cliques are in bijection with all labeled codebooks, including the empty codebook. An independent regeneration used prefix/suffix set intersection and coordinate-deletion projections (two distinct words agree after some aligned coordinate is deleted exactly when they differ at one coordinate). It recovered 320 pairs, 104 admissible vertices and 1068 edges, and validated the seven-color certificate and matching witness. A binary include/exclude census terminating at leaves, with a degree-based choice of the branching vertex, gave (1,104,1068,3472,4648,2776,720,56), total 12845. All eight letter permutations commuting with complement preserve the allowed composition range, including the pair swaps that interchange counts two and three. Checking each permutation's fixed maxima gave (56,0,0,0,0,0,0,0), proving seven free orbits of eight. Thus the maximum is 14 words and every claimed coefficient and equality count is reproduced.

## originality

PASS

The closest matches separately omit Hamming separation or change the length and balance restrictions. None of the inspected statements supplies the combined admissibility graph, its size polynomial, or the maximum orbit classification. Pass is for that exact finite classification, not for the general clique reduction, strand-closure concept, or universal priority.

## value

PASS

Five is a natural odd test length: strand closure here forces two-word orbits and exact half balance is impossible, making the adjacent two GC counts the natural symmetric choice. Comparing with the otherwise identical maximum of 24 quantifies the true cost of aligned single-substitution detection (a drop to 14). The full size spectrum and classification of optimal designs up to the natural relabeling group give an exact benchmark beyond an exhibited example or mere upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.

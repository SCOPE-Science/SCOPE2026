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

Each one-order CW subcomplex is the join of the factor word complexes: every allowed pair of block subwords occurs, and face identifications are the join deletions. Mixed words cannot occur in both orders; the overlap is precisely the disjoint union of the two factors. Each factor is connected (a facet from a full permutation contains every vertex); coning into the opposite factor and then moving the endpoints along paths makes both maps from the overlap null. The subcomplex pushout is a homotopy pushout. Its constant-map double mapping cylinder is the two joins attached at the poles of the unreduced suspension of the overlap, hence homotopy equivalent to their wedge with that suspension. To split the latter, view it as the two unreduced component suspensions joined along their two common poles. The two-point inclusions into the connected suspensions are null, so the same pushout lemma gives the two suspensions and one circle. This avoids the imprecise maximal-tree wording in Step 4: the union of the two suspension arcs is already a circle. The joins and the component suspensions are simply connected, also when one alphabet is a singleton. Thus the circle is the sole fundamental-group generator. The known derangement sphere wedges, reduced join formula, and two available block orders give the stated full-symmetric and equal-block subgroup specializations. The frozen 234 Betti comparisons were inspected, not reproduced; mod-2 and mod-101 Betti checks alone do not establish an integral homotopy equivalence.

## originality

FAIL

No verbatim arbitrary-family formula was identified. Nevertheless the claim is covered by direct implication: the published concatenation/join identity in the product-indexed case supplies both pieces, the intersection is forced by the two orders, and the usual constant-map homotopy pushout gives the entire wedge, including the circle, without any additional classification of the pieces or attachment maps. The sphere and wreath-product specializations do not leave a distinct invariant beyond these implications.

## value

FAIL

The two-block construction and integral homotopy types are natural, but the submitted formula is a direct deduction from the existing join identity and standard pushout calculation. The full-symmetric and wreath-product displays only substitute known factor wedges. No distinct equivariant, interleaving, or other surviving mathematical claim was proved, so none is proposed as a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.

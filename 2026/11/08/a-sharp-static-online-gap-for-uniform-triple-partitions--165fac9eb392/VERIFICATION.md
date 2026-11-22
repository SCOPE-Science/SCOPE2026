---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Checked every step of frozen RESULT.md (Git blob 95e19f...): the all-positive realization restricts S to within m triples, at most two edges/triple (triangle transitivity forbids shattering). At 2m-1 or 2m support edges the forced-all-positive other m-1 full triples leave three vertices uniquely determined, making a selected negative edge impossible. The lower support with m-1 two-edge paths and one unqueried reserve triple realizes every trace via pair/singleton breaking and cyclic exchanges. For an online tree of depth 2m, following 2m-1 positive edges forces a forest and uniquely determines the triple partition, contradicting branching at the next level. The distinct strong witness uses m-2 path units and two one-edge units; r>=3 has two distinct cyclic derangements, and r=2 is handled by identity/swap when both single edges are positive or two orientations of a negative single edge otherwise. Every label admits two hypotheses, so adaptive leaf splitting yields depth 2m-1. m=1 has a singleton hypothesis and zero dimensions. The proof is for all integers m>=2, unordered triple blocks and ALL pair queries; finite checks corroborate but cannot generalize.

## originality

PASS

Qualified best-of-knowledge: the exact uniform triple-partition pair-equality class has the claimed (2m-2,2m-1) dimensions for all m>=2, and no inspected relevant primary theorem or previously published result entails both. Highly relevant Pasteris et al. (2018) supplies nonsharp general online bounds; Bressan et al. (2019) treats all partitions; the refinement-closed and size-capped classifications cannot be specialized because they allow refinements. Earlier (2,3)-two-block class has a different hypothesis domain and theorem. Negative database searches alone do not establish priority; alternative nomenclature remains risk.

## value

PASS

A mathematically motivated natural fixed-block equivalence concept class shows exact persistent VC-vs-Littlestone gap one for every nontrivial m, unlike refinement-closed partitions whose dimensions agree. The two-realizer trace lemma is a structural mechanism for converting near-maximal static shattering into an extra adaptive round. The result defines a complete sharp infinite-family classification with nontrivial capacity constraints, not a one-off tiny enumeration or an immediate substitution into a generic theorem. It does not claim noise robustness, other block sizes or a larger gap than established fixed-(2,3) products.

The dated certificate retains the supplied scientific assessment, sources and limitations.

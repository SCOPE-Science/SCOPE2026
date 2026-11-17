---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The infinite-parameter VC claim is proved by an induced matching on queried positions 2,5,...,3t-1 (all label patterns extend to maximal independent sets) and induction using the minimum queried vertex: conditioning on its answer 1 or, if it is vertex 1, 0 forces a dominated prefix and leaves a suffix of at most n-3 with independently maximal restrictions. Thus VCdim(M_n)=floor((n+1)/3) for all n. For n<=9 complete concept counts 1,2,2,3,4,5,7,9,12 make the 2^{VC}<=|M|<2^{VC+1} bound tight for Littlestone; at n=10 there are 16 concepts, and the actual fetched tree_P10.json has 15 internal query nodes and 16 distinct valid maximal independent-set word leaves consistent with every path, certifying Ldim=4 vs VC=3. The connected amplification inserts one separator between any two P10 blocks and sets it to 1 exactly when both neighboring block endpoints are 0; every juxtaposed choice of block concepts remains independent and dominating. This yields depth >=4k on P_{11k-1}; VC=floor(11k/3), so the lower gap is ceil(k/3). Independent finite enumeration through n=10 and k=2 tested 256 product realizers; infinite conclusion relies on symbolic separator proof.

## originality

PASS

PASS for the complete final theorem on connected paths, qualified. The prior November 2 record proves the exact P10 first gap and unbounded growth only for DISCONNECTED disjoint unions of P10, explicitly does not establish connected path amplification. The new separator embedding preserves full product without disconnecting the graph, giving linear unbounded separation for connected paths and a universal exact VC formula. Neither the known induced-matching upper bound nor the prior disjoint union alone implies the connected result. No equivalent earlier connected-path theorem was located in the checked indexed searches or primary comparison, but unindexed equivalent online-learning work remains a priority risk.

## value

PASS

PASS. Maintaining connectivity while obtaining an unbounded static/adaptive shattering gap is a meaningful new structural strengthening: paths are the simplest connected max-degree-2 graphs, and connecting disjoint components generally destroys the Cartesian product of maximal independent-set concepts. The explicit one-vertex separator extension solves the genuine domination boundary obstruction and proves quantitative linear gap along an infinite family. This is mathematically motivated even without an exact formula for general path Littlestone dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.

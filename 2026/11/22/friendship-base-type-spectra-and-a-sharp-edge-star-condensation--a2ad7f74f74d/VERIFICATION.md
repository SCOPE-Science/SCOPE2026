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

A named, injective tuple diagram occurs exactly if the combined graph is K4-free, and two realizations of the same diagram have the same full type by homogeneity. A forbidden clique cannot use endpoints from different petals. With a common hub-neighborhood C fixed, the potential cliques using old vertices are exhausted by the three triangle tests, the three independent intersection tests, and the empty triple intersection; choices then factor across the labeled petals. For nonempty C a singleton pair U=V={c} witnesses strict loss relative to C empty. In the dominant empty-hub term the both-neighbors state is an independent random set with inclusion p=1/4, with an additional triangle constraint that is vacuous for stars. An independent proof of the needed extremum orders k edges and partitions the event that some edge has both endpoints included by its first such edge. For the ith edge, conditioning on inclusion of its ends, one can exclude one endpoint outside it for each of the i-1 preceding edges, giving at least p^2(1-p)^(i-1) as the unconditional probability of that first-edge event. All bounds are exact for a star. For a nonstar order a disjoint pair first, if there is one: exclusion of that preceding pair then has probability 1-p^2 > 1-p. With no such pair, a pairwise-intersecting nonstar contains a triangle; ordering its edges first gives strictness at the third edge because the earlier two use the same external endpoint. Extra edges strictly reduce independence, as witnessed by selecting only the endpoints of a deleted edge. This proves the claimed sharp envelope and equality cases without needing a finite formulation from the clique-density citation. The edgeless count is (4^m+3^m)^r; finite numbers of labeled graphs and a strict exponential gap give the prefactor and conditional law for fixed r,k, including k=1. For r=2 the edge has petal bases 15,12,12,7 and the nonedge bases factor across the two coordinates. Twenty direct full-diagram tests across r=2,3 and m=1,2 agreed with the transfer; replay: python3 /workspace/branches/reproductions/combinatorics.py. This checks small cases, not the fixed-arity infinite limit or varying arities.

## originality

PASS

The complete-type framework, forbidden-clique tests in general, the weighted star extremum and the illustrative pair formulas are not claimed as independent new results. The supported distinction is the hub-conditioned transfer combined with the exact leading probability and conditional star structure for every fixed threshold in the stated range. The strongest earlier named-clique transfer has no shared hub and its explicit rare-edge law concerns the first two thresholds over that other base.

## value

PASS

Conditioning on several rare edges probes more than overall sparsity or a pair-channel count. For a natural common-hub parameter family this gives a whole range of exact exponential rates with multiplicities and identifies the unique surviving motif. It answers a motivated higher-arity question about uniform logical types, not random vertices or a new general extremal graph theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.

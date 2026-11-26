---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For the ordinary-poset root embedding, only root differences occur, so every step sign in Beck–Hlavacek's definition is +1. The root-sum condition forces consistent orientation of consecutive comparisons, giving an ordinary chain (possibly listed in reverse); transitivity gives the signed chain for each ordinary chain. Singletons are allowed. Using all chains, not just maximal chains, permits taking the positive and negative subchains. Thus x in the signed body implies x^+ and x^- are separately in C(P); conversely each difference from C(P) has every chain sum in [-1,1]. The antichain-vertex theorem gives a finite hull of signed differences, and deleting common coordinates makes each generator's squared norm the total size of two disjoint antichains. The largest such value is d_2. Strict convexity of the squared norm rules out mixtures of distinct generators from the contact sphere. A maximizing generator and its negative force radius ≥sqrt(d_2), and the average of the two squared distances to any other center is d_2 plus the squared displacement, ruling out every other center. Equality in the diameter bound is exactly antipodality of contacts. Every maximum support has height ≤2, equivalent to its induced comparability graph being bipartite; one pair of signings per connected component gives 2^c distinct signed points. The ordinal-layer, chain, singleton/antichain and ratio boundary cases follow by counting those supports: for the lower ratio endpoint, if a maximum antichain omits any point, a singleton second antichain raises d_2; the upper endpoint needs two disjoint maximum antichains. Independent replay by enumerating transitive subsets of naturally ordered comparable pairs at sizes 1 through 4, then testing all ternary vectors, all antichain-indicator differences, and all two-colorings of maximum supports, compared 50 posets, 1952 integer points and 282 contact occurrences without discrepancy. The frozen verify.py was inspected but not executed; integer-point enumeration does not certify the real-body identity. The proof applies only to the stated ordinary signed-chain specialization in fixed Euclidean coordinates.

## originality

PASS

The chain-body identity is a specialization of anti-blocking orthant decomposition combined with the defining chain inequalities. The discrete second width and indicator generators are likewise established. The independently useful residue is the full Euclidean contact invariant and its comparison with enriched-chain geometry, including the count over maximally supported bipartite induced subgraphs. The inspected published results give the bodies or combinatorial statistics, not this complete contact law. The elementary extension to a general stable-set difference body increases the chance of earlier equivalent work; no such published result was established in the bounded comparison.

## value

PASS

The relevant exact invariant is motivated by comparing two natural signed realizations of a chain polytope, where standard width and the second width govern different Euclidean radii. Knowing only the radius does not count or locate its contacts. An explicit all-poset description of those contacts and diametral pairs, including the support-weighted count and sharp comparison equality cases, is useful geometric information despite the short proof. This value does not depend on treating the anti-blocking decomposition or the Greene invariant as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.

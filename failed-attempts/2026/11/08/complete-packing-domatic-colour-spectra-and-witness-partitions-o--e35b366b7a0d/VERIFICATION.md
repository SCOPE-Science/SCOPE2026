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

The finite connected multipartite graph has diameter <=2. Packing forces every color >=2 to be a singleton, and any color-one vertices to lie within one independent part. Every high-color singleton broadcasts globally. A block containing only color-one vertices can dominate precisely when it is the entire color-one class and that class equals a full part. This proves kappa=h+1 exactly for full parts and kappa=h otherwise, including absence of color 1. Counting vertex subsets and injective assignments gives E. For W, partition h distinct high-color vertices into k unordered nonempty blocks (Stirling S(h,k)), attach s color-one vertices independently (k^s); in the whole-part case there is exactly one further option: a separate color-one block and S(h,k-1). The lower palette bound max(n-a+1,k) and forced equality cases yield the displayed k-spectrum/optimizer multiplicities, with k=n and complete-graph boundaries checked. Independently recomputed five profiles (K_3, K_{2,2}, K_{3,1}, K_{2,1,1}, K_{3,2}) at six palette values each by full graph-distance packing and set-partition enumeration, matching E and W exactly. The unrestricted proof is structural; finite tests only corroborate. All seven actual Git source blobs were retrieved at the assigned frozen commit; independently reconstructed their Git tree hash to 690aa5773fabf215d0eaf6edf83e6759ea3f9024.

## originality

FAIL

A published 2026-10-18 theorem for every connected diameter-at-most-two graph already gives every packing k-domatic map-count polynomial F_{G,k}(t), all optimal palette values, and all optimal named-colouring multiplicities in independent/maximal independent set counts. A complete multipartite graph is a specialization: its independent sets are contained in single parts and its maximal independent sets are precisely entire parts. Thus the submitted capacity enumerator is recovered exactly by [u^j]E=F_{G,j}(t)-F_{G,j+1}(t), and its entire spectrum/optimizer table is prior. An earlier 2026-10-12 published theorem even states the complete multipartite all-k spectrum explicitly. The only formula not printed in these prior findings is W_{G,t,k}, counting witnessing partitions; it follows mechanically from the 2026-10-18 theorem's explicit unique-obstruction proof by applying ordinary Stirling set-partition counts and assigning each color-one vertex to a root-bearing block. This is an immediate corollary of a previously proved stronger characterization, not a substantive new claim. Inaccessible primary manuscript is a disclosed residual risk, not relied upon for rejection.

## value

FAIL

The problem and exact witness-count normalization are natural, but the main spectrum, all-palette color-map enumeration, optimal-coloring classification and count are already proven by 2026-10-12/18 stronger diameter-two results. The only additional W formula requires no new graph structural understanding: it is the standard Stirling partition count applied immediately to the earlier 2026-10-18 necessary-and-sufficient proof of which rootless block is allowed. This is bookkeeping from an already complete characterization rather than an independently needed new exact invariant, meaningful cutoff or independent classification. Its correctness and reproducibility alone do not establish mathematical value as a new theorem; no surviving substantive repair is identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.

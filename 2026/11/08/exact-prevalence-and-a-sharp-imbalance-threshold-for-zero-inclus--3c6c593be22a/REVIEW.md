# Scientific review

**Claim reviewed.** Exact zero-inclusive EFX0 orientation census on labeled unit-valued bicliques, its structural partition into source-free and singleton-source families, and the limit law at the asymmetric part-size scale \(b\asymp2^a\).

## Correctness — PASS

The zero-inclusive EFX definition matches the source's requirement to check *every* removed item. A zero-indegree agent violates it exactly when a neighbor receives that agent's incident edge and another edge. The source criterion is necessary and sufficient because a comparer can value no more than one edge in another bundle. In \(K_{a,b}\) a source uniquely determines the orientation; all remaining orientations have no source. The two forbidden matrix events, a zero row and an all-one column, are mutually exclusive. Inclusion-exclusion gives the integer count. Dividing by \(2^{ab}\) and bounding the residual probability proves the threshold. The standalone independent direct-definition verifier checked \(142602\) complete small orientations and found no discrepancy. This finite verification does not replace the universal proof.

## Originality — PASS (best-knowledge, not independent certification)

The primary graphical EFX manuscript [1,2] introduces orientations, proves an NP-completeness result and the existence of possibly wasteful EFX allocations, and identifies several graph classes with guaranteed orientations. It does not establish the all-orientation count or probability law inspected here. Afshinmehr et al. [3] classify orientation existence on bipartite multigraphs by multiplicity and diameter, rather than counting uniform simple-biclique orientations. Neoh and Teh [4] study general counting complexity and minimum EFX multiplicity for other domains. Six actual semantic-record queries and literature searches for source, EFX0, biclique counting and random orientation found no dominating/equivalent statement. The closest ranked records concern other graph invariants, so the absence of a record does not establish uniqueness. Residual risk is a separately phrased or unindexed equivalent statement, particularly through known enumeration of source-free directed bicliques.

## Value — PASS

The question is whether uniform endpoint-only allocation is *typically* EFX0 in a simple dense bipartite network. A guaranteed fair outcome does not answer that question, and an exact count matters for random fair-allocation mechanisms and rejection-sampling feasibility. The result turns a qualitative existence issue into a complete probability law: for growing balanced bicliques fair orientations dominate, whereas crossing the sharp size scale \(b\asymp2^a\) yields a nontrivial limiting fairness probability and further imbalance forces rarity. The zero-inclusive deletion convention is a structural cause of the effect, not a cosmetic distinction. The cutoff and source classification motivate the precise invariant beyond a simple small numerical census.

## Closest literature and limitations

[1,2] provide the source setting and strong EFX convention; [3] provides related bipartite multigraph existence results; [4] provides broader counting motivation. The result is limited to simple bicliques, unit-valued incident edges, and orientations; it is not a general EFX counting algorithm or a claim for the zero-excluding variant. General combinatorial inclusion-exclusion is credited as a proof tool; priority in unindexed literature is not guaranteed. Independent external scientific validation remains unperformed.

Self-review: passed. Independent audit: not yet performed.

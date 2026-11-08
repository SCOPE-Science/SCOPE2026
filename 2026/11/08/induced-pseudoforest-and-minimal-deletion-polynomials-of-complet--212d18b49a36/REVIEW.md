# Mathematical review

## Correctness — PASS

The graph-theoretic core is the connected-component cycle-rank equivalence: an induced two-part biclique \(K_{a,b}\) is a pseudoforest exactly when \((a-1)(b-1)\le1\). A selection meeting at least three parts must use exactly one vertex per part and meet exactly three parts: \(K_{2,1,1}\) and \(K_4\) already violate pseudoforesthood. One-vertex extension tests then exhaust all maximal profiles, including the easily missed full-part \((2,1)\) class when an occupied part has size two and the other has size one. Counting the disjoint classes gives both polynomials, and the standard complement bijection gives minimal deletion sets. The asymptotics follow from explicit polynomial growth. Independent direct graph-subset enumeration within the same review agrees for 52 small graph instances. Limitation: finite checks by themselves prove nothing for unbounded order.

## Originality — PASS (provisional publication priority)

Full-text comparisons used Hanaka et al., DOI:10.4230/LIPIcs.SWAT.2018.24 / arXiv:1807.11518; Sheng, arXiv:1912.06966; and Lokshtanov et al., arXiv:2211.02717. Their inspected propositions concern orientation/deletion algorithms, kernelization, or approximation, not the complete family-specific labeled cardinality distributions. A related complete-multipartite dissociation enumerator concerns maximum induced degree one, which is not the pseudoforest condition (triangles and four-cycles are excluded by dissociation but allowed here). OEIS A134964 counts unlabeled pseudoforests rather than subsets of an assigned host graph. No equivalent complete multipartite result appeared in the completed mathematical searches. Residual risks: unindexed source formulations, and incomplete access to the older SIAM paper; these do not constitute a decisive implication from a known stronger result.

## Mathematical value — PASS

Pseudoforest deletion is a motivated optimization problem. The result classifies **every** minimal deletion set on a canonical multipartite family, not just the optimum cardinality. On connected regular vertex-transitive \(K_{m,m,m}\), almost every maximal induced pseudoforest has four vertices while the optimum has \(m+1\), and the exact feasible-size set leaves a growing interval of impossible sizes. This shows a strong distinction between typical maximal and maximum solutions in a highly symmetric family and provides a concrete enumeration benchmark. No theorem beyond this explicit graph family is claimed.

## Closest literature and limitations

The earlier algorithms do not count maximal vertex-set solutions. The proof and finite checker are bundled, but an independent audit has not occurred and priority is provisional. Claims of uniqueness beyond the searched literature are not made.

Self-review: passed. Independent audit: not yet performed.

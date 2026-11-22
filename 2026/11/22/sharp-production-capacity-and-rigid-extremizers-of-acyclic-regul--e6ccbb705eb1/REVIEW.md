# Review of sharp acyclic-grammar production capacity

## Correctness (C): PASS

The production-to-edge translation is exact and handles terminal and empty-string productions. Splitting all source edges yields the sharp sum-product recurrence for complete derivations. Strict monotonicity of the resulting integer-break product forces every edge to be productive at equality; if two distinct successor nodes each reached all remaining edges, acyclicity would fail. Hence equality forces a single chain of parallel-edge layers. Mixed-radix unary labels produce all consecutive lengths without collisions, proving the universal maximum and exact cover inverse. The two standalone scripts confirm sample budgets, exact word spectra and finite DAG equality cases, while the written induction supplies the infinite argument.

## Originality (O): PASS with residual priority risk

The November 12, 2026 Hetzl--Shadman paper establishes NP-completeness of regular cover, not exact production-cardinality capacity or unary interval production thresholds. Hetzl--Wolfsteiner (2019, Lemma 7) give the weaker \(2^{p-1}\) cardinality bound; the new sharp formula yields \(C(6)=9\). Wolfsteiner's 2020 dissertation cites logarithmic-size descriptions of finite unary languages but does not state this exact capacity or graph-rigidity classification in inspected sections. Recorded published-finding corpus statement/implication searches for unary intervals, cardinality, acyclic grammars, and extremal DAGs yielded no same claim. The 1981 Bucher et al. primary text and 2026 Hajac et al. full all-path graph paper could not be inspected; the latter maximizes a different all-endpoint functional, but an unquoted stronger sublemma remains a real possibility. These are explicit priority limits, not purported proofs of noncoverage.

## Value (V): PASS

Exact maximal language capacity at each grammar budget and all maximizing derivation graphs are useful structural benchmarks for regular-cover optimization. The unary consecutive-length family is a natural complete infinitely parameterized solvable subcase of a newly proved NP-complete general problem. Both the precise staircase and its \(3/\log3\) natural-logarithmic leading constant sharpen earlier qualitative logarithmic statements; the equality rigidity is not merely a renaming or parameter substitution. The result is independent of the lengths of rule labels, by design of this production-count model.

## Closest literature and limitations

The most directly related sources are Hetzl--Shadman (arXiv:2611.16562v1), Hetzl--Wolfsteiner (Theoretical Computer Science 798, 2019, Lemma 7), Wolfsteiner (TU Wien dissertation, 2020, Chapter 4), the 1981 Bucher et al. primary citation, and Hajac et al. (arXiv:2606.16095). Claims are restricted to acyclic right-regular productions with arbitrary terminal blocks; the exact cover corollary applies only to consecutive unary exponents. Independent external review and full-text priority comparisons of the two stated inaccessible primaries remain outstanding.

Self-review: passed. Independent audit: not yet performed.

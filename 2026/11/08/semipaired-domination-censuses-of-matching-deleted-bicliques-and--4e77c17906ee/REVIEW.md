# Self-review

## Correctness — PASS

For integers \(a,b\ge3\), the proof first identifies the only distance-three pairs (the deleted matching), then proves partnerability for every even set of size at least four, and separately enumerates all dominating shore-occupancy cases. Its inclusion-minimality argument checks **all proper semipaired subsets** through a two/four-set reduction; it does not rely on single-vertex deletions. Inclusion-exclusion counts the four-set configurations, and the one-edge crossover follows from an explicit exact polynomial identity. An independently implemented exhaustive graph-level checker agreed on all three polynomial coefficient dictionaries for 61 instances and 58,819 nonempty subsets. Finite checks are corroboration only, not the universal proof.

## Originality — PASS (provisional publication priority)

The closest examined primary papers are Henning–Pandey–Tripathi (2019, arXiv:1904.00964) on complexity and algorithms for semipaired domination, and Henning–Pandey–Tripathi (2020, arXiv:2008.13491) on chordal and block graph algorithms. Their complete accessible texts do not give the all-set/minimal-set enumerators of \(K_{a,b}\) with a matching removed or the exact order-ten sign change. Haynes–Henning (2018) provides the underlying concept and scalar inequalities. Results for *paired* domination are not equivalent to semipaired domination: a whole even shore is semipaired but has no induced perfect matching. An exhaustive publication-priority assertion is not made; the 2018 original was accessible only as a bibliographic abstract, and unindexed specialty articles remain a risk.

## Mathematical value — PASS

The family \(K_{a,b}\) minus a matching interpolates between complete bipartite and crown graphs and arises naturally as a dense bipartite graph with disjoint missing edges. The result determines every feasible semipaired-set cardinality and every inclusion-minimal configuration for three structural parameters. In particular it identifies long gaps between minimal cardinalities and a nonmonotone change in minimal **counts** under a single edge restoration: the sign reverses exactly at \(n=10\), even though the family of feasible sets is monotone under edge restoration. Those facts refine scalar semipaired domination and are not supplied by complexity results alone.

## Residual scientific limitations

The proof has scope \(a,b\ge3\) and deletion of a matching only. The 2018 introductory article's full text was not obtained; its accessible bibliographic description addresses parameter inequalities and trees rather than labeled distributions. The available literature search cannot establish absolute novelty. The computational evidence is finite, and no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.

# Scientific review of the Desargues dissociation and alliance classification

## Correctness — PASS

The exact domain is the twenty-vertex bipartite Kneser graph \(H(5,2)\) with two labeled shores of ten pairs each. The degree-three condition makes a global offensive alliance exactly the complement of a dissociation set. The global cardinality bound \(|D|\leq12\) follows from the crossing-edge count \(2|D|\leq e(D,V\setminus D)\leq3(20-|D|)\). All five size-twelve examples follow directly from four-label complementary pairs. Uniqueness, the full face and facet polynomials, and the twelve natural-group orbits have separately specified exhaustive proofs implemented in independent direct-bitmask C++ and recursive Python codes. The Python code verifies the unique extension of each of the sixty valid size-eleven sets. All \(2^{20}\) masks are covered; no inference from finite testing to larger graph families is made.

## Originality — PASS subject to historical risk

The 2006 foundational source proves the generic cubic bounds, including the size-eight lower bound in this order, and characterizes equality in general terms; it does not give the exact number of extremizers, much less all \(844\) inclusion-minimal alliances or their twelve orbits. A 2010 dissociation-problem preprint and its 2011 journal version address computational complexity. The 2023 full-paper cubic dissociation enumerator bound compares arbitrary cubic graphs against unions of \(K_4\) and does not determine any specific Desargues coefficients. A previously indexed complete dissociation classification of the Petersen graph \(KG(5,2)\) concerns a nonisomorphic ten-vertex graph, not its twenty-vertex bipartite double cover. Searches using both alliances and dissociation terminology and the graph aliases revealed no equivalent or strictly stronger result. This is best-knowledge originality, not a guarantee that no unindexed exact table exists.

## Value — PASS

The result completes two natural incidence-graph invariants (all dissociation faces and inclusion-maximal facets) at a classical distance-transitive cubic graph. It explains a nonpure facet spectrum with a missing cardinality: the minimal global offensive alliance sizes jump from eight to ten, even though some nine-vertex alliances succeed. The five extremizers are geometrically rigid four-label lifts, and all sixty almost-extremal dissociation sets complete uniquely to one of them. The exact orbit breakdown makes the counts structurally interpretable and reproducible. This is a complete, motivated finite classification, not a general asymptotic theorem.

## Closest literature and residual limitations

- Rodríguez and Sigarreta, *Offensive alliances in cubic graphs*, first publicly available 2006-09-30, https://arxiv.org/abs/math/0610023 (general definitions, bounds and equality characterizations).
- Orlovich, Dolgui, Finke, Gordon and Werner, *The complexity of dissociation set problems in graphs*, 2010 preprint and 2011 article, https://doi.org/10.1016/j.dam.2011.04.023 (problem complexity, not the graph-specific census).
- Tu, Xiao and Lang, *Counting the number of dissociation sets in cubic graphs*, 2023, https://doi.org/10.3934/math.2023507 (universal coefficient/occupancy upper bounds, not the exact Desargues enumerator).
- Weisstein, *Desargues Graph*, https://mathworld.wolfram.com/DesarguesGraph.html (object and alternative graph models).

The finite exhaustive certificate depends on reproducible code and the stated graph labeling; no independent publication-priority search can be exhaustive. The supplied code was replayed successfully, but no independent scholarly audit has been performed.

Self-review: passed. Independent audit: not yet performed.

# Self-review

## Correctness — PASS

The same precise claim and graph labelling are used throughout. The two standalone Python verifiers independently construct all 20 graph edges, enumerate all 1024 subsets of cardinality at most five (finding no feasible set of cardinality below five), test all 462 candidate five-sets by their exact open/closed trace definitions, and build legal reconfiguration adjacencies using distinct representations. Every pairwise metric is determined by exhaustive BFS over the entire feasible state graph; both verifiers check every one of the 5995 locating-total endpoint pairs for each move type. The computed histograms and component sizes match. The intermediate state of the displayed two-slide witness is identifying and not locating-total. The result is finite and claims no infinite extrapolation. Full computational reproducibility follows from the included sources and output assertions.

## Originality — PASS (historical-priority qualified)

The strongest overlapping primary paper on Mycielskian identifying codes, Shaminejad–Vatandoost–Mirasheh (2022), proves an upper bound of five for this base but does not give the exact 191 minimum codes, the 110 minimum locating-total sets or any cross-property shortest-path count. Chakraborty et al. (2022) study general locating-total bounds in other stated graph classes; Mynhardt–Teshima (2017) give a reconfiguration framework and realizability constructions but not this particular exact comparison. Searches for alternative names (Grötzsch, Grotzsch, Mycielski of \(C_5\)), the two code notions, three-slide distance improvement and counting constants did not uncover a published exact equivalent in indexed mathematical records. Closest indexed findings concern the Pappus, dodecahedral or cycle graph and cannot logically imply these finite Grötzsch enumeration or distance histograms. This is best-knowledge originality, not a uniqueness certificate; unindexed historical work remains a risk.

## Value — PASS

The Grötzsch graph is the smallest triangle-free four-chromatic graph, a canonical Mycielskian test case, making it a motivated rather than arbitrary finite host. The two distinct, standard localization requirements both admit optimal five-sensor sets, and the strict optimum-set inclusion creates a natural controlled relaxation experiment: permitting identification without total domination during motion saves up to three *physical adjacent moves* without increasing the detector budget. The fully resolved 5995-pair histogram and symmetry classes show this is a robust finite phenomenon, not one opportunistically chosen pair or an isolated scalar recomputation. It provides an exact reproducible benchmark for comparing sensing specifications under restricted reconfiguration. It does not establish a general theorem, and none is asserted.

## Literature and limitations

* Shaminejad, Vatandoost and Mirasheh (2022), Theorem 2.4, https://toc.ui.ac.ir/article_26088_858b032cc710d026f084d95cbe679621.pdf — relevant upper bound; not the exact optimization or transition counts.
* Chakraborty et al. (2022), https://arxiv.org/abs/2211.14178 — the selected source with publicly verified posting date, the locating-total predicate and general structural context.
* Mynhardt and Teshima (2017), https://arxiv.org/abs/1707.02039 — earlier code reconfiguration model; no exact Grötzsch cross-code comparison.

Scope is restricted to the explicitly labelled 11-vertex graph. The evidence is transparent exhaustive computation with two independent code implementations, but independent external mathematical audit and complete historical priority verification are not claimed.

Self-review: passed. Independent audit: not yet performed.

# Scientific review of the five-rung ladder token-swap metric

## Correctness — PASS

The claim is a fixed finite classification with an exhaustive proof certificate, not an inference from sampling. Both self-contained implementations enumerate all \(10!=3{,}628{,}800\) states using BFS, agree on the full shortest-distance and lower-bound shortfall histograms, and identify the same four diameter endpoints and unique shortfall-eight endpoint. The mathematical deduction of state transitivity and of the matching of all-pair extremal shortfalls is explicit. The finite certificate was executed from its packaged files. Residual risk: hidden programming mistakes shared by both enumerators; independently external audit has not been performed.

## Originality — PASS, with priority risk

The closest primary comparison is Bansal–Günlük–Shapley (arXiv:2411.18581), whose full accessible HTML treats the **same ladder graph family** but optimizes synchronous parallel rounds and proves a \(2OPT+2\) approximation, not the exact sequential-swap metric. Aichholzer et al. (arXiv:2103.06707), Bonnet–Miltzow–Rzążewski (Algorithmica 2017), and Sadanandan–Chitturi (Algorithms 2022) establish graph-swap frameworks, bounds and sorting results for other graph classes. Related indexed exact results for the Petersen graph and other finite networks do not imply this ladder-specific census. Targeted exact-phrase, graph-alias, database and source checks found no covering statement. Residual risk: an unindexed older table, thesis or alternative Cayley-group notation may already contain these values.

## Value — PASS

The five-rung ladder is a natural ten-site rectangular nearest-neighbor architecture. Its complete \(10!\)-state metric is a reproducible exact benchmark for serial token-routing methods. A particularly informative difference emerges between two extremal objectives: four configurations are distance-\(21\) antipodes, whereas a different, uniquely determined state maximizes the failure of the standard transportation lower bound by eight swaps. This distinction is not a mere renaming or a cheap normalization check; the full state-space census is required to establish its uniqueness and maximality. It does not imply a general theorem for all ladder lengths.

Self-review: passed. Independent audit: not yet performed.

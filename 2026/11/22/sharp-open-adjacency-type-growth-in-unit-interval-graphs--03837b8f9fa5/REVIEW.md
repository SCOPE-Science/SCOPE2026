# Scientific review

## Correctness
PASS. Every unit interval graph admits a real-coordinate representation in which adjacency between distinct vertices is unit distance or less. A sweep of the \(2m\) endpoints of the windows centered on marked intervals yields at most \(2m\) distinct full patterns, and the only possible open-pattern exceptions arise by self-deletion at the \(m\) marked vertices. For sharpness, the explicit arithmetic progression of spacing \(3/4\) produces \(2m\) distinct full patterns and, at \(m\ge4\), \(m\) pairwise different absent-from-full-pattern open traces. Smaller parameters are checked directly. Independent adjacency-matrix computation supports the statements on a quarter-unit grid, and exact rational witnesses were checked through \(m=40\). Experiments do not establish the all-size statements by themselves; the explicit proof does.

## Originality
PASS on currently inspected evidence, with priority risk. Relevant search phrases included `open neighborhood trace unit interval proper interval 3m`, `unit interval graph neighborhood complexity sharp linear`, `proper interval adjacency types VC dimension`, and wider one-variable and interval graph formulations. Dreier et al. (arXiv:2607.10941) prove almost-linear behavior in a far larger class; Beaudou et al. (arXiv:2501.08895) discuss profile complexity and known asymptotic bounds for unit intervals; Rutter et al. (2025) establish the proper/unit representation equivalence. Published general-interval profile bounds are not sufficiently specialized to imply the open-trace coefficient three. Exact historical coverage cannot be guaranteed, especially for older locating-code variants.

## Value
PASS. Proper interval graphs form a canonical dense hereditary graph subclass and are equivalent to unit interval graphs. The result sharpens qualitative linear neighborhood complexity to its exact coefficient at every cardinality, identifies the minimum vertex budget for sharpness, and exhibits the strict VC-density distinction between proper and general interval graphs. The simultaneous open/closed result shows that the self-exclusion convention causes a real shift in VC dimension even though both growth rates are linear, making the precise coefficient and convention useful for one-variable type counts.

## Literature and limits
The nearest primary texts inspected were Dreier et al. (2026), Beaudou et al. (2025), and Rutter et al. (2025); the full 2026 arXiv text and the full 2025 HTML texts were read in relevant portions. The claim neither determines higher quantifier ranks nor asserts exclusive priority or a classification of all extremal representations. The exact earlier coefficient in the closed case follows from the standard monotone-neighborhood representation.

Self-review: passed. Independent audit: not yet performed.

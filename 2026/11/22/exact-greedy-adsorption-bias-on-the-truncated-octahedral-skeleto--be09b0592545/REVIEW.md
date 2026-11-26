# Independent mathematical audit

## correctness

PASS

A separate standard-library replay generated all signed coordinate permutations and squared-distance-two edges and verified a connected 24-vertex cubic graph with 36 edges. For a residual set S of size n, fixing the first vertex v leaves m vertices in S minus its closed neighborhood. Each order on those m vertices extends to exactly (n-1)!/m! orders of the remaining n-1 vertices, with the deleted neighbors blocked and irrelevant. Thus integer permutation counts for k+1 accepts are sums of the child counts for k accepts multiplied by that factor, with the empty graph contributing one empty order. The independent integer replay asserts each state's total is n! and visits 23,123 states; dividing at the root by 24! yields exactly the four frozen fractions at sizes 8,9,10,12 and zero elsewhere. Independent include/exclude enumeration counts an independent set just when its closed neighborhoods cover the graph, which is equivalent to inclusion maximality. Each independent set has exactly one branch path; all maximal ones are realizable by putting their vertices first. The verified histogram is 117,208,36,2 at the same sizes, total 363. The exact greedy-minus-uniform tail gaps at t=9,10,12 are 1498489579/7527168000, 12449256306871/43153254144000 and 593402617631/6164750592000. The t=11 gap equals t=12, these cover the nonconstant real thresholds by rounding up, and tails coincide outside 8<t<=12. The mean is 1161395055131/122594472000 and the exact maximum-packing amplification is 627368185631/33965568000>18. Replay: python3 /workspace/branches/9e706cee-cf49-4fb7-8565-711e369ac2ef/reproduce_truncated_octahedral_adsorption.py (optional --smoke for the eight-vertex slice); full output at /workspace/branches/9e706cee-cf49-4fb7-8565-711e369ac2ef/replay.log. The frozen checker was inspected, not executed. This is exact exhaustive counting for this graph, not a sampling experiment or proof for a graph family.

## originality

PASS

The nearest-neighbor exclusion process and the first-vertex decomposition are standard. Other exact finite studies, including distinct same-day indexed results, use analogous comparisons but different graphs. The distinct result is the complete exact terminal-size law, independent-set size histogram and strict stochastic comparison for this specific natural skeleton, not a new general adsorption algorithm.

## value

PASS

The truncated-octahedral skeleton is a canonical cubic, vertex-transitive finite contact network for a space-filling solid. On this specific graph the full distribution is useful for benchmarking greedy sampling and packing: size 11 never occurs, only two maximal sets are maximum, and the more-than-18-fold comparison and strict tails quantify a large inequivalence between dynamic and uniform sampling over the same maximal states. The finite exact law is not inferred from an independence number or an asymptotic mean and does not claim the bias is universal.

The dated certificate retains the supplied scientific assessment, sources and limitations.

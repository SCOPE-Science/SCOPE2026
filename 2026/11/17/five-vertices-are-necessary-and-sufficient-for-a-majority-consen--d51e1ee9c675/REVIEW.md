# Mathematical assessment

## Correctness

PASS. For each graph of order at most five, the adjacency-bit encoding enumerates every simple labelled graph. Checking connectivity before and after each possible edge deletion exhausts exactly the eligible pairs. The consensus basin is the reverse-reachable set of the two absorbing unanimous words. Two independently implemented complete enumerations give the same \(240\) positive labelled pairs and the same two marked-isomorphism types (each with \(120\) labelled realizations). Explicit forward trajectories witness both lost and newly gained basin members in each type. The statement is carefully limited to the minimum order and its types.

## Originality

PASS, with residual historical-priority uncertainty. Mustafa and Pekeč (2000) already showed nonmonotonicity of the *initial-majority correctness* property under graph changes, but did not establish the simultaneous gain of the unconditional consensus basin and loss of its old members, or a five-vertex minimum. Benjamini et al. (2014) and Fountoulakis et al. (2020) study eventual periods and random-graph unanimity rather than such exact edge perturbations. A published one-edge \(K_{a,b}\) census has disjoint graph-family hypotheses: both present witnesses contain triangles. The earlier Heawood two-edge result does not imply this one-edge minimality. Searches did not identify equivalent sharp classifications; this is evidence, not a guarantee of absolute historical priority.

## Value

PASS. The graph-order threshold is a natural, sharp dynamical robustness invariant: the first size at which an edge deletion simultaneously improves global consensus likelihood under uniform initial bits and destroys consensus for specific starting profiles. Both exceptional graph types and exact lost/gained populations are classified. The result separates aggregate success from statewise resilience on the smallest networks capable of exhibiting the paradox.

## Limits

The result addresses connected graphs before and after a single edge deletion, tie-retaining synchronous majority and only the sharp minimum order; it does not classify larger networks. The finite checkers are provided for reproducibility but have not been independently externally audited.

Self-review: passed. Independent audit: not yet performed.

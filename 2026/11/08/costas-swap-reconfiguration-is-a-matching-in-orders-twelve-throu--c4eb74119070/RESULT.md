# Costas-swap reconfiguration is a matching in orders twelve through fourteen

## Finding

For each \(n\in\{12,13,14\}\), form the graph whose vertices are all order-\(n\) Costas permutations and whose edges are transpositions of two entries that keep the Costas property. Its complete connected-component decomposition is
\[
\begin{array}{c|r|r|l}
 n & \text{vertices} & \text{edges} &\text{components}\\ \hline
 12&7852&136&7580K_1\sqcup136K_2\\
 13&12828&88&12652K_1\sqcup88K_2\\
 14&17252&120&17012K_1\sqcup120K_2
\end{array}.
\]
Thus every valid Costas permutation has **at most one** valid two-position swap. A reconfiguration procedure required to remain within the set of Costas permutations cannot reach any third state from its initial state using these moves. There is a sharp contrast at order eleven, where eight permutations have two legal swaps.

The numbers of unordered edges at each positional gap \(h\), for \(1\le h<n\), are:

| Order | Edge counts in increasing positional gap |
|---|---|
| \(12\) | 8, 16, 4, 0, 20, 40, 8, 8, 20, 8, 4 |
| \(13\) | 12, 16, 8, 4, 12, 4, 8, 0, 0, 8, 8, 8 |
| \(14\) | 12, 0, 20, 0, 0, 8, 8, 0, 12, 12, 32, 12, 4 |

The aggregate edge counts at these orders are previously published; the component-degree theorem and positional-gap distributions are the findings here.

## Assumptions and scope

A permutation \(p=(p(0),\ldots,p(n-1))\) is a bijection from \(\{0,\ldots,n-1\}\) to itself. The Costas condition is
\[
\forall h\in\{1,\ldots,n-1\},\quad
\bigl(p(i+h)-p(i)\bigr)_{i=0}^{n-h-1}
\quad\text{has pairwise distinct entries}.
\]
Two *different* valid permutations are adjacent only when they differ by exactly one transposition of their entries at positions \(i<j\); their positional gap is \(j-i\). Vertices are labelled by their exact one-line permutations; dihedral symmetries are not quotiented. The theorem applies only to orders 12, 13 and 14 and to a move that changes exactly two entries, not to moves through invalid intermediate arrays or simultaneous multi-entry trades.

## Proof

The finite classification follows from complete enumeration with a correctness-preserving pruning invariant, independently checked through a second search.

**First exhaustive enumeration.** Construct length-\(k\) prefixes from left to right, each using distinct values. For each distance \(h\in\{1,\ldots,k-1\}\), maintain the set of already observed forward differences \(p(i+h)-p(i)\) among the prefix. Appending a new value \(x\) at position \(k\) creates exactly one new difference \(x-p(k-h)\) at each gap \(h\in\{1,\ldots,k\}\). Reject the append iff any such value already appears at its corresponding gap. Every prefix of a valid full Costas permutation passes these tests. Conversely every completed permutation accepted by this recurrence has no repeated differences, and is therefore Costas. Exploring every unused value at each step proves the enumeration is exhaustive, not sampled.

Encode a complete permutation by its entries in distinct four-bit blocks (possible for these orders). For every complete permutation \(p\) and every \(i<j\), exchange the blocks at positions \(i,j\) and look up the resulting permutation in the complete set. Each undirected edge is counted exactly once by keeping only the destination with a larger enumeration index; increment the degrees of both endpoints and the positional-gap counter \(j-i\). This yields the vertex count, edge count, degree sequence and gap histogram in the table. In each target order, all degrees are zero or one, which alone proves the asserted graph is a disjoint union of isolated vertices and edges.

**Independent exhaustive cross-check.** A separate recursive search builds from right to left, storing displacement differences in integer bitmasks instead of boolean arrays. Upon reaching a complete Costas permutation, it tries every pair of indices, modifies the array, and *retests the whole Costas condition directly* by scanning differences at all gaps. This procedure accumulates directed degrees and directed gap totals (twice their undirected counts); it does not use the hash table or the partial-prefix test to classify a swap. The two implementations agree on every integer in the statement.

The order-eleven comparison is also exhaustively checked by both programs: \(4368\) states, \(140\) edges and vertex degrees \(4096\) at zero, \(264\) at one and \(8\) at two. It is only a local boundary comparison, not a claim about all larger orders.

## Verification

Two complete C++17 checker source files are attached: `verify_forward.cpp` and `verify_reverse.cpp`. Compile independently using `g++ -O2 -std=c++17` and run the first with arguments `11 12 13 14`; run the second without arguments. Both have hard-coded assertion checks for every target vertex/edge count and each entire positional-gap histogram, while the forward checker asserts the exact degree histograms and the reverse checker independently checks the degree bound. Successful execution exits with code zero and prints its census.

The complete searches examine the full space of valid Costas permutations, not all raw permutations by brute force; the prefix pruning proof establishes that no valid permutation is omitted. The independent reverse search validates the pruning and all swap tests. Both checkers were compiled and executed successfully on the stated orders.

## Relationship to prior work

Drakakis, Healy and Rickard (2008, Section 3.2 and Table 2) already report the exact numbers of **pairs at Hamming distance two** as \(136,88,120\) for orders 12, 13 and 14. Those totals, and previously known numbers of Costas arrays, are explicitly *not* claimed as new. An aggregate number of pairs does **not** imply their degree distribution: edges can share vertices. The present classification resolves whether any Costas array can be connected by two consecutive valid transpositions, and gives the additional exact gap refinement relevant for constrained switching heuristics.

Ardalani and Pott (2023) study an index-multiplication transformation \(g(i)=f(ki\bmod(n+1))\), where the modular map permutes many positions; this is not an unrestricted transposition of two entries and does not determine our graph. Drakakis and Rickard (2007) provide a dated public treatment of Costas definitions, and Drakakis (2011) surveys broader questions. An exact-match or stronger earlier result could remain in unindexed work.

## Limitations

This is a finite, reproducible classification for three specified orders, not a theorem for all \(n\ge12\). The graph permits only legal Costas-to-Costas transpositions, not intermediate violations; it does not bound the efficiency of broader stochastic searches that traverse invalid permutations. The published edge totals provide an external consistency check but not an independent proof of the new degree and location data. The result has undergone only self-review, not independent scholarly audit.

## References

1. K. Drakakis, J. Healy, S. Rickard, *A stochastic analysis approach in the search for Costas arrays* (manuscript dated 15 April 2008; publicly indexed in May 2008), Section 3.2, Table 2. https://www.researchgate.net/publication/228340808_A_stochastic_analysis_approach_in_the_search_for_Costas_arrays
2. K. Drakakis and S. Rickard, *On the generalization of the Costas property in the continuum*, arXiv:0706.1379, first posted 10 June 2007. https://arxiv.org/abs/0706.1379
3. K. Drakakis, *Open problems in Costas arrays*, arXiv:1102.5727, first posted 28 February 2011. https://arxiv.org/abs/1102.5727
4. S. Ardalani and A. Pott, *A New Transformation for Costas Arrays*, IEICE Transactions on Fundamentals E106-A (2023), definition of modular index transformation. https://www.jstage.jst.go.jp/article/transfun/E106.A/12/E106.A_2023SDP0005/_pdf

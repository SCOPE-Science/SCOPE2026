# The sharp switch metric and two antipodes of five-by-five binary two-factor tables

## Finding
Let \(\mathcal B_5\) be the set of zero-one \(5\times5\) matrices with precisely two ones in every row and column. The graph \(\mathcal S_5\) connects two such matrices when one switch replaces a block
\[
\begin{pmatrix}1&0\\0&1\end{pmatrix}
\quad\longleftrightarrow\quad
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Then \(\mathcal S_5\) is connected, with radius \(5\) and **sharp diameter \(6\)**. Its configurations have precisely two possible support structures: one alternating bipartite ten-cycle (\(1440\) configurations), or a disjoint four-cycle plus six-cycle (\(600\) configurations). The complete distance profiles, counting the base vertex itself at distance zero, are:

| Support structure | Number of states | Distance-shell profile for distances \(0,\ldots,6\) | Eccentricity |
| --- | ---: | --- | ---: |
| \(C_{10}\) | \(1440\) | \((1,25,230,810,831,141,2)\) | \(6\) |
| \(C_4\sqcup C_6\) | \(600\) | \((1,27,242,840,810,120,0)\) | \(5\) |

Each ten-cycle state has **exactly two antipodes**, both ten-cycle states. To state them explicitly, choose cyclic orderings \(r_0,\ldots,r_4\) of the rows and \(c_0,\ldots,c_4\) of the columns so that row \(r_i\) has its ones in columns \(c_i,c_{i+1}\), with all indices modulo \(5\). The two matrices at distance six are exactly the configurations in which row \(r_i\) has ones in columns \(c_{i+2},c_{i+3}\), or in columns \(c_{i+3},c_{i+4}\), respectively. Any reversal of the cyclic presentation permutes this two-element set rather than changing the conclusion.

The unordered distance-pair distribution at distances \(1,\ldots,6\) is
\[
(26100,238200,835200,841320,137520,1440).
\]
Hence there are exactly \(1440\) unordered diametral pairs. The exact state and edge counts, although reproduced below, are background data rather than the claimed novelty.

## Assumptions and scope
Rows and columns are individually labelled and are **not** identified under isomorphism in the graph being measured. A state has ten occupied cells; diagonal entries are allowed. A move changes exactly two ones and two zeros in distinct rows and distinct columns; no other move, including any longer alternating-cycle flip, is permitted. Distance is the shortest number of these switches. In a support graph, the two vertex classes each contain five labelled vertices; each vertex has degree two. Its possible connected components are bipartite even cycles of length at least four, so the only partitions of its ten vertices are \(C_{10}\) and \(C_4\sqcup C_6\). The entire theorem is specific to order five and makes no claim about arbitrary matrix orders.

## Proof
**1. All configurations and the two symmetry orbits.** Encode a row by a five-bit mask of Hamming weight two. There are \(\binom52=10\) allowed row masks, hence precisely \(10^5\) ordered row candidates. Retain a candidate if and only if the five computed column sums all equal two. The resulting complete list has \(2040\) distinct matrices. This number can also be checked without machine search: the number of Hamiltonian ten-cycles in the labelled complete bipartite graph \(K_{5,5}\) is \(5!4!/2=1440\), and choosing the two rows and two columns of a four-cycle, then choosing a spanning six-cycle on the complementary three-plus-three vertices, gives \(\binom52^2(3!2!/2)=600\) further configurations. The two support types exhaust the set. The group \(S_5\times S_5\) of row and column relabellings is transitive on each of these two types and preserves all legal switches. Thus two representative distance searches characterize all vertices.

**2. Exact adjacency and distance certification.** For every retained row-mask vector, examine all \(\binom52^2=100\) choices of two rows and two columns. A neighbor exists precisely when the four bits form one of the two checkerboards; XOR the corresponding two column bits in both rows and look up the resulting state in the complete list. This completely generates the finite simple graph, with no omitted move or duplicated edge. The Python verifier generates the \(2040\) row vectors independently of this proof exposition, constructs the \(26100\) undirected edges, checks edge reversibility, then performs breadth-first searches from **each of the \(2040\) states**. Since breadth-first search first discovers a vertex at its minimum path length, its computed distances are exact and exhaustive. It asserts the two complete shell vectors displayed above for every vertex of the appropriate support type, and independently sums the unordered pair histogram. In particular, all vertices are reached, proving connectedness, and the largest distance is six.

**3. Independent construction and symmetry check.** A second verifier written in C++17 obtains the matrices by taking unions of two edge-disjoint permutation matchings. It considers all \(5!\) first permutations and all \(5!\) second permutations, retains disjoint pairs, and deduplicates the resulting row-mask encodings; it independently obtains \(2040\) states. It reconstructs every edge by its own nested loop over row and column pairs, then performs breadth-first searches from the two fixed support-type representatives below. Their profile vectors are exactly
\[
(1,25,230,810,831,141,2)\quad\text{and}\quad
(1,27,242,840,810,120),
\]
with the final zero suppressed from the second vector. Transitivity from Step 1 turns these two complete finite calculations into a second verification of *all* eccentricities and the sharp diameter, without assuming the Python all-pairs implementation is correct.

**4. Antipode classification and exact witness.** Encode five rows as decimal bit masks, with bit zero representing the first column. Take the canonical ten-cycle state \((3,6,12,24,17)\); its two antipodes are precisely \((12,24,17,3,6)\) and \((24,17,3,6,12)\). The independently generated breadth-first distance array for that representative contains exactly two entries at distance six, and the second verifier asserts these entries are exactly the displayed shifted states. Transporting these identities by the row-and-column permutation action establishes the general cyclic antipode description. A concrete legal six-switch path, represented as successive vectors of five decimal row masks, is:

```
(3, 6, 12, 24, 17)
(3, 3, 12, 24, 20)
(10, 3, 12, 17, 20)
(10, 3, 24, 5, 20)
(12, 3, 24, 3, 20)
(12, 10, 17, 3, 20)
(12, 24, 17, 3, 6)
```

Every adjacent pair in this sequence differs by exactly one checkerboard switch; the complete breadth-first distance arrays rule out any path of length at most five. Each of the \(1440\) ten-cycle states has two distance-six neighbors, and none of the other \(600\) states has one, so the unordered number of diametral pairs is \(1440\cdot2/2=1440\). Adding the shell counts from all states and dividing by two gives the displayed entire unordered pair histogram, whose entries sum to \(\binom{2040}{2}=2079780\).

## Verification
The embedded standalone files `verify_switch_5x5.py` and `verify_switch_5x5.cpp` are executable source code containing all enumeration and shortest-path machinery; neither requires a previously generated database, result log, or another-row artifact. Run:

```
python3 verify_switch_5x5.py
g++ -std=c++17 -O2 -Wall -Wextra verify_switch_5x5.cpp -o verify_switch_5x5
./verify_switch_5x5
```

The Python checker independently enumerates all states by row masks, checks each column margin, constructs all legal switches, performs all-source BFS, verifies all type-dependent shells and all pair counts. The C++ checker independently enumerates unions of disjoint perfect matchings, builds the graph, checks the two canonical orbit BFS profiles, and verifies the two explicit antipodes. Both completed with their PASS assertions satisfied. Separate small enumerations found only self-centered switch graphs at orders three and four: all \(6\) states have eccentricity two at order three, and all \(90\) states have eccentricity four at order four. Thus order five is the first order in this series exhibiting a distinction in eccentricity between bipartite cycle types.

## Relationship to prior work
The swap operation, its general connectivity in bipartite degree-sequence realizations, and broad formulae and bounds for shortest switch sequences are established mathematics. Erdős–Király–Miklós, *On the swap-distances of different realizations of a graphical degree sequence* (arXiv:1205.2842, v1 May 13, 2012), Section 4, proves a general pairwise formula using maximum alternating-cycle decompositions and Theorem 4.1 gives an all-pairs upper bound. Applied with five vertices on each side and all degrees two, that bound is eight, not the sharp six, and the article supplies neither the two support-type distance profiles nor the unique two-antipode description. Will's earlier *Switching Distance Between Graphs with the Same Degrees* (1999) establishes the general symmetric-circuit formula and complexity landscape, not a documented \(5\times5\) metric census. Miklós–Erdős–Soukup (2013) studies the uniform switch chain and polynomial mixing for half-regular bipartite degree sequences rather than these exact distances.

An earlier all-order study of degree-two bipartite switch chains determines the **cycle-type transition kernel and multiplicities**. Those structural counts, switch rates, and orbit descriptions are not claimed here; indeed its cycle-type quotient loses the individual-state distances needed for the present result. The new content is the exact order-five metric, its two distinct eccentricity strata, complete shells, and precisely characterized two-antipode geometry. The previously known order-five total and degrees are reused only to state and check the metric. Matching terminology in general swap-distance formulae is not treated as proof of novelty: the literature comparison concerns whether their conclusions actually specify the sharp numerical metric and the complete antipode classification.

## Limitations
This is a complete **finite** classification, not an all-order diameter theorem; the exhaustive exact calculations are part of its proof. The two independently organized verifiers both use exact integer enumeration and BFS, rather than formal external verification. An equivalent published or unpublished finite census not located by the targeted literature searches could exist. Only an independently implemented check and not an independent scholarly audit is reported. The 1999 original paper was accessible as an abstract but not as full text, and absolute historical priority is not certified. No conclusions about Markov-chain mixing times or weighted switch costs follow from this metric alone.

## References
1. P. L. Erdős, Z. Király, I. Miklós, *On the swap-distances of different realizations of a graphical degree sequence*, first posted 2012-05-13, arXiv:1205.2842; Sections 2 and 4, Theorem 4.1. https://arxiv.org/abs/1205.2842 ; https://arxiv.org/pdf/1205.2842
2. T. G. Will, *Switching Distance Between Graphs with the Same Degrees*, SIAM Journal on Discrete Mathematics 12(3) (1999), 298–306, DOI:10.1137/S0895480197331156. https://doi.org/10.1137/S0895480197331156
3. I. Miklós, P. L. Erdős, L. Soukup, *Towards Random Uniform Sampling of Bipartite Graphs with given Degree Sequence*, Electronic Journal of Combinatorics 20(1) (2013), P16, DOI:10.37236/3028. https://doi.org/10.37236/3028

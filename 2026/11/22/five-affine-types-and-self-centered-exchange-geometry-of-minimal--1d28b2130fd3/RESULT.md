# Five affine types and self-centered exchange geometry of minimal connected domination in the Paley thirteen-graph

## Finding
Let \(G=P_{13}\) be the Paley graph of order thirteen, described below. A connected dominating set is a vertex set inducing a connected subgraph and having each outside vertex adjacent to a selected vertex. All inclusion-minimal connected dominating sets of \(G\) have cardinality four, and precisely 260 exist; thus \(\gamma_c(G)=4\) and the minimal-connected-domination polynomial is \(260z^4\).

Make an exchange graph \(\mathcal X\) on those 260 sets: two distinct four-sets are adjacent when one vertex is deleted and one other vertex inserted. It has 1,911 edges and is connected, with \(\operatorname{rad}(\mathcal X)=\operatorname{diam}(\mathcal X)=4\). Its five quadratic-affine orbits, representatives shown as hexadecimal vertex-incidence masks, are:

| Representative | Orbit size | Degree | Distances zero through four |
|---|---:|---:|---|
| `0x17` | 78 | 14 | \((1,14,79,115,51)\) |
| `0x1b` | 39 | 20 | \((1,20,70,116,53)\) |
| `0x2b` | 78 | 14 | \((1,14,70,132,43)\) |
| `0x2d` | 39 | 12 | \((1,12,74,128,45)\) |
| `0x8d` | 26 | 15 | \((1,15,69,133,42)\) |

All distance vectors sum to 260, and their last entries are positive. The weighted degree identity \((78\cdot14+39\cdot20+78\cdot14+39\cdot12+26\cdot15)/2=1911\) is an independent consistency relation. Although \(\mathcal X\) is not regular, every optimum has eccentricity four.

## Assumptions and scope
This is an exact finite graph claim, not an assertion for other Paley graph orders. Label the vertex set by \(\mathbb Z/13\mathbb Z\). Two distinct labels \(i,j\) are adjacent if and only if \(i-j\) belongs modulo thirteen to the nonzero quadratic-residue set \(Q=\{1,3,4,9,10,12\}\). A mask \(s\in\{1,\ldots,8191\}\) encodes vertices having their corresponding bit set. A dominating set \(S\) satisfies \(S\cup N(S)=V(G)\). A connected dominating set is *inclusion-minimal* if deleting any one member destroys that property; because a connected dominating set dominates every vertex, connected domination is upward-closed under vertex addition, so this deletion criterion is equivalent to full inclusion minimality. The exchange graph is at fixed size four and does not restrict the moved vertex to an original graph edge.

## Proof
A reproducible finite exhaustive certificate suffices for this fixed thirteen-vertex statement. First generate the symmetric adjacency graph from the six residues, or equivalently by Euler's quadratic-residue test. For every nonempty bitmask, test domination by OR-ing selected closed neighborhoods and test connectedness within the selected induced graph. The Python checker uses exact flood-fill on bitmasks; the independently implemented C++ checker uses modular exponentiation and a disjoint-set connectivity test. These independent constructions both determine the entire feasible list, containing exactly the following numbers at selected sizes four through thirteen: \((260,975,1625,1703,1287,715,286,78,13,1)\). None exists at size at most three.

Among the feasible masks, retain precisely those for which deleting each individual selected vertex makes the set infeasible. Every such set has four elements, and their number is 260. This exhausts all candidate masks and proves both minimum cardinality and inclusion-minimality; no sampling or inference from a bounded range of graph orders occurs.

For each pair of the 260 minimal sets, put an edge precisely when their XOR has two set bits. Directly enumerating every unordered pair gives 1,911 such edges. A breadth-first search from *each* of the 260 exchange vertices visits all 260 and attains maximum distance exactly four; hence connectivity and equal radius and diameter follow. The finite group of all 78 maps \(i\mapsto ai+b\), where \(a\in Q\) and \(b\in\mathbb Z/13\mathbb Z\), acts by graph automorphisms. Enumerating each group's image of every minimal set yields exactly five disjoint orbits, with the sizes and representatives in the table. For every set in each orbit, the checkers compare its exchange degree and full five-entry shortest-distance vector to the representative's. The displayed degrees and vectors are thereby exhaustive, rather than being extrapolated from a few representatives.

Every loop is visibly finite: all masks range from one to 8,191; every minimal-mask pair is considered for exchanges; every source in the 260-state exchange graph is used for breadth-first search. Both provided source programs assert and print the exact independent calculations.

## Verification
Run `python3 verify_exact.py` and `c++ -std=c++17 -O2 verify_independent.cpp -o verify_independent && ./verify_independent`. Each uses only its respective language standard library. The package includes their exact reference stdout files `verify_exact_output.txt` and `verify_independent_output.txt`; successful replay ends in `CHECKS_PASS`. One checker builds adjacency from a literal residue set and bitmask flood-fill; the other uses Euler's criterion and union-find. Both test the entire mask universe, all exchange edges, all-source shortest paths, and all affine orbit members. This is independent implementation of finite algorithms, not independent scholarly review.

## Relationship to prior work
Elsawy, *Paley Graphs and Their Generalizations* (public preprint 2012), develops the finite-field Paley-graph setting and its combinatorial properties. Golovach, Heggernes and Kratsch, *Enumerating Minimal Connected Dominating Sets in Graphs of Bounded Chordality* (2015), treats algorithmic enumeration of minimal connected dominating sets. The former supplies a canonical graph family and the latter the intrinsic extremal invariant. Neither inspected document gives the exact Paley-thirteen inclusion-minimal census together with its optimal-exchange metric and affine orbit shells. Published work on the Paley-thirteen neighborhood/dominance complexes studies different simplicial complexes rather than this solution-exchange graph. A four-cube connected-domination exchange classification covers a different graph, so it cannot imply these specific counts. The result does not claim a new definition of the Paley graph or of connected domination.

## Limitations
The result is an exact computationally reproducible finite theorem for one natural named graph, not an infinite-family classification. The programs are self-contained exhaustive certificates but their execution and mutual agreement are not a substitute for independent mathematical peer review. Historical priority remains provisional because inaccessible and unindexed papers or tables may contain an equivalent enumeration. No physical-network performance guarantee follows from these purely combinatorial data.

## References
1. A. N. Elsawy, *Paley Graphs and Their Generalizations*, arXiv:1203.1818, first posted 2012-03-07. https://arxiv.org/abs/1203.1818
2. P. A. Golovach, P. Heggernes, and S. Kratsch, *Enumerating Minimal Connected Dominating Sets in Graphs of Bounded Chordality*, LIPIcs IPEC 2015, 307–318, DOI:10.4230/LIPIcs.IPEC.2015.307. https://doi.org/10.4230/LIPIcs.IPEC.2015.307

# Frozen and mobile fault-tolerant metric bases in two strongly regular graphs

## Finding
Let \(S\) be the Shrikhande graph and \(R=K_4\square K_4\) the four-by-four rook graph. Although both are strongly regular with parameters \((16,6,2,2)\), their optimal one-failure-tolerant distance-landmark configurations have different mobility.

Both graphs have fault-tolerant metric dimension \(6\). On the labeled sixteen-vertex graphs, \(S\) has precisely \(448\) minimum fault-tolerant resolving sets (bases), whereas \(R\) has precisely \(1600\).

For each graph form the exchange graph on its minimum bases, joining distinct six-sets when one selected vertex is replaced by one previously unselected vertex. The Shrikhande exchange graph consists of \(448\) isolated vertices. The rook exchange graph is connected, with \(12{,}816\) edges, radius \(6\), diameter \(6\), and every base having eccentricity \(6\).

If a move on Shrikhande bases instead replaces **exactly two** selected vertices with two previously unselected vertices, the resulting \(448\)-vertex graph is connected, \(45\)-regular, has \(10{,}080\) edges, and has radius and diameter \(3\). Thus the minimum simultaneous replacement budget that permits passage between all optimal bases is \(2\) for \(S\) and \(1\) for \(R\).

The full unordered distinct-pair distance multiplicities for the rook one-exchange graph are
\[
(d,m_d)=(1,12816),(2,102096),(3,357744),(4,521376),(5,244944),(6,40224).
\]
For the Shrikhande exactly-two-exchange graph these are
\[
(d,m_d)=(1,10080),(2,70560),(3,19488).
\]
Under their natural automorphism groups (of orders \(192\) and \(1152\), respectively), Shrikhande bases form nine orbits of sizes \(16,16,32,32,48,48,64,96,96\), and rook bases form seven orbits of sizes \(16,96,144,192,288,288,576\).

## Assumptions and scope
Graphs are simple and undirected, and graph distance is the shortest-path distance. Label the common vertex set by \(V=(\mathbb Z/4\mathbb Z)^2\), encoding \((i,j)\) by \(4i+j\). In \(R\), two distinct vertices are adjacent if they agree in a coordinate. In \(S\), two vertices are adjacent if their difference lies in
\[
\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}\pmod4.
\]
Both have diameter two, degree six, and exactly two common neighbors for each distinct vertex pair.

A set \(B\subseteq V\) is *fault-tolerant resolving* if, after deleting any one landmark from \(B\), every two graph vertices still have different distance vectors to the surviving landmarks. Equivalently, for every unordered pair \(\{u,v\}\subset V\), there are **at least two distinct** \(w\in B\) satisfying \(d(w,u)\ne d(w,v)\). A *minimum base* minimizes \(|B|\); no landmarks are ordered or repeated. The exchange relation of order \(r\) means \(|B\setminus C|=|C\setminus B|=r\). This is not token sliding along underlying graph edges and no intermediate sets of size other than six are permitted.

## Proof
The following exhaustive finite certificate proves the complete result for the two specified labeled sixteen-vertex graphs. Every step uses exact integer distances, bit operations, and explicit finite loops, with no numerical tolerance or sampling.

**Step 1: graph construction.** Construct both labeled adjacency matrices from the rules above. Independently obtain graph distances by breadth-first search (Python verifier) or by the exactly specified zero/one/two distance formula (C++ verifier). The six neighbors per vertex and two common neighbors per distinct pair are checked for every vertex and pair, respectively; both graph diameters are two.

**Step 2: the two-witness criterion.** For every unordered distinct vertex pair \(\{u,v\}\) (there are \(\binom{16}{2}=120\)), compute its full distinguishing-vertex mask
\[
W_{uv}=\{w\in V:d(w,u)\ne d(w,v)\}.
\]
The condition is exactly \(|B\cap W_{uv}|\ge2\) for all \(120\) pairs. Both implementations test all \(\binom{16}{5}=4368\) five-subsets and establish that none satisfy it. Monotonicity (adding landmarks cannot eliminate a distinguishing witness) excludes all sets with fewer than five vertices. They then test all \(\binom{16}{6}=8008\) six-subsets, obtaining \(448\) Shrikhande bases and \(1600\) rook bases. The C++ implementation instead explicitly deletes each selected landmark and retests ordinary distance-vector resolution; this is logically equivalent but computationally independent of the two-witness mask test. This proves minimum size six and both counts.

**Step 3: exact exchange graphs.** Map each accepted six-set to its sixteen-bit integer mask. The Python verifier enumerates all combinations of \(r\) deletions and \(r\) additions, checking membership in the accepted-base set. The C++ verifier independently examines all unordered pairs of accepted masks and inserts an edge precisely when their symmetric difference contains \(2r\) vertices. For \(r=1\), both certify that the Shrikhande graph has no edges and the rook graph has \(12{,}816\) edges and one component. For \(r=2\), both certify that the Shrikhande graph has \(10{,}080\) edges, each of its \(448\) vertices has degree \(45\), and it is connected. Consequently the minimum connecting batch sizes are exactly two and one, respectively.

**Step 4: all-pairs metric and symmetry.** Both programs run unweighted breadth-first search from **every accepted base** in the connected exchange graphs, determine each eccentricity and count only unordered pairs, producing precisely the distance distributions stated above. The pair counts sum to \(\binom{448}{2}=100128\) and \(\binom{1600}{2}=1279200\), excluding any unreachable pair. The Python program independently builds \(192\) translations/linear stabilizers preserving the Shrikhande Cayley generator set, and \(1152\) independent row/column permutations and coordinate swaps for rook; applying these concrete automorphisms yields the asserted orbit partitions. Each orbit member is verified to remain a valid base.

Since all possible relevant subsets, exchanges, and pairwise distances are enumerated with stated finite domains, the programs constitute exhaustive certificates of the claimed finite statements, not empirical extrapolations.

## Verification
With Python 3 standard library and a C++17 compiler, save all accompanying files together and execute:

```sh
python3 verify_pair_masks.py
c++ -std=c++17 -O2 -Wall -Wextra verify_direct.cpp -o verify_direct
./verify_direct
```

The expected exact outputs are supplied as `VERIFY_PYTHON_OUTPUT.txt` and `VERIFY_DIRECT_OUTPUT.txt`. Each program contains assertions for the essential counts, connectivity and metric profiles. The Python program also validates the symmetry orbit decompositions. No external data files or libraries are needed.

## Relationship to prior work
Hernando, Mora, Slater and Wood introduced fault-tolerant resolving sets and investigated trees and general bounds; their published text does not classify either of the graphs here or optimal-base exchanges. Estrada-Moreno, Rodríguez-Velázquez and Yero introduced the general \(k\)-metric generator, whose \(k=2\) instance agrees precisely with the present one-erasure model; their inspected text does not give these two bases' censuses or reconfiguration metrics. Bailey's archived 2013 classification gives **ordinary** metric dimension \(4\) for both \(H(2,4)\) and the Shrikhande graph, but ordinary resolution only requires one witness and does not imply the new two-witness counts or movement graphs.

Published classifications of identifying codes, global locating-dominating codes, independent sets and induced matchings on these same two strongly regular graphs study different admissible families. Their exchange connectivity patterns do not imply the present metric-base exchange edges; the admissible six-subsets here are defined by all \(120\) pairwise distance-separation constraints. Likewise, weak two-metric notions based on sums of absolute distance differences are not identical to requiring two different landmarks to distinguish each pair.

## Limitations
This is a complete exact result only for the two displayed labeled sixteen-vertex graphs; it is not a formula for all strongly regular graphs, arbitrary Hamming graphs or arbitrary fault-tolerant resolving sets. The finite verification is exhaustive but is not an independent scholarly audit. Relevant indexed and published texts were compared by statements and implications; inaccessible or unindexed historical work could still establish priority overlap. The precise 2013-12-17 archival date identifies the dated Bailey source, not the first creation of metric dimension as a concept.

## References
1. C. Hernando, M. Mora, P. J. Slater and D. R. Wood, *Fault-Tolerant Metric Dimension of Graphs* (2008). Author-hosted full text: https://users.monash.edu/~davidwo/papers/HMSW-FaultTolerant.pdf
2. R. F. Bailey, *The metric dimension of small distance-regular and strongly regular graphs*, first arXiv version December 17, 2013, https://arxiv.org/abs/1312.4973 ; author-hosted full text: https://www.math.mun.ca/rbailey00/papers/small.pdf
3. A. Estrada-Moreno, J. A. Rodríguez-Velázquez and I. G. Yero, *The k-metric dimension of a graph*, arXiv first version December 24, 2013, https://arxiv.org/abs/1312.6840
4. A. Estrada-Moreno, I. G. Yero and J. A. Rodríguez-Velázquez, *The k-metric dimension of graphs: a general approach*, first arXiv version May 21, 2016, https://arxiv.org/abs/1605.06709

# Sharp square-flip distances and diametral geometry of four-cube domino tilings

## Finding
Let \(Q_4\) be the graph on \(\{0,1\}^{4}\), joining binary vectors that differ in exactly one coordinate. A domino tiling of the corresponding \(2\times2\times2\times2\) box is a perfect matching of \(Q_4\). Join two tilings when their symmetric difference is the four edges of one coordinate square: equivalently, exchange two parallel dominoes within a \(2\times2\) square.

The previously recorded square-flip component decomposition has one mobile component \(H\) with \(264\) tilings and eight isolated tilings. The **new exact metric classification** is

\[
\operatorname{rad}(H)=7,\qquad \operatorname{diam}(H)=8.
\]

Exactly \(252\) mobile tilings have eccentricity \(7\), and the remaining \(12\) have eccentricity \(8\). The latter are **precisely** the mobile tilings admitting four legal square flips. All \(12\) lie in one orbit of the natural hyperoctahedral cube symmetry group. Form an auxiliary graph on these \(12\) tilings, joining two when their shortest square-flip distance is \(8\). This graph is the disjoint union of three four-cycles, \(3C_4\); the \(12\) unordered diametral pairs constitute one cube-symmetry orbit.

The numbers of unordered pairs of mobile tilings at exact minimum flip distances \(1,2,3,4,5,6,7,8\) are respectively

\[
(768,\ 2640,\ 6032,\ 9360,\ 9504,\ 5296,\ 1104,\ 12).
\]

They sum to \(\binom{264}{2}=34716\). Thus eight elementary flips always suffice inside the mobile sector, and eight are sometimes necessary.

## Assumptions and scope
Vertices are binary four-tuples, identified for reproducibility with integers \(0,\ldots,15\) via binary expansion. Graph edges have Hamming distance one. States are *all* perfect matchings of this labelled graph, with no identification under symmetry. A move is legal only when the four edges of one simple coordinate four-cycle alternate between occupied and unoccupied; all \(24\) coordinate squares are allowed. No six-cycle trades, arbitrary alternating-cycle trades, boundary extension, or intermediate nonmatchings are permitted.

Eccentricity, radius, diameter, and pair distances refer to the connected \(264\)-state mobile component, not to the disconnected full graph. An isolated configuration has no legal square flip.

## Proof
**1. Complete finite state space.** For any set \(U\) of unmatched vertices, take its least-labelled vertex \(u\). Every perfect matching of the induced remaining graph must pair \(u\) with exactly one neighbor \(v\in U\). Choosing each such neighbor and recursing on \(U\setminus\{u,v\}\) lists every perfect matching once. The supplied independent implementation enumerates bijections from the eight even-parity cube vertices to the eight odd-parity cube vertices and keeps exactly the bijections whose edges have Hamming length one. Both enumerations yield \(272\) matchings, a count already in the literature.

**2. Exactly the legal moves.** Each coordinate square is obtained by choosing two distinct coordinate directions and fixing the other two bits. There are \(\binom42\cdot 2^2=24\) squares. If a matching contains two edges of such a square, they must be opposite, and symmetric difference with the four-cycle replaces them with the other opposite pair, yielding a perfect matching. Conversely every allowed move has this form. The Python verifier enumerates the \(24\) squares explicitly; the independent C++ verifier checks all pairs of even-parity vertices for a legal swap of their two odd partners. The resulting graph has \(768\) undirected edges and components of sizes \(264,1,1,1,1,1,1,1,1\). These counts and the component decomposition are checks against existing results, not originality claims.

**3. Exact shortest paths.** From each of the \(264\) mobile states, breadth-first search traverses *all* edges generated in step 2 and assigns graph distance by nondecreasing path length. Since breadth-first search visits every reachable vertex at the minimum path length, the complete computed distance matrix is exact, not a sample. Summing its entries above the diagonal yields the displayed pair-distance vector. The eccentricity tally is \(252\) at \(7\) and \(12\) at \(8\), proving the radius and diameter. The full degree tally over all \(272\) states is \(\{0:8,3:32,4:12,5:96,6:48,8:72,12:4\}\); comparing individual degrees with eccentricities proves the claimed if-and-only-if characterization.

For an explicit sharpness witness, list the even-parity vertices in the order \((0,3,5,6,9,10,12,15)\). Match these respectively to odd-parity vertices

\[
A=(1,2,7,4,11,8,13,14),\quad B=(4,7,13,14,1,2,8,11).
\]

Both vectors describe legitimate perfect matchings. The complete shortest-path computation establishes \(d_H(A,B)=8\), independently checked by both included programs.

**4. Symmetry and the diametral graph.** A coordinate permutation followed by bitwise translation acts on \(Q_4\) and preserves every square flip. The \(16\cdot4!=384\) such maps exhaust the cube automorphism group: an automorphism is determined by the image of one vertex and the permutation of its four neighbors. Applying all of them to each matching gives eight orbits with cardinalities \(4,8,12,24,32,48,48,96\). The \(12\) eccentricity-eight configurations comprise precisely the orbit of size \(12\). In the exact distance matrix each such state has exactly two partners at distance eight, and the resulting distance-eight graph has three connected components, each with four vertices and degree two; hence each is \(C_4\). Applying all cube automorphisms to one diametral pair produces exactly all \(12\) such pairs, establishing the single-pair-orbit assertion.

The two complete verification programs use different state-generation and flip-generation algorithms and independently recompute the full graph and all-source distances; the Python program additionally verifies every symmetry assertion. Both programs are self-contained and supplied with this result.

## Verification
Execute `python3 q4_square_metric.py` and `g++ -std=c++17 -O2 q4_square_metric_independent.cpp -o q4_metric && ./q4_metric`. Each program includes assertions for the complete enumeration, legal adjacency, components, edge count, degree and eccentricity distributions, distance histogram, extremal witness, and distance-eight subgraph. The Python checker additionally proves the asserted symmetry orbits by exhaustive action of all \(384\) natural cube automorphisms. The scripts contain the complete input graph specification and require no external data.

## Relationship to prior work
The perfect-matching count of \(272\) is classical (Graham–Harary; Östergård–Pettersson). Klivans–Saldanha explicitly recorded that the \(2\times2\times2\times2\) domino box has nine square-flip components: one of size \(264\) and eight isolated states, also identifying their twist sectors. Neither the count nor this decomposition is claimed here. Milet–Saldanha supplies the earlier geometric flip-and-twist framework. Bonamy and collaborators study the same four-cycle matching-reconfiguration move for general graph classes and explain why shortest-path metrics matter, but their general results do not give the sharp four-cube metric. The present contribution is specifically the radius, diameter, all-pairs distance distribution, eccentricity characterization, and extremal symmetry geometry *within the already known mobile component*.

## Limitations
The theorem concerns exactly the sixteen-vertex four-cube, square flips, and the fixed state space of perfect matchings. It neither establishes a formula for larger cubes nor any mixing-time estimate. The calculations are finite exhaustive proofs, not evidence for a universal theorem. A prior unpublished or unindexed calculation of the same distances remains possible; no independent audit of historical priority is claimed.

## References
1. P. R. J. Östergård and V. H. Pettersson, *Enumerating Perfect Matchings in n-Cubes*, **Order** 30 (2013), 821–835, first online 2012-11-21. DOI: https://doi.org/10.1007/s11083-012-9279-8.
2. P. H. Milet and N. C. Saldanha, *Domino tilings of three-dimensional regions: flips, trits and twists*, arXiv:1410.7693, first submitted 2014-10-28. https://arxiv.org/abs/1410.7693.
3. M. Bonamy et al., *The Perfect Matching Reconfiguration Problem*, arXiv:1904.06184, first submitted 2019-04-12. https://arxiv.org/html/1904.06184v1.
4. C. J. Klivans and N. C. Saldanha, *Domino tilings and flips in dimensions 4 and higher*, arXiv:2007.08474 (2020), **Algebraic Combinatorics** 5 (2022), 163–185. Example 2.2 and Remark 8.2 explicitly contain the nine-component four-cube classification. https://www.numdam.org/item/10.5802/alco.205.pdf.
5. OEIS A005271, established perfect-matching counts of hypercubes; https://oeis.org/A005271.

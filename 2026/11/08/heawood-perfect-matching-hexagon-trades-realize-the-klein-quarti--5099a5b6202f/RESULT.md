# Heawood perfect-matching hexagon trades realize the Klein quartic graph

## Finding

Let \(H\) be the incidence graph of the seven-point Fano plane. Form the graph \(T(H)\) whose vertices are all perfect matchings of \(H\), joining \(M\) and \(M'\) when their symmetric difference is the edge set of a single simple six-cycle. Then \(T(H)\) is the **Klein quartic graph on 24 vertices**. More explicitly, it is connected and seven-regular, has 84 edges, and is distance-regular with intersection array
\[
\{7,4,1;1,2,7\},
\]
so the distance distribution from every matching is \((1,7,14,2)\), and the diameter is three.

There is a canonical realization of this trade graph inside the Coxeter graph \(C\): identify each of the 28 Heawood six-cycles with one vertex of \(C\), joining two when the original six-cycles are vertex-disjoint. For a perfect matching \(M\), let \(A(M)\) be the seven six-cycles alternating with respect to \(M\). Then \(C[A(M)]\) is an induced seven-cycle, and \(M\mapsto A(M)\) bijects the 24 matchings with the 24 seven-cycles of \(C\). Moreover,
\[
M\sim_{T(H)}M'\quad\Longleftrightarrow\quad
A(M)\cap A(M')\text{ consists of a common two-edge path in }C.
\]
Thus the natural matching trade agrees with the classical adjacency of the Klein graph obtained from Coxeter seven-cycles.

By contrast, fix the natural seven-hexagon orientable toroidal embedding of \(H\), and allow exchanges **only** around its seven facial six-cycles. The resulting facial resonance graph on the *same* 24 perfect matchings is exactly
\[
3K_1\ \sqcup\ 3C_7.
\]
Its three isolated matchings are the three parallel-direction matchings; each remaining seven-cycle has a constant direction signature, one of \((2,4,1)\), \((4,1,2)\), and \((1,2,4)\). Consequently, allowing the 21 nonfacial six-cycles changes a disconnected facial reconfiguration system into the diameter-three Klein graph.

## Assumptions and scope

Use point vertices \(P_i\) and line vertices \(L_j\), for \(i,j\in\mathbb Z/7\mathbb Z\), with
\[
P_iL_j\in E(H)\quad\Longleftrightarrow\quad i-j\in\{0,1,3\}\pmod 7.
\]
A perfect matching is an edge set meeting every vertex exactly once. A six-cycle trade replaces its three matching edges by the three complementary cycle edges. Trades are allowed only when all three alternating cycle edges belong to the matching. Matchings are **not** identified under graph automorphisms, and adjacency is undirected. A Heawood six-cycle is a simple cycle of length six, not necessarily a face of the embedding.

For the facial version, take the oriented local rotations
\[
(P_i: L_i,L_{i-1},L_{i-3}),\qquad
(L_j:P_j,P_{j+1},P_{j+3}),
\]
with indices modulo seven. Their dart-successor face traversal yields seven distinct hexagonal faces, each Heawood edge lying on precisely two faces; Euler characteristic is zero, and these rotations specify an orientable torus embedding. Use the same 24 matching states but restrict the allowed trades to these seven faces. Define the direction signature of a matching \(M\) by recording its counts of edges \(P_iL_j\) with \(i-j\equiv 0,1,3\pmod7\), in that order.

## Proof

**Step 1: exhaust all states and six-cycles.** Every matching is a bijection from the seven points to the seven lines respecting the displayed incidence rule. Enumerate either all \(3^7\) local incidence choices and retain the bijections, or all \(7!\) line permutations and retain those respecting incidence. Both exhaustive methods yield precisely 24 matchings. Exhaustive simple-cycle enumeration, or the independent correspondence with noncollinear point triples in the Fano plane, gives exactly 28 undirected six-cycles.

**Step 2: recover the complete trade graph.** For each matching and each six-cycle, test whether exactly three cycle edges belong to the matching. In that case symmetric difference with the cycle produces another perfect matching, and every possible six-cycle trade arises this way. The first complete enumerator gives seven legal cycles from each of the 24 matchings, hence 84 unordered edges. The second enumerator independently observes that, because the Heawood graph has no four-cycles, two perfect matchings differ on precisely three point assignments if and only if their symmetric difference is a single alternating six-cycle. It reconstructs the same parameters without enumerating the trades in the first manner.

Breadth-first search from **every** matching gives layers \((1,7,14,2)\). For each root, vertex at distance \(k\), and its seven neighbors, count neighbors at distances \(k-1,k,k+1\). For \(k=1,2,3\), these triples are respectively \((1,2,4)\), \((2,4,1)\), and \((7,0,0)\), with no exceptions. This proves distance-regularity with intersection array \(\{7,4,1;1,2,7\}\); the known classification identifies the unique graph with this intersection array as the 24-vertex Klein quartic graph. This is a finite exhaustive proof, not an inference from sampling.

**Step 3: the Coxeter correspondence.** The Coxeter graph constructed on the 28 six-cycles by vertex-disjointness is cubic. For each of the 24 matchings, exactly seven six-cycles alternate with it. Their induced Coxeter subgraph is connected and has degree two at each of its seven vertices, hence is a seven-cycle. These 24 seven-subsets are distinct; the established Coxeter cycle classification contains exactly 24 seven-cycles, so the assignment is a bijection onto all of them. Exhausting the 276 unordered pairs of matchings shows that two are adjacent by one hexagon trade exactly when their seven-subsets intersect in **three** Coxeter vertices spanning **two** Coxeter edges, i.e. a common two-edge path. Together with the known Coxeter-to-Klein construction, this gives an explicit matching-theoretic model of the Klein graph.

**Step 4: faces versus all cycles.** Trace each oriented dart under the prescribed local rotations. The 42 darts partition into seven length-six faces. Restricting the legal-trade test of Step 2 to these seven face edge sets produces 21 undirected adjacency edges. Exactly three matching vertices have facial degree zero; the other 21 have facial degree two, and form three connected seven-cycles. The three isolated matchings have direction signatures \((7,0,0)\), \((0,7,0)\), \((0,0,7)\). The other matching signatures are \((2,4,1)\), \((4,1,2)\), \((1,2,4)\), each occurring seven times and identifying one connected component. An independent Fano arithmetic program uses seven explicit translated face edge sets rather than local dart traversal and obtains the same answer. These are exhaustive enumerations of finite sets, with executable code given below.

## Verification

Two stand-alone standard-library Python files accompany this statement: `verify_matchings.py` builds matchings from local incidence choices, enumerates all simple hexagons, flips, and torus faces from rotations; `verify_fano.py` builds the Fano incidence matrix via the nonzero elements of \(\mathbb F_2^3\), tests all line permutations, constructs hexagons from noncollinear triples, and checks the same claims using three-coordinate Hamming differences and explicitly translated faces. Run `python3 verify_matchings.py` and `python3 verify_fano.py` from the extracted package directory. Both terminate with `PASS` assertions covering the 24 states, 28 hexagons, 84 all-hexagon trade edges, distance-regular intersection array, Coxeter seven-cycles and common-path criterion, and the facial \(3K_1\sqcup3C_7\) decomposition. Neither script relies on external packages, stored enumeration lists, external tables or internet access.

## Relationship to prior work

The number 24 of Heawood perfect matchings and the 28 Heawood six-cycles are classical; **neither is newly asserted**. Ye and Zhang's 2009 preprint discusses the Heawood graph in toroidal/Pfaffian polyhex theory. Dejter's 2010 preprint already constructs the Coxeter graph from the 28 Heawood six-cycles, describes its 24 seven-cycles and the associated 24-vertex Klein quartic graph; the existence and parameters of the Klein graph are **not newly asserted**. The additional assertion here is the explicit bijection \(M\mapsto A(M)\) from *perfect matchings*, with exact equivalence between *alternating-hexagon trades* and the Coxeter common-two-path adjacency.

Tratnik and Ye develop resonance graphs for matchings on surfaces, including structural results when a proper subset of faces is used. The full seven-face setting here is not within their proper-face-subset condition, so its three odd seven-cycles are consistent with that theorem. The later toroidal-polyhex work of Liang and Zhang gives general facial resonance conditions and discusses trivial frozen parallel matchings; those general phenomena are **not claimed as new**. The exact seven-face Heawood decomposition and its sharp contrast with the unrestricted all-hexagon Klein trade graph are the finite claims supplied here. Known descriptions of the Heawood and Klein graphs alone do not state the matching-to-Coxeter trade equivalence.

## Limitations

This is a complete finite computation for the specific incidence graph and the specified seven-face oriented toroidal embedding. It does not establish analogous claims for higher-order projective planes, all toroidal hexagonal graphs, or every embedding. The identification with the named Klein graph invokes its already published uniqueness for the stated intersection array; all enumerative and adjacency assertions have independently executable proof certificates. A differently named historical description of this matching/heptagon correspondence cannot be excluded without exhaustive archival access. No independent scholarly audit is claimed.

## References

1. D. Ye and H. Zhang, *Embeddings of Pfaffian Braces and Polyhex Graphs* (2009 preprint, arXiv:0908.1506v1, publicly submitted 2009-08-11), https://arxiv.org/abs/0908.1506 .
2. I. J. Dejter, *From the Coxeter Graph to the Klein Graph* (2010 preprint, arXiv:1002.1960v1), https://arxiv.org/abs/1002.1960 .
3. N. Tratnik and D. Ye, *Resonance Graphs and Perfect Matchings of Graphs on Surfaces* (2017 preprint, arXiv:1710.00761v1), https://arxiv.org/abs/1710.00761 .
4. L. Liang and H. Zhang, *The Resonance Graphs of Nanotubes and Toroidal Polyhexes* (2026 preprint, arXiv:2609.19766v1), https://arxiv.org/abs/2609.19766 .
5. *Klein graph*, DistanceRegular.org, https://www.math.mun.ca/distanceregular/graphs/klein.html (established graph parameters; may use an updated URL if needed).

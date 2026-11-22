# Parity phases and full graph homotopy types of three-tuplings of triple polygon joins

## Finding
Let \(m,n,\ell\ge4\) be integers, and let \(X=C_m*C_n*C_\ell\) denote the simplicial join of three polygon boundaries. This is a triangulated \(5\)-sphere. Write \(D^3(X)\) for the simplicial three-tupling: vertices are the triangles of \(X\), and two such vertices form an edge exactly when their disjoint union is a face of \(X\).

With \(\times\) denoting the **categorical (tensor/direct) product of loopless graphs**, there is a canonical graph isomorphism
\[
D^3(X)\cong (C_m\times C_n\times C_\ell)\;\sqcup\;(C_m\times K_{n,\ell})\;\sqcup\;(C_n\times K_{m,\ell})\;\sqcup\;(C_\ell\times K_{m,n}).
\]
For \(b=\mathbf1_{2\mid m}+\mathbf1_{2\mid n}+\mathbf1_{2\mid\ell}\), set \(t=2^{\max\{b-1,0\}}\) and \(t_m=1+\mathbf1_{2\mid m}\), with \(t_n,t_\ell\) analogous. Then the exact integral homotopy type is the **disjoint union** of
\[
 t\text{ copies of }\bigvee^{3mn\ell/t+1}S^1,
\qquad t_m\text{ copies of }\bigvee^{[2mn\ell-m(n+\ell)]/t_m+1}S^1,
\]
\[
 t_n\text{ copies of }\bigvee^{[2mn\ell-n(m+\ell)]/t_n+1}S^1,
\qquad t_\ell\text{ copies of }\bigvee^{[2mn\ell-\ell(m+n)]/t_\ell+1}S^1.
\]
Thus the number of components is \(t+3+b\), taking the four values \(4,5,7,10\) as \(b=0,1,2,3\). The first Betti number (sum over components) is
\[
\operatorname{rank}H_1(D^3(X);\mathbb Z)=9mn\ell-2(mn+m\ell+n\ell)+t+3+b.
\]
All integral homology is torsion-free, all homology above degree one vanishes, and every component has free fundamental group of its stated circle rank. In particular \(D^3(C_4*C_4*C_4)\) is a disjoint union of **ten copies of a wedge of 49 circles**.

## Assumptions and scope
The polygons are unfilled simplicial one-spheres with \(m,n,\ell\ge4\) disjoint vertex sets; the graph product is categorical, not Cartesian or strong. The three-tupling uses exactly three vertices per vertex of \(D^3(X)\). Graph components are regarded as a disjoint union, not identified by wedging at a common basepoint. All ranks and homotopy types are integral.

## Proof
**1. Dimension and vertex types.** A face of \(X\) contains at most two vertices from each polygon, so it has at most six vertices. In particular \(D^3(X)\) has no simplices of dimension two or higher. Its vertices are the three-element faces of \(X\), of only two combinatorial types: occupancy \((1,1,1)\), or a permutation of \((2,1,0)\), with the double occupancy necessarily being a polygon edge.

**2. Exact graph identification.** Two triangles are adjacent in \(D^3(X)\) precisely when their union contains one edge in each polygon. This forces their respective occupancy patterns to add coordinatewise to \((2,2,2)\). A triangle of type \((1,1,1)\) can therefore only meet another of that type; adjacency means that all three coordinates are adjacent in their respective cycle, giving \(C_m\times C_n\times C_\ell\). For a triangle with one vertex in the first polygon, the only other possibilities are an edge in the second and no vertices in the third, or vice versa. Adjacency demands adjacent singleton vertices in \(C_m\), and places no restriction on the choice of edges from the second and third polygons. The two edge-choice shores have sizes \(n\) and \(\ell\), yielding exactly \(C_m\times K_{n,\ell}\). Cyclically permute the three polygon factors. These cases exhaust the vertices and edges, proving the displayed **isomorphism**, not merely a homotopy equivalence.

**3. Connected components of categorical products.** We use the following elementary walk fact. For a connected loopless graph, between any two vertices there are arbitrarily long walks of every sufficiently large length having a prescribed feasible parity; backtracking adds length two. In a nonbipartite graph, walking once around an odd cycle makes both parities feasible. In a bipartite graph, the parity is fixed by the endpoints' color classes. A product walk of length \(L\) is precisely a coordinatewise family of length-\(L\) walks. Thus a product of connected graphs with \(q\ge1\) bipartite factors has exactly \(2^{q-1}\) components indexed by parity differences of the bipartition coordinates; with no bipartite factors it is connected. This is also the standard graph direct-product connectivity criterion. A polygon is bipartite exactly when its length is even; \(K_{n,\ell}\) is always connected and bipartite. Consequently the first block has \(t\) components, and each block containing \(C_m\), \(C_n\), or \(C_\ell\) has \(t_m\), \(t_n\), or \(t_\ell\) components.

**4. Exact circle ranks in each component.** The first block has \(mn\ell\) vertices and \(4mn\ell\) edges. Its components all have equal vertex and edge counts: rotations in any even cycle interchange its parity classes and act transitively on the parity-difference labels. Every component has \(mn\ell/t\) vertices and \(4mn\ell/t\) edges, hence cycle rank \(3mn\ell/t+1\). In the second block \(C_m\times K_{n,\ell}\), there are \(m(n+\ell)\) vertices and \(2mn\ell\) edges. If \(m\) is even, rotation of \(C_m\) swaps the two product components, so they have equal counts. Each component therefore has rank \([2mn\ell-m(n+\ell)]/t_m+1\); the other blocks are analogous. Every connected graph deformation retracts onto a wedge of \(E-V+1\) circles by collapsing a spanning tree. This proves all four claimed homotopy summands.

**5. Global counts and a sharp connectivity example.** Every triple of polygon edges yields a six-vertex maximal face of \(X\). It has exactly \(\binom63/2=10\) partitions into two unlabeled triangles, and these partitions uniquely determine edges in \(D^3(X)\). Thus \(E=10mn\ell\). Counting the triangles of types above gives \(V=mn\ell+2(mn+m\ell+n\ell)\). Euler's graph formula \(\beta_1=E-V+\beta_0\) gives the global rank. The initial five-sphere admits four or more tripling components, showing that an arbitrary additional connectedness conclusion beyond the zero-dimensional weak-Cohen–Macaulay bound for such three-tuplings cannot hold even for combinatorial spheres.

## Verification
A dependency-free Python program separately enumerates every six-vertex facet and its ten three-plus-three partitions, builds the resulting three-tupling graph, and constructs the four predicted edge-type families from their occupancy patterns. It checks the exact labeled edge sets, connected components, edge and vertex counts, and ranks for eight length triples, spanning all four parity regimes. Run `python verify_polygon_triple_tupling.py` in the same directory. The recorded output is `verify_polygon_triple_tupling_output.txt`; its final marker is `POLYGON_TRIPLE_TUPLING_COMPLETE_GRAPH_CHECK_PASS`. These tests supplement rather than replace the universal proof.

## Relationship to prior work
Lesh–Schreiner–Wahl introduced simplicial \(r\)-tupling and proved a weak-Cohen–Macaulay connectivity lower bound (Theorem A and Definition 2.1 of arXiv:2506.10436). Their general bound, for a five-sphere and \(r=3\), does not determine components or homotopy ranks. The categorical-product component criterion is classical and is used transparently, not claimed as new. Recent separate calculations of three-tuplings of cyclic six-polytope boundaries give different underlying complexes and parity behavior; they do not provide the present four-factor graph isomorphism or these ranks. The new claim is the joined-polygon specialization and its complete integral homotopy and parity classification.

## Limitations
No claim is made for filled polygons, arbitrary triangulated five-spheres, larger three-tupling dimensions, or higher tuple sizes. The componentwise sphere-wedge ranks are nonnegative positive integers for the stated ranges, and the statement is not an equivariant homotopy classification. The identification rests on the standard simplicial definition; results for Cartesian graph products do not apply. The literature check does not exclude a mathematically equivalent but unindexed statement.

## References
1. K. Lesh, B. Schreiner, N. Wahl, *The double of a simplicial complex*, first public arXiv version June 12, 2025, arXiv:2506.10436v1, Definition 2.1 and Theorem A. https://arxiv.org/abs/2506.10436
2. P. M. Weichsel, *The Kronecker product of graphs*, Proc. Amer. Math. Soc. **13** (1962), 47–52 (connectivity of categorical graph products).

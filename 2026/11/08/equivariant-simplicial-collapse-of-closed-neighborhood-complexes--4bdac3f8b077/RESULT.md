# Equivariant simplicial collapse of closed-neighborhood complexes without four-cycles

## Finding

**Theorem.** Let \(G=(V,E)\) be a finite nonempty simple undirected graph containing no cycle of length four as a *subgraph* (chords do not exempt a four-cycle). Let \(\mathcal C(G)\) be its clique (flag) complex, and let \(\mathcal N[G]\) be its closed-neighborhood complex: a nonempty vertex set \(\sigma\) is a face when \(\sigma\subseteq N_G[v]\) for some \(v\in V\). Then \(\mathcal N[G]\) admits an \(\operatorname{Aut}(G)\)-invariant, dimension-ordered sequence of elementary simplicial collapses onto \(\mathcal C(G)\). In particular, the inclusion \(\mathcal C(G)\hookrightarrow\mathcal N[G]\) is an automorphism-equivariant simple-homotopy equivalence.

Let \(c\) denote the number of connected components, \(n=|V|\), \(e=|E|\), and \(t\) the number of unordered triangles of \(G\). Each component of \(\mathcal N[G]\) is homotopy equivalent to a wedge of circles, and the **total** number of circle summands is
\[
\beta=e-n+c-t.
\]
More precisely, the component corresponding to a connected component \(H\subseteq G\) has \(|E(H)|-|V(H)|+1-t(H)\) circles. The reduced integral homology is \(\widetilde H_0\cong\mathbb Z^{c-1}\), \(H_1\cong\mathbb Z^\beta\), and it vanishes in all higher degrees.

The automorphism action is determined **over the integers** by the natural exact sequence of \(\mathbb Z[\operatorname{Aut}(G)]\)-modules
\[
0\longrightarrow \mathbb Z[\mathcal T]_{\mathrm{or}}\xrightarrow{\ \partial_\triangle\ }H_1(G;\mathbb Z)\longrightarrow H_1(\mathcal N[G];\mathbb Z)\longrightarrow0.
\]
Here \(\mathcal T\) is the set of graph triangles, \(\mathbb Z[\mathcal T]_{\mathrm{or}}\) means the free abelian group on oriented triangles modulo reversing orientation by a sign, and \(\partial_\triangle\) sends an oriented triangle to its oriented edge-boundary. The injection is primitive, so the quotient has no torsion. The result is not only a rank formula: it specifies the natural integral symmetry representation.

**Sharpness of the uniform condition.** The four-cycle itself has \(\mathcal N[C_4]=\partial\Delta^3\simeq S^2\), while \(\mathcal C(C_4)\simeq S^1\). Thus a uniform collapse theorem cannot simply permit arbitrary four-cycles.

## Assumptions and scope

All complexes are finite abstract simplicial complexes and all homotopy statements concern their geometric realizations. Isolated vertices and disconnected graphs are permitted; the empty graph is excluded. The hypothesis forbids every four-cycle, not merely induced four-cycles. A triangle is an unordered three-vertex clique; a connected component consisting of a single vertex contributes zero circles. The equivariance assertion concerns graph automorphisms (not arbitrary graph homomorphisms). Oriented edges and triangles carry the usual sign under reversal.

## Proof

**1. Unique center of a nonflag simplex.** If two distinct vertices \(x,y\) have two distinct common neighbors \(u,v\), then \(x,u,y,v,x\) is a four-cycle. Therefore any pair of vertices in \(G\) has at most one common neighbor. Every simplex \(\sigma\in\mathcal N[G]\setminus\mathcal C(G)\) contains two nonadjacent vertices \(x,y\). A center \(v\) witnessing \(\sigma\subseteq N_G[v]\) must differ from both \(x,y\) and be their common neighbor. Consequently \(\sigma\) has a *unique* witnessing center \(v=v(\sigma)\). Since every vertex of \(\sigma\setminus\{v\}\) is adjacent to \(v\), a nonadjacent pair in \(\sigma\) remains after removing \(v\). Thus \(\sigma\setminus\{v\}\) is also nonflag. If \(v\notin\sigma\), the coface \(\sigma\cup\{v\}\) is nonflag and has the same unique center.

**2. The elementary collapses.** For every nonflag simplex \(\tau\) with \(v(\tau)\notin\tau\), pair
\[
  (\tau,\ \tau\cup\{v(\tau)\}).
\]
These pairs partition *all* nonflag simplices: a nonflag simplex containing its center is paired with the same simplex after removal of that center. Order lower members \(\tau\) by decreasing cardinality, breaking ties arbitrarily. When \(\tau\) is considered, any proper coface \(\rho\supsetneq\tau\) is nonflag and has the same unique center \(v(\tau)\). If \(\rho\) has more than one extra vertex, then it has already been removed in an earlier pair. If it has exactly one extra vertex other than the center, it too was an earlier lower or upper member: if it contains the center it must be the designated upper member; otherwise its lower member has larger cardinality than \(\tau\). Hence the only remaining proper coface of \(\tau\) is \(\tau\cup\{v(\tau)\}\). This proves each ordered cancellation is an elementary simplicial collapse. The unpaired simplices are precisely the cliques, so the resulting subcomplex is \(\mathcal C(G)\).

The center and the pairing are canonical under every graph automorphism; cardinality is invariant too. All pairs of a fixed lower cardinality can be removed in arbitrary order, and such equal-size pairs never share a face. Therefore each cardinality-stage is invariant under \(\operatorname{Aut}(G)\) and defines an equivariant collapse of the realization. (A chosen tie-breaking order need not itself be equivariant, but the stagewise collapse is.)

**3. Reduction to one-dimensional topology.** The graph has no four-vertex clique, because any such clique contains a four-cycle. Thus \(\mathcal C(G)\) has dimension at most two. Its two-simplices are the triangles of \(G\). Two distinct triangles cannot share an edge: if triangles \(abc\) and \(abd\) share \(ab\), the vertices \(c,a,d,b\) form a four-cycle, irrespective of extra edges. Every triangle therefore contains edges not used by any other triangle. Choose one edge in each triangle and remove the triangle together with that free edge. This is a sequence of elementary collapses from \(\mathcal C(G)\) to a graph with \(n\) vertices and \(e-t\) edges, with the original \(c\) components. Each remaining component has the homotopy type of a wedge of \(|E(H)|-|V(H)|+1-t(H)\) circles, giving the stated rank and homology. No equivariance is asserted for this *second* arbitrary edge-selection step.

**4. Integral symmetry lattice.** The chain groups in degrees zero and one of \(\mathcal C(G)\) are identical to those of \(G\); the only additional boundary generators are the oriented triangle boundaries. Therefore
\[
H_1(\mathcal N[G];\mathbb Z)\cong H_1(\mathcal C(G);\mathbb Z)
=\ker(\partial_1:C_1(G;\mathbb Z)\to C_0(G;\mathbb Z)) /\langle\partial_\triangle(T):T\in\mathcal T\rangle.
\]
The triangle boundaries are independent and span a primitive sublattice: their supports on graph edges are disjoint and each has a coefficient \(\pm1\) on its own private edge. Thus they can be included in an integral basis of \(C_1(G;\mathbb Z)\), and their quotient in the cycle lattice is torsion-free. All maps preserve the natural automorphism action, proving the exact module sequence. Higher homology vanishes by the graph collapse.

**5. Sharpness.** For the four-cycle \(C_4\), its four closed neighborhoods are precisely the four three-element subsets of the vertex set. Hence the closed-neighborhood complex is the boundary of a tetrahedron, whereas the graph clique complex is the four-cycle itself. Their integral homology differs.

## Verification

The standalone `verify.py` enumerates **every labeled simple graph** on one through six vertices (33,867 graphs in total). It identifies 8,597 graphs with no four-cycle. For each qualifying graph it independently builds all neighborhood faces and all cliques, derives the unique-center pairing, replays every elementary deletion, and checks that the remaining faces are exactly the clique complex. It also checks the Euler characteristic against the component/triangle formula. Three symmetric examples separately verify the pairing against every graph automorphism: a five-cycle, two triangles joined at a vertex, and a six-vertex star. Finally, the checker reconstructs the tetrahedral-boundary complex for the excluded four-cycle. The exact output is embedded in `verify_output.txt` and terminates with `ALL_VERIFY_OK`.

Run `python3 verify.py` in a directory containing the supplied file. These finite checks test the algorithm, not the universally quantified proof in Steps 1–5.

## Relationship to prior work

Matsushita, *Closed neighborhood complexes of graphs* (arXiv:2511.12608, first public version November 16, 2025), defines this precise complex, relates it to doubled-cover independence complexes and neighborhood hypergraphs, and identifies its fundamental group with a graph-theoretic fundamental group. The present result instead supplies an explicit automorphism-invariant elementary collapse, a complete integral homotopy classification, and an integral triangle-relation representation under the no-four-cycle condition. These are not consequences of the stated fundamental-group identification alone.

Borgwardt, Carr, Chen, Ge, Hartke, Huang and Moon, *Reconstruction of \(C_4\)-free graphs from the set of closed neighborhoods and digital convexity* (arXiv:2510.21195, first public version October 24, 2025), studies reconstruction from neighborhood *sets*. Its main theorems are not statements about simplicial homotopy, collapse or homology. Here \(C_4\)-free always means free of a four-cycle as a subgraph; the reconstruction literature sometimes uses the weaker induced-free convention.

## Limitations

The result does not apply indiscriminately to graphs containing four-cycles; the four-cycle itself is an obstruction. It does not determine the homotopy type of all closed-neighborhood complexes, nor does it provide an equivariant *graph-level* one-dimensional collapse after triangle removal. The finite checker stops at six graph vertices, while the mathematical proof covers every finite graph satisfying the hypothesis. No independent external mathematical review has been performed.

## References

1. T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608 (first posted November 16, 2025), https://arxiv.org/abs/2511.12608 .
2. S. Borgwardt, M. Carr, C. Chen, W. Ge, S. G. Hartke, Y. Huang and A. Moon, *Reconstruction of \(C_4\)-free graphs from the set of closed neighborhoods and digital convexity*, arXiv:2510.21195 (first posted October 24, 2025), https://arxiv.org/abs/2510.21195 .

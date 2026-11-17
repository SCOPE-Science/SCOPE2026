# Distance-three stabilization for open-neighborhood complexes of doubly punctured Boolean cubes

## Finding
Let \(Q_n\) be the graph on \(\{0,1\}^n\), with edges joining Hamming-distance-one vertices. For two distinct vertices \(u,v\), put \(d=d_H(u,v)\). The *ordinary open-neighborhood complex* \(\mathcal N(G)\) consists of all finite nonempty vertex sets contained in the open graph neighborhood of some vertex, together with their subfaces. For every integer \(n\ge4\), \(\mathcal N(Q_n-\{u,v\})\) has exactly two components. Each component is homotopy equivalent over the integers to a wedge of \(b_n(d)\) two-spheres, where

\[\begin{aligned}
\mu_n&=2^{n-3}(n^2-5n+8)-1,\\
b_n(d)&=\mu_n-\binom{n-1}{2}-e_n(d),\\
e_n(d)&=\begin{cases}
\binom{n-2}{2},&d=1,\\
\binom{n-1}{2}-1,&d=2,\\
\binom{n-1}{2},&3\le d\le n.
\end{cases}
\end{aligned}\]

All integral homology is torsion-free. The stable value for all distances at least three is the same although the punctured graphs need not be isomorphic. For \(n=3\), the two components are contractible at distances one and two, and each is \(S^1\) at distance three. The multiplicities for \(n=4\) are respectively \(3,2,1\), and for \(n=5\) they are \(22,20,19\), in the three distance regimes.

## Assumptions and scope
Graph edges are undirected, open rather than closed neighborhoods are used, and the complex contains no empty-face vertex when it is realized. Two parity classes of the hypercube induce disjoint neighborhood-complex components. All homotopy equivalences are ordinary nonequivariant integral equivalences. For \(n\ge3\), deleting two graph vertices leaves no isolated graph vertices; the theorem does not include lower dimensions.

## Proof
**1. Two-sided duality.** If \(G\) is bipartite with shores \(A,B\) and has no isolated vertices, the component of \(\mathcal N(G)\) on \(A\) is covered by full simplices \(\Delta(N_G(b))\) for \(b\in B\). Every nonempty intersection is a simplex; its nerve is exactly the component on \(B\). The nerve lemma therefore gives a homotopy equivalence between the two components. This remains valid after deleting either or both cube vertices. It suffices to compute the side on which the relevant deletion removes a neighborhood **facet**.

**2. Full-cube model.** Fix one parity side. Its vertices are the \(2^{n-1}\) cube vertices of that parity; its edges join pairs at Hamming distance two. A three-element subset of a cube vertex's open neighborhood has that vertex as its unique common neighbor. Consequently every face of size at least three belongs to one unique neighborhood simplex. In each such simplex, choose one apex and pair every face of cardinality at least three that omits the apex with the face obtained by adding it, processing descending cardinalities. This gives a sequence of elementary collapses to dimension at most two (the triangle faces containing the apex remain). The number of edges is \(2^{n-2}\binom n2\). Its Euler characteristic is
\[\chi=2^{n-3}(n^2-5n+8),\]
by counting unique neighborhood-supported faces of size at least three.

Its fundamental group is trivial: take the two-coordinate flips as the edges of the halved cube, and choose the independent generators \(e_1+e_i\), \(2\le i\le n\). A triangle on three neighbors of a cube vertex replaces any edge labeled \(e_i+e_j\) (with \(i,j>1\)) by a length-two path of these chosen generators. The remaining Cayley graph is the \((n-1)\)-cube; every square commutation relation is filled by two of the original triangles. A presentation of the cubical graph by its square relations proves simple connectivity. The collapsed simply connected two-dimensional CW complex is therefore a wedge of \(\mu_n=\chi-1\) two-spheres: its only reduced homology is free in degree two, and the Hurewicz and Whitehead theorems apply.

**3. Facet-removal lemma.** Suppose a center vertex \(a\) is removed, so its full simplex \(\Delta(N(a))\) is removed from a neighborhood component. The old complex is \(Z=Y\cup\Delta(N(a))\). The intersection \(A=Y\cap\Delta(N(a))\) is a **graph**: no triangle of three distinct neighbors of \(a\) has another common graph neighbor. If \(A\) is connected and its inclusion in \(Y\) is nullhomotopic, the homotopy pushout for cofibrations yields \(Z\simeq Y\vee\Sigma A\). Hence when \(Z\simeq\bigvee^r S^2\) and \(Y\) retains a collapse to dimension two, \(Y\simeq\bigvee^{r-\beta_1(A)}S^2\). Indeed \(\pi_1(Y)=0\) by the wedge splitting; a simply connected two-dimensional CW complex is a wedge of two-spheres. The connectedness and nullhomotopy hypotheses are verified in each application below.

**4. First puncture.** Remove \(u\) as a center from one parity component. Its attaching graph \(A\) is the complete graph on the \(n\) neighbors of \(u\): every pair has a second supporting center and no triple does. Its rank is \(\binom{n-1}{2}\). Every triangle in this graph bounds the three triangles with fourth vertex \(u+e_i+e_j+e_k\); all their supporting centers remain. Thus inclusion \(A\to Y\) is nullhomotopic and the first puncture gives a wedge of \(\nu_n=\mu_n-\binom{n-1}{2}\) two-spheres. By Step 1 this is the homotopy type on either parity side.

**5. Even-distance second puncture.** If \(d\) is even, choose the side on which both deleted graph vertices act as centers. After removing \(u\), remove \(v\). For \(d\ge4\), the attaching graph is again complete on \(n\) vertices. For \(d=2\), exactly the edge between the two common neighbors of \(u\) and \(v\) is missing: their pair has only the two supporting centers \(u,v\). The graph is then \(K_n\) with one edge removed, which is connected for \(n\ge4\). Every triangle of either attaching graph bounds via the three triangles supported around the vertex obtained by flipping its three corresponding coordinates at \(v\). That vertex is distinct from the already deleted \(u\), because the latter lies an even distance from \(v\). The cycle space of a complete graph, or a complete graph with one edge removed, is generated by its triangles. Their nullhomotopic boundaries establish nullhomotopy of the attaching graph, proving the distance-two and even-distance-at-least-four cases.

**6. Odd-distance second puncture.** If \(d\) is odd, choose the parity side containing \(u\) as a simplex vertex and \(v\) as a center. Following deletion of \(u\), the neighborhood of \(v\) has \(n-1\) surviving vertices for \(d=1\) and \(n\) for \(d\ge3\). The attaching graph is complete on those surviving vertices. Its cycle rank is respectively \(\binom{n-2}{2}\) or \(\binom{n-1}{2}\). Its triangles admit the same three-triangle fillings unless \(d=3\) and the required opposite cube vertex is precisely the deleted \(u\). In this one case, let the exceptional triangle's vertices be \(w_1=v+e_1,w_2=v+e_2,w_3=v+e_3\) after relabeling; choose a fourth coordinate \(h\) (possible since \(n\ge4\)), and write \(z_{ij}=v+e_i+e_j+e_h\). The following seven triangles form an explicit simplicial disk with boundary \(w_1w_2+w_2w_3+w_1w_3\):
\[\begin{gathered}
(w_1,w_2,z_{12}),\ (w_2,w_3,z_{23}),\ (w_1,w_3,z_{13}),\\
(w_1,z_{12},z_{13}),\ (w_2,z_{12},z_{23}),\ (w_3,z_{13},z_{23}),\\
(z_{12},z_{13},z_{23}).
\end{gathered}\]
Every triangle belongs to the surviving neighborhood complex, and no listed vertex is deleted. Therefore all attaching graph triangles bound, and the attaching map is nullhomotopic. The lemma yields the distance-one and odd-distance-at-least-three formulas.

**7. Small boundary and components.** At \(n=3\), deletion of opposite cube vertices leaves a six-cycle, whose open neighborhood complex is two triangles' boundaries, each a circle. At distances one and two, direct enumeration gives a contractible component on each parity side (each is a tree or a simplex). For \(n\ge4\), the connected attaching graphs ensure the remaining parity components are connected at every deletion stage. The stated multiplicities are nonnegative, completing the proof.

## Verification
The standalone `verify.py` reconstructs all faces directly from each remaining center's open neighborhood. It independently calculates the mod-two triangle-to-edge boundary rank, the number of one-skeleton components, and the full Euler characteristic; the proved collapse to dimension two supplies the degree-two Betti number. Every pair-distance orbit and both parities are checked for \(n=3,4,5,6,7\): 50 complexes containing 111,952 enumerated nonempty faces in total. All agree with the displayed formula. An additional check constructs and validates each of the seven triangles in the exceptional disk for \(n=4,5,6,7\), including its boundary. Execute `python3 verify.py`; the expected output is in `check_output.txt`. Computations validate finite cases, **not** the all-dimensional claim; the latter follows from Steps 1–7.

## Relationship to prior work
The general open-neighborhood construction and the topological perspective on Lovász complexes appear in Arana and Stehlík [1]. Their surface-quadrangulation classification assumes nonbipartite graphs and does not specialize to these bipartite cubes. Shen et al. [2] examine neighborhood homotopy for induced independence graphs and several graph families other than doubly punctured hypercubes. An indexed earlier full-cube result gives the same \(\mu_n\), while an earlier one-point puncture statement gives \(\nu_n\); neither implies the second-deletion distance dependence without identifying the attaching map. Those two inputs were reproved above, making this argument self-contained. The present claim is solely the complete **two-vertex deletion** classification.

## Limitations
The result uses the ordinary **open** neighborhood construction and exactly two deleted vertices. It does not classify three or more punctures, induced maps between different deletion stages, equivariant sphere splittings, or graph-metric Rips complexes. Similar or unindexed prior formulations could remain undiscovered. All verification is internal; no independent mathematical audit has been performed.

## References
[1] Carmen Arana and Matěj Stehlík, *Quadrangulations and the Lovász complex*, arXiv:2510.03698, first posted 2025-10-04. https://arxiv.org/abs/2510.03698

[2] Yufeng Shen, Zhiyu Song, Feneglin Yu, Leopold Wuhan Zhou, and Jingqi Zhuang, *Neighborhood Complexes of induced k-independent graphs*, arXiv:2512.09674, first posted 2025-12-10. https://arxiv.org/abs/2512.09674

# A sharp pentagon threshold for the homotopy interleaving distance of cactus enriched nerves

## Finding
Let \(G\) be a finite connected simple cactus graph with at least two vertices, every edge of unit length, and shortest-path metric \(d_G\). A cactus graph means one whose every edge belongs to at most one simple cycle. Let \(N(G)\) be the **ordered enriched nerve** persistent simplicial set: at real scale \(t\ge 0\), a \(q\)-simplex is a tuple \((x_0,\ldots,x_q)\) of vertices satisfying
\[
\sum_{i=0}^{q-1}d_G(x_i,x_{i+1})\le t,
\]
with face maps deleting vertices and degeneracy maps duplicating them. Let \(d_{\mathrm{IHC}}\) be the interleaving distance in the homotopy category of real-indexed persistence simplicial sets with the projective model structure.

**Theorem.** If every simple cycle in \(G\) has length at most five, then
\[
d_{\mathrm{IHC}}\bigl(N(G),N(\mathrm{pt})\bigr)
=\begin{cases}
\tfrac12,&\text{if all cycles have length at most four},\\
1,&\text{if some cycle has length five}.
\end{cases}
\]
Trees are included in the first case. More generally, if \(G\) is any finite connected cactus graph with a simple cycle of length at least five, then
\[
d_{\mathrm{IHC}}\bigl(N(G),N(\mathrm{pt})\bigr)\ge 1.
\]
No exact value is asserted for cacti containing longer cycles.

## Assumptions and scope
All simplicial sets use the inclusive length convention \(\le t\), not an unordered Vietoris--Rips or clique complex. The topology is encoded in the persistent ordered simplicial set itself; \(d_{\mathrm{IHC}}\) is *not* the distance between its homology barcodes. Maps of finite graph metrics are \(1\)-Lipschitz when they do not increase shortest-path distances. An elementary \(r\)-homotopy of such maps has pointwise displacement at most \(r\), and an \(r\)-homotopy is a finite zigzag of elementary \(r\)-homotopies. The external homotopy-interleaving theorem used below says \(r\)-homotopy equivalence implies \(r/2\)-interleaving of enriched nerves in the homotopy category [1, Theorem 3.9]. All quantifiers in this theorem range over finite connected simple unit-edge cactus graphs of the specified type.

## Proof
**1. Rooted block contractions.** The block--cut incidence graph of a connected cactus is a tree; its nontrivial blocks are single edges or chordless cycles. Root this tree and repeatedly prune a terminal block \(B\) meeting the unpruned graph in just its attachment vertex \(a\). Every local map below fixes vertices outside \(B\). Such a map is \(1\)-Lipschitz globally if each original graph edge maps to a graph edge or a point; this is because the distance of two images cannot exceed the length of the image of a shortest edge path.

For an edge or triangle, map all vertices in \(B\) to \(a\), a \(1\)-Lipschitz map moving no vertex more than one unit. For a four-cycle whose cyclic order is \((a,b,c,d,a)\), first use the map \((a,b,c,d)\mapsto(a,b,b,a)\), then send \(b\) to \(a\). Both maps fix \(a\) and all exterior vertices, are \(1\)-Lipschitz, and move every vertex by at most one. Thus every block with at most four edges can be pruned by a zigzag of elementary \(1\)-homotopies, yielding a \(1\)-homotopy between the identity on the original graph and a constant map.

For a five-cycle rooted at \(a\), send the entire block to \(a\) in one map. It is \(1\)-Lipschitz and moves each vertex by at most two, since the cycle radius from \(a\) is two. The edge, triangle and four-cycle contractions above are also elementary \(2\)-homotopies, so every cactus with cycle lengths at most five admits a \(2\)-homotopy from its identity to a constant map. Formally, compose each local contraction with all preceding contractions; the resulting maps on the original vertex set remain \(1\)-Lipschitz and retain the stated pointwise consecutive-displacement bound. For \(p:G\to\mathrm{pt}\) and \(i:\mathrm{pt}\to G\) selecting the final vertex, we have \(pi=\mathrm{id}\) and \(ip\) homotopic to \(\mathrm{id}_G\) at the indicated bound. Theorem 3.9 of [1] therefore yields
\[
d_{\mathrm{IHC}}(N(G),N(\mathrm{pt}))\le\tfrac12
\quad\text{or}\quad
\le1
\]
respectively.

**2. Universal half-unit lower bound.** For each \(0\le t<1\), \(N(G)(t)\) is the discrete simplicial set on the \(|V(G)|\ge2\) vertices. If \(\delta<\tfrac12\), an interleaving with a point would force the structure map on \(H_0\) from scale zero to \(2\delta<1\) to factor through the rank-one \(H_0\) of a point. This structure map is the identity on \(\mathbb Z^{|V(G)|}\), an impossibility. Since homology descends to the homotopy category, this proves
\[
d_{\mathrm{IHC}}(N(G),N(\mathrm{pt}))\ge\tfrac12.
\]

**3. Persistent winding obstruction on a long cactus cycle.** Suppose \(G\) contains a cycle \(C_n\) of length \(n\ge5\). A cactus contains no external path between distinct vertices of a given cycle: such a path would produce a second simple cycle sharing edges with it. Consequently \(C_n\) embeds isometrically in \(G\), and collapsing each component of \(G\setminus V(C_n)\) to its unique attachment vertex yields a \(1\)-Lipschitz retraction \(\rho:G\to C_n\). It follows that the homology persistence of \(N(C_n)\) is a direct summand, by maps induced from the inclusion and \(\rho\), of the corresponding persistence of \(N(G)\).

Index the vertices of \(C_n\) by \(\mathbb Z/n\mathbb Z\). Every directed one-simplex \((i,j)\) in \(N(C_n)(2)\) has a **unique** signed displacement \(\omega(i,j)\in\{-2,-1,0,1,2\}\) satisfying \(j\equiv i+\omega(i,j)\pmod n\). Uniqueness uses \(n\ge5\), and the integer is the signed shortest displacement; for a degenerate edge it is zero. For each ordered two-simplex \((i,j,k)\) of total length at most two, the displacements add without wrapping, so
\[
\omega(j,k)-\omega(i,k)+\omega(i,j)=0.
\]
Thus \(\omega\) is an integral degree-one cocycle on \(N(C_n)(2)\). The oriented cycle
\[
\gamma=\sum_{i\in\mathbb Z/n\mathbb Z}(i,i+1)
\]
is a degree-one cycle already at scale one and pairs with \(\omega\) to \(n\ne0\). Hence its class survives under \(H_1(N(C_n)(1);\mathbb Z)\to H_1(N(C_n)(2);\mathbb Z)\). By the retraction it also survives from scale one to two in \(N(G)\).

All distances in \(G\) are integers, so the filtration is constant at noninteger scales. For any \(0\le\delta<1\), the structure map from scale \(1\) to scale \(1+2\delta<3\) contains this same nonzero \(H_1\)-transition from scale one to two (or is the identity at scale one if \(2\delta<1\)). An interleaving with a point would make that homology transition factor through zero, since \(H_1(N(\mathrm{pt})(t);\mathbb Z)=0\) for every \(t\). Thus no such \(\delta\) exists and
\[
d_{\mathrm{IHC}}(N(G),N(\mathrm{pt}))\ge1.
\]
Combining all lower and upper bounds proves the theorem. \(\square\)

## Verification
The standalone `check_cactus_nerve.py` performs 23 deterministic finite checks: it verifies that explicit maps on selected bouquets of edge, triangular, quadrilateral and pentagonal blocks are globally nonexpansive and satisfy the claimed pointwise move bounds, and it checks the integral winding cocycle identity and nonzero pairing on cycles of lengths five through eighteen. Execute `python check_cactus_nerve.py` with Python 3. It passed with output `PASS 23 finite fold and integral-cocycle checks`. The infinite-family argument is the block--cut induction and the winding cocycle proof above; finite tests alone do not establish that claim.

## Relationship to prior work
Kuribayashi [1] defines the interleaving distance \(d_{\mathrm{IHC}}\) for enriched nerves, proves the upper bound from \(r\)-homotopy equivalence (Theorem 3.9), and establishes the exact one-half value for complete graphs (Corollary 3.13). That upper-bound theorem alone does not assert the existence of short homotopy contractions on cacti or the converse lower obstruction at a five-cycle. The new claims here are the uniform sharp block-length threshold, the explicit relative four-cycle folds and the persistent integral winding argument, which together determine the distance independently of graph diameter throughout the indicated cactus class. Ivanov and Xu [2] identify the ordered \(\ell_1\)-Vietoris--Rips simplicial set with blurred magnitude homology, and Lanari and Scoccola [3] develop the interleaving-in-homotopy-category framework. These definitional/stability results do not themselves compute this cactus threshold. A separately indexed chordality theorem for squares of cactus-block graphs concerns a graph-power property, not the enriched nerve's interleaving distance [4].

## Limitations
The exact two-phase formula is proved only when every cycle has length at most five. For longer cycles this paper proves the lower bound one, not an exact distance. The hypotheses require finite connected unweighted simple cactus graphs with at least two vertices; they do not extend by assertion to weighted graphs or arbitrary graphs sharing cycle edges. The result is for the ordered enriched nerve and homotopy-category interleaving distance, not an unordered simplicial complex or a strict interleaving distance. No external independent audit has been performed. Literature searches cannot exclude unindexed equivalent calculations.

## References
[1] K. Kuribayashi, *Enriched nerves, interleaving distances and the multiplicative magnitude-path spectral sequence*, arXiv:2611.22433v1, first public 17 November 2026, Definitions 3.3, Theorem 3.9, Corollaries 3.11--3.14. https://arxiv.org/html/2611.22433v1

[2] S. O. Ivanov and X. Xu, *On \(\ell_p\)-Vietoris--Rips complexes*, arXiv:2411.01857v2, first public 4 November 2024, Sections 1--3. https://arxiv.org/html/2411.01857v2

[3] E. Lanari and L. Scoccola, *Rectification of interleavings and a persistent Whitehead theorem*, arXiv:2010.05378, first public 12 October 2020, Sections 1--2. https://arxiv.org/abs/2010.05378

[4] *Sharp five-cycle threshold for chordal squares of cactus-block graphs*, 2026, published research index. https://github.com/published-finding corpus/2026/tree/main/2026/9/18/SCOPE-chordal-squares-block-cactus-cycle-threshold--38333a852fbc

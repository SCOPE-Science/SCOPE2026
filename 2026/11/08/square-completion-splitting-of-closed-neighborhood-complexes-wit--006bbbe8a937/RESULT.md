# Square-completion splitting of closed-neighborhood complexes with codegree at most two

## Finding
For every finite connected simple triangle-free graph \(G\) satisfying \(|N(u)\cap N(v)|\le2\) for all distinct vertices \(u,v\), its closed-neighborhood complex \(\mathcal N[G]\) admits a simplicial collapse onto \(G\) together with one tetrahedral boundary for every four-cycle. If \(q\) is the number of four-cycles and \(K_\square(G)\) is the square-filled CW complex, then
\[
|\mathcal N[G]|\simeq|K_\square(G)|\vee\bigvee^q S^2.
\]
The splitting is an integral homotopy equivalence, not just a homology identity. It is not asserted to be canonical or equivariant.

As a consequence, take integers \(m,n\ge5\) and the twisted grid \(G_{m,n}^{\mathrm{tw}}\) whose vertices are pairs \((a,b)\) with \(a\in\mathbb Z/m\mathbb Z\) and \(0\le b<n\). The edges join \((a,b)\) to \((a+1,b)\), join \((a,b)\) to \((a,b+1)\) for \(b<n-1\), and join \((a,n-1)\) to \((-a,0)\). Its natural square completion is the Klein bottle \(\mathbb K\), with exactly \(mn\) four-cycles. Thus
\[
|\mathcal N[G_{m,n}^{\mathrm{tw}}]|\simeq\mathbb K\vee\bigvee^{mn} S^2,
\qquad H_1(\mathcal N[G_{m,n}^{\mathrm{tw}}];\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2\mathbb Z,
\quad H_2\cong\mathbb Z^{mn}.
\]
This exhibits integral torsion in a natural triangle-free graph-neighborhood complex while identifying its full homotopy type.

## Assumptions and scope
All graphs are finite, undirected, loopless, simple and connected. \(N(v)\) is the open neighborhood and \(N[v]=N(v)\cup\{v\}\) the closed neighborhood. The simplicial complex \(\mathcal N[G]\) consists of all subsets of some \(N[v]\). A four-cycle means an unoriented simple cycle with four distinct vertices; its four-element vertex set uniquely determines it under the codegree hypothesis. The CW square completion \(K_\square(G)\) attaches one closed two-cell along each embedded four-cycle of the graph \(G\). A zero-fold wedge of spheres is a point. The Klein bottle \(\mathbb K\) means the standard connected closed nonorientable surface with Euler characteristic zero. 

The codegree condition is equivalent to exclusion of a \(K_{2,3}\) subgraph, not necessarily induced. Four-cycles may share one edge and many vertices. This genuinely extends the edge-disjoint-square situation. No assertion is made about graphs with triangles or with three common neighbors for some pair.

## Proof
**Step 1 (uniqueness of large faces).** If two distinct vertices \(v,w\) are adjacent, then by triangle-freeness their closed neighborhoods intersect in precisely \(\{v,w\}\). If they are nonadjacent, \(N[v]\cap N[w]=N(v)\cap N(w)\), which has size at most two by hypothesis. Therefore every simplex with at least three vertices belongs to exactly one closed-neighborhood maximal simplex \(\Delta(N[v])\).

**Step 2 (large-face collapses).** Fix a center \(v\). For each integer \(k\) descending from \(|N(v)|\) to three, and each \(k\)-element subset \(S\subseteq N(v)\), pair the face \(S\) with \(S\cup\{v\}\) for an elementary simplicial collapse. At the moment of removal, uniqueness from Step 1 prevents any other neighborhood simplex from containing \(S\). Descending order removes all its possible larger cofaces. Hence \(S\) is a free face of exactly the coface \(S\cup\{v\}\). The operations do not interfere across centers. What remains contains original vertices and graph edges; its two-dimensional simplices are exactly the triples \(\{v,a,b\}\) with \(a,b\in N(v)\) distinct, and it has the corresponding \(\{a,b\}\) diagonal edges.

**Step 3 (unique common neighbors).** For every nonadjacent pair \(\{a,b\}\) having exactly one common neighbor \(v\), the edge \(\{a,b\}\) is incident to the single remaining triangle \(\{a,b,v\}\). Removing this free edge and triangle is an elementary collapse. An adjacent pair does not receive a triangle: triangles in the remaining complex use two nonadjacent neighbors of their center, since \(G\) is triangle-free.

**Step 4 (the residual square spheres).** If a nonadjacent pair \(a,b\) has two common neighbors \(v,w\), these four vertices determine the cycle \(a-v-b-w-a\); the other diagonal \(v,w\) is also a nonedge and has exactly the common neighbors \(a,b\). Thus the residual triangles on these vertices are precisely \(\{a,b,v\},\{a,b,w\},\{a,v,w\},\{b,v,w\}\), the boundary of the tetrahedron on the cycle's four vertices. Every residual non-graph edge is a diagonal of precisely one such square, because two different squares containing it would give at least three common neighbors to its endpoints. Consequently the residual simplicial complex is exactly
\[
L=G\cup\bigcup_{Q\in\mathscr Q(G)}\partial\Delta^3(Q).
\]
Different tetrahedral boundaries may meet along original graph edges and vertices, but share neither diagonals nor triangles. Steps 2 and 3 constitute an explicit simplicial collapse \(\mathcal N[G]\searrow L\).

**Step 5 (homotopy decomposition).** For each square \(Q=(a,v,b,w,a)\), choose the diagonal \(a-b\). The two triangles incident to this diagonal form a closed triangulated two-disk whose boundary is exactly the four-cycle in \(G\). The collection of these first two-disks attached to \(G\) is a triangulation of \(K_\square(G)\). The remaining two triangles in the tetrahedral boundary form a second closed disk whose attaching map is the same four-cycle (up to orientation). That loop is already nullhomotopic in \(K_\square(G)\), being the boundary of the first disk. Attaching each remaining two-cell therefore wedges on one two-sphere, with standard basepoint paths if necessary. All these additional cells attach independently along nullhomotopic loops, even if different original square rims share graph edges. Thus \(|L|\simeq |K_\square(G)|\vee\bigvee^q S^2\), proving the theorem. In particular, \(\pi_1(\mathcal N[G])\cong\pi_1(K_\square(G))\) and \(H_2(\mathcal N[G];\mathbb Z)\cong H_2(K_\square(G);\mathbb Z)\oplus\mathbb Z^q\).

**Step 6 (nonorientable example).** The twisted grid described above is the one-skeleton of the standard square-cell decomposition obtained by identifying one pair of opposite sides of a rectangle periodically and the other with a reflection. For \(m,n\ge5\), its only four-cycles are its \(mn\) elementary squares: any four-step closed path in the universal square lattice must consist of two opposite moves in each of two coordinate directions, and the minimum nontrivial deck-translation length is at least five. The graph is triangle-free and pairs of vertices have at most two common neighbors. Its square-filled CW complex is the Klein bottle. The fundamental polygon presentation \(\pi_1(\mathbb K)=\langle x,y\mid xyx^{-1}=y^{-1}\rangle\) abelianizes to \(\mathbb Z\oplus\mathbb Z/2\mathbb Z\); \(H_2(\mathbb K;\mathbb Z)=0\). Substituting in Step 5 gives the stated homotopy and integral homology for all \(m,n\ge5\).

## Verification
The standalone standard-library verifier `verify.py` enumerates every face of each closed-neighborhood simplex, makes precisely the proposed free-face removals, and checks **all** remaining cofaces at every collapse, not just codimension one. It independently reconstructs \(G\cup\bigcup_Q\partial\Delta^3(Q)\), checks that square diagonals have unique owners, and computes reduced simplicial homology over \(\mathbb F_2\). It covers cycles of lengths five, six and eight; hypercubes in dimensions three through five; ordinary rectangular tori of sizes five-by-five and five-by-six; twisted Klein grids of the same sizes; the eleven-vertex Grötzsch graph; and 606 additional random graphs satisfying the hypotheses. The exact recorded output is `verify_output.txt`. The Grötzsch graph returns reduced mod-two Betti numbers \((1,11)\) in dimensions one and two, agreeing with its previously recorded integral torsion profile. The two twisted grids return mod-two Betti numbers \((\beta_1,\beta_2)=(2,26)\) and \((2,31)\), in agreement with the theorem. These are checks of finite instances, not the infinite proof; the latter is Steps 1–6.

## Relationship to prior work
Matsushita introduced systematic connections of closed-neighborhood complexes with graph fundamental groups and other topological constructions in 2025 [1]. Adams, Shukla and Singh already calculated the scale-two Čech complexes of binary hypercube graphs [2]; those examples are **not** claimed as new. Other established results identify square-sphere contributions for products of graphs of girth at least five and for graphs with pairwise edge-disjoint four-cycles [3–4]. The present result goes beyond these by permitting arbitrary overlap of distinct four-cycles along single edges; its twisted-grid example has integral first-homology torsion that cannot occur in the known product-of-graphs and edge-disjoint-square wedge classifications. A previously reported finite computation detects \(\mathbb Z/2\) in first homology of the Grötzsch graph’s scale-two Čech complex [5]; the present theorem does not claim this is the first example of torsion, and the verifier recovers its mod-two ranks. Related results for **open** neighborhood complexes and higher-scale Vietoris–Rips complexes do not imply a closed-neighborhood square-completion splitting.

## Limitations
The graphs must be triangle-free and have no vertex pair with three or more common neighbors. The wedge splitting is nonequivariant and noncanonical. The theorem does not classify homotopy types of all square completions, although it gives an exact functorial-looking reduction of the closed-neighborhood topology to a finite square complex; neither full functoriality nor a universal equivariant splitting is claimed. The computational tests do not replace the proof. The comparison with literature is limited by the accessibility of some full-text sources; coincident equivalent results not identified in the sources remain possible. No independent external mathematical review has been performed.

## References
[1] Takahiro Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608, first public version November 16, 2025, https://arxiv.org/abs/2511.12608.

[2] Henry Adams, Samir Shukla and Anurag Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871, December 12, 2022, https://arxiv.org/abs/2212.05871; Homology, Homotopy and Applications, 2025.

[3] *A high-girth prism Čech collapse and its integral symmetry module*, publicly indexed mathematical research record, October 2026. Restricted to prisms of high-girth factors.

[4] *Square-localized spheres in closed-neighborhood complexes*, mathematical research result, November 2026. Restricted to pairwise edge-disjoint squares.

[5] *Integral two-torsion in the scale-two graph Čech nerve of the Grötzsch graph*, publicly indexed mathematical research record, October 2026. An exact finite calculation, not an arbitrary-codegree-two homotopy splitting.

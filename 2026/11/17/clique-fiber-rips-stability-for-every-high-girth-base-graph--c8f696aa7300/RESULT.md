# Clique-fiber Rips stability for every high-girth base graph

## Finding
Let \(H\) be a finite connected simple graph with at least one edge and girth at least seven (trees have infinite girth), and let \(m\ge3\) be an integer. Give the Cartesian graph product \(P=H\square K_m\) its unit-edge shortest-path metric. Its inclusive scale-two Vietoris–Rips simplicial complex admits an explicit sequence of elementary simplicial collapses **onto the particular fixed-color copy of \(H\)**:
\[
\operatorname{VR}_{\le2}(P)\searrow H\times\{0\}.
\]
Consequently, with \(b=|E(H)|-|V(H)|+1\), its integral homotopy type is \(\bigvee^b S^1\) (a point when \(b=0\)). The inclusion from the scale-one Rips complex has a primitive, split-surjective map in integral first homology,
\[
\mathbb Z^{m|E(H)|-|V(H)|+1}\longrightarrow
\mathbb Z^{|E(H)|-|V(H)|+1},
\]
whose kernel has rank exactly \((m-1)|E(H)|\). Thus all additional fiber-induced circles disappear at scale two while every base-graph circle survives; no positive-dimensional higher integral homology occurs at that scale.

More precisely, if \(d_H(v)\) is the degree of \(v\), one explicit complete collapse uses exactly
\[
\boxed{m2^{m-1}\sum_{v\in V(H)}\bigl(2^{d_H(v)}-d_H(v)-1\bigr)
+|E(H)|\bigl(2^{2m-1}-2^m\bigr)
+|V(H)|\bigl(2^{m-1}-1\bigr)}
\]
elementary face/coface pairs. The no-six-cycle condition is sharp for a uniform all-base statement: already \(H=C_6\) has \(\operatorname{VR}_{\le2}(K_m\square C_6)\simeq\bigvee^{2m-1}S^2\).

## Assumptions and scope
Vertices of \(P\) are pairs \((v,a)\) with \(v\in V(H)\) and \(a\in\{0,\ldots,m-1\}\). Distances satisfy
\[
d_P((v,a),(w,c))=d_H(v,w)+\mathbf1_{a\ne c}.
\]
Every finite set with pairwise distance at most two is a Rips simplex, including its subsets. The complex is finite and abstract; no geometric realization of graph edges is used in the metric. Fix the color \(0\) throughout. For \(v\in V(H)\), let \(F_v=\{(v,a):0\le a<m\}\), and for \(uv\in E(H)\) write \(A_{uv}=F_u\cup F_v\). For each \(v,a\), put \(B_{v,a}=F_v\cup\{(u,a):u\in N_H(v)\}\). Here \(\Delta(S)\) denotes the full simplex on \(S\).

## Proof
**1. All Rips faces have explicit carriers.** Every \(\Delta(A_{uv})\) and \(\Delta(B_{v,a})\) is a Rips simplex by the product-distance formula. Conversely, consider a Rips face \(\sigma\) and its projection \(Q\) to \(V(H)\). All projected pairwise distances are at most two. If every two distinct vertices of \(Q\) are adjacent, triangle-freeness implies \(|Q|\le2\); thus \(\sigma\subseteq A_{uv}\) for some edge \(uv\), with connectedness and the existence of an edge handling singleton supports.

Otherwise choose \(x,y\in Q\) at distance two. They have a unique common neighbor \(v\), because two different intermediates would form a four-cycle. Every \(z\in Q\) is within distance two of both \(x\) and \(y\). The union of the two length-at-most-two geodesics from \(z\) to \(x,y\) and the path \(x-v-y\) is a closed walk of length at most six. If \(z\notin N_H[v]\), that union would contain a cycle of length at most six: in an acyclic union, its unique path from \(x\) to \(y\) would run through \(v\) and the distance constraints would force \(z\in N_H[v]\). Hence \(Q\subseteq N_H[v]\). Distinct vertices of \(Q\setminus\{v\}\) are nonadjacent, because a triangle with \(v\) is forbidden. Their colored representatives must therefore all have the same color \(a\): different colors would raise their product distance from two to three. Representatives over \(v\) can have any color. Consequently \(\sigma\subseteq B_{v,a}\). We have proved the exact carrier identity
\[
\operatorname{VR}_{\le2}(P)=
\bigcup_{uv\in E(H)}\Delta(A_{uv})\ \cup\
\bigcup_{v\in V(H),\,0\le a<m}\Delta(B_{v,a}).
\]

**2. Delete the private branch faces by elementary collapses.** Fix \((v,a)\), set \(p=(v,a)\), \(N_{v,a}=\{(u,a):u\in N_H(v)\}\), and let \(R=F_v\setminus\{p\}\). For each \(T\subseteq N_{v,a}\) with \(|T|\ge2\) and each \(D\subseteq R\), pair the lower face \(T\cup D\) with \(T\cup D\cup\{p\}\), in decreasing order of lower-face cardinality. The two or more neighbor-column vertices in \(T\) have a unique common base neighbor \(v\), so neither face appears in a different branch carrier or in any edge carrier. Faces from different such matchings are disjoint. All larger private cofaces of a lower face have been removed first, so its unique remaining codimension-one coface is precisely the displayed upper face. Each pair is therefore a legal elementary simplicial collapse. There are \(2^{m-1}(2^{d_H(v)}-d_H(v)-1)\) pairs at each \((v,a)\). Removing all of them leaves exactly
\[
U=\bigcup_{uv\in E(H)}\Delta(F_u\cup F_v).
\]
The first-stage pair count is the first term in the boxed formula.

**3. Remove the extra colors without altering the base graph.** In \(U\), for any \(a\ne0\), the vertex \((v,a)\) is dominated by \((v,0)\): every maximal simplex containing \((v,a)\) is some edge carrier \(\Delta(F_v\cup F_u)\), which also contains \((v,0)\). A dominated vertex can be removed by matching every face containing \((v,a)\) but not \((v,0)\) with its extension by \((v,0)\), descending in face cardinality. Each is an elementary collapse; iterating over all \(v\) and all \(a\ne0\) leaves precisely the graph \(H\times\{0\}\), as a subcomplex. The number of faces of \(U\), including the empty face, is
\[
1+|V(H)|(2^m-1)+|E(H)|(2^{2m}-2^{m+1}+1),
\]
because different edge carriers intersect only in whole common fiber simplices. The graph target has \(1+|V(H)|+|E(H)|\) faces including the empty face. Their difference, divided by two, yields the second and third terms in the boxed count. This proves the integral simplicial-collapse statement, not merely a homology computation.

**4. Integral first-scale persistence.** At scale one, triangles occur only inside the filled fiber simplices \(\Delta(F_v)\) (because \(H\) has no triangles). The remaining edges are exactly the \(m\) same-color copies of each base edge. Contracting the contractible filled fibers gives a connected multigraph having \(m\) parallel edges over each edge of \(H\); therefore
\[
H_1(\operatorname{VR}_{\le1}(P);\mathbb Z)
\cong\mathbb Z^{m|E(H)|-|V(H)|+1},
\]
and there is no higher reduced homology. The fixed-color graph \(H\times\{0\}\) includes into scale one, then into scale two, and its final inclusion is a homotopy equivalence by Steps 2–3. Thus the scale-one-to-two map on integral first homology has a section induced by the fixed-color graph and a free, primitive kernel of the stated rank. Its cokernel vanishes and its image is all of \(\mathbb Z^b\), with no torsion hidden by field computations.

**5. Sharpness and distinctiveness.** In the six-cycle base, the previously established clique-fiber cyclic calculation gives a wedge of \(2m-1\) two-spheres at scale two, so the theorem cannot uniformly replace girth seven by six. By contrast, the graph Čech nerve at scale two for this same high-girth clique-fiber family is known to have an additional \((m-1)^2\) two-spheres for each base edge. The two constructions cannot be conflated: the Rips carrier \(\Delta(F_u\cup F_v)\) is a full simplex, whereas the Čech edge block need not be. In the Rips complex the extra Čech two-dimensional classes vanish.

## Verification
Run `python3 verify_clique_fiber_rips.py` using only the Python standard library. The independently generated shortest-path Rips face set is compared with the union of carrier simplices. Every proposed elementary collapse is tested against every existing immediate coface; the two expected residual complexes are compared as complete face sets. The executable covers 22 cases of paths, a four-leaf star, cycles of lengths seven through nine, a girth-eight theta graph with shared poles, and two seven-cycles sharing one vertex, using two, three, and four fiber colors. Its recorded final line is `VERIFY_OK 22 complete independent face-cover and elementary-collapse certificates`. These finite checks support but do not replace the all-parameter argument above.

## Relationship to prior work
Adams, Adetowubo, Barriga-Acosta, Feng and Sterling examine graph-metric torus-grid Vietoris–Rips complexes, including a small-scale homotopy-recovery regime; their graph factors are cyclic and do not imply the arbitrary-base clique-fiber theorem. A published high-girth prism result proves the two-color case \(H\square K_2\), already acknowledged and excluded from the new parameter range. A published clique-fiber cycle theorem treats \(H=C_n\), including the sharp six-cycle counterexample; it cannot cover noncycle bases such as trees with branching, theta graphs, or two intersecting long cycles. A published high-girth clique-fiber **Čech** calculation treats the same Cartesian graph family but a different simplicial complex, and gives extra two-dimensional homology not present here. The new assertion is the simultaneous unbounded-width, arbitrary-high-girth-base Rips collapse, its exact face-pair count, and its primitive integral scale-one map. Relevant broader literature and bounded priority risks are discussed in the accompanying review.

## Limitations
The statement assumes finite connected simple base graphs of girth at least seven and at least one edge, clique width at least three, the graph's unit-edge shortest-path metric, and inclusive scale two. It does not classify radii above two or arbitrary graph-product factors, nor claim the girth threshold is necessary for each individual graph. No claim of canonical equivariance under the full fiber-permutation action is made: a fixed color is selected. The computations test finitely many small cases only; the proof is the source of the unbounded conclusion.

## References
1. H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng, J. Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134, first public 2025-02-10, https://arxiv.org/html/2502.07134v2 (Sections 1–3 and 5 inspected).
2. *A uniform scale-two Vietoris–Rips collapse for prisms over graphs of girth at least seven*, published research record 4061be6b33be, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-uniform-scale-two-vietoris-rips-collapse-for-prisms-over-graph--4061be6b33be/RESULT.md (width-two boundary).
3. *A sharp one-circle-to-sphere-wedge transition for clique-fiber cyclic Rips complexes*, published research record e28e5da49d34, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-a-sharp-one-circle-to-sphere-wedge-transition-for-clique-fiber-c--e28e5da49d34/RESULT.md (cycle-only family and girth-six boundary).
4. *Clique-fiber Čech nerves over graphs of girth at least five*, published research record bcf5b8b96c75, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-clique-fiber-ech-nerves-over-graphs-of-girth-at-least-five--bcf5b8b96c75/RESULT.md (different nerve construction).
5. M. Adamaszek et al., *Vietoris–Rips and Čech Complexes of Metric Gluings*, SoCG 2018, https://doi.org/10.4230/LIPIcs.SoCG.2018.3 (metric-gluing framework, different hypotheses).

# Rooted furtherness persistence of graph incidence spaces detects local triangles

## Finding
Let \(G=(V,E)\) be any finite, connected, simple, undirected graph with \(n=|V|\ge2\), \(m=|E|\), and \(\beta=m-n+1\). Form the height-two **incidence poset** \(P(G)=V\sqcup E\), in which \(v<e\) precisely when \(v\) is an endpoint of \(e\). Give it the lower Alexandrov topology, so \(U_x=\downarrow x\). For any root \(x\in P(G)\), set
\[
F_x(t)=\Delta\bigl(\{y\in P(G):|U_y\setminus U_x|\le t\}\bigr),\qquad t\in\mathbb R,
\]
where \(\Delta\) is the order complex and sublevels are inclusive. Persistence is ordinary, unreduced homology over any field \(\mathbb K\), with bars \([b,d)\), ignoring zero-length intervals.

**Complete barcode theorem.** For a vertex root \(v\) of degree \(d_v\),
\[
\begin{aligned}
\mathrm{Dgm}_0(F_v)&=\{[0,\infty)\}\sqcup d_v\{[1,2)\}\sqcup(n-1-d_v)\{[1,3)\},\\
\mathrm{Dgm}_1(F_v)&=\beta\{[3,\infty)\}.
\end{aligned}
\]
For an edge root \(e=uv\), let \(c_e=|N_G(u)\cap N_G(v)|\) and \(k_e=d_u+d_v-2-c_e\). Then
\[
\begin{aligned}
\mathrm{Dgm}_0(F_e)&=\{[0,\infty)\}\sqcup k_e\{[1,2)\}\sqcup(n-2-k_e)\{[1,3)\},\\
\mathrm{Dgm}_1(F_e)&=c_e\{[2,\infty)\}\sqcup(\beta-c_e)\{[3,\infty)\}.
\end{aligned}
\]
All barcodes in degrees \(j\ge2\) are empty. A coefficient of zero means no bars of that type.

**Recovery and indistinguishability.** The vertex-root degree-zero barcode records \(d_v\), while the edge-root degree-one barcode records the number \(c_e\) of triangles through \(e\). Hence the complete root-type-tagged profile recovers \(n\), \(m\), the degree sequence, the edge common-neighbor multiset, and the global triangle count \(\frac13\sum_{e\in E}c_e\). Conversely, the diagrams of a given root depend only on the displayed parameters. The Petersen graph and the pentagonal prism are nonisomorphic, connected, triangle-free cubic graphs with \(n=10\), \(m=15\), and \(\beta=6\). Their full **multisets** of rooted barcodes agree, but their incidence posets are not homotopy equivalent as finite Alexandrov spaces.

## Assumptions and scope
Graphs have no loops, parallel edges, or isolated vertices and are connected; the lower bound \(n\ge2\) includes the single-edge graph. A vertex root and an edge root are distinct kinds of poset elements. The topological claim is about their **order-complex filtrations**; the finite-space nonhomotopy claim uses ordinary Stong homotopy of finite \(T_0\)-spaces, which is stronger than weak homotopy equivalence of order complexes. No geometric edge lengths or graph-metric Rips construction occurs. For \(t<0\) the complex is empty; at \(t\ge3\) it is the full graph subdivision. All homology is torsion-free at each stage; interval statements hold over every coefficient field.

## Proof
**1. Exact furtherness weights.** The principal lower sets are \(U_v=\{v\}\) and \(U_{uv}=\{u,v,uv\}\). For vertex root \(v\), its own weight is zero, every other graph vertex has weight one, any graph edge incident to \(v\) has weight two, and any other edge has weight three. For edge root \(e=uv\), the points \(u,v,e\) have weight zero, every other graph vertex has weight one, any other edge incident to \(u\) or \(v\) has weight two, and every edge disjoint from \(\{u,v\}\) has weight three. These are exhaustive because the graph is simple.

**2. Order complex is an actual graph subdivision.** Each strict chain consists of a graph vertex below an incident graph edge; there are no strict chains of length three. Thus \(\Delta(P(G))\) is the graph obtained by subdividing every edge of \(G\) once. Every stage is a subgraph of this subdivision. Its first homology is a free cycle lattice, each inclusion induces an injection on \(H_1(-;\mathbb Z)\), and there are no higher-dimensional chain groups. In particular, positive-degree classes never die.

**3. Vertex-root filtration.** At time zero there is one vertex. At time one all \(n\) graph vertices are present as isolated vertices. At time two the edges incident to \(v\), together with their subdivision vertices, form a star. This connects the root component to its \(d_v\) neighbors, killing exactly \(d_v\) classes born at time one; it creates no cycle. At time three the whole subdivision graph appears. Connectedness kills the remaining \(n-1-d_v\) degree-zero classes; its first Betti number is \(\beta\). All \(\beta\) essential degree-one classes therefore begin at time three.

**4. Edge-root filtration.** At time zero \(u,e,v\) already form a path, hence one component. At time one the other \(n-2\) vertices appear separately. At time two, among original graph edges, precisely those touching \(u\) or \(v\) have appeared. They form a double star joined by \(uv\). Its non-root vertices comprise exactly \(k_e=|\bigl(N(u)\cup N(v)\bigr)\setminus\{u,v\}|=d_u+d_v-2-c_e\) distinct graph vertices. Each joins the root component, killing one time-one degree-zero class. Any common neighbor \(w\in N(u)\cap N(v)\) gives the extra edge that closes the triangle \(u-v-w-u\); choosing one incident edge to each non-root vertex gives a spanning tree of the nonisolated component, and the remaining \(c_e\) edges are independent fundamental cycles. Consequently, exactly \(c_e\) degree-one classes are born at time two. At time three all missing graph edges arrive, joining the remaining \(n-2-k_e\) isolated vertices and adding exactly \(\beta-c_e\) further cycles; none of the earlier cycles is killed. This proves the formulas, including all boundary cases.

**5. Nonseparation of two finite spaces.** Both the Petersen graph and pentagonal prism are cubic, triangle-free, on ten vertices; each has fifteen edges and cycle rank six. Substitution into the complete formula gives identical root-type-tagged multisets: ten copies of the vertex-root barcode with \(3\) bars \([1,2)\), \(6\) bars \([1,3)\), and \(6\) first-homology bars \([3,\infty)\); and fifteen copies of the edge-root barcode with \(4\) bars of each of the two finite kinds and the same six essential first-homology bars. The pentagonal prism has a four-cycle, whereas the Petersen graph has none, so they are not isomorphic. Since every graph vertex has degree three, each minimal poset point has at least two incomparable strict upper elements; each maximal point has two incomparable strict lower elements. Neither incidence poset has a beat point. Stong's finite-space core theorem and the graph reconstruction from the incidence relation imply that two such spaces are homotopy equivalent only when their graphs are isomorphic. Therefore these two finite spaces are not homotopy equivalent even though their complete rooted barcodes agree.

## Verification
Run `python3 verify.py` with a standard Python 3 installation. The self-contained program constructs the poset and its principal opens from edges, assigns filtration times by literal set differences, builds every filtration simplex independently, and computes persistent \(H_0\) and \(H_1\) by incremental graph reduction. It checks the theorem on all connected labeled simple graphs with two through five vertices, plus seeded graphs with six through nine vertices. In the recorded replay there were 1,100 connected test graphs and 14,946 graph-root tests. It independently checks the ten-vertex Petersen/prism equality and their four-cycle distinction; the output is `VERIFY_OK`. Finite tests are corroboration only: the all-graph proof above relies on exact set/cardinality and cycle-lattice arguments, not exhaustive testing.

## Relationship to prior work
Badra and Singh (arXiv:2610.16386v1, first public 12 October 2026) define the rooted furtherness filtration and investigate degree-zero persistence and general component-merger principles. They do not give the full all-degree, graph-specific formula or edge-root local-triangle characterization. A publicly available calculation, *Complete furtherness barcodes of Steiner incidence spaces* (25 October 2026), provides complete barcodes for Steiner \(2\)-design incidence posets. Its special case of block size two corresponds to the complete graph \(K_n\), and is **covered** by the present arbitrary-connected-graph formula; the earlier complete-graph case is not claimed as new. Its formula for general larger blocks does not imply the heterogeneous-degree or edge-common-neighbor results for arbitrary simple graphs. The note *Graph 2-cores classify Stong cores of incidence posets* (4 October 2026) already supplies the finite-space homotopy classification by graph 2-core, which is credited rather than reproved as a new general theorem; here it is applied to a new barcode collision. General graph persistence and Stong theory are standard ingredients, but they do not state the specific all-root furtherness classification and local-triangle detection.

## Limitations
The result concerns height-two incidence posets of **simple connected** graphs and the specified lower Alexandrov furtherness; it does not extend unchanged to multigraphs, hypergraphs, arbitrary height-two posets or graph-metric persistent homology. The barcode profile is an incomplete graph-isomorphism invariant. The example proves nonhomotopy-equivalence of the finite spaces, not different weak homotopy types of their order complexes (both order complexes are wedges of six circles). Independent mathematical review and exhaustive publication-priority certification are not performed, and equivalent unindexed formulations remain possible.

## References
1. A. Badra and H. K. Singh, *Persistence diagrams of finite topological spaces*, arXiv:2610.16386v1, first posted 12 October 2026, especially Definitions 2.6 and Sections 3–4. https://arxiv.org/abs/2610.16386
2. *Complete furtherness barcodes of Steiner incidence spaces*, public research note dated 25 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-complete-furtherness-barcodes-of-steiner-incidence-spaces--f241a0823713
3. *Graph 2-cores classify Stong cores of incidence posets*, public research note dated 4 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-graph-2-cores-classify-stong-cores-of-incidence-posets--2eb6df597d95
4. R. E. Stong, *Finite topological spaces*, Transactions of the American Mathematical Society 123 (1966), 325–340 (finite-space beat points and core uniqueness).

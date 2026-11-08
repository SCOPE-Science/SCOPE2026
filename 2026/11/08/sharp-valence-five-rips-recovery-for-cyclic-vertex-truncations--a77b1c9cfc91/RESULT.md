# Sharp valence-five Rips recovery for cyclic vertex truncations

## Finding

**Theorem (Rips recovery, integral persistence, and sharp degree bound).** Let \(H\) be a finite connected simple triangle-free graph with at least one edge, vertex set \(V(H)\), and maximum degree at most five. Give the incident half-edges at each vertex any cyclic ordering. Replace each vertex of degree \(d\geq3\) by a chordless \(d\)-cycle through its incident half-edges, replace vertices of degree two by a single edge and vertices of degree one by a point, and join the two ports belonging to each original edge by an external edge. Call the resulting finite graph \(T=T_{\mathrm{cyc}}(H)\). All edge lengths are one and all Rips scales refer to the **vertex-set shortest-path metric**, with inclusive threshold.

The simplicial map from the scale-two Rips complex to \(H\), assigning each port to its original vertex,
\[
 p:\operatorname{VR}_{\leq2}(T)\longrightarrow H,
\]
is a homotopy equivalence. Writing \(n=|V(H)|\), \(m=|E(H)|\), and \(q=|\{v\in V(H):\deg_H(v)\in\{4,5\}\}|\), the two initial Rips stages satisfy
\[
 \operatorname{VR}_{\leq1}(T)\simeq\bigvee^{m-n+1+q}S^1,
 \qquad
 \operatorname{VR}_{\leq2}(T)\simeq\bigvee^{m-n+1}S^1.
\]
The inclusion induces a surjection on integral first homology with the canonical primitive kernel
\[
 0\longrightarrow\bigoplus_{\substack{v\in V(H)\\\deg_H(v)\in\{4,5\}}}
 \mathbb Z[\gamma_v]\longrightarrow H_1(\operatorname{VR}_{\leq1}(T);\mathbb Z)
 \longrightarrow H_1(\operatorname{VR}_{\leq2}(T);\mathbb Z)\longrightarrow0,
\]
where \(\gamma_v\) is the oriented local port cycle. There is no integral torsion or positive-degree homology beyond degree one at either scale. This applies for **every choice of local cyclic orders**.

The degree bound is sharp for a uniform theorem: when \(H=K_{1,6}\), the scale-two Rips complex of its cyclic truncation is homotopy equivalent to \(S^2\), whereas \(H\) is contractible.

For example, the cyclic truncation of \(H=C_a\square C_b\) for \(a,b\geq4\) has \(\operatorname{VR}_{\leq2}(T)\simeq\bigvee^{ab+1}S^1\), and the scale-one-to-two first-homology kernel has rank \(ab\). The corresponding ranks for the cyclic truncation of \(K_{5,5}\) are \(26\) at scale one and \(16\) at scale two.

## Assumptions and scope

A *port* is the ordered pair \((v,w)\) associated with an original edge \(vw\). For each \(v\), write \(C_v=\{(v,w):vw\in E(H)\}\). When \(\deg_H(v)=d\), order these \(d\) ports cyclically. Inside \(C_v\), insert the edges of the cycle if \(d\geq3\), the sole pair if \(d=2\), and no edges if \(d=1\); in addition insert the reversal edge \((v,w)(w,v)\) for every \(vw\). These are *all* edges of \(T\). Thus every port lies on exactly one external edge, and the sets \(C_v\) are disjoint. The original graph \(H\) is viewed as a one-dimensional simplicial complex, not as its clique complex; triangle-freeness makes this unambiguous. The complex \(\operatorname{VR}_{\leq r}(T)\) is the flag complex whose edges join distinct ports of distance at most \(r\) in \(T\). We use integral homology and ordinary geometric homotopy equivalence; no assertions about other scales or metric realizations of the edges are made.

## Proof

**1. The projection is simplicial.** The graph map sending \((v,w)\) to \(v\) takes every internal edge to one vertex and every reversal edge to an edge of \(H\). Every shortest path between distinct ports of length at most two in \(T\) contains at most one reversal edge, because the reversals form a matching. Therefore any adjacent pair in the second power of \(T\) projects either to the same vertex of \(H\) or to two adjacent vertices of \(H\). If \(\sigma\) is a simplex of the scale-two Rips complex, its set of projection vertices is a clique of \(H\). Since \(H\) is triangle-free, it contains at most two vertices. This proves that \(p\) is a simplicial map \(\operatorname{VR}_{\leq2}(T)\to H\).

**2. Fibers over original vertices.** For each original vertex \(v\), the full subcomplex on \(p^{-1}(v)=C_v\) is a simplex. Indeed, the port fiber is a point, an edge, or a cycle of length three, four or five, all of diameter at most two. Thus the inverse image of the closed vertex simplex \(\{v\}\) is contractible. This is the only place where the degree bound five is needed in the positive theorem.

**3. Fibers over original edges.** Fix \(uv\in E(H)\), and put \(a=(u,v)\), \(b=(v,u)\). We claim the full subcomplex \(F_{uv}\) on \(C_u\cup C_v\) strongly collapses to the edge \(ab\). Within either fiber all its vertices are mutually Rips-adjacent by Step 2. Between the fibers, a path of length at most two must traverse their **unique** reversal edge \(ab\), hence a mixed Rips edge is precisely one of the following: \(ab\); \(xb\) when \(x\in C_u\) is internally adjacent to \(a\); or \(ay\) when \(y\in C_v\) is internally adjacent to \(b\). In particular, no Rips edge joins \(C_u\setminus\{a\}\) to \(C_v\setminus\{b\}\). Every vertex \(x\in C_u\setminus\{a\}\) is consequently dominated by \(a\) in the one-skeleton of \(F_{uv}\): its closed neighborhood is contained in that of \(a\). For a flag complex, such a dominated vertex can be removed by elementary simplicial collapses (pairing each face containing \(x\) but not \(a\) with its union with \(a\), in descending order). After all these vertices are removed, every vertex of \(C_v\setminus\{b\}\) is likewise dominated by \(b\), so \(F_{uv}\searrow ab\). This also covers degree-one and degree-two endpoints.

**4. Homotopy recovery.** Consider the induced order-preserving map on posets of nonempty faces \(\mathcal F(p):\mathcal F(\operatorname{VR}_{\leq2}(T))\to\mathcal F(H)\). The inverse image of the principal lower ideal of a nonempty simplex \(\tau\) of \(H\) is the face poset of the full subcomplex on \(p^{-1}(\tau)\), which is contractible by Step 2 when \(\tau\) is a vertex and by Step 3 when \(\tau\) is an edge. The poset fiber theorem (Quillen's Theorem A for finite posets, equivalently the simplicial fiber lemma) makes \(\mathcal F(p)\) a homotopy equivalence on order complexes. Order complexes are barycentric subdivisions, so the original simplicial map \(p\) is a homotopy equivalence. Because \(H\) is connected, \(H\simeq\bigvee^{m-n+1}S^1\), giving the integral scale-two statement.

**5. Scale-one topology and integral kernel.** At scale one, \(\operatorname{VR}_{\leq1}(T)=\operatorname{Cl}(T)\). Its only triangles are the complete internal port triangles at vertices of degree three. There are no triangles involving reversal edges, since each port has exactly one external neighbor. Collapse every such filled triangle onto an internal spanning tree, fixing all external reversal edges. Every internal degree-four or degree-five port cycle remains an unfilled cycle, while each degree-one/two/three port fiber becomes a tree. Contract a spanning tree inside every resulting fiber. The resulting one-dimensional CW complex consists of the base graph \(H\) with one additional loop at each degree-four or degree-five vertex. Therefore the first homology is a free abelian group of rank \(m-n+1+q\), and the port-cycle classes form a primitive direct-summand lattice. More precisely, the original port-projection \(p_1:\operatorname{VR}_{\leq1}(T)\to H\) kills exactly these local loops and induces a split surjection on first homology. The identity \(p_1=p\circ\iota\), where \(\iota\) is the Rips scale-one-to-two inclusion, and the integral homology isomorphism \(p_*\) from Step 4 imply \(\ker\iota_* =\bigoplus\mathbb Z[\gamma_v]\) and \(\iota_*\) is surjective. This proves the primitive exact sequence without relying on mod-two rank data.

**6. Sharpness at degree six.** If \(H=K_{1,6}\), the six central ports form the cycle \(C_6\) and the six leaf ports are pendant neighbors. In the distance-two graph, each pendant port has its closed neighborhood contained in that of its adjacent central port. Remove the pendant ports by dominated-vertex collapses. The remaining complex is \(\operatorname{VR}_{\leq2}(C_6)\): its only forbidden vertex pairs are the three antipodal pairs, so it is the join of three two-point discrete complexes, i.e. the boundary of an octahedron \(S^2\). It is not homotopy equivalent to the tree \(H\), establishing sharpness.

## Verification

The standard-library `verify.py` independently constructs all ports and graph edges, squares the graph by explicit length-two walks, enumerates maximal cliques, and obtains integral-independent mod-two boundary ranks by exact bitwise elimination. It checks thirty-nine connected triangle-free examples (including stars, cycles, \(K_{4,4}\), \(K_{5,5}\), the cube, two toroidal grids and seeded irregular bipartite graphs), verifies the projection and local cross-fiber constraints directly from enumerated simplices, and computes the degree-six star obstruction. Every example matched the predicted scale-one and scale-two homology, and the obstruction gave Betti numbers \((1,0,1,0)\). The recorded executable output ends in `CYCLIC_TRUNCATION_RIPS2_CHECKS_OK 39 examples`. These finite checks are corroboration; Steps 1–6 prove the unrestricted assertions and all integral conclusions.

## Relationship to prior work

Adams, Adetowubo, Barriga-Acosta, Feng and Sterling (arXiv:2502.07134, first public 2025-02-10, §5) prove small-scale graph-metric Rips recovery for the *original* sufficiently large rectangular torus grids. Here the metric graph is a distinct **cyclic vertex truncation** of the original base, including arbitrary triangle-free graphs of maximum degree five, arbitrary cyclic orderings, a sharp degree-six obstruction and a primitive integral persistence kernel. The torus-grid theorem does not imply these assertions. Bendersky, Elia and Grbić (arXiv:2605.00705, first public 2026-05-01) study cohomology of Rips complexes of binary hypercube graphs, a different metric family and invariant.

A closely related published result, *Scale-three Čech persistence survives vertex truncation of triangle-free graphs* (2026-10-11, linked in the references), treats the **vertex-centered intrinsic Čech nerve** of the line graph of the once-subdivision \(L(S(H))\). There the local fibers are complete graphs (all ports mutually adjacent already at scale one) and the theorem concerns Čech scales two and three. The present graph instead has **chordless cyclic fibers at degrees four and five**, and its invariant is the **graph-metric Vietoris–Rips** complex at scale two, with a nonzero integral scale-one-to-two kernel precisely in those degrees. The published statement does not imply the present one, nor does the general line-graph clique-complex equivalence of Goyal, Shukla and Singh (arXiv:2009.12130, Corollary 3.3). General work on Vietoris–Rips complexes of metric gluings requires its own hypotheses and does not provide this cyclic-port calculation as a stated specialization.

## Limitations

The theorem assumes finite connected **triangle-free** base graphs, at least one edge, and maximum degree at most five, with the stipulated simple cyclic-port expansion and unit graph metric. It classifies only scales one and two and does not assert contractibility of individual higher-dimensional attaching maps at larger scales. The proof does not claim the degree-six obstruction occurs for every graph of maximum degree six: it supplies a sharp **failure of a uniform all-graph statement**. The computation is not an independent proof of integral claims, and unrelated higher-scale behavior remains open.

## References

1. H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng, J. Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134v1 (first public 2025-02-10), §5; https://arxiv.org/abs/2502.07134 .
2. M. Bendersky, S. Elia, J. Grbić, *Cohomological properties of the Vietoris–Rips Complex of a Hypercube Graph*, arXiv:2605.00705v1 (first public 2026-05-01); https://arxiv.org/abs/2605.00705 .
3. *Scale-three Čech persistence survives vertex truncation of triangle-free graphs* (2026-10-11), public mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-scale-three-ech-persistence-survives-vertex-truncation-of-triang--050621e1a6fe .
4. S. Goyal, S. Shukla, A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130 (first public 2020-09-25), Corollary 3.3; https://arxiv.org/abs/2009.12130 .
5. M. Adamaszek et al., *Vietoris–Rips and Čech Complexes of Metric Gluings*, SoCG 2018, DOI 10.4230/LIPIcs.SoCG.2018.3; https://doi.org/10.4230/LIPIcs.SoCG.2018.3 .

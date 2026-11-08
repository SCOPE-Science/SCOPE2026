# A uniform scale-two Vietoris–Rips collapse for prisms over graphs of girth at least seven

## Finding
For every finite connected simple graph \(H\) with at least one edge and girth at least seven, the inclusive graph-metric Vietoris–Rips complex at radius two of its prism \(P=H\square K_2\) collapses simplicially to a triangulation of \(|H|\times[0,1]\). Thus
\[
\operatorname{VR}_{\le2}(P)\simeq H,
\qquad \widetilde H_i(\operatorname{VR}_{\le2}(P);\mathbb Z)
\cong \begin{cases}
\mathbb Z^{|E(H)|-|V(H)|+1},&i=1,\\
0,&i\ne1.
\end{cases}
\]
An explicit schedule contains exactly
\[
4\sum_{v\in V(H)}(2^{\deg_H(v)}-\deg_H(v)-1)+2|E(H)|
\]
elementary collapse pairs. This result covers arbitrary degrees and noncactus graphs, including theta graphs with shared paths.

## Assumptions and scope
All graphs are finite, connected, simple, and unweighted; a tree has infinite girth. Write \(v^a=(v,a)\) for \(a\in\{0,1\}\). The metric is shortest-path distance on the prism, not Euclidean distance, and a finite set is a simplex if every distance is at most two. The empty face is conventional but is not counted among the elementary collapse pairs. For edges \(uv\in E(H)\), choose any fixed ordering of endpoints \(u<v\).

## Proof
**1. Complete classification of simplices.** In the product metric,
\[d_P(u^a,v^b)=d_H(u,v)+|a-b|.\]
Let \(N_H[v]\) denote a closed graph neighborhood. Define the full simplices
\[
K_{v,a}=\Delta\big(\{v^0,v^1\}\cup\{u^a:u\in N_H(v)\}\big),\quad
F_{uv}=\Delta\{u^0,u^1,v^0,v^1\}\ (uv\in E(H)).
\]
We show these simplices cover the entire Vietoris–Rips complex. For one layer, a set with pairwise base-graph distances at most two is contained in some closed neighborhood of \(H\). Indeed, if it has a pair at distance two, their unique intermediate vertex is the only possible common center for every other member: a different connecting path of length at most two would create a cycle of length at most six. If all pairs are adjacent, the triangle-free condition makes the set have size at most two, so it lies in a closed neighborhood. If a simplex spans both layers, let \(A,B\subseteq V(H)\) be its base-vertex sets in layers zero and one. Every crossing pair has base distance at most one. If \(|A|\ge2\) and \(|B|=1\), its vertices lie in a suitable \(K_{v,a}\); similarly with layers swapped. If both cardinalities are at least two, choose distinct \(x,y\in A\). Their common closed neighborhood contains at most one point when \(d_H(x,y)=2\), and equals \(\{x,y\}\) when \(xy\in E(H)\), since the graph has no triangles or four-cycles. Thus \(A=B=\{x,y\}\) with \(xy\) an edge, and the simplex lies in \(F_{xy}\). The remaining cardinality cases are immediate.

**2. Private neighbor-pair collapse.** Fix a vertex \(v\) and layer \(a\), put \(B_{v,a}=\{u^a:u\in N_H(v)\}\), \(p=v^a\), and \(q=v^{1-a}\). For every subset \(T\subseteq B_{v,a}\) of cardinality at least two, and each \(\varepsilon\in\{0,1\}\), match the face \(\sigma=T\cup(\{q\}\text{ if }\varepsilon=1\text{ else }\varnothing)\) with \(\sigma\cup\{p\}\). Process these pairs by decreasing cardinality of the lower face, breaking ties arbitrarily. Such a lower face is private to \(K_{v,a}\): its two distinct neighbor vertices in one layer have distance two and the unique common neighbor \(v\), and the girth assumption excludes any competing clique with that pair outside \(K_{v,a}\). All larger private faces were previously removed, so the indicated upper face is the *only remaining proper coface* of the lower one at the time of removal. Hence every pair is an elementary simplicial collapse. No pair is repeated between different vertices or layers. This step deletes precisely the faces of \(K_{v,a}\) with at least two vertices from \(B_{v,a}\), leaving each \(F_{uv}\) intact. There are \(2(2^{\deg v}-\deg v-1)\) pairs for each \((v,a)\), giving \(4\sum_v(2^{\deg v}-\deg v-1)\) pairs in total.

**3. Tetrahedra to squares.** What remains is exactly \(\bigcup_{uv\in E(H)}F_{uv}\), with different tetrahedra intersecting in at most a rung edge. For each ordered edge \(u<v\), first collapse \(F_{uv}\) with its triangular face \(\{u^1,v^0,v^1\}\); next collapse the remaining triangle \(\{u^0,u^1,v^0\}\) with the private edge \(\{u^1,v^0\}\). Both are free-face pairs, independently of all other edges. The two surviving triangles are \(\{u^0,v^0,v^1\}\) and \(\{u^0,u^1,v^1\}\), a standard triangulation of the square over the edge \(uv\). The total is therefore the triangular-square product \(|H|\times[0,1]\), which deformation retracts onto \(|H|\). There are two extra collapse pairs per edge, proving the formula and the integral homotopy statement.

**4. Boundary of the hypothesis.** The six-cycle prism \(C_6\square K_2\) is known to have scale-two Rips complex with nontrivial second homology (indeed three two-spheres), so girth six cannot be admitted uniformly. The theorem makes no claim that every individual graph of smaller girth fails.

## Verification
Run `python3 verify_high_girth_prism.py`; it requires only Python's standard library. It constructs the full graph-metric Rips complex independently, tests the exact clique cover, then checks every proposed collapse against *all currently remaining proper cofaces*, and finally compares the residual face set with the prescribed two-triangle-per-edge product. The supplied log records 165 passing cases: all 146 labeled trees with one through five vertices, further paths, stars and cycles of lengths six through eleven where admissible, two septagons joined by a bridge, and a three-arm theta graph with arms of length four. The theta example verifies genuinely overlapping cycles. The proof above, not these finite tests, establishes the assertion for all finite graphs satisfying the hypotheses.

## Relationship to prior work
Adams, Adetowubo, Barriga-Acosta, Feng and Sterling study graph-metric Vietoris–Rips complexes of torus grids and describe the graph-power clique-complex viewpoint; their 2025 paper does not assert this arbitrary-base, girth-controlled prism collapse in the inspected introduction and graph-definition sections. A published circular-ladder classification establishes the special case \(H=C_n\) for \(n\ge7\), but its indexed claim is limited to cycles and therefore does not imply the present result for arbitrary high-girth graphs. A separate high-girth **Čech**-prism calculation yields extra two-spheres and concerns a different simplicial complex. General graph-metric gluing results use different decomposition hypotheses. Source-access limitations and possible alternate formulations are recorded in the scientific review.

## Limitations
The conclusion concerns the inclusive **radius-two** graph-metric Rips complex, finite simple graphs of girth at least seven, and ordinary nonequivariant simplicial collapses. It does not classify higher radii, arbitrary graph products, shorter-girth graphs individually, or naturality under arbitrary graph maps. The general result is a simplicial collapse onto a triangulated product, not a simplicial isomorphism to the original graph.

## References
- H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng, J. Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134, first submitted 2025-02-10; Sections 1 and 3.5 consulted.
- *Scale-two Rips homotopy types of finite circular ladders*, published research record ccd7a360a668 (specialization to cycles).
- *A high-girth prism Čech collapse and its integral symmetry modules*, published research record e4f536ceab68 (different nerve construction).
- *Vietoris–Rips and Čech Complexes of Metric Gluings*, SoCG 2018, DOI:10.4230/LIPIcs.SoCG.2018.3.

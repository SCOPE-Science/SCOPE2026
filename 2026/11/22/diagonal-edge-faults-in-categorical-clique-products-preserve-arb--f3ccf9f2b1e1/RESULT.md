# Diagonal edge faults in categorical clique products preserve arbitrary flag-complex topology

## Finding

Let \(H\) be **any** finite simple graph on the ordered vertex set \([n]=\{1,\ldots,n\}\), with \(n\ge2\). Take the categorical graph product \(B_n=K_n\times K_n\), with vertices \(v_{ij}=(i,j)\) and graph adjacency precisely when **both** coordinates differ. For every edge \(\{i,j\}\in E(H)\), remove the graph edge \(\{v_{ii},v_{jj}\}\), and call the resulting graph \(G_H\). Write \(K=\operatorname{Cl}(H)\) for the flag (clique) complex, \(c\) for the number of connected components of \(H\), and \(q=\binom n2-|E(H)|\).

**Theorem.** The independence complex \(\operatorname{Ind}(G_H)\) simplicially collapses onto the subcomplex \(L_H\) made of the full diagonal clique complex \(K\) on \(v_{ii}\), together with **two separate subdivided edges** from \(v_{ii}\) to \(v_{jj}\) for each nonedge \(\{i,j\}\notin E(H)\). More precisely the two paths are
\[
v_{ii}-v_{ij}-v_{jj},\qquad v_{ii}-v_{ji}-v_{jj}.
\]
There are no other faces in \(L_H\). In particular, if \(K_1,\ldots,K_c\) are the connected components of \(K\), with an arbitrary basepoint chosen in each, then
\[
\boxed{\quad|\operatorname{Ind}(G_H)|\simeq
\left(\bigvee_{a=1}^c|K_a|\right)\vee
\bigvee^{\,2q-c+1} S^1.\quad}
\]
Here the wedge of the \(c\) initially separate components means that their chosen basepoints are identified. The rank \(2q-c+1\) is nonnegative; in particular, when \(H\) is connected it is exactly \(2q\).

**Integral consequence.** All positive-degree integral homology groups of \(K\) persist as direct summands. In degrees \(j\ge2\),
\[
\widetilde H_j(\operatorname{Ind}(G_H);\mathbb Z)\cong\widetilde H_j(K;\mathbb Z),
\]
and
\[
H_1(\operatorname{Ind}(G_H);\mathbb Z)\cong
H_1(K;\mathbb Z)\oplus\mathbb Z^{\,2q-c+1}.
\]
The induced inclusion \(K\hookrightarrow\operatorname{Ind}(G_H)\) realizes the indicated split injection in every positive homology degree, component by component. Therefore higher-dimensional integral torsion or homotopy present in an arbitrary flag complex can survive a structured deletion of graph edges from a categorical complete-graph product, even though the unperturbed independence complex is a wedge of circles.

## Assumptions and scope

All graphs are finite, undirected, loopless and simple; the graph product is categorical/direct, **not** Cartesian. The graph \(H\) may be disconnected or have isolated vertices. \(K\) denotes its simplicial clique complex, including all its nonempty faces. The two paths associated with a nonedge use distinct off-diagonal vertices. A collapse is a sequence of deleting a free codimension-one face together with its unique coface. The homotopy equivalence and integral groups are nonequivariant. No statement is made for arbitrary non-diagonal graph-edge deletions or for products with more than two factors.

## Proof

**1. Exhaust all faces.** Let \(d_i=v_{ii}\). In \(B_n\), a nonempty independent subset is contained in one full row \(R_i=\{v_{ij}:j\in[n]\}\) or one full column \(C_j=\{v_{ij}:i\in[n]\}\). After the specified faults, any newly independent set must contain two different diagonal vertices \(d_i,d_j\) with \(\{i,j\}\in E(H)\). A third diagonal vertex may be added if and only if it is connected to each of the previous diagonal vertices in \(H\); consequently all independent diagonal subsets are precisely the faces of \(K\). A non-diagonal vertex \(v_{ab}\) (\(a\ne b\)) can coexist with both \(d_i\) and \(d_j\) only if \(\{i,j\}=\{a,b\}\), since for each diagonal vertex \(d_t\) it must satisfy \(t=a\) or \(t=b\). No two distinct non-diagonal vertices can coexist with those two diagonal vertices: the only possible choices \(v_{ij}\) and \(v_{ji}\) are adjacent. Hence the entire complex is **exactly** the union of all full row and column simplices, \(K\), and, for every edge \(\{i,j\}\in E(H)\), precisely the two triangles \(\{d_i,d_j,v_{ij}\}\) and \(\{d_i,d_j,v_{ji}\}\), with all their subfaces.

**2. Row/column elementary collapses.** For every row \(R_i\), set \(O_i=R_i\setminus\{d_i\}\). For each subset \(S\subseteq O_i\) of size at least two, processed in **decreasing cardinality**, collapse the pair \((S,S\cup\{d_i\})\). Its first member is free at that moment: any simplex containing at least two off-diagonal entries in row \(i\) lies in that row simplex alone (no column simplex, diagonal clique or added triangle includes such a pair), and all larger such row faces have already been removed. Repeat the same decreasing-cardinality sequence independently for each column \(C_j\), using \(O'_j=C_j\setminus\{d_j\}\) and the pairs \((S,S\cup\{d_j\})\). The row and column operations do not interfere because their relevant faces meet only in singleton off-diagonal vertices. These collapses leave just the star edges \(d_i v_{ij}\) and \(v_{ij}d_j\) for each off-diagonal \(v_{ij}\), together with \(K\) and the extra triangles.

**3. Delete each filled diagonal fault.** For each \(\{i,j\}\in E(H)\), collapse the triangle \(\{d_i,d_j,v_{ij}\}\) along its free edge \(\{d_i,v_{ij}\}\), then collapse the now-pendant edge \(\{d_j,v_{ij}\}\) along its free vertex \(v_{ij}\). Perform the analogous two collapses for \(v_{ji}\). Each off-diagonal vertex appears in no other triangle, and only its two star edges remain; therefore every indicated pair is free. The edge \(\{d_i,d_j\}\) stays as part of \(K\). All off-diagonal vertices for nonedges survive, with their two incident edges and no higher faces. The remaining complex is exactly \(L_H\), proving the asserted **simplicial collapse**, not just a homology equivalence.

**4. Identify its homotopy type.** Collapse each length-two path in \(L_H\) topologically to an ordinary added edge with the same endpoints; this merely suppresses degree-two vertices. The resulting CW complex consists of \(c\) connected clique-complex components \(|K_a|\) plus \(2q\) added one-cells, every one joining two existing diagonal vertices. Because every pair of vertices in different components of \(H\) is a nonedge, the incidence graph of the new one-cells connects all \(c\) components. Choose a spanning tree of exactly \(c-1\) such intercomponent one-cells, and a path inside each \(K_a\) connecting its attachment vertices to its basepoint. Contracting that combined tree is a homotopy equivalence of the graph-of-spaces, identifying the component basepoints. Each of the remaining \(2q-(c-1)\) added edges is a free circle. This gives the displayed wedge and the integral homology formulas. The identification leaves all clique-complex summands intact up to homotopy and makes their positive-degree homology injections primitive.

## Verification

The included standalone `verify.py` uses only Python's standard library. It constructs all faces from the theorem's explicit characterization, performs **every stated elementary collapse** and independently checks that each proposed lower face has exactly one remaining coface. It verifies that the final face set is exactly \(L_H\). For all \(74\) graphs with \(2\le n\le4\), it additionally enumerates every grid-vertex subset and checks that actual graph independence agrees with the formula. Boundary, complete, cyclic, tripartite and seeded random graphs with \(n=5,6,7\) stress-test the unrestricted collapse. The collected run was: `PASS: 134 fault-graph instances, 29108 explicit elementary free-face collapses; target complexes matched exactly.` These tests corroborate but do not replace the all-parameter proof.

## Relationship to prior work

Goyal, Shukla and Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs* (arXiv:1905.06926v1, first posted 2019-05-16, Proposition 3.2) proved the intact-product \(\operatorname{Ind}(K_m\times K_n)\simeq\bigvee^{(m-1)(n-1)}S^1\). Their complete accessible manuscript treats an unrelated crossing-replacement perturbation in Section 5, but not diagonal graph-edge deletions indexed by an arbitrary graph. Their *Topology of Clique Complexes of Line Graphs* (arXiv:2009.12130) concerns the unaugmented line graph: \(\operatorname{Ind}(K_n\times K_n)\) is also the clique complex of \(L(K_{n,n})\). The diagonal faults here **add** edges among its matching vertices, so this is not the line-graph complex of the original \(K_{n,n}\).

Antolín Camarena and Carnero Bravo, *Homotopy Type of the Independence Complex of Some Categorical Products of Graphs* (arXiv:2307.12401, published 2024), treat higher categorical products and cycle products; neither the stated theorems nor the inspected sections treat the present arbitrary diagonal-fault family. A published later equivariant spine calculation for intact categorical products strengthens the intact baseline but does not imply the full family of faulted clique-complex embeddings. The exact assertion is an elementary-collapse classification over **every** graph \(H\), not merely the original graph's Betti rank.

## Limitations

The argument does not classify all possible perturbations of categorical products, the full equivariant structure of the collapses under arbitrary symmetries of \(H\), or the homotopy maps for nested fault sets. No claim of exhaustive bibliographic uniqueness is made; unindexed or inaccessible work on augmented line-graph clique complexes remains a possible source of equivalent statements. Higher-homotopy groups of the resulting wedge are not in general the direct sum of those of its components; only the stated wedge homotopy type and integral homology splitting are asserted.

## References

1. S. Goyal, S. Shukla, A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926v1 (2019), Proposition 3.2 and Section 5, https://arxiv.org/abs/1905.06926.
2. S. Goyal, S. Shukla, A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130, https://arxiv.org/abs/2009.12130.
3. O. Antolín Camarena, A. Carnero Bravo, *Homotopy Type of the Independence Complex of Some Categorical Products of Graphs*, arXiv:2307.12401; *Homology, Homotopy and Applications* **26** (2024), 349–373, https://arxiv.org/abs/2307.12401.

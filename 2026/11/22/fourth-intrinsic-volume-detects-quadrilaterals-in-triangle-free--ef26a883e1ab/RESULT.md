# Fourth intrinsic volume detects quadrilaterals in triangle-free regular graphical zonotopes

## Finding
Let \(G\) be a connected finite simple triangle-free \(d\)-regular graph on \(n\ge5\) vertices, with \(d\ge2\), and let \(q_4(G)\) be its number of unoriented simple four-cycles. Form its unweighted canonical Euclidean graphical zonotope
\[
Z_G=\sum_{\{i,j\}\in E(G)}[0,e_i-e_j]\subset\mathbf1^\perp\subset\mathbb R^n.
\]
Write \(V_j\) for the \(j\)-th intrinsic volume in Steiner normalization, and put \(m=nd/2\), \(w=n\binom d2\), \(s=n\binom d3\), and \(t=s+m(d-1)^2\). Define the following five explicit numbers (with \(\binom ab=0\) for \(a<b\), \(b\ge0\)):
\[
\begin{aligned}
 E_0&=n\binom d4+3n\binom d3(d-1)+m(d-1)^3,\\
 D_0&=t(m-4d+3),\\
 C_0&=\frac w2\left(w-9\binom d2+4(d-1)\right),\\
 B_0&=w\left[\binom{m-3d+2}{2}-(n-3)\binom d2+(d-1)(3d-4)\right],\\
 A_0&=\binom m4-B_0-C_0-D_0-E_0.
\end{aligned}
\]
Then the **exact fourth intrinsic volume** is
\[
\boxed{V_4(Z_G)=4A_0+2\sqrt3B_0+3C_0+2\sqrt2D_0+\sqrt5E_0-\alpha q_4(G)},
\qquad
\alpha=8\sqrt3+4\sqrt5-10-8\sqrt2>0.
\]
The first three intrinsic volumes depend only on \(n,d\):
\[
\begin{aligned}
V_1(Z_G)&=m\sqrt2,\\
V_2(Z_G)&=2\left(\binom m2-w\right)+\sqrt3w,\\
V_3(Z_G)&=2\sqrt2\left[\binom m3-w(m-3d+2)-t\right]
+\sqrt6w(m-3d+2)+2t.
\end{aligned}
\]
Consequently, among connected triangle-free \(d\)-regular graphs of a fixed order \(n\), the ordered intrinsic-volume data \(V_1,V_2,V_3\) are identical, whereas \(V_4\) **strictly and exactly recovers the four-cycle count**. In particular, for two such graphs \(G,H\),
\[
V_4(Z_G)-V_4(Z_H)=-\alpha\bigl(q_4(G)-q_4(H)\bigr).
\]
There is no assertion that \(V_4\) distinguishes nonisomorphic graphs having the same four-cycle count.

## Assumptions and scope
All graphs are simple, connected, loopless, triangle-free and \(d\)-regular, with \(n\ge5\) and \(d\ge2\). The connectedness assumption ensures \(\dim Z_G=n-1\ge4\), so \(V_4\) is an intrinsic volume of positive dimension. Edge vectors are the **unscaled** incidence roots \(e_i-e_j\) of Euclidean length \(\sqrt2\); signs and translation do not affect intrinsic volumes. The metric is inherited from \(\mathbb R^n\) on the zero-sum hyperplane; volume normalization is the Steiner formula
\[
\operatorname{Vol}_{n-1}(Z_G+rB_{n-1})=\sum_{j=0}^{n-1}\kappa_{n-1-j}V_j(Z_G)r^{n-1-j}.
\]
A four-cycle is counted once for each unoriented, unrooted simple cycle of length four; a graph can have multiple such cycles on different edge sets. No regularity or triangle-freeness beyond the stated class is inferred.

## Proof
**1. A standard geometric identity.** For \(j\le n-1\), the zonotope intrinsic-volume formula gives
\[
V_j(Z_G)=\sum_{\substack{F\subseteq E(G)\\|F|=j}}\sqrt{\det(B_F^{\mathsf T}B_F)},
\]
where \(B_F\) is the matrix of arbitrary oriented incidence columns of the edges in \(F\). A dependent edge set contributes zero. The columns are independent exactly when \(F\) is a forest. For a forest with nontrivial tree components of vertex orders \(r_1,\ldots,r_h\), the matrix-tree determinant identity, applied separately on each component's orthogonal coordinate block, gives
\[
\det(B_F^{\mathsf T}B_F)=\prod_{i=1}^h r_i.
\]
This proves the stated determinant weights independently of any computer experiment. With four edges, the only five forest component edge-size partitions, and their Euclidean weights, are
\[
(1,1,1,1):4,\quad(2,1,1):2\sqrt3,\quad(2,2):3,\quad(3,1):2\sqrt2,\quad(4):\sqrt5.
\]
A nonforest four-edge subset of a triangle-free simple graph consists exactly of the four edges of a four-cycle; hence there are \(q_4(G)\) dependent four-edge subsets.

**2. Small-edge census and the first three volumes.** There are \(m\) one-edge forests; every such edge has weight \(\sqrt2\). There are \(w=n\binom d2\) adjacent edge pairs, each with weight \(\sqrt3\), and the other \(\binom m2-w\) pairs have weight \(2\). Every three-edge subset is a forest by triangle-freeness. Its connected cases are a three-edge star, counted by \(s=n\binom d3\), or a simple three-edge path. The latter has \(m(d-1)^2\) instances: select its middle edge and one distinct continuing edge at either end; a triangle could invalidate the resulting path but is excluded. Thus the connected count is \(t\). Fixing any two-edge wedge on three vertices, the number of edges disjoint from its vertices is \(m-(3d-2)=m-3d+2\); consequently, there are \(w(m-3d+2)\) forests consisting of a wedge and a separated edge. All remaining three-edge subsets are three mutually disjoint edges. Their respective wedge weights are \(2\), \(\sqrt6\), and \(2\sqrt2\), establishing all first-three formulas.

**3. Four-edge trees.** There are three isomorphism types of four-edge trees: \(K_{1,4}\), a broom of degree sequence \((3,2,1,1,1)\), and a length-four path. Their counts are respectively \(n\binom d4\), \(3n\binom d3(d-1)\), and \(m(d-1)^3-4q_4(G)\). For the last count, start with the \(m(d-1)^3\) nonbacktracking walks of length four modulo reversal. Triangle-freeness excludes every repeated vertex except a closed walk around a four-cycle; each unoriented four-cycle contributes four reversally identified walks. Therefore the number \(F_4\) of connected four-edge forests is
\[
F_4=E_0-4q_4(G).
\]

**4. Three-edge tree plus an isolated edge.** Each of the \(t\) three-edge trees occupies four vertices; its three internal edges contribute six to the four-vertex degree sum. If its four vertices support no fourth internal edge, exactly \(m-4d+3\) graph edges lie wholly outside. An extra internal edge would close the endpoints of a three-edge path into a four-cycle. Exactly four three-edge paths on each four-cycle have such an additional chord. Hence the count \(F_{31}\) of a three-edge tree and disjoint singleton edge is
\[
F_{31}=t(m-4d+3)+4q_4(G)=D_0+4q_4(G).
\]

**5. Two separated wedges.** Fix a two-edge wedge \(a-v-b\). Every graph vertex lies in exactly \(3\binom d2\) wedges (as their center or endpoint). Inclusion–exclusion for wedges touching the three vertices \(a,v,b\) shows that the number disjoint from them equals
\[
w-9\binom d2+4(d-1)+c_{ab}-1,
\]
where \(c_{ab}=|N(a)\cap N(b)|\). The two adjacent pairs \(av,bv\) contribute \(2(d-1)\) overlapping wedges each, \(a,b\) contribute \(c_{ab}\), and the chosen wedge gives the triple intersection. Summed over all wedges, \(\sum c_{ab}=w+4q_4(G)\): the wedge center itself is always one common neighbor, and each additional common neighbor bijects with a four-cycle marked at one of its four wedges. Each unordered pair of vertex-disjoint wedges is counted twice. Thus
\[
F_{22}=\frac12 w\left(w-9\binom d2+4(d-1)\right)+2q_4(G)=C_0+2q_4(G).
\]

**6. A wedge and two isolated edges.** For a fixed wedge with vertex set \(S=\{a,v,b\}\), there are \(h=m-3d+2\) edges wholly outside \(S\). From \(\binom h2\) pairs subtract pairs sharing a vertex outside \(S\). If \(r_x\) denotes the number of neighbors of an outside vertex \(x\) in \(S\), the number of adjacent pairs of exterior edges is
\[
\sum_{x\notin S}\binom{d-r_x}{2}
=(n-3)\binom d2-(d-1)(3d-4)+(c_{ab}-1).
\]
Indeed the cut from \(S\) contains \(3d-4\) edges, and by triangle-freeness the only outside common neighbors of two vertices in \(S\) are those shared by \(a,b\), numbering \(c_{ab}-1\). Sum over all \(w\) wedges and use \(\sum(c_{ab}-1)=4q_4(G)\). Hence
\[
F_{211}=w\left[\binom{m-3d+2}{2}-(n-3)\binom d2+(d-1)(3d-4)\right]-4q_4(G)
=B_0-4q_4(G).
\]

**7. Four mutually disjoint edges and the final coefficient.** Partition all \(\binom m4\) edge quadruples into the five forest types and the \(q_4(G)\) dependent cycles. Substitution gives
\[
F_{1111}=\binom m4-F_{211}-F_{22}-F_{31}-F_4-q_4(G)=A_0+q_4(G).
\]
Multiplying the five counts by their exact geometric weights proves the boxed fourth-volume identity, with coefficient
\[
4(1)-2\sqrt3(4)+3(2)+2\sqrt2(4)-\sqrt5(4)
=10+8\sqrt2-8\sqrt3-4\sqrt5=-\alpha.
\]
For strict negativity, the elementary rational bounds \(\sqrt2<3/2\), \(\sqrt3>5/3\), and \(\sqrt5>11/5\) yield \(-\alpha<-2/15<0\). The claimed identification of \(q_4\) and the equality of the preceding three intrinsic volumes now follow.

## Verification
Run the dependency-free companion program `python3 artifacts/verify.py` from the directory containing this file. It enumerates every four-edge subset and directly computes its integer incidence-column Gram determinant for ten connected triangle-free regular graphs, including cycles, bicliques, the cube, the Petersen graph, and three bipartite circulants. It independently counts actual four-cycles by checking all four-vertex subsets, reconstructs the five forest types, and compares their exact counts to the displayed formulas. The program also verifies the three-edge tree census, ending with `GRAPHICAL_ZONOTOPE_FOURTH_VOLUME_PASS`.

For a concrete nontrivial separation, the bipartite circulant graphs on two classes of seven vertices, with edges from \(i\) to \(i+s\pmod7\) for \(s\in\{0,1,2\}\) and for \(s\in\{0,1,3\}\), are connected and cubic. The first has seven four-cycles and the second has none. Their first three intrinsic volumes agree, but their fourth intrinsic volumes differ by exactly \(7\alpha\). Finite computations are corroboration, not proof for unrestricted \(n,d\).

## Relationship to prior work
Padrol, Pilaud and Poullot developed the deformation cones of graphical zonotopes (arXiv:2111.12422, first version 24 November 2021); their paper explicitly treats triangle-free graphs and four-cycle examples, but its geometric statements concern deformation cones rather than fourth Steiner intrinsic volumes or recovery of the number of four-cycles. The general zonotope intrinsic-volume determinant formula is an established input, given for example by Joós and Lángi (arXiv:2206.03204; first version 7 June 2022), who also credit earlier work of Brazitikos and McIntyre. Those formulas alone do not supply the five-type fourth-edge census or its strictly signed four-cycle coefficient.

The previously recorded third-intrinsic-volume extremal formula for graphs with a few missing complete-graph edges uses only three-edge forest motifs and does not entail this fourth-volume theorem for sparse regular graphs. A recorded all-ranks formula for the two-hub graphical zonotope \(K_{2,q}\) is family-specific: except in the four-cycle case \(q=2\) (intrinsic dimension three), these graphs are not regular. Previous cubic directional-width-moment formulas for regular graphical zonotopes identify triangles, not four-cycles through the fourth intrinsic volume. The genuinely new asserted content, subject to historical-priority assessment, is the exact \(q_4\)-sensitive fourth-volume identity within the triangle-free regular class, coupled with the complete equality of the earlier three intrinsic volumes.

## Limitations
The theorem is restricted to connected simple triangle-free regular graphs with \(n\ge5\), \(d\ge2\), unweighted incidence-root segments, and the fourth Steiner intrinsic volume. It does not extend automatically to irregular, weighted or triangle-containing graphs. Distinct graphs with equal four-cycle counts remain indistinguishable by this particular invariant. The finite checker neither establishes the all-parameter theorem nor proves historical novelty; the proof is combinatorial and exact. Equivalent results could exist in literature under weighted forest enumerators, girth-restricted graphic-matroid valuations, or an unstated specialization of a broader formula. Independent external mathematical validation remains outstanding.

## References
1. A. Padrol, V. Pilaud and G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422 (first version 2021-11-24), https://arxiv.org/abs/2111.12422; open-access journal version, https://doi.org/10.1007/s00454-023-00586-x.
2. A. Joós and Z. Lángi, *Isoperimetric Problems for Zonotopes*, arXiv:2206.03204 (first version 2022-06-07), https://arxiv.org/abs/2206.03204; *Mathematika* **69** (2023), 508–534.
3. S. Brazitikos and F. McIntyre, *Vector-Valued Maclaurin Inequalities*, arXiv:2102.05900 (2021), https://arxiv.org/abs/2102.05900.
4. *Sharp third-intrinsic-volume extrema for nearly complete graphical zonotopes*, public mathematical result at https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-third-intrinsic-volume-extrema-for-nearly-complete-graphic--138f7ed54317.
5. *Two-hub graphical zonotopes: complete intrinsic volumes and a square-root forest-connectivity anomaly*, public mathematical result at https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-two-hub-graphical-zonotopes-complete-intrinsic-volumes-and-a-squ--6dc29c3b9e4b.
6. *Third angular-width moments of regular graphical zonotopes recover graph triangles*, public mathematical result at https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-third-angular-width-moments-of-regular-graphical-zonotopes-recov--49a1005c0e97.

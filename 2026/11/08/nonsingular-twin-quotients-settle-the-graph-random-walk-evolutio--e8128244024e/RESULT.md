# Nonsingular twin quotients settle the graph–random-walk evolution-algebra isomorphism criterion

## Finding
Let \(H\) be a finite connected undirected loopless graph with at least two vertices and nonsingular real adjacency matrix. Replace each vertex \(i\) by a nonempty independent set of \(m_i\) clones; join two clone sets completely if and only if their original vertices are adjacent in \(H\). Denote this graph by \(G=H[\overline K_{m_1},\ldots,\overline K_{m_r}]\). Then the two real evolution algebras formed from the adjacency matrix and from the simple-random-walk transition matrix are isomorphic **if and only if** \(G\) is regular or bipartite biregular:

\[
A(G)\cong_{\mathbb R} A_{\mathrm{RW}}(G)
\quad\Longleftrightarrow\quad
G\text{ is regular or bipartite biregular}.
\]

In particular, this conclusion holds for **every** complete multipartite graph with at least two nonempty parts. For exactly two parts the graph is bipartite biregular and the algebras are isomorphic; with at least three parts they are isomorphic exactly when all part sizes are equal. If any clone set has more than one vertex then the expanded adjacency matrix is singular, so the theorem genuinely includes singular graphs.

## Assumptions and scope
All algebras and linear maps are over \(\mathbb R\). The base \(H\) is connected, finite, undirected and simple; its adjacency matrix is invertible over \(\mathbb R\). Each multiplicity \(m_i\) is an integer at least one. The clone graph \(G\) is simple and connected with positive vertex degrees.

For any finite simple graph \(F\) with no isolated vertices, both algebras have natural basis \(\{e_v:v\in V(F)\}\), with \(e_ve_w=0\) for \(v\ne w\). In \(A(F)\), \(e_v^2=\sum_{w\sim v}e_w\); in \(A_{\mathrm{RW}}(F)\), \(e_v^2=\deg(v)^{-1}\sum_{w\sim v}e_w\). An algebra isomorphism means an invertible real linear map preserving these products. A graph is *bipartite biregular* if it has a bipartition such that all degrees within each side are equal, with the two side degrees allowed to differ.

Write \(V_i\) for the clone set above \(i\), \(U_i=\operatorname{span}_{\mathbb R}\{e_v:v\in V_i\}\), \(u_i=\sum_{v\in V_i}e_v\), \(w_i=\sum_{j\sim_H i}u_j\), and \(d_i=\sum_{j\sim_H i}m_j\). These have no dependence on a choice of ordering within clone sets.

## Proof
**Step 1: multiplication ranks intrinsically recover the clone spaces.** For elements \(x=\sum_i x_i\) and \(y=\sum_i y_i\), where \(x_i,y_i\in U_i\), the two products are
\[
xy=\sum_i\langle x_i,y_i\rangle w_i,
\qquad
x\mathbin{*}y=\sum_i d_i^{-1}\langle x_i,y_i\rangle w_i.
\]
Here the brackets are the standard Euclidean dot products on the disjoint coordinate blocks. Since the adjacency matrix of \(H\) is nonsingular, the vectors \(w_1,\ldots,w_r\) are linearly independent: their coordinates relative to the independent vectors \(u_j\) are the columns of that matrix.

Let \(L_x\) denote left multiplication by \(x\) in either algebra. The nonzero coordinate functionals \(y_i\mapsto\langle x_i,y_i\rangle\) have mutually independent domains, so
\[
\operatorname{rank}(L_x)=\bigl|\{i:x_i\ne0\}\bigr|.
\]
Thus the maximal linear subspaces on which every vector has multiplication rank at most one are precisely \(U_1,\ldots,U_r\). Indeed, a linear space contained in their union cannot contain nonzero vectors from two distinct blocks, because the sum would have rank two. This characterization is algebra-intrinsic: for an algebra isomorphism \(T\), left multiplications satisfy \(L_{T(x)}=T L_x T^{-1}\). Hence any isomorphism \(T:A(G)\to A_{\mathrm{RW}}(G)\) permutes the clone spaces, say \(T(U_i)=U_{\sigma(i)}\), and consequently \(m_i=m_{\sigma(i)}\).

**Step 2: every isomorphism is conformal on each block.** Denote \(T|_{U_i}\) by \(T_i\). For any basis element \(e_v\in U_i\), the square identity implies that \(T(w_i)=(\|T_i(e_v)\|^2/d_{\sigma(i)})w_{\sigma(i)}\). Its coefficient is strictly positive because \(T\) is invertible, and it is independent of \(v\), since the left side is. Denote it by \(c_i>0\). The identities \(e_ve_w=0\) for distinct basis elements in \(V_i\), together with their square identities, imply
\[
T(w_i)=c_iw_{\sigma(i)},\qquad
T_i^{\mathsf T}T_i=c_i d_{\sigma(i)} I_{m_i}.
\]
In particular, each \(T_i\) is an invertible scaled orthogonal map.

**Step 3: the induced permutation is a graph automorphism.** Expanding the first equality gives
\[
\sum_{j\sim_H i}T_j(u_j)=c_i\sum_{k\sim_H\sigma(i)}u_k.
\]
Each \(T_j(u_j)\ne0\) lies in the distinct block \(U_{\sigma(j)}\). Comparing nonzero block supports yields \(\sigma(N_H(i))=N_H(\sigma(i))\). Therefore \(\sigma\in\operatorname{Aut}(H)\). In particular, the clone-size preservation from Step 1 implies \(d_{\sigma(j)}=d_j\). Comparing the individual block coordinates of the same displayed equality also yields, on every edge \(ij\) of \(H\),
\[
T_j(u_j)=c_i u_{\sigma(j)}.
\]
If two vertices have a common neighbor, they have the same \(c\)-value. Taking squared Euclidean norms in the last identity and using the conformality of \(T_j\) gives
\[
c_i^2 m_j=\|T_j(u_j)\|^2
=c_j d_{\sigma(j)}m_j
=c_jd_jm_j.
\]
Since \(m_j>0\), we have the **edge constraint**
\[
c_i^2=c_jd_j\quad\text{for every edge }ij.
\]

**Step 4: the edge constraint forces (bi)regularity.** The equivalence classes generated by even-length walks form one class in a connected nonbipartite graph, and precisely its two bipartition sides in a connected bipartite graph. Because vertices with a common neighbor have equal \(c\)-values, in the nonbipartite case all \(c_i=c>0\). The edge constraint then gives \(d_j=c\) for every \(j\), so \(G\) is regular. In the bipartite case \(c\) takes constants \(c_L>0\) and \(c_R>0\) on the respective sides of \(H\); for any vertex \(j\) on the left, \(d_j=c_R^2/c_L\), and for any vertex on the right, \(d_j=c_L^2/c_R\). Since degrees of all clones in \(V_j\) equal \(d_j\), the blown-up graph is bipartite biregular.

**Step 5: construct the converse isomorphisms.** If \(G\) is regular of degree \(D>0\), the diagonal map \(T(e_v)=D e_v\) satisfies \(T(e_v^2)=T(e_v)\mathbin{*}T(e_v)\) for every basis vertex and preserves all cross-products, so it is an isomorphism. If \(G\) is bipartite biregular with positive degrees \(D_L\) and \(D_R\) on its two sides, put
\[
a_L=(D_L^2D_R)^{1/3},\qquad a_R=(D_LD_R^2)^{1/3}.
\]
The diagonal map multiplying basis vectors on the respective sides by \(a_L\) and \(a_R\) is invertible. Since \(a_L^2/D_L=a_R\) and \(a_R^2/D_R=a_L\), its square and cross-product identities hold. This completes both implications.

**Complete multipartite specialization.** The quotient base is the complete graph on the parts. Its adjacency matrix has eigenvalues \(r-1\) once and \(-1\) with multiplicity \(r-1\), so is invertible for \(r\ge2\). For \(r=2\) all such blow-ups are bipartite biregular. For \(r\ge3\), the graph is nonbipartite, and a vertex in part \(i\) has degree \(N-m_i\), where \(N=\sum_jm_j\), constant over all vertices exactly when all part sizes coincide. If some \(m_i>1\), two distinct clone vertices have identical adjacency rows and the expanded adjacency matrix is singular.

## Verification
The standalone script `verification/check_blowup.py` uses exact rational row reduction for the base-adjacency nonsingularity checks; directly constructs seven blow-ups; verifies the specified real diagonal isomorphisms by their multiplication-table identities; and checks the intrinsic rank formula against every nonzero vector over \(\mathbb F_5\) for the six cases with at most six vertices. The last test covers exactly \(38{,}244\) vectors. The complete output is included in `verification/OUTPUT.txt`. Run it with `python3 verification/check_blowup.py` in a directory containing the extracted package files. The finite-field enumeration checks an algebraic rank identity and does not establish the real-field isomorphism obstruction; that obstruction is proved in Steps 1–4.

## Relationship to prior work
The 2026 survey of Kaygorodov, Martín González and Viruel, Question 26, explicitly asks whether the adjacency and random-walk evolution algebras of any finite connected graph are isomorphic only in the regular or biregular cases. Cadavid, Rodiño Montoya and Rodríguez (2017 preprint; later published) prove this characterization when the *whole* adjacency matrix is nonsingular and exhibit singular complete-bipartite examples. Cadavid, Rodiño Montoya, Rodríguez and Vidal (2024) study nonisomorphism for particular singular caterpillars, tadpoles and the bull graph; they identify the twin-partition approach as a promising direction. Neither cited paper states the present theorem for **every** independent-set blow-up with nonsingular quotient. This result extends the criterion to a parametrized family of singular graphs: it is not a corollary of whole-graph nonsingularity because blown-up graphs with repeated clones have singular adjacency matrices. The direct rank-one-locus proof permits full, possibly mixing, real-linear algebra isomorphisms; it does not assume that an isomorphism is diagonal.

## Limitations
The theorem does **not** resolve the conjecture for all finite connected singular graphs; a graph whose false-twin quotient still has singular adjacency matrix is outside the hypotheses. It is specific to real evolution algebras. The proof uses the positive-definite coordinate dot product, and no assertion over arbitrary coefficient fields is made. The classification is for existence of isomorphisms, not for all homomorphisms or a full automorphism-group classification. Earlier literature under alternative twin-reduction or algebra-isomorphism terminology may contain an equivalent result, and such historical-priority uncertainty is not proof of novelty.

## References
1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first publicly posted 2026-10-15), Question 26. https://arxiv.org/abs/2610.22248
2. P. Cadavid, M. L. Rodiño Montoya and P. M. Rodríguez, *On the isomorphisms between evolution algebras of graphs and random walks*, arXiv:1710.10516 (first publicly posted 2017-10-28), Theorem 2.3 and Examples 2.2–2.4. https://arxiv.org/abs/1710.10516
3. P. Cadavid, M. L. Rodiño Montoya, P. M. Rodríguez and S. J. Vidal, *On some singular graphs with non-isomorphic associated evolution algebras*, arXiv:2405.12341v1 (first publicly posted 2024-05-20), Sections 2–3. https://arxiv.org/abs/2405.12341

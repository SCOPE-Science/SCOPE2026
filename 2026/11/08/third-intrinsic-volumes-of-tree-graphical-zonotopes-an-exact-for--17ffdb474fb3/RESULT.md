# Third intrinsic volumes of tree graphical zonotopes: an exact formula and sharp path–star bounds

## Finding

For every finite simple tree \(T\) on \(n\ge6\) vertices, form its centered graphical zonotope
\[
Z_T=\sum_{\{u,v\}\in E(T)}[-(e_u-e_v)/2,(e_u-e_v)/2]\subseteq\mathbf1^{\perp}\subset\mathbb R^n.
\]
Set \(m=n-1\). Let \(M_2(T)\) and \(M_3(T)\) count edge matchings with two and three edges, respectively, and let \(P_4(T)\) count unoriented simple paths on four vertices (three consecutive edges). Define
\[
\alpha=\frac{\sqrt6-2}{2}>0,\qquad
\beta=1+2\sqrt2-\frac{3\sqrt6}{2}>0.
\]
Then the intrinsic third volume, under the standard Euclidean normalization, is
\[
\boxed{V_3(Z_T)=2\binom m3+\alpha\big((m-2)M_2(T)-P_4(T)\big)+\beta M_3(T).}
\tag{1}
\]
Among trees on \(n\) vertices, the unique minimizer (up to isomorphism) is the star \(S_n\), and the unique maximizer is the path \(P_n\): for every tree distinct from both,
\[
\boxed{2\binom{n-1}{3}=V_3(Z_{S_n})<V_3(Z_T)<V_3(Z_{P_n})}
\]
where
\[
\boxed{V_3(Z_{P_n})=2(n-3)+\sqrt6(n-3)(n-4)+2\sqrt2\binom{n-3}{3}.}
\]
Their exact gap is
\[
V_3(Z_{P_n})-V_3(Z_{S_n})
=\alpha(n-3)\left(\binom{n-2}{2}-1\right)
+\beta\binom{n-3}{3}>0,
\]
and their ratio tends to \(\sqrt2\) as \(n\to\infty\).

Unlike the degree-determined width variance, the third intrinsic volume distinguishes some trees with identical degree sequences. Specifically, the two six-vertex spiders with arm-length multisets \((3,1,1)\) and \((2,2,1)\) satisfy
\[
V_3(Z_{(3,1,1)})-V_3(Z_{(2,2,1)})
=2\sqrt6-2\sqrt2-2>0.
\]

## Assumptions and scope

All graphs are finite, connected, simple and unweighted; here the graph is specifically a tree. The affine span is the Euclidean hyperplane \(H=\{x\in\mathbb R^n:\sum_i x_i=0\}\), of dimension \(d=n-1\), with its inherited Euclidean metric. The vectors \(e_i\) are the standard orthonormal basis of \(\mathbb R^n\). Signs/orientations chosen for each edge do not affect the centered zonotope.

The intrinsic volumes \(V_j\) use the Steiner identity
\[
\operatorname{Vol}_d(K+tB_d)=\sum_{j=0}^d\kappa_{d-j}V_j(K)t^{d-j}\quad(t\ge0),
\]
where \(\kappa_r\) is the volume of the Euclidean unit \(r\)-ball. In particular, \(V_d(K)\) is ordinary \(d\)-volume, while \(V_3\) is the third intrinsic volume, which is not generally surface area. The domain \(n\ge6\) keeps the assertion separate from the near-top \(V_{n-2}\) surface-area case in small dimensions. All path counts are unoriented, all matchings consist of distinct pairwise vertex-disjoint edges, and binomial coefficients outside their ordinary range are taken as zero.

## Proof

**1. Intrinsic-volume reduction and the exact forest determinant.** The zonotope intrinsic-volume formula, proved for arbitrary generator vectors by Brazitikos–McIntyre and Joós–Lángi, states that if \(Z=\sum_{i=1}^{m}[0,g_i]\), then
\[
V_3(Z)=\sum_{1\le i<j<k\le m}\sqrt{\det\big(\langle g_a,g_b\rangle\big)_{a,b\in\{i,j,k\}}}.
\tag{2}
\]
Translation from \(\sum_e[0,e_u-e_v]\) to the centered zonotope does not alter intrinsic volumes. Any chosen three tree edges form a forest \(F\). In each nontrivial connected component of \(F\) with \(r\) vertices, the vertex-edge incidence matrix \(B\) has \(r-1\) columns. Its \(r\) maximal square minors, obtained by deleting one row, have determinants \(\pm1\): remove a leaf successively to verify this by induction. Cauchy–Binet therefore yields \(\det(B^{\mathsf T}B)=r\). Different components have disjoint supports, so the entire triple Gram determinant is the product of the nontrivial component sizes.

There are exactly three possibilities for three edges: one component of four vertices (determinant \(4\), parallelotope volume \(2\)); components of three and two vertices (determinant \(6\), volume \(\sqrt6\)); or three components each with two vertices (determinant \(8\), volume \(2\sqrt2\)). Denote the numbers of these types by \(a,b,c\), respectively. Thus
\[
V_3(Z_T)=2a+\sqrt6b+2\sqrt2c,
\quad a+b+c=\binom m3,\quad c=M_3(T).
\tag{3}
\]

**2. Matching–path identity.** Every two-edge matching extends to a three-edge subset in exactly \(m-2\) ways. A connected three-edge path has one pair of disjoint edges; a connected claw has none; a two-component triple of types two-edges-plus-one has exactly two; and three disjoint edges have exactly three. Consequently,
\[
(m-2)M_2(T)=P_4(T)+2b+3c.
\tag{4}
\]
Substituting \(b=((m-2)M_2-P_4-3M_3)/2\) and \(a=\binom m3-b-c\) in (3) gives (1) with the displayed positive coefficients. Their positivity is elementary; for \(\beta\), it follows from \(2+4\sqrt2>3\sqrt6\), which in turn follows after squaring from \(36+16\sqrt2>54\).

**3. Unique minimum.** Each three-generator volume in (3) is at least \(2\), so \(V_3(Z_T)\ge2\binom m3\). For a star, every three-edge subset is connected, so equality holds. Conversely, a nonstar tree has a path of three consecutive edges \(e_1,e_2,e_3\). Since \(m\ge5\), there is another edge \(f\) outside that path. Deleting \(e_2\) partitions the tree into two components, with \(e_1\) and \(e_3\) on opposite sides. The edge \(f\) cannot reconnect them; hence \(\{e_1,e_3,f\}\) is disconnected, with volume strictly greater than \(2\). This proves unique star minimality.

**4. Matching bound for all forests.** Let \(m_k(F)\) denote the number of \(k\)-edge matchings in a forest with \(N\) vertices. For every \(N,k\ge0\),
\[
m_k(F)\le\binom{N-k}{k}.
\tag{5}
\]
Proof is by induction on \(N\). If there is an isolated vertex, delete it without changing the matching count and use monotonicity in \(N\). Otherwise take a leaf \(v\) with neighbor \(u\): matchings either omit \(uv\) or contain it, whence
\[
m_k(F)=m_k(F-v)+m_{k-1}(F-\{u,v\})
\le\binom{N-k-1}{k}+\binom{N-k-1}{k-1}
=\binom{N-k}{k}.
\]
The path attains equality, since its \(k\) pairwise nonconsecutive edge positions are enumerated by the right-hand binomial coefficient. In particular,
\[
M_3(T)\le M_3(P_n)=\binom{n-3}{3}.
\tag{6}
\]

**5. Unique maximum.** Let \(D(T)=(m-2)M_2(T)-P_4(T)\). Two edges are adjacent exactly when they meet at a tree vertex, so
\[
M_2(T)=\binom m2-\sum_{v\in V(T)}\binom{\deg(v)}2.
\]
As \(\sum_v(\deg(v)-1)=n-2\), it follows that
\[
M_2(P_n)-M_2(T)=R(T),\quad
R(T)=\sum_v\binom{\deg(v)-1}{2}.
\]
For a nonpath tree, some vertex has degree at least three, hence \(R(T)\ge1\). Since a nonpath tree is not a star unless it is the minimum case already handled, every nonpath nonstar has a four-vertex path and thus \(P_4(T)\ge1\). The same inequality also holds for stars when used in the upper-bound calculation with a separate observation: for a star, \(R(S_n)=\binom{n-2}{2}\ge6\) for \(n\ge6\), while \(P_4(S_n)=0\). On a path, \(P_4(P_n)=m-2=n-3\). Therefore, for all nonpath trees \(T\),
\[
D(P_n)-D(T)=(m-2)(R(T)-1)+P_4(T)>0.
\tag{7}
\]
Indeed, for nonstar nonpaths the second term is positive, while for stars the first term is positive. Combining (6), (7), \(\alpha>0\) and \(\beta>0\) in formula (1) proves the path is the unique maximum.

On the path, the numbers of three-edge subsets with respectively one, two, or three components are \(n-3\), \((n-3)(n-4)\), and \(\binom{n-3}{3}\). Equation (3) yields the stated path formula. Subtracting the star value and using (1) gives the exact gap. The cubic leading term in the path formula comes from three disjoint edges, with coefficient \(2\sqrt2/6\), versus \(2/6\) for the star, proving the asymptotic ratio.

**6. Same-degree separation.** Both six-vertex spiders specified in the finding have degree sequence \((3,2,2,1,1,1)\). For arm lengths \((3,1,1)\), the triple-subforest counts \((a,b,c)\) are \((4,6,0)\). For \((2,2,1)\), they are \((5,4,1)\). Equation (3) proves the exact stated nonzero difference. This completes the proof.

## Verification

A separate finite checker, included as `CHECKER.py`, independently builds all oriented incidence vectors and their integer Gram determinants. It enumerates every unlabeled tree on \(6\le n\le11\), independently compares the intrinsic-volume formula against sums of triple parallelotope volumes, checks the three forest types and matchings, and verifies strict uniqueness against the path and star. It also checks the two same-degree spiders. Running `python CHECKER.py` with `networkx>=3.0,<4.0` produced `THIRD_INTRINSIC_TREE_ZONOTOPE_CHECKS_PASSED 428 40821 416` and the spider-difference decimal `0.07055236082016547`. The counts refer to 428 tree configurations, 40,821 individual triple determinants, and 416 strict intermediate tree cases. This computation is a finite corroboration, not an infinite proof; the analytical argument above handles all \(n\ge6\).

## Relationship to prior work

The general intrinsic-volume formula for zonotopes is established in Brazitikos–McIntyre (2021) and in Joós–Lángi (2022 preprint, Corollary 1). Those broad results supply (2), but do not determine the forest triple-type counts or sharp extremizers when the generators are the standard incidence vectors of *all* trees of fixed order. A prior geometric study of tree graphical zonotopes determines a different width-variance invariant using incident-edge pairs and identifies path–star extremizers for that invariant; the same-degree spider pair above shows that the present \(V_3\) is not determined by that pair statistic. Existing near-top surface-area statements concern different intrinsic-volume indices for \(n\ge6\). A literature search did not find a theorem implying (1) together with both uniqueness statements; historical priority is not independently established.

## Limitations

The result holds for unit-weight incidence generators, the canonical inherited Euclidean metric, and trees on at least six vertices. Affine-equivalent but nonisometric zonotope realizations need not share intrinsic volumes. It does not classify arbitrary connected graphs with cycles or arbitrary weighted trees. The finite checker was not used as a substitute for proof. Other equivalent earlier results under graphical-matroid or intrinsic-volume terminology may exist.

## References

- S. Brazitikos and F. McIntyre, *Vector-Valued Maclaurin Inequalities*, arXiv:2102.05900, first publicly available February 11, 2021; in particular the vector-wedge and intrinsic-volume discussion. https://arxiv.org/abs/2102.05900
- A. Joós and Z. Lángi, *Isoperimetric Problems for Zonotopes*, arXiv:2206.03204, first publicly available June 7, 2022; especially Corollary 1 and Sections 3–4. https://arxiv.org/abs/2206.03204

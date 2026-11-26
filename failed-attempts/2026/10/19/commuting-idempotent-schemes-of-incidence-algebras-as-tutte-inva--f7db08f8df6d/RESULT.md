# Commuting-idempotent schemes of incidence algebras as Tutte invariants, with a sharp four-point reconstruction failure

## Finding
Let \(P\) be a finite poset, \(G_P\) its (simple, undirected) **comparability graph**, and \(I(P,k)\) its incidence algebra over a field \(k\). For every integer \(r\ge1\), let \(X_r(P)\) be the affine scheme of ordered tuples \((E_1,\ldots,E_r)\) satisfying \(E_i^2=E_i\) and \(E_iE_j=E_jE_i\) for every \(i,j\). Put \(L_r=\{0,1\}^r\), and for each coloring \(c:P\to L_r\) let
\[
d(c)=\#\{\{x,y\}\in E(G_P):c(x)\ne c(y)\}.
\]
There is a (generally noncanonical) **scheme isomorphism** over every field, including characteristic two,
\[
X_r(P)\;\cong\;\coprod_{c:P\to L_r}\mathbb A_k^{d(c)}.\tag{1}
\]
In particular, every component is reduced, smooth and geometrically connected, and its dimension is the graph-cut size \(d(c)\). The scheme therefore depends on the poset only through the cut-size distributions of colorings of its comparability graph, not through the direction of its partial order.

Let \(m=|E(G_P)|\), \(n=|P|\), and \(Q=2^r\). For every finite field \(\mathbb F_q\),
\[
\begin{aligned}
|X_r(P)(\mathbb F_q)|
&=\sum_{c:P\to[Q]}q^{d(c)}\\
&=\sum_{S\subseteq E(G_P)}q^{m-|S|}(1-q)^{|S|}Q^{k(S)}\\
&=q^m Z_{G_P}\!\left(Q,\frac{1-q}{q}\right),
\end{aligned}\tag{2}
\]
where \(k(S)\) denotes the number of connected components of the spanning subgraph \((P,S)\) and \(Z_G(Q,v)=\sum_{S\subseteq E(G)}Q^{k(S)}v^{|S|}\) is the Fortuin–Kasteleyn random-cluster (multivariate Tutte/Potts) polynomial. If \(P\) and \(P'\) are **connected**, then the following are equivalent: the comparability graphs have equal Tutte polynomials; \(X_r(P)\) and \(X_r(P')\) are isomorphic as abstract schemes for every \(r\ge1\) over every field; and their \(\mathbb F_q\)-point counts agree for every \(r\ge1\) and every prime-power \(q\). The graph-isomorphism claim is not made: the invariant is precisely the Tutte polynomial.

For any connected **height-one** poset with tree comparability graph on \(n\ge2\) vertices, the stronger decomposition is
\[
X_r(P)\cong\coprod_{j=0}^{n-1}
\left(\mathbb A_k^j\right)^{\sqcup\,Q\binom{n-1}{j}(Q-1)^j},
\qquad
|X_r(P)(\mathbb F_q)|=Q\bigl(1+(Q-1)q\bigr)^{n-1}.\tag{3}
\]
Among connected height-one posets, **four is the smallest cardinality** at which nonisomorphic and non-anti-isomorphic incidence algebras can have all the schemes \(X_r\) isomorphic. One witness is the four-point star with strict comparable pairs \((0,3),(1,3),(2,3)\); the other is the alternating path with strict comparable pairs \((0,1),(2,1),(2,3)\). Both incidence algebras have dimension seven; their comparability graphs are distinct four-vertex trees and have the same Tutte polynomial.

## Assumptions and scope
The base \(k\) is any field, of unrestricted characteristic; scheme equalities are statements of functors on **all commutative \(k\)-algebras**, not just equalities of closed-point counts. The poset is arbitrary finite unless connectedness or height one is explicitly stipulated. The algebra is the full incidence algebra, with basis elements indexed by all intervals \(x\le y\). The graph uses *all* strict comparable pairs, not merely Hasse edges; for height-one posets these graphs coincide. Isomorphism of \(X_r\) is as abstract schemes, without an identification with the surrounding affine algebra space or a prescribed labeling of diagonal components. The Tutte equivalence is stated for connected graphs, so the ordinary two-variable Tutte polynomial determines vertex and edge counts.

## Proof
**1. Diagonal color strata.** Fix \(r\). On the affine scheme \(X_r(P)\), each diagonal entry of each idempotent satisfies \(a^2=a\). The identities \(a(1-a)=0\) split its coordinate algebra by central orthogonal idempotents, over any field and without dividing by two. Consequently the diagonal map has open-and-closed fibers \(X_{r,c}\), one for each function \(c:P\to L_r\). On the fiber \(c\), let \(D_t\) denote the diagonal incidence-algebra element whose \(x\)-entry is \(c(x)_t\).

**2. Simultaneous conjugation, valid over arbitrary rings.** Let \(R\) be any commutative \(k\)-algebra and take a point \((E_t)\in X_{r,c}(R)\). Because the idempotents commute, the elements
\[
P_{\lambda}=\prod_{t=1}^{r}
\begin{cases}E_t,&\lambda_t=1,\\1-E_t,&\lambda_t=0,\end{cases}
\qquad\lambda\in L_r,
\]
are pairwise orthogonal idempotents with sum one. Let \(e_x\) denote the standard column at vertex \(x\), and define an upper incidence-supported matrix \(u\) by setting its column at \(x\) equal to \(P_{c(x)}e_x\). Since the diagonal of \(P_{c(x)}\) has value one at \(x\), the matrix \(u\) lies in the unipotent group \(U=1+J\) of the incidence algebra. The polynomial identities \(E_tP_{c(x)}=c(x)_tP_{c(x)}\) give \(E_tu=uD_t\), hence \(E_t=uD_tu^{-1}\). This construction and the triangular inverse of \(u\) are polynomial over \(\mathbb Z\), so no field-extension or reduced-point argument is involved.

**3. Explicit affine quotient section.** Let \(H_c\subset U\) consist of matrices \(1+h\) whose entry \(h_{xy}\) is zero whenever \(x<y\) and \(c(x)\ne c(y)\). It is precisely the stabilizer of all \(D_t\), because \([h,D_t]_{xy}=(c(y)_t-c(x)_t)h_{xy}\). Define the cross-color affine section \(S_c\subset U\) to consist of \(1+s\) with \(s_{xy}=0\) when \(c(x)=c(y)\); it is an affine space of dimension \(d(c)\). The map
\[
S_c\times H_c\longrightarrow U,\qquad(s,h)\longmapsto sh,
\]
is a polynomial isomorphism: the entry at each comparable pair \(x<y\) satisfies
\[
(sh)_{xy}=s_{xy}+h_{xy}+\sum_{x<z<y}s_{xz}h_{zy}.
\]
Proceeding by increasing interval length (equivalently, a linear extension of proper intervals), the sum is already known, and exactly one of \(s_{xy},h_{xy}\) is permitted to be nonzero. This recursively gives the inverse polynomial map, with no denominators. Since the entire stabilizer \(H_c\) centralizes the diagonal tuple, the simultaneous-conjugation orbit map \(s\mapsto(sD_ts^{-1})_t\) is bijective on \(R\)-points for **every** commutative \(R\), with its inverse induced by the polynomial conjugator construction followed by the polynomial factorization \(u=sh\). By the functor-of-points criterion it is a scheme isomorphism \(S_c\simeq X_{r,c}\), proving (1) scheme-theoretically.

**4. Cut transform and exact graph reconstruction threshold.** For fixed coloring \(c\), the product over graph edges satisfies
\[
q^{d(c)}=\prod_{e=\{x,y\}}\bigl(q+(1-q)\mathbf1_{c(x)=c(y)}\bigr).
\]
Expand the product over edge subsets \(S\); a coloring is constant along every edge in \(S\) exactly when it is constant on the \(k(S)\) connected components of \((P,S)\), giving \(Q^{k(S)}\) assignments. This proves (2). The polynomial \(F_G(Q,q)=\sum_cq^{d(c)}\) has integral coefficients. Equality of all point counts at \(Q=2^r\) and all prime powers \(q\) is equality of bivariate polynomials by two successive polynomial identity arguments. Its degree in \(q\) equals \(m\), because assigning pairwise distinct colors for \(Q\ge n\) cuts every edge. Thus \(F_G\) determines \(m\), and the invertible change of variables \(v=(1-q)/q\) determines \(Z_G(Q,v)\). For connected graphs \(Z_G\) is equivalent to the ordinary Tutte polynomial via \(Z_G(Q,v)=Qv^{n-1}T_G(1+Q/v,1+v)\); conversely the Tutte polynomial determines \(n,m\), \(Z_G\), all component-dimension multiplicities, and hence all abstract schemes (1). In particular, no extra graph orientation information survives.

**5. Trees and the minimal nonreconstruction.** Root a tree. The root receives any of \(Q\) colors; each of its \(n-1\) edges independently retains the parent color in one way or chooses one of the other \(Q-1\) colors. Exactly \(j\) changed edges occur in \(Q\binom{n-1}{j}(Q-1)^j\) colorings, proving (3). The two displayed four-point posets are connected, height-one, and have different numbers of minimal elements: three versus two. Their opposites have respectively one versus two minimal elements. Therefore the posets are neither isomorphic nor anti-isomorphic. Their incidence algebras are correspondingly neither isomorphic nor anti-isomorphic, for example because the quiver of the basic split incidence algebra recovers these orientations. With at most three vertices a connected height-one poset is a singleton, a two-element chain, or a three-vertex \(V\)-shaped poset and its dual, so four is minimal within the stated class. Both witnesses have tree comparability graphs, and (3) identifies their full commuting-idempotent schemes over all fields.

## Verification
The accompanying `verify.py` uses direct multiplication in the incidence algebra, independently enumerating *all idempotents* and *all commuting ordered pairs* over \(\mathbb F_2\) and \(\mathbb F_3\). It checks every individual diagonal coloring fiber against \(q^{d(c)}\) for the four-point star, four-point path, four-point diamond, and three-element chain. For the two four-point trees it obtains 54 idempotents and 1372 commuting pairs over \(\mathbb F_2\), and 128 idempotents and 4000 commuting pairs over \(\mathbb F_3\). The non-tree diamond has 114/4132 and 416/23872 respectively, confirming the interval-closure and non-tree cases are not assumed away. A separate direct graph-coloring enumeration agrees with the edge-subset Potts expansion for \(Q=2,4,8\) and \(q=2,3,5\). Run `python3 verify.py` with Python 3.8 or later and expect `VERIFY_OK`. This is a finite check, not a substitute for the functorial algebraic proof.

## Relationship to prior work
Brion (2013) studies smoothness and conjugacy of *single* idempotents in algebraic monoids. Bilen Can, Casimiro and Malheiro (2022) determine idempotent components of incidence monoids and analyze particular bipartite cases, but the inspected results concern single idempotents rather than schemes of arbitrarily many commuting idempotents and their Tutte equivalence. Santulo, Souza and Yasumura (2019), Lemma 8, establish simultaneous diagonalization for certain orthogonal idempotent families in incidence algebras; that background is explicitly not claimed as new. Sokal (2005) supplies the established Fortuin–Kasteleyn/Tutte representation of weighted graph coloring counts. The specific asserted additional relationship is the functorial, all-characteristic affine-component decomposition of **commuting-idempotent tuple schemes**, their complete determination by the Tutte polynomial, and the minimal nonreconstruction result for incidence algebras. The 2024 article of Kolegov concerns the minimum size of idempotent *generating sets* and an associated hypercube graph embedding; its accessible abstract does not resolve this all-arity commuting-scheme comparison. The result may nonetheless be subsumed by a general theorem in additional specialized literature; absence from the inspected material does not establish absolute priority.

## Limitations
The decomposition is not canonically indexed after forgetting diagonal coordinates. It does not assert that arbitrary posets with the same Tutte polynomial have isomorphic incidence algebras, nor that the commuting-idempotent schemes detect the comparability graph itself. The sharp four-vertex threshold is proved only within **connected height-one** posets, up to isomorphism or anti-isomorphism. The Tutte-polynomial equivalence is stated only for connected comparability graphs; disconnected graphs require component-count conventions. Neither the general classification of arbitrary algebraic idempotent tuples nor a uniqueness claim beyond the searched literature is asserted. No independent mathematical audit has been performed.

## References
- A. D. Sokal, The multivariate Tutte polynomial (alias Potts model) for graphs and matroids, arXiv:math/0503607 (2005-03-25). https://arxiv.org/abs/math/0503607
- M. Brion, On algebraic semigroups and monoids, II, arXiv:1303.3955 (2013-03-16). https://arxiv.org/abs/1303.3955
- E. A. Santulo Jr., J. P. Souza and F. Y. Yasumura, Group gradings on finite dimensional incidence algebras, arXiv:1905.08391 (2019-05-21). https://arxiv.org/abs/1905.08391
- M. Bilen Can, A. Casimiro and A. Malheiro, Idempotent Varieties of Incidence Monoids and Bipartite Posets, arXiv:2208.01073 (2022-08-01). https://arxiv.org/abs/2208.01073
- N. A. Kolegov, Idempotent generators of incidence algebras, Bull. Aust. Math. Soc. 110 (2024), 488–497. https://doi.org/10.1017/S0004972724000078
- J. J. Garcés and M. Khrypchenko, Potent preservers of incidence algebras, Linear Algebra Appl. 635 (2022), 171–200. https://doi.org/10.1016/j.laa.2021.11.020

# Complete clique and maximal-clique spectra of rank-one partial transformations

## Finding

Let \(X\) be an \(n\)-element set with \(n\ge1\). Let \(\mathcal P(X)\) be the semigroup of partial selfmaps, with empty map permitted, and let \(\Gamma_n\) be the simple graph whose vertices are **all nonempty image-rank-one partial maps**; two distinct vertices are adjacent precisely when they commute under composition. Define \(P_n(z)=\sum_{C\text{ clique}}z^{|C|}\), including the empty clique, and \(M_n(z)=\sum_{C\text{ inclusion-maximal clique}}z^{|C|}\).

Put \(d=n-h\) and \(m_d=2^d-1\). For every \(n\ge1\), the exact polynomials are
\[
P_n(z)=1+\sum_{h=1}^n\binom nh\left((1+z)^{m_{n-h}}-1+2^{n-h}z\right)^h
\]
and
\[
M_n(z)=\sum_{h=1}^n\binom nh\left((2^h-1)^{n-h}z^h+\mathbf 1_{h<n}\sum_{e=1}^h\binom he\,2^{(n-h)(h-e)}z^{e(2^{n-h}-1)+h-e}\right).
\]
Their maximum nonzero exponent is
\[
\omega(\Gamma_n)=\max\{n,2^{n-1}-1\}.
\]
For \(n\ge4\), exactly \(n\) cliques achieve this size, one for each fixed image point. These consist of **all** nonempty partial constant maps to that point whose domains avoid it. The formula determines all maximal-clique cardinalities and multiplicities, not just the maximum.

## Assumptions and scope

Every vertex is uniquely \(f_{A,a}:A\to X\), given by \(f_{A,a}(x)=a\) for \(x\in A\), where \(\varnothing\ne A\subseteq X\) and \(a\in X\). We compose partial maps as partial functions, with \(fg=f\circ g\). This is not the symmetric inverse semigroup (domains may have any size), and the vertex set includes both idempotent and square-zero rank-one maps. The induced commuting graph omits the empty map and excludes loops; a clique is pairwise commuting, not necessarily closed under multiplication. All formulas count labeled maps on a fixed \(X\) and require no assumptions about fields.

## Proof

**1. Commutation criterion.** For two vertices \(f_{A,a}\) and \(f_{B,b}\), the composite \(f_{A,a}\circ f_{B,b}\) is zero if \(b\notin A\), and otherwise is the map with domain \(B\) and constant value \(a\). Similarly the reverse composite is zero if \(a\notin B\), and otherwise has domain \(A\) and constant value \(b\). If both products are nonzero and equal, their domains and constant values agree, forcing \(A=B\) and \(a=b\); thus the two vertices are identical. If exactly one product is nonzero, they do not commute. Consequently, **distinct** vertices commute if and only if
\[
 a\notin B\quad\text{and}\quad b\notin A.
\]
This proves the criterion even for the boundary case of two maps with the same image point.

**2. Structure of a clique.** Fix a nonempty clique \(C\), let \(H\subseteq X\) be its set of image points, \(h=|H|\), and \(R=X\setminus H\), \(d=|R|\). For each \(a\in H\), every map in the clique with image \(a\) has domain contained in \(R\cup\{a\}\): domains must avoid every other image point by the criterion. Maps with image \(a\) and domain contained in \(R\) are called *external*; there are \(m_d=2^d-1\) such maps and any selection of them commutes. Maps with image \(a\) and domain containing \(a\) are called *self*; there are \(2^d\) such maps, and two distinct self maps never commute. A self map also fails to commute with any external map at the same image point. Hence for each \(a\in H\) we choose either a nonempty subset of the \(m_d\) external maps or exactly one of the \(2^d\) self maps; choices at different image points commute automatically. The size-generating factor per image point is
\[
((1+z)^{m_d}-1)+2^d z.
\]
There are \(\binom nh\) choices of \(H\). Summing disjointly over \(h\) gives \(P_n(z)\), adding one for the empty clique.

**3. Inclusion-maximality.** For fixed \(H\), a clique can be extended at any image point represented by a nonempty proper subset of the external maps; hence each image point must carry either all external maps (possible only when \(d>0\)) or one self map. If any image point carries all external maps, then every \(r\in R\) occurs in some domain; consequently no new image point \(r\) can be introduced, because its image would violate the criterion against an existing external map. Such a clique is maximal. Choosing the \(e\ge1\) external image points among \(h\), and one of \(2^d\) self domains for each of the remaining \(h-e\), gives \(\binom he2^{d(h-e)}\) maximal cliques of size \(e m_d+h-e\), per fixed \(H\).

If no image point is external, the clique comprises exactly one self map at each point of \(H\). It cannot be enlarged at these existing image points. A new image point \(r\in R\) is allowed exactly when \(r\) is absent from the domain of **every** current map, for then the singleton identity on \(r\) commutes with all of them. Therefore this all-self clique is maximal exactly when the union of its extra domain parts equals \(R\). For each \(r\in R\), the set of those \(h\) self domains containing \(r\) must be nonempty, providing \((2^h-1)^d\) choices. Each has size \(h\). The cases are disjoint and exhaustive, yielding \(M_n(z)\). When \(d=0\), only the all-self case exists and consists of the \(n\) singleton partial identities, all within one clique.

**4. Maximum clique size and uniqueness.** In a fixed image set of size \(h<n\), each image point contributes at most \(2^{n-h}-1\) maps, since \(d\ge1\). Thus the clique size is at most \(h(2^{n-h}-1)\). For \(h\ge2\), the elementary inequality \(h\le2^{h-1}\) implies \(h(2^{n-h}-1)\le2^{n-1}-h<2^{n-1}-1\). With \(h=1\), the bound \(2^{n-1}-1\) is attained exactly by taking every external map. With \(h=n\), the only clique consists of the \(n\) singleton partial identities. This establishes the maximum formula. For \(n\ge4\), \(2^{n-1}-1>n\), so its only maximizers are the \(n\) one-image-point external cliques.

## Verification

The standalone script `check_partial_rank1.py` constructs all \(n(2^n-1)\) nonzero rank-one partial maps for each \(1\le n\le4\), tests commutativity by **direct partial-map composition** rather than by the theorem's adjacency criterion, and independently enumerates all cliques and all inclusion-maximal cliques by bitmask recursion and Bron–Kerbosch recursion. It compares every coefficient of \(P_n\) and \(M_n\), plus their maximum degrees. Observed vertex counts are \(1,6,21,60\), total numbers of cliques (including the empty clique) \(2,8,62,1376\), and maximal-clique counts \(1,5,31,221\), respectively. All coefficients agree. This finite test supports but does not replace the argument for arbitrary \(n\).

## Relationship to prior work

The partial-transformation monoid is the object defined and studied by Cicalò–Fernandes–Schneider [1], whose stated results concern structural generation, order, ranks and presentations, not this induced rank-one commutation graph. Araújo–Bentz–Konieczny [2] study commuting partial **bijections**, excluding the noninjective constant maps with multi-element domains used here. Paulista [3] characterizes maximum commutative subsemigroups and discusses clique numbers of the **full** partial-transformation commuting graph; that does not give all cliques and all inclusion-maximal cliques of its induced rank-one subgraph. The published Boolean-relation rank-one idempotent clique enumeration [4] and rank-one square-zero matrix clique enumeration [5] have different multiplications, vertices, and compatibility criteria. No direct theorem subsuming both enumerators above was identified in the inspected material; a previously implicit equivalent remains a priority risk.

## Limitations

The theorem concerns the induced graph on nonempty rank-one **partial** maps, not all ranks, the full graph, or arbitrary commutative subsemigroups. In particular, a maximal clique in this induced graph need not be maximal in the ambient semigroup's full commuting graph. The expressions classify labeled cliques, not conjugacy classes. The finite checker only covers \(n\le4\). The historical literature comparison does not establish global uniqueness or independent validation.

## References

[1] S. Cicalò, V. H. Fernandes, C. Schneider, *Partial transformation monoids preserving a uniform partition*, arXiv:1210.4775, publicly posted 2012-10-17, https://arxiv.org/abs/1210.4775.

[2] J. Araújo, W. Bentz, J. Konieczny, *The commuting graph of the symmetric inverse semigroup*, arXiv:1205.1664, 2012, https://arxiv.org/abs/1205.1664.

[3] T. Paulista, *Characterizing the largest commutative (full and partial) transformation semigroups of certain types*, arXiv:2511.09495, 2025, https://arxiv.org/abs/2511.09495.

[4] *Clique and maximal-clique enumerators for rank-one idempotent Boolean relations*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-clique-and-maximal-clique-enumerators-for-rank-one-idempotent-bo--a2f16599b2ee.

[5] *Projective geometry and clique spectra of rank-one nilpotent commuting graphs*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-projective-geometry-and-clique-spectra-of-rank-one-nilpotent-com--00e8b0fff4f8.

# A single extremal type coefficient detects a Möbius twist in Henson-graph ladder bases

## Finding
Let \(n\ge4\). Let \(P_n=C_n\square K_2\) be the ordinary two-rail prism and \(M_n\) its Möbius-twisted version, each with \(2n\) vertices and \(3n\) edges. Put \(A_n^{\mathrm P}=L(P_n)\) and \(A_n^{\mathrm M}=L(M_n)\), considered as pointwise-named finite induced parameter graphs in the countable homogeneous \(K_4\)-free graph \(\mathcal H_4\).

Give the two rail edges leaving column \(i\) the same formal weight \(u_i\), and the rung in column \(i\) weight \(v_i\), for \(0\le i<n\). For each complete nonalgebraic singleton type \(p\) over either parameter graph, let \(D(p)\) be its set of **nonneighbors** among the named parameters, and define
\[
F_{\mathrm P,n}(\mathbf u,\mathbf v)=\sum_p\prod_{e\in D(p)}w(e),\qquad
F_{\mathrm M,n}(\mathbf u,\mathbf v)=\sum_p\prod_{e\in D(p)}w(e).
\]
The two formal polynomials, defined over \(\mathbb Z[u_0,\ldots,u_{n-1},v_0,\ldots,v_{n-1}]\), satisfy the exact *inhomogeneous twist cancellation*
\[
\boxed{F_{\mathrm P,n}(\mathbf u,\mathbf v)-F_{\mathrm M,n}(\mathbf u,\mathbf v)=2(-1)^n\prod_{i=0}^{n-1}u_i.}
\]
Thus the entire refined logical one-type distribution is insensitive to the twist except for one rail-only monomial. The identity holds with arbitrarily and independently chosen rung activities \(v_i\) and paired-rail activities \(u_i\).

In particular, giving **all** old parameters nonneighbor weight \(z\), their cardinality-graded spectra \(f_{\mathrm P,n}(z)\), \(f_{\mathrm M,n}(z)\) obey
\[
f_{\mathrm P,n}(z)-f_{\mathrm M,n}(z)=2(-1)^nz^n.
\]
Every coefficient other than the minimum nonneighbor degree \(n\) is identical. Equivalently, with adjacency-graded polynomials \(a_{\mathrm P,n}(z)\) and \(a_{\mathrm M,n}(z)\),
\[
a_{\mathrm P,n}(z)-a_{\mathrm M,n}(z)=2(-1)^nz^{2n}.
\]
The *unweighted* total type numbers differ by exactly \(2(-1)^n\). For instance, the prism and Möbius totals at \(n=4,5,6\) are respectively \((1699,1697)\), \((10895,10897)\), and \((69943,69941)\).

## Assumptions and scope
For \(n\ge4\), vertices are \((i,r)\) with \(i\in\mathbb Z/n\mathbb Z\) and \(r\in\{0,1\}\). The rung at \(i\) joins \((i,0)\) and \((i,1)\). Two rail edges go from column \(i\) to \(i+1\); all use the same row at the next column except the seam from \(n-1\) to \(0\), which preserves rows in \(P_n\) and interchanges rows in \(M_n\). The graphs are simple, cubic and triangle-free. Their line graphs contain no \(K_4\), so both parameter configurations occur as induced finite subgraphs of \(\mathcal H_4\). All parameters are individually named; types identify no distinct parameter vertices and exclude the case in which the new vertex equals a parameter. The polynomial counts logical types, not vertex frequencies.

The label-to-weight identification across the two bases pairs the two parallel rail edges at each column; it does not assert an isomorphism of the underlying graphs or a coordinatewise bijection of the type spaces.

## Proof
**Step 1: types become edge covers.** For any finite induced \(K_4\)-free graph \(A\subset\mathcal H_4\), a singleton's set of *neighbors* in \(A\) must induce a triangle-free graph; conversely every such neighborhood extends to a finite \(K_4\)-free one-point graph and therefore is realized as a nonalgebraic complete one-type by homogeneity and quantifier elimination. When \(A=L(G)\) and \(G\) is a simple cubic triangle-free graph, every triangle of \(L(G)\) consists of all three edges of \(G\) incident to one vertex. Indeed any three pairwise incident distinct edges either form a star or form a triangle in \(G\), and the latter is excluded. Consequently a set \(D\subseteq E(G)\) is the nonneighbor set of one such type exactly when \(D\) meets every three-edge star, i.e. exactly when \(D\) is an edge cover of \(G\). This identifies \(F\) with the weighted edge-cover polynomial of the ladder graph, without changing a weight.

**Step 2: one-site transfer.** For consecutive columns, a binary state \(s=(s_0,s_1)\in\{0,1\}^2\) specifies the two incoming selected rail edges of an edge cover, and \(t=(t_0,t_1)\) the two outgoing selected rail edges. Let \(q_i=v_i\) be the chosen rung weight. If the rung is selected, its contribution is \(v_i\) and both vertices of column \(i\) are covered regardless of rails. If the rung is absent, both vertices must be covered by incoming or outgoing rails. Hence the four-by-four polynomial transfer matrix, with states ordered \(00,01,10,11\), is
\[
B_i(s,t)=u_i^{t_0+t_1}\left(v_i+\mathbf1_{(s_0\lor t_0)\land(s_1\lor t_1)}\right).
\]
The rail weights are counted exactly once, on the outgoing transition. With \(B=B_0B_1\cdots B_{n-1}\), ordinary closure gives \(F_{\mathrm P,n}=\operatorname{tr}B\). Define \(J(s_0,s_1)=(s_1,s_0)\) and also write \(J\) for its permutation matrix. The twisted seam imposes the swapped boundary state, so \(F_{\mathrm M,n}=\operatorname{tr}(BJ)\).

**Step 3: all bulk modes cancel.** Simultaneously swapping the two coordinates in \(s,t\) preserves each \(B_i(s,t)\); hence \(B_i\) commutes with \(J\). The \(+1\) eigenspace of \(J\) has dimension three, while the \(-1\) eigenspace is spanned by \(h=e_{01}-e_{10}\). Directly from the displayed transfer matrix,
\[
B_i h=-u_i h.
\]
Therefore \(B h=(-1)^n(\prod_i u_i)h\), and
\[
\operatorname{tr}B-\operatorname{tr}(BJ)
=2\operatorname{tr}\bigl(B\mid_{\langle h\rangle}\bigr)
=2(-1)^n\prod_i u_i.
\]
This is an identity in the full polynomial ring, proving the finding for every \(n\ge4\), independently of any finite enumeration.

**Step 4: graded consequences.** Every edge cover of a graph with \(2n\) vertices uses at least \(n\) edges, and equality means a perfect matching. Thus the sole differing coefficient of the nonneighbor-graded spectra is the minimum possible degree. There are \(3n\) named line-graph vertices, so replacing nonneighbor count \(k\) by neighbor count \(3n-k\) gives the adjacency-graded identity at degree \(2n\). Setting all weights to one gives the asserted two-unit difference.

## Verification
Run `python3 checker.py` in the directory containing the packaged code. The checker constructs both cubic graphs independently, verifies triangle-freeness, directly enumerates all edge subsets for \(n=4,5,6\), compares all cover-polynomial coefficients and checks the expected two-unit difference. For \(n=4,5\) it independently enumerates triangle-free neighborhoods of the line graphs and compares the resulting type distributions. It also compares direct weighted cover enumeration with transfer counts at unequal site weights and verifies the transfer identity for widths through \(12\). These finite tests support the implementation; the polynomial proof in Step 3 is all-order.

## Relationship to prior work
The generic \(K_4\)-free Henson graph and finite-extension interpretation of types are standard; see Conant [1]. The ordinary edge-cover polynomial was introduced and studied by Akbari and Oboudi [2], and the complete ten-vertex cubic-graph census in Alikhani and Jahari [3] includes pairs differing only at the minimum edge-cover coefficient (a finite special case of the unweighted cancellation pattern). Lekshmi and West [4] determine the parity-sensitive two-unit difference in **perfect-matching counts**, which explains the minimum coefficient but says nothing by itself about the coincidence of *every higher coefficient*. A standard reference [5] tabulates a shared homogeneous recurrence for the two graph families, so the unweighted polynomial relation is not presented as an independent priority claim. The distinct contribution assessed here is the stronger multivariate equality with arbitrarily many independent rung weights and paired-rail weights, together with its full graded one-type interpretation. The known homogeneous recurrences do not specify these inhomogeneous polynomials.

## Limitations
The claim concerns the specified paired-rail weight symmetry and \(n\ge4\); independent weights on the two rails need not satisfy this identity. It does not identify individual types or claim an unweighted identity outside the two stated graph families. Earlier edge-cover recurrences and the perfect-matching parity formula cover important specializations. Full text of [4] could not be inspected during this comparison, and an unindexed multivariate transfer identity could predate the present derivation. No independent review or publication-priority certification is asserted.

## References
1. G. Conant, *Forking and dividing in Henson graphs*, arXiv:1401.1570, first submitted 2014-01-08, https://arxiv.org/html/1401.1570v1.
2. S. Akbari and M. R. Oboudi, *On the edge cover polynomial of a graph*, European Journal of Combinatorics **34** (2013), 297–321, DOI:10.1016/j.ejc.2012.05.005; accessible preprint https://janos.cs.technion.ac.il/COURSES/236603-11/oboudi.pdf.
3. S. Alikhani and S. Jahari, *The edge cover polynomials of cubic graphs of order 10*, arXiv:1312.7506, first submitted 2013-12-29, https://arxiv.org/abs/1312.7506.
4. R. S. Lekshmi and D. B. West, *The Number of Perfect Matchings in Möbius Ladders and Prisms*, arXiv:2003.09602 (2020), https://arxiv.org/abs/2003.09602.
5. E. W. Weisstein, *Edge Cover Polynomial*, MathWorld, https://mathworld.wolfram.com/EdgeCoverPolynomial.html (family recurrences; used as prior coverage, not as an initiating source).

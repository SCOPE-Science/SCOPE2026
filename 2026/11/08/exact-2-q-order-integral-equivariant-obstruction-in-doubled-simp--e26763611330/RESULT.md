# Exact \(2^q\)-order integral equivariant obstruction in doubled simplex boundaries

## Finding
For every integer \(q\ge3\), inflate each vertex of the boundary of the \((q-1)\)-simplex into two signed copies, allowing a simplex to select at most one copy from each original vertex and at most \(q-1\) originals. Denote the resulting simplicial complex by \(X_q\). Let \(W_q=(C_2)^q\rtimes S_q\) be the signed-coordinate permutation group, \(T_q=(C_2)^q\), and \(\varepsilon_q:W_q\to\{\pm1\}\) its determinant character.

There is a canonical exact sequence of integral \(\mathbb Z[W_q]\)-modules
\[
0\longrightarrow\mathbb Z_{\varepsilon_q}
\xrightarrow{\ i\ }\mathbb Z^{\{+,-\}^q}_{\mathrm{or}}
\longrightarrow\widetilde H_{q-2}(X_q;\mathbb Z)
\longrightarrow0.
\]
Here the middle module is the free lattice on oriented facets of the \(q\)-cross-polytope, with signed action induced by coordinate permutation. **The extension class has exact additive order \(2^q\)** in
\[
\operatorname{Ext}^{1}_{\mathbb Z[W_q]}
\bigl(\widetilde H_{q-2}(X_q;\mathbb Z),\mathbb Z_{\varepsilon_q}\bigr).
\]
Its restriction to \(T_q\) generates the cyclic group
\[
\operatorname{Ext}^{1}_{\mathbb Z[T_q]}
\bigl(\widetilde H_{q-2}(X_q;\mathbb Z),\mathbb Z_{\varepsilon_q}\bigr)
\cong\mathbb Z/2^q\mathbb Z.
\]
In particular the exact sequence cannot be split over the integers even for the coordinate-flip subgroup, but it splits over \(\mathbb Z[1/2]\) and hence over \(\mathbb Q\).

The already-known ordinary homotopy formula \(X_q\simeq\bigvee^{2^q-1}S^{q-2}\) supplies context, **not** the originality claim here.

## Assumptions and scope
The vertices are ordered pairs \((j,s)\) with \(j\in\{1,\ldots,q\}\) and \(s\in\{0,1\}\). A face uses distinct \(j\)'s and at most \(q-1\) coordinates. The \((q-1)\)-sphere \(B_q=(S^0)^{*q}\) is the full cross-polytope boundary, and \(X_q=B_q^{(q-2)}\) is its codimension-one skeleton. The group \(W_q\) acts by permuting coordinates and interchanging the two signs in each coordinate. All homology and module maps are integral, unless another ring is explicitly indicated. \(\operatorname{Ext}^1\) is the usual derived functor in the category of left modules over the stated integral group ring; the order is the order of the Yoneda extension class, not the order of an element in ordinary homology.

## Proof
**1. Geometric exact sequence.** Because \(B_q\cong S^{q-1}\) and \(q\ge3\), the long exact sequence of \((B_q,X_q)\) reduces to
\[
0\to H_{q-1}(B_q;\mathbb Z)\to H_{q-1}(B_q,X_q;\mathbb Z)
\to\widetilde H_{q-2}(X_q;\mathbb Z)\to0.
\]
The relative chain group is free on its \(2^q\) facets since \(X_q\) contains every proper face. The top integral orientation of the cross-polytope boundary carries the determinant character \(\varepsilon_q\). Thus this is the asserted exact sequence, including natural equivariance.

**2. Explicit fundamental cycle and signed augmentation.** Orient a facet by increasing coordinate index, write \(e_b\) for the facet choosing signs \(b=(b_1,\ldots,b_q)\in\{0,1\}^q\), and set
\[
z_q=\sum_b(-1)^{\sum_jb_j}e_b.
\]
Each codimension-one face occurs in two facets with opposite coefficients, so \(\partial z_q=0\), and \(z_q\) generates the top integral orientation lattice. An element \((t,\sigma)\in T_q\rtimes S_q\) sends \(e_b\) to \(\operatorname{sgn}(\sigma)e_{t+\sigma b}\), using bit-vector addition modulo two; it sends \(z_q\) to \(\varepsilon_q(t,\sigma)z_q\), where \(\varepsilon_q(t,\sigma)=(-1)^{\sum_jt_j}\operatorname{sgn}(\sigma)\).

Define the lattice morphism \(a:E_q\to\mathbb Z_{\varepsilon_q}\) by \(a(e_b)=(-1)^{\sum_jb_j}\). This is \(W_q\)-equivariant and satisfies
\[
a(z_q)=\sum_b1=2^q.
\]

**3. Sharp lower bound after restriction.** As a \(\mathbb Z[T_q]\)-module, \(E_q\) is the regular free module \(\mathbb Z[T_q]\): the coordinate flips act simply transitively on its oriented-facet basis. Therefore \(\operatorname{Ext}^1_{\mathbb Z[T_q]}(E_q,\mathbb Z_{\varepsilon_q})=0\), and
\[
\operatorname{Hom}_{\mathbb Z[T_q]}(E_q,\mathbb Z_{\varepsilon_q})
\cong\mathbb Z.
\]
Under these identifications, the restriction map to the embedded orientation line is precisely multiplication by \(2^q\), because a \(T_q\)-equivariant map is determined by its integer value on \(e_0\), and its value on \(z_q\) is \(2^q\) times that integer. The long exact Hom–Ext sequence gives
\[
\operatorname{Ext}^{1}_{\mathbb Z[T_q]}(M_q,\mathbb Z_{\varepsilon_q})
\cong\operatorname{coker}(\mathbb Z\xrightarrow{2^q}\mathbb Z)
\cong\mathbb Z/2^q\mathbb Z,
\]
where \(M_q=\widetilde H_{q-2}(X_q;\mathbb Z)\). The image of the displayed extension is the connecting-map image of the identity of \(\mathbb Z_{\varepsilon_q}\), hence is a generator. Its order before restriction is therefore at least \(2^q\).

**4. Matching upper bound under all symmetries.** Applying \(\operatorname{Hom}_{\mathbb Z[W_q]}(-,\mathbb Z_{\varepsilon_q})\) to the original exact sequence, the connecting map sends the identity of the orientation line to its extension class. Since the \(W_q\)-equivariant map \(a\) restricts to \(2^q\) times the identity, \(2^q\) times the extension class vanishes. The lower bound from \(T_q\) proves that its exact order is \(2^q\).

The same map divided by \(2^q\) yields an equivariant retraction after inverting two. This does not claim a geometric equivariant wedge decomposition or a splitting over \(\mathbb Z\).

## Verification
The standalone standard-library script `verify.py` exhaustively checks dimensions \(3\le q\le8\). It reconstructs every oriented facet, checks cancellation on every codimension-one face, tests the signed coefficient and facet actions for the generators of \(W_q\), and checks the reduced Euler characteristic and signed-augmentation period. To run: `python3 verify.py`. The expected deterministic output is recorded in `verification_output.txt`. This finite replay corroborates the explicit formulas; the Hom–Ext argument proves the unbounded \(q\)-statement.

## Relationship to prior work
Björner–Wachs–Welker, *Poset fiber theorems* (2005), Theorem 6.2 and Corollary 6.3, give the ordinary homotopy and integral homology of vertex inflations; Section 8, especially Corollary 8.5, gives equivariant homology representations **only over a field of characteristic zero**. Thus the known sphere count and rational symmetry splitting are not claimed as new. Ayzenberg–Khoroshavkina (first publicly posted 2026-02-09, arXiv:2602.08694v1), §4.2 and §7.2, extend and contextualize inflation formulas but do not calculate integral equivariant extension orders. Ayzenberg–Rukhovich (arXiv:2012.07600v1), §6 and Remark 7.9, treat functoriality of other inflation decompositions and explicitly distinguish categories that do not admit such functorial wedge decomposition. The present exact \(2^q\)-order obstruction is a distinct module-level integral assertion that cannot be inferred from a nonequivariant wedge formula or a characteristic-zero decomposition.

## Limitations
The obstruction refers to a specific canonical relative-chain extension, not to every possible comparison of homology representations or a stable-equivalence obstruction. It is formulated for the two-copy inflation of a simplex boundary, not general vertex multiplicities or arbitrary complexes. Its existence does not imply torsion in the ordinary integral homology, which is free. Independent validation has not been performed, and an equivalent unindexed group-ring computation cannot be ruled out absolutely.

## References
1. A. Ayzenberg and N. Khoroshavkina, *Homotopy types of finite étale spaces and generalized inflations*, arXiv:2602.08694v1 (first public 2026-02-09), §§4.2, 7.2; https://arxiv.org/html/2602.08694 .
2. A. Björner, M. L. Wachs and V. Welker, *Poset fiber theorems*, Trans. Amer. Math. Soc. 357 (2005), 1877–1899, §§6, 8; https://www.math.miami.edu/~wachs/papers/fibers.pdf .
3. A. Ayzenberg and A. Rukhovich, *Clique complexes of multigraphs, edge inflations, and tournaplexes*, arXiv:2012.07600v1 (2020), §§6–7; https://arxiv.org/pdf/2012.07600 .

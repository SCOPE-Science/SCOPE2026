# Prime polygon associahedral quotients are explicit lens spaces

## Finding
Let \(\mathcal A_n\) be the simplicial complex whose vertices are the diagonals of a convex regular \(n\)-gon and whose faces are collections of pairwise noncrossing diagonals. Let \(C_n=\langle r\rangle\) rotate polygon vertices forward by one position. For every integer \(n\ge4\), the action of \(C_n\) on the geometric realization \(|\mathcal A_n|\) is free **if and only if** \(n\) is prime. For every odd prime \(p\ge7\), its quotient is homeomorphic to the explicitly weighted lens space

\[
|\mathcal A_p|/C_p\ \cong\ L\bigl(p;2,3,\ldots,(p-1)/2\bigr)
= S\!\left(\bigoplus_{j=2}^{(p-1)/2}\mathbb C_j\right)/C_p,
\]

where \(r\) acts on \(\mathbb C_j\) as multiplication by \(\exp(2\pi i j/p)\). In particular, with \(m=(p-3)/2\), the quotient is a closed orientable manifold of dimension \(2m-1=p-4\), and

\[
\pi_1(|\mathcal A_p|/C_p)\cong C_p,\qquad
\widetilde H_k(|\mathcal A_p|/C_p;\mathbb Z)\cong
\begin{cases}
\mathbb Z/p\mathbb Z,&k\in\{1,3,\ldots,p-6\},\\
\mathbb Z,&k=p-4,\\
0,&\text{otherwise}.
\end{cases}
\]

For an integral cohomology generator \(u\in H^2(|\mathcal A_p|/C_p;\mathbb Z)\cong\mathbb Z/p\mathbb Z\), every power \(u^k\) is nonzero for \(1\le k\le (p-5)/2\). The first genuinely higher-dimensional example is the three-manifold \(L(7;2,3)\), equivalently \(L(7;1,5)\) after changing the cyclic generator.

## Assumptions and scope
Write \(P\) for the filled polygon. The polygon has labeled vertices \(v_i=(\cos(2\pi i/n),\sin(2\pi i/n))\) for \(i=0,\ldots,n-1\), and its diagonals do not include boundary edges. A face is a *set* of diagonals; the geometric quotient is the actual topological orbit space, not a naive quotient abstract simplicial complex. A lens space \(L(p;q_1,\ldots,q_m)\) is the quotient of the unit sphere in \(\mathbb C^m\) by the specified free diagonal action. The five-gon case is a free rotation of a circle and has circle quotient; the asserted fundamental-group and integral-homology formula begins at \(p=7\). All statements concern the standard simplicial diagonal complex, not other realizations or subdivisions chosen without equivariance.

## Proof
**1. An equivariant simplicial model.** For any triangulation \(T\) of the regular polygon, write its GKZ vector \(a(T)\in\mathbb R^n\), whose coordinate \(a_i(T)\) is the sum of the areas of triangles of \(T\) incident to vertex \(v_i\). Let \(P_n\) be the convex hull of these vectors. The classical secondary-polytope theorem states that \(P_n\) is a simple polytope of dimension \(n-3\), with a facet for each polygon diagonal and nonempty intersections of facets exactly for collections of noncrossing diagonals. Rotating the polygon permutes the coordinates of every GKZ vector, so the resulting \(C_n\)-action on \(P_n\) is orthogonal and preserves this facet correspondence.

**2. Exact affine direction.** Every triangulation satisfies the two vector identities

\[
\sum_i a_i(T)=3\operatorname{area}(P),\qquad
\sum_i a_i(T)v_i=3\int_P x\,dA(x),
\]

because each triangle contributes its area once per vertex, and its three vertices sum to three times its centroid. Consequently the difference of two GKZ vectors lies in

\[
W_n=\left\{y\in\mathbb R^n:\ \sum_i y_i=0,\quad
\sum_i y_i\cos(2\pi i/n)=0,\quad
\sum_i y_i\sin(2\pi i/n)=0\right\}.
\]

The three constraints are independent for \(n\ge4\), and the secondary-polytope dimension theorem shows that the affine direction of \(P_n\) is **all** of \(W_n\), not a proper subspace. Let \(b\) be the average of the GKZ vectors over all triangulations. Since they are the vertices of the full-dimensional \(P_n\), \(b\) lies in its relative interior. It is fixed by rotations; thus \(P_n-b\subset W_n\) is a full-dimensional convex polytope containing the origin in its interior.

**3. Equivariant radial sphere.** In \(W_n\) take the Euclidean polar

\[
Q_n=\{w\in W_n:\langle w,x\rangle\le1\text{ for all }x\in P_n-b\}.
\]

Because \(P_n\) is simple, \(Q_n\) is simplicial; its vertices correspond to facets of \(P_n\), and its simplices correspond to pairwise noncrossing sets of diagonals. This is an actual \(C_n\)-equivariant simplicial identification \(\mathcal A_n\cong\partial Q_n\). As the origin is interior to \(Q_n\), radial projection \(w\mapsto w/\|w\|\) is a homeomorphism \(\partial Q_n\to S(W_n)\). It commutes with rotations because the action is orthogonal.

**4. Fourier weights and sharp freeness.** Under cyclic permutation of \(n\) real coordinates, the constant Fourier mode is weight zero and the planar coordinate modes \(\cos(2\pi i/n),\sin(2\pi i/n)\) have weights \(\pm1\). Orthogonality of discrete Fourier characters gives

\[
W_n=\bigoplus_{2\le j<n/2} V_j\ \oplus\
\begin{cases}V_{n/2},&2\mid n,\\0,&2\nmid n,\end{cases}
\]

where \(V_j\) is a real rotation plane with eigenvalues \(\exp(\pm2\pi i j/n)\), and \(V_{n/2}\) is the one-dimensional sign representation when it occurs. If \(n=p\) is prime, all nonzero modes are faithful, so no nonidentity rotation fixes a nonzero vector of \(W_p\). Thus the action on its sphere and on \(|\mathcal A_p|\) is free. Conversely, for composite \(n\ge4\), choose a proper divisor \(d\) with \(2\le d\le n/2\). The nonzero real Fourier mode of weight \(d\) belongs to \(W_n\) and is fixed pointwise by the nonidentity rotation \(r^{n/d}\). Its unit vectors give fixed points on \(S(W_n)\). This proves the equivalence for all \(n\ge4\).

**5. Exact lens-space identification.** When \(p\ge7\) is prime, the real representation \(W_p\) is the direct sum of the complex one-dimensional characters \(\mathbb C_j\), for \(j=2,\ldots,(p-1)/2\), after choosing compatible Fourier complex coordinates. Therefore the radial identification in Step 3 descends to the displayed **homeomorphism**, not merely a homology isomorphism. Standard lens-space covering theory gives \(\pi_1=C_p\), the asserted integral homology in degrees below the top dimension, and an orientation class in the top degree. The integral cohomology ring in degrees strictly below the top has successive nonzero powers of the degree-two generator, equivalently the nonzero powers of the standard class in \(H^*(BC_p;\mathbb Z)\) through \(2m-2\). In dimension three, multiplying both lens weights \((2,3)\) by \(2^{-1}\equiv4\pmod7\) changes the chosen generator and gives \((1,5)\).

## Verification
A standalone, standard-library-only program `verify_associahedral_lens.py` independently enumerates every triangulation of regular polygons with \(n=5,7,11\), confirms the Catalan counts \(5,42,4862\), checks that no nonidentity rotation fixes any maximal triangulation, checks all nonidentity rotation fixed-eigenspace dimensions in \(W_n\), and verifies explicit fixed modes for composite \(n=4,6,8,9,10,12,15\). The output concludes `ASSOCIAHEDRAL_LENS_FINITE_CHECKS_OK`. These are finite consistency tests only; Steps 1–5, especially the secondary-polytope dimension theorem, prove the infinite family.

## Relationship to prior work
Reiner, Stanton and White established the cyclic sieving phenomenon for polygon dissections, including rotation-fixed *finite sets* of faces (Theorem 7.1), but not the topology of the geometric orbit space. Ceballos, Santos and Ziegler review the GKZ secondary-polytope realization and its precise dimension and facet structure (Theorem 3.2 and Corollary 3.4). Fossas Tenas and McCammond state that regular-polygon isometries act by isometries on standard associahedra (Proposition 1.5). The present result identifies the missing real Fourier representation, constructs an equivariant radial homeomorphism, and derives the exact lens weights and all-prime torsion pattern. The freeness criterion concerns *every geometric point*, a stronger condition than absence of fixed triangulations. No claim is made that the source polytope construction, cyclic sieving, or standard lens-space homology is new.

## Limitations
The result determines ordinary geometric rotation quotients only; it does not classify reflection-containing group quotients, composite rotation quotient singularities, or the lens spaces' canonical metric geometry. The closed-manifold and integral-homology formulas in the Finding require prime \(p\ge7\); for prime \(p=5\) the quotient is a circle. Novelty was compared against identified primary literature and indexed mathematical records, but unindexed equivalent analyses remain a publication-priority risk. Independent external mathematical review has not been performed.

## References
1. V. Reiner, D. Stanton and D. White, *The cyclic sieving phenomenon*, Journal of Combinatorial Theory, Series A **108** (2004), 17–50, Theorem 7.1; publicly available July 24, 2004. DOI: https://doi.org/10.1016/j.jcta.2004.04.009 ; accessible full text: https://sites.math.washington.edu/~billey/classes/561.fall.2021/past.articles/reiner.stanton.white.pdf
2. C. Ceballos, F. Santos and G. M. Ziegler, *Many non-equivalent realizations of the associahedron*, first arXiv posting September 26, 2011, arXiv:1109.5544, Section 3.1. https://arxiv.org/abs/1109.5544
3. A. Fossas Tenas and J. McCammond, *The infinite cyclohedron and its automorphism group*, first arXiv posting November 13, 2014, arXiv:1411.3647, Definitions 1.3–1.4 and Proposition 1.5. https://arxiv.org/abs/1411.3647
4. Classical generalized lens-space definitions and homology, as in https://encyclopediaofmath.org/wiki/Lens_space .

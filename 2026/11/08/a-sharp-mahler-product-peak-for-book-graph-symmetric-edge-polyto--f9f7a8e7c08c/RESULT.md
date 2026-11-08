# A sharp Mahler-product peak for book-graph symmetric edge polytopes

## Finding

For each integer \(m\geq 1\), let \(G_m\) be the **triangular book** consisting of \(m\) triangles sharing a common edge, equivalently the complete tripartite graph \(K_{1,1,m}\). Let
\[
P_m=\operatorname{conv}\{\pm(e_u-e_v):uv\in E(G_m)\}
\subset\{x\in\mathbb R^{m+2}:\sum_i x_i=0\}.
\]
The dimension is \(d=m+1\). Write \(P_m^\circ\) for its intrinsic polar with respect to the standard inner product on its linear span, and \(\Pi(P_m)=\operatorname{vol}_d(P_m)\operatorname{vol}_d(P_m^\circ)\). Then
\[
\boxed{\frac{d!}{4^d}\,\Pi(P_m)
=R_m=\frac{m+2}{m+1}\left(1-2^{-(m+1)}\right).}
\]
Moreover, \(R_1<R_2<R_3\), whereas \(R_{m+1}<R_m\) for every \(m\ge3\). Hence the **unique global maximizer** over triangular books is the three-page book, with \(R_3=75/64\). Every finite member satisfies \(R_m>1\), and \(R_m\downarrow1\) as \(m\to\infty\); more precisely,
\[
\lim_{m\to\infty}(m+1)(R_m-1)=1.
\]
The value \(1\) is the Hanner-polytope benchmark for this normalization, not a claim of an all-polytopes Mahler bound.

## Assumptions and scope

All graphs are unweighted, finite, connected and simple. The two hubs of \(G_m\) are joined to each other and to all \(m\) mutually nonadjacent leaves. We use the natural root-vector realization displayed above, with the body centered at the origin. Because \(P_m=-P_m\) and has nonempty relative interior, the origin is its Santaló point and its intrinsic volume product is well-defined. Both volumes are in the \(d\)-dimensional Euclidean measure of the zero-sum hyperplane. The proof evaluates volumes using dual coordinate systems; their Jacobian factors cancel in the product.

## Proof

**1. Dual coordinates.** Designate one hub as the base vertex. The \(d=m+1\) roots pointing from that vertex to the other hub and to the leaves form an integer coordinate basis of the zero-sum hyperplane. Write a primal coordinate vector as \((z,y_1,\ldots,y_m)\), and its algebraic dual as \((t,w_1,\ldots,w_m)\), with pairing \(zt+\sum_i y_iw_i\). The root vertex set of \(P_m\) in these coordinates is
\[
\{\pm e_0,\ \pm e_i,\ \pm(e_0-e_i):1\le i\le m\}.
\]
Thus its algebraic polar is exactly
\[
Q_m=\{(t,w):|t|\le1,\ |w_i|\le1,\ |t-w_i|\le1\ (1\le i\le m)\}.
\]
As \(P_m\) and \(Q_m\) are a dual pair in mutually paired bases, the determinant of any change to orthonormal coordinates multiplies one volume and divides the other by the same factor. Consequently their ordinary coordinate volumes multiply to the intrinsic Euclidean Mahler product.

**2. Polar volume.** Fix \(t\in[-1,1]\). Each leaf coordinate \(w_i\) ranges independently in the interval
\[
[\max\{-1,t-1\},\min\{1,t+1\}],
\]
whose length is \(2-|t|\). By Fubini's theorem,
\[
\operatorname{vol}_{\mathrm{coord}}(Q_m)
=\int_{-1}^{1}(2-|t|)^m\,dt
=\frac{2(2^{m+1}-1)}{m+1}.
\]

**3. Primal volume.** Put \(A=\sum_i\max(y_i,0)\), \(B=\sum_i\max(-y_i,0)\), and \(S=A+B=\sum_i|y_i|\). Maximizing the linear functional \(zt+\sum_i y_iw_i\) over the above polar separately on \(0\le t\le1\) and \(-1\le t\le0\) gives exactly
\[
h_{Q_m}(z,y)=\max\{S,A+z,B-z\}.
\]
Indeed, for \(t\ge0\) the maximizing leaf coordinates equal \(1\) when \(y_i\ge0\), and \(t-1\) when \(y_i<0\); the resulting objective is \(S+(z-B)t\). For \(t\le0\), the maximizing choices are \(t+1\) when \(y_i\ge0\) and \(-1\) when \(y_i<0\); the objective is \(S+(z+A)t\). Since \(P_m=Q_m^\circ\), it follows without omitted facets that
\[
P_m=\{(z,y): S\le1,\ B-1\le z\le1-A\}.
\]
For each \(y\) in the \(m\)-dimensional \(\ell_1\)-unit ball, the permitted interval of \(z\) has length \(2-S\). The \(\ell_1\)-unit ball has volume \(2^m/m!\), and by integration on its \(2^m\) standard simplices its mean \(S\) is \(m/(m+1)\). Therefore
\[
\operatorname{vol}_{\mathrm{coord}}(P_m)
=\int_{\sum|y_i|\le1}(2-S)\,dy
=\frac{2^m(m+2)}{(m+1)!}.
\]
Multiplying with the polar formula, using \(d=m+1\) and dividing by \(4^d/d!\), yields the formula for \(R_m\).

**4. Unique maximum.** A direct common-denominator calculation gives
\[
R_{m+1}-R_m
=\frac{m^2+4m+5-2^{m+2}}{2^{m+2}(m+1)(m+2)}.
\]
The numerator is positive for \(m=1\) and \(m=2\), and negative at \(m=3\). To prove negativity for every later integer, observe that the strict inequality \(2^{m+2}>m^2+4m+5\) holds at \(m=3\) since \(32>26\), and propagation from \(m\) to \(m+1\) follows from
\[
2(m^2+4m+5)-[(m+1)^2+4(m+1)+5]=m^2+2m>0.
\]
Thus the complete strict monotonicity classification follows for all \(m\ge1\), and evaluation gives \(R_3=75/64\). Finally,
\[
R_m-1=\frac{2^{m+1}-m-2}{(m+1)2^{m+1}}>0.
\]
The strict sign follows at \(m=1\) from \(4>3\) and propagates by doubling. The same expression shows \((m+1)(R_m-1)\to1\), completing the proof.

## Verification

The accompanying `check.py` verifies the exact rational formulas and the difference identity for \(1\le m\le199\), and tests the predicted sign pattern at those parameters. In addition, for \(1\le m\le4\), it constructs the original root-vertex hull and its dual half-space intersection, computes facet triangulations numerically solely to find their incidence sets, and evaluates all simplex determinants as **exact integers** using fraction-free elimination. The resulting exact rational primal and polar volumes match the formulas. The all-integer theorem, notably the strict monotonicity and limit, follows from the analytical calculations above; finite tests are not used as an infinite proof.

## Relationship to prior work

The symmetric edge-polytope framework and its relation to finite Lipschitz-free spaces are standard. D'Alì--Delucchi--Michałek describe general symmetric edge-polytope geometry; Alexander--Fradelizi--García-Lirola--Zvavitch develop volume-product geometry for Lipschitz-free spaces. Crucially, Ohsugi--Tsuchiya's theorem on suspensions of cactus graphs already determines the **primal normalized volume** for this family (the suspension of a star), equal to \(2^m(m+2)\); that known quantity is **not** presented as a novel result here. Recent work of Higashitani--Mori identifies triangular books as an exceptional family in Minkowski decomposability. The present claim is the evaluated polar volume together with the resulting complete **normalized Mahler-product profile and sharp three-page extremum**. The inspected prior statements do not establish that profile; this is a best-knowledge literature comparison, not a guarantee of historical priority.

## Limitations

The theorem concerns only unweighted triangular book graphs \(K_{1,1,m}\); it does not claim comparable monotonicity for arbitrary graphs, weighted books, or other edge polytopes. The affine-invariant volume product is determined, but this does not address finer face numbers or isotropic constants. A complete search of all non-digitized literature is impossible, so an equivalent previously published specialized polar formula remains a residual priority risk. No independent mathematical audit has been performed.

## References

1. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193, initial public preprint 2019-10-11. https://arxiv.org/abs/1910.05193
2. M. Alexander, M. Fradelizi, L. C. García-Lirola, A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, initial public preprint 2019-11-24. https://arxiv.org/abs/1911.10642
3. H. Ohsugi, A. Tsuchiya, *Symmetric edge polytopes and matching generating polynomials*, arXiv:2008.08621, initial public preprint 2020-08-19. https://arxiv.org/abs/2008.08621
4. A. Higashitani, H. Mori, *Minkowski decomposability of symmetric edge polytopes*, arXiv:2608.02445, initial public preprint 2026-08-03. https://arxiv.org/abs/2608.02445

# A sharp Löwner ellipsoid edge-invisibility threshold for book-graph symmetric edge polytopes

## Finding
For each integer \(m\ge 2\), let \(B_m=K_2\vee\overline{K}_m\) be the book graph consisting of \(m\) triangles sharing one edge. Write its hubs as \(h_1,h_2\), its remaining vertices as \(z_1,\ldots,z_m\), and set \(d=m+1\). In the Euclidean hyperplane \(H=\{x\in\mathbb R^{m+2}:\sum_i x_i=0\}\) define the symmetric edge polytope
\[
P_m=\operatorname{conv}\{\pm(e_i-e_j):ij\in E(B_m)\}.
\]
Let \(a=e_{h_1}-e_{h_2}\), \(c=(m,m,-2,\ldots,-2)\), and let \(\Pi_a\) and \(\Pi_c\) denote the orthogonal projections in \(H\) onto their spans; put \(\Pi_\ell=I_H-\Pi_a-\Pi_c\). Define
\[
(w_m,v_m)=\begin{cases}(2/9,1/9),&m=2,\\(1/(2m),0),&m\ge3,\end{cases}
\]
and
\[
\lambda_\ell=2w_m,\qquad \lambda_a=mw_m+2v_m,\qquad \lambda_c=(m+2)w_m.
\]
**The unique minimum-volume enclosing ellipsoid** of \(P_m\), in its intrinsic Euclidean metric, is
\[
E_m=\left\{x\in H:
\frac{\|\Pi_\ell x\|^2}{\lambda_\ell}+
\frac{\|\Pi_a x\|^2}{\lambda_a}+
\frac{\|\Pi_c x\|^2}{\lambda_c}\le d\right\}.
\]
Its center is the origin, its squared principal semiaxis lengths are \(d\lambda_\ell\) (multiplicity \(m-1\)), \(d\lambda_a\), and \(d\lambda_c\), and its intrinsic volume is
\[
\operatorname{vol}_{d}(E_m)=
\begin{cases}
32\pi/9,&m=2,\\[2pt]
\displaystyle \kappa_{m+1}(m+1)^{(m+1)/2}
\sqrt{\frac{m+2}{4m^{m}}},&m\ge3,
\end{cases}
\]
where \(\kappa_d=\pi^{d/2}/\Gamma(d/2+1)\) is the Euclidean unit-ball volume.

For \(m=2\), **all ten** vertices of \(P_m\) lie on \(\partial E_m\). For \(m=3\), **all fourteen** vertices lie on \(\partial E_m\), although the optimal weight of the common hub edge is zero. For every \(m\ge4\), **exactly the \(4m\) spoke vertices** \(\pm(e_{h_i}-e_{z_j})\) lie on \(\partial E_m\): the two vertices \(\pm(e_{h_1}-e_{h_2})\) lie strictly inside. Thus the exact contact transition occurs at \(m=3\) / \(m=4\).

Moreover, if \(Q_m\) is the symmetric edge polytope of the complete bipartite spoke graph \(K_{2,m}\), then \(Q_m\subsetneq P_m\), yet **the two distinct polytopes have precisely the same Löwner ellipsoid for every \(m\ge3\)**. For \(m=2\), their unique enclosing ellipsoids differ, with exact volume ratio \(16/(9\sqrt3)\) in the order \(P_2/Q_2\). These assertions collectively form one edge-invisibility and contact-transition theorem.

## Assumptions and scope
All graphs here are finite, undirected, and simple. Every root \(e_i-e_j\) uses the standard coordinate basis and has Euclidean length \(\sqrt2\); no graph-metric or unimodular change of metric is made. The ellipsoid and volume are computed in the affine hull \(H\) with its inherited Euclidean inner product, **not** in \(\mathbb R^{m+2}\). The graph has \(m+2\) vertices and \(2m+1\) edges, and \(P_m\) is full-dimensional in \(H\) because the graph is connected. The integer range is exactly \(m\ge2\).

## Proof
**1. Covariance and orthogonal eigenvalues.** For each undirected graph edge \(ij\), let \(b_{ij}=e_i-e_j\); the sign does not affect \(b_{ij}b_{ij}^{T}\). Give each of the \(2m\) spoke edges weight \(w\), and the common edge weight \(v\), with \(2mw+v=1\). Define the symmetric matrix on \(H\)
\[
C(w,v)=w\sum_{j=1}^{m}\sum_{i=1}^{2} b_{h_i z_j}b_{h_i z_j}^{T}
+v b_{h_1h_2}b_{h_1h_2}^{T}.
\]
When \(w>0\), the spokes alone span \(H\), hence \(C(w,v)\) is positive definite on \(H\). The orthogonal decomposition \(H=\operatorname{span}\{a\}\oplus\operatorname{span}\{c\}\oplus H_\ell\), where \(H_\ell\) consists of vectors with zero hub coordinates and zero sum of leaf coordinates, yields
\[
C(w,v)=(mw+2v)\Pi_a+(m+2)w\Pi_c+2w\Pi_\ell.
\]
Here \(\dim H_\ell=m-1\). Consequently,
\[
\det_H C(w,v)=(2w)^{m-1}(mw+2v)(m+2)w.
\]

**2. The two edge leverages.** Set \(C=C(w,v)\). For either spoke root \(b\), its squared orthogonal projections onto the \(a\), \(c\), and \(H_\ell\) spaces are \(1/2\), \((m+2)/(2m)\), and \((m-1)/m\), respectively. The hub root \(a\) lies entirely in the first space and has squared norm \(2\). Therefore
\[
R_{\mathrm{spoke}}=b^TC^{-1}b=\frac{1}{2w}+\frac{1}{2(mw+2v)},
\qquad R_{\mathrm{hub}}=a^TC^{-1}a=\frac{2}{mw+2v}.
\]
The inverse is understood on \(H\), and both signs of each root have the same leverage. These formulas need no pseudoinverse outside \(H\).

**3. Exact feasible weights and contacts.** Since \(v=1-2mw\), the determinant becomes \(2^{m-1}(m+2)w^m(2-3mw)\). Its logarithmic derivative vanishes at \(w=2/[3(m+1)]\); on the feasible interval \(0<w\le1/(2m)\), this point is feasible exactly when \(m\le3\). The maximizing weights are therefore \((w_2,v_2)=(2/9,1/9)\), and \((w_m,v_m)=(1/(2m),0)\) for \(m\ge3\). This one-variable calculation also independently motivates the threshold.

For \(m=2\), substitution gives \(R_{\mathrm{spoke}}=R_{\mathrm{hub}}=3=d\). For \(m\ge3\), substitution gives \(R_{\mathrm{spoke}}=m+1=d\), while \(R_{\mathrm{hub}}=4\), which equals \(d\) only at \(m=3\) and is strictly less than \(d\) for every \(m\ge4\). Thus the displayed ellipsoid contains **every** vertex of \(P_m\), and has exactly the asserted contact vertices.

**4. Global enclosing-ellipsoid minimality and uniqueness.** Write \(C_m=C(w_m,v_m)\); it is positive definite and \(2mw_m+v_m=1\). The proposed ellipsoid \(x^TC_m^{-1}x\le d\) is feasible by step 3. Consider any enclosing ellipsoid of \(P_m\) of the general, possibly nonsymmetric, off-center form
\[
\mathcal E(y,S)=\{x\in H:(x-y)^TS^{-1}(x-y)\le d\},\quad S\succ0.
\]
For each root \(\pm b\) of \(P_m\), average the two containment inequalities to obtain \(b^TS^{-1}b+y^TS^{-1}y\le d\). Multiply by its corresponding nonnegative weight and sum over the \(2m+1\) undirected edges. Because the weights add to one,
\[
\operatorname{tr}_H(S^{-1}C_m)+y^TS^{-1}y\le d.
\]
For the \(d\) positive eigenvalues of \(S^{-1/2}C_mS^{-1/2}\), arithmetic–geometric mean gives
\[
\left(\frac{\det_H C_m}{\det_H S}\right)^{1/d}
\le\frac{\operatorname{tr}_H(S^{-1}C_m)}{d}\le1.
\]
Since ellipsoid volume is \(\kappa_d d^{d/2}\sqrt{\det_H S}\), no enclosing ellipsoid has smaller volume. Equality forces \(y=0\) and \(S^{-1/2}C_mS^{-1/2}=I_H\), hence \(S=C_m\); uniqueness holds globally. This argument also covers weights vanishing on the hub edge when \(m\ge3\).

**5. Volume and the invisible-edge transition.** For \(m\ge3\), the eigenvalues of \(C_m\) are \(1/m\) with multiplicity \(m-1\), \(1/2\), and \((m+2)/(2m)\). Their product is \((m+2)/(4m^m)\). For \(m=2\), the eigenvalues are \(4/9\), \(2/3\), and \(8/9\); their product is \(64/243\), giving \(32\pi/9\) after multiplying by \(\kappa_3 3^{3/2}\).

For \(K_{2,m}\), the uniform spoke weights \(w=1/(2m)\) already give leverage \(d\) on all its roots, so the same certificate establishes that its Löwner ellipsoid is \(x^TC(1/(2m),0)^{-1}x\le d\). For \(m\ge3\), this is exactly \(E_m\), even though the hub roots are additional vertices in \(P_m\): strictness of \(Q_m\subsetneq P_m\) follows because a root \(e_{h_1}-e_{h_2}\), of norm \(\sqrt2\), cannot lie in the convex hull of different roots of the same norm by strict convexity of the Euclidean sphere. When \(m=2\), \(\det_H C_{K_{2,2}}=1/4\) whereas \(\det_H C_2=64/243\), yielding the claimed ratio \(16/(9\sqrt3)\). This completes the proof.

## Verification
The self-contained standard-library Python program `verify_book_ellipsoid.py` constructs the weighted graph Laplacian and its exact rational inverse on \(H\) for every integer \(2\le m\le12\). It independently reconstructs the three orthogonal projection matrices, verifies their covariance spectral decomposition and inverse, evaluates every hub and spoke leverage exactly, and counts the contact edge pairs. Its successful completion prints `EXACT_CHECKS_PASS`. Run with `python3 verify_book_ellipsoid.py` from the directory holding this file. The finite computation is a consistency check only: step 4, not enumeration, proves the infinite-dimensional theorem for all \(m\ge2\).

## Relationship to prior work
D'Alì, Delucchi and Michałek (arXiv:1910.05193) develop symmetric edge polytopes and their graph and metric interpretations. Chen, Davis and Korchevskaia (arXiv:2107.12315), and Mori, Mori and Ohsugi (arXiv:2312.11287), give facet and join-graph results. Those inspected results concern different invariants and do not themselves evaluate the book graph's Euclidean Löwner ellipsoid.

Crucially, Suliman and Weinstein (arXiv:2302.05966, §§1, 3.4 and Appendix A.3) already establish the **general** link between weighted-graph effective resistance, \(D\)-optimal design, and minimum enclosing ellipsoids. The covariance certificate above is an explicit application of that established principle, **not** a newly claimed general ellipsoid–resistance equivalence. The present claim is solely the evaluated book-graph weights, exact Euclidean eigenvalues and volume, and the sharp contact/invisible-edge transition. Published general D-optimal optimality conditions imply a solvable convex optimization problem, but without book-graph evaluation do not state the threshold or equality of the two distinct polytopes' optimal ellipsoids.

## Limitations
The theorem concerns Euclidean **outer** Löwner ellipsoids, not maximum inscribed John ellipsoids, facet counts, or other graph families. No assertion is made that the same ellipsoid survives adding different edges. Exact source noncoverage is limited to the inspected materials, and an equivalent previously recorded book-graph computation under effective-resistance or infinite Lewis-weight terminology remains a literature risk. A finite rational check, however broad, is not an infinite proof or independent audit.

## References
1. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (first posted 2019-10-11), https://arxiv.org/abs/1910.05193.
2. T. Chen, R. Davis and A. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (2021), https://arxiv.org/abs/2107.12315.
3. A. Mori, K. Mori and H. Ohsugi, *Number of facets of symmetric edge polytopes arising from join graphs*, arXiv:2312.11287 (2023), https://arxiv.org/abs/2312.11287.
4. M. Suliman and O. Weinstein, *Infinite Lewis Weights in Spectral Graph Theory*, arXiv:2302.05966 (2023), https://arxiv.org/abs/2302.05966.

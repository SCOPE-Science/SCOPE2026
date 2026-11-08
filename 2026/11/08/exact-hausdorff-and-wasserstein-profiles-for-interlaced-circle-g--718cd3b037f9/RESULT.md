# Exact Hausdorff and Wasserstein profiles for interlaced circle grids

## Finding

For each integer \(m\ge3\), each \(-1\le\varepsilon\le1\), and \(N=2m\), put \(\Delta=2\pi/N\) and
\[
\nu_{m,\varepsilon}=\frac1N\sum_{j=0}^{N-1}(1+\varepsilon(-1)^j)\,\delta_{u_j},\qquad
u_{m,0}=\frac1N\sum_{j=0}^{N-1}\delta_{u_j},\qquad
u_{m,\varepsilon}(S^1)=1,\quad u_j=(\cos(j\Delta),\sin(j\Delta)).
\]
Let \(\sigma\) be uniform angular probability on the circle, and let \(K_{m,\varepsilon}\) be the unique **Steiner-centered** planar convex body with surface-area measure \(2\pi\nu_{m,\varepsilon}\). Write \(B\) for the unit disk. Then
\[
\boxed{d_H(K_{m,\varepsilon},B)
=1-\frac{\pi}{N}\cot\frac{\pi}{N}
+|\varepsilon|\frac{\pi}{N}\tan\frac{\pi}{N}.}\tag{1}
\]
For \(d_g\), the **geodesic** circle distance, the exact transport costs are
\[
\boxed{W_1(\nu_{m,\varepsilon},\sigma)=\frac{\pi}{2N}(1+\varepsilon^2),\qquad
W_1(\nu_{m,\varepsilon},\nu_{m,0})=\frac{\pi|\varepsilon|}{N}.}\tag{2}
\]
For fixed or varying \(\varepsilon_m\in[-1,1]\), uniformly in that interval,
\[
d_H(K_{m,\varepsilon_m},B)=\frac{\pi^2}{3N^2}(1+3|\varepsilon_m|)+O(N^{-4}).\tag{3}
\]
In particular, whenever \(|\varepsilon_m|\ge c>0\), the Wasserstein perturbation from the equal-weight \(N\)-grid is of order \(N^{-1}\), whereas the reconstructed body's Hausdorff error is of order \(N^{-2}\). Thus an \(O(N^{-2})\) Wasserstein perturbation assumption is sufficient but **not necessary** for preservation of quadratic Hausdorff convergence within this natural family. For \(\varepsilon\ne0\), the positive-weight quadrature rule integrates all trigonometric polynomials of degree at most \(m-1\) but not all of degree \(m\); at \(\varepsilon=0\) its exact degree is \(2m-1\).

## Assumptions and scope

The parameter \(m\) is an arbitrary integer at least three, \(\varepsilon\) is real in the closed interval, and all lengths are Euclidean. The measure is balanced because its two constituent \(m\)-grids are each balanced; it is never supported on only an antipodal pair. At the endpoints \(\varepsilon=\pm1\), half the displayed nodes have zero weight and the convex polygon has \(m\), not \(2m\), sides. The perimeter of every reconstructed body is \(2\pi\). Steiner centering fixes Minkowski's translation ambiguity; it agrees with the origin, the common center of all regular polygons used below. The geodesic circle distance takes values in \([0,\pi]\), and all Wasserstein distances are for probability measures.

For clarity define \(x=\pi/m=2\pi/N\) and the radius pair
\[
r_m=x\cot x,\qquad R_m=x\csc x.
\]
These are the inradius and circumradius of the centered regular \(m\)-gon of perimeter \(2\pi\). The exact origin-centered inradius and circumradius of \(K_{m,\varepsilon}\) are
\[
\boxed{r_{m,\varepsilon}=\frac{r_m+R_m-|\varepsilon|(R_m-r_m)}2,\quad
R_{m,\varepsilon}=R_m\sqrt{\cos^2(x/2)+\varepsilon^2\sin^2(x/2)}.}\tag{4}
\]

## Proof

**1. Two interlaced polygons.** Let \(P_m\) be the centered regular \(m\)-gon of perimeter \(2\pi\) with outward facet normals at \(0,2x,4x,\ldots\), and let \(R_xP_m\) be its rotation through \(x\). Their surface-area measures respectively place mass \(2x\) on every even and odd grid normal. In the plane, perimeter measures are additive under Minkowski addition: \(S_{aC+bD}=aS_C+bS_D\) for \(a,b\ge0\), as follows from additivity of support functions and \(S_C=h_C+h_C''\) in distributions. Consequently, uniqueness in the planar Minkowski existence theorem and invariance of the Steiner point under Minkowski addition give
\[
K_{m,\varepsilon}=\frac{1+\varepsilon}{2}P_m+rac{1-\varepsilon}{2}R_xP_m.\tag{5}
\]
For \(|\varepsilon|<1\) the normal fan is the common refinement of two regular fans; each of the \(2m\) facets has outward normal \(u_j\) and length \(x(1+\varepsilon(-1)^j)\). At endpoints one summand collapses to the origin and the other is a regular \(m\)-gon.

**2. Exact inner and outer radii.** The vertices of \(P_m\) lie on the radius-\(R_m\) circle at arguments \((2j+1)x\). For \(a=(1+\varepsilon)/2\) and \(b=(1-\varepsilon)/2\), consecutive vertices of the Minkowski sum arise as weighted sums of adjacent vertices of the two rotated regular polygons, with angular separation \(x\). Hence all vertices of the sum have equal Euclidean norm
\[
R_m|a+b e^{ix}|=R_m\sqrt{\cos^2(x/2)+\varepsilon^2\sin^2(x/2)}.
\]
This is the outer radius. At even facet normals, the supporting value is \(a r_m+bR_m\); at odd facet normals it is \(aR_m+b r_m\). Since the support function is the linear form of a fixed vertex on each cone between consecutive facet normals, and is positive there, it attains its minimum on that cone at one of its endpoints: \(\cos\) is concave on the angular range of positive support. The smaller of those two displayed values is the inner radius in (4). These statements remain true at \(\varepsilon=\pm1\) by continuity or direct inspection of the regular \(m\)-gon.

**3. Inward discrepancy is the larger one.** For any origin-containing convex body with minimum and maximum support values \(r\) and \(R\), one has \(d_H(K,B)=\max\{1-r,R-1\}\). Let \(s=|\varepsilon|\in[0,1]\). The function
\[
F(s)=R_m\sqrt{\cos^2(x/2)+s^2\sin^2(x/2)}
+\frac{r_m+R_m-s(R_m-r_m)}2
\]
is convex in \(s\). The two endpoint sums are \(F(0)=r_{2m}+R_{2m}\) and \(F(1)=r_m+R_m\). For every integer \(k\ge3\),
\[
r_k+R_k=\frac\pi k\cot\frac{\pi}{2k}<2,
\]
because \(t\cot t<1\) for \(0<t<\pi/2\). A convex function on a closed interval does not exceed the larger endpoint value, so \(F(s)<2\) for all \(s\). Thus \(1-r_{m,\varepsilon}>R_{m,\varepsilon}-1\). Since \(\cot x+\csc x=\cot(x/2)\) and \(\csc x-\cot x=\tan(x/2)\), substituting (4) gives
\[
d_H(K_{m,\varepsilon},B)=1-\frac x2\cot\frac x2
+s\frac x2\tan\frac x2.
\]
Putting \(x=2\pi/N\) proves (1). In particular the Hausdorff error is strictly affine in \(s\), with unique minimizer \(s=0\).

**4. Exact geodesic transport to the circle.** Write \(\Delta=2\pi/N\) and \(s_j=(-1)^j\). Form the consecutive arcs \(C_j\), centered on \(u_j\), with lengths
\[
L_j=\Delta(1+\varepsilon s_j).
\]
They partition the circle without gaps because \((L_j+L_{j+1})/2=\Delta\). Their uniform masses are \(L_j/(2\pi)=(1+\varepsilon s_j)/N\), so sending each \(C_j\) to \(u_j\) is a feasible coupling with cost
\[
\sum_{j=0}^{N-1}\frac1{2\pi}\int_{-L_j/2}^{L_j/2}|t|\,dt
=\frac1{8\pi}\sum_jL_j^2
=\frac{\pi}{2N}(1+\varepsilon^2).\tag{6}
\]
For optimality, set \(\lambda_j=0\) for even \(j\) and \(\lambda_j=\Delta\varepsilon\) for odd \(j\), and define
\[
f(\theta)=\min_j\bigl[d_g(e^{i\theta},u_j)+\lambda_j\bigr].
\]
This is a geodesic \(1\)-Lipschitz function. The offsets obey \(|\lambda_j-\lambda_k|\le d_g(u_j,u_k)\); thus \(f(u_j)=\lambda_j\). Along the circle, its weighted Voronoi cells are exactly \(C_j\): equality of the costs from consecutive nodes is located a distance \(L_j/2\) after the \(j\)-th node, and any other node costs at least as much by the triangle inequality and alternating offsets. On \(C_j\), therefore, \(f(\theta)-f(u_j)=d_g(e^{i\theta},u_j)\). The Kantorovich–Rubinstein dual lower bound for this \(f\) equals the cost of the coupling (6); optimality and the first formula in (2) follow. At \(|\varepsilon|=1\), zero-length cells and ties are harmless by continuity.

**5. Distance to the equal grid.** The signed difference \(\nu_{m,\varepsilon}-\nu_{m,0}\) has extra mass \(|\varepsilon|/N\) at each node of one parity and missing mass of that size at each node of the other parity. Moving every excess to an adjacent node costs \((N/2)(|\varepsilon|/N)\Delta=|\varepsilon|\Delta/2\). For the reverse bound, use the geodesic \(1\)-Lipschitz function \(g(u)=d_g(u,H)\), where \(H\) is the set of excess-mass nodes. It takes value \(0\) on excess nodes and \(\Delta\) on deficit nodes, so its dual gap has absolute value \(|\varepsilon|\Delta/2\). This proves the second formula in (2).

**6. Uniform asymptotics and design strength.** Uniform Taylor expansions \(1-y\cot y=y^2/3+O(y^4)\) and \(y\tan y=y^2+O(y^4)\), with \(y=\pi/N\), give (3). The Fourier coefficient of \(\nu_{m,\varepsilon}\) vanishes at every nonzero frequency below \(m\), while at frequency \(m\) it equals \(\varepsilon\). For \(\varepsilon\ne0\), that obstructs exactness at degree \(m\) and establishes precise strength \(m-1\). At \(\varepsilon=0\) the rule is the uniform \(2m\)-grid, of strength \(2m-1\).

## Verification

The analytic steps prove (1)–(4) simultaneously for every integer \(m\ge3\) and every real \(\varepsilon\in[-1,1]\); no finite test is used as an infinite proof. The accompanying `verify.py` independently constructs the Minkowski sum by taking convex hulls of vertex sums, calculates minima of sampled facet supports and maxima of Euclidean vertex radii, and compares them against (4) for \(m=3,\ldots,40\) and nine sample weights including the endpoints. It also checks all transport-cell second moments for \(m=3,\ldots,29\). Run `python3 verify.py` after installing NumPy and SciPy; expected output is `INTERLACED_GRID_OK 1215`. A separate discretized linear-programming transport check for \(m=3\), \(\varepsilon=0.6\), and 480 equal source intervals gave transport cost \(0.3560471674068442\) against the exact value \(0.35604716740684317\). The minimax and transport optimality statements are established by the dual constructions, not by numerical outputs.

## Relationship to prior work

An (2026), Sections 2, 4, 5 and 6, proves the equal-weight regular-grid identity \(d_H(P_N,B)=1-(\pi/N)\cot(\pi/N)\), the exact equal-grid cost \(W_1(\nu_{N},\sigma)=\pi/(2N)\), and a general planar Steiner-centered Minkowski inverse Lipschitz bound. Corollary 6.4 gives \(W_1(\rho_N,\nu_N)=O(N^{-2})\) as a sufficient condition for quadratic convergence. Those baseline facts and the general inversion equation are used here; they are **not** new. The additional explicit statements are the full two-interlaced alternating-weight parameter profile (1)–(2), its exact transport dual witnesses, and the demonstration that the sufficient Wasserstein-perturbation order cannot be made a necessary condition. Böröczky–Machado–Ramos (2026) develop general Minkowski stability bounds in other discrepancy metrics; their scope does not give this special family's sharp values. Published work on finite Cauchy **perimeter quadrature** concerns a different quantity and does not identify the stated Hausdorff and Wasserstein formulas.

## Limitations

This is a deliberately structured two-interlaced, alternating-weight family. It does not determine the Hausdorff error of arbitrary weighted grids or optimize over all positive weights or arbitrary planar bodies. Explicit formulas are a special-case refinement of known planar Minkowski inversion rather than a new general inversion theorem; the formulas and implication gap are the mathematical contribution. The transport distance uses geodesic distance, not chordal distance. A failed search is not proof of first publication: an older, unindexed calculation for alternating equiangular polygons could overlap. No independent mathematical audit is claimed.

## References

1. C. An, *Gauss–Chebyshev Quadrature, S¹-Designs, and the Planar Minkowski Inverse Problem: A One-Dimensional Model for Design-Induced Convex Geometry*, arXiv:2610.11814v1, first posted 2026-10-08, https://arxiv.org/abs/2610.11814, especially Sections 4–6.
2. K. Böröczky, J. M. Machado and J. P. G. Ramos, *Quantitative Stability for Minkowski's Problem*, arXiv:2603.17726, first posted 2026-03-18, https://arxiv.org/abs/2603.17726.
3. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, second expanded edition, Cambridge University Press, 2014, for the planar Minkowski reconstruction theorem.
4. *Sharp positive N-direction Cauchy quadrature and angular rigidity*, published-finding corpus 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-positive-n-direction-cauchy-quadrature-and-angular-rigidit--33b1062b46ae.

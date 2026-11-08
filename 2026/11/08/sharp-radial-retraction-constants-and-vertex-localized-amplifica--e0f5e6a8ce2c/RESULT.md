# Sharp radial-retraction constants and vertex-localized amplification for regular even polygons

## Finding
Let \(N\ge4\) be an even integer. Let \(B_N\subset\mathbb R^2\) be the regular Euclidean \(N\)-gon of circumradius one, centered at the origin, and let \(\|\cdot\|_N\) be its Minkowski functional. The canonical radial retraction
\[
R_N(x)=\frac{x}{\max\{1,\|x\|_N\}}
\]
onto \(B_N\) has **exact global Lipschitz constant**
\[
\operatorname{Lip}_{\|\cdot\|_N}(R_N)=
\begin{cases}
\sec^2(\pi/N),&N\equiv0\pmod4,\\
1,&N\equiv2\pmod4.
\end{cases}
\tag{1}
\]
Here the second branch is the classical Radon-plane nonexpansivity phenomenon; the quantitative first branch and its sharp localization are the focus of the result. The value is unchanged for any invertible affine-linear image of the centered regular polygon, interpreted with its induced norm.

When \(4\mid N\), amplification strictly greater than one is approached only through exterior derivatives tending to **vertices** of the unit polygon. At a chosen vertex, the sharp input directions are precisely the two unit vertices obtained by quarter turns. No pair of distinct points attains the global Lipschitz ratio: the sharp factor is a local boundary limit. On the other hand, for \(N\equiv2\pmod4\) the constant one is attained by any two distinct points inside \(B_N\).

In the expansive congruence class, \(\operatorname{Lip}(R_4)=2\), \(\operatorname{Lip}(R_8)=4-2\sqrt2\), \(\operatorname{Lip}(R_{12})=8-4\sqrt3\), and the values strictly decrease as \(N\) increases through multiples of four. Along this subsequence,
\[
\operatorname{Lip}(R_N)=1+\frac{\pi^2}{N^2}+\frac{2\pi^4}{3N^4}+O(N^{-6}).
\tag{2}
\]

## Assumptions and scope
Everything is real and two-dimensional. The side count \(N\) is even and at least four. The vertices of \(B_N\) are
\[
v_j=(\cos(2\pi j/N),\sin(2\pi j/N)),\quad j=0,\ldots,N-1.
\]
Set \(\delta=\pi/N\). For the side \([v_j,v_{j+1}]\), the unique norm-one supporting functional is
\[
\varphi_j(h)=\frac{\langle h,(\cos((2j+1)\delta),\sin((2j+1)\delta))\rangle}{\cos\delta}.
\]
The polygon norm is \(\|h\|_N=\max_j\varphi_j(h)\) (the collection includes opposite facets, since \(N\) is even). All Lipschitz constants and operator norms are measured using this same polygon norm in both domain and range.

## Proof
**1. Sharp reduction from the nonlinear map to incident facet operators.** On the open exterior cone where one facet functional \(\varphi\) is uniquely norming, write \(r=\|x\|_N=\varphi(x)>1\) and \(u=x/r\) on the relative interior of the corresponding boundary facet. Differentiation gives
\[
D R_N(x)h=\frac1r\bigl(h-u\varphi(h)\bigr).
\tag{3}
\]
Inside the ball the derivative is the identity. Along a fixed side, \(u\mapsto\|I-u\otimes\varphi\|\) is convex, as it is the norm of an operator depending affinely on \(u\). Its maximum on that side is therefore attained at one of its vertices. By dihedral symmetry, all such endpoint operator norms have the same value \(L_N\).

The radial map is piecewise smooth on the finitely many cones of the polygonal norm. Integrating the derivative on generic line segments, and then passing to arbitrary segments by continuity, yields
\[
\operatorname{Lip}(R_N)\le\max\{1,L_N\}.
\tag{4}
\]
Conversely, for either incident facet at a vertex, first take a boundary point in the relative interior of that facet and approach it from the exterior. Formula (3) then has a derivative norm arbitrarily close to the corresponding boundary operator norm. Finally let the boundary point approach the vertex. This proves the reverse bound, so the global constant in (4) is exact.

**2. An exact two-dimensional rank-one calculation.** Use the side \([v_0,v_1]\), write
\[
v_0=(1,0),\quad v_1=(\cos2\delta,\sin2\delta),\quad e=v_1-v_0,
\quad\varphi=\varphi_0.
\]
For \(u_t=(1-t)v_0+t v_1\) and \(0\le t\le1\), set \(P_t=I-u_t\otimes\varphi\). Since \(\varphi(e)=0\), the range of \(P_t\) is the line spanned by \(e\); since \(P_t(u_t)=0\), taking determinants gives the exact formula
\[
P_t h=\frac{\det(u_t,h)}{\det(u_t,e)}e
=\frac{\det(u_t,h)}{\sin(2\delta)}e.
\tag{5}
\]
(The first equality follows because \(\det(u_t,P_th)=\det(u_t,h)\); the displayed denominator is positive.) Consequently
\[
\|P_t\|_{N\to N}=\frac{\|e\|_N}{\sin(2\delta)}
\max_{0\le j<N}|\det(u_t,v_j)|.
\tag{6}
\]
The last maximum occurs at a vertex because the determinant is a linear functional, whose absolute maximum on a convex polygon is attained at a vertex. For fixed \(v_j\), its absolute determinant is convex in \(t\); therefore the right-hand maximum in (6) is a convex function of \(t\). Its endpoints have equal value by facet reflection.

**3. Modulo-four geometry.** The chord \(e\) has Euclidean length \(2\sin\delta\) and angle \(\pi/2+\delta\). If \(4\mid N\), this direction is a facet-normal ray, so
\[
\|e\|_N=2\tan\delta,
\quad\max_j|\det(v_0,v_j)|=1,
\]
the latter maximum being attained only at the two quarter-turn vertices. Inserting into (6) at \(t=0\) gives
\[
L_N=\frac{2\tan\delta}{2\sin\delta\cos\delta}=\sec^2\delta>1.
\]
If \(N\equiv2\pmod4\), the direction of \(e\) is instead a vertex ray. Hence
\[
\|e\|_N=2\sin\delta,
\quad\max_j|\det(v_0,v_j)|=\cos\delta,
\]
and (6) gives \(L_N=1\). Combining this calculation with (4) proves (1). The second case also agrees with the previously known Radon-plane characterization.

**4. Rigidity and nonattainment on the expansive branch.** Suppose \(4\mid N\) and \(0<t<1\). For every unit-polygon vertex \(h\), the triangle inequality yields
\[
|\det(u_t,h)|\le(1-t)|\det(v_0,h)|+t|\det(v_1,h)|\le1.
\]
Equality would require the same vertex \(h\) to be Euclidean perpendicular to both distinct unit vectors \(v_0\) and \(v_1\), which is impossible. There are only finitely many such \(h\), so (6) is strictly below \(L_N\) in every relative facet interior. At an endpoint, equality in (6) requires \(h=\pm Jv_0\), where \(J\) is the Euclidean quarter turn. Rotating the argument classifies every local maximizing endpoint and tangent input direction.

At each differentiability point in the open exterior region, the extra factor \(1/r\) in (3) is strictly below one, while the interior region has local Lipschitz factor one. Thus the metric speed along any nonconstant line segment is strictly less than \(L_N\) almost everywhere (on special segments confined to facet boundaries or vertex rays, the one-dimensional radial derivative also has norm at most one). Integrating along the segment gives a **strict** Lipschitz inequality for each distinct input pair. Formula (3), with exterior points approaching a facet endpoint and the perpendicular unit input direction, supplies a sequence of difference quotients tending to \(L_N\). This proves the claimed nonattainment and limiting localization.

Finally, monotonicity follows from the strict decrease of \(\sec^2 x\) as \(x\downarrow0\) for positive \(x<\pi/2\). Formula (2) is the Taylor expansion of \(\sec^2 x\) at zero.

## Verification
The standalone `verify_regular_polygon_radial.py` independently reconstructs polygon vertices and facet-normal support functionals, evaluates the induced rank-one norms via determinant extrema, and verifies 413 sampled facet-operator identities for all even side counts between four and 120. It checks strict interior deficit for multiples of four and 15 explicit exterior finite-difference quotients approaching the asserted constant. Its final diagnostic is `ALL_REGULAR_POLYGON_RADIAL_DIAGNOSTICS_PASSED`. The script uses standard Python without external dependencies; run `python verify_regular_polygon_radial.py` in this package directory. The all-side-count and nonattainment claims are proved above, not inferred from sampling.

## Relationship to prior work
De Figueiredo and Karlovitz (1967) and Thele (1974) established basic radial-projection geometry and general quantitative characterizations. Martini and Swanepoel, *Antinorms and Radon curves* (arXiv:math/0409200v1, 2004), Section 12, Theorem 16 and Corollary 17, explicitly credit the classical statement that the radial projection is nonexpansive exactly for a Radon norm. In particular, this **already implies** the constant-one half of (1) for regular polygons with \(N\equiv2\pmod4\). That half is given here for a unified statement, **not** presented as a novel theorem.

The publicly available *Sharp radial-retraction Lipschitz profile of the real Lorentz-predual octagonal planes* gives the more general weighted octagon profile and its regular octagon value \(4-2\sqrt2\). It also uses a related facet-derivative reduction. The regular octagon case and that reduction are therefore not original here. The extension assessed here is the all-even-side-count exact quantitative formula, the complete congruence-class contrast and the strict vertex-localization/nonattainment on the expansive branch.

Other published results on the *Zbăganu* and *Liu--Li Euler--Lagrange* constants of regular fourfold polygons feature the same numerical expression \(\sec^2(\pi/N)\), but concern different bilinear/product or two-parameter invariants rather than the Lipschitz modulus of this particular nonlinear radial mapping. The numerical coincidence is disclosed, and no unproved identity between the invariants is assumed.

## Limitations
The calculation concerns the **canonical radial retraction**, not the infimum of Lipschitz constants among *all* retractions onto a polygonal ball. It applies only to real two-dimensional norms with even regular polygonal balls (or invertible linear images); it does not assert a formula for arbitrary centrally symmetric polygons, arbitrary Banach spaces, or nearest-point projections. The rigidity statement describes limiting exterior derivatives and strict nonattainment, not every possible rate of approach of a maximizing sequence.

Historical original full texts by De Figueiredo--Karlovitz (1967) and Thele (1974) were not accessible in the checked public routes. Their established general conclusions were compared through original bibliographic records and the inspected detailed exposition by Martini--Swanepoel. An equivalent old quantitative evaluation for all regular polygons under another formulation cannot be excluded solely by electronic literature searches.

## References
1. H. Martini and K. J. Swanepoel, *Antinorms and Radon curves*, arXiv:math/0409200v1, first submitted 13 September 2004, Section 12, especially Corollary 17 (full original inspected).
2. D. G. de Figueiredo and L. A. Karlovitz, *On the radial projection in normed spaces*, Bulletin of the American Mathematical Society 73 (1967), 364--368, DOI:10.1090/S0002-9904-1967-11753-1 (full original inaccessible in checked routes).
3. R. L. Thele, *Some results on the radial projection in Banach spaces*, Proceedings of the American Mathematical Society 42 (1974), 483--486, DOI:10.1090/S0002-9939-1974-0328550-1 (full original inaccessible in checked routes).
4. *Sharp radial-retraction Lipschitz profile of the real Lorentz-predual octagonal planes*, published complete result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-radial-retraction-lipschitz-profile-of-the-real-lorentz-pr--09dd18ddb4e6 (RESULT.md inspected).
5. *Facet-resonant Euler--Lagrange constants on regular fourfold polygonal Banach planes*, published complete result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-facet-resonant-euler-lagrange-constants-on-regular-4n-gonal-bana--8e11112b0d76 (RESULT.md inspected).
6. *Complete Zbăganu extremizers of regular fourfold polygonal Banach planes*, published complete result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-zb-ganu-extremizers-of-regular-4m-gonal-banach-planes--8181a908ccaa (RESULT.md inspected).

# The closest-generator distance law of a Reuleaux triangle

## Finding
Let \(v_0,v_1,v_2\) be the vertices of a Euclidean equilateral triangle of side one. Put
\[
K=\bigcap_{j=0}^{2}\overline B(v_j,1),\qquad
A=\operatorname{area}(K)=\frac{\pi-\sqrt3}{2}.
\]
Let \(X\) have normalized planar area measure on the width-one Reuleaux triangle \(K\), and set
\[
D=\min_{0\le j\le2}\|X-v_j\|,\quad
r_0=\sqrt{2-\sqrt3},\quad R=\frac1{\sqrt3}.
\]
Define, on their indicated domains,
\[
\Phi(r)=\arccos\frac r2-\frac\pi6\quad (0\le r\le R),
\qquad
\alpha(r)=\arccos\frac1{2r}\quad (1/2\le r\le R).
\]
Then \(D\) is supported on \([0,R]\), has no atoms, and its density is \(f_D(r)=3rL(r)/A\), with the **complete three-branch angular law**
\[
L(r)=\begin{cases}
2\Phi(r), &0<r\le\frac12,\\
2\bigl(\Phi(r)-2\alpha(r)\bigr),&\frac12<r\le r_0,\\
\frac\pi3-2\alpha(r),&r_0<r<R.
\end{cases}
\]
The cumulative distribution is elementary. For \(0\le r\le R\), put
\[
H(r)=\frac{r^2}{2}\Phi(r)+\arcsin\frac r2-\frac{r\sqrt{4-r^2}}4,
\qquad
Q(r)=\frac{r^2}{2}\alpha(r)-\frac{\sqrt{4r^2-1}}8\quad(r\ge\tfrac12).
\]
Then \(F_D(r)=\frac3A J(r)\), where
\[
J(r)=\begin{cases}
2H(r),&0\le r\le\frac12,\\
2H(r)-4Q(r),&\frac12<r\le r_0,\\
2H(r_0)-2Q(r_0)+\frac\pi6(r^2-r_0^2)-2Q(r),&r_0<r\le R.
\end{cases}
\]
Set \(F_D(r)=0\) for \(r<0\) and \(F_D(r)=1\) for \(r\ge R\). In particular, \(F_D(1/2)=0.935908004331490\ldots\) and \(F_D(r_0)=0.969346062324249\ldots\).

These are three distinct geometric regimes, with two nonanalytic transition radii. Writing \(F_{\mathrm{an}}(r)=6H(r)/A\) for the analytic continuation of the first branch, as \(\varepsilon\downarrow0\),
\[
F_D(\tfrac12+\varepsilon)=F_{\mathrm{an}}(\tfrac12+\varepsilon)-\frac8A\varepsilon^{3/2}+O(\varepsilon^{5/2}),
\]
and the finite second-derivative jump at \(r_0\) is
\[
F_D''(r_0+)-F_D''(r_0-)=\frac{24}{A}.
\]
At the two support endpoints,
\[
F_D(r)=\frac\pi A r^2+O(r^3)\quad(r\downarrow0),\qquad
\Pr\{D>R-\varepsilon\}=\frac{3\sqrt3}{A}\varepsilon^2+O(\varepsilon^3).
\]

## Assumptions and scope
The Euclidean width of \(K\) is one. Uniformity means normalized two-dimensional Lebesgue measure on its interior, not arclength sampling on its boundary. The three comparison sites are the vertices **generating** the Reuleaux triangle; they are not independently sampled sites. Distances are ordinary Euclidean distances. Scaling the shape by \(w>0\) scales \(D\), \(r_0\), and \(R\) by \(w\), leaving the normalized distribution unchanged. Ties among nearest sites lie on bisectors and have area zero.

## Proof
**1. Polar geometry and Voronoi reduction.** By threefold rotational symmetry, it suffices to examine the Voronoi cell of one generating vertex \(v_0\). Choose orthonormal coordinates based at \(v_0\), with the positive second axis pointing towards the centroid, so the other generating vertices have coordinates \((\pm\tfrac12,\tfrac{\sqrt3}2)\). A radius-\(r\) point in these coordinates has the form
\[
Z=r(\sin\varphi,\cos\varphi).
\]
Because \(r\le R<1\), its membership in the generating disk centered at \(v_0\) is automatic. Membership in both other generating disks is equivalent to
\[
r\le2\cos(\tfrac\pi6+|\varphi|),\quad |\varphi|\le\tfrac\pi3,
\]
so the admitted angular interval before nearest-site constraints is \(|\varphi|\le\Phi(r)\). The condition that \(v_0\) be at least as close to \(Z\) as either other vertex is exactly
\[
r\cos(\tfrac\pi6-|\varphi|)\le\frac12.
\]
For \(r\le1/2\), this is automatic. For \(r>1/2\), with \(\alpha(r)=\arccos(1/(2r))\), the allowed angles are the intersection of \(|\varphi|\le\Phi(r)\) with
\[
|\varphi|\le\frac\pi6-\alpha(r)
\quad\text{or}\quad
|\varphi|\ge\frac\pi6+\alpha(r).
\]
The outer angular band is nonempty precisely if \(\Phi(r)>\pi/6+\alpha(r)\). Its left-minus-right endpoint gap is strictly decreasing, since \(\Phi'(r)<0\) and \(\alpha'(r)>0\). Equality occurs at the exact radius
\[
r_0=\sqrt{2-\sqrt3},\quad
\alpha(r_0)=\frac\pi{12},\quad \Phi(r_0)=\frac\pi4.
\]
Indeed, \(r_0/2=\sin(\pi/12)\), and \(1/(2r_0)=\cos(\pi/12)\). Thus before \(1/2\) there is one angular interval; until \(r_0\) the central interval and two outer intervals coexist; above \(r_0\) only the central interval remains. Their combined angular lengths are exactly the three displayed formulas for \(L(r)\). At \(R=1/\sqrt3\), \(\alpha(R)=\pi/6\), so no positive angular length remains, establishing the maximal nearest distance.

**2. Density and cumulative law.** The nearest-site cells partition \(K\) up to area-zero bisectors. The area in a polar radius shell \([r,r+dr]\) of one cell is \(rL(r)dr\). Therefore the normalized threefold sum gives
\[
f_D(r)=\frac{3rL(r)}{A},\qquad F_D(r)=\frac3A\int_0^r tL(t)\,dt.
\]
Direct differentiation verifies \(H'(r)=r\Phi(r)\), \(Q'(r)=r\alpha(r)\), \(H(0)=0\), and \(Q(1/2)=0\). Integrating across the two angular transitions with continuity yields the stated elementary formulas for \(J\). Their integral at \(R\) equals \(A/3\), because the three nearest-site cells partition the Reuleaux triangle. This is also independently checked by substituting the endpoint trigonometric values into the primitives. There are no atoms because planar area gives zero measure to each level circle around the finitely many sites.

**3. Sharp transitions.** Set \(r=\frac12+\varepsilon\). The expansion \(\alpha(r)=2\sqrt\varepsilon+O(\varepsilon^{3/2})\), together with \(Q'(r)=r\alpha(r)\), gives \(Q(r)=\frac23\varepsilon^{3/2}+O(\varepsilon^{5/2})\). The middle CDF formula now yields the displayed \(-8\varepsilon^{3/2}/A\) correction. At \(r_0\), the only disappearing term is twice the outer-band angular length \(2(\Phi-\pi/6-\alpha)\). Its first derivative has a jump, giving
\[
F_D''(r_0+)-F_D''(r_0-)
=\frac{6r_0}{A}\bigl(\alpha'(r_0)-\Phi'(r_0)\bigr)
=\frac6A\left(\frac1{r_0^2}+r_0^2\right)=\frac{24}{A},
\]
where \(\Phi'(r_0)=-r_0\) and \(\alpha'(r_0)=r_0^{-3}\). As \(r\downarrow0\), \(L(r)=2\pi/3+O(r)\), yielding \(F_D(r)=\pi r^2/A+O(r^3)\). As \(r\uparrow R\), \(\alpha'(R)=3\), so \(L(r)=6(R-r)+O((R-r)^2)\). Integrating the density from \(R-\varepsilon\) to \(R\) gives the terminal coefficient \(3\sqrt3/A\).

## Verification
The attached `verify.py` independently evaluates the three angular bands from the original disk and Voronoi inequalities, checks the closed-form density and CDF against numerical radial quadrature, verifies the endpoint and transition constants, and samples points uniformly in a bounding rectangle conditioned on inclusion in the three generating disks. Run `python verify.py` with Python 3 and its standard library. All computations are finite corroboration; the continuous-domain proof is the polar-inequality analysis and exact integration above.

## Relationship to prior work
Harrell's 2000 analysis proves the Reuleaux triangle's extremality among planar constant-width bodies using support functions and curvature; it does not give a nearest-generating-vertex distance distribution. Bezdek's 2009 disk-polygon study establishes geometric area, width, and inradius comparisons and describes the regular disk triangle; its statements do not imply the stated Voronoi radial measure without new integration. The published *Exact centered-disk area profile of the Reuleaux triangle* treats distance from the **centroid** to a random interior point and concentric disks, rather than distance to the nearest of the three corners; its radial density and phase radii are different. Published regular-polytope nearest-vertex gap results assume a **polytope**, whereas \(K\) has three circular arcs, and concern the gap between the two smallest squared distances, not this minimum. Triangle-specific point-picking formulas concern polygonal triangle interiors and fixed reference vertices, not the curved three-disk intersection. An indexed-search failure is not proof of historical novelty; a wider classical or unindexed computational-geometry treatment might contain the same law.

## Limitations
This is an exact calculation for one fixed Reuleaux geometry and three fixed generating sites, not a characterization of all constant-width curves or a universal point-process theorem. The density is continuous, but the CDF is not twice continuously differentiable at either interior transition. No distribution for random sites or for geodesic distances is asserted. Historical priority is provisional; no independent mathematical audit is asserted.

## References
1. E. M. Harrell II, *A direct proof of a theorem of Blaschke and Lebesgue*, first public version 2000-09-14, arXiv:math/0009137v1, https://arxiv.org/abs/math/0009137.
2. M. Bezdek, *On a generalization of the Blaschke-Lebesgue theorem for disk-polygons*, first public version 2009-03-31, arXiv:0903.5361v1, https://arxiv.org/abs/0903.5361.
3. *Exact centered-disk area profile of the Reuleaux triangle*, published geometric result, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-centered-disk-area-profile-of-the-reuleaux-triangle--9c2a3f200b56.
4. *Universal nearest-vertex squared-distance margin in regular polytopes*, published result, 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-universal-nearest-vertex-squared-distance-margin-in-regular-poly--a6d70db3bcca.
5. *Moments of Distance from a Vertex to a Uniformly Distributed Random Point within Arbitrary Triangles*, open-access article first published 2016-12-08, DOI:10.1155/2016/8371750, https://doi.org/10.1155/2016/8371750.

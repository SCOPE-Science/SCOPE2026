# Strict Santaló-volume growth through the icosahedral rhombic transition

## Finding

Let \(I\subset\mathbb R^3\) be the regular icosahedron with all twelve vertices on the unit sphere, and let \(U\) be its set of twenty outward *unit* face normals. Define \(K_t=\operatorname{conv}(I\cup tU)\). The polytope is centrally symmetric, so its Santaló point is the origin and its affine-invariant volume product is \(\mathcal P(t)=\operatorname{vol}(K_t)\operatorname{vol}(K_t^\circ)\), where \(K_t^\circ=\{x:\langle x,y\rangle\le1\text{ for every }y\in K_t\}\).

**Theorem.** The volume product is strictly increasing from the icosahedron at \(t=a\) to the golden rhombic triacontahedron at \(t=t_0\), with explicit pre-transition law \(\mathcal P(t)=V(t)W_-(t)\) below. This comparison extends across the transition all the way to \(t=1\); the post-transition law and its strict increase up to \(1\) are included for completeness and are not claimed as distinct from the post-rhombic result cited below. The unique combinatorial transition in \((a,1)\) is at \(t_0\). At \(t=1\), the hull is the thirty-two-vertex inscribed realization of the pentakis dodecahedron that maximizes ordinary volume in the cited sphere-inscription theorem. Numerically, \(\mathcal P(a)=14.0763745333445\ldots\), \(\mathcal P(t_0)=15.4205486916856\ldots\), and \(\mathcal P(1)=16.2080044346791\ldots\). These are evaluations of the exact expressions, not claims of rationality.

## Assumptions and scope

The face-normal set \(U\) is the regular unit-circumradius dodecahedron \(D=\operatorname{conv}(U)\). Write
\[
\begin{aligned}
 a&=\sqrt{\frac{5+2\sqrt5}{15}},& c&=\frac{\sqrt5}{3},& q&=1+c-2a^2=\frac{5+\sqrt5}{15},\\
 L&=\sqrt{2-\frac2{\sqrt5}},& s&=\sin\frac{2\pi}{5}=\frac{\sqrt{10+2\sqrt5}}4, & t_0&=\frac{2a}{1+c},\\
 V_D&=10a(1-a^2)s.&&&&
\end{aligned}
\]
Here \(L\) is the icosahedral edge length; \(a\) is the inradius of both unit-circumradius regular solids; \(c\) is the inner product of adjacent normals in \(U\); and \(V_D=\operatorname{vol}(D)\). Numerically \(a=0.79465447229\ldots\) and \(t_0=0.91059299731\ldots\).

The exact primal volume is
\[
V(t):=\operatorname{vol}(K_t)=
\begin{cases}
\dfrac{2V_Dt}{1+c},&a\le t\le t_0,\\[2mm]
\dfrac{V_Dt^2}{a},&t_0\le t\le1.
\end{cases}
\]
For \(a\le t\le t_0\), the exact polar volume is
\[
W_-(t)=\frac{V_D}{a^3}-\frac{5\sqrt3(1+c)}{a^3(1-c)}\left(1-\frac at\right)^3.
\]
For \(t_0\le t\le1\), put
\[
\mu=\frac{t^{-1}-a}{q},\quad\lambda=1-2a\mu,\quad
F_5=5q\mu^2s,\quad
F_6=\frac{\sqrt3}{4}\left[(L\lambda)^2+4(L\lambda)\frac{2\mu}{\sqrt3}+\left(\frac{2\mu}{\sqrt3}\right)^2\right]
\]
and
\[
W_+(t)=4F_5+\frac{20}{3t}F_6.
\]
The promised exact volume-product law is \(\mathcal P(t)=V(t)W_-(t)\) on the first interval and \(\mathcal P(t)=V(t)W_+(t)\) on the second. Both formulas agree at \(t=t_0\). In particular, \(\mathcal P(1)=(V_D/a)(4F_5(1)+20F_6(1)/3)\) is an explicit exact radical expression, using the definitions above.

## Proof

**1. Supporting-face transition.** Unit icosahedral vertices have adjacent inner product \(1/\sqrt5\). Three incident vertices have outward face normal equal to their sum divided by \(3a\). Adjacent face normals have inner product \(c=\sqrt5/3\). For an icosahedral edge with endpoints \(v,w\), let \(u_+,u_-\) be the normals of its two incident faces. The four points \(v,w,tu_+,tu_-\) are coplanar exactly when \(t=t_0=2a/(1+c)\). Their opposite diagonals then bisect each other at right angles and have ratio \((\|v-w\|)/(t_0\|u_+-u_-\|)=(1+\sqrt5)/2\). The resulting thirty quadrilaterals are golden rhombi.

For \(a<t<t_0\), the sixty supporting triangles are \(\operatorname{conv}(v,w,tu)\), where \(v,w\) is an edge of the face of \(I\) having outward normal \(u\). For \(t_0<t\le1\), they are \(\operatorname{conv}(v,tu,tu')\), where \(u,u'\) are normals of adjacent icosahedral faces meeting at the vertex \(v\). The following support-plane calculation proves both classifications.

Write \(g=(1+\sqrt5)/2\), \(R=\sqrt{g+2}\). The vertices of \(I\) are the cyclic permutations of \((0,\pm1,\pm g)/R\); those of \(D\) are the cyclic permutations of \((\pm g^{-1},0,\pm g)/\sqrt3\) together with \((\pm1,\pm1,\pm1)/\sqrt3\). Take \(v=(0,1,g)/R\), \(w=(0,-1,g)/R\) and \(u_\pm=(\pm g^{-1},0,g)/\sqrt3\). Here \(a=g^2/(\sqrt3 R)\) and \(t_0=\sqrt3/R\). At \(t_0\) the plane \(z=g/R\) supports exactly the four indicated points. The first-branch triangle with \(u_+\) has supporting inequality \(nx+z\le g/R\), where \(n=g^2(t_0/t-1)\) and \((x,y,z)\) are ambient coordinates. For the fixed icosahedral vertices the inequalities interpolate affinely in \(n\) between the original face plane at \(t=a\) and the common rhombus plane at \(t_0\). For the scaled normal vertices the left side is affine in \(t\), since both \(tn\) and \(t\) are affine. At \(a\), among normal vertices only \(au_+\) lies in the plane. At \(t_0\) only \(v,w\) among icosahedral vertices lie in the plane. Thus exactly the three desired points lie in the plane for \(a<t<t_0\).

On the second branch the inequality is \(my+z\le tg/\sqrt3\), with \(m=g(t/t_0-1)\). For \(t_0<t\le1\), \(0<mg<g-1\): indeed \(t_0>9/10\) and \(g^2/9<g-1\). Unnormalized coordinates other than the two highest points in each set have \(z\le1\), \(|y|\le g\), so none can reach the plane. The remaining fixed vertices \(v,w\) give \(v\) on the plane and \(w\) strictly below, while both \(tu_\pm\) lie on it. In each branch symmetry gives sixty triangular facets; at \(t_0\) it gives thirty quadrilateral facets with the diagonals in the previous paragraph. Completeness follows from Euler's formula: triangulating the quadrilateral faces if needed already gives sixty triangles on at most thirty-two vertices, which exhausts the bound \(2\#\mathrm{vertices}-4\). At \(a\) the hull is the original icosahedron.

**2. Primal volumes.** The first-branch volume is the volume of \(I\) plus the twenty outward pyramids over its triangular faces. In fact the pyramids from the origin to the classified supporting triangles partition \(K_t\); grouping them by the original face gives the pyramid from the origin to that face and the outward pyramid over it. The latter has height \(t-a\). Adding these yields \(V(t)=(t/a)\operatorname{vol}(I)\). On the second branch, grouping the origin pyramids by the corresponding face of \(tD\) gives \(tD\) plus twelve outward pentagonal pyramids. Each base plane is at radial distance \(ta\) and the pyramidal height is \(1-ta\). Since \(\operatorname{vol}(tD)=t^3V_D\), the sum is \(t^3V_D+(t^2V_D/a)(1-ta)=V_Dt^2/a\). Continuity at \(t_0\) then gives \(V(t)=V_Dt_0t/a=2V_Dt/(1+c)\) on the first branch.

**3. Polar volumes.** The polar is
\[
K_t^\circ=\{x:\langle x,v\rangle\le1\ (v\in I\text{ vertices}),\quad\langle x,u\rangle\le t^{-1}\ (u\in U)\}.
\]
At \(t=a\) it is the dodecahedron \(D/a\). In unit dodecahedral coordinates, the cutting plane at \(u\) has height \(a/t\) in direction \(u\). The coordinates above show that \(c\) is the largest inner product between any two distinct vertices of \(D\). Thus for \(a/t\ge(1+c)/2\) a cut separates just one original vertex and intersects its three incident edges at fraction \(\tau=(1-a/t)/(1-c)\le1/2\) of the edge length. Each resulting cap is inside the tetrahedron spanned by its vertex and the three incident edge midpoints. Every vertex and every edge midpoint in the midpoint tetrahedron of a *different* cap has inner product with \(u\) at most \((1+c)/2\), so the caps have disjoint interiors. A vertex and its three neighbors determine a tetrahedron of volume \(\sqrt3(1-c)(1-c^2)/4\), from the base equilateral triangle of circumradius \(\sqrt{1-c^2}\) and height \(1-c\). The scaling factor for one cap is \((\tau/a)^3\); subtracting twenty caps yields \(W_-(t)\).

For \(t>t_0\), duality with the sixty triangular primal facets gives twelve polar pentagonal facets with outward normal \(v\) at distance one and twenty polar equiangular hexagonal facets with outward normal \(u\) at distance \(t^{-1}\). At the triangle \(\operatorname{conv}(v,tu,tu')\), the corresponding polar vertex is
\[
x=\lambda v+\mu(u+u'),
\]
where solving \(\langle x,v\rangle=1\) and \(\langle x,u\rangle=\langle x,u'\rangle=t^{-1}\) gives the displayed \(\lambda,\mu\). The pentagonal facet has circumradius \(\mu\|u+u'-2av\|=\sqrt{2q}\,\mu\), hence area \(F_5\). On the plane of the hexagon, the uncut face of \((tD)^\circ\) is an equilateral triangle; the planes corresponding to the three vertices of the icosahedral face with normal \(u\) cut its corners parallel to the opposite edges. From the dual vertices above, edges keeping \(u,u'\) fixed have length \(A=L\lambda\); edges keeping \(u,v\) fixed have length \(B=\mu\|u'-u''\|=2\mu/\sqrt3\). In the representative coordinates, the latter pair across the two edges issuing from \(v\) of the face with normal \(u_+\) is \(u_-\) and \((1,1,1)/\sqrt3\). The area is that of the equilateral triangle of side \(A+2B\) minus three equilateral triangles of side \(B\), giving \(F_6\). Decomposing the polar volume into pyramids from the origin gives \(W_+(t)=12F_5/3+20F_6/(3t)\), as claimed. Continuity of the polars (all hulls contain the fixed inball of \(I\)) extends the formula to the switch, where \(\lambda(t_0)=0\) and the hexagons become triangles.

**4. Strict increase, with rational certificates.** On the first branch define \(h=1-a/t\in[0,(1-c)/2]\). Differentiating \(\mathcal P(t)=[2V_D/(1+c)]t[\,V_D/a^3-C h^3\,]\), where \(C=5\sqrt3(1+c)/(a^3(1-c))\), gives a positive multiple of
\[
 V_D-a^3 C h^2(3-2h).
\]
The subtracted expression is increasing in \(h\in[0,1]\). At the right endpoint the required strict inequality reduces to
\[
V_D>\frac{5\sqrt3(2+c)}9.
\]
This inequality holds by exact radical isolation (the two sides are approximately \(2.78516\) and \(2.64172\), with strictly separated rational enclosures).

For the second branch, \(\mathcal P(t)=(V_D/a)E(t)\), and expansion yields
\[
E(t)=p_2t^2+p_1t+p_0+\frac{p_{-1}}t,
\]
with
\[
\begin{aligned}
p_2&=\frac{20a^2s}{q},\\
p_1&=-\frac{40as}{q}+\frac{5\sqrt3}{3q^2}\left[L^2(1+c)^2-\frac{8La(1+c)}{\sqrt3}+\frac{4a^2}{3}\right],\\
p_{-1}&=\frac{5\sqrt3}{3q^2}\left[4a^2L^2-\frac{16aL}{\sqrt3}+\frac43\right].
\end{aligned}
\]
Exact rational interval arithmetic certifies \(24.898<p_2<24.900\), \(-94.001<p_1<-93.998\), \(-44.567<p_{-1}<-44.562\). Consequently \(E''(t)=2p_2+2p_{-1}/t^3<0\) for \(t_0\le t\le1\), while \(E'(1)=2p_2+p_1-p_{-1}>0.357\). Therefore \(E'(t)>0\) for all \(t\in[t_0,1]\). Both branches are continuous and increasing; so is the entire product.

## Verification

The supplied \(\texttt{check.py}\) uses only Python standard libraries for outward-rounded square-root enclosures based on \(\operatorname{isqrt}\) and exact rational endpoints for the two derivative inequalities. When NumPy and SciPy are available it also runs ten direct convex-hull / halfspace-intersection volume comparisons. These finite comparisons corroborate, but do not prove, the two formulas. The supporting-plane classifications and interval derivative proof are the grounds for the universally quantified theorem.

## Relationship to prior work

The maximum-volume thirty-two-vertex inscribed configuration is established by Hoehner (2026), building on Wimmer (1998). Barthe and Fradelizi's same-reflection-symmetry minimum theorem supplies a comparison with the icosahedral endpoint but not strict comparisons between arbitrary successive parameters of this interpolation. Classical tables treat the standard Catalan pentakis dodecahedron and its Archimedean dual, in different metric realizations from the unit-sphere construction here. The distinct post-rhombic result linked below gives a rational volume-product law on that branch and locates its maximum above \(1\). The overlapping upper branch is not claimed here as a separate new law, and no priority between accounts of that branch is asserted. The focus here is the pre-rhombic strict comparison with its exact law and the ordering through the transition. On that branch the primal volume increases linearly, whereas the disjoint polar truncations decrease the polar volume; neither nesting of hulls nor an endpoint-minimization theorem alone orders the intervening volume products.

## Limitations

The theorem is restricted to the explicit one-parameter family and to \(a\le t\le1\); no general monotonicity for arbitrary paths or arbitrary polyhedra is claimed. The specific full-text dissertation of Wimmer (1998) was not accessible, so priority risks remain. The asserted monotonicity is for the product along this family; the cited inscribed endpoint maximizes primal volume, and is not asserted here to globally maximize the volume product among 32-vertex polytopes.

## References

- Steven Hoehner, *On maximum volume polytopes inscribed in the sphere*, arXiv:2611.10777v1, first public 2026-11-07, Theorem 1.4 and Section 7. https://arxiv.org/abs/2611.10777
- F. Barthe and M. Fradelizi, *The volume product of convex bodies with many hyperplane symmetries*, 2011, Theorem 1(i). https://perso.math.u-pem.fr/fradelizi.matthieu/pdf/symmetries-ajm.pdf
- Lienhard Wimmer, *Das maximale Volumen der konvexen Hülle von Punkten auf der Einheitskugel*, PhD thesis, Universität Salzburg, 1998, Chapter IV, cited by Hoehner.
- David McCooey, *Pentakis Dodecahedron*, geometric reference table. https://www.dmccooey.com/polyhedra/java/PentakisDodecahedron.html
- *A unique non-spherical Mahler maximum along the post-rhombic icosahedral hull*, indexed statement. https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-unique-non-spherical-mahler-maximum-along-the-post-rhombic-ico--76971a460352

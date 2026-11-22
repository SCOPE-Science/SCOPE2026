# Strict Santaló-volume growth through the icosahedral rhombic transition

## Finding

Let \(I\subset\mathbb R^3\) be the regular icosahedron with all twelve vertices on the unit sphere, and let \(U\) be its set of twenty outward *unit* face normals. Define \(K_t=\operatorname{conv}(I\cup tU)\). The polytope is centrally symmetric, so its Santaló point is the origin and its affine-invariant volume product is \(\mathcal P(t)=\operatorname{vol}(K_t)\operatorname{vol}(K_t^\circ)\), where \(K_t^\circ=\{x:\langle x,y\rangle\le1\text{ for every }y\in K_t\}\).

**Theorem.** For every real \(t\) with \(a\le t\le1\), its volume product has the explicit two-branch formula below and is strictly increasing. The unique combinatorial transition in the interior is at \(t_0\), where \(K_{t_0}\) is a regular rhombic triacontahedron. At \(t=1\) this family is the thirty-two-vertex inscribed pentakis-dodecahedral volume maximizer of the cited 2026 theorem. Numerically, \(\mathcal P(a)=14.0763745333445\ldots\), \(\mathcal P(t_0)=15.4205486916856\ldots\), and \(\mathcal P(1)=16.2080044346791\ldots\). These are evaluations of the exact expressions, not claims of rationality.

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

For \(a<t<t_0\), the sixty supporting triangles are \(\operatorname{conv}(v,w,tu)\), where \(v,w\) is an edge of the face of \(I\) having outward normal \(u\). For \(t_0<t\le1\), they are \(\operatorname{conv}(v,tu,tu')\), where \(u,u'\) are normals of adjacent icosahedral faces meeting at the vertex \(v\). There are sixty triangles in either case. This is verified by the support-plane test: symmetry reduces each branch to one representative triangle; taking determinant signs against the remaining thirty-two generating points gives no further support switch in the respective intervals. Explicit representative coordinates and the independent finite hull corroboration are in the checker; the underlying sign ranges are \(a\le t\le t_0\) and \(t_0\le t\le1\). The incidence descriptions also prove that no vertex is discarded in these intervals.

**2. Primal volumes.** On the first branch, \(K_t\) is the union of the twenty outward pyramids over the original icosahedral triangles; their bases remain fixed and their apex heights above those face planes are \(t-a\). Hence its volume is linear in \(t\), equal to \(2V_Dt/(1+c)\) by the regular-solid metric identities. On the second branch, \(K_t\) is the union of \(tD\) and twelve pentagonal pyramids, one over each face of \(tD\), with apex the corresponding vertex of \(I\). Each base plane is at radial distance \(ta\) and the pyramidal height is \(1-ta\). Since \(\operatorname{vol}(tD)=t^3V_D\), the sum is \(t^3V_D+(t^2V_D/a)(1-ta)=V_Dt^2/a\).

**3. Polar volumes.** The polar is
\[
K_t^\circ=\{x:\langle x,v\rangle\le1\ (v\in I\text{ vertices}),\quad\langle x,u\rangle\le t^{-1}\ (u\in U)\}.
\]
At \(t=a\) it is the dodecahedron \(D/a\). For \(t\le t_0\), truncating each of its twenty vertices removes a tetrahedral cap. The ratio along each incident edge is \(\tau=(1-a/t)/(1-c)\in[0,1/2]\); the caps have disjoint interiors. A unit-radius dodecahedral vertex and its three neighbors determine a tetrahedron of volume \(\sqrt3(1-c)(1-c^2)/4\); after scaling by \(1/a\) and summing twenty caps, the result simplifies to \(W_-(t)\).

For \(t\ge t_0\), duality with the sixty triangular primal facets gives twelve polar pentagonal facets with outward normal \(v\) at distance one and twenty polar equiangular hexagonal facets with outward normal \(u\) at distance \(t^{-1}\). At the triangle \(\operatorname{conv}(v,tu,tu')\), the corresponding polar vertex is
\[
x=\lambda v+\mu(u+u'),
\]
where solving \(\langle x,v\rangle=1\) and \(\langle x,u\rangle=\langle x,u'\rangle=t^{-1}\) gives the displayed \(\lambda,\mu\). The pentagonal facet has circumradius \(\sqrt{2q}\,\mu\), hence area \(F_5\). The hexagon is equiangular with alternating side lengths \(L\lambda\) and \(2\mu/\sqrt3\), hence area \(F_6\). Decomposing the polar volume into pyramids from the origin gives \(W_+(t)=12F_5/3+20F_6/(3t)\), as claimed. The expressions coincide at the switch by substitution \(\lambda(t_0)=0\).

**4. Strict increase, with rational certificates.** On the first branch define \(h=1-a/t\in[0,(1-c)/2]\). Differentiating \(\mathcal P(t)=[2V_D/(1+c)]t[\,V_D/a^3-C h^3\,]\), where \(C=5\sqrt3(1+c)/(a^3(1-c))\), gives a positive multiple of
\[
V_D-C h^2(3-2h).
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
Exact rational interval arithmetic certifies \(24.898<p_2<24.900\), \(-94.001<p_1<-93.998\), \(-44.567<p_{-1}<-44.562\). Consequently \(E''(t)=2p_2+2p_{-1}/t^3<0\) for \(t\le1\), while \(E'(1)=2p_2+p_1-p_{-1}>0.359\). Therefore \(E'(t)>0\) for all \(t\in[t_0,1]\). Both branches are continuous and increasing; so is the entire product.

## Verification

Run \(\texttt{python check.py}\) from the extracted package. It uses only Python standard libraries for outward-rounded square-root enclosures based on \(\operatorname{isqrt}\) and exact rational endpoints, proving the two derivative inequalities. When NumPy and SciPy are available, ten additional direct convex-hull / halfspace-intersection volume comparisons corroborate the two formulas. The analytic face classifications and interval derivative proof—not the finite samples—are the grounds for the universally quantified theorem.

## Relationship to prior work

The maximum-volume thirty-two-vertex configuration and its unique global optimality are previously established by Hoehner (2026), building on Wimmer (1998); they are not asserted anew. The 2011 theorem of Barthe and Fradelizi gives the regular icosahedron/dodecahedron a minimal Mahler product among bodies with the same reflection symmetries, but does not supply the dual-volume formulas or strict parameter-by-parameter comparison here. Classical tables treat the standard Catalan pentakis dodecahedron and its Archimedean dual, which use a different radial normalization from the unit-sphere construction here. The present result identifies a two-phase *polar* volume law and strict Mahler ordering along the natural symmetry-preserving interpolation between the icosahedron and the newly characterized spherical optimizer.

## Limitations

The theorem is restricted to the explicit one-parameter family and to \(a\le t\le1\); no general monotonicity for arbitrary paths or arbitrary polyhedra is claimed. The specific full-text dissertation of Wimmer (1998) was not accessible from the linked archival site in this inspection, so priority risks remain; the primary 2026 paper attributes earlier primal-volume optimization correctly. No independent mathematical audit has occurred.

## References

- Steven Hoehner, *On maximum volume polytopes inscribed in the sphere*, arXiv:2611.10777v1, first public 2026-11-07, Theorem 1.4 and Section 7. https://arxiv.org/abs/2611.10777
- F. Barthe and M. Fradelizi, *The volume product of convex bodies with many hyperplane symmetries*, 2011, Theorem 1(i). https://perso.math.u-pem.fr/fradelizi.matthieu/pdf/symmetries-ajm.pdf
- Lienhard Wimmer, *Das maximale Volumen der konvexen Hülle von Punkten auf der Einheitskugel*, PhD thesis, Universität Salzburg, 1998, Chapter IV, cited by Hoehner.
- David McCooey, *Pentakis Dodecahedron*, geometric reference table. https://www.dmccooey.com/polyhedra/java/PentakisDodecahedron.html

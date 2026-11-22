# Half-step twist is the unique isoperimetric optimizer among two-ring regular prismatoids

## Finding
For every integer \(n\ge3\), take two congruent, centered, regular Euclidean \(n\)-gons of circumradius \(R>0\), put them in parallel planes a distance \(h>0\) apart, rotate the second through an arbitrary angle \(\phi\), and take their convex hull \(K_{n,R,h,\phi}\). The complete, sharp isoperimetric classification is as follows: among **all** these shapes, with circumradius, height and twist unconstrained except for a fixed positive volume, surface area has a unique minimum up to similarity and planar dihedral symmetry. Its twist is the half-step \(\phi\equiv\pi/n\pmod{2\pi/n}\), so it is a right regular antiprism, and its height-to-base-radius ratio is explicitly determined below.

Write
\[
 c=\cos(\pi/n),\qquad b=1-c,\qquad
 T=c+\sqrt{c^2+3b^2},\qquad Y=\sqrt{T^2-b^2}.
\]
Then the optimal aspect ratio is \(h/R=Y\), and the sharp inequality is
\[
 \frac{S(K)^3}{V(K)^2}\ge
 Q_n:=\frac{72n\sin(\pi/n)(c+T)^3}{Y^2(1+2c)^2},
\]
with equality **if and only if** the foregoing twist and aspect ratio hold. Here \(S\) is ordinary two-dimensional Euclidean boundary area and \(V\) is three-dimensional volume. Consequently the minimum boundary area at prescribed volume \(V_0\) is \(Q_n^{1/3}V_0^{2/3}\).

For \(n=3\) the optimizer is the regular octahedron, with \(Y=\sqrt2\) and \(Q_3=108\sqrt3\). For every \(n\ge4\), the optimal antiprism is strictly *taller* than the uniform antiprism whose triangular side faces are equilateral. The limiting shape under fixed base radius approaches the optimally proportioned circular cylinder:
\[
 \lim_{n\to\infty}Y=2,\qquad \lim_{n\to\infty}Q_n=54\pi.
\]
These are sharp statements for this natural two-parameter family, not for all convex polyhedra with a fixed number of vertices.

## Assumptions and scope
Define \(P_n(R)=\operatorname{conv}\{R(\cos(2\pi j/n),\sin(2\pi j/n)):0\le j<n\}\) and
\[
 K_{n,R,h,\phi}=\operatorname{conv}\bigl((P_n(R)\times\{0\})\cup(\mathcal R_\phi P_n(R)\times\{h\})\bigr),
\]
where \(\mathcal R_\phi\) is planar rotation. Require \(n\ge3\), \(R>0\), and \(h>0\). Reflection and rotation reduce the relative twist to the unique \(\delta\in[0,\pi/n]\) congruent to \(\phi\) modulo rotation and reflection. All quotients are similarity-invariant. In an isoperimetric optimization with fixed volume, the free scaling variable \(R\) is set by the volume constraint after selecting \(h/R\) and \(\delta\). No other symmetry or equal-edge condition is assumed.

## Proof
**1. Facets and exact surface and volume.** Put \(\beta=\pi/n\), \(c=\cos\beta\), \(y=h/R\), and
\[
 a=\cos(\beta-\delta)-\cos\beta,
 \qquad 0\le a\le1-c.
\]
As \(\delta\) goes from \(0\) to \(\beta\), \(a\) increases strictly from \(0\) to \(1-c\). For \(0<\delta\le\beta\), the boundary consists of two polygonal caps and \(2n\) congruent triangles (isosceles at the half-step twist). A cap has area \(nR^2\sin\beta\cos\beta\). Every lateral triangle has base length \(2R\sin\beta\) and its altitude perpendicular to that edge in three dimensions is \(\sqrt{h^2+R^2a^2}\): the horizontal projection of the opposite vertex is \(Ra\) past the supporting line of the edge in its outward normal direction, and any tangential displacement does not contribute to the perpendicular altitude. At \(\delta=0\) the triangles pair into rectangles, with the same limiting total. Therefore
\[
 S=2nR^2\sin\beta\left(c+\sqrt{y^2+a^2}\right).
 \tag{1}
\]
For volume, the section at fractional height \(z\in[0,1]\) is the Minkowski combination \((1-z)P_n(R)+z\mathcal R_\delta P_n(R)\). The polygon area is \(nR^2\sin\beta\,c\), while the mixed area of the two polygons is \(nR^2\sin\beta\cos(\beta-\delta)=nR^2\sin\beta(c+a)\), as follows by summing the support values of the rotated polygon at the outward normals of the original polygon edges. Integrating the quadratic section-area polynomial gives
\[
 V=nR^3y\sin\beta\left(c+\frac a3\right).
 \tag{2}
\]
Both formulas remain valid at the prism and half-step endpoint twists.

**2. Height optimization for a fixed twist.** By (1)–(2), minimizing \(S^3/V^2\) for fixed \(n\) is equivalent to minimizing
\[
 H(y,a)=\frac{(c+\sqrt{y^2+a^2})^3}{y^2(c+a/3)^2},\qquad y>0.
 \tag{3}
\]
Writing \(t=\sqrt{y^2+a^2}\), the sign of \(\partial_y\log H\) is precisely the sign of \(t^2-2ct-3a^2\). It is negative near \(y=0\), positive for large \(y\), and has one positive crossing at
\[
 t_*(a)=c+\sqrt{c^2+3a^2},\qquad
 y_*(a)=\sqrt{t_*(a)^2-a^2}.
 \tag{4}
\]
Thus (4) is the unique global height minimizer. It cannot lie at infinity or zero because \(H\) diverges at both ends.

**3. Strict twist optimization, including endpoints.** Differentiate the optimized logarithm \(\log H(y_*(a),a)\) by the envelope rule. Since \(\partial_y H=0\) at (4), its derivative has the sign of
\[
 \frac{3a}{t_*(c+t_*)}-\frac2{3c+a}.
 \tag{5}
\]
After multiplying by positive denominators and applying \(t_*^2-2ct_*-3a^2=0\), this sign is that of \(9ac-t_*(t_*+4c)\). For \(n\ge3\) we have \(c\ge1/2\) and \(0\le a\le1-c\le c\), whereas \(t_*\ge2c\). Consequently
\[
 9ac-t_*(t_*+4c)\le9c^2-12c^2=-3c^2<0.
 \tag{6}
\]
Hence the optimal quotient decreases **strictly** with every increase of twist \(\delta\in[0,\beta]\), even though one is simultaneously allowed to re-optimize the height. It reaches its sole minimum at \(a=b=1-c\), equivalent to the half-step twist. Substitution into (1)–(4) gives \(Y\) and \(Q_n\) in the Finding. Positive homothety fixes the requested volume and cannot create any other equality cases.

**4. Edge-uniform comparison and limit.** At half-step twist, the polygonal base edges have squared length \(4R^2(1-c^2)\), and each connecting edge has squared length \(R^2(y^2+2(1-c))\). Equilateral lateral faces therefore correspond to
\[
 y_{\mathrm U}=\sqrt{2(1-c)(1+2c)}.
\]
For \(n=3\), \(c=1/2\) and (4) gives \(Y=y_{\mathrm U}=\sqrt2\). For \(n\ge4\), \(c\ge1/\sqrt2\), so
\[
 2c>\sqrt{3(1-c^2)}=\sqrt{y_{\mathrm U}^2+b^2},
\]
while \(T\ge2c\); hence \(Y>y_{\mathrm U}\). Finally \(\cos(\pi/n)\to1\) and \(n\sin(\pi/n)\to\pi\), so \(T,Y\to2\) and the expression for \(Q_n\) tends to \(54\pi\). At \(n=3\), direct substitution yields \(108\sqrt3\). This completes the proof.

## Verification
The accompanying standalone `verify_antiprism_isoperimetry.py` constructs the convex hull of every vertex configuration independently using a three-dimensional hull algorithm. It checks the surface and volume formulas against its facet areas and tetrahedral volume calculation for \(3\le n\le18\), seven relative twists and three independent radius/height pairs. It also numerically tests the sharp bound and strict optimizer against a two-parameter family of competitors for \(3\le n\le100\), exact low-order normalization and the cylinder limit. The recorded execution returned `TWISTED_PRISMATOID_ISOPERIMETRY_OK 5582`. These finite floating-point checks are **not** used to prove the global assertions; the proof above is analytic for every integer \(n\ge3\) and all real geometry parameters.

Run from an extracted package directory with `python verify_antiprism_isoperimetry.py`; Python 3, NumPy and SciPy are the only dependencies.

## Relationship to prior work
Abrosimov and Vuong (2021) study antiprism geometry in spherical space and explicitly describe the ordinary antiprism family, but their theorems concern spherical existence and volume integrals, not the Euclidean isoperimetric optimization here. Horváth and Lángi (2013) study convex-hull volumes of congruent bodies under isometries; their general translation/reflection extremal results do not supply a three-dimensional boundary-area/volume quotient or jointly optimize the twist and base separation of regular parallel polygonal rings.

An earlier public calculation, *Exact John–Löwner ellipsoid profile of twisted regular polygonal prismatoids* (2026), derives exactly the **volume** formula in (2) and optimizes ellipsoid-volume ratios under rotation. Its distinct theorem does not provide (1), the joint isoperimetric optimization, or the unique height (4). Two related public antiprism studies identify respectively the height minimizing mean silhouette complexity (the **edge-uniform** realization) and the height minimizing maximum dihedral angle. Neither theorem implies the present sharp surface-area/volume classification. The strict difference from the edge-uniform silhouette optimizer for every \(n\ge4\) provides an independently interpretable geometric contrast.

## Limitations
The extremal statement applies only to the convex hull of **two** congruent centered regular polygons in parallel planes. Unequal bases, offsets of the projected centers, arbitrary planar convex bases, non-Euclidean volume, and unconstrained polyhedra are not covered. The limit to the optimal circular-cylinder ratio is a limit inside this family, not a general isoperimetric assertion. Some previously published mixed-area ingredients are reused and not claimed as new. Historical priority is assessed against accessible documents and indexed records; an unindexed full-strength treatment of isoperimetric antiprisms or a theorem implying it remains a residual risk. Independent mathematical validation is not part of this package.

## References
1. N. V. Abrosimov and B. Vuong, *The volume of a spherical antiprism*, arXiv:2110.12265v1, first posted 2021-10-23, https://arxiv.org/abs/2110.12265 .
2. Á. G. Horváth and Z. Lángi, *On the volume of the convex hull of two convex bodies*, arXiv:1302.6164 (2013), https://arxiv.org/abs/1302.6164 .
3. *Exact John–Löwner ellipsoid profile of twisted regular polygonal prismatoids* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-john-l-wner-ellipsoid-profile-of-twisted-regular-polygonal--4eb565e76a67 .
4. *Uniform antiprisms uniquely minimize mean planar-silhouette complexity in every order* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-uniform-antiprisms-uniquely-minimize-mean-planar-silhouette-comp--b44d8c773553 .
5. *Equidihedral minimax and volume–angle separation in regular antiprisms* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-equidihedral-minimax-and-volume-angle-separation-in-regular-anti--12f724b4a957 .

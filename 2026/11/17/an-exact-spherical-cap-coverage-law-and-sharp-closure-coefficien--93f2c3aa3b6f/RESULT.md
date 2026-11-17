# An exact spherical-cap coverage law and sharp closure coefficients for staggered latitude rings

## Finding
For every integer \(n\ge3\) and \(0<h<1\), put \(a=\sqrt{1-h^2}\) and consider the following \(2n\) unit-sphere sites, consisting of equally spaced rings at opposite heights and separated by a half angular step:
\[
 v_j^+=(a\cos(2\pi j/n),a\sin(2\pi j/n),h),\quad
 v_j^-=(a\cos((2j+1)\pi/n),a\sin((2j+1)\pi/n),-h),\quad j=0,\ldots,n-1.
\]
For a uniform surface-area direction \(X\in S^2\), set \(T(X)=\min_j\{\arccos(X\cdot v_j^+),\arccos(X\cdot v_j^-)\}\) and \(U_{n,h}(r)=\Pr(T(X)>r)\). Define \(\Delta=\pi/n\), \(t=\cos r\), and for \(-1<z<1\)
\[
 A_\pm(z;r)=\arccos\!\left(\operatorname{clip}_{[-1,1]}\frac{t\mp hz}{a\sqrt{1-z^2}}\right).
\]
Then **for all** \(n\ge3\), \(0<h<1\), and \(0\le r\le\pi\), the exact uncovered fraction, or equivalently the entire nearest-site distance distribution, is
\[
 \boxed{U_{n,h}(r)=\frac12\int_{-1}^1\left[1-\frac{A_+(z;r)+A_-(z;r)}{\Delta}\right]_+\,dz.}\tag{1}
\]
Here \([u]_+=\max(u,0)\) and \(\operatorname{clip}_{[-1,1]}\) truncates a real number to the interval \([-1,1]\). This is an exact one-dimensional integral with no polygonal numerical approximation.

Specialize to the previously known **covering-optimal** height within this two-ring family,
\[
 c=\cos(\pi/n),\quad s=\sin(\pi/n),\quad h_*^2=\frac{c}{1+c},\quad \rho_*=\arccos h_*.
\]
The **new sharp all-order gap-closure law** is
\[
 \boxed{U_{n,h_*}(\rho_*-\varepsilon)
 =K_n\varepsilon^2+O_n(\varepsilon^3),\qquad
 K_n=\frac{n(1+c)}{\pi c s},\quad \varepsilon\downarrow0.}\tag{2}
\]
For fixed \(n\), this controls the extreme proximity of a random direction to the largest empty caps. In particular, if \(X_1,\ldots,X_m\) are independent uniform sphere directions and \(Z_m=\max_{j\le m} T(X_j)\), then for each fixed \(x\ge0\)
\[
 \boxed{\lim_{m\to\infty}\Pr\!\left(\sqrt m(\rho_*-Z_m)>x\right)
 =\exp(-K_nx^2).}\tag{3}
\]
The coefficients grow as \(K_n=2n^2/\pi^2+5/6+O(n^{-2})\). The already established square-antiprism special case is \(K_4=(8+4\sqrt2)/\pi\); it is **not** claimed as new, and neither is the previously known optimal height or covering radius.

## Assumptions and scope
The sphere has radius one and normalized rotation-invariant area measure; all cap radii are geodesic angles in radians. The two rings have the same horizontal radius, equal populations, opposite heights and precisely half-step relative twist. Heights range over the open interval \((0,1)\); formula (1) permits every cap radius from zero to \(\pi\), including hemispheres and larger caps. At the measure-zero poles the integrand can be assigned arbitrary values. Formula (2) concerns a *fixed* integer \(n\), with a remainder constant that may depend on \(n\); it does not assert a two-parameter uniform limit as \(n\to\infty\) and \(\varepsilon\to0\). No unrestricted optimum over all spherical \(2n\)-point sets is asserted.

## Proof
**1. Exact distribution by horizontal slicing.** Parameterize the sphere by \(X=(\sqrt{1-z^2}\cos\theta,\sqrt{1-z^2}\sin\theta,z)\). Its normalized area measure is \(dz\,d\theta/(4\pi)\). For fixed \(z\), an upper site covers precisely the circular arc whose azimuthal half-width is \(A_+(z;r)\); its dot product with \(X\) is \(a\sqrt{1-z^2}\cos(\theta-2\pi j/n)+hz\). The corresponding lower arc has half-width \(A_-(z;r)\) around longitude \((2j+1)\pi/n\). The clamp handles both empty arcs and entire circles. On each of the \(2n\) successive half-step intervals of length \(\Delta\) between the alternating upper and lower site longitudes, the closest longitude of either ring is one of its endpoints. Therefore its uncovered angular length is exactly \([\Delta-A_+-A_-]_+\), even if individual arcs cover adjacent intervals. Summing these intervals and integrating \(z\) gives (1), including all thresholds and all heights.

**2. Existing covering geometry and its contact points.** The convex hull of the \(2n\) sites at \(h=h_*\) has two polar regular \(n\)-gonal faces and \(2n\) triangular lateral faces. The minimum distance from the origin to any supporting face plane is \(h_*\); hence \(\max T=\rho_*\). The polar face normals are the poles, and each triangular lateral face has a different unit normal at the same support distance. To verify the last assertion without numerical input, choose one triangular face with upper sites at angular offsets \(\pm\Delta\) and a lower site at longitude zero. Its outward unit normal is
\[
 w=(b,0,q),\qquad b=\frac{2\sqrt c}{1+c},\quad q=\frac{1-c}{1+c},\quad b^2+q^2=1.
\]
Direct substitution yields \(v\cdot w=h_*\) for these three vertices, while every other vertex has strictly smaller dot product because it has a larger angular separation from its nearest longitude. The rotated copies are the other lateral triangles; together with the polar faces they comprise the entire polyhedral boundary. All \(2n+2\) face normals are distinct for fixed \(n\ge3\), so these are precisely the isolated maximizers of \(T\). This also recovers the previously known covering radius, but does not treat that radius as original.

**3. Local area at the two polar contact points.** Write an exponential tangent coordinate \(X=\exp_{(0,0,1)}(\varepsilon y)\). As \(\varepsilon\downarrow0\),
\[
 \cos(\rho_*-\varepsilon)=h_*+a_*\varepsilon+O(\varepsilon^2),\qquad a_*=\sqrt{1-h_*^2}.
\]
The \(n\) active upper vertices give the first-order inequalities
\[
 \cos(2\pi j/n)y_1+\sin(2\pi j/n)y_2<1\quad(0\le j<n).
\]
They bound a regular \(n\)-gon of inradius one and area \(n\tan\Delta\). The south pole contributes the same area. The spherical-area Jacobian in the rescaled coordinates is \(\varepsilon^2(1+O(\varepsilon^2))\).

**4. Local area at each of the \(2n\) lateral contacts.** Use tangent basis \(e_1=(0,1,0)\), \(e_2=(-q,0,b)\) at the normal \(w\) above. The projections of the two active upper vertices onto the plane, divided by \(a_*\), are \((\pm s,c)\); the corresponding projection of the active lower vertex is \((0,-1)\). The first-order uncovered region in scaled tangent coordinates is therefore
\[
 sy_1+cy_2<1,\qquad -sy_1+cy_2<1,\qquad -y_2<1.
\]
It is a triangle with base width \(2(1+c)/s\), height \(1+1/c\), and area \((1+c)^2/(cs)\). Its \(2n\) rotated copies have the same area.

**5. Exhaustion, remainder, and coefficient.** Because there are only finitely many isolated strict facet normals, away from their disjoint neighborhoods the support function is uniformly greater than \(h_*\). For sufficiently small \(\varepsilon\), no uncovered points lie outside those neighborhoods. At each contact the three or \(n\) active tangent constraints are nondegenerate and have smooth \(\varepsilon\)-dependent boundaries; their bounded polygonal rescalings differ from the limiting polygon by \(O_n(\varepsilon)\), yielding physical-area error \(O_n(\varepsilon^3)\). Summing the area contributions and dividing by the sphere area \(4\pi\) gives
\[
 K_n=\frac{2n\tan\Delta+2n(1+c)^2/(cs)}{4\pi}
 =\frac{n(1+c)}{\pi cs}.
\]
The final simplification uses \(s^2=1-c^2\). Taylor expansions of \(c\) and \(s\) establish the stated large-\(n\) coefficient. For independent probes, \(\Pr(\rho_*-Z_m>t/\sqrt m)=(1-U_{n,h_*}(\rho_*-t/\sqrt m))^m\); substituting (2) proves (3), without requiring a finite-sample independence assumption beyond the stated independent probe directions.

## Verification
The standalone `verify_antiprism_law.py`, requiring Python, NumPy and SciPy, ran successfully with `ANTIPRISM_TAIL_VERIFIED 550 assertions`. It independently reconstructs triangular and polar facets via `scipy.spatial.ConvexHull` for eight values of \(n\); checks 32 small-radius deficits against separately integrated horizontal interval-root geometry; and compares 468 circular-angle memberships from actual three-dimensional dot products against the exact latitude formula for both optimal and arbitrary heights, including cap radii above \(\pi/2\). It also checks the independently known \(n=3\) and \(n=4\) limiting constants. The proof for all real heights, radii and integer orders is the analysis above, not the finite tests.

## Relationship to prior work
Roychowdhury (2026) develops exact *discrete-distribution* geodesic quantization on the equator and on latitude rings. Its two-small-circle model concerns discrete supports and optimally placed representatives, not the distribution of nearest distance from a uniform direction across the entire sphere to a fixed staggered antiprism. This study motivates the distinct fixed-code spherical problem here.

*Sharp spherical covering by two twisted regular latitude rings* (2026) already proves the exact covering radius for all heights and twists, with the uniquely optimal half-step twist and height \(h_*\); these geometric threshold and optimization facts are explicitly prior, and no novelty is asserted for them. Its result does not state the all-radii uncovered-area integral, the explicit all-\(n\) tail coefficient, or the probe-extreme distribution; knowing only the covering radius does not imply a local area coefficient.

*Ten-hole quadratic closure law for an eight-site spherical antiprism* (2026) already proves the \(n=4\) case and even identifies its ten local holes and coefficient \((8+4\sqrt2)/\pi\). That case is expressly excluded from a stand-alone novelty claim. The addition here is the complete all-height and all-radius distribution formula, the general every-order face-tangent calculation and the full formula for \(n\ge3\), with new orders beyond the isolated cases. Published nearest-direction laws for the icosahedron, icosidodecahedron, and cube–octahedron compound concern different fixed spherical codes, and do not imply antiprism values.

Fowler, Tarnai and Gáspár (2002) numerically and geometrically study best cap-covered area as the radius varies for selected antipodally constrained point sets; their configurations are in general reoptimized at each radius, in contrast with the fixed antiprism, and the work does not furnish this exact all-order distribution or coefficient. The older paper remains an important historical comparison rather than a source of any new assertion of global optimality.

## Limitations
The formula is a one-dimensional integral, not asserted to be elementary in all parameter ranges. The local tail requires a *fixed* order and the covering-optimal latitude; no claimed uniform error in the order and no optimum over unrestricted point sets is supplied. The Rayleigh-type extreme limit describes independent random probe directions for a fixed site set, not random sites. Verification is numerical and finite; historical priority can remain uncertain for classical analyses under other names or in unindexed literature. The special square-antiprism tail, covering geometry and basic local tangent-plane method have prior antecedents. Independent mathematical audit has not been performed.

## References
1. M. K. Roychowdhury, *Discrete Quantization on Spherical Geometries: Explicit Models, Computations, and Didactic Exposition*, Mathematics **14** (2026), 750. https://doi.org/10.3390/math14050750 ; https://arxiv.org/abs/2605.00006 .
2. *Sharp spherical covering by two twisted regular latitude rings* (2026), published mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-spherical-covering-by-two-twisted-regular-latitude-rings--d6c704c1d311 .
3. *Ten-hole quadratic closure law for an eight-site spherical antiprism* (2026), existing prior mathematical record; the \(n=4\) special coefficient is acknowledged as prior.
4. P. W. Fowler, T. Tarnai and Zs. Gáspár, *From circle packing to covering on a sphere with antipodal constraints*, Proceedings of the Royal Society A **458** (2002), 2275–2287. https://doi.org/10.1098/rspa.2002.0990 .
5. *The exact nearest-direction law of the regular icosahedron* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-the-exact-nearest-direction-law-of-the-regular-icosahedron--23de31ea3def .
6. *Exact angular contact law of the 30-vertex icosidodecahedral spherical code* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-angular-contact-law-of-the-30-vertex-icosidodecahedral-sph--26f54352ffa9 .
7. *Exact fourteen-site spherical coverage law and quadratic closure of the cube–octahedron gaps* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-fourteen-site-spherical-coverage-law-and-quadratic-closure--30bf08287af3 .

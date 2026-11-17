# Odd-base bipyramids have a sharp parity defect in full-shadow visibility

## Finding
For each **odd integer** \(n\ge5\) and height \(h>0\), let \(B_{n,h}\) be the convex hull in \(\mathbb R^3\) of the circumradius-one regular \(n\)-gon in the horizontal plane and the two points \((0,0,\pm h)\). Project orthogonally onto a Haar-uniform unoriented plane. The shadow has all \(n+2\) original vertices precisely on an event with probability
\[
\boxed{P_n(h)=\frac{2n}{\pi}\left[2\arcsin\!\left(t\sin\frac\pi n\right)-\arcsin\!\left(t\sin\frac\pi{2n}\right)-\arcsin\!\left(t\sin\frac{3\pi}{2n}\right)\right]},
\qquad t=\frac{h}{\sqrt{h^2+\cos^2(\pi/n)}}.
\]
This probability is positive for finite \(h>0\) and tends to zero for \(h\downarrow0\) and \(h\to\infty\). Every height at which it is globally maximal lies in the **explicit interval**
\[
\boxed{\frac{\cos(\pi/n)}{\sqrt2\cos(\pi/(2n))}\le h_{n,\max}\le
\frac{\cos(\pi/n)}{\sqrt2\cos(3\pi/(2n))}.}
\]
The theorem does not assert uniqueness of the finite-\(n\) maximizer. It gives the sharp asymptotic law
\[
\boxed{n^2P_n(h)\longrightarrow\frac{\pi^2}{2}\frac{h}{(1+h^2)^{3/2}}\quad\text{for each fixed }h>0,}
\]
and, for *any* choice of maximizing heights,
\[
\boxed{h_{n,\max}\longrightarrow\frac1{\sqrt2},\qquad
n^2\max_{h>0}P_n(h)\longrightarrow\frac{\pi^2}{3\sqrt3}.}
\]
All limits in the last two displays are taken along odd integers. The leading maximal probability is exactly **one half** of that for the corresponding single-apex regular-pyramid family; for even polygonal bipyramids the full-vertex event agrees with the single-apex event and thus has the larger coefficient. The known single-apex result is explicitly not claimed as new.

## Assumptions and scope
Put \(\delta=\pi/n\) and \(c=\cos\delta\). The base vertices are \((\cos(2\pi j/n),\sin(2\pi j/n),0)\) for \(j=0,\ldots,n-1\). The plane is sampled from the rotation-invariant probability measure on the unoriented Grassmannian of two-planes through the origin. A projected vertex means a distinct extreme point of the projected polygon. Exceptional viewing normals that make the restriction of projection to the base plane singular, or create collinear planar vertices, have probability zero. The two apices are equidistant from the base plane. Scaling all coordinates by the same positive factor has no effect on the probability.

## Proof
**1. An affine planar reduction and its probability law.** Let \(u=(u_1,u_2,u_3)\) be the unit normal, chosen in the hemisphere \(u_3>0\). Away from the null set \(u_3=0\), orthogonal projection to \(u^\perp\), restricted to \(z=0\), is a linear isomorphism. Under its inverse, the two projected apices become \(\pm b\), where \(b=h(u_1,u_2)/u_3\) (the sign convention is immaterial because both are present). Thus the random shadow is affinely equivalent to \(\operatorname{conv}(P_n\cup\{b,-b\})\), with \(P_n\) the planar regular polygon. Spherical area measure under the ratio map \(u\mapsto b\) gives
\[
\boxed{f_h(b)=\frac{h}{2\pi(h^2+\|b\|^2)^{3/2}}\quad(b\in\mathbb R^2).}
\]
In particular the polar angle of \(b\) is uniform, and at fixed angle the probability of radius in \((a,z)\), \(0<a<z\), is
\[
 h\left(\frac1{\sqrt{h^2+a^2}}-\frac1{\sqrt{h^2+z^2}}\right).
\]
This radial law is normalized: its density integrates to one over \(\mathbb R^2\).

**2. The full-silhouette geometric criterion.** The polygon has support description \(P_n=\{x:\langle x,v_j\rangle\le c\text{ for all }j\}\), with outward unit side normals \(v_j\) separated by angles \(2\pi/n\). For a generic exterior point \(b\), adding \(b\) preserves all old vertices if and only if \(b\) violates exactly one of the polygon's support-line inequalities: it then replaces exactly the open edge between the two endpoint vertices. If two or more adjacent inequalities are violated, the intermediate original polygon vertex is lost. A point inside the polygon is not a new vertex. For the pair \(b,-b\), their segment crosses the interior of \(P_n\); for odd \(n\ge5\), the unique violated edges, when they exist, are nonadjacent. Hence all original base vertices and both apices survive simultaneously if and only if **each of \(b\) and \(-b\) violates exactly one support inequality**. This criterion can also be checked directly by ordering the tangent rays from each exterior point to the strictly convex polygonal vertex sequence.

**3. Opposite-facet parity.** By rotational and reflection symmetry restrict the polar angle \(\alpha\) of \(b\) to \(0\le\alpha\le\delta\), measured from one nearest outward side normal. The nearest and second-nearest side-normal angular distances for \(b\) are \(\alpha\) and \(2\delta-\alpha\). Because \(n\) is odd, for \(-b\) these two distances are \(\delta-\alpha\) and \(\delta+\alpha\), not the same pair. Since \(n\ge5\), all four distances are strictly less than \(\pi/2\) except for harmless endpoints, and the radial interval for exactly one violated side is determined by the nearest and second-nearest side normals.
Consequently the allowed radius at angle \(\alpha\) lies in the intersection
\[
\left(c\sec\alpha,\ c\sec(2\delta-\alpha)\right)
\cap\left(c\sec(\delta-\alpha),\ c\sec(\delta+\alpha)\right).
\]
For \(0\le\alpha\le\delta/2\), the resulting interval is \((c\sec(\delta-\alpha),c\sec(\delta+\alpha))\); for \(\delta/2\le\alpha\le\delta\), it is \((c\sec\alpha,c\sec(2\delta-\alpha))\). It is nonempty for every interior \(\alpha\), and closes at the endpoints. Thus, writing
\[
 g_h(s)=\frac{h\cos s}{\sqrt{c^2+h^2\cos^2s}},
\]
which is positive for \(0\le s\le3\delta/2<\pi/2\), the normalized angular integral is
\[
 P_n(h)=\frac n\pi\int_0^\delta\left[g_h(\alpha_{\mathrm{low}})-g_h(\alpha_{\mathrm{high}})\right]d\alpha
 =\frac{2n}{\pi}\left(\int_{\delta/2}^{\delta}g_h(s)\,ds-\int_{\delta}^{3\delta/2}g_h(s)\,ds\right).
\]
The antiderivative is elementary:
\[
 \int g_h(s)\,ds=\arcsin\!\left(\frac{h\sin s}{\sqrt{h^2+c^2}}\right).
\]
This proves the asserted exact formula. Strict positivity follows also because \(g_h\) is strictly decreasing on \((0,3\delta/2)\) for \(h>0\). At \(h\downarrow0\) the formula tends to zero; as \(h\to\infty\) the arcsines tend to the corresponding angles and their displayed second difference vanishes.

**4. A finite-order interval for every maximizing height.** From the permitted radii in step 3, every eligible \(b\) has
\[
 r_{\min}=\frac c{\cos(\delta/2)}\le \|b\|\le
 r_{\max}=\frac c{\cos(3\delta/2)}.
\]
The integrand in the planar probability representation is proportional to \(k_h(r)=h(h^2+r^2)^{-3/2}\), whose derivative has the sign of \(r^2-2h^2\). Hence \(P_n(h)\) is strictly increasing on \((0,r_{\min}/\sqrt2)\) and strictly decreasing on \((r_{\max}/\sqrt2,\infty)\). Since it is continuous, positive somewhere and vanishes at both endpoints, a maximum exists and all its locations satisfy the displayed interval. No assertion of finite-order uniqueness is needed.

**5. The sharp parity asymptotic.** Fix \(h>0\), put \(t_n=h/\sqrt{h^2+\cos^2\delta}\), and expand uniformly for \(t_n\in(0,1)\):
\[
\arcsin(t_n\sin s)=t_n s-\frac{t_n(1-t_n^2)}6s^3+O(s^5)
\quad(s\to0).
\]
Therefore
\[
2\arcsin(t_n\sin\delta)-\arcsin(t_n\sin(\delta/2))
-\arcsin(t_n\sin(3\delta/2))
=\frac{t_n(1-t_n^2)}4\delta^3+O(\delta^5).
\]
The exact expression gives
\[
 n^2P_n(h)\longrightarrow\frac{\pi^2}{2}\frac{h}{(1+h^2)^{3/2}}.
\]
The height bracket in step 4 squeezes every optimizer to \(1/\sqrt2\). The expansion is uniform on any compact positive-height interval, so evaluating at the maximizing heights yields \(n^2\max P_n\to\pi^2/(3\sqrt3)\); the limiting profile has its unique maximum at \(h=1/\sqrt2\).

**6. Comparison with even parity and with a single apex.** For even \(n\), side normals occur in antipodal pairs. Exactly one violated side inequality for \(b\) automatically means exactly one (opposite) violated side inequality for \(-b\). The two-apex full-vertex event therefore agrees with the single-apex pyramid event. Its probability is the already-known expression
\[
\frac n\pi\left[2\arcsin\!\left(t\sin\delta\right)
-\arcsin\!\left(t\sin2\delta\right)\right],
\]
whose fixed-height leading coefficient is \(\pi^2h/(1+h^2)^{3/2}\). For odd \(n\), the second apex imposes an additional nontrivial condition; for example, on the outward normal ray of a base side, radii between \(c\) and \(1\) make the first apex extreme but the opposite apex interior. Thus the single-apex marginal is strictly larger, and the limiting coefficient is precisely twice the odd-bipyramid coefficient. The even formula and its optimization are prior coverage, not new findings.

## Verification
The file `verify_odd_bipyramid.py` is a standalone Python 3 checker with no external package dependencies. Run `python verify_odd_bipyramid.py`. It independently computes the proposed law via numerical angular/radial quadrature, reconstructs planar convex hulls after sampling the Cauchy affine images of random viewing normals, compares those hulls against the support-line criterion, tests simulated probabilities, and checks the large-order coefficient and optimizing-height bounds. The mathematical proof is the analysis above; finite numerical testing is not a substitute for its universal quantifiers.

## Relationship to prior work
Black and Criado's 2024 preprint (published as an open-access article in 2026) provides general expected-random-shadow complexity bounds and normal-fan viewpoints. Those bounds do not evaluate the odd-bipyramid all-vertex event. A previous regular-pyramid full-silhouette computation gives the displayed one-apex expression and covers the even-bipyramid consequence; that work is credited rather than restated as new. The additional antipodal requirement for odd side counts has a different radial intersection geometry and produces the distinct four-arcsine combination and factor-of-two asymptotic. The derivation here compares full events, not merely matching paper titles or numerical parameters. Priority remains provisional: an older equivalent calculation under angular visibility or stereological terminology may exist.

## Limitations
The exact theorem requires odd \(n\ge5\), a right symmetric bipyramid with equally spaced unit-circumradius base vertices, equal apex heights, and Haar-uniform orthogonal projections. It gives a nontrivial bracket and common asymptotic limit for maximizing heights but **does not prove uniqueness** of a finite-order maximizing height. It does not claim the full distribution of all possible silhouette vertex counts, asymmetric apices, irregular bases, or nonuniform/perspective projections. Its mathematical novelty assessment is provisional pending external priority review, and no independent audit has been performed.

## References
1. Alexander E. Black and Francisco Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936, first posted June 11, 2024; later published in *Discrete & Computational Geometry* (2026), DOI:10.1007/s00454-026-00880-4. General expected-shadow bounds; neither odd-bipyramid formula nor the parity asymptotic.
2. Prior regular-polygonal-pyramid full-silhouette calculation (comparison statement reproduced in step 6). Its already-established one-apex result is not claimed here.

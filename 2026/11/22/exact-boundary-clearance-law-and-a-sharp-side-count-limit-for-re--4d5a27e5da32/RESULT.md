# Exact boundary-clearance law and a sharp side-count limit for regular ideal hyperbolic polygons

## Finding

Let \(P_n\) be the regular ideal \(n\)-gon in the curvature-\(-1\) hyperbolic plane, for an integer \(n\ge3\). Choose \(X_n\) uniformly with respect to hyperbolic area on \(P_n\), and let \(D_n\) be the intrinsic hyperbolic distance from \(X_n\) to the polygon boundary. Put \(\alpha_n=\pi/n\) and \(\rho_n=\operatorname{arsinh}(\cot\alpha_n)\). Then, for every \(0<t<\rho_n\), the **complete** cumulative distribution and probability density are

\[
F_n(t)=\Pr(D_n\le t)=\frac{2n}{(n-2)\pi}\left[\arctan(\sinh t)+\sinh t\log\bigl(\cos\alpha_n\,\coth t\bigr)\right],
\]
\[
f_n(t)=\frac{2n}{(n-2)\pi}\cosh t\log\bigl(\cos\alpha_n\,\coth t\bigr).
\]

The CDF is zero at \(t\le0\) and one at \(t\ge\rho_n\); the density vanishes off \((0,\rho_n)\). In particular, for every pair of integers \(3\le n<m\),

\[
F_n(t)>F_m(t)\quad\text{for every }0<t<\rho_m.
\]

Consequently the sequence \(D_n\) is strictly increasing in the usual stochastic order. Although \(\rho_n\to\infty\), these distributions converge to a **proper, nondegenerate** limit \(D_\infty\), whose density and CDF, for \(t>0\), are

\[
f_\infty(t)=\frac2\pi\cosh t\log\coth t,\qquad
F_\infty(t)=\frac2\pi\left[\arctan(\sinh t)+\sinh t\log\coth t\right].
\]

Moreover, convergence has an **exact** finite-size total variation distance:

\[
\boxed{d_{\mathrm{TV}}\bigl(\mathcal L(D_n),\mathcal L(D_\infty)\bigr)=
\frac4{\pi(n-2)}\arcsin\left(\cos^{n/2}\!\frac\pi n\right)
=\frac2n-\frac{2\sqrt2}{n^{3/2}}+O(n^{-2}).}
\]

The density difference changes sign exactly once, at
\[
t_n^*=\operatorname{artanh}\left(\cos^{n/2}\!\frac\pi n\right),
\]
which lies strictly between zero and \(\rho_n\). The limit has the exponentially decaying upper tail \(\Pr(D_\infty>t)\sim(2/\pi)e^{-t}\). The known ideal-triangle special case and the previously established universal small-clearance expansion for fixed ideal polygons are explicitly not proposed as discoveries here; the contribution is the global regular-polygon family, stochastic ordering, and exact quantitative limit.

## Assumptions and scope

The regular ideal polygon has ideal vertices equally spaced on the boundary of a Poincaré disk. Each side is the complete geodesic joining consecutive ideal vertices. Sampling means normalized intrinsic *area* measure, not Euclidean disk measure, boundary measure or geodesic measure. The polygon area equals \((n-2)\pi\) by Gauss–Bonnet; therefore the uniform probability measure is well defined despite its infinite side lengths. Distances are intrinsic hyperbolic distances to the union of the sides. Results hold for every fixed integer \(n\ge3\), with no unproved interchange of the limits \(n\to\infty\) and \(t\to0\).

## Proof

### Hyperbolic side coordinates

Set \(\alpha=\pi/n\) and denote the centered incircle radius by \(\rho\). The standard right ideal triangle gives \(\cosh\rho=\csc\alpha\), hence \(\sinh\rho=\cot\alpha\) and \(\tanh\rho=\cos\alpha\). Fix one side, its closest point to the polygon center, and a geodesic normal from that point to the center. In hyperboloid polar coordinates \((r,\theta)\) about the center, the signed distance \(\delta\) to this side satisfies

\[
\sinh\delta=\cot\alpha\cosh r-\csc\alpha\sinh r\cos\theta.
\]

The inward offsets from all \(n\) sides define the superlevel region \(P_n(t)=\{x\in P_n:d(x,\partial P_n)\ge t\}\). Adjacent offset hypercycles intersect on the bisector between their inward side normals, so \(\theta=\alpha\). Substituting \(\delta=t\) in the displayed signed-distance identity gives the exact radial position of their intersection,

\[
r_t=\log\frac{\cot\alpha}{\sinh t}.
\]

This is nonnegative exactly for \(t\le\rho\); the superlevel set collapses to the polygon center at \(t=\rho\).

### Entire level-set perimeter and area

Let \(s_t\) denote the unsigned distance *along the original side* from its center footpoint to the perpendicular projection of an intersection vertex of neighboring offset hypercycles. The hyperbolic right-triangle identity in Fermi coordinates gives

\[
\sinh s_t=\frac{\sinh r_t\sin\alpha}{\cosh t}.
\]

Inserting the formula for \(r_t\) and simplifying the hyperbolic sine yields the exact expression

\[
s_t=\log(\cos\alpha\,\coth t).
\]

A hypercycle at normal distance \(t\) from its axis has Fermi metric \(dt^2+\cosh^2t\,ds^2\), so each of the \(n\) boundary arcs of \(P_n(t)\) has length \(2s_t\cosh t\). Hence

\[
L_n(t)=2n\cosh t\log(\cos\alpha\,\coth t).
\]

The nearest-side distance has unit gradient away from a finite union of bisectors and their intersections, which has zero area. Applying the coarea formula (or differentiating the inward Fermi strips) gives \(A_n'(t)=-L_n(t)\) for \(0<t<\rho\), where \(A_n(t)=\operatorname{Area}(P_n(t))\). Since \(A_n(\rho)=0\), integrate the perimeter. The elementary antiderivative

\[
\int\cosh t\log(\cos\alpha\coth t)\,dt
=\arctan(\sinh t)+\sinh t\log(\cos\alpha\coth t)
\]

is verified by differentiation. The lower endpoint of this antiderivative is zero; the upper endpoint is \((\pi/2-\alpha)\). Consequently \(A_n(0)=(n-2)\pi\), consistently with Gauss–Bonnet. Dividing \(A_n(0)-A_n(t)\) by \(A_n(0)\) proves the CDF and differentiating proves the density, including their support and normalization.

### Strict stochastic ordering

Permit the continuous parameter \(x=\pi/n\in(0,\pi/3]\), and write \(\rho(x)=\operatorname{artanh}(\cos x)\). For \(t<\rho(x)\), put

\[
W(t)=\frac{\arctan(\sinh t)}{\sinh t}+\log\coth t.
\]

Both summands are strictly decreasing for \(t>0\). From \(\tanh\rho(x)=\cos x\),

\[
W(\rho(x))=(\pi/2-x)\tan x-\log\cos x.
\]

Writing \(F_x(t)=2\sinh t\,[W(t)+\log\cos x]/(\pi-2x)\), differentiation at fixed \(t<\rho(x)\) gives

\[
\frac{\partial F_x(t)}{\partial x}
=\frac{4\sinh t}{(\pi-2x)^2}\,[W(t)-W(\rho(x))]>0.
\]

Since \(x=\pi/n\) decreases with \(n\), increasing the number of sides strictly decreases the CDF where both supports are active. If \(t\) lies above the shorter support endpoint but below the longer one, the strict comparison is immediate from the support definition. This proves the stated ordering for all integer pairs.

### Limit and the exact total variation error

For every fixed positive \(t\), the finite CDF formula tends to the asserted \(F_\infty(t)\) as \(n\to\infty\). The limiting formula tends to zero at \(t\downarrow0\) and one at \(t\to\infty\), so it defines a proper probability law. Its derivative is the claimed nonnegative density. Expanding \(\arctan(\sinh t)\) and \(\log\coth t\) at large \(t\) gives the limit survival asymptotic.

For \(0<t<\rho_n\), subtract densities:

\[
f_n(t)-f_\infty(t)=\frac{2\cosh t}{(n-2)\pi}
\left[2\log\coth t+n\log\cos(\pi/n)\right].
\]

The bracket is strictly decreasing from positive infinity to a negative value at \(t=\rho_n\), and its unique zero satisfies \(\tanh t=\cos^{n/2}(\pi/n)\). Past \(\rho_n\), the finite density is zero and the limiting density is positive. Thus the two densities have exactly one crossing, so the total variation distance is the maximum gap of their CDFs at this crossing. Substituting the crossing identity into \(F_n-F_\infty\) cancels all logarithmic terms and gives

\[
F_n(t_n^*)-F_\infty(t_n^*)
=\frac4{\pi(n-2)}\arctan(\sinh t_n^*)
=\frac4{\pi(n-2)}\arcsin\left(\cos^{n/2}\!\frac\pi n\right).
\]

Taylor expansion of \(\log\cos(\pi/n)\) and the inverse sine at one proves the sharp two-term total-variation expansion.

For completeness, the complete finite law also gives \(\Pr(D_n>\rho_n-h)=\frac{n\tan(\pi/n)}{(n-2)\pi}h^2+O_n(h^3)\) as \(h\downarrow0\). This follows by expanding its density at \(\rho_n\), where the logarithmic factor has a simple zero. This endpoint consistency check is not a separate novelty claim.

## Verification

The standalone deterministic script `checks/regular_ideal_clearance.py` reproduces 810 successful numerical checks using Python 3 and SciPy. It computes the inner-area integral independently in hyperbolic polar coordinates, compares the exact CDF at five thresholds each for seven side counts, integrates the density for normalization, independently integrates the signed-density variation to test the total-variation identity, checks CDF ordering for consecutive side counts, and tests endpoint and asymptotic coefficients. Run `python checks/regular_ideal_clearance.py` after extracting the files. These finite numerical checks support the calculations but do not replace the geometric and analytic proof above.

## Relationship to prior work

The ideal-polygon area, right-ideal-triangle inradius and hypercycle Fermi metric are classical. Gallego and Solanes (2001) study hyperbolic convex-set perimeter, diameter and area asymptotics; their hypotheses and conclusions do not supply the probability law in this theorem. Xu (2014) studies the Liouville-geodesic *chord-length* distribution in ideal polygons, a different sampling measure and statistic. Parlier (2025) establishes the regular ideal polygon's maximal inradius and studies orthogeodesic decompositions and Voronoi structure, but does not calculate the area-uniform clearance CDF or its side-count limit.

The published record *The logarithmic boundary-distance law and a renormalized shape invariant for ideal hyperbolic polygons* (2026; see reference) proves a universal small-clearance expansion for fixed ideal polygons and the complete CDF for ideal triangles. Those parts are credited and not proposed as new. Its explicitly delimited global CDF covers the ideal triangle only, not regular polygons of every side count, and its fixed-polygon local expansion does not imply the global stochastic comparison or the exact total-variation convergence formula. This is the closest identified direct overlap. Other located works on cusp-pair distance tails, ideal-polyhedron tube coefficients and centered radial distances concern different statistics. A possible overlooked general equidistant-inner-area theorem remains a historical-priority risk; no claim of exhaustive novelty is made.

## Limitations

The family is strictly regular, with ideal vertices and curvature exactly \(-1\), and the law uses the nearest *side* of the polygon under area sampling. The theorem does not give a full distribution for arbitrary nonregular ideal polygons, random geodesic chords, or a simultaneous uniform expansion for variable \(n\) and \(t\). Source comparisons and numerical tests do not constitute independent validation or an exhaustive priority search. In particular, the small-clearance asymptotics and the triangle case are prior results rather than new components.

## References

- Eduardo Gallego and Gil Solanes, *Perimeter, Diameter and Area of Convex Sets in the Hyperbolic Plane*, Journal of the London Mathematical Society **64** (2001), 161–178, first published 2001-08-01. DOI: `10.1112/S002461070100223X`; author-hosted full text: `https://mat.uab.cat/~egallego/papers/Diperen3%20.pdf`.
- Binbin Xu, *On the Ambartzumian-Pleijel identity in hyperbolic geometry*, arXiv:1410.4052, first posted 2014-10-15, full text: `https://arxiv.org/html/1410.4052v1`.
- Hugo Parlier, *Near ideal decompositions of ideal polygons*, 2025, full text: `https://homeweb.unifr.ch/parlierh/pub/Papers/Ideal2025-10-29.pdf`.
- *The logarithmic boundary-distance law and a renormalized shape invariant for ideal hyperbolic polygons*, publicly available 2026-11-08, `https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-logarithmic-boundary-distance-law-and-a-renormalized-shape-i--1d7379fbdbb6`.

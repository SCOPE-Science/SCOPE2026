# A square-root rare-cell law and a conditional area-shape limit for three random great circles

## Finding

Let three independent Haar-uniform unoriented great circles cut the unit sphere into eight cells. Let \(M\) be their smallest spherical area, in steradians, and define

\[
J=\int_{\substack{q_1,q_2>0\\q_1+q_2<1}}
\sqrt{\sin(\pi q_1)\sin(\pi q_2)\sin(\pi(1-q_1-q_2))}\,dq_1\,dq_2.
\]

Then \(J=0.218175921304\ldots\) and the exact first-order small-cell law is

\[
\Pr(M<x)=\sqrt{2}\,\pi J\sqrt{x}+o(\sqrt{x})
=0.96933007828\ldots\sqrt{x}+o(\sqrt{x})
\quad (x\downarrow0).
\]

For the accompanying conditional limit, choose independent uniform unit normals for the three great circles, and label four antipodal pairs by the sign patterns \((+++),(++-),(+-+),(-++)\). Let \(p_i\) denote each pair's cell area divided by \(2\pi\), and \(I\) the unique index of the smallest \(p_i\) (ties have probability zero). Conditional on \(\min_i p_i<\varepsilon\), as \(\varepsilon\downarrow0\), the index \(I\) is uniform over four labels; the normalized minimum \(\min_i p_i/\varepsilon\) has limiting cumulative distribution \(\sqrt{s}\) for \(0\leq s\leq1\); and, independently, the remaining three \(p\)-coordinates, taken in their fixed relative order, converge to the probability measure on \(q_1,q_2,q_3>0\), \(q_1+q_2+q_3=1\), with density

\[
\frac1J\sqrt{\sin(\pi q_1)\sin(\pi q_2)\sin(\pi q_3)}
\]

in coordinates \((q_1,q_2)\). Thus an unusually small cell comes with an explicit nonuniform distribution of the other three macroscopic cell areas, rather than just a marginal tail exponent.

## Assumptions and scope

The sphere has unit radius. Each circle is the intersection with a plane through the origin having an independently Haar-uniform normal. The orientation of the selected normal does not change the unoriented circle. All cells are measured by the usual area on the unit sphere; the generic event that no three circles concur has probability one. Each of the eight cells is a spherical triangle; antipodal cells have equal areas, so four positive proportions sum to one. The probability law applies only to exactly three independent isotropic great circles. The limit is taken with fixed sphere and fixed number of circles.

## Proof

**1. Four-cell parametrization.** Let \(\alpha,\beta,\gamma\in(0,\pi)\) be the pairwise angular distances among the three oriented normals, in the order \((1,2),(1,3),(2,3)\). Girard's formula applied to the eight sign cones gives four antipodally paired areas

\[
2\pi p_0=2\pi-\alpha-\beta-\gamma,\quad
2\pi p_1=\beta+\gamma-\alpha,\quad
2\pi p_2=\alpha+\gamma-\beta,\quad
2\pi p_3=\alpha+\beta-\gamma.
\]

The inequalities defining a nondegenerate three-normal Gram matrix ensure all four are positive, with \(\sum_{i=0}^3p_i=1\). Conversely \(\alpha=\pi(p_2+p_3)\), \(\beta=\pi(p_1+p_3)\), \(\gamma=\pi(p_1+p_2)\). This affine map has absolute Jacobian \(2\pi^3\).

**2. Known angular density, transformed.** Fix the first normal. The second and third polar angles \(\alpha,\beta\) independently have densities \(\sin\alpha/2,\sin\beta/2\), while their relative azimuth is uniform on \([0,2\pi)\). Differentiating the spherical cosine rule yields the joint density

\[
f(\alpha,\beta,\gamma)=\frac{\sin\alpha\sin\beta\sin\gamma}{4\pi\sqrt{G}},\qquad
G=1+2\cos\alpha\cos\beta\cos\gamma
-\cos^2\alpha-\cos^2\beta-\cos^2\gamma.
\]

The spherical Heron identity \(G=4\sin(\pi p_0)\sin(\pi p_1)\sin(\pi p_2)\sin(\pi p_3)\) gives the joint probability density for \((p_1,p_2,p_3)\), with \(p_0=1-p_1-p_2-p_3\):

\[
g(p)=\frac{\pi^2}{4}\,
\frac{\sin(\pi(p_1+p_2))\sin(\pi(p_1+p_3))\sin(\pi(p_2+p_3))}{\sqrt{\prod_{i=0}^3\sin(\pi p_i)}}
\quad(p_i>0,\ \textstyle\sum p_i=1).
\]

This is a change of variables from the classical three-side/three-angle joint law, *not* itself asserted as a new probability law. The density is symmetric under permuting the four \(p_i\), as follows by the sine complement identity and by independent sign reversals of the normals.

**3. Singular face localization.** Put \(p_0=u\) and \(p_j=(1-u)q_j\) for \(j=1,2,3\), \(q_j>0\), \(\sum q_j=1\). As \(u\downarrow0\), pointwise for positive \(q\),

\[
\sqrt{u}\,g(u,(1-u)q_1,(1-u)q_2,(1-u)q_3)
\longrightarrow\frac{\pi^{3/2}}4\sqrt{\prod_{j=1}^3\sin(\pi q_j)}.
\]

The coordinate Jacobian in \((q_1,q_2)\) is \((1-u)^2\). For \(u\) in a fixed sufficiently small interval, the sine bounds \(c z(1-z)\le\sin(\pi z)\le C\) yield a common integrable majorant of the form \(C'\prod_{j=1}^3[q_j(1-q_j)]^{-1/2}\) for \(\sqrt u\,g\,(1-u)^2\). At simplex corners its worst growth is \(O((a+b)^{-1/2}a^{-1/2}b^{-1/2})\), integrable in \((a,b)\). Dominated convergence therefore yields

\[
\Pr(p_0<\varepsilon)=\frac{\pi^{3/2}}2J\sqrt\varepsilon+o(\sqrt\varepsilon).
\]

It also yields the conditional limit for the normalized remaining three coordinates and the relative minimum, since \(\int_0^{s\varepsilon}u^{-1/2}du/\int_0^\varepsilon u^{-1/2}du=\sqrt s\). The joint product limit makes these two conditional marks independent.

**4. Exclusion of simultaneous rare cells.** For example, if \(p_0=u\) and \(p_1=v\) are both at most \(\varepsilon\), the sine factor associated with \(p_2+p_3=1-u-v\) is at most \(\pi(u+v)\). The two other sine numerators are bounded by one. Integrating over the remaining free proportion and using the endpoint estimate

\[
\int_0^{1-u-v}\frac{dy}{\sqrt{\sin(\pi y)\sin(\pi(1-u-v-y))}}
=O\bigl(1+|\log(u+v)|\bigr)
\]

shows \(\Pr(p_0<\varepsilon,p_1<\varepsilon)=O(\varepsilon^2\log(1/\varepsilon))=o(\sqrt\varepsilon)\). The same estimate holds for any pair by exchangeability, so inclusion–exclusion gives

\[
\Pr(\min_i p_i<\varepsilon)=2\pi^{3/2}J\sqrt\varepsilon+o(\sqrt\varepsilon).
\]

Finally \(M=2\pi\min_i p_i\), giving the claimed coefficient \(\sqrt2\pi J\). Exchangeability and negligible double rare events give uniform asymptotic index. The conditional three-area law follows from step 3.

## Verification

The accompanying `verify_three_circle.py` is standalone Python using only its standard library. Run `python3 verify_three_circle.py` to (i) reconstruct 1,200 spherical cell areas independently from actual cone-vertex intersections and compare them with the angular formula, (ii) evaluate two deterministic midpoint approximations to \(J\), and (iii) compare 140,000 seeded random arrangements' rare-event frequency against the asymptotic prediction. Higher-accuracy adaptive quadrature gives \(J\approx0.2181759213044\). Finite tests and numerical integration corroborate rather than establish the theorem; the infinite-parameter statement follows from the preceding density, domination, and overlap arguments.

## Relationship to prior work

The trivariate distribution of the sides and angles of a random spherical triangle and the dual-triangle interpretation predate this finding; see Finch–Jones and the older references they cite. In particular the displayed full joint density can be obtained from those known formulas and is a proof tool, not a novelty claim. Kabluchko (2026) studies distributional geometry of random polyhedral cones, including their solid-angle moments and duality; Hug–Thäle (2026) study edge lengths and incidences in random spherical tessellations. The contribution claimed here is restricted to the **minimum across four dependent antipodal pairs**, its sharp \(1/2\)-exponent and integral coefficient, and the simultaneously conditioned three-area limit. The known angular law is stronger as a raw joint-distribution description, but identifying its singular face geometry and negligible joint-rare intersections requires the explicit asymptotic calculation above.

## Limitations

No claim is made for arbitrary numbers of circles, anisotropic circle distributions, higher-dimensional spheres, or full small-cell finite-threshold distribution. The constant is expressed by an exact, absolutely convergent integral rather than an elementary closed form. The historical-priority assessment is provisional: older stochastic-geometry papers may contain related boundary asymptotics not found in the inspected literature. Only self-review has been performed; independent mathematical audit has not been performed.

## References

- Z. Kabluchko, *Random Polyhedral Cones: Distributional Results via Gale Duality*, arXiv:2602.08581, first submitted 2026-02-09. https://arxiv.org/abs/2602.08581
- D. Hug and C. Thäle, *Lengths and incidences in Poisson hypersphere and spherical splitting tessellations*, arXiv:2609.07725, first submitted 2026-09-07. https://arxiv.org/abs/2609.07725
- S. R. Finch and A. J. Jones, *Random Spherical Triangles*, arXiv:1009.5329, first submitted 2010-09-27. https://arxiv.org/html/1009.5329v3

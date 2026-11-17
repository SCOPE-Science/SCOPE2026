# Spatial crossing-point law for independent geodesics in a hemisphere

## Finding

Let \(H=\{x\in S^2:x_3\geq0\}\) be the unit northern hemisphere, with spherical-area-uniform probability sampling. Choose four independent points \(X_1,X_2,X_3,X_4\in H\), and join \(X_1\) to \(X_2\) and \(X_3\) to \(X_4\) by their shortest spherical geodesic arcs. Almost surely the arcs either do not meet or intersect transversely in precisely one point \(Z\in H^\circ\). Let \(E\) be the crossing event. On \(E\) take the gnomonic coordinate
\[
W=(Z_1/Z_3,Z_2/Z_3)\in\mathbb R^2,\qquad r=\|W\|.
\]
The **unconditional crossing-location subprobability measure** \(\Pr(E,W\in dw)\) has the explicit density
\[
\boxed{h(w)=\frac{2}{\pi^3}\frac{\log(1+\|w\|^2)}{\|w\|^2(1+\|w\|^2)^{3/2}},\quad h(0)=\frac2{\pi^3}.}
\]
In spherical-area coordinates the subprobability density is
\[
\boxed{g(z)=\frac{2}{\pi^3}\frac{\log(1+r^2)}{r^2},\quad r=\frac{\sqrt{z_1^2+z_2^2}}{z_3}.}
\]
It is strictly decreasing from the north pole toward the equator, and tends to zero at the equator. For every \(R\ge0\), the exact joint probability that the arcs cross and their gnomonic crossing lies in the radius-\(R\) disk is
\[
\Pr(E,\|W\|\le R)=\frac4{\pi^2}\int_0^R\frac{\log(1+t^2)}{t(1+t^2)^{3/2}}\,dt.
\]
In particular, \(\Pr(E)=1-8/\pi^2\). This **scalar crossing probability is previously implied by the known four-point halfsphere hull law and is not claimed as new**; the contribution asserted here is the evaluated spatial crossing-point law. The conditional density of \(W\), given \(E\), is \(h(w)/(1-8/\pi^2)\). For \(m\ge2\) independent random arcs drawn as above, their crossing-point count measure has expected intensity \(\binom m2h(w)\,dw\).

## Assumptions and scope

All four endpoints are independent and each has normalized two-dimensional spherical area on the fixed closed hemisphere (not uniform spherical azimuth/latitude, or random infinite great circles). Arcs are the unique shorter intrinsic great-circle arcs except at probability-zero antipodal pairs. The crossing is a transversal interior intersection; endpoints, coincident great circles, and tangencies have probability zero. The gnomonic coordinate is defined when the height is positive; crossings on the equator have probability zero. The planar and spherical densities are **subprobability** densities, not probability densities until divided by \(\Pr(E)\). The multi-arc intensity is for finite \(m\), with no claim that different crossings are independent.

## Proof

**1. Planar reduction and endpoint density.** The gnomonic map \(\Psi(x)=(x_1/x_3,x_2/x_3)\) maps \(H^\circ\) bijectively to \(\mathbb R^2\), mapping each minimizing geodesic between its points to the Euclidean segment between their images. Since the spherical-area element is \((1+\|u\|^2)^{-3/2}du\) and the hemisphere area is \(2\pi\), each planar endpoint independently has density
\[
f(u)=\frac{1}{2\pi(1+\|u\|^2)^{3/2}}.
\]
Hence it suffices to determine the intersection-location law for two independent segments with independent endpoints drawn from this planar density.

**2. Directional crossing flux.** Fix an intersection candidate \(w\in\mathbb R^2\) and let \(e_\alpha=(\cos\alpha,\sin\alpha)\) with \(0\le\alpha<\pi\). Opposite-side endpoint representations of a segment through \(w\) are \(w+u e_\alpha\) and \(w-v e_\alpha\), with \(u,v>0\). Define the one-orientation flux
\[
J(w,\alpha)=\int_0^\infty\!\int_0^\infty (u+v)f(w+ue_\alpha)f(w-ve_\alpha)\,du\,dv.
\]
Let \(s=\sqrt{1+\|w\|^2}\), \(a=w\cdot e_\alpha\), \(c=s^2-a^2\). Direct integration gives
\[
\begin{aligned}
\int_0^\infty(1+\|w+ue_\alpha\|^2)^{-3/2}du&=(1-a/s)/c,\\
\int_0^\infty u(1+\|w+ue_\alpha\|^2)^{-3/2}du&=(s-a)/c,
\end{aligned}
\]
with their minus-direction counterparts obtained by changing the sign of \(a\). Consequently,
\[
J(w,\alpha)=\frac{1}{2\pi^2sc}.
\]
The factor \(u+v\) is the Jacobian from ordered endpoint pairs to the line's transverse offset and the two along-line coordinates. The ordering of the endpoints adds a factor two to each segment's unoriented line flux; since two transverse lines at angles \(\alpha,\beta\) have offset-to-intersection-point Jacobian \(\lvert\sin(\alpha-\beta)\rvert\), the coarea/change-of-variables formula gives
\[
h(w)=4\int_0^\pi\!\int_0^\pi |\sin(\alpha-\beta)|J(w,\alpha)J(w,\beta)\,d\alpha\,d\beta.
\]
All integrands are nonnegative, and the measure-zero cases of parallel lines or degeneracies do not affect this formula.

**3. Evaluation of the angular integral.** By rotating planar coordinates assume \(w=(r,0)\). Then \(c=1+r^2\sin^2\alpha\), and the preceding integral becomes
\[
h(w)=\frac{I(r)}{\pi^4s^2},\quad
I(r)=\int_0^\pi\!\int_0^\pi
\frac{|\sin(\alpha-\beta)|\,d\alpha\,d\beta}
{(1+r^2\sin^2\alpha)(1+r^2\sin^2\beta)}.
\]
Set \(q=(s-1)/(s+1)\in[0,1)\). The uniformly convergent Fourier series for each finite \(r\) are
\[
\frac{1}{1+r^2\sin^2\alpha}=\frac1s\Big(1+2\sum_{n\ge1}q^n\cos(2n\alpha)\Big),\qquad
|\sin t|=\frac2\pi-\frac4\pi\sum_{n\ge1}\frac{\cos(2nt)}{4n^2-1}.
\]
Orthogonality on \([0,\pi]\) gives
\[
I(r)=\frac{2\pi}{s^2}\left(1-2\sum_{n\ge1}\frac{q^{2n}}{4n^2-1}\right).
\]
The elementary series identity
\[
1-2\sum_{n\ge1}\frac{q^{2n}}{4n^2-1}
=(q^{-1}-q)\operatorname{arctanh}q
=\frac{2s\log s}{r^2}
\]
holds for \(0<q<1\) (expand \(\operatorname{arctanh}q=\sum_{k\ge0}q^{2k+1}/(2k+1)\) and collect coefficients), with continuous limits at zero. Therefore \(I(r)=4\pi\log s/(r^2s)\), proving the boxed planar density. Its north-pole limit follows from \(\log(1+r^2)\sim r^2\).

**4. Spherical density, monotonicity, normalization.** The inverse gnomonic map has spherical Jacobian \((1+r^2)^{-3/2}\), so \(g(z)=h(w)(1+r^2)^{3/2}\). The function \(x\mapsto\log(1+x)/x\) strictly decreases for \(x>0\), proving the spherical radial monotonicity. Polar integration yields the stated disk formula. With \(v=(1+t^2)^{-1/2}\), its integral over \(R=\infty\) evaluates as
\[
\Pr(E)=\frac8{\pi^2}\int_0^1 \frac{-v^2\log v}{1-v^2}\,dv
=\frac8{\pi^2}\sum_{n\ge0}\frac1{(2n+3)^2}
=1-\frac8{\pi^2}.
\]
The series converges absolutely; its last equality uses the classical sum over positive odd reciprocal squares. This also validates the total subprobability mass without relying on previous work. The conditional and finite-arc expected intensity formulas follow by normalization and linearity of expectation.

## Verification

The accompanying `check_crossing_density.py` independently evaluates the pre-Fourier double angular integral by numerical quadrature, checks the normalized radial integral, and simulates 600,000 independent four-endpoint configurations. It verifies radius-truncated crossing masses at \(R=0.25,0.5,1,2,4\), and the total crossing probability, against their exact expressions within predeclared five-standard-error sampling tolerances. From the package directory execute `python check_crossing_density.py` with NumPy and SciPy installed. The reproducible checker prints `HEMISPHERE_GEODESIC_CROSSING_LOCATION_LAW_OK` upon success. Such finite tests corroborate but do not prove the continuum statements, which follow from the displayed change-of-variables and Fourier calculations.

## Relationship to prior work

Bárány, Hug, Reitzner and Schneider, *Random points in halfspheres*, arXiv:1505.04672v1 (18 May 2015), analyze random hemispherical convex hulls. Their four-point hull probabilities already imply the **unmarked crossing probability** \(1-8/\pi^2\); that scalar number is not a novelty claim here. A more recent exact disk/Cauchy factorization for the midpoint of one hemispherical geodesic (`published-finding corpus`, identifier below) computes an important one-arc distribution, but does not state the two-arc intersection-location pushforward. The present calculation must combine *two* independent directional endpoint fluxes with a transverse-crossing Jacobian and evaluate their angular convolution. Manrique-Mirón studies intersection angles for four uniform **planar disk** endpoints, not the spatial intersection intensity for hemispherical geodesic arcs. Böttcher studies straight segment overlap models with different sampling. The strongest live overlap risk is a potentially equivalent older stochastic-geometric crossing density under gnomonic/Cauchy terminology; absence of a search match does not prove absolute priority.

## Limitations

Only independent endpoint-uniform shorter geodesics on the unit hemisphere are covered. The density is not asserted for uniformly sampled infinite great circles, other spherical caps, other endpoint distributions, or an unconditioned full sphere. No claim is made of independence of distinct crossing locations in larger samples. The scalar crossing probability is already implied by known convex-hull results. Absolute historical uniqueness has not been independently established; older stochastic integral-geometry papers could encode an equivalent local crossing intensity. No independent mathematical audit has been performed.

## References

1. I. Bárány, D. Hug, M. Reitzner, R. Schneider, *Random points in halfspheres*, arXiv:1505.04672v1, publicly posted 18 May 2015. https://arxiv.org/abs/1505.04672 ; open text https://arxiv.org/html/1505.04672.
2. *Uniform-disk law and Cauchy disintegration for hemispherical geodesic midpoints*, published published-finding corpus mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-uniform-disk-law-and-cauchy-disintegration-for-hemispherical-geo--4acbe55d8e4e .
3. P. Manrique-Mirón, *Angle between two random segments*, arXiv:2309.03032. https://arxiv.org/abs/2309.03032 .
4. L. Böttcher, *A Random-Line-Graph Approach to Overlapping Line Segments*, arXiv:1911.10679. https://arxiv.org/abs/1911.10679 .

# Sharp near-diameter chord tails and a unique shape optimum for ring-torus surfaces

## Finding

Let \(R>r>0\), and let \(X,Y\) be independent points uniformly distributed by surface area on the standard embedded ring-torus surface
\[
\mathcal T(R,r)=\{((R+r\cos v)\cos u,(R+r\cos v)\sin u,r\sin v):u,v\in[0,2\pi)\}.
\]
For their ambient **Euclidean chord** distance \(D=\|X-Y\|_2\), the maximal possible value is \(d_*=2(R+r)\). As \(\varepsilon\downarrow0\) with \(R,r\) fixed,
\[
\boxed{\Pr(D>d_*-\varepsilon)=\frac{2(R+r)^2}{3\pi^2rR^{5/2}}\,\varepsilon^{3/2}+O_{R,r}(\varepsilon^{5/2}).}
\]
For prescribed diameter \(d_*\), put \(k=R/r>1\). The **dimensionless coefficient** in \(\Pr(D>d_*(1-\eta))\sim H(k)\eta^{3/2}\) is
\[
H(k)=\frac{2^{5/2}(k+1)^{7/2}}{3\pi^2k^{5/2}}.
\]
It has a **unique global minimum** among all embedded ring tori, attained exactly when \(R/r=5/2\):
\[
\boxed{H(k)\ge H(5/2)=\frac{2\sqrt2\,7^{7/2}}{3\pi^2 5^{5/2}}\approx1.5507511882,}
\]
with equality only at \(k=5/2\). It decreases strictly on \((1,5/2)\), increases strictly on \((5/2,\infty)\), approaches \(64/(3\pi^2)\) at the excluded horn-torus boundary \(k\downarrow1\), and diverges as \(k\to\infty\). In particular, every dimensionless coefficient strictly between the minimum and \(64/(3\pi^2)\) is realized by exactly **two noncongruent** embedded ring-torus shapes of equal diameter.

A conditional limiting law accompanies the tail: if \(u_1,u_2,v_1,v_2\) are the two points' angular coordinates and \(\theta=u_2-u_1-\pi\in(-\pi,\pi]\), put \(s=(v_1+v_2)/\sqrt2\), \(t=(v_1-v_2)/\sqrt2\). Conditional on \(D>d_*-\varepsilon\), the vector
\[
\left(\frac{\sqrt{2r(R+r)}\,s}{\sqrt{4(R+r)\varepsilon}},\frac{\sqrt{2rR}\,t}{\sqrt{4(R+r)\varepsilon}},\frac{(R+r)\theta}{\sqrt{4(R+r)\varepsilon}}\right)
\]
converges in distribution to **uniform volume measure on the unit ball in \(\mathbb R^3\)**. The initial longitude \(u_1\) is, even before conditioning, uniform and independent of these relative coordinates.

## Assumptions and scope

The torus is the two-dimensional **surface**, not a solid torus, with \(R>r>0\), so no spindle or horn self-contact occurs. Surface area is normalized to a probability measure, and the two observations are independent. The sampling law in the angular parameterization is \(u\sim\operatorname{Unif}[0,2\pi)\) and \(v\) has density \((R+r\cos v)/(2\pi R)\), independently. In particular, equal-uniform meridian angles do not model surface-area sampling. All distances are ambient Euclidean, not intrinsic geodesic distances. The \(O_{R,r}\) remainder is for each fixed nondegenerate ring torus and makes no uniform assertion as \(r/R\to0\) or \(r/R\to1\). Limits of strict inequalities are unaffected by events of measure zero.

## Proof

**Diameter and maximizing manifold.** Every torus point satisfies \(\|X\|\le R+r=:A\), with equality only on the outer equator \(v=0\). The triangle inequality gives \(D\le2A\). Equality requires both points on the outer equator, at opposite longitudes. Thus the full ordered maximizing locus is the single compact circle \(v_1=v_2=0\), \(u_2=u_1+\pi\pmod{2\pi}\). Away from any fixed neighborhood of this circle, compactness gives a strict positive diameter deficit.

**Exact deficit and nondegenerate normal form.** Write \(\alpha=v_1\), \(\beta=v_2\), \(u_2-u_1=\pi+\theta\) in a neighborhood of that circle; \(\rho_1=R+r\cos\alpha\), \(\rho_2=R+r\cos\beta\). Directly from the parameterization,
\[
D^2=\rho_1^2+\rho_2^2+2\rho_1\rho_2\cos\theta+r^2(\sin\alpha-\sin\beta)^2.
\]
Put \(s=(\alpha+\beta)/\sqrt2\), \(t=(\alpha-\beta)/\sqrt2\), an orthogonal transformation with unit absolute Jacobian. Taylor expansion at the maximizing circle yields
\[
4A^2-D^2=2rA\,s^2+2rR\,t^2+A^2\theta^2+O_{R,r}((|s|+|t|+|\theta|)^4).
\]
The quadratic form is positive definite, since \(R,r>0\). The fourth-order remainder (rather than cubic) follows from the exact invariance under simultaneous sign reversal \((\alpha,\beta,\theta)\mapsto(-\alpha,-\beta,-\theta)\). The exact deficit inequality \(D>2A-\varepsilon\) is equivalently \(4A^2-D^2<4A\varepsilon-\varepsilon^2\). Its normal-coordinate region is therefore contained in, and contains, uniformly small \(O(\varepsilon)\) relative perturbations of the ellipsoid
\[
2rA\,s^2+2rR\,t^2+A^2\theta^2<4A\varepsilon.
\]
That ellipsoid has Euclidean \((s,t,\theta)\) volume
\[
\frac{4\pi}{3}\frac{(4A\varepsilon)^{3/2}}{\sqrt{2rA}\sqrt{2rR}\,A}=\frac{16\pi}{3r\sqrt R}\varepsilon^{3/2}.
\]

**Sampling density and the exact constant.** Integrating out \(u_1\), the joint density in \((\alpha,\beta,\theta)\) is
\[
\frac{(R+r\cos\alpha)(R+r\cos\beta)}{8\pi^3R^2}
=\frac{A^2}{8\pi^3R^2}\bigl(1+O_{R,r}(\alpha^2+\beta^2)\bigr).
\]
Multiplying the leading density by the ellipsoid volume yields
\[
\frac{A^2}{8\pi^3R^2}\frac{16\pi}{3r\sqrt R}\varepsilon^{3/2}
=\frac{2A^2}{3\pi^2rR^{5/2}}\varepsilon^{3/2}.
\]
The quartic geometric error moves each rescaled ellipsoid boundary by \(O_{R,r}(\varepsilon)\), and the density differs relatively by \(O_{R,r}(\varepsilon)\) there. Both errors contribute \(O_{R,r}(\varepsilon^{5/2})\) to probability. Compactness excludes other contributions. Rescaling the three positive quadratic directions produces the unit-ball law by dominated convergence, and the common longitude remains Haar-uniform by rotational invariance.

**Shape optimum and multiplicity.** Setting \(\varepsilon=2A\eta\) and \(k=R/r\), the dimensionless leading coefficient is
\[
H(k)=\frac{2^{5/2}}{3\pi^2}\frac{(1+k)^{7/2}}{k^{5/2}},\qquad
\frac{d}{dk}\log H(k)=\frac{2k-5}{2k(k+1)}.
\]
It follows that \(k=5/2\) is the only stationary point and unique global minimum. Evaluating the limits at \(1\) and \(\infty\) gives the sharp stated range and the exact two-shape ambiguity below the excluded horn endpoint. Scale is uniquely reconstructed from the prescribed diameter by \(r=d_*/[2(k+1)]\), \(R=kr\); different \(k\) are therefore noncongruent. This proves every assertion.

## Verification

The accompanying `verify_torus_tail.py` uses only the Python standard library. It independently integrates the exact conditional longitude-angle probability over the two meridian parameters using a two-dimensional low-discrepancy quadrature and **the correct area density**. For radii \((R,r)=(1.2,1),(2,1),(4,1)\) and \(\varepsilon=0.02,0.005\), the numerical quotient of exact tail probability to the predicted leading term is within \(0.025\) of one. It also checks the unique coefficient minimum at sample shapes and the closed minimum expression. Run `python3 verify_torus_tail.py` alongside this document; the observed successful marker was `VERIFY_TORUS_DIAMETER_TAIL_OK 20`. These finite checks do not establish the theorem, which rests on the analytical localization and Taylor estimates above.

## Relationship to prior work

Tu and Fischbach's 2002 random-distance work develops the distance-distribution problem for spherical objects and radial densities, primarily volume sampling. Sidiropoulos's 2014 work gives exact chords and their distributions for hypersphere **surfaces**, without a toroidal shape parameter. Bäsel's 2012 work treats polygon chord and interior-point distances. The previously published *Sharp two-moment ambiguity and three-moment reconstruction of ring-torus surfaces* uses **the identical embedded surface and sampling measure**, but its inspected full text concerns the second/fourth/sixth distance moments and their inversion, not a near-diameter tail, the coefficient's extremal aspect ratio, or the conditional near-maximal endpoint law. These forward-moment results do not imply the present extreme-tail coefficient, since finite moments do not determine local tail behavior. Related intrinsic-torus diameter-tail results use a **different distance** and geometry. No checked source establishes the asserted exact Euclidean tail and shape optimum; an older unindexed equivalent remains possible.

## Limitations

The asymptotics and conditional limit hold only for a **fixed embedded ring torus** with \(0<r<R\) and a specified surface-area sampling law. No claim is made for the solid-torus volume distribution, geodesic distance, general toroidal embeddings, or uniform asymptotics in degenerating parameter regimes. The leading tail coefficient is **not** a globally injective aspect-ratio statistic: it has the proved two-shape ambiguity over an explicit interval. The statement of historical priority is provisional and does not constitute independent validation or an exhaustive literature theorem.

## References

1. S.-J. Tu and E. Fischbach, *Random Distance Distribution for Spherical Objects: General Theory and Applications to n-Dimensional Physics*, arXiv:math-ph/0201046v1, first public preprint 2002-01-22. https://arxiv.org/html/math-ph/0201046v1
2. P. Sidiropoulos, *N-sphere chord length distribution*, arXiv:1411.5639v1, first public preprint 2014-11-20. https://arxiv.org/html/1411.5639v1
3. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first public preprint 2012-04-12. https://arxiv.org/abs/1204.2707
4. *Sharp two-moment ambiguity and three-moment reconstruction of ring-torus surfaces*, published mathematical record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-two-moment-ambiguity-and-three-moment-reconstruction-of-ri--99081f2abf19
5. *A singular diameter-tail boundary layer for sheared flat two-tori*, published mathematical record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-singular-diameter-tail-boundary-layer-for-sheared-flat-two-tor--56adedbed03c

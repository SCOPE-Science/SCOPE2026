# The diameter-tail coefficient recovers the cone angle of spherical footballs

## Finding
Let \(0<\alpha<1\). On the spherical football \(F_\alpha\), obtained by doubling a spherical lune of angle \(\pi\alpha\), take independent normalized-area-uniform points \(X,Y\). This compact surface has curvature \(+1\) away from two cone points, both of total angle \(2\pi\alpha\), at distance \(\pi\). Let \(D=d_{F_\alpha}(X,Y)\) be intrinsic geodesic distance. Then

\[
\lim_{\varepsilon\downarrow0}\frac{\Pr\{D>\pi-\varepsilon\}}{\varepsilon^4}
=C(\alpha)
=\frac1{32}\left[\csc^2(\pi\alpha)-\frac{\cot(\pi\alpha)}{\pi\alpha}\right].
\]

The map \(C:(0,1)\to(1/48,\infty)\) is a continuous **strictly increasing bijection**. Thus the coefficient of the extreme-distance tail uniquely recovers the cone angle, among *all* spherical footballs with angle smaller than \(2\pi\). At the smooth endpoint \(\alpha=1\), by contrast, \(F_1\) is the ordinary round sphere and \(\Pr\{D>\pi-\varepsilon\}\sim\varepsilon^2/4\); the exponent changes from four to two.

For the cyclic spherical quotient \(F_{1/m}=S^2/C_m\), with integer \(m\ge2\), the exact coefficient is
\[
C(1/m)=\frac1{32}\left[\csc^2(\pi/m)-\frac{m}{\pi}\cot(\pi/m)\right],
\]
strictly decreasing with \(m\), equal to \(1/32\) at \(m=2\), and converging to \(1/48\) as \(m\to\infty\).

## Assumptions and scope
The metric is normalized to Gaussian curvature \(+1\) at regular points. The coordinate realization is
\[
F_\alpha=([0,\pi]\times\mathbb R/(2\pi\alpha\mathbb Z),\quad
 ds^2=d\theta^2+\sin^2\theta\,d\varphi^2),
\]
with each endpoint circle contracted to one cone point. The total area is \(4\pi\alpha\). Each uniform point has colatitude density \(\tfrac12\sin\theta\) and longitude uniform modulo \(2\pi\alpha\). The distance is the intrinsic length metric, **not** the ambient Euclidean chord distance or the great-circle distance on a hypothetical nonsingular covering sphere. Both points are sampled independently; \(\varepsilon\downarrow0\) at fixed \(\alpha\in(0,1)\). The result does not assert a uniform remainder as \(\alpha\uparrow1\).

## Proof
**1. Distance and diameter locus.** For colatitudes \(\theta_1,\theta_2\) and the least absolute longitude difference \(0\le\delta\le\pi\alpha<\pi\), the intrinsic distance obeys the spherical cosine rule
\[
\cos D=\cos\theta_1\cos\theta_2+\sin\theta_1\sin\theta_2\cos\delta.
\]
Indeed, the lune bounded by these two meridians has opening \(\delta<\pi\) and is geodesically convex in the unit sphere; its short great-circle arc gives a permissible path. A shorter minimizing regular geodesic cannot use an alternative longitude lift: such a spherical arc of length below \(\pi\) has an angular variation of at most \(\pi\), and among lifts of that size \(\delta\) is minimal. A path through a pole is no shorter than the spherical geodesic joining the developed endpoints. The same formula follows directly from the standard quotient or spherical-lune construction. Since
\[
1+\cos D=1+\cos(\theta_1+\theta_2)
 +(1+\cos\delta)\sin\theta_1\sin\theta_2,
\]
and \(1+\cos\delta>0\), equality \(D=\pi\) occurs only at the two ordered opposite-pole pairs. Compactness then confines \(D>\pi-\varepsilon\), for small enough \(\varepsilon\), to neighborhoods of these two pairs.

**2. Uniform quadratic blow-up.** Near one ordered pair write \(\theta_1=s\), \(\theta_2=\pi-t\), with \(s,t\ge0\). The angular gap \(\delta\) is uniform on \([0,a]\), where \(a=\pi\alpha\). The exact distance relation becomes
\[
\cos D=-\cos s\cos t+\sin s\sin t\cos\delta.
\]
For fixed \(a<\pi\), this quadratic form is coercive on the **positive quadrant**: \(Q_\delta(u,v)\ge\min\{1,1+\cos a\}(u^2+v^2)\), uniformly for \(0\le\delta\le a\) and \(u,v\ge0\). (No positive-definiteness claim on all of \(\mathbb R^2\) is needed.) Hence the condition \(D>\pi-\varepsilon\) forces \(s,t=O_\alpha(\varepsilon)\); for \(s=\varepsilon u\), \(t=\varepsilon v\) it converges, uniformly on bounded sets of \((u,v,\delta)\), away from the zero-area boundary, to \(Q_\delta(u,v)<1\). The two opposite-pole configurations contribute equally, while each normalized colatitude density is \(\sin s/2\). Dominated convergence gives
\[
C(\alpha)=\frac1{2a}\int_0^a I(\cos\delta)\,d\delta,
\qquad I(c)=\int_0^\infty\!\int_0^\infty
uv\,\mathbf1\{u^2+v^2+2cuv<1\}\,du\,dv.
\]
The factor \(1/2\) combines the two ordered pole pairs with the two normalized colatitude densities; there is no missing symmetry factor.

**3. Exact angular integration.** Substitute \(u=r\cos\tau\), \(v=r\sin\tau\). For \(-1<c\le1\),
\[
I(c)=\frac18\int_0^{\pi/2}\frac{\sin(2\tau)}{(1+c\sin(2\tau))^2}\,d\tau
=-\frac18\frac{d}{dc}J(c),
\qquad J(c)=\int_0^{\pi/2}\frac{d\tau}{1+c\sin(2\tau)}.
\]
Putting \(z=\tan\tau\), one finds \(J(c)=\arccos(c)/\sqrt{1-c^2}\). Therefore, for \(0<\delta<\pi\),
\[
I(\cos\delta)=\frac{\sin\delta-\delta\cos\delta}{8\sin^3\delta},
\quad I(1)=\frac1{24}.
\]
The elementary antiderivative
\[
\int_0^a\frac{\sin\delta-\delta\cos\delta}{\sin^3\delta}\,d\delta
=\frac12\left[a\csc^2a-\cot a\right]
\]
gives the stated closed coefficient.

**4. Strict inverse and endpoint.** For positive \(u,v\), the sublevel domain defining \(I(c)\) expands strictly as \(c\) decreases. Thus \(I(\cos\delta)\) is strictly increasing on \((0,\pi)\); so its average \(C(\alpha)=(2a)^{-1}\int_0^a I(\cos\delta)\,d\delta\) is strictly increasing in \(a\). Its limits are \(1/48\) as \(a\downarrow0\), and \(+\infty\) as \(a\uparrow\pi\), the latter because \(I(\cos\delta)\sim\pi/[8(\pi-\delta)^3]\). Continuity proves bijectivity. At \(\alpha=1\), rotational invariance on the round sphere gives \(\Pr(D>\pi-\varepsilon)=(1-\cos\varepsilon)/2\sim\varepsilon^2/4\). This completes the proof.

## Verification
The standalone, standard-library Python file `verify_football.py` numerically evaluates (i) the original two-variable radial integral, (ii) its one-variable analytic reduction, (iii) the closed coefficient and (iv) finite-distance probabilities obtained from the **unexpanded** spherical cosine inequality in opposite-pole coordinates. The tests use four angles, including one exceeding \(\pi\) in the doubled-lune opening, and verify convergence of the normalized probabilities as \(\varepsilon\downarrow0\). Exact proof is in the preceding steps; numerical quadrature is corroborative only.

## Relationship to prior work
Mondello and Panov, *Spherical metrics with conical singularities on a 2-sphere: angle constraints* (first publicly posted 2015-05-08, arXiv:1505.01994v1), construct and discuss the doubled spherical bigons with arbitrary cone angles (Section 3.1.1, Corollary 3.5), but study angle constraints and holonomy, not random pair-distance tails. Tu and Fischbach, *Random Distance Distribution for Spherical Objects* (arXiv:math-ph/0201046v1, 2002-01-22), derive distributions of **ambient Euclidean distances inside Euclidean balls**, not intrinsic distances on conical spherical quotients. The ordinary round-sphere pair-distance law is classical and is used explicitly as the endpoint comparison. The calculation here concerns the distinct singular metric and extracts a cone-angle-determining fourth-order diameter-tail invariant. No universal originality guarantee is claimed from searchable literature.

## Limitations
The coefficient concerns the **long-distance endpoint** at fixed cone angle, not the complete distance CDF; it does not cover super-round cone angles \(\alpha\ge1\), general conical sphere metrics with three or more singularities, or nonuniform point distributions. The limit and the smooth-sphere endpoint cannot be interchanged. Although all critical integrals are evaluated analytically, priority against older unindexed stereology or cone-surface distance literature is not independently certified.

## References
1. G. Mondello and D. Panov, *Spherical metrics with conical singularities on a 2-sphere: angle constraints*, arXiv:1505.01994v1 (first posted 2015-05-08), Section 3.1.1, Corollary 3.5. https://arxiv.org/abs/1505.01994
2. S.-J. Tu and E. Fischbach, *Random Distance Distribution for Spherical Objects: General Theory and Applications to n-Dimensional Physics*, arXiv:math-ph/0201046v1 (first posted 2002-01-22), Sections I–III. https://arxiv.org/abs/math-ph/0201046
3. J. E. Borzellino, *Pinching theorems for teardrops and footballs of revolution*, Bull. Aust. Math. Soc. (2009), https://doi.org/10.1017/S0004972709000187 (context on orbifold football geometry; the probability theorem is not attributed to this source).

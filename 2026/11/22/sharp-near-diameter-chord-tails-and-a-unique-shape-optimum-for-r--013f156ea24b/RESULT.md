# Sharp near-diameter chord tails and a unique shape optimum for ring-torus surfaces

## Finding and scope

Let \(R>r>0\), and sample \(X,Y\) independently from normalized surface area on the embedded ring torus
\[
\mathcal T(R,r)=\{((R+r\cos v)\cos u,(R+r\cos v)\sin u,r\sin v): u,v\in[0,2\pi)\}.
\]
For the ambient Euclidean chord distance \(D=\|X-Y\|_2\), put \(A=R+r\). The diameter is \(d_*=2A\), and, as \(\varepsilon\downarrow0\) for fixed \(R,r\),
\[
\Pr(D>d_*-\varepsilon)=\frac{2A^2}{3\pi^2 rR^{5/2}}\varepsilon^{3/2}+O_{R,r}(\varepsilon^{5/2}).
\]
Writing \(k=R/r\) and \(\eta=\varepsilon/d_*\), the coefficient of \(\eta^{3/2}\) is
\[
H(k)=\frac{2^{5/2}(k+1)^{7/2}}{3\pi^2 k^{5/2}}.
\]
Its unique global minimum for \(k>1\) is \(H(5/2)=2\sqrt{2}\,7^{7/2}/(3\pi^2 5^{5/2})\approx1.5507511882\). It decreases strictly from the excluded horn limit \(64/(3\pi^2)\) to its minimum and then increases strictly to infinity. Each coefficient strictly between the minimum and \(64/(3\pi^2)\) therefore corresponds to exactly two noncongruent ring tori at any prescribed diameter.

For the conditional limit, let \(\alpha,\beta\in(-\pi,\pi]\) be the **signed representatives modulo \(2\pi\)** of the two meridian angles \(v_1,v_2\), centered at the outer equator. Let \(\theta\in(-\pi,\pi]\) be the representative of \(u_2-u_1-\pi\) modulo \(2\pi\), and put \(s=(\alpha+\beta)/\sqrt{2}\), \(t=(\alpha-\beta)/\sqrt{2}\). Given \(D>d_*-\varepsilon\),
\[
\frac{1}{\sqrt{4A\varepsilon}}\bigl(\sqrt{2rA}\,s,\sqrt{2rR}\,t,A\theta\bigr)
\ \Longrightarrow\ \operatorname{Unif}(\{w\in\mathbb R^3:|w|\le1\}),
\]
where the limit is normalized volume. The initial longitude \(u_1\) is uniform and independent of \((\alpha,\beta,\theta)\), both before and after conditioning.

This is a result for a smooth ring-torus surface and Euclidean distance, not for the volume law in a solid torus or intrinsic distance. The error estimate makes no claim of uniformity in degenerating aspect ratios.

## Proof

**Maximizing manifold.** The squared norm of a torus point is \(R^2+r^2+2Rr\cos v\). Thus its norm is at most \(A\), with equality precisely for \(v=0\) modulo \(2\pi\). By the triangle inequality, \(D=2A\) is attained exactly when both points are on the outer equator, at opposite longitudes. In signed relative coordinates this locus is \((\alpha,\beta,\theta)=(0,0,0)\), with \(u_1\) free. Compactness bounds the squared deficit strictly away from zero outside any fixed small neighborhood of the maximizing circle.

**Transverse expansion.** Write \(\rho_1=R+r\cos\alpha\), \(\rho_2=R+r\cos\beta\). The parameterization gives
\[
D^2=\rho_1^2+\rho_2^2+2\rho_1\rho_2\cos\theta+r^2(\sin\alpha-\sin\beta)^2.
\]
In the orthogonal coordinates \((s,t,\theta)\), the second-order terms of the deficit are
\[
4A^2-D^2=Q(s,t,\theta)+O_{R,r}((|s|+|t|+|\theta|)^4),\qquad
Q=2rA s^2+2rR t^2+A^2\theta^2.
\]
Indeed the horizontal contribution to the deficit at second order is \(2Ar(\alpha^2+\beta^2)+A^2\theta^2\), and the vertical contribution is \(-r^2(\alpha-\beta)^2\). Simultaneous reversal of the three angles leaves the exact deficit invariant, so there is no cubic term. Positive definiteness gives \(4A^2-D^2\ge c_{R,r}(s^2+t^2+\theta^2)\) in a fixed small chart. Since the tail is the sublevel set with deficit \(<4A\varepsilon-\varepsilon^2\), it lies at distance \(O_{R,r}(\sqrt\varepsilon)\) from the origin of this chart. There the expansion has error \(O_{R,r}(\varepsilon^2)\). In particular, for fixed sufficiently large \(B=B(R,r)\), the tail contains \(\{Q<4A\varepsilon-B\varepsilon^2\}\) and is contained in \(\{Q<4A\varepsilon+B\varepsilon^2\}\) for all sufficiently small \(\varepsilon\). The ellipsoid at threshold \(4A\varepsilon\) has volume
\[
\frac{4\pi}{3}\frac{(4A\varepsilon)^{3/2}}{\sqrt{2rA}\sqrt{2rR}\,A}
=\frac{16\pi}{3r\sqrt R}\varepsilon^{3/2}.
\]
The volume between the bounding ellipsoids is \(O_{R,r}(\varepsilon^{5/2})\) by the \(3/2\)-power scaling of ellipsoid volume with threshold.

**Surface-area weight and limit law.** The area element is \(r(R+r\cos v)\,du\,dv\), and its integral is \(4\pi^2Rr\). Hence each longitude is uniform and independent of its meridian angle, whose density is \((R+r\cos v)/(2\pi R)\). The relative longitude is uniform and independent of the initial longitude. The joint density in \((s,t,\theta)\) is
\[
\frac{(R+r\cos\alpha)(R+r\cos\beta)}{8\pi^3R^2}
=\frac{A^2}{8\pi^3R^2}\bigl(1+O_{R,r}(\alpha^2+\beta^2)\bigr).
\]
Multiplying its central value by the ellipsoid volume gives the claimed coefficient. The density differs by \(O_{R,r}(\varepsilon)\) on the contributing region, so its variation contributes at most \(O_{R,r}(\varepsilon^{5/2})\). After the displayed scaling, the two bounding ellipsoids become concentric balls with radii \(1+O_{R,r}(\varepsilon)\) and the rescaled density, up to its common Jacobian factor, converges uniformly there to a positive constant. Normalizing yields the conditional limit. The conditioning event depends only on relative coordinates and hence does not change the independent initial longitude.

**Shape comparison.** Substituting \(\varepsilon=2A\eta\) gives the stated formula for \(H\), with
\[
\frac{d}{dk}\log H(k)=\frac{2k-5}{2k(k+1)}.
\]
This proves the two strict monotonicity intervals and uniqueness of the minimizer. The limits follow by substitution at \(k=1\) and by the leading power \(k^1\) as \(k\to\infty\). At fixed \(A=d_*/2\), each aspect ratio specifies exactly one pair \((R,r)=(Ak/(k+1),A/(k+1))\). Distinct ratios give distinct surface areas, since \(Rr=A^2 k/(k+1)^2\) is strictly decreasing for \(k>1\). They cannot be Euclidean-congruent.

## Reproducibility and relation to other distance laws

The accompanying `verify_torus_tail.py` evaluates the exact conditional longitude tail probability followed by numerical integration against the two meridian densities. This is a finite check of the leading coefficient, not a proof of the error estimate, the conditional law or the global optimum. Those are derived above.

The same surface and sampling measure occur in *Sharp two-moment ambiguity and three-moment reconstruction of ring-torus surfaces* (SCOPE-20261102-99081f2abf19), in which the reported observables are low-order even chord moments. Here the contrast is an extremum and a two-shape ambiguity for a local endpoint coefficient, not for a finite moment. See also Sidiropoulos (arXiv:1411.5639) for hypersphere surface chords, Tu and Fischbach (arXiv:math-ph/0201046) for spherical random distances, and Bäsel (arXiv:1204.2707) for polygons. These settings do not have the ring-torus aspect parameter. Historical priority outside the compared material is not asserted.

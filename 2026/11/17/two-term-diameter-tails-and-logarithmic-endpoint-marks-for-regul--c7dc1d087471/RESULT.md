# Two-term diameter tails and logarithmic endpoint marks for regular Reuleaux odd-gons

## Finding

Fix an odd integer \(n\ge5\). Let \(R_n\subset\mathbb R^2\) be the regular Reuleaux \(n\)-gon of width one. For independent arclength-uniform \(X,Y\in\partial R_n\) and \(D=\|X-Y\|\),
\[
\Pr(D>1-\varepsilon)=\frac{2n}{\pi^2}\,\varepsilon\left[\log\frac1\varepsilon+1+2\log\left(2\tan\frac{\pi}{2n}\right)\right]+o_n(\varepsilon).
\]
Consequently the normalized coefficient of \(\varepsilon\log(1/\varepsilon)\), multiplied by \(\pi^2/2\), recovers the odd number of curvature-jump vertices \(n\), despite all these curves having the same width one and perimeter \(\pi\). More precisely, the exceptional points concentrate on \(2n\) distinct ordered, mutually centered arc-pair sectors, asymptotically with equal probability. In each sector write \(s\) for arclength from the distinguished vertex at the first endpoint, and define \(U_\varepsilon=\log s/\log\varepsilon\) and \(W_\varepsilon=(1-D)/\varepsilon\). Their joint conditional law with the sector converges **in total variation** to the product of the uniform sector law and two independent \(\operatorname{Unif}(0,1)\) variables. Arbitrary labels outside these sectors do not affect the limit because their conditional probability tends to zero.

## Assumptions and scope

Write \(\alpha=\pi/n\) and \(\rho=[2\cos(\pi/(2n))]^{-1}\). Begin with regular planar vertices \(v_j=\rho(\cos(2\pi j/n),\sin(2\pi j/n))\), \(0\le j<n\). For each \(j\), replace the edge \([v_j,v_{j+1}]\) with the short unit-radius circular arc centered at \(v_{j+(n+1)/2}\), indices modulo \(n\). The arcs have length \(\alpha\) each, so \(P=n\alpha=\pi\). Their bounded convex interior is the unit-width body \(R_n\). All boundary-point sampling is independent and uniform with respect to Euclidean arclength, **not** uniform interior area or invariant random lines. The integer \(n\) is fixed before the distance threshold tends to zero.

## Proof

**1. Classify diameter contacts.** The curve is the intersection of the unit disks centered at the regular vertices and has diameter one. A boundary point in the relative interior of the circular arc centered at a vertex \(a\) is at distance exactly one from \(a\), whereas its distance from every other boundary point is strictly less than one. To justify the latter, equality in the unit-disk constraint \(\|z-a\|\le1\) at such a point selects this unique active circle and the opposing endpoint of a diameter in a convex body of constant width is the center \(a\); equivalently the unique normal at the smooth point selects its opposite support point. At a vertex there are two adjacent incident arcs, centered at its two opposite regular vertices. Consequently exactly \(2n\) ordered pairs of arcs possess a positive-length diameter-contact branch: in each, the first arc has one endpoint at the center of the second, and the second arc has one endpoint at the center of the first. All remaining ordered arc pairs have at most finitely many diameter contacts at pairs of vertices. At such other corner contacts neither boundary tangent is tangent to the unit circle centered at the opposite vertex, so the distance deficit grows at least linearly in each nonnegative arc parameter. They contribute \(O_n(\varepsilon^2)\) to the unnormalized event. Compactness excludes all other pairs for sufficiently small thresholds.

**2. Exact local law.** Every exceptional arc pair is congruent, with its two mutually opposite contact vertices at \(A=(0,0)\) and \(B=(1,0)\). Choose the side of the common diameter into which the two arcs bend. Their arclength charts are
\[
x(s)=(1-\cos s,\sin s),\quad y(t)=(\cos t,\sin t),\qquad 0\le s,t\le\alpha.
\]
They obey the exact identity
\[
\|x(s)-y(t)\|^2=1-4\sin(s/2)\bigl[\sin(s/2+t)-\sin(s/2)\bigr].
\]
In particular, the distance deficit \(F(s,t)=1-\|x(s)-y(t)\|\) satisfies \(F(s,t)=st[1+O(s+t)]\) as both arguments tend to zero, and for every fixed \(s\in(0,\alpha]\),
\[
F(s,t)=t\sin s+O_s(t^2)\quad(t\downarrow0).
\]
The same holds with \(s,t\) interchanged. All \(2n\) sectors therefore have the same local area
\[
I_\alpha(\varepsilon)=\int_0^\alpha\int_0^\alpha\mathbf1\{F(s,t)<\varepsilon\}\,dt\,ds.
\]
The full probability is \(\frac{2n}{\pi^2}I_\alpha(\varepsilon)+O_n(\varepsilon^2)\), since each ordered arc has length \(\alpha\) and all of \(\partial R_n\) has perimeter \(\pi\).

**3. Two-term integral asymptotic.** Choose the intermediate scale \(\delta=\varepsilon^{1/3}\), so \(\varepsilon\ll\delta^2\ll1\). Partition the square into the inner square \(0\le s,t\le\delta\), the two outer strips with one parameter at least \(\delta\) and the other at most \(\delta\), and the empty upper-right square. On the inner square the exact formula yields \(F(s,t)=st(1+O(\delta^2))\) uniformly; the elementary hyperbolic-area integral \(\int_{[0,\delta]^2}\mathbf1\{st<\varepsilon\}\,dsdt=\varepsilon[1+\log(\delta^2/\varepsilon)]\) is therefore accurate up to \(O(\varepsilon\delta^2\log(1/\varepsilon))=o(\varepsilon)\). In either outer strip the smaller parameter has boundary threshold \(\varepsilon/\sin s+O(\varepsilon^2/\delta^3)\) uniformly for \(\delta\le s\le\alpha\). Hence both outer strips together contribute
\[
2\varepsilon\int_\delta^\alpha\frac{ds}{\sin s}+o(\varepsilon)=2\varepsilon\log\frac{\tan(\alpha/2)}{\tan(\delta/2)}+o(\varepsilon).
\]
The error integral is \(O(\varepsilon^2/\delta^2)=o(\varepsilon)\); the upper-right square is empty for small enough \(\varepsilon\). Using \(\tan(\delta/2)=\delta/2+O(\delta^3)\), the sum simplifies to
\[
I_\alpha(\varepsilon)=\varepsilon\left[\log(1/\varepsilon)+1+2\log(2\tan(\alpha/2))\right]+o(\varepsilon).
\]
The factor \(2n/\pi^2\) completes the scalar theorem.

**4. Marked total-variation law.** In a selected pair, let \(L=\log(1/\varepsilon)\) and change variables \(u=-\log s/L\), \(w=F(s,t)/\varepsilon\). On every compact subrectangle of \((0,1)^2\), \(s=\varepsilon^u\), \(t\sim\varepsilon^{1-u}w\), and the Jacobian satisfies \(|\partial(s,t)/\partial(u,w)|\sim\varepsilon L\). Therefore the conditional joint density of \((u,w)\), normalized by \(I_\alpha(\varepsilon)\sim\varepsilon L\), converges pointwise to one almost everywhere on \((0,1)^2\). These densities have total mass one, so Scheffé's lemma proves convergence in \(L^1\), hence total variation. Equal sector areas make the finite sector label asymptotically uniform and independent. The nonselected arc pairs contribute only \(O_n(\varepsilon^2)=o(\varepsilon L)\), so including them does not change the limit.

## Verification

The standalone `verify_reuleaux.py` evaluates \(I_\alpha\) directly by deterministic one-dimensional integration after solving the exact trigonometric threshold. For odd \(n\in\{3,5,7,9\}\) and three small thresholds it independently tests the predicted two-term constant. The \(n=3\) calculation agrees with its independently known closed constant \(1+\log(4/3)\). Separate direct Sobol point-pair experiments on the constructed circular arcs for \(n=3,5,7\) check the leading count dependence. The finite numerical checks support, but do not replace, the exact local calculation and asymptotic argument.

## Relationship to prior work

The classical width and curve geometry is represented by Craizer and Martini (2014); their work studies involutes of constant-width polygons in normed planes rather than boundary-point distance tails. Bäsel (2012) computes invariant-line chord distributions and area-uniform pair distances for straight-edged regular polygons, which are different bodies and sampling measures. Existing published research on regular Reuleaux odd-gons covers **area-uniform** point-pair near-diameter tails, of order \(\varepsilon^3\log(1/\varepsilon)\), not boundary-uniform tails. The known Reuleaux triangle boundary-uniform law, including its second coefficient and logarithmic marks, agrees exactly with the \(n=3\) extension of the formulas above and is explicitly not claimed as new. The new statement concerns the entire fixed odd family \(n\ge5\), its sharp second coefficient, and its corner-count and joint-mark laws. Publication priority beyond the inspected sources is not certified.

## Limitations

The result is pointwise for each fixed odd \(n\ge5\). It is not uniform as \(n\to\infty\), and its singular logarithmic endpoint scale should not be substituted for the circle's different scale. It does not apply to perimeter-nonuniform sampling, area-uniform sampling, straight-sided regular polygons, or arbitrary nonsymmetric constant-width bodies. The total variation claim concerns the explicitly marked rare event, not the unconditioned endpoint positions. No exact finite-threshold CDF or independent mathematical audit is claimed.

## References

1. M. Craizer and H. Martini, *Involutes of Polygons of Constant Width in Minkowski Planes*, arXiv:1406.3205v1, 12 June 2014, https://arxiv.org/abs/1406.3205 (primary geometric MSC 52A10; context for constant-width polygon geometry, different normed-plane model).
2. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707v1, 12 April 2012, https://arxiv.org/abs/1204.2707 (straight-sided and different random measures).
3. A. Falcó and S. Myroshnychenko, *Area Minimization Among Group-Invariant Planar Convex Bodies of Constant Width*, arXiv:2608.05125v1, 5 August 2026, https://arxiv.org/abs/2608.05125 (regular Euclidean Reuleaux construction, supporting geometry only).
4. *Logarithmic near-diameter distance tails for every regular Reuleaux odd-gon*, published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-logarithmic-near-diameter-distance-tails-for-every-regular-reule--f7a617353911 (different area-uniform model).
5. *A logarithmic terminal chord law for the Reuleaux triangle*, published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-logarithmic-terminal-chord-law-for-the-reuleaux-triangle--bbcd3963fc69 (invariant-line sampling).

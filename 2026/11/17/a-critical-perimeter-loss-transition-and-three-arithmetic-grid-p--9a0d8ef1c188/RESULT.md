# A critical perimeter-loss transition and three arithmetic grid phases for superelliptic polygons

## Finding
Fix \(p>1\) and put
\[
K_p=\{(x,y)\in\mathbb R^2:|x|^p+|y|^p\le1\},\qquad
\gamma_p(\theta)=\frac{(\cos\theta,\sin\theta)}{(|\cos\theta|^p+|\sin\theta|^p)^{1/p}}.
\]
For \(n\ge3\), let \(Q_{p,n}\) be the convex hull of the \(n\) points \(\gamma_p(2\pi j/n)\), \(0\le j<n\), let \(E_{p,n}=\operatorname{per}(K_p)-\operatorname{per}(Q_{p,n})\), and write \(h=2\pi/n\). There is a sharp transition at \(p=3/2\).

**Singular regime \(1<p<3/2\).** For \(a\in\mathbb R\) define
\[
q_p(a)=\frac12\left(\int_a^{a+1}|t|^{2p-2}\,dt
-\left(\int_a^{a+1}\operatorname{sgn}(t)|t|^{p-1}\,dt\right)^2\right),
\qquad S_p(\delta)=\sum_{j\in\mathbb Z}q_p(j-\delta).
\]
The series is absolutely convergent and positive; \(S_p(1-\delta)=S_p(\delta)\). Along \(n\equiv r\pmod4\),
\[
\lim_{n\to\infty}\frac{E_{p,n}}{h^{2p-1}}
=\begin{cases}
4S_p(0), &r=0,\\
S_p(0)+2S_p(1/4)+S_p(1/2),&r=1,3,\\
2S_p(0)+2S_p(1/2),&r=2.
\end{cases}
\]
The three coefficients are genuinely distinct at least for all \(p>1\) sufficiently close to one: as \(p\downarrow1\) they tend respectively to \(0,5/4,1\).

**Critical regime \(p=3/2\).** The residue-independent leading law is
\[
\lim_{n\to\infty}\frac{E_{3/2,n}}{h^2\log n}=\frac1{12},
\qquad E_{3/2,n}\sim\frac{\pi^2}{3n^2}\log n.
\]

**Integrable-curvature regime \(p>3/2\).** With the usual planar determinant,
\[
\lim_{n\to\infty}\frac{E_{p,n}}{h^2}=
\frac1{24}\int_0^{2\pi}\frac{\det(\gamma_p'(\theta),\gamma_p''(\theta))^2}
{|\gamma_p'(\theta)|^3}\,d\theta=:C_p\in(0,\infty).
\]
The integral is interpreted off the four axes, where the derivative is classical, and by its integrable limit near the axes. In particular \(C_2=\pi/12\), matching \(2\pi-2n\sin(\pi/n)\).

## Assumptions and scope
The bodies, perimeter, determinant and norms are Euclidean. For each fixed \(p>1\), the vertices are sampled at angular roots of unity with zero initial phase; no result about optimally placed, arclength-equidistributed or randomly sampled polygons, nonunit semiaxes, or mixed \(p,n\) limits is asserted. In particular the limits are not uniform near \(p=3/2\).

## Proof
**1. Arc-minus-chord defect.** For a regular \(C^2\) plane curve \(\gamma\) and an interval \(I=[a,a+h]\) disjoint from singularities, let \(\ell_I=\int_I|\gamma'|\) and \(c_I=|\gamma(a+h)-\gamma(a)|\). On any compact regular \(C^2\) subarc, Taylor expansion yields uniformly
\[
\ell_I-c_I=\frac{h^3}{24}
\frac{\det(\gamma',\gamma'')^2}{|\gamma'|^3}+o(h^3),
\]
where the coefficient is evaluated at a point of the interval. The defect is nonnegative. The full perimeter difference is the sum of these defects over all adjacent sampling angles.

**2. Correct singular normal form and local lattice coefficient.** Rotate coordinates so an axis tip is \(\gamma_p(\alpha)=(1,0)\). For \(1<p<2\) the actual expansion is
\[
\gamma_p(\alpha+t)=\left(1-\frac{|t|^p}{p}+O_p(t^2),\quad t+O_p(|t|^{p+1})\right),\qquad t\to0.
\tag{1}
\]
The \(O(t^2)\) in the first component is essential: the cosine supplies a nonzero quadratic term. Because \(p<2\), this is \(o(|t|^p)\); the tangent direction has leading angular deviation \(-\operatorname{sgn}(t)|t|^{p-1}+o(|t|^{p-1})\). In tangent coordinate \(y=t+o(t)\), the normal graph is \(x=1-|y|^p/p+o(|y|^p)\). On a fixed rescaled cell \(t\in[ah,(a+1)h]\), expand the arc integrand \(\sqrt{1+v^2}=1+v^2/2+o(v^2)\) and the chord slope analogously, with leading slope \(-\operatorname{sgn}(t)|t|^{p-1}\). It follows that
\[
\ell_I-c_I=h^{2p-1}q_p(a)+o(h^{2p-1})
\tag{2}
\]
for each fixed \(a\). The quantity \(q_p(a)\) is precisely half the variance of the leading slope over a unit cell; identical calculations apply at the other three rotated axes.

**3. Uniform tail control, lattice phases, and the subcritical law.** The curve is regular \(C^1\). At angular distance \(d\) from an axis its unit tangent derivative is bounded in magnitude by \(C_pd^{p-2}\). For any cell of length \(h\),
\[
\ell_I^2-c_I^2=\int_I\!\int_I|\gamma'(s)||\gamma'(t)|
\bigl(1-\widehat\tau(s)\cdot\widehat\tau(t)\bigr)\,ds\,dt,
\qquad\widehat\tau=\gamma'/|\gamma'|.
\]
Using \(1-u\cdot v\le |u-v|^2/2\) for unit vectors and \(\ell_I+c_I\asymp h\), the defect is at most \(C_ph^3d^{2p-4}\) when \(d\ge h\). Cells touching an axis have defect \(O_p(h^{2p-1})\). Thus the total normalized contribution of cells at distance at least \(Mh\) from all axes is bounded by \(C_p\sum_{j\ge M}j^{2p-4}\) plus \(O_p(h^{3-2p})\) from the smooth complement. This vanishes as \(M\to\infty\) when \(p<3/2\). Formula (2) may therefore be summed over the lattice offsets at all four axes. Since \(q_p(j-\delta)\sim(p-1)^2|j|^{2p-4}/24\), the defining series converges absolutely.

The fractional locations of the four axes in the grid are \(\{kn/4\}\), \(k=0,1,2,3\). Their multisets are \(\{0,0,0,0\}\) for \(r=0\), \(\{0,0,1/2,1/2\}\) for \(r=2\), and \(\{0,1/4,1/2,3/4\}\) for odd \(n\). Reflection \(q_p(-1-a)=q_p(a)\) implies \(S_p(1-\delta)=S_p(\delta)\). Adding their series proves the three displayed subcritical limits.

**4. The logarithmic boundary.** For \(p=3/2\), direct differentiation away from an axis gives
\[
\frac{\det(\gamma_p',\gamma_p'')^2}{|\gamma_p'|^3}
=\frac1{4d}(1+o(1)),\qquad d\downarrow0.
\]
On cells whose distances lie between \(Mh\) and a small fixed \(\varepsilon\), the smooth-cell estimate of Step 1 has relative error bounded by terms tending to zero after first taking \(M\to\infty\) and then \(\varepsilon\to0\). Each of the eight sides of the four axes contributes \(h^2\log(1/h)/96\) at leading order. Cells within distance \(Mh\) contribute \(O_M(h^2)\), and those outside the fixed axis neighborhoods contribute \(O_\varepsilon(h^2)\). Summing eight sides gives \(h^2\log(1/h)/12\), and \(\log(1/h)=\log n+O(1)\).

**5. The integrable-curvature range.** If \(3/2<p<2\), summing the tail estimate in Step 3 bounds the near-axis contribution divided by \(h^2\) by \(O_p(\varepsilon^{2p-3})+o(1)\). For \(p\ge2\), the curvature density is bounded at the axes. On compact complementary subarcs, Step 1 and Riemann sums give the stated curvature integral. Sending \(\varepsilon\downarrow0\) proves the limit. Positivity follows from strict convexity, and near an axis the density is asymptotic to \((p-1)^2d^{2p-4}\) for \(1<p<2\), integrable exactly when \(p>3/2\).

**6. Genuine arithmetic distinction.** As \(p\downarrow1\), \(\operatorname{sgn}(t)|t|^{p-1}\to\operatorname{sgn}(t)\) outside zero. The variance on a unit cell tends to zero unless it straddles zero. If the negative fraction of a straddling cell is \(\delta\), its limiting half-variance is \(2\delta(1-\delta)\). Uniform summability follows from the tail estimate for \(p\) in a fixed neighborhood of one. Hence \(S_p(0)\to0\), \(S_p(1/4)\to3/8\), and \(S_p(1/2)\to1/2\), yielding respectively \(0,5/4,1\) for the three phase coefficients. By continuity they are pairwise distinct on a nonempty interval to the right of one.

## Verification
`verify_perimeter.py` in the unchanged source package computes polygon edge lengths, continuous perimeter, the lattice-variance series and the curvature integral independently. Its finite numerical checks are corroborative, not proofs of an unbounded sequence limit. The circle case gives exactly \(E_{2,n}=2\pi-2n\sin(\pi/n)\) and \(E_{2,n}/h^2\to\pi/12\). Formula (1) corrects an overly strong Taylor remainder in the original proof; all regime limits, constants, domains and comparisons are unchanged.

## Relationship to prior work
Fodor and Minuță, arXiv:2605.24599 (2026), construct this same radial root-of-unity polygon and prove qualitative Hausdorff convergence (Theorem 5.5), not the perimeter-loss coefficient or logarithmic crossover. The earlier *Sharp grid-phase Hausdorff asymptotics for radially sampled superelliptic disks* establishes maximum normal-distance errors for the same polygons; this does not imply the summed arc-minus-chord perimeter loss. Rodríguez and Montilla, arXiv:2607.09048 (2026), study hypergeometric formulas for the limiting Lamé curve perimeter, not a discrete sampling-error asymptotic in their accessible abstract. Smooth positive-curvature approximation frameworks such as Glasauer–Schneider (1996) do not directly include the singular axis regime. Historical priority relative to specialized chord quadrature remains open; inaccessible source text cannot be ruled out on the basis of an abstract.

## Limitations
Only fixed \(p>1\), zero-phase angular grids are treated. This is not an optimal-inscription theorem, a joint limit with \(p\) moving, or a result about a projection algorithm's rate. The critical leading logarithm has no residue dependence; no lower-order phase assertion is made. Some primary literature was not fully accessible, and this is not a claim of exhaustive priority or external certification.

## References
1. V.-A. Fodor and V.-A. Minuță, *An algorithm for approximating the metric projection onto a superelliptic disk*, arXiv:2605.24599v1 (2026-05-23), v2 (2026-10-04), https://arxiv.org/abs/2605.24599.
2. R. O. Rodríguez and Y. Montilla, *Hypergeometric Series Representations for the Perimeter of Lamé Superellipses*, arXiv:2607.09048v1 (2026-07-10), https://arxiv.org/abs/2607.09048.
3. *Sharp grid-phase Hausdorff asymptotics for radially sampled superelliptic disks*, public mathematical record (2026-11-08), https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-sharp-grid-phase-hausdorff-asymptotics-for-radially-sampled-supe--188b17416968.
4. S. Glasauer and R. Schneider, *Asymptotic approximation of smooth convex bodies by polytopes*, Forum Mathematicum 8 (1996), 363–377.

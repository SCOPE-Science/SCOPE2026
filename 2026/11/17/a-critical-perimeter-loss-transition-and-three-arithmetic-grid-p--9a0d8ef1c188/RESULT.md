# A critical perimeter-loss transition and three arithmetic grid phases for superelliptic polygons

## Finding
Let \(p>1\) be fixed, and define the planar superelliptic disk
\[
K_p=\{(x,y)\in\mathbb R^2:|x|^p+|y|^p\le1\},\qquad
\gamma_p(\theta)=\frac{(\cos\theta,\sin\theta)}{(|\cos\theta|^p+|\sin\theta|^p)^{1/p}}.
\]
For each integer \(n\ge3\), let \(Q_{p,n}\) be the convex hull of the \(n\) points \(\gamma_p(2\pi j/n)\), \(0\le j<n\), and let \(E_{p,n}=\operatorname{per}(K_p)-\operatorname{per}(Q_{p,n})\). Write \(h=2\pi/n\).

There is a sharp transition at \(p=3/2\), with **three distinct arithmetic subsequence laws possible below the transition**:

**Singular regime \(1<p<3/2\).** Define, for \(a\in\mathbb R\),
\[
q_p(a)=\frac12\left(\int_a^{a+1}|t|^{2p-2}\,dt
-\left(\int_a^{a+1}\operatorname{sgn}(t)|t|^{p-1}\,dt\right)^2\right),\quad
S_p(\delta)=\sum_{j\in\mathbb Z}q_p(j-\delta).
\]
The series converges absolutely, is strictly positive, and satisfies \(S_p(1-\delta)=S_p(\delta)\). Then
\[
\lim_{\substack{n\to\infty\\ n\equiv r\pmod4}}\frac{E_{p,n}}{h^{2p-1}}
=\begin{cases}
4S_p(0),&r=0,\\
S_p(0)+2S_p(1/4)+S_p(1/2),&r=1,3,\\
2S_p(0)+2S_p(1/2),&r=2.
\end{cases}
\]
These are exact, geometrically intrinsic, rapidly specifiable constants (although their defining series converges slowly when \(p\) approaches \(3/2\)). They are genuinely different at least for every \(p>1\) sufficiently close to \(1\): as \(p\downarrow1\), the three displayed coefficients converge respectively to \(0\), \(5/4\), and \(1\).

**Critical regime \(p=3/2\).** Independently of the residue class,
\[
\lim_{n\to\infty}\frac{E_{3/2,n}}{h^2\log n}=\frac1{12},
\quad\text{equivalently}\quad
E_{3/2,n}\sim\frac{\pi^2}{3n^2}\log n.
\]

**Integrable-curvature regime \(p>3/2\).** Let the determinant be the scalar planar cross product. Then
\[
\lim_{n\to\infty}\frac{E_{p,n}}{h^2}
=C_p:=\frac1{24}\int_0^{2\pi}
\frac{\det(\gamma_p'(\theta),\gamma_p''(\theta))^2}{|\gamma_p'(\theta)|^3}\,d\theta.
\]
The integral is positive and finite for every fixed \(p>3/2\). In particular \(C_2=\pi/12\), consistent with the exact circular polygon perimeter \(2n\sin(\pi/n)\).

## Assumptions and scope
All perimeter and Euclidean norms are ordinary Euclidean quantities, and \(p\) is fixed as \(n\to\infty\). Vertices are sampled at angular roots of unity with zero initial phase; no claim is made about arclength-equidistributed, optimally placed, or randomly sampled polygons. The source paper establishes Hausdorff convergence of exactly this radial sampling construction; the result here gives new perimeter-loss asymptotics. No assertion of uniformity in \(p\), especially across \(3/2\), is made.

## Proof
**1. Smooth-cell defect.** For a regular \(C^2\) plane curve \(\gamma\) with \(\gamma'\ne0\), put \(\ell_I=\int_I|\gamma'|\,dt\) and \(c_I=|\gamma(b)-\gamma(a)|\) for \(I=[a,b]\) of width \(h\). Taylor expansion at the left endpoint (or at the midpoint) gives
\[
\ell_I-c_I=\frac{h^3}{24}
\frac{\det(\gamma',\gamma'')^2}{|\gamma'|^3}+o(h^3),
\]
uniformly on compact arcs avoiding all coordinate axes. The difference is nonnegative by the triangle inequality. The perimeter deficit is the sum of the defects of the \(n\) consecutive arcs.

**2. Local singular normal form.** Near an axial angle \(\alpha\), rotate so that \(\gamma_p(\alpha)=(1,0)\). For \(1<p<2\), as \(t\to0\) the radial curve satisfies
\[
\gamma_p(\alpha+t)=\left(1-\frac{|t|^p}{p}+O(|t|^{\min(2p,p+2)}),\ t+O(|t|^{p+1})\right).
\]
(The Taylor bounds are local and may be enlarged without affecting the leading term.) Its tangent direction differs from the axial tangent by \(-\operatorname{sgn}(t)|t|^{p-1}+o(|t|^{p-1})\). Thus, for any fixed real \(a\), the arc whose angular endpoints are \(\alpha+ah\) and \(\alpha+(a+1)h\) has
\[
\ell_I-c_I=h^{2p-1}q_p(a)+o(h^{2p-1}).\tag{1}
\]
Indeed, in tangent coordinate \(y=t+o(t)\), the normal coordinate is \(x=1-|y|^p/p+o(|y|^p)\); expanding \(\sqrt{1+v^2}=1+v^2/2+o(v^2)\) in arc length and chord length yields precisely one half the variance of \(\operatorname{sgn}(t)|t|^{p-1}\) over the interval. The same calculation works for the other three axes by rotations.

**3. A uniform tail bound.** For \(1<p<2\), the curve is regular and \(C^1\); its unit tangent is locally \((p-1)\)-Hölder, and away from an axis its derivative is bounded by \(C_p d^{p-2}\), with \(d\) the distance in angle to the nearest axis. The identity
\[
\ell_I^2-c_I^2=\int_I\!\int_I |\gamma'(s)||\gamma'(t)|
\bigl(1-\widehat\tau(s)\cdot\widehat\tau(t)\bigr)\,ds\,dt,
\quad\widehat\tau=\gamma'/|\gamma'|,
\]
gives \(0\le\ell_I-c_I\le C_ph^3d^{2p-4}\) if \(d\ge h\), and \(O_p(h^{2p-1})\) on the finitely many cells meeting an axis. Consequently, after dividing by \(h^{2p-1}\), the total contribution of intervals farther than \(Mh\) but closer than a fixed small angle to an axis is bounded by
\[
C_p\sum_{j\ge M}j^{2p-4}.
\]
When \(p<3/2\), this tends to zero as \(M\to\infty\); the intervals away from all axes contribute only \(O_p(h^2)=o(h^{2p-1})\). Formula (1) therefore sums to the four axial lattice series, proving the first regime.

At the axis \(\alpha_k=k\pi/2\), the fractional position among sample angles is \(\delta_k=\{kn/4\}\). The multisets of four phases are \(\{0,0,0,0\}\) if \(n\equiv0\pmod4\), \(\{0,0,1/2,1/2\}\) if \(n\equiv2\pmod4\), and \(\{0,1/4,1/2,3/4\}\) if \(n\) is odd. Reflection invariance \(q_p(-1-a)=q_p(a)\) gives the claimed coefficients. The asymptotic \(q_p(j-\delta)\sim(p-1)^2|j|^{2p-4}/24\) proves absolute convergence.

**4. Critical logarithm.** At \(p=3/2\), the curvature-density appearing in Step 1 is, as angular distance \(d\downarrow0\) from each side of any axis,
\[
\frac{\det(\gamma_{3/2}',\gamma_{3/2}'')^2}{|\gamma_{3/2}'|^3}
=\frac1{4d}(1+o(1)).
\]
On cells between \(Mh\) and fixed small angular distance \(\varepsilon\), the local smooth-cell expansion is uniform up to a relative \(o_M(1)+o_\varepsilon(1)\) error. Each side of each axis contributes
\(h^2\log(1/h)/96+o(h^2\log(1/h))\), so the eight sides contribute \(h^2\log(1/h)/12\). Cells within \(Mh\) of an axis or outside the fixed small neighborhood contribute \(O_M(h^2)+O_\varepsilon(h^2)\), negligible on this scale. Since \(\log(1/h)=\log n+O(1)\), this proves the critical coefficient.

**5. Integrable curvature.** If \(3/2<p<2\), the same tail estimate in Step 3 shows that the contribution of cells within angular distance \(\varepsilon\) from the four axes, normalized by \(h^2\), is \(O_p(\varepsilon^{2p-3})+o(1)\). For \(p\ge2\), the curvature density is bounded at each axis. On the complementary smooth arcs, Step 1 sums by Riemann integration. Sending \(\varepsilon\downarrow0\) gives the integral in the third regime. The formula is positive because \(K_p\) is strictly convex, and finite since its integrand behaves like \((p-1)^2d^{2p-4}\) at the axes when \(1<p<2\).

**6. The three constants are not an artifact.** For \(p\downarrow1\), the local tangent graph converges to the diamond corner: \(\operatorname{sgn}(t)|t|^{p-1}\to\operatorname{sgn}(t)\) away from zero. Hence \(q_p(a)\) tends to zero unless \([a,a+1]\) crosses zero, where it tends to \(2\delta(1-\delta)\), with \(\delta\) the fraction of the interval lying on the negative side. The tail bound can be made uniform for \(p\) near one, so \(S_p(0)\to0\), \(S_p(1/4)\to3/8\), and \(S_p(1/2)\to1/2\). Thus the three residue-class coefficients tend to \(0,5/4,1\), respectively, and remain pairwise distinct for all \(p\) in some nonempty right neighborhood of one.

## Verification
The standalone script `verify_perimeter.py` independently computes polygon edge lengths from radial samples, the full curve perimeter from a separate Cartesian arc-length integral, the lattice-variance coefficients, and the limiting curvature integral from analytically differentiated polar coordinates. Executing `python verify_perimeter.py` with NumPy and SciPy produced `PASS: 44 numerical consistency checks`, including the exact circular identity, four congruence classes at \(p=5/4\), the logarithmic normalization at \(p=3/2\), and curvature-integral limits at \(p=1.7,2.5\). Finite calculations are only corroborative; none certifies the asymptotic claims.

## Relationship to prior work
Fodor and Minuță (arXiv:2605.24599v1, first public 2026-05-23; v2 2026-10-04) introduced exactly these equally spaced radial polygons and proved qualitative Hausdorff convergence in their Theorem 5.5. Their full manuscript's Section 5 and introductory roadmap do not claim a perimeter-loss order, an \(L^2\)-curvature integrability transition, or these arithmetic constants. A separately published theorem titled *Sharp grid-phase Hausdorff asymptotics for radially sampled superelliptic disks* derives leading **Hausdorff** errors for the same polygons; it does not imply perimeter-loss constants, because Hausdorff distance controls the maximal local gap whereas perimeter loss sums local squared tangent variations. Rodríguez and Montilla (arXiv:2607.09048v1) study exact representations of the **limiting curve's perimeter**, not the stated sampling error in their accessible abstract. General smooth-body approximation theorems presupposing bounded positive curvature do not apply verbatim to the singular interval \(1<p\le3/2\). A specialized existing result in asymptotic chordal quadrature could still cover these formulas; historical priority is provisional, not certified.

## Limitations
Only the fixed-\(p\), zero-phase angular sampling rule is covered. The result does not assert optimal perimeter approximation, a rate for the metric-projection algorithm itself, a complete joint \(p,n\) crossover, or anything about non-unit semiaxes. The \(p=3/2\) logarithmic law has no phase dependence in its leading term; possible lower-order phase corrections are not claimed. Published-priority comparisons are not exhaustive, and the Rodríguez–Montilla manuscript was available here only via abstract.

## References
1. V.-A. Fodor and V.-A. Minuță, *An algorithm for approximating the metric projection onto a superelliptic disk*, arXiv:2605.24599v1 (2026-05-23), v2 (2026-10-04), https://pdfs.assets.alphaxiv.org/2605.24599v2.pdf.
2. R. O. Rodríguez and Y. Montilla, *Hypergeometric Series Representations for the Perimeter of Lamé Superellipses*, arXiv:2607.09048v1 (2026-07-10), https://arxiv.org/abs/2607.09048.
3. *Sharp grid-phase Hausdorff asymptotics for radially sampled superelliptic disks*, published mathematical record (2026-11-08), published-finding corpus record 2026/11/8/188b17416968 (public mathematical archive).
4. S. Glasauer and R. Schneider, *Asymptotic approximation of smooth convex bodies by polytopes*, Forum Mathematicum 8 (1996), 363–377.

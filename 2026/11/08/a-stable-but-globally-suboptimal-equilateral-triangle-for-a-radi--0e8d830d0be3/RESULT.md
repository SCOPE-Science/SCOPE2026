# A stable but globally suboptimal equilateral triangle for a radial power density

## Finding

For any real \(p\ge0\) and Euclidean triangle \(T\) in the closed centered unit disk \(B=\{x\in\mathbb R^2:\|x\|_2\le1\}\), define the radial weighted area
\[
F_p(T)=\int_T\|x\|_2^p\,dx.
\]
The regular equilateral triangle with all three vertices on \(\partial B\) is a **strict local maximizer, modulo rigid rotations**, for every \(0\le p<2\). Nevertheless this local optimizer need not be global. At the rational exponent \(p=7/4\), let \(T_{\mathrm{iso}}\) have three vertices on \(\partial B\) with successive counterclockwise central gaps
\[
\left(\frac{19\pi}{36},\frac{19\pi}{36},\frac{17\pi}{18}\right).
\]
These gaps add to \(2\pi\) and are each strictly smaller than \(\pi\), so the origin lies in the strict interior. The exact, certified inequality is
\[
\boxed{F_{7/4}(T_{\mathrm{iso}})-F_{7/4}(T_{\mathrm{eq}})>0.00011.}
\]
Hence a whole open interval of exponents around \(7/4\), entirely below \(2\), exhibits **local-but-not-global equilateral optimality**. The conclusion applies to the full family of triangles contained in the disk, not just the isosceles family.

## Assumptions and scope

The disk is fixed at the origin, has Euclidean radius one, and is not allowed to translate. The functional uses ordinary two-dimensional Lebesgue area. A strict local maximum *modulo rotations* means that in a sufficiently small neighborhood of the regular triangle all distinct nonrotated competitors have strictly smaller weighted area; rotations preserve the value. The stronger global-inequality witness is a bona fide origin-containing triangle with all vertices on the unit circle. Its specified gaps are angles between rays to consecutive vertices, not interior angles of the triangle. We do not require all candidate triangles to contain the origin; this condition holds automatically in a small neighborhood of the equilateral triangle.

## Proof

**1. Boundary reduction and sector formula.** Let \(T\) contain the origin in its interior. Move any vertex radially outward along its own ray until it reaches \(\partial B\). The resulting triangle still contains the origin strictly, includes the original triangle, and has strictly greater \(F_p\) unless the vertex was already on the circle (the integrand is positive except on a measure-zero set). Therefore a local maximum around the equilateral triangle must have three boundary vertices.

Write their successive angular gaps as \(\delta_1,\delta_2,\delta_3\), with \(0<\delta_i<\pi\) and \(\delta_1+\delta_2+\delta_3=2\pi\). The supporting line of the edge spanning a gap \(\delta\), in polar coordinates measured from the edge-normal direction, is \(r\cos t=\cos(\delta/2)\). Its radial extent is \(\cos(\delta/2)/\cos t\) for \(-\delta/2\le t\le\delta/2\). Integrating \(r^{p+1}\,dr\,dt\) yields the exact decomposition
\[
F_p(T)=\sum_{i=1}^3 f_p(\delta_i),\qquad
f_p(\delta)=\frac{2}{p+2}\int_0^{\delta/2}
\left(\frac{\cos(\delta/2)}{\cos t}\right)^{p+2}dt.
\]
This is valid for all admissible gap triples, not just symmetric triangles.

**2. Uniform strict local stability for the complete range \(0\le p<2\).** Differentiate the preceding expression twice with respect to the full gap \(\delta\), taking its upper integration limit into account. With \(\alpha=\delta/2\) and \(s=p+2\), one obtains
\[
f_p''(\delta)=-\frac12\left[(1-(s-1)\tan^2\alpha)(\cos\alpha)^s\int_0^\alpha(\cos t)^{-s}\,dt+\tan\alpha\right].
\]
At the equilateral gaps \(\delta=2\pi/3\), substitution \(u=\tan t\) gives
\[
2f_p''(2\pi/3)=(3p+2)I_p-\sqrt3,\qquad
I_p=2^{-(p+2)}\int_0^{\sqrt3}(1+u^2)^{p/2}\,du.
\]
For \(0\le p\le2\), Hölder's inequality and the exact endpoint integrals imply
\[
\int_0^{\sqrt3}(1+u^2)^{p/2}\,du
\le (\sqrt3)^{1-p/2}(2\sqrt3)^{p/2}=\sqrt3\,2^{p/2}.
\]
Thus
\[
2f_p''(2\pi/3)\le\sqrt3\left(\frac{3p+2}{2^{p/2+2}}-1\right)<0
\quad(0\le p<2).
\]
Indeed \(h(p)=4\,2^{p/2}-(3p+2)\) has \(h(2)=0\) and derivative \(h'(p)=2(\log2)2^{p/2}-3\le4\log2-3<0\) on this interval. Hence \(h(p)>0\) for every \(p<2\). Under the constraint \(\sum_i\delta_i=2\pi\), the second variation is \(f_p''(2\pi/3)\sum_i(\delta_i-2\pi/3)^2<0\) away from the rotational direction. Taylor's theorem proves strict local maximality for boundary triangles, and radial monotonicity handles possible interior vertices. No assertion of a uniform neighborhood as \(p\uparrow2\) is needed.

**3. A strict nonregular improvement at a rational exponent.** Put \(s=15/4\), and for \(0<a<\pi/2\) write
\[
J_s(a)=\int_0^a g_{s,a}(t)\,dt,
\qquad g_{s,a}(t)=\left(\frac{\cos a}{\cos t}\right)^s.
\]
The integrand increases monotonically from \((\cos a)^s\) to \(1\). For each positive integer \(N\), elementary left and right Riemann sums therefore give a *rigorous finite enclosure*
\[
L_N(a)=\frac aN\sum_{j=0}^{N-1}g_{s,a}(ja/N)
\le J_s(a)\le
L_N(a)+\frac aN\bigl(1-(\cos a)^s\bigr)=U_N(a).
\]
For the isosceles comparator, the three half-gaps are \(19\pi/72,19\pi/72,17\pi/36\); the equilateral half-gaps are all \(\pi/3\). Consequently the exact weighted-area difference is bounded below by
\[
\frac{2}{s}\left(2L_N(19\pi/72)+L_N(17\pi/36)-3U_N(\pi/3)\right).
\]
Set \(N=4096\). Directed interval evaluation of the displayed finite elementary sum gives a certified lower bound greater than \(0.0001117232163\). In particular the advertised \(0.00011\) strict inequality follows. The included script `check.py` reproduces this interval bound from the definition of the finite sums, including enclosure of \(\pi\) and trigonometric evaluations. No finite sample or floating-point quadrature is substituted for an infinite-dimensional optimization proof: the analytic local theorem and exact monotone Riemann enclosures establish the statements.

**4. An open exponent interval.** For each fixed nondegenerate triangle in the unit disk, \(p\mapsto F_p(T)\) is continuous by dominated convergence. Hence the strict positive comparison at \(p=7/4\) persists on some nonempty open interval about that exponent, chosen inside \((0,2)\). Step 2 proves local equilateral maximality throughout the interval, while Step 3 gives a competing triangle of larger weighted area.

## Verification

Run `python3 check.py` after installing dependencies from `requirements.txt`. The checker evaluates the strictly increasing one-dimensional sector integral using 4096-piece left and right interval Riemann sums. It requires both the positive certified comparison and the negative local second-variation interval bound, and also independently integrates the density directly in Cartesian triangle coordinates by two-dimensional midpoint quadrature. Successful execution prints `ALL_RADIAL_WEIGHTED_TRIANGLE_CHECKS_PASSED`. The two-dimensional midpoint quadrature is a consistency test, not a proof; the Riemann interval bounds plus the analytic arguments above certify the theorem. In the specified interval setup, the stronger numerical enclosure from the checker's monotone sums has lower bound about \(0.00011172321630575\). The checker uses the `mpmath.iv` directed interval implementation; independent formal verification of that implementation is not asserted.

## Relationship to prior work

Basit and Lángi, *Discrete isoperimetric problems in spaces of constant curvature*, Section 4, establish radial-density extremal principles under different containment and monotonicity assumptions; their Section 5, Example 1, shows that general radial-density maximality of inscribed regular triangles can fail for a specially chosen concentrated radial density. Their example does not furnish a smooth power-law density with a **strictly locally stable but globally nonoptimal** regular triangle. Besau, Hoehner and Kur develop dual-volume deviations, including general radial exponents and large-vertex approximation, without this finite-vertex local/global dichotomy. Hoehner, Schütt and Werner obtain nonasymptotic, non-sharp-for-three-vertices bounds for all real dual exponents, not an equality-shape or local-maximizer classification.

A published published-finding corpus result titled *Sharp fourth-order dual deviation of the disk for inscribed triangles* gives the sharp case corresponding to \(p=2\), and shows that the equilateral triangle is then a degenerate cubic saddle rather than a local maximizer. This case is expressly **not** claimed new. The present result distinguishes \(0\le p<2\), where the regular triangle remains strictly locally stable, from its global failure already at the explicitly certified interior exponent \(7/4\). A statement only at \(p=2\) does not imply this combination of local and global behavior.

## Limitations

No classification of global maximizers for general \(p\) is claimed, and the precise parameter where global optimality first fails is not determined. The theorem is about planar triangles in a fixed centered unit disk and the radial power density \(\|x\|_2^p\). It does not cover arbitrary polygons, non-power weights, moving disk centers, or other dimensions. The inequality certificate uses reproducible directed interval arithmetic; a mathematically independent audit has not been performed. An older or differently formulated equivalent result cannot be excluded absolutely.

## References

1. F. Besau, S. Hoehner, G. Kur, *Intrinsic and Dual Volume Deviations of Convex Bodies and Polytopes*, arXiv:1905.08862v1 (May 21, 2019), https://arxiv.org/html/1905.08862v2 .
2. B. Basit, Z. Lángi, *Discrete isoperimetric problems in spaces of constant curvature*, arXiv:2206.04323v1 (June 9, 2022), https://doi.org/10.1112/mtk.12175 .
3. S. Hoehner, C. Schütt, E. M. Werner, *Dual volume approximation of the Euclidean ball by polytopes with a fixed number of k-faces*, arXiv:2608.02554v1 (August 3, 2026), https://arxiv.org/html/2608.02554v1 .
4. *Sharp fourth-order dual deviation of the disk for inscribed triangles*, published-finding corpus public research record (October 11, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-order-dual-deviation-of-the-disk-for-inscribed-tria--99043051040d .

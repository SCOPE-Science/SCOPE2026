# Central disk interception by random boundary chords: a sharp isoperimetric intensity and stability law

## Finding
Let \(K\subset\mathbb R^2\) be any compact, origin-symmetric convex body with the origin in its interior, Euclidean perimeter \(P\), and radial function \(r(\theta)>0\). Take two independent points \(X,Y\) uniformly by **arclength on its boundary**, and let \(H_K(\varepsilon)\) be the probability that the finite segment \([X,Y]\) intersects the centered closed Euclidean disk of radius \(\varepsilon\). Put \(q(\theta)=\sqrt{r(\theta)^2+r'(\theta)^2}\) at almost every angle (the radial function is Lipschitz). Then, as \(\varepsilon\downarrow0\),
\[
H_K(\varepsilon)=\kappa_K\varepsilon+o_K(\varepsilon),\qquad
\boxed{\kappa_K=\frac4{P^2}\int_0^{2\pi}\frac{q(\theta)^2}{r(\theta)}\,d\theta.}
\]
The sharp perimeter-only bound is
\[
\boxed{\kappa_K\ge\frac4P},
\]
with equality if and only if \(K\) is a disk centered at the origin. There is a **quantitative sharp deficit**
\[
\boxed{\kappa_K-\frac4P\ \ge\ \frac2{P^2}\int_0^{2\pi}\frac{r'(\theta)^2}{r(\theta)}\,d\theta.}
\]
No larger universal factor than \(2\) can replace the factor \(2\) on the right. For any fixed noncircular \(K\), its central-disk interception probability is consequently strictly greater than that of the centered disk having the same perimeter for all sufficiently small positive \(\varepsilon\).

For the square \(K=[-1,1]^2\), the exact intensity is
\[
\boxed{\kappa_K=\frac{\sqrt2+\log(1+\sqrt2)}4=0.573896787348159\ldots,}
\]
compared with \(4/P=1/2\) for the equal-perimeter disk.

## Assumptions and scope
Here \(\partial K\) is sampled according to normalized Euclidean **one-dimensional Hausdorff measure**, independently with replacement. It is not the Crofton law of an invariant random supporting line, a midpoint-uniform chord law, or uniform interior sampling. The body need not have a differentiable boundary: squares and other polygons are included. Its origin symmetry is \(K=-K\), and the target is a Euclidean disk, not a homothetic copy of \(K\). The quantity \(H_K\) tests the entire finite segment, not its supporting infinite line. Corners and radial nondifferentiability angles have zero arclength probability. The coefficient and \(o_K(\varepsilon)\) are for a fixed body: no shape-uniform error rate is asserted. All integrals over angles are Lebesgue integrals and radial derivatives are the almost-everywhere derivatives of the Lipschitz function \(r\).

## Proof
**1. Radial arclength representation.** A compact convex body containing a neighborhood of the origin has a positive, bounded, Lipschitz radial function. Its polar parametrization is \(x(\theta)=r(\theta)(\cos\theta,\sin\theta)\), and its arclength element equals \(q(\theta)\,d\theta\) almost everywhere, where \(q=\sqrt{r^2+(r')^2}\). Consequently \(P=\int_0^{2\pi}q\,d\theta\). Central symmetry implies \(r(\theta+\pi)=r(\theta)\) and \(q(\theta+\pi)=q(\theta)\) almost everywhere.

**2. Localizing intercepting pairs.** The segment between two distinct boundary points contains the origin if and only if the points lie on opposite radial rays: \(Y=-X\) after adjusting the lengths, and central symmetry then makes them exactly antipodal. By compactness, for every fixed small angular separation cutoff \(\delta_0>0\), the minimum distance from the origin to all boundary segments whose endpoint angles differ from \(\pi\) by at least \(\delta_0\) has a strictly positive lower bound. Hence sufficiently small disk interceptions occur only for angular pairs \((\theta,\theta+\pi+\delta)\) with \(|\delta|<\delta_0\).

Fix \(\theta\). Write \(a=r(\theta)\) and \(b=r(\theta+\delta)\). The endpoints are \(a(\cos\theta,\sin\theta)\) and \(-b(\cos(\theta+\delta),\sin(\theta+\delta))\). When \(\delta\) is small, the perpendicular projection of the origin onto their supporting line lies strictly inside the segment (uniformly in \(\theta\), since \(r\) is bounded away from zero). Therefore the true segment distance is
\[
d(0,[X,Y])=\frac{ab|\sin\delta|}{\sqrt{a^2+b^2+2ab\cos\delta}}.
\]
The Lipschitz bound \(b=a+O_K(|\delta|)\) and positive lower bound for \(a\) imply, **uniformly** in the first angle,
\[
d(0,[X,Y])=\frac{r(\theta)}2|\delta|+O_K(\delta^2).
\]
It follows by sandwiching the distance test between angular windows that the permitted second-angle interval is, up to an error of length \(O_K(\varepsilon^2)\),
\[
|\delta|\le\frac{2\varepsilon}{r(\theta)}.
\]
The sandwich does not require differentiability or strict monotonicity at corners: for a suitable uniform constant \(C_K\), the inner and outer windows have halfwidths \(2\varepsilon/r(\theta)\mp C_K\varepsilon^2\).

**3. Integrating the angular window.** The angular density of each arclength-uniform endpoint is \(q/P\). Conditional on a first angle \(\theta\), Lebesgue's differentiation theorem at the antipodal angle and \(q(\theta+\pi)=q(\theta)\) give, for almost every \(\theta\),
\[
\Pr\{[X,Y]\cap B_\varepsilon\ne\varnothing\mid\theta_X=\theta\}
=\frac{4\varepsilon}{P}\frac{q(\theta)}{r(\theta)}+o_\theta(\varepsilon).
\]
Because \(q\) is essentially bounded and \(r\) bounded away from zero, the angular-window probability divided by \(\varepsilon\) has a uniform bound. Dominated convergence against the first-endpoint density \(q/P\) yields the announced expression for \(\kappa_K\). It also proves the expansion for convex polygons, where the differentiation theorem applies away from finitely many vertex angles.

**4. Exact deficit, rigidity, and sharpness.** Since \(q\ge r>0\) almost everywhere,
\[
\begin{aligned}
\kappa_K-\frac4P
&=\frac4{P^2}\int_0^{2\pi}\left(\frac{q^2}{r}-q\right)d\theta\\
&=\frac4{P^2}\int_0^{2\pi}\frac{(r')^2}{r}\frac{q}{q+r}\,d\theta\\
&\ge\frac2{P^2}\int_0^{2\pi}\frac{(r')^2}{r}\,d\theta.
\end{aligned}
\]
If equality holds in \(\kappa_K\ge4/P\), the nonnegative integrand forces \(r'=0\) almost everywhere. Lipschitz continuity implies \(r\) is constant, hence \(K\) is a centered disk. Conversely, for a centered disk of radius \(R\), chord geometry gives the exact law \(H_K(\varepsilon)=\tfrac2\pi\arcsin(\varepsilon/R)\) for \(0\le\varepsilon\le R\), with derivative \(2/(\pi R)=4/P\).

To prove **optimality of the quantitative factor**, take the smooth radial family \(r_\eta(\theta)=1+\eta\cos(2\theta)\). For sufficiently small \(|\eta|\), it is the radial function of a strictly convex centrally symmetric body: its polar curvature numerator \(r_\eta^2+2(r_\eta')^2-r_\eta r_\eta''\) is then positive. As \(\eta\to0\), \(q_\eta/(q_\eta+r_\eta)\to1/2\) uniformly, while \(\int (r_\eta')^2/r_\eta\,d\theta>0\) for \(\eta\ne0\). The quotient of the exact deficit by \(\frac2{P_\eta^2}\int (r_\eta')^2/r_\eta\) therefore tends to one. Thus increasing \(2\) even slightly would invalidate the inequality for sufficiently small nonzero \(\eta\).

**5. Square evaluation.** On the right edge of \([-1,1]^2\), \(-\pi/4\le\theta\le\pi/4\), one has \(r(\theta)=\sec\theta\), \(q(\theta)=\sec^2\theta\), and \(q^2/r=\sec^3\theta\). Fourfold rotation symmetry and \(P=8\) yield
\[
\kappa_K=\frac4{64}\cdot4\int_{-\pi/4}^{\pi/4}\sec^3\theta\,d\theta
=\frac{\sqrt2+\log(1+\sqrt2)}4.
\]

## Verification
The companion `checks/central_chord_check.py` computes the square coefficient from direct one-dimensional quadrature, **independently** rederives the square coefficient from opposite-side endpoint coordinates \(u=(y_1+y_2)/2\), \(v=(y_2-y_1)/2\) and \(d=|u|/\sqrt{1+v^2}\), checks the closed form, calculates the full radial deficit for three strictly convex perturbations, and independently simulates \(3{,}500{,}000\) endpoint pairs on square sides. The actual segment-to-origin distance is calculated by projecting and clipping onto each segment, not by assuming the supporting-line model. Four small disk radii were compared with the linear coefficient, and the perturbation stability ratio approached one. The checker reported `CENTRAL_CHORD_INTENSITY_DIAGNOSTICS_OK`. These finite calculations check formulas and scales; the above proof, not Monte Carlo, justifies the infinite theorem. Run `python checks/central_chord_check.py` after installing `numpy` and `scipy`.

## Relationship to prior work
The classic random-chord problem is sensitive to the **sampling law**. Bäsel's *Random chords and point distances in regular polygons* (2012) defines chords from motion-invariant lines and derives chord-length and interior-pair-distance distributions. In contrast, the present sampling first chooses two independent **boundary-arclength points**, then asks whether their segment penetrates a tiny *Euclidean* central disk. The well-known exact concentric-disk formula for two uniform endpoints on a **circle** supplies an equality benchmark, not the noncircular formula or the universal stability inequality. Related published triangle and rectangle boundary-endpoint interception studies consider **homothetic polygonal cores**, not a Euclidean disk; their target-specific distribution formulas do not supply the present radial square-gradient energy or universal perimeter extremizer. A published Crofton disk-hit law for regular polygons instead uses invariant lines. These distinctions were checked against the substantive full published results, including their assumptions and mathematical claims.

## Limitations
This theorem applies only to centrally symmetric convex planar bodies, to a disk centered at their symmetry center, and to independent uniform-*arclength* boundary endpoints. The strict small-target comparison is pointwise for each fixed noncircular body, not uniform over degenerating shape families. It does not determine the complete intercept distribution at positive disk radii, optimize arbitrary off-center targets, or solve a general multidimensional analogue. The historical originality assessment remains provisional because unindexed or inaccessible older work could contain an equivalent radial identity; independent verification is not performed.

## References
1. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first public 2012-04-12, https://arxiv.org/abs/1204.2707 .
2. H. S. Harutyunyan and V. K. Ohanyan, *The chord length distribution function for regular polygons*, *Advances in Applied Probability* 41 (2009), 358–366, doi:10.1239/aap/1246886615 (invariant random-line model).
3. *A universal crossing law for random chords of rectangles*, publicly indexed mathematical research record (2026), boundary-endpoint sampling with homothetic rectangular cores.
4. *Universal chord-interception law for centroidal cores of triangles*, publicly indexed mathematical research record (2026), boundary-endpoint sampling with homothetic triangular cores.
5. *A strict Crofton line-distance order for every regular polygon*, publicly indexed mathematical research record (2026), motion-invariant random lines conditioned on polygon intersection.
6. P. F. Ehlers and E. G. Enns, *Random secants of a convex body generated by surface randomness*, *Journal of Applied Probability* 18 (1981), 157–166, doi:10.2307/3213176 (abstract inspected, full text unavailable).
7. D. Ren, *Random chord distributions and containment functions*, *Advances in Applied Mathematics* 58 (2014), 1–20, doi:10.1016/j.aam.2014.05.003 (abstract inspected, full text unavailable).

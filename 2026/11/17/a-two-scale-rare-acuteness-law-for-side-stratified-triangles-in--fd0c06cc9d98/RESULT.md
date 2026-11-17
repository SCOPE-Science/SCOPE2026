# A two-scale rare-acuteness law for side-stratified triangles in a collapsing isosceles triangle

## Finding
Let \(T_h\) have vertices \((-1,0)\), \((1,0)\), and \((0,h)\), with \(0<h\le1\). Draw one point independently and uniformly by Euclidean arclength from each of the three distinct sides. Let \(\mathcal A_h\) denote the event that their triangle is strictly acute. Then
\[
\boxed{\Pr(\mathcal A_h)=\left(\frac83\log2-\frac76\right)h^2+o(h^2),\quad h\downarrow0.}
\]
The exact positive coefficient is \(C=\frac83\log2-\frac76\approx0.681725814826521\). Unlike interior-uniform or perimeter-uniform samples of thin rectangles, this side-stratified thin-triangle problem has no leading logarithmic factor.

The theorem also determines the **entire marked rare-configuration law**. Parametrize the sampled points by independent uniform variables \(p\in[-1,1]\), \(q,t\in[0,1]\):
\[
P=(p,0),\quad Q=(q,h(1-q)),\quad R=(-t,h(1-t)),\quad L=q+t.
\]
For \(L>0\), label the endpoint closer horizontally to \(P\) by \(H_h=R\) if \(|p+t|\le|q-p|\), and \(H_h=Q\) otherwise. Define the signed mark
\[
Z_h=\begin{cases}L(p+t)/h^2,&H_h=R,\\L(q-p)/h^2,&H_h=Q.\end{cases}
\]
Conditioned on \(\mathcal A_h\), the joint law \((H_h,q,t,Z_h)\) converges **in total variation** to the probability measure with density in \((q,t,z)\), with respect to counting measure on the label and Lebesgue measure on \((0,1)^2\times\mathbb R\),
\[
\boxed{f_R(q,t,z)=\frac{\mathbf1_{\{-(1-t)(q-t)<z<(1-q)(1-t)\}}}{2C(q+t)},}
\]
\[
\boxed{f_Q(q,t,z)=\frac{\mathbf1_{\{(1-q)(q-t)<z<(1-q)(1-t)\}}}{2C(q+t)}.}
\]
Each label has limiting probability \(1/2\), but the label and the side parameters are generally dependent. The two families correspond to horizontal coincidence with either of the two sloping-side points, on the finer \(h^2\) scale.

## Assumptions and scope
All sampling is independent. Since each side is a straight segment, arclength-uniformity agrees with uniformity of the stated linear side parameter. The probability measure on \((p,q,t)\) is \(\frac12\,dp\,dq\,dt\) on \([-1,1]\times[0,1]^2\). The parent degenerates only through \(h\downarrow0\), with its fixed horizontal base \([-1,1]\). Strict acuteness requires the three distinct sampled vertices and each of their three inner products at the sampled vertices to be positive; right and coincident configurations have measure zero. The normalization \(h^2\), labels and signed marks are part of the assertion. Convergence is for the complete marked probability measures, not solely their scalar marginals.

## Proof
**1. Exact inequalities.** Put \(a=(1-q)(1-t)\) and \(L=q+t\). Taking the dot products at \(P,Q,R\), respectively, gives the following **necessary and sufficient** system when \(L>0\):
\[
(q-p)(p+t)<h^2a,\qquad
L(q-p)>h^2(1-q)(q-t),\qquad
L(p+t)>-h^2(1-t)(q-t).
\tag{1}
\]
The second and third inequalities bound \(p\) by
\[
-t-\frac{h^2(1-t)(q-t)}{L}<p<q-\frac{h^2(1-q)(q-t)}{L}.
\tag{2}
\]
All probability statements follow by integrating the allowed length of this interval after imposing the first inequality.

**2. Pointwise localization at fixed side parameters.** Fix \(q,t\in(0,1)\), so \(L>0\). As \(h\downarrow0\), the first inequality in (1) excludes any fixed compact subinterval of \((-t,q)\). Thus allowed \(p\) values form two disjoint strips of length \(O(h^2)\) around \(-t\) and \(q\). Their exact scaled limits follow by substitution into (1).

Near \(-t\), write \(p=-t+h^2z/L\). The conditions at \(P\) and \(R\) tend to
\[
 z<(1-q)(1-t),\qquad z>-(1-t)(q-t).
\]
The condition at \(Q\) is automatically satisfied for small \(h\). The length in the rescaled \(z\)-coordinate is \((1-t)^2\), so this strip contributes \(h^2(1-t)^2/L+o(h^2)\) to the allowed \(p\)-length.

Near \(q\), write \(p=q-h^2z/L\). The limiting conditions at \(P\) and \(Q\) are
\[
 z<(1-q)(1-t),\qquad z>(1-q)(q-t),
\]
and the condition at \(R\) is automatic. This strip contributes \(h^2(1-q)^2/L+o(h^2)\). Both interval lengths are nonnegative and vanish only on parameter-null boundaries.

**3. Uniform integrable domination.** Let \(m_h(q,t)\) denote the total favorable \(p\)-length. From (2), the part of the allowed interval outside \([-t,q]\) has length at most \(2h^2/L\) (using \(|q-t|\le L\)); inside \([-t,q]\), the first inequality in (1) and \(\max\{q-p,p+t\}\ge L/2\) imply \(\min\{q-p,p+t\}<2h^2a/L\). Thus, uniformly for \(0<h\le1\),
\[
 0\le \frac{m_h(q,t)}{h^2}\le\frac{2+4a}{L}\le\frac6{q+t}.
\tag{3}
\]
The majorant is integrable over \((0,1)^2\). Dominated convergence therefore yields
\[
\lim_{h\downarrow0}\frac{\Pr(\mathcal A_h)}{h^2}
=\frac12\int_0^1\int_0^1\frac{(1-t)^2+(1-q)^2}{q+t}\,dq\,dt.
\]
Symmetry and elementary integration reduce this to
\[
C=\int_0^1(1-x)^2\log\frac{1+x}{x}\,dx
=\frac83\log2-\frac76.
\]
This proves the first formula and positivity.

**4. Total-variation convergence of the marked law.** For each fixed \((q,t)\) with \(L>0\), the two strip parametrizations above have Jacobian \(dp=h^2\,dz/L\). After division by \(h^2\), their densities with respect to \(dq\,dt\,dz\) tend almost everywhere to \(\frac1{2L}\) times the two stated limiting interval indicators. On the acute event, inequalities (1)–(2) and the fact that the chosen label is the nearer of the two endpoints imply \(|Z_h|\le4\), for \(0<h\le1\). Thus the unnormalized densities vanish outside a common compact \(z\)-interval and are dominated by \(\mathbf1_{\{|z|\le4\}}/(2(q+t))\), integrable over all three continuous variables. Dominated convergence gives convergence in \(L^1\) of the unnormalized marked measures. Step 3 shows their total masses converge to \(C\), proving convergence in total variation after conditioning. Integrating the limiting \(z\)-intervals gives each label mass \(\frac1{2C}\int(1-t)^2/(q+t)\,dq\,dt=1/2\), by symmetry. \(\square\)

## Verification
The standalone `check.py` implements the **exact** finite-\(h\) interval endpoints from (2), intersected with the outer intervals from the quadratic inequality in (1). It compares the resulting favorable lengths with an independent direct three-dot-product mesh test for eighteen configurations, verifies the coefficient both analytically and by numerical quadrature, and integrates exact favorable lengths over a seeded \(2^{20}\)-point Sobol sample at three heights. It reports `ALL_ANGLE_INTERSECTION_CHECK_OK`, `LIMIT_INTEGRAL_CHECK_OK`, and `THIN_TRIANGLE_ACUTENESS_DIAGNOSTICS_OK`. The rescaled probabilities approach \(0.6817258148\) as predicted. These computations are diagnostics; the proof of all-parameter asymptotics and total-variation convergence is analytic.

## Relationship to prior work
Edelman and Strang's 2015 review of random triangle theory develops the Gaussian and hemisphere-uniform shape model, including an acute probability of \(1/4\) for that model. It does not establish the law for one arclength-uniform point on each side of a degenerating parent triangle. A 2015 public geometry problem uses the same one-per-side sampling design for an *equilateral* parent but asks for an area tail rather than acuteness or a collapsing-height asymptotic.

A publicly available 2026 equilateral-perimeter acuteness theorem gives a known one-per-side contribution at a *single equilateral shape*; it does not imply the present non-equilateral limit or the marked rare-configuration distribution. Separately, two-dimensional interior-uniform sampling of a thin convex body and full-perimeter sampling of a thin rectangle produce \(h^2\log(1/h)\)-type acuteness laws; their measures and shapes differ, and none of their scalings or constants imply the present two-strip law. The exact comparisons and remaining historical-priority risks are detailed in `AUDIT.json`.

## Limitations
The result holds for this degenerating **isosceles** host family, one point per **specified** side, and the Euclidean strict-acute event. It does not provide a finite-height elementary closed form, an error term stronger than \(o(h^2)\), a non-isosceles universality theorem, or independent historical certification. The limiting density does not imply independence between the rare-configuration label and the side parameters. Some relevant historical literature may be unindexed; independent mathematical and bibliographic review remains outstanding.

## References
1. A. Edelman and G. Strang, *Random Triangle Theory with Geometry and Applications*, arXiv:1501.03053, submitted January 9, 2015. https://arxiv.org/abs/1501.03053
2. H. Ghaffari et al., *Three points on sides of equilateral triangle*, Mathematics Stack Exchange discussion, posted April 29, 2015. https://math.stackexchange.com/questions/1258210/three-points-on-sides-of-equilateral-triangle
3. *Exact acute-triangle probability for independent uniform perimeter points of an equilateral triangle*, public geometric-probability research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-acute-triangle-probability-for-independent-uniform-perimet--bacc607a9136
4. *A logarithmic acute-triangle law for the boundary of a thin rectangle*, public geometric-probability research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-logarithmic-acute-triangle-law-for-the-boundary-of-a-thin-rect--f2b630dbf4b1
5. *Fifth-chord-moment law for acute triangles in thin convex bodies*, public geometric-probability research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-fifth-chord-moment-law-for-acute-triangles-in-thin-convex-bodies--6f181af2eba0

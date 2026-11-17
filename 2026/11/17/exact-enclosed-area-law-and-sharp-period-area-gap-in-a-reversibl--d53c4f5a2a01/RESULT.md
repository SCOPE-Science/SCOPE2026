# Exact enclosed-area law and sharp period–area gap in a reversible two-zone focus center

## Finding

A reversible two-zone piecewise-affine center admits an exact formula for the **Euclidean area enclosed by each crossing cycle**, expressed directly through its two switching velocities. This produces a sharp period-versus-area law that is not a consequence of the known existence criterion or the previously calculated period-versus-crossing-speed law alone.

Fix \(a,t,d>0\) with \(4d>t^2\). On either open half-plane define
\[
(\dot x,\dot y)=
\begin{cases}
(tx-y,\;dx+a),&x<0,\\
(-tx-y,\;dx-a),&x>0.
\end{cases}
\]
At transverse points of \(x=0\), take the continuous normal component \(\dot x=-y\). Write
\[
\omega=\sqrt{d-t^2/4},\qquad c=\frac{t}{2\omega},\qquad p=\frac ad.
\]
There is a unique \(\theta_0\in(\pi,2\pi)\) satisfying
\[
\cos\theta_0-e^{-c\theta_0}=c\sin\theta_0.
\]
For each \(\theta\in(\pi,\theta_0)\), define the upper switching velocity \(v>0\), lower switching velocity \(w<0\), enclosed Euclidean area \(\mathcal A\), and least period \(T\) by
\[
\begin{aligned}
v(\theta)&=p\omega\left(\frac{\cos\theta-e^{-c\theta}}{\sin\theta}-c\right),\\
w(\theta)&=p\omega\left(\frac{e^{c\theta}-\cos\theta}{\sin\theta}-c\right),\\
T(\theta)&=\frac{2\theta}{\omega},\\
\mathcal A(\theta)&=\boxed{\frac{w(\theta)^2-v(\theta)^2}{t}}\\
&=\frac{4p^2\omega^2}{t}\frac{\cosh(c\theta)-\cos\theta}{\sin\theta}
\left(\frac{\sinh(c\theta)}{\sin\theta}-c\right).
\end{aligned}
\]
For every \(v>0\), precisely one of these cycles passes through \((0,v)\). Their Euclidean areas increase strictly from a positive finite limit \(\mathcal A_{\min}=w(\theta_0)^2/t\) to infinity as \(v\) grows; their physical periods decrease strictly from \(2\theta_0/\omega\) to \(2\pi/\omega\). In particular, area is a global coordinate on this crossing-cycle annulus.

The **sharp period–area edge law** is
\[
\boxed{
\lim_{\mathcal A\to\infty}
\left(T-\frac{2\pi}{\omega}\right)\sqrt{\mathcal A}
=\frac{2a}{d}(1+e^{-\pi c})
\sqrt{\frac{e^{2\pi c}-1}{t}}.}
\]
The limit is taken with the three coefficients fixed; its right side is strictly positive. No statement is made about trajectories that do not belong to the specified crossing-cycle family.

## Assumptions and scope

The coefficient conditions are exactly \(a>0\), \(t>0\), and \(d>t^2/4\). We consider only cycles with one transverse crossing at \((0,v)\), \(v>0\), and one at \((0,w)\), \(w<0\). Every such crossing is unambiguous, since the normal velocities from both sides agree and are nonzero. The switching point \((0,0)\) is not a transverse point; any Filippov selection there is outside the assertion. The enclosed area is ordinary Cartesian Lebesgue area in the displayed coordinates, and periods are measured in original, unscaled physical time. Coefficients are not simultaneously rescaled when taking the high-area limit.

## Proof

**1. First-return parametrization.** On the left put \(u=-x\). The original field implies
\[
u''-tu'+du=a,\qquad u(0)=0,\qquad u'(0)=v.
\]
With \(g(s)=e^{ts/2}\sin(\omega s)/\omega\) and \(W(s)=\int_0^s g(z)\,dz\), variation of constants gives \(u(s)=vg(s)+aW(s)\). Direct integration yields
\[
W(s)=\frac{1+e^{ts/2}\bigl(c\sin(\omega s)-\cos(\omega s)\bigr)}d.
\]
On \(0<s<\pi/\omega\), \(g,W>0\), so no return is possible. For \(\theta=\omega s\in(\pi,2\pi)\), the equation \(u(s)=0\) is exactly \(v=v(\theta)\) as displayed in the finding. Define \(h(\theta)=(\cos\theta-e^{-c\theta})/\sin\theta-c\). Then
\[
h'(\theta)=\frac{-1+e^{-c\theta}(\cos\theta+c\sin\theta)}{\sin^2\theta}<0,
\qquad \pi<\theta<2\pi.
\]
Indeed the numerator's exponential term has derivative \(-(1+c^2)e^{-c\theta}\sin\theta>0\) and increases to \(e^{-2\pi c}<1\). As \(\theta\downarrow\pi\), \(v(\theta)\to+\infty\); as \(\theta\uparrow2\pi\), \(v(\theta)\to-\infty\). Hence the unique zero \(\theta_0\) exists, and \(v:(\pi,\theta_0)\to(0,\infty)\) is a decreasing bijection. If \(\pi<\omega s<\theta\), then \(g(s)<0\) and \(v(\omega s)>v(\theta)\), implying \(u(s)=g(s)[v-v(\omega s)]>0\). Thus this root is the first return and the left excursion stays in \(x<0\).

**2. Exact closure and crossing velocities.** Differentiating \(u\) at \(s=\theta/\omega\) shows \(\dot x=-w>0\), where \(w(\theta)\) is the stated negative expression; the two crossings are transverse. The reflection \(R(x,y)=(-x,y)\) satisfies \(R F(z)=-F(Rz)\) whenever \(z\) and \(Rz\) lie in opposite half-planes. Therefore reflecting the left trajectory and reversing time supplies a right excursion from \((0,w)\) back to \((0,v)\), without any intermediate crossing. This gives one simple closed orbit and its least period \(T=2\theta/\omega\). All possible upper-section crossing cycles are exhausted because their left first-return must satisfy the derived equation.

**3. Area-to-energy identity.** The closed orbit is positively oriented: it travels from its upper switching point through the left half-plane to its lower switching point, then back through the right half-plane. Green's theorem and reflected symmetry give
\[
\mathcal A=\oint x\,dy=2\int_0^{\theta/\omega}x(s)\bigl(dx(s)+a\bigr)\,ds.
\]
The left second-order equation is \(x''-tx'+dx=-a\), hence \(dx+a=tx'-x''\). Integrating by parts, with \(x\) vanishing at both switching times, gives
\[
\mathcal A=2\int_0^{\theta/\omega}(x'(s))^2\,ds.
\]
For the energy-like quantity \(H=(x'^2+dx^2)/2+ax\), the exact identity \(H'=t(x')^2\) holds on the left excursion. Its endpoint values are \(H(0)=v^2/2\) and \(H(\theta/\omega)=w^2/2\). Substitution proves \(\mathcal A=(w^2-v^2)/t\). Elementary algebra using the formulas for \(v,w\) produces the displayed hyperbolic-trigonometric area formula.

**4. Strict area ordering and endpoint geometry.** Smooth uniqueness away from \((0,0)\) makes two distinct transverse crossing cycles disjoint Jordan curves. The left-section half-return has derivative \(dw/dv=e^{t\theta/\omega}v/w<0\): this follows from the planar variational determinant and the common normal crossing velocity \(\dot x=-y\) at both endpoints. Consequently if \(v_1<v_2\), then \(w(v_1)>w(v_2)\); their switching intervals are strictly nested. The disjoint Jordan interiors are nested as well, so area grows strictly with \(v\). The limit \(v\downarrow0\) corresponds to \(\theta\uparrow\theta_0\), and has \(\mathcal A\to w(\theta_0)^2/t>0\): it is a nontransverse inner boundary, not a zero-area small circle. The limit \(v\uparrow\infty\) corresponds to \(\theta\downarrow\pi\), and the formulas below force \(\mathcal A\to\infty\). The period decreases strictly because \(T\) increases with \(\theta\), while \(v\) decreases with \(\theta\).

**5. Sharp area–period asymptotic.** Put \(\delta=\theta-\pi\downarrow0\). From the exact formulas,
\[
\delta\,v\longrightarrow p\omega(1+e^{-\pi c}),\qquad
\frac{w}{v}\longrightarrow-e^{\pi c}.
\]
Thus
\[
\mathcal A\sim\frac{e^{2\pi c}-1}{t}\,v^2,
\qquad
T-\frac{2\pi}{\omega}=\frac{2\delta}{\omega}
\sim\frac{2p(1+e^{-\pi c})}{v}.
\]
Multiplying the latter two asymptotics yields the claimed positive limit. These are asymptotic analytic identities, not extrapolations from sampled orbits.

## Verification

The companion `verify.py` checks the exact switching-time, velocity, hyperbolic area, Green-integral and high-area expressions for three nondegenerate parameter triples and multiple crossing speeds, using only the Python standard library. Execution prints `CROSSING_AREA_AND_PERIOD_EDGE_CHECK_OK`. These finite numerical checks support arithmetic reproducibility; the preceding proof establishes every asserted continuum and asymptotic statement.

## Relationship to prior work

Carmona, Fernández-Sánchez and Novaes [1,2] proved necessary and sufficient conditions for crossing period annuli in two-zone affine planar systems. Their full open-access article gives canonical forms and Poincaré half-map integral characterizations; the existence of this balanced family is covered by that literature and is **not** a new criterion. A published note [3] addresses five spectral endpoint laws for the **original-time period versus section speed** in a related balanced two-zone family, including elementary focus-flight expressions. The focus period calculation in this result is not independently claimed as new. The result here is the Euclidean **enclosed-area identity**, its explicit nonzero inner area endpoint, global area parametrization, and the resulting sharp period correction with respect to **enclosed area**, a distinct geometric invariant that is not determined by the period as a function of speed alone without computing the orbit shape or its area. A 2026 paper [4] treats the critical-period count of general two-zone annuli; its abstract does not state an area law, but its inaccessible full text remains a publication-priority risk.

## Limitations

The area formula and asymptotics hold only for the displayed reversible focus-focus family with \(t>0\) and its specified transverse crossing family. The nontransverse inner boundary is a limit and is not asserted to be a uniquely defined Filippov orbit. No description is given of basins of either affine focus or the full nonsmooth global phase portrait. A stronger or equivalent unindexed area calculation may predate this finding, especially within full texts not accessible for inspection. There has been no independent mathematical audit.

## References

[1] V. Carmona, F. Fernández-Sánchez, and D. D. Novaes, *A succinct characterization of period annuli in planar piecewise linear differential systems with a straight line of nonsmoothness*, arXiv:2212.09063, first public version 18 December 2022, https://arxiv.org/abs/2212.09063.

[2] Same authors, *Journal of Nonlinear Science* **33**, article 88 (2023), DOI 10.1007/s00332-023-09947-5; complete open-access article inspected at https://link.springer.com/article/10.1007/s00332-023-09947-5.

[3] *Five spectral edge laws for a two-zone crossing period annulus*, 11 October 2026, public mathematical result and proof, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-five-spectral-edge-laws-for-a-two-zone-crossing-period-annulus--95dca04b66d6/RESULT.md.

[4] H. Liu, C. Liu and S. Wang, *The crossing period annulus and critical periods for the planar piecewise linear systems with a straight line of separation*, *Journal of Nonlinear Science* **36**, article 51 (2026), DOI 10.1007/s00332-026-10269-5; abstract inspected, full text inaccessible.

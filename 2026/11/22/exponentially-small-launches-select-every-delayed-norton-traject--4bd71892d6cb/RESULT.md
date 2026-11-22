# Exponentially small launches select every delayed Norton trajectory in the finite-sphere limit

## Finding

Fix finite \(a>1\) and \(c,g>0\). On the generalized Norton dome, consider a frictionless homogeneous rigid sphere of radius \(\rho>0\) placed at the apex with a positive outward center speed, with no spin. For sufficiently small fixed contact arclength \(\varepsilon>0\), define
\[
 b_\rho=\left(\frac{\rho c}{g}\right)^{a/(a-1)},\qquad
 v_\rho^*=b_\rho\sqrt{\frac g\rho},\qquad 0<\eta\le1.
\]
Let \(t_\rho(\varepsilon;v)\) denote the first time the point of contact reaches \(r=\varepsilon\) when the initial outward center speed is \(v\). Then, uniformly in all \(0<\eta\le1\),
\[
 \boxed{\ t_\rho(\varepsilon;v_\rho^*\eta)
 =\frac{2a}{a-1}\sqrt{\frac{a+1}{2ac}}\,\varepsilon^{(a-1)/(2a)}
 +\sqrt{\frac\rho g}\log\frac1\eta
 +O_{a,c,g,\varepsilon}\!\left(\sqrt{\frac\rho g}\right).\ }
\]
In particular, if \(\sqrt{\rho/g}\log(1/\eta_\rho)\to T\in[0,\infty]\), the outward contact trajectories converge uniformly on each compact time interval, stopped at \(r=\varepsilon\), to
\[
 r_T(t)=\begin{cases}
 0,&0\le t\le T,\\
 \displaystyle \left[\frac{c(a-1)^2}{2a(a+1)}\right]^{a/(a-1)}(t-T)^{2a/(a-1)},&t>T,
 \end{cases}
\]
with the convention \(r_\infty\equiv0\). Every such finite delay can be selected by \(\eta_\rho=\exp[-T\sqrt{g/\rho}]\). All corresponding finite-sphere initial velocities tend to zero. Conversely, when \(\sqrt{\rho/g}\log(1/\eta_\rho)\to0\), the selected solution has no delay. Thus a universal exponential launch-velocity scale, rather than the mere presence of positive sphere radius, distinguishes every finite waiting-time branch in the singular limit.

## Assumptions and scope

The dome is parameterized locally by its meridional contact arclength \(r\) and vertical descent
\[
 h_a(r)=\frac{ac}{(a+1)g}r^{(a+1)/a},\quad
 \sin\theta(r)=\frac cg r^{1/a},\quad
 0\le r< (g/c)^a.
\]
The radius-\(\rho\) sphere moves along a fixed meridian without rolling or spin. The frictionless normal force acts through its center; initial motion is outward. The center arclength and its vertical drop are exactly
\[
 q_\rho(r)=r+\rho\arcsin\!\left(\frac cg r^{1/a}\right),\quad
 H_\rho(r)=h_a(r)+\rho\left(1-\sqrt{1-\frac{c^2}{g^2}r^{2/a}}\right).
\]
The curvature of the support is
\[
 \kappa_a(r)=\frac{c}{ag}\frac{r^{1/a-1}}{\sqrt{1-(c/g)^2r^{2/a}}},\qquad
 q'_\rho(r)=1+\rho\kappa_a(r).
\]
For any positive initial center speed \(v\), energy conservation and outward monotonicity yield the exact first-passage integral
\[
 t_\rho(\varepsilon;v)=\int_0^\varepsilon
 \frac{1+\rho\kappa_a(r)}{\sqrt{v^2+2gH_\rho(r)}}\,dr.
\]
All statements are local to a sufficiently small fixed \(\varepsilon\); one can choose it so the normal reaction stays strictly compressive for every sufficiently small \(\rho\) and all \(0<\eta\le1\). All limits are at fixed \(a,c,g,\varepsilon\); uniformity is asserted in \(\eta\), not in \(a\) or \(\varepsilon\).

## Proof

**Step 1 (the inner scale).** Set \(b=b_\rho\) and \(s=b/\rho\). Because \(a>1\), \(s\to0\), and \((c/g)b^{1/a}=s\). For \(r=by\) with \(0\le y\le1\), define
\[
 Q_s(y)=\frac{q_\rho(by)}b=y+\frac1s\arcsin(sy^{1/a}),
\]
\[
 F_s(y)=\frac{2\rho H_\rho(by)}{b^2}
 =\frac{2a}{a+1}y^{(a+1)/a}+
 \frac{2y^{2/a}}{1+\sqrt{1-s^2y^{2/a}}}.
\]
Substituting \(v=v_\rho^*\eta\), and using \(q'_\rho(by)=Q_s'(y)\), gives the exact identity
\[
 t_\rho(b;v_\rho^*\eta)
 =\sqrt{\frac\rho g}\int_0^1\frac{Q_s'(y)}{\sqrt{\eta^2+F_s(y)}}\,dy.
\]
For \(0<s\le1/2\), elementary bounds for \(\arcsin z\) and \(1-\sqrt{1-z^2}\) on \([0,1/2]\) give, with constants depending on \(a\),
\[
 C^{-1}y^{1/a}\le Q_s(y)\le Cy^{1/a},\quad
 F_s(y)\ge C^{-1}Q_s(y)^2,\quad
 \frac{Q_s'(y)}{Q_s(y)}\le\frac Cy,
\]
and the comparison bound
\[
 \frac{|F_s(y)-Q_s(y)^2|}{Q_s(y)^2}
 \le C\left(y^{(a-1)/a}+s^2y^{2/a}\right).
\]
Indeed \(Q_s=y+y^{1/a}+O(s^2y^{3/a})\) and \(F_s=y^{2/a}+[2a/(a+1)]y^{(a+1)/a}+O(s^2y^{4/a})\), with uniformly bounded remainders; the cross term \(2y^{1+1/a}\) in \(Q_s^2\) gives the stated first error. The difference-of-reciprocals identity and the positive lower bound for \(F_s\) imply
\[
 \left|\frac{Q'_s}{\sqrt{\eta^2+F_s}}-
 \frac{Q'_s}{\sqrt{\eta^2+Q_s^2}}\right|
 \le C\frac{y^{(a-1)/a}+s^2y^{2/a}}{y}.
\]
This majorant is integrable at zero precisely because \(a>1\), with an integral bounded uniformly in \(0<\eta\le1\). The reference integral is exact:
\[
 \int_0^1\frac{Q_s'(y)}{\sqrt{\eta^2+Q_s(y)^2}}\,dy
 =\operatorname{arsinh}\!\left(\frac{Q_s(1)}\eta\right)
 =\log\frac1\eta+O(1),
\]
where \(Q_s(1)\) is bounded above and below away from zero. Therefore
\[
 t_\rho(b;v_\rho^*\eta)
 =\sqrt{\frac\rho g}\log\frac1\eta+O\!\left(\sqrt{\frac\rho g}\right)
\]
uniformly in \(\eta\).

**Step 2 (the outer scale).** Write
\[
 I_0(r)=\frac1{\sqrt{2gh_a(r)}}
 =\sqrt{\frac{a+1}{2ac}}\,r^{-(a+1)/(2a)}.
\]
For \(b\le r\le\varepsilon\), and \(\varepsilon\) sufficiently small, the exact geometry yields
\[
 \rho\kappa_a(r)\le C\rho r^{1/a-1},\quad
 \frac{H_\rho(r)-h_a(r)}{h_a(r)}\le C\rho r^{1/a-1},\quad
 \frac{(v_\rho^*\eta)^2}{2gh_a(r)}\le C\left(\frac br\right)^{(a+1)/a}
 \le C\rho r^{1/a-1}.
\]
The last inequality uses \(b^{(a-1)/a}=\rho c/g\) and \(b/r\le1\). The inverse-square-root Lipschitz bound on the nonnegative perturbations to the energy denominator then gives
\[
 \left|\frac{1+\rho\kappa_a(r)}{\sqrt{(v_\rho^*\eta)^2+2gH_\rho(r)}}-I_0(r)\right|
 \le C\rho\,r^{(1-3a)/(2a)}.
\]
Because \(a>1\), its integral over \([b,\varepsilon]\) is bounded by \(C\rho b^{-(a-1)/(2a)}=O(\sqrt{\rho/g})\), with fixed-dimensional constants. Moreover,
\[
 \int_0^b I_0(r)\,dr=O\left(b^{(a-1)/(2a)}\right)=O\!\left(\sqrt{\rho/g}\right).
\]
Adding the two intervals and evaluating \(\int_0^\varepsilon I_0\) proves the boxed uniform estimate.

**Step 3 (limit trajectories).** For every fixed \(x\in(0,\varepsilon]\), the same proof, with \(\varepsilon\) replaced by \(x\), gives
\[
 t_\rho(x;v_\rho^*\eta_\rho)=T_\rho+
 \frac{2a}{a-1}\sqrt{\frac{a+1}{2ac}}x^{(a-1)/(2a)}+o(1),
 \quad T_\rho=\sqrt{\rho/g}\log(1/\eta_\rho).
\]
Every travel-time map is continuous and strictly increasing in \(x\); convergence of such inverse functions at positive interior levels and continuity of the limiting trajectory prove convergence on compact time intervals after clipping at \(\varepsilon\). At the initial zero plateau, monotonicity bounds the finite-sphere trajectory by arbitrarily small levels until the limiting departure time, yielding uniform convergence there as well. For \(T_\rho\to\infty\), every positive-level hitting time tends to infinity, forcing the stationary limit. Because \(v_\rho^*=b\sqrt{g/\rho}\to0\), every allowed launch velocity tends to zero.

**Step 4 (contact admissibility).** The center-path curvature is \(\kappa_q=\kappa_a/(1+\rho\kappa_a)\le1/\rho\). The inward normal reaction has the exact form
\[
 N/m=g\cos\theta-\bigl(v^2+2gH_\rho\bigr)\kappa_q.
\]
For \(0<r\le\varepsilon\), \(H_\rho(r)\kappa_q(r)\le C r^{2/a}+o_\rho(1)\) uniformly (split at \(b\), or bound the terms using \(\rho\kappa_q\le1\) and the explicit height). Also \(v^2\kappa_q\le(v_\rho^*)^2/\rho=g(b/\rho)^2\to0\). Thus choosing \(\varepsilon\) small, then \(\rho\) small, ensures \(N>mg/2\) on the entire trajectory before \(r=\varepsilon\). This verifies the frictionless contact solution remains physically admissible within the stated scope.

## Verification

The standalone `checker.py` uses only the Python standard library and recomputes the exact finite-radius energy integral via a logarithmic coordinate and Simpson quadrature, independently of the asymptotic algebra. It tests the three exponents \(a\in\{1.5,2,3\}\), two delays, three small radii, geometric derivative identities and sample positive normal reactions. Run `python3 checker.py`; its expected output is `PASS: 174 finite-parameter assertions; independent proof in RESULT.md`. These finite checks do not prove uniformity for all positive \(\eta\), infinite-dimensional parameter ranges or the singular limit: Steps 1–4 provide those proofs.

## Relationship to prior work

Chen and Kuo (arXiv:2611.16797v1, first public 2026-11-12), Sections 3 and 7, derive the generalized point-particle equation, the finite-sphere offset geometry and the divergence of travel time from exact rest for every fixed radius; these are used here and are **not** claimed as new. Their theorem concerns exact rest and explicitly separates uniqueness from perturbation stability. The present result adds a uniform two-parameter, positive-velocity travel-time estimate and shows how every delayed point-particle solution is recovered by a radius-dependent launch speed.

General studies of selection under regularization, including Eyink and Bandak (arXiv:2007.01333), concern different stochastic/regularized dynamics. Vanpoucke and Wenmackers (Chaos 31, 123131, 2021) analyze a hyperfinite-grid initial-data model of the point-particle nonuniqueness and assign a prior-dependent probability to immediate departure; their full text does not analyze finite-radius sphere geometry. Fletcher's work on minimal approximations to Norton's dome concerns physical-model approximation and represents a related comparison, but its full text could not be inspected here; priority under implicit reductions remains uncertain. No claim of absolute uniqueness in the literature is made.

## Limitations

Only outward, frictionless, nonspinning spheres on the specified generalized meridian, with \(a>1\), are covered. There is no claim for rolling spheres, arbitrary rigid shapes, random perturbations, globally continued trajectories, or universal uniformity in exponent, dome scale or observation distance. The threshold is for the initial center speed, scaled by \(v_\rho^*\), at the exact apex. The result does not assign a probability law to waiting times; it identifies deterministic selections. An equivalent result implicit in general singular-regularization literature could affect publication priority. Independent validation has not been performed.

## References

1. Guan-Chuan Chen and En-Jui Kuo, *Finite Bodies on Norton's Dome: Escape-Time Divergence and a Center-of-Mass Barrier Theorem*, arXiv:2611.16797v1, submitted 2026-11-12, https://arxiv.org/abs/2611.16797 (Sections 3 and 7, especially equations (35)–(55)).
2. Gregory L. Eyink and Daniel Bandak, *A Renormalization Group Approach to Spontaneous Stochasticity*, arXiv:2007.01333, https://arxiv.org/abs/2007.01333 (different regularized dynamics).
3. Danny E. P. Vanpoucke and Sylvia Wenmackers, *Assigning probabilities to non-Lipschitz mechanical systems*, Chaos 31 (2021) 123131, https://doi.org/10.1063/5.0063388 (finite-difference and phase-space probability treatment).
4. Samuel C. Fletcher, *Minimal Approximations and Norton's Dome*, published philosophical analysis (full text not available for comparison); see also related discussion of model approximation in the literature cited by Chen and Kuo.

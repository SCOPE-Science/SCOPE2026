# A sharp balanced-clock optimum and pre-contact angular arrest for three equilateral quartic cycles

## Finding
Fix a unit equilateral triangle with three pairwise exterior circles of common radius \(r\). For all degree-at-most-four planar polynomial vector fields preserving these circles and whose angular-gradient scale satisfies \(\kappa\sqrt3/2=1\), require all three circles to be **counterclockwise regular periodic trajectories**. This requirement is feasible exactly when \(0<r<r_c=1/(2\sqrt3)\). In that range the largest of their three actual physical-time periods has a **unique minimizer** in the entire normal-form family, at \(\lambda=\mu=-2/3\). The three periods coincide there, with exact value
\[
T_*(r)=3\int_{-\pi}^{\pi}\frac{dt}{(1-2\sqrt3r\cos t)[1-2r\cos(t+\pi/6)][1-2r\cos(t-\pi/6)]}.
\]
The sharp angular-arrest law is
\[
\lim_{r\uparrow r_c}\sqrt{r_c-r}\,T_*(r)=\frac{12\pi}{3^{1/4}}.
\]
This arrest precedes geometric circle contact at \(r=1/2\). At the unique optimal field the three trajectories are nonhyperbolic, whereas for each fixed subcritical \(r\) there exist hyperbolic triples arbitrarily close to the optimum, but none attains it. The same \(T_*(r)\) is therefore a strict, unattained infimum when all three circles are required to be hyperbolic.

## Assumptions and scope
Write \(v=\sqrt3/2\), \(C_1=(0,0)\), \(C_2=(1,0)\), \(C_3=(1/2,v)\), \(0<r<1/2\), and \(f_i(x,y)=|(x,y)-C_i|^2-r^2\). The complete degree-at-most-four normal form preserving these circles, due to Cao and Llibre, is
\[
\begin{aligned}
\dot x&=-yA_1f_2f_3-yA_2f_1f_3-(y-v)A_3f_1f_2,\\
\dot y&=xA_1f_2f_3+(x-1)A_2f_1f_3+(x-1/2)A_3f_1f_2,\\
A_1&=-\lambda-\mu+\kappa(-vx-y/2-v),\\
A_2&=\lambda+\kappa(vx-y/2),\qquad A_3=\mu+\kappa y.
\end{aligned}
\]
We fix \(\kappa=1/v=2/\sqrt3\), which fixes the angular-variation time scale and avoids unconstrained common rescaling of the flow. The two remaining unrestricted real coefficients are \(\lambda,\mu\). We compare **least positive physical-time periods**, not rotation numbers or time-reparametrized periods. No global attractor or absence of other periodic orbits is assumed.

## Proof
**1. Exact angular equations and a conserved speed budget.** On the circle centered at \(C_i\), the other two circle-polynomials are strictly positive, and the normal form gives \(\dot\theta_i=A_i\prod_{j\ne i}f_j\). Define
\[
\omega_1=-\lambda-\mu-1,\quad \omega_2=\lambda+1,\quad \omega_3=\mu+1.
\]
Their sum is **exactly one**. The gradient of \(A_i\) has length \(\kappa\), and on each circle \(A_i\) is a sinusoid with mean \(\omega_i\) and amplitude \(\kappa r=2r/\sqrt3\). Therefore three counterclockwise regular cycles exist exactly when
\[
\omega_i>2r/\sqrt3\quad(i=1,2,3),\qquad \omega_1+\omega_2+\omega_3=1.
\]
A positive triple satisfying these inequalities exists if and only if \(2\sqrt3 r<1\). For \(r_c\le r<1/2\), the circles remain strictly disjoint, but the requisite angular inequalities cannot all hold. This is an angular feasibility transition, not geometric tangency.

**2. A single strictly decreasing clock function.** Symmetry under the three rotations of the equilateral triangle turns each circle's positive-time integral, after an angular shift, into
\[
T_i=F_r(\omega_i),\qquad F_r(w)=\int_{-\pi}^{\pi}\frac{dt}{(w-2r\cos(t)/\sqrt3)[1-2r\cos(t+\pi/6)][1-2r\cos(t-\pi/6)]}.
\]
The two bracketed power factors are bounded below by \(1-2r>0\). For \(w>2r/\sqrt3\), differentiation under the integral gives
\[
F'_r(w)=-\int_{-\pi}^{\pi}\frac{dt}{(w-2r\cos t/\sqrt3)^2[1-2r\cos(t+\pi/6)][1-2r\cos(t-\pi/6)]}<0.
\]
Hence \(\max_i T_i=F_r(\min_i\omega_i)\). The fixed sum gives \(\min_i\omega_i\le1/3\), with equality only if all three equal \(1/3\). This proves sharpness and uniqueness. The linear relations defining the \(\omega_i\) then give precisely \(\lambda=\mu=-2/3\), and substitution into the quadrature yields the stated formula for \(T_*(r)\).

**3. Sharp angular-arrest constant.** Let \(d=r_c-r\) and \(\varepsilon=2\sqrt3d\). At the optimal parameters the vanishing angular factor becomes
\[
1-2\sqrt3r\cos t=\varepsilon+(1-\varepsilon)(1-\cos t).
\]
The two other factors stay strictly positive and converge, at \(t=0\), to \(1/2\) each. Thus the integrand has the local principal part \(12/(\varepsilon+t^2/2)\). Split the integral at a small fixed angular neighborhood, set \(t=\sqrt{2\varepsilon}\,z\), and dominate the rescaled integrand by a constant multiple of \((1+z^2)^{-1}\). Its complement is uniformly bounded and negligible after multiplication by \(\sqrt d\). Since \(\int_{\mathbb R}(1+z^2)^{-1}dz=\pi\),
\[
T_*(r)\sim12\pi\sqrt{2/\varepsilon}=\frac{12\pi}{3^{1/4}}d^{-1/2}.
\]
This proves the exact coefficient, not just the blow-up exponent.

**4. The optimal clock lies on a nonhyperbolic boundary.** The already-published equilateral Floquet specialization expresses the three transverse logarithmic multipliers as nonzero positive factors times \(\omega_3-\omega_2\), \(\omega_1-\omega_3\), and \(\omega_2-\omega_1\), respectively, whenever the three angular means are positive and \(\kappa>0\). At the unique balanced minimizer all three differences vanish, so all three multipliers equal one. For any fixed \(r<r_c\), let \(\lambda=-2/3+\eta\), \(\mu=-2/3\), with \(0<\eta<1/3-2r/\sqrt3\). Then \((\omega_1,\omega_2,\omega_3)=(1/3-\eta,1/3+\eta,1/3)\), and the three pairwise differences are all nonzero. By the published Floquet criterion all three circles are hyperbolic. Their maximum period tends continuously to \(T_*(r)\) as \(\eta\downarrow0\), but strict monotonicity shows every such hyperbolic triple is slower in the worst case. Hence the hyperbolic infimum equals \(T_*(r)\) without being attained.

## Verification
The companion `verify.py` evaluates periods both from the full quartic polynomial vector field and from the independently reduced angular quadrature for all three circles. It makes 24 full-field-versus-quadrature comparisons, eight strict clock-monotonicity checks, and four numerical checks of the singular asymptotic coefficient. All pass. These finite calculations corroborate the reduction; the optimization, open-parameter characterization, and singular limit follow from the displayed analytical proof.

## Relationship to prior work
Cao and Llibre's arXiv:2611.05696v1 (2026-11-03), Theorem D and Section 6, supply the entire quartic normal form, the three periodicity inequalities, and the Floquet formulas. Those ingredients, including the characterization of neutral cycles, are not new here. A published equilateral specialization further classifies neutral-circle reversibility and mixed stability signs, but does not optimize physical-time periods. Other published calculations treat two independent period controls for a concentric-pair configuration, and time slowing as *two geometric circles approach tangency*. Here the new object is the **sharp minimax of three actual periods with the common angular-gradient coefficient fixed**, its unique and nonhyperbolic optimizer, its unattained hyperbolic infimum, and a different pre-contact **angular-zero** singularity at \(r_c=1/(2\sqrt3)\). Broad prescribed-period realization results do not imply this fixed-degree/fixed-geometry constrained optimum.

## Limitations
The equilateral equal-radius geometry and the normalization \(\kappa v=1\) are essential. This is a simultaneous counterclockwise, not mixed-orientation, result. The nonhyperbolicity statement concerns only the prescribed three circles. It does not classify other periodic trajectories, global basins, or other geometric configurations. The asymptotic requires approaching the angular-arrest critical radius from below. Published full text and relevant related statements were checked, but priority outside accessible literature is not guaranteed. Independent mathematical validation has not been performed.

## References
1. C. Cao and J. Llibre, *Quartic polynomial differential systems with three disjoint invariant circles*, arXiv:2611.05696v1 (first public 2026-11-03), Theorem D and Section 6. https://arxiv.org/abs/2611.05696
2. *Neutral-circle reversibility and mixed stability for three equilateral quartic cycles*, publicly indexed published-finding corpus record, 2026-11-17. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-neutral-circle-reversibility-and-mixed-stability-for-three-equil--24ae2c1fbee3
3. *Two Cauchy time gates and bounded transverse multipliers as invariant circles approach tangency*, publicly indexed published-finding corpus record, 2026-11-17. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-two-cauchy-time-gates-and-bounded-transverse-multipliers-as-inva--e79ae2e5228d
4. *Two independently tunable periods with a frozen third clock in quartic three-circle flows*, publicly indexed published-finding corpus record, 2026-11-17. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-two-independently-tunable-periods-with-a-frozen-third-clock-in-q--40d0808ad01b

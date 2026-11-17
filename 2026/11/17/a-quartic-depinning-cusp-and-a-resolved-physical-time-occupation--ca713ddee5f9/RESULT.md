# A quartic depinning cusp and a resolved physical-time occupation law for a contracting cubic star-node flow

## Finding
Fix \(\lambda,\omega>0\), \(\eta\in\mathbb R\), and \(a>|\eta|+2\omega\). For \(\varepsilon>0\) and \(\delta\in\mathbb R\), consider the **original-physical-time** polynomial flow
\[
\begin{aligned}
\dot x&=\lambda x-[a(x^2+y^2)+\eta(x^2-y^2)]x-\delta y(x^2+y^2)-\omega y^3-\varepsilon y(x^2+y^2),\\
\dot y&=\lambda y-[a(x^2+y^2)+\eta(x^2-y^2)]y+\varepsilon x(x^2+y^2).
\end{aligned}
\]
For fixed \(\tau\in\mathbb R\), impose the critical two-parameter path \(\delta=\tau\sqrt\varepsilon\) and let \(\varepsilon\downarrow0\). For all sufficiently small positive \(\varepsilon\), the flow has a unique nonconstant periodic orbit, globally attracting every nonzero trajectory, **if and only if** \(\tau>-2\sqrt\omega\). On the other side, including equality, no nonconstant periodic orbit exists.

For \(\tau>-2\sqrt\omega\), its minimal physical period \(T_\varepsilon\) satisfies
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{3/4}T_\varepsilon
=\frac{2\pi(a+\eta)}{\lambda\sqrt{\tau+2\sqrt\omega}}.}
\]
This convergence is uniform as \(\tau\) ranges over a fixed compact subset of \((-2\sqrt\omega,\infty)\).

Let \(\Theta_\varepsilon\in[0,2\pi)\) be the angle of a point sampled uniformly in physical time along one full periodic orbit. Let \(J_\varepsilon=0\) when its principal angle lies in \((-\pi/2,\pi/2)\) and \(J_\varepsilon=1\) otherwise, so that its nearest gate is \(\pi J_\varepsilon\) modulo \(2\pi\). Let \(V_\varepsilon\) be the signed principal-angle difference from this nearest gate, divided by \(\varepsilon^{1/4}\). Then the joint law of \((J_\varepsilon,V_\varepsilon)\) converges **in total variation** to the law on \(\{0,1\}\times\mathbb R\) with densities
\[
\boxed{\mathbb P(J=j,V\in dv)=
\frac{\sqrt{\tau+2\sqrt\omega}}{2\pi\,[1+\tau v^2+\omega v^4]}\,dv,
\quad j=0,1.}
\]
Consequently the two gates have limiting probability \(1/2\) each; conditioned on a gate, the signed rescaled angular displacement has the normalized quartic-rational density. This density is unimodal at zero for \(\tau\ge0\) and has two peaks at \(v=\pm\sqrt{-\tau/(2\omega)}\) for \(-2\sqrt\omega<\tau<0\). The physical planar occupation measure converges weakly to equal atoms at \((R,0)\) and \((-R,0)\), where \(R=\sqrt{\lambda/(a+\eta)}\).

## Assumptions and scope
The inequalities are strict: \(\lambda,\omega>0\), \(a>|\eta|+2\omega\), and \(\tau\) is a fixed finite real number. The path \(\delta=\tau\sqrt\varepsilon\) approaches the codimension-two pinning cusp. The parameter \(\varepsilon\) is not time; no time reparametrization is used. A nonconstant periodic orbit means a closed trajectory other than an equilibrium. The two intervals defining \(J_\varepsilon\) are understood modulo \(2\pi\); boundary angles have zero time mass when the cycle exists. Total variation refers to the measures of the joint discrete-continuous variables on their common state space, not to the singular planar limiting measure. The given radial contraction assumption is sufficient, not optimal.

## Proof
**1. Exact polar equations and a global cycle criterion.** Put \(x=r\cos\theta\), \(y=r\sin\theta\), \(r>0\). Direct polynomial calculation gives
\[
\dot r=r[\lambda-F_\delta(\theta)r^2],\qquad
\dot\theta=r^2 G_{\varepsilon,\delta}(\theta),
\]
where
\[
F_\delta(\theta)=a+\eta\cos2\theta+\delta\cos\theta\sin\theta+\omega\cos\theta\sin^3\theta,
\qquad G_{\varepsilon,\delta}(\theta)=\varepsilon+\delta\sin^2\theta+\omega\sin^4\theta.
\]
For \(|\delta|\le\omega\), the lower bound \(F_\delta\ge a-|\eta|-3\omega/2>0\) holds, so the nonlinear radial field is strictly contracting. Write \(s=\sin^2\theta\in[0,1]\). Along \(\delta=\tau\sqrt\varepsilon\), the angular factor becomes \(\varepsilon+\tau\sqrt\varepsilon\,s+\omega s^2\). If \(\tau\ge0\) it is strictly positive. If \(\tau<0\), its minimum for sufficiently small \(\varepsilon\) occurs at \(s_*=-\tau\sqrt\varepsilon/(2\omega)\in(0,1)\), and equals \(\varepsilon(1-\tau^2/(4\omega))\). Thus it is positive everywhere exactly when \(\tau>-2\sqrt\omega\). At equality it has invariant zero-angular-speed rays, and for smaller \(\tau\) it has several such rays. Any nonstationary orbit confined between invariant rays has angular coordinate strictly monotone where it moves, so cannot close; consequently no nonconstant periodic orbit exists when \(\tau\le-2\sqrt\omega\).

When \(G>0\), \(u=r^2\) satisfies the linear angular equation
\[
\frac{du}{d\theta}=\frac{2\lambda-2F_\delta(\theta)u}{G_{\varepsilon,\delta}(\theta)}.
\]
Its full-turn affine return has strictly positive additive term and multiplier strictly between zero and one, hence exactly one positive periodic solution \(u_\varepsilon(\theta)\). It defines the unique nonzero periodic orbit. Every nonzero trajectory converges to this radial graph by the same contractive angular equation, and radial logistic comparison prevents finite-time escape. There exist parameter-independent positive constants \(m,M\) with \(m\le F_\delta\le M\), and the periodic solution obeys
\[\lambda/M\le u_\varepsilon(\theta)\le\lambda/m\quad\text{for all }\theta.\]

**2. Exact physical period identity, explicitly credited as established background.** On the periodic graph, \(d(\log r)/dt=\lambda-F_\delta(\theta)u\). Its integral over a period vanishes. Since \(dt=d\theta/[uG]\),
\[
\lambda T_\varepsilon=\int_0^{2\pi}\frac{F_\delta(\theta)}{G_{\varepsilon,\delta}(\theta)}\,d\theta.
\]
This is the already-established general physical-period identity for contracting homogeneous star-node flows [2], **not** an asserted new lemma. Both terms involving \(\cos\theta\sin\theta\) integrate to zero by the reflection \(\theta\mapsto\pi-\theta\); hence
\[
T_\varepsilon=\frac1\lambda\int_0^{2\pi}
\frac{a+\eta\cos2\theta}{\varepsilon+\tau\sqrt\varepsilon\sin^2\theta+\omega\sin^4\theta}\,d\theta.\tag{1}
\]

**3. The quartic two-parameter critical layer.** For fixed \(\tau>-2\sqrt\omega\), only the neighborhoods of \(\theta=0\pmod\pi\) contribute to the leading divergence in (1). Put \(\theta=j\pi+\varepsilon^{1/4}v\). Uniformly for \(v\) on compact sets,
\[
\varepsilon^{-1}G_{\varepsilon,\delta}(\theta)\longrightarrow 1+\tau v^2+\omega v^4,
\qquad a+\eta\cos2\theta\longrightarrow a+\eta.
\]
The polynomial \(1+\tau v^2+\omega v^4\) is strictly positive precisely for \(\tau>-2\sqrt\omega\). On any compact set of such \(\tau\), it bounds a positive multiple of \(1+v^4\), uniformly; local sine comparison upgrades this to a uniform integrable bound for the rescaled integrands of (1). Away from the two gates, the contribution is bounded as \(\varepsilon\downarrow0\) and vanishes after multiplication by \(\varepsilon^{3/4}\). Therefore
\[
\lim\varepsilon^{3/4}T_\varepsilon=\frac{2(a+\eta)}\lambda
\int_{-\infty}^{\infty}\frac{dv}{1+\tau v^2+\omega v^4}.
\]
The elementary identity
\[
\int_{-\infty}^{\infty}\frac{dv}{1+\tau v^2+\omega v^4}
=\frac{\pi}{\sqrt{\tau+2\sqrt\omega}}
\qquad(\tau>-2\sqrt\omega)
\]
follows by scaling \(v\) by \(\omega^{-1/4}\), pairing the integrals under inversion \(z\mapsto1/z\) on the positive half-line, and substituting \(t=z-z^{-1}\). This proves the explicit period limit and its stated compact-parameter uniformity.

**4. Radial equilibration and the full time-sampling law.** Fix either gate \(\theta_j=j\pi\). We claim that, uniformly for bounded \(v\),
\[
u_\varepsilon(\theta_j+\varepsilon^{1/4}v)\longrightarrow\frac\lambda{a+\eta}.
\tag{2}
\]
To prove it, fix a small \(h>0\) and use the linear angular equation on the interval from \(\theta_j-h\) to \(\theta_j+\varepsilon^{1/4}v\) (using an unwrapped angle). On this interval \(F_\delta\) differs from \(a+\eta\) by at most a modulus \(\xi(h)+O(|\delta|)\), with \(\xi(h)\downarrow0\). Variation of constants about the target \(\lambda/(a+\eta)\), together with the uniform upper and lower bounds on the radial graph, gives an error no larger than a constant times \(\xi(h)+|\delta|\) plus a uniformly bounded initial error multiplied by
\[
\exp\left[-\int_{\theta_j-h}^{\theta_j+\varepsilon^{1/4}v}
\frac{2F_\delta(\theta)}{G_{\varepsilon,\delta}(\theta)}\,d\theta\right].
\]
For bounded \(v\), the integral in this exponent tends to infinity: even a fixed interval on the incoming side of the critical layer contributes a positive multiple of \(\varepsilon^{-3/4}\). Thus the initial error disappears. First let \(\varepsilon\downarrow0\), then \(h\downarrow0\), proving (2).

The physical-time angular density is \(p_\varepsilon(\theta)=1/[T_\varepsilon u_\varepsilon(\theta)G_{\varepsilon,\delta}(\theta)]\). Under \(\theta=\theta_j+\varepsilon^{1/4}v\), equations (1)--(2) give pointwise density convergence, for each gate label, to
\[
\frac{\sqrt{\tau+2\sqrt\omega}}{2\pi(1+\tau v^2+\omega v^4)}.
\]
The two limits each integrate to \(1/2\). The change of variables from the full angular density to \((J_\varepsilon,V_\varepsilon)\) has unit total probability for every \(\varepsilon\), so Scheffé's lemma upgrades pointwise density convergence to **total variation convergence** of the joint laws. Equation (2) and tightness of the limiting scaled angular variable imply that the physical radius converges in probability to \(R=\sqrt{\lambda/(a+\eta)}\); the two atom planar limit follows. Finally the denominator's derivative \(2\tau v+4\omega v^3\) gives the asserted one-peak/two-peak shape transition. This completes the proof.

## Verification
The accompanying standalone Python program `aux_check.py` symbolically verifies the polynomial polar reduction and tests the exact quartic-rational integral at four parameter pairs. It computes the exact physical-period quadrature independently for three critical directions and three shrinking parameters and compares to the proved leading coefficient. It exits with `CUBIC_STAR_NODE_QUARTIC_CUSP_CHECK_OK`. Those finite checks are corroboration only; the proof of the infinite-parameter limit, the phase criterion, and the total-variation law is given above.

## Relationship to prior work
Alarcón, Castro, and Labouriau [1] establish the invariant-circle and angular-zero phase-portrait classification for strictly contracting homogeneous planar star-node flows, including cubic flows; no new existence theorem in that generality is claimed. An earlier quantitative result [2] already proves the entire-class original-time period identity and Floquet contraction; (1) is expressly used as background. A distinct explicit cubic example [3] yields four **quadratic** slow gates, unequal gate masses, and Cauchy layers at the ordinary inverse-square-root slowdown. Kuehn [4] proves the general degenerate saddle-node slowdown exponent, including the \(3/4\) power for quartic zeros; that exponent by itself is not presented as new. The present finding is the **joint sharp algebraic pinning boundary and parameter-resolved total-variation occupation limit at coalescing quartic gates**, with its exact quartic-rational density and internal one-to-two-peak transition for an explicit strictly contracting cubic polynomial flow. None of the inspected statements gives that two-parameter polynomial-flow law or its precise phase-space occupation conclusion.

## Limitations
The result concerns one concrete cubic family in the stated contraction regime and critical paths with fixed \(\tau\). It does not establish arbitrary-parameter-uniform estimates all the way to \(\tau=-2\sqrt\omega\), where periodic orbits cease to exist. The density-limit theorem is total variation only for the rescaled angular variable jointly with its discrete gate label; its singular planar limit is only weak. General higher-degeneracy delay theorems may imply the period exponent, and a more broadly phrased phase-reduction result may potentially subsume the local density calculation; publication priority requires independent human literature assessment. No independent mathematical audit has been performed.

## References
1. B. Alarcón, S. B. S. D. Castro and I. S. Labouriau, *Global planar dynamics with a star node and contracting nonlinearity*, arXiv:2307.16020v1 (first publicly available 2023-07-29); version 2 full text at https://arxiv.org/html/2307.16020v2 . Primary MSC2020 34C05, 37G05.
2. *Exact angular return and physical-time Floquet rigidity for contracting homogeneous star-node cycles*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-angular-return-and-physical-time-floquet-rigidity-for-cont--7c00337eaa41 , RESULT.md (full text examined).
3. *Four-gate physical-time concentration with unequal residence weights in a cubic star-node oscillator*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-four-gate-physical-time-concentration-with-unequal-residence-wei--41d1dd3d23ee , RESULT.md (full text examined).
4. C. Kuehn, *Scaling of Saddle-Node Bifurcations: Degeneracies and Rapid Quantitative Changes*, arXiv:0807.1546v2, Section 2.1, https://arxiv.org/html/0807.1546v2 .

# Exact phase basins and logarithmic barrier delay in a quadrature adaptive oscillator pair

## Finding

For the zero-detuning two-oscillator adaptive Kuramoto system of Jüttner and Martens at interaction lag \(\alpha=\pi/2\) and learning shift \(\beta=\pi/2\), **the sign of the initial cosine of phase difference determines the final phase locking, independently of the initial directed coupling strengths**. Both open phase semicircles converge to their respective phase-aligned or antipodal equilibria; the two boundary phases are invariant saddle separatrices. In the interior, the squared directed-coupling asymmetry has the exact lifetime integral
\[
\int_0^\infty \left(\frac{\kappa_{12}(t)-\kappa_{21}(t)}2\right)^2\,dt
=\frac{(\kappa_{12}(0)-\kappa_{21}(0))^2}{8\varepsilon}
-a\log|\cos\phi(0)|.
\]
The time needed to enter any fixed compact phase core from near a separatrix has the sharp asymptotic law \(a^{-1}\log(1/|\cos\phi(0)|)+O(1)\). The linearized attraction changes from oscillatory to nonoscillatory exactly at \(\varepsilon=4a\).

## Assumptions and scope

Fix arbitrary \(a>0\) and \(\varepsilon>0\). The relative phase \(\phi=\phi_1-\phi_2\) belongs to the circle \(\mathbb R/(2\pi\mathbb Z)\); the two directed couplings \(\kappa_{12},\kappa_{21}\) are initially arbitrary real numbers. Set frequency mismatch \(\omega=0\), interaction lag \(\alpha=\pi/2\), and adaptation shift \(\beta=\pi/2\) in equations (6a–c) of [1]. The resulting system is
\[
\begin{aligned}
\dot\phi&=\tfrac12(\kappa_{12}-\kappa_{21})\cos\phi,\\
\dot\kappa_{12}&=\varepsilon(1-a\sin\phi-\kappa_{12}),\\
\dot\kappa_{21}&=\varepsilon(1+a\sin\phi-\kappa_{21}).
\end{aligned}
\]
No positivity assumption on transient coupling weights is needed. All solutions exist for every positive time. The theorem concerns phase difference modulo \(2\pi\), not common phase or absolute frequency.

Let \(S=(\kappa_{12}+\kappa_{21})/2\), \(D=(\kappa_{12}-\kappa_{21})/2\). Then
\[
\dot\phi=D\cos\phi,\quad \dot D=-\varepsilon(D+a\sin\phi),\quad \dot S=\varepsilon(1-S).
\]
If \(\cos\phi(0)>0\), the orbit converges to \((\phi,D,S)=(0,0,1)\). If \(\cos\phi(0)<0\), it converges to \((\pi,0,1)\). The invariant boundary \(\phi=\pi/2\) tends to \((\pi/2,-a,1)\); the boundary \(\phi=3\pi/2\) tends to \((3\pi/2,a,1)\). These are all equilibria. The boundary equilibria have one expanding direction and two contracting directions; their global stable sets are exactly the corresponding boundary planes.

For any fixed \(R>0\), define \(q_0=\operatorname{artanh}(\sin\phi(0))\) when \(\cos\phi(0)\ne0\), and \(T_R=\inf\{t\ge0:|q(t)|=R\}\) for \(|q_0|>R\). Holding \(a,\varepsilon,R\) fixed and keeping \(|D(0)|\le M\) for any fixed \(M<\infty\), as \(|q_0|\to\infty\) one has uniformly
\[
T_R=\frac{|q_0|}{a}+O_{a,\varepsilon,R,M}(1)
=\frac1a\log\frac1{|\cos\phi(0)|}+O_{a,\varepsilon,R,M}(1).
\]
This is a **first entrance** estimate, not a claim that the trajectory never leaves the core again.

## Proof

**1. Exact split and invariant basins.** The displayed system for \((\phi,D,S)\) follows by summing and subtracting the two adaptive equations. Since the right-hand side of the phase equation vanishes identically at \(\phi=\pi/2\) and \(\phi=3\pi/2\), uniqueness prevents any finite-time crossing of these invariant boundaries. The variables \(D,S\) are bounded forward by explicit variation of constants because \(|\sin\phi|\le1\), proving global existence. On either open semicircle the map \(q=\operatorname{artanh}(\sin\phi)\) is a smooth bijection onto \(\mathbb R\). Its derivative along solutions is \(\dot q=\dot\phi/\cos\phi=D\), so
\[
\ddot q+\varepsilon\dot q+\varepsilon a\tanh q=0.
\]
The energy \(H(q,\dot q)=\tfrac12\dot q^2+\varepsilon a\log\cosh q\) is coercive, since \(\log\cosh q\sim|q|\) as \(|q|\to\infty\), and
\[
\dot H=-\varepsilon(\dot q)^2.
\]
Sublevel compactness gives precompact positive trajectories. The largest invariant subset of \(\dot H=0\) consists only of \((q,\dot q)=(0,0)\), because \(\dot D=-\varepsilon a\tanh q\) there. LaSalle's invariance principle yields convergence to that state. Since \(S(t)=1+(S(0)-1)e^{-\varepsilon t}\), this proves the claimed basins. Along either invariant boundary \(D(t)\to\mp a\), respectively. The normal phase eigenvalue at \(\phi=\pi/2\) equals \(a>0\), and at \(3\pi/2\) also equals \(a>0\), while the remaining two eigenvalues are \(-\varepsilon\), proving saddle status and the stable-set statement.

**2. Dissipation certificate.** Integrate \(\dot H=-\varepsilon D^2\) to infinity, using \(H(\infty)=0\). The identity \(\cosh(\operatorname{artanh}u)=(1-u^2)^{-1/2}\), applied to \(u=\sin\phi(0)\), gives \(H(0)=D(0)^2/2-\varepsilon a\log|\cos\phi(0)|\). Divide by \(\varepsilon\). Every factor in the displayed integral is therefore fixed by the initial phase and coupling asymmetry, independently of the initial mean coupling.

**3. Uniform logarithmic first-entrance delay.** Reflect \((q,D)\mapsto(-q,-D)\) if needed, so \(q_0\to+\infty\) and initially \(|D_0|\le M\). Until the first time \(q=R\), one has \(\tanh q\ge m_R:=\tanh R>0\). Variation of constants yields \(D(t)\le (M+a)e^{-\varepsilon t}-a m_R\). Thus after a time bounded solely in terms of \(a,\varepsilon,R,M\), say \(t_*\), we have \(D(t)\le-a m_R/2=:-b<0\). Moreover \(|D(t)|\le M+a\) for all such times. The finite initial stage changes \(q\) by at most a constant, and the subsequent strictly descending stage must hit \(R\) in finite time. Because \(1-\tanh q\le2e^{-2q}\), integrating with \(-\dot q\ge b\) on the descending stage shows
\[
0\le\int_0^{T_R}(1-\tanh q(t))\,dt
\le 2t_*+\frac1b\int_R^\infty 2e^{-2q}\,dq=O(1).
\]
Integrate \(D'+\varepsilon D=-\varepsilon a\tanh q\) from zero to \(T_R\) and use \(\int_0^{T_R}D\,dt=R-q_0\). This gives
\[
aT_R=q_0-R+\frac{D_0-D(T_R)}\varepsilon+a\int_0^{T_R}(1-\tanh q(t))\,dt
=q_0+O(1).
\]
Finally \(q_0=\log((1+\sin\phi_0)/|\cos\phi_0|)\) on the positive boundary and its reflected version on the negative boundary, so \(|q_0|=\log(1/|\cos\phi_0|)+O(1)\). The asymptotic coefficient is exactly \(1/a\), independent of \(\varepsilon\).

**4. Relaxation transition.** At \((q,D)=(0,0)\), the transverse linear matrix is \(\left(\begin{smallmatrix}0&1\\-\varepsilon a&-\varepsilon\end{smallmatrix}\right)\); its eigenvalues solve \(\lambda^2+\varepsilon\lambda+\varepsilon a=0\), with discriminant \(\varepsilon(\varepsilon-4a)\). For \(0<\varepsilon<4a\), the nonlinear remainder \(\varepsilon a(q-\tanh q)=O(q^3)\) is of higher order than the stable-focus linear part; the asymptotic angular speed approaches the nonzero imaginary part of these eigenvalues. Every nonstationary trajectory consequently crosses \(q=0\) infinitely many times. For \(\varepsilon>4a\), a hyperbolic stable node has real asymptotic eigendirections, so trajectories eventually remain on one side of \(q=0\) and have only finitely many crossings. At \(\varepsilon=4a\), setting \(p=D+2aq\) yields \(q'=p-2aq\), \(p'=-2ap+4a^2(q-\tanh q)\). Variation of constants, the cubic bound on \(q-\tanh q\), and exponential stability produce a finite \(B=\lim_{t\to\infty}e^{2at}p(t)\), with \(e^{2at}q(t)=Bt+A+o(1)\). The map from sufficiently small initial states to \(B\) has derivative \((q_0,D_0)\mapsto2aq_0+D_0\), so \(B\ne0\) is generic. In either case there are only finitely many zero crossings. The independently relaxing mean-coupling direction has exponent \(-\varepsilon\).

## Verification

The standalone `checker.py` performs exact symbolic substitutions for the reduction, energy identity and critical characteristic polynomial; integrates the full three-variable model and the transformed two-variable oscillator for sixteen independently specified configurations; and checks the dissipation budget by numerical quadrature. It also measures first-entrance times for a sequence of large logarithmic phase coordinates and checks the predicted linear delay coefficient. Finally, it compares finite-time focus/node trajectories and a critical Jordan-mode diagnostic. Finite experiments are consistency checks only; the global, infinite-time and first-entrance assertions are established in the proof.

## Relationship to prior work

Jüttner and Martens [1] introduce exactly the directed two-oscillator phase-adaptation equations, analyze local bifurcations, and discuss the asymmetric learning case \(\beta=\pi/2\), particularly at interaction lags \(\alpha=0\) and \(\alpha=-\pi/10\) (their Section III.3.2). The present global theorem isolates the different boundary interaction lag \(\alpha=\pi/2\), at which the phase dynamics depends solely on directed coupling asymmetry, producing an exact damped-gradient representation. The separately studied inertial Hebbian model [2] has additional second-order phase variables and a different learning law. The continuum adaptive-Kuramoto study [3] addresses a many-oscillator limit and symmetric learning rather than the present directed two-oscillator global basins. Neither comparison is an assertion of universal priority: the novelty claim is confined to the exact combined basin, dissipation and barrier-delay statements as checked against these accessible sources.

## Limitations

The result assumes identical intrinsic frequencies and both lags exactly at quadrature; detuning or perturbing either lag can destroy the invariant boundaries and energy identity. The uniform entrance-time estimate requires initial directed-coupling asymmetry bounded as the phase approaches a saddle; it does not claim a universal additive constant. The theorem does not describe absolute common-phase drift, large networks, or stochastic perturbations. A mathematically equivalent treatment under a different parametrization may exist outside the inspected literature. No external independent audit is claimed.

## References

[1] B. Jüttner and E. A. Martens, *Complex dynamics in adaptive phase oscillator networks*, arXiv:2209.10514 (initial public submission 2022-09-21), https://arxiv.org/abs/2209.10514 .

[2] T. Ruangkriengsin and M. A. Porter, *Low-Dimensional Behavior of a Kuramoto Model with Inertia and Hebbian Learning*, arXiv:2203.12090 (2022), https://arxiv.org/abs/2203.12090 .

[3] R. Cestnik and E. A. Martens, *Continuum limit of the adaptive Kuramoto model*, arXiv:2407.03433 (2024), https://arxiv.org/abs/2407.03433 .

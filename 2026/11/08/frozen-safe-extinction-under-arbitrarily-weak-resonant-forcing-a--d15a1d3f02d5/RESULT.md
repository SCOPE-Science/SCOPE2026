# Frozen-safe extinction under arbitrarily weak resonant forcing: a universal step-to-sine gap

## Finding

Let the **threshold logistic predator–prey differential inclusion** be the Filippov extension across the switching lines \(N=N_a\) and \(P=P_a\) of the four vector fields
\[
\begin{array}{ll}
 f_1=(\rho N(1-N/K)-aNP,\;(abN-m)P),&N>N_a,\;P>P_a,\\
 f_2=(-\rho N-aNP,\;(abN-m)P),&N<N_a,\;P>P_a,\\
 f_3=(-\rho N,\;-mP),&N<N_a,\;P<P_a,\\
 f_4=(\rho N(1-N/K),\;-mP),&N>N_a,\;P<P_a.
\end{array}
\]
Here \(N\) and \(P\) are nonnegative prey and predator abundances, \(r,K,a,b,m>0\), and \(\rho>0\) is the growth rate. The Filippov convex-hull convention applies only on the switching lines; the smooth equations above apply in the open compartments.

Assume \(n=m/(ab)\in(0,K)\) and define
\[
p=\frac r a(1-n/K),\quad
\alpha=\frac{rn}{K},\quad d=rm(1-n/K),\quad
c=n(1-n/K),\quad q=\sqrt{d-\alpha^2/4},\quad
\kappa=\frac{1-n/K}{a}.
\]
Suppose the positive coexistence equilibrium \((n,p)\) is a stable focus: \(\alpha^2<4d\), so \(q>0\). Choose any \(s,u,v>0\) such that
\[
\boxed{\quad\frac{2sc}{e\alpha}<u<\frac{sc}{\alpha},\qquad
v>s\kappa\coth\!\left(\frac{\pi\alpha}{4q}\right).\quad}
\tag{1}
\]
The interval for \(u\) is nonempty for **every** stable-focus parameter choice. For all sufficiently small \(\varepsilon>0\), set
\[
N_a=n-\varepsilon u,\quad P_a=p-\varepsilon v,\quad
\rho_{\eta}=r+\varepsilon s\eta\ \ (-1\le\eta\le1),\quad
\rho_{\mathrm{per}}(t)=r+\varepsilon s\sin(\sqrt d\,t).
\]
Every **constant-rate** threshold system with \(\rho=\rho_\eta\), initialized at \((n,p)\), stays in the coexistence compartment for all positive time and converges to the positive frozen equilibrium \((n,\kappa\rho_\eta)\). By contrast, the **periodic-rate** threshold system initialized at exactly \((n,p)\) has at least one forward Filippov solution that enters the region \(N<N_a,\ P>P_a\) in finite time and then converges to complete extinction \((0,0)\). Consequently no frozen bifurcation, nor any frozen loss of viability from this initial state, is necessary for extinction under periodic forcing as its amplitude tends to zero.

The constant \(2/e\) is a universal (parameter-independent) sharp upper bound on the ratio of the maximal frozen-step first-order prey excursion to the amplitude of the resonant sinusoidal first-order prey response in the underdamped family. No claim is made that (1) is the sharp nonlinear tipping boundary at any fixed \(\varepsilon\).

## Assumptions and scope

The parameters \(r,K,a,b,m,s,u,v\) are fixed positive constants satisfying \(n\in(0,K)\), \(\alpha^2<4d\), and the strict inequalities (1). Only \(\varepsilon\downarrow0\) varies; the two abundance thresholds approach the positive coexistence state linearly in \(\varepsilon\). The initial point is fixed at \((n,p)\) and both growth-rate inputs have the same range \([r-\varepsilon s,r+\varepsilon s]\). The conclusion for the piecewise-smooth periodic system asserts existence of a forward Filippov continuation; it does not classify all continuations at a tangential contact, smoothing effects, or nonresonant forcing frequencies.

## Proof

**1. The uniformly valid first-order approximation.** In the coexistence compartment, put \(z=(N-n,P-p)^{\mathsf T}\). With \(\rho=r+\varepsilon s h(t)\), where \(|h(t)|\le1\), the vector field becomes
\[
\dot z=Jz+\varepsilon s c h(t)e_1+R(z,\varepsilon,h),\quad
J=\begin{pmatrix}-\alpha&-an\\ abp&0\end{pmatrix},\qquad
|R|\le C(|z|^2+\varepsilon|z|)
\]
for \(|z|\) in a fixed neighborhood of zero. Since the eigenvalues of \(J\) are \(-\alpha/2\pm iq\), there are \(M,\lambda>0\) such that \(\|e^{Jt}\|\le Me^{-\lambda t}\). A variation-of-constants bootstrap gives a bound \(\sup_{t\ge0}|z(t)|\le C_1\varepsilon\), uniformly in every bounded input \(h\): on any first-exit interval from a ball of radius \(B\varepsilon\), estimate its integral equation by \(Mc s\varepsilon/\lambda+ MC(B^2\varepsilon^2+B\varepsilon^2)/\lambda\), then fix \(B>2Mcs/\lambda\) and take \(\varepsilon\) sufficiently small. In particular, the smooth coexistence solution exists inside that ball for all forward time. Reusing the integral formula bounds the nonlinear remainder uniformly by \(C_2\varepsilon^2\) and proves
\[
 z(t)=\varepsilon s c\int_0^t e^{J(t-\tau)}e_1h(\tau)\,d\tau+O(\varepsilon^2),\qquad t\ge0,
\tag{2}
\]
with one constant in the \(O(\varepsilon^2)\) independent of time and of \(h\) with \(|h|\le1\).

**2. Uniform safety of all frozen controls.** Put \(p_0=\alpha/2\). Matrix exponentiation gives
\[
 [e^{Jt}]_{21}=\frac{abp}{q}e^{-p_0t}\sin(qt),\qquad
\int_0^t[e^{J\tau}]_{11}\,d\tau
=\frac{e^{-p_0t}\sin(qt)}q.
\tag{3}
\]
For \(h(t)\equiv\eta\), the first-order prey departure in (2) therefore satisfies
\[
 |N(t)-n|\le\varepsilon s c\frac{e^{-p_0t}|\sin(qt)|}{q}+C_2\varepsilon^2
\le\varepsilon\frac{2sc}{e\alpha}+C_2\varepsilon^2,
\quad t\ge0,
\tag{4}
\]
because \(|\sin(qt)|\le qt\) and \(\max_{t\ge0}te^{-\alpha t/2}=2/(e\alpha)\). The predator component has the input-independent bound
\[
 |P(t)-p|\le\varepsilon s H+C_2\varepsilon^2,
\quad H=c\int_0^\infty|[e^{Jt}]_{21}|\,dt
=\kappa\coth\!\left(\frac{\pi\alpha}{4q}\right).
\tag{5}
\]
Indeed \(c(abp)/d=\kappa\), and summation of the absolute-sine half-period integrals proves the displayed hyperbolic-cotangent identity. Both strict inequalities in (1) and (4)–(5) give \(N(t)>N_a\), \(P(t)>P_a\) for all \(t\ge0\) and all \(\eta\in[-1,1]\), provided \(\varepsilon\) is sufficiently small. Thus the smooth solutions are the actual threshold-system solutions without switching. The frozen coexistence equilibrium is \((n,\kappa\rho_\eta)\); it remains locally asymptotically stable (the Jacobian trace is negative and determinant positive). The small, forward-invariant neighborhood obtained in Step 1 lies in its local basin after shrinking \(\varepsilon\), so these trajectories converge to that equilibrium.

**3. The resonant response must reach the prey threshold.** The transfer function for prey is
\[
 \widehat N(\omega)=\frac{ci\omega}{d-\omega^2+i\alpha\omega},
\]
so for \(h(t)=\sin(\sqrt d\,t)\) the limiting periodic solution of the first-order variational equation has prey amplitude precisely \(c/\alpha\). Its transient correction is \(O(e^{-\alpha t/2})\). The strict upper inequality in (1) consequently provides a **finite** time \(T\), fixed independently of \(\varepsilon\), at which its prey component is strictly less than \(-u/s\). Formula (2) then gives \(N(T)<N_a\) for sufficiently small \(\varepsilon\). Equation (5), valid also for sinusoidal input, guarantees \(P(t)>P_a\) along the entire smooth solution before and through this time.

**4. An admissible entry causes irreversible extinction.** Follow the smooth coexistence field \(f_1\) until the first time it enters \(N<N_a\); such an entry exists by Step 3. At any earlier tangential contact with the switching line, following \(f_1\) is allowed by the Filippov convexification, and its smooth continuation remains in \(N\ge N_a\). At the first actual downward entry, \(f_1\) has nonpositive outward normal component, while \(f_2\) has strictly negative prey component \(-\rho N-aNP<0\). Hence a Filippov continuation may enter the region \(N<N_a\) while the predator remains above its threshold. Once inside, every subsequent prey vector field has \(\dot N\le-\rho N\), because \(\rho(t)\ge r-\varepsilon s>0\); therefore \(N(t)\downarrow0\) exponentially and never returns to the prey threshold. Once \(N(t)<m/(2ab)\), every relevant predator vector field satisfies \(\dot P\le-(m/2)P\), whether \(P\) is above or below its threshold. Thus \(P(t)\to0\), proving the claim.

**5. Sharpness of the step-to-sine constant.** The exact maximum (over \(t\ge0\)) of the first-order frozen-step prey excursion per unit step amplitude is
\[
 S_N=\frac c{\sqrt d}\exp\!\left[-\frac{\alpha}{2q}\arctan\!\left(\frac{2q}{\alpha}\right)\right].
\]
The bound from Step 2 says \(S_N/(c/\alpha)<2/e\). As \(q/\alpha\downarrow0\) through stable-focus matrices, the ratio tends to \(2/e\). Hence the universal numerical factor cannot be replaced by a smaller factor valid throughout the underdamped family. This limiting sharpness does not assert that the chosen sufficient threshold corridor is the exact finite-amplitude boundary.

## Verification

An accompanying standalone program independently evaluates the matrix-exponential frozen-step identity over 79 times and integrates the smooth solution for three small forcing amplitudes and 39 frozen controls. Its output is `VERIFY_OK linear_step_checks=79 frozen_profiles=39 forced_crossings=3`. It checks the strict inequalities, observes downward resonant prey-threshold crossings with predators above their thresholds, and observes frozen trajectories staying above both thresholds. Run `python verify.py` with NumPy and SciPy. These finite computational tests corroborate, but do not replace, the analytic all-parameter and small-amplitude proof above.

A reproducible rational-decimal example is \(r=1.2\), \(K=6\), \(a=1.1\), \(b=0.32\), \(m=0.45\), \(s=0.3\), \(u=v=1\). Here \(\alpha\approx0.2556818\), \(d\approx0.4249432\), and \(q\approx0.6392182\); the step bound is approximately \(0.869\) whereas the resonant amplitude coefficient is approximately \(1.1804\). The predator bound is \(sH\approx0.7055<1\). Simulations with \(\varepsilon\in\{0.02,0.008,0.002\}\) recover the predicted qualitative separation.

## Relationship to prior work

Gao, Poloni, Wang and Lewis (2026) introduced this threshold predator–prey system and used numerical frequency scans plus a Filippov crossing criterion to demonstrate frequency-induced tipping. Prior quantitative analysis of its smooth coexistence subsystem already gives the exact prey and predator first-harmonic transfer amplitudes, including the prey optimizer \(\omega=\sqrt d\); those amplitudes are **not claimed as new here**. The new result compares a uniform frozen-step response with the forced response, supplies a universal \(2/e\) separation, controls the predator barrier uniformly in time, and proves actual extinction for a continuum of arbitrarily small forcing amplitudes from the same initial state, while **every** frozen rate in the forcing range gives coexistence.

Swailem and Rucklidge (2025/2026) analyze parametric resonance and chaos in a different Lotka–Volterra family with periodically varying carrying capacity and, sometimes, predation rate; their model has no corresponding Filippov threshold mechanism. Naess, Dimentberg and Gaidai (2008) consider temporally varying prey reproduction in a generalized Lotka–Volterra model; only its abstract was accessible for comparison, which is a residual historical-priority risk.

## Limitations

This is a sufficient **existence** theorem for moving near-equilibrium abundance thresholds, not a sharp finite-amplitude tipping-phase diagram. The thresholds must scale with \(\varepsilon\), the unforced coexistence must be a stable focus, and the growth forcing is sinusoidal at the prey-response optimum. The conclusion asserts existence of a forward Filippov extinction trajectory, not uniqueness at a grazing contact. No claim is made about smoothing the discontinuous thresholds, random forcing, spatial dynamics, or numerical estimates beyond the explicitly specified example. Historical priority and independent validation are not exhaustive.

## References

1. S. Gao, S. Poloni, H. Wang, and M. Lewis, *Frequency-induced Tipping: Resonance-Driven Tipping in a Threshold Predator-Prey System*, arXiv:2610.39113v1 (first posted 2026-10-29), https://arxiv.org/html/2610.39113v1. Sections 2.2–2.4, 4.1–4.2, and Supplementary Information inspected.
2. M. Swailem and A. M. Rucklidge, *Parametric resonance, chaos and spatial structure in the Lotka–Volterra model*, arXiv:2511.03521v2 (2026), https://arxiv.org/html/2511.03521v2. Sections I–III and model definitions inspected.
3. A. Naess, M. F. Dimentberg, and O. Gaidai, *Lotka–Volterra systems in environments with randomly disordered temporal periodicity*, Phys. Rev. E 78 (2008), 021126, https://doi.org/10.1103/PhysRevE.78.021126. Abstract only inspected.

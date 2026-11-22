# Reentrant optimization of dissipation in a critically damped chiral active oscillator

## Finding
For a two-dimensional unit-mass, critically damped harmonic oscillator driven by a unit-orientation active force of fixed magnitude \(f>0\), the stationary *translational* heat dissipation \(Q\) has a reentrant global maximizer as angular chirality is increased at fixed trap and friction. Let \(d\geq 0\) be angular diffusion, \(\Omega\in\mathbb R\) angular drift, \(t=\Omega^2\), and \(w=1+d\). Then
\[
\frac{Q}{f^2}=F(w,t)=\frac{w^3-w^2+(w+1)t}{(w^2+t)^2},\qquad w\geq1,\ t\geq0.
\]
Let \(t_*\) be the unique positive root of
\[
P(t)=t^6-17t^5+105t^4+74t^3+15t^2-t-1.
\]
It lies in \((0.19,0.2)\), with \(t_*=0.190531907893624\ldots\). Let \(t_+=3+2\sqrt 2=5.82842712474619\ldots\). The exact classification of **global** maximizers of \(Q\) over \(d\geq0\) is:

1. If \(0\leq t<t_*\), exactly one maximizing \(d_*(t)>0\) exists. At zero chirality, \(d_*(0)=1\).
2. At \(t=t_*\), precisely two maximizers coexist: \(d=0\) and \(d=d_{\mathrm{jump}}=0.507653856356458\ldots\). The latter is the larger positive stationary root shifted by one.
3. If \(t_*<t\leq t_+\), \(d=0\) is the sole global maximizer.
4. If \(t>t_+\), exactly one maximizing \(d_*(t)>0\) exists, with \(d_*(t)\to0\) as \(t\downarrow t_+\).

The low-chirality optimizer thus disappears by a discontinuous jump, while the high-chirality optimizer emerges continuously. More precisely,
\[
 d_*(t)=1-\frac32t+O(t^2)\quad(t\downarrow0),\qquad
 d_*(t)=(3-2\sqrt2)(t-t_+)+O((t-t_+)^2)\quad(t\downarrow t_+),
\]
where the second expansion is from above; for \(t\to\infty\), \(d_*(t)=\sqrt t-2+o(1)\). The result is independent of independent translational thermal noise at fixed active-force amplitude.

## Assumptions and scope
Let \(X_s,V_s\in\mathbb R^2\) and \(\theta_s\in\mathbb R/(2\pi\mathbb Z)\) obey the stationary dynamics
\[
 dX_s=V_s\,ds,\qquad dV_s=(-2V_s-X_s+f(\cos\theta_s,\sin\theta_s))\,ds+2\sqrt T\,dW_s,
 \qquad d\theta_s=\Omega\,ds+\sqrt{2d}\,dB_s.
\]
Here \(T>0\), \(f>0\), independent standard Brownian motions \(W\) and \(B\), and \(d\geq0\). For \(d=0\), take the invariant uniform angular-phase ensemble; when \(\Omega=0\), all stationary angular ensembles give the same power. The translational thermal bath has friction coefficient \(2\) and unit mass, stiffness, and natural frequency. Define the stationary active power entering the oscillator and corresponding excess bath heat flux by
\[
Q=f\,\mathbb E[(\cos\theta,\sin\theta)\cdot V]=2(\mathbb E\|V\|^2-2T).
\]
This \(Q\) counts translational heat delivered to the thermal bath, not entropy produced by maintaining the angular drift, or any total entropy production of an underlying motor. When divided by \(T\), it is the translational housekeeping heat rate in entropy units under the usual active-force convention. Maxima are over nonnegative angular diffusion at **fixed** \(\Omega\), \(f\), and mechanical coefficients. If \(d>0\) is required strictly, the intervals with boundary maximum have an unattained supremum as \(d\downarrow0\).

## Proof
**Stationary response and normalization.** The damped mechanical response has impulse displacement kernel \(s e^{-s}\) and impulse velocity kernel \((1-s)e^{-s}\), for \(s\geq0\). Angular stationarity gives the exactly known orientational correlation \(\mathbb E[n_s\cdot n_{s-u}]=e^{-du}\cos(\Omega u)\). Since thermal noise is independent, the active contribution to power is
\[
Q=f^2\int_0^\infty e^{-(1+d)u}(1-u)\cos(\Omega u)\,du
=f^2\operatorname{Re}\frac{d+i\Omega}{(1+d+i\Omega)^2}.
\]
Equivalently, the stationary complex moments \(Z=\mathbb E[(X_1+iX_2)e^{-i\theta}]\), \(U=\mathbb E[(V_1+iV_2)e^{-i\theta}]\) obey \(0=U-(d+i\Omega)Z\) and \(0=-(2+d+i\Omega)U-Z+f\), giving the same power. Rationalization gives the displayed \(F\). The stationary mechanical energy balance gives the displayed heat identity and temperature independence.

**Number of competing maxima.** Direct differentiation gives
\[
\partial_w F(w,t)=\frac{N(w,t)}{(w^2+t)^3},\qquad N(w,t)=t^2-6tw-w^4+2w^3.
\]
Because \(\partial_w^2N=12w(1-w)<0\) for \(w>1\), \(N\) is strictly concave there, and tends to \(-\infty\). Thus \(F\) has at most one interior *local maximum*. It tends to zero as \(w\to\infty\), so its global maxima are either \(w=1\), a single interior maximum, or both. At \(t=0\), \(N=w^3(2-w)\), so the unique maximizer is \(w=2\).

**Where the global maximum can change.** Writing
\[
 F(w,t)-F(1,t)=\frac{(w-1)G(w,t)}{(w^2+t)^2(1+t)^2},
\]
with
\[
G=t^3+t^2w^2-4t^2w-2t^2-2tw^3-2tw-t+w^2,
\]
one obtains by the exact Sylvester resultant
\[
\operatorname{Res}_w(N,G)=-16t^3(t^2-6t+1)P(t).
\]
Hence an interior stationary maximum tied with the boundary can occur only at positive roots of \(P(t)\) or \(t^2-6t+1\). A change through the boundary with no distinct interior tied maximum also requires \(N(1,t)=t^2-6t+1=0\). There cannot be a switch between two distinct interior local maxima because there is at most one.

The polynomial \(P\) has exactly one positive root: \(P(0)=-1\), \(P'(0)=-1\), \(P(t)\to\infty\), and
\[
P''(t)=t^2(30t^2-340t+1260)+444t+30>0\qquad(t\geq0),
\]
since the quadratic has negative discriminant and positive leading coefficient. Exact rational substitution gives \(P(19/100)<0<P(1/5)\). At \(t=19/100\), the trial \(w=3/2\) satisfies \(G=106/15625>0\), proving an interior competitor beats the boundary. At \(t=1/5\), with \(y=w-1\geq0\),
\[
 G(w,1/5)=-\frac2{125}\big[25y^3+10(y-1)^2+2\big]<0,
\]
so the boundary wins globally. Thus the unique intervening tie occurs at \(t=t_*\); the larger stationary root has \(w=1.507653856356458\ldots\). These facts and continuity of the maximal value establish the first-order switch.

The only other positive candidates for boundary/interior switches are \(t_-=3-2\sqrt2\) and \(t_+=3+2\sqrt2\). At \(t_-\), \(N(1,t_-)=0\) but \(\partial_wN(1,t_-)=2-6t_->0\), so the boundary cannot be a global maximum; this does not interrupt the interior-maximizer regime. At \(t_+\), \(N(1,t_+)=0\) and \(\partial_wN(1,t_+)<0\); the boundary is the unique maximizer there (by the preceding no-switch argument, or direct strict concavity). For \(t>t_+\), \(N(1,t)>0\), forcing a unique interior global maximum. The classification follows, including all equalities.

**Critical scalings.** Implicit differentiation of \(N(w_*(t),t)=0\) at \((w,t)=(2,0)\) gives \(w_*'(0)=-3/2\). At \((1,t_+)\), it gives \(w_*'(t_+)=3-2\sqrt2\). For \(t\to\infty\), substituting \(w=\sqrt t+a+o(1)\) into \(N=0\) yields \(a=-1\), so \(d=w-1=\sqrt t-2+o(1)\). No finite-grid computations are used as infinite-domain proofs.

## Verification
Run `python CHECKER.py` from the same directory, with `sympy` and `mpmath` installed. This independently checks the exact derivative, polynomial identity and resultant, exact rational sign tests, strictly convex threshold polynomial, moment-equation response, and numerical time-domain response integrals, then compares representative global maximizers. A reference replay passed 137 checks. The resultants and sign arguments above, not numerical sampling, establish the universal assertions. The checker prints the first-order frequency-squared threshold, optimizer jump, and continuous onset threshold.

## Relationship to prior work
Frydel [1] derives the general active-force heat-flow relation and the achiral harmonic-oscillator result that dissipation is maximized at persistence time equal to the inverse oscillator frequency. That theorem corresponds to the \(t=0\) boundary of the present calculation, and is not claimed as new. Olsen and Löwen [2] establish the chiral orientational correlation and optimize **unconfined spatial diffusivity**, not translational heat flow in an inertial harmonic trap. Later work on inertial chiral particles [3] gives free-particle velocity and fluctuation formulas, while [4] studies harmonic-trap spatial distributions and position kurtosis; neither inspected statement gives this critically damped translational heat-optimum bifurcation. The new contribution is the exact *global* reentrant optimizer and the one discontinuous plus one continuous onset law in a fully specified mechanical model. A broader optimization analysis in work not inspected here could still implicitly cover this specialized case.

## Limitations
The result concerns the critically damped isotropic linear trap with unit mass, friction 2, stiffness 1, fixed propulsion amplitude, and angular drift fixed during optimization. It does not classify other damping ratios, nonlinear traps, parameter-dependent active-force amplitudes, or the entropy cost of creating and maintaining chiral torque. At \(d=0\), a stationary angular phase ensemble must be specified; for positive \(d\) it is unique. No statement about a whole-system thermodynamic optimum is made. The source-priority assessment is based on the inspected accessible material and may require independent literature review.

## References
[1] D. Frydel, *Entropy production of active particles in underdamped regime*, first publicly posted 2022-11-03, arXiv:2211.02082, https://arxiv.org/abs/2211.02082 . See especially the heat-balance definition and harmonic-trap Eq. (41).

[2] K. S. Olsen and H. Löwen, *Optimal diffusion of chiral active particles with strategic reorientations*, first posted 2024-05-23, arXiv:2405.14326, https://arxiv.org/abs/2405.14326 . See Sec. II.1 for the chiral angular correlation and Sec. II.3 for the diffusivity objective.

[3] A. Pattanayak, S. Roy and A. Chaudhuri, *Inertia–chirality interplay in active Brownian motion: exact dynamics and phase maps*, arXiv:2511.18361, https://arxiv.org/abs/2511.18361 . Covers inertial chiral *free* motion.

[4] M. Muhsin, S. Deion and M. Sahoo, *Inertial chiral active Brownian particle in a harmonic confinement: Resonance-like response*, arXiv:2604.05722, https://arxiv.org/abs/2604.05722 . Covers confinement, spatial fluctuations and position kurtosis.

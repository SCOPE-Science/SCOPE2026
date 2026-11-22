# Universal critical clearance and a two-scale inaccessible-infection tail in an awareness–fatigue epidemic

## Finding
At the critical invasion threshold in the prevalence-driven SIRA model, *every* epidemic-seeded feasible trajectory tends to the disease-free state, but the total infectious fraction has a universal algebraic tail rather than exponential clearance. Put \(k=\gamma+\mu\) and
\[
Q=k\left[\frac{k}{\mu}+\frac{\rho}{\omega}\left(\frac{\mu+\kappa_1}{\mu+\kappa_2}+\frac{\delta_1}{\delta_2+k}\right)\right].
\]
For every feasible initial state with \(I(0)>0\), the sharp limits are
\[
\begin{aligned}
\lim_{t\to\infty}tI(t)&=Q^{-1},
&\lim_{t\to\infty}tI_a(t)&=Q^{-1},\\
\lim_{t\to\infty}tA(t)&=\frac{\rho}{\omega Q},
&\lim_{t\to\infty}tS_u(t)&=\frac{(\mu+\kappa_1)\rho}{(\mu+\kappa_2)\omega Q},\\
\lim_{t\to\infty}tR(t)&=\frac{\gamma}{\mu Q},
&\lim_{t\to\infty}t^2 I_u(t)&=\frac{\delta_1\rho}{\omega(\delta_2+k)Q^2}.
\end{aligned}
\]
Furthermore, for all \(t\ge0\), \(I(t)\le I(0)/[1+kI(0)t]\), and \(\int_0^T I(t)\,dt\sim Q^{-1}\log T\). Thus the infectious population outside accessible interactions is one order smaller, \(I_u=\Theta(t^{-2})\), than accessible infection, \(I_a=\Theta(t^{-1})\). The two positive terms multiplying \(\rho/\omega\) in \(Q\) quantify susceptible withdrawal (including newborn allocation) and infectious sequestration separately. For fixed biological rates and positive awareness response, \(Q>k^2/\mu\), so this critical tail has strictly smaller amplitude than the no-awareness SIR benchmark despite the identical basic reproduction number.

## Assumptions and scope
The state is \((S_a,S_u,I_a,I_u,R,A)\) with nonnegative population fractions, \(S_a+S_u+I_a+I_u+R=1\), and \(0\le A\le1\). Fix \(\gamma,\mu,\kappa_1,\kappa_2,\delta_1,\delta_2,\rho,\omega>0\), and let \(\beta=k=\gamma+\mu\). Here \(S_a,S_u\) are accessible/inaccessible susceptible fractions, \(I_a,I_u\) are accessible/inaccessible infectious fractions, \(R\) is recovered, and \(A\) is awareness. Precisely the autonomous equations (1)–(6) of [1] are used, with no external awareness source:
\[
\begin{aligned}
\dot S_a&=\mu(1-A)-kS_a I_a+\kappa_2(1-A)S_u-\kappa_1 A S_a-\mu S_a,\\
\dot S_u&=\mu A+\kappa_1 A S_a-[\kappa_2(1-A)+\mu]S_u,\\
\dot I_a&=kS_a I_a-\delta_1 A I_a+\delta_2(1-A)I_u-k I_a,\\
\dot I_u&=\delta_1 A I_a-[\delta_2(1-A)+k]I_u,\\
\dot R&=\gamma(I_a+I_u)-\mu R,\\
\dot A&=\rho(I_a+I_u)(1-A)-\omega A.
\end{aligned}
\]
The feasible simplex is forward invariant by the source's boundary-invariance argument. The conclusion is deterministic and asymptotic, with no claim about stochastic extinction or finite-time elimination.

## Proof
Write \(I=I_a+I_u\), and assume \(I(0)>0\). The infectious total obeys the exact identity
\[
\dot I=kS_a I_a-kI=-k\big[(1-S_a)I_a+I_u\big].
\]
Since \(S_a\le1-I\) and \(I_a\le I\), the differential inequalities \(-kI\le\dot I\le-kI^2\) hold on the feasible simplex. Consequently infection remains positive at every finite time and
\[
0<I(t)\le\frac{I(0)}{1+kI(0)t}\longrightarrow0.
\]
The awareness and recovered equations are stable linear filters with forcing tending to zero, hence \(A,R\to0\). The equation for \(S_u\) has decay coefficient \(\kappa_2(1-A)+\mu\ge\mu>0\) and forcing \(A(\mu+\kappa_1S_a)\to0\), so \(S_u\to0\). By conservation \(S_a\to1\). This proves *global* clearance even at exact criticality.

Set \(q=I_u/I\), which is defined for all finite times. Direct differentiation gives
\[
\dot q=(1-q)(\delta_1 A-kS_a q)-\delta_2(1-A)q\le\delta_1 A-\delta_2(1-A)q.
\]
Since \(A\to0\), eventually the right side is bounded by \(\delta_1 A-(\delta_2/2)q\). Scalar comparison yields \(q\to0\), hence
\[
\frac{\dot I}{I}=kS_a(1-q)-k\longrightarrow0.
\]
We use the following elementary filter lemma. If \(x>0\), \(\dot x/x\to0\), and \(y'=-a(t)y+b(t)x^p\) for some fixed \(p>0\), with \(a(t)\to a_*>0\) and \(b(t)\to b_*\), then \(y/x^p\to b_*/a_*\). Indeed, \(z=y/x^p\) satisfies \(z'=-(a(t)+p\dot x/x)z+b(t)\), a scalar equation with limiting strictly positive damping; variation of constants proves the limit. No center-manifold or numerical approximation is needed.

Apply the lemma with \(x=I\) successively to the awareness, recovered, inaccessible-susceptible, and inaccessible-infected equations (the last with \(p=2\)). The exact limits are
\[
\frac A I\to\frac\rho\omega,\quad
\frac R I\to\frac\gamma\mu,\quad
\frac{S_u}I\to\frac{(\mu+\kappa_1)\rho}{(\mu+\kappa_2)\omega},\quad
\frac{I_u}{I^2}\to\frac{\delta_1\rho}{\omega(\delta_2+k)}.
\]
For the final application, its forcing coefficient is \(\delta_1(A/I)(I_a/I)\to\delta_1\rho/\omega\), while its damping tends to \(\delta_2+k\). Also \((1-S_a)/I=1+S_u/I+R/I\). Dividing the exact infectious-total identity by \(-I^2\) therefore gives
\[
\frac{d}{dt}\left(\frac1I\right)
=k\left[\frac{1-S_a}{I}\left(1-\frac{I_u}{I}\right)+\frac{I_u}{I^2}\right]\longrightarrow Q.
\]
Integrating this derivative, \((1/I(t))/t\to Q\); thus \(tI(t)\to1/Q\). All stated component limits follow by multiplication of the ratios, and the logarithmic person-time law follows by integrating \(I(t)\sim 1/(Qt)\). Since \(\rho>0\), both behavior-dependent contributions to \(Q\) are positive, proving the strict no-awareness comparison. This completes the proof for arbitrary seeded feasible initial data.

## Verification
The supplied stand-alone `CHECK.py` evaluates the rational example \(\gamma=\mu=\kappa_1=\kappa_2=\delta_1=\delta_2=\rho=\omega=1\), \(\beta=2\). It checks \(Q=20/3\) and the exact asymptotic coefficients \(\lim tI=3/20\), \(\lim tA=\lim tS_u=\lim tR=3/20\), and \(\lim t^2I_u=3/400\); it also checks the exact infected-total identity at sampled states and compares a numerical integration to the predicted finite-time tail. These finite checks corroborate the calculations; the inequalities and ratio limits in the proof establish the infinite-time theorem.

## Relationship to prior work
Mohammed and Alsammani [1], equations (1)–(6), introduce exactly this accessibility-and-fatigue model. Their Proposition 3.2 establishes \(\mathcal R_0=\beta/(\gamma+\mu)\); Theorem 3.4 proves global disease-free convergence only for \(\mathcal R_0<1\); Theorem 3.6 excludes endemic equilibria for \(\mathcal R_0\le1\); Corollary 3.7 establishes a forward transcritical bifurcation; and Theorem 3.9 decomposes *supercritical equilibrium* burden. These results do not provide global convergence at the exact boundary, a critical-time infection amplitude, or the second-order inaccessible-infection tail. The classical critical SIR \(1/t\) law and stable-filter comparison are background methods, not claimed as new. The contribution is the all-initial-state critical theorem and its exact, two-channel coefficients for the full six-state model. Other published awareness and protected-population epidemic models exhibit critical algebraic clearance, but their different infection and behavior equations do not imply the coefficients above.

## Limitations
All rates specified above are strictly positive; changing the aware-newborn allocation, adding external awareness forcing, or introducing infection/recovery memory changes the equations and may change the coefficients. The statement holds at the exact boundary \(\beta=\gamma+\mu\), not at fixed supercriticality. Stochastic outbreak statistics and empirical parameter calibration are not addressed. Scientific historical priority outside the inspected accessible literature remains subject to independent review.

## References
[1] M. Mohammed and A. Alsammani, *Long-term Coexistence of Epidemics and Risk Awareness: Impacts of Adaptive Human Response and Fatigue*, arXiv:2607.18301 (first public preprint 2026-07-16), https://arxiv.org/abs/2607.18301; journal version, *Biomath* **15** (2026), https://doi.org/10.55630/j.biomath.2026.10.234.

[2] P. van den Driessche and J. Watmough, *Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission*, *Mathematical Biosciences* **180** (2002), 29–48, https://doi.org/10.1016/S0025-5564(02)00108-6.

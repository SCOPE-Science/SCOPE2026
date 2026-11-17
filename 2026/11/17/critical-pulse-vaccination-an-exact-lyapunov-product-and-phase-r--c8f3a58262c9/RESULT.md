# Critical pulse vaccination: an exact Lyapunov product and phase-resolved epidemic clearance

## Finding

For the logistic-susceptible impulsive epidemic system below, on its exact disease-invasion threshold, every solution starting with strictly positive susceptible and infectious populations converges to the positive disease-free periodic orbit. More precisely, the infection clears with an explicit, initial-condition-independent, **phase-resolved reciprocal-period law**; the susceptible deficit has an explicit periodic leading coefficient. A strictly decreasing pulse-continuous Lyapunov product proves that no strictly positive recurrent or periodic solution can coexist at the threshold.

Fix \(A,\beta,\delta,T>0\) with \(0<\delta<\beta A\) and put
\[
q=\exp\bigl(-(A-\delta/\beta)T\bigr)\in(0,1).
\]
For \(n=0,1,2,\ldots\), let \(S,I>0\) solve, between successive impulses,
\[
\dot S=S(A-S-\beta I),\qquad \dot I=I(\beta S-\delta),\qquad nT<t<(n+1)T,
\]
with the end-of-period pulse \(S((n+1)T^+)=qS((n+1)T^-)\), \(I((n+1)T^+)=I((n+1)T^-)\). Initial values refer to \(0^+\). Define
\[
s_* =\frac{A(qe^{AT}-1)}{e^{AT}-1}>0,\qquad
s(\tau)=\frac{A s_*e^{A\tau}}{A+s_*(e^{A\tau}-1)},\quad 0\le\tau<T,
\]
\[
w(\tau)=q^{-\beta\tau/T}s(\tau)^{-\beta},\qquad
C=\beta^2\int_0^T w(u)\,du>0.
\]
Then, uniformly over \(0\le\tau<T\),
\[
S(nT+\tau)\longrightarrow s(\tau),\qquad
\boxed{\lim_{n\to\infty}nI(nT+\tau)=\frac{w(\tau)}{C}}.
\]
There is also an exact leading susceptible correction. Let \(k\) be the unique positive \(T\)-periodic (impulse-continuous) solution of
\[
k'(\tau)+s(\tau)k(\tau)=\beta w(\tau),\qquad k(T)=k(0),
\]
which is explicitly defined by
\[
B(\tau)=\int_0^\tau s(v)\,dv,\quad
k(0)=\frac{\beta\int_0^T e^{B(v)}w(v)\,dv}{e^{B(T)}-1},\quad
k(\tau)=e^{-B(\tau)}\left(k(0)+\beta\int_0^\tau e^{B(v)}w(v)\,dv\right).
\]
Uniformly on each pulse interval,
\[
\boxed{\lim_{n\to\infty}n\bigl(S(nT+\tau)-s(\tau)\bigr)
=-\frac{s(\tau)k(\tau)}{C}<0.}
\]
The two displayed limits use \(n\) (number of completed periods), not physical time \(nT+\tau\). In particular, infection is asymptotic to a positive periodic profile divided by \(n\), and the susceptible coordinate ultimately lies strictly below the disease-free profile.

## Assumptions and scope

All parameters and initial coordinates are real. The hypotheses are exactly \(A,\beta,\delta,T>0\), \(\delta<\beta A\), critical coverage \(q=e^{-(A-\delta/\beta)T}\), and \(S(0^+),I(0^+)>0\). No small-infection hypothesis is imposed and the whole positive quadrant is allowed. The system is the no-seasonality, two-dimensional logistic-susceptible pulse-vaccination reduction, with infectious removal \(\delta\). The origin's disease-free solution and the infectious-free axis are not part of the strictly positive assertion. Impulses occur at positive multiples of \(T\) and the coordinate \(\tau\) records time since the latest pulse.

## Proof

**1. Positivity, boundedness, and positive susceptible floor.** Positivity between pulses follows from multiplicative right-hand sides and is preserved by \(q>0\). Set \(K=\max\{A,S(0^+)\}\). Since \(\dot S\le S(A-S)\), and the pulse only decreases \(S\), we have \(S(t)\le K\). For \(P=S+I\) between impulses, \(\dot P=A S-S^2-\delta I\le K(A+\delta)-\delta P\), and pulses do not increase \(P\); hence \(S+I\le M:=\max\{S(0^+)+I(0^+),K(A+\delta)/\delta\}\) for all times.

A uniform strictly positive lower bound on \(S\) is needed below; it does not follow merely from positivity. Write \(S_n=S(nT^+)\), \(I_n=I(nT^+)\) and define
\[
h=\delta/(2\beta),\quad \eta=he^{-AT},\quad r=e^{-\delta T/2}<1,\quad \rho=q e^{(A-h)T}=e^{\delta T/(2\beta)}>1.
\]
If \(S_n<\eta\), then \(S(nT+u)\le S_ne^{Au}<h\) for \(0\le u<T\), and therefore \(I_{n+1}\le rI_n\). Integrating \(\dot S/S\) across that period and its terminal pulse gives
\[
S_{n+1}\ge \rho S_n e^{-\beta T I_n}.
\]
During any maximal consecutive run of such low periods, \(I\) decreases geometrically, so every susceptible value at the period endpoints is at least its value at entry times \(\exp[-\beta TM/(1-r)]\). The entry value is either \(S_0\), or at least \(\eta c_0\), where \(c_0=q\exp[(A-K-\beta M)T]>0\) is a global one-step lower bound for \(S_{n+1}/S_n\). Thus
\[
\inf_{n\ge0}S_n\ge \min\{S_0,\eta c_0,\eta\}\exp[-\beta TM/(1-r)]>0.
\]
Between pulses, \(\dot S/S\ge-(K+\beta M)\), supplying a positive floor on continuous segments too.

**2. Exact pulse-continuous Lyapunov identity.** For \(t=nT+\tau\), \(0\le\tau<T\), define
\[
L(t)=q^{\beta\tau/T}S(t)^\beta I(t).
\]
The critical identity \(\delta=\beta(A+\log q/T)\) and the equations give exactly
\[
\frac{d}{dt}\log L
=\frac{\beta\log q}{T}+\beta(A-S-\beta I)+(\beta S-\delta)
=-\beta^2 I.
\]
At a pulse the phase factor changes from \(q^\beta\) to \(1\) while \(S^\beta\) changes by \(q^\beta\), so \(L\) is continuous and strictly decreasing on every nonzero-length positive trajectory. This excludes positive periodic/recurrent trajectories: they would have to revisit the same positive value of \(L\), despite its strict descent.

Because \(L\) is bounded below, it has a limit. If that limit were positive, boundedness of \(S\) and \(q^{\beta\tau/T}\le1\) would give a fixed lower bound for \(I\), forcing exponential descent of \(L\), a contradiction. Hence \(L\to0\). The susceptible floor and \(q^{\beta\tau/T}\ge q^\beta\) then imply \(I\to0\), uniformly within periods.

**3. Global convergence of susceptible to its pulse orbit.** For arbitrarily small \(\varepsilon>0\), eventually \(0<I(t)<\varepsilon\). Thus on subsequent pulse intervals, \(S\) is squeezed between the logistic flows \(\dot S=S(A-\beta\varepsilon-S)\) and \(\dot S=S(A-S)\), with the same multiplier \(q\) at pulses. Their stroboscopic maps have attracting positive fixed points
\[
s_*(a)=\frac{a(qe^{aT}-1)}{e^{aT}-1},\quad a=A-\beta\varepsilon\text{ or }A,
\]
provided \(\varepsilon\) is small enough that \(qe^{(A-\beta\varepsilon)T}>1\). The susceptible floor excludes the zero equilibrium. Comparison and then \(\varepsilon\downarrow0\) show \(S_n\to s_*\); continuous dependence on each bounded pulse interval yields \(S(nT+\tau)\to s(\tau)\) uniformly.

**4. Exact inverse-product integration and infection profile.** The identity in step 2 gives
\[
\frac{d}{dt}\frac1{L(t)}
=\frac{\beta^2}{q^{\beta\tau/T}S(t)^\beta}.
\]
Integrating over complete periods and using the uniform convergence in step 3 gives, by Cesàro averaging,
\[
\lim_{n\to\infty}\frac1n\frac1{L(nT^+)}
=\beta^2\int_0^T q^{-\beta\tau/T}s(\tau)^{-\beta}\,d\tau=C.
\]
Since \(L(nT+\tau)/L(nT^+)\to1\) uniformly for \(0\le\tau<T\), it follows that \(nL(nT+\tau)\to1/C\). Multiplying by \(q^{-\beta\tau/T}S(nT+\tau)^{-\beta}\) proves the infection formula.

**5. Susceptible correction.** The impulse-continuous ratio \(z(t)=\log[S(t)/s(\tau)]\) obeys the exact equation
\[
\dot z=-s(\tau)(e^z-1)-\beta I=-a(t)z-\beta I,
\quad a(t)=s(\tau)\frac{e^z-1}{z},
\]
with the continuous extension \(a=s\) at \(z=0\). We have \(a(t)\to s(\tau)>0\) uniformly over phases. Variation of constants, exponential decay of the linear kernel, and \(I(nT+\tau)=O(1/n)\) imply \(z(nT+\tau)=O(1/n)\) uniformly. Multiply the variation-of-constants expression by \(n\). Terms at fixed backward time separations converge, using \(nI(nT+\tau)\to w(\tau)/C\), and the exponentially small distant-past tail is negligible. The limit is the unique bounded periodic solution of \(u'+su=-\beta w/C\), namely \(u=-k/C\) with the formula above. Since \(S=s e^z\), we obtain \(n(S-s)\to-sk/C\) uniformly. Strict positivity of \(k\) follows from its explicit representation and positivity of \(s,w\). This completes the proof.

## Verification

The standalone `check.py` requires Python 3, SymPy and mpmath; run `python check.py`. It verifies the exact weighted-logarithmic derivative symbolically and compares the exact integrated reciprocal-product identity and both fixed-phase infected limits against three explicit positive-parameter trajectories. Its reported convergence tolerances concern finite trajectories and numerical quadrature, not an infinite proof. The proof's key global steps are the strict Lyapunov product, the susceptible-floor argument, scalar logistic comparison and Cesàro reciprocal integration. No external numerical data or paid software are required.

## Relationship to prior work

Maurício de Carvalho and Rodrigues (2023 preprint, 2024 journal article) introduce precisely this logistic-susceptible impulsive SIR reduction, derive the disease-free periodic orbit and the reproduction threshold, and identify a transcritical boundary. Their Theorem A states the global alternatives on open parameter regions on either side, rather than the equality case, and their sections on Floquet stability do not provide the pulse-continuous Lyapunov product or the phase-resolved critical clearance coefficient. This theorem addresses that boundary without claiming novelty for the model or for its threshold. Other published work on stage-structured pulses (Zhou, Sattayatham and Jiao, 2016) and on a linearly implicit pulse-SIR numerical method (Zhang and coauthors, 2024) uses materially different state dynamics; their qualitative thresholds do not directly imply the present profile. Generic center-manifold predictions of reciprocal-time slowing do not by themselves establish the global basin, the exact pulse-continuous identity, or the full phase coefficient.

## Limitations

The result concerns the deterministic unseasonal two-variable reduced system with a fixed proportional pulse at exact threshold and excludes infection-free starting points from the reciprocal-amplitude conclusion. It does not cover seasonally varying transmission, stage structure, state-dependent pulse sizes, noise or arbitrary impulse schedules. The leading amplitudes are asymptotic and are not finite-time estimates. No publication-priority claim is made against inaccessible or unindexed equivalent mathematical work, and no independent audit is asserted.

## References

- J. P. S. Maurício de Carvalho and A. A. Rodrigues, *Pulse vaccination in a SIR model: global dynamics, bifurcations and seasonality*, first public arXiv version 2023-12-04, arXiv:2312.02306, https://arxiv.org/abs/2312.02306 ; journal version, *Communications in Nonlinear Science and Numerical Simulation* 139 (2024), 108272, https://doi.org/10.1016/j.cnsns.2024.108272 . An author-uploaded full-text HTML transcription was consulted: https://www.researchgate.net/publication/383190903_Pulse_vaccination_in_a_SIR_model_Global_dynamics_bifurcations_and_seasonality .
- A. Zhou, P. Sattayatham and J. Jiao, *Dynamics of an SIR epidemic model with stage structure and pulse vaccination*, *Advances in Difference Equations* 2016:140, https://doi.org/10.1186/s13662-016-0853-z .
- G.-L. Zhang, Z.-Y. Zhu, L.-K. Chen and S.-S. Liu, *Impulsive Linearly Implicit Euler Method for the SIR Epidemic Model with Pulse Vaccination Strategy*, *Axioms* 13 (2024), 854, https://doi.org/10.3390/axioms13120854 .

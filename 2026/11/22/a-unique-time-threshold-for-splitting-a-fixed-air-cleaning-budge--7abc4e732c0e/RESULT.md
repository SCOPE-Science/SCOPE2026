# A unique time threshold for splitting a fixed air-cleaning budget after a two-room pollution pulse

## Finding
For every exchange rate \(k>0\), removal budget \(F>0\), baseline removal \(a\geq0\), impulse size \(Q>0\) and assessment time \(t>0\), consider two equally sized well-mixed rooms with symmetric exchange. One pulse enters room 1 at time zero; the total supplemental first-order removal rate \(F\) is divided, once and held constant, between the rooms. Minimizing the residual **source-room** concentration has a unique critical assessment time \(t_c(k,F)>0\). At and below this time, all supplemental removal belongs in room 1. After this time the unique optimum strictly splits removal between both rooms, allocating more to room 1; its source-room excess over half the budget equals \(1/t+O(t^{-2})\) as \(t\to\infty\). In contrast, minimizing residual **remote-room** concentration always has the unique equal-split allocation. The optimal allocations are independent of \(a\) and \(Q\).

Put \(z= (f_1-f_2)/2\), where \(f_1+f_2=F\), and \(s=F/2\). Then \(-s\le z\le s\), \(\omega(z)=\sqrt{k^2+z^2}\), and \(c=a+k+s\). For \(r=s/\omega(s)\), define \(u_c\) as the unique positive zero of
\[
L_r(u)=ur(1-r\coth u)-(1-r^2).
\]
Then \(t_c=u_c/\omega(s)\). For \(t>t_c\), the unique source-optimal allocation is \(f_1=s+z_*(t)\), \(f_2=s-z_*(t)\), where \(z_*(t)\in(0,s)\) is the unique root of \(L_{z/\omega(z)}(t\omega(z))=0\).

## Assumptions and scope
The two rooms have equal modeled volumes and perfectly mixed concentrations. Exchange between rooms follows constant symmetric first-order rate \(k\), and a background removal rate \(a\) acts in both rooms. The additional cleaning rates \(f_1,f_2\geq0\) are each constant throughout the observation interval and satisfy \(f_1+f_2=F>0\); there are no switching or capacity constraints beyond the shared budget. There is no continuing emission after an instantaneous concentration pulse. The state obeys
\[
\frac{d}{dt}\begin{pmatrix}x_1\\x_2\end{pmatrix}
=\begin{pmatrix}-(a+k+f_1)&k\\k&-(a+k+f_2)\end{pmatrix}
\begin{pmatrix}x_1\\x_2\end{pmatrix},\qquad
(x_1(0),x_2(0))=(Q,0).
\]
The objectives are separate: minimize either \(x_1(t)\) or \(x_2(t)\) over constant allocations at a fixed \(t>0\). These objectives need not select the same allocation. All quantifiers and boundary cases are included in the stated strict parameter ranges; \(F=0\), \(k=0\), and variable-control policies are excluded.

## Proof
Exponentiating the two-by-two matrix gives, for \(\omega=\sqrt{k^2+z^2}\),
\[
 x_1(t;z)=Qe^{-ct}\left(\cosh(t\omega)-\frac z\omega\sinh(t\omega)\right),\qquad
 x_2(t;z)=Qe^{-ct}\frac k\omega\sinh(t\omega).
\]
Because \(\sinh(t\omega)/\omega\) is strictly increasing in \(\omega>0\) for every \(t>0\) (its derivative has numerator \(t\omega\cosh(t\omega)-\sinh(t\omega)>0\)), the remote-room expression has its unique minimum at \(z=0\).

To establish *global* rather than local source optimality, let \(X\) be a continuous-time two-state symmetric jump chain of rate \(k\), begun at state 1, and define \(Y=\int_0^t(\mathbf1_{\{X_v=1\}}-\mathbf1_{\{X_v=2\}})\,dv\). The finite-state Feynman–Kac formula yields
\[
\cosh(t\omega)-\frac z\omega\sinh(t\omega)
=e^{kt}\mathbb E_1[e^{-zY}\mathbf1_{\{X_t=1\}}].
\]
Its second derivative with respect to \(z\) is strictly positive since the no-jump event has probability \(e^{-kt}>0\) and contributes \(Y=t\neq0\). Thus \(x_1(t;z)\) is strictly convex on the whole feasible interval. Also the source expression is strictly smaller at \(z>0\) than at \(-z\); hence its unique minimizer is strictly positive. Its derivative at \(z=0\) is negative.

At each \(z>0\), writing \(r_z=z/\omega(z)\in(0,1)\), \(u=t\omega(z)>0\), direct differentiation gives
\[
\frac{e^{ct}}Q\frac{\partial x_1}{\partial z}
=\frac{\sinh u}{\omega(z)}\left[ur_z(1-r_z\coth u)-(1-r_z^2)\right]
=\frac{\sinh u}{\omega(z)}L_{r_z}(u).
\]
For each fixed \(0<r<1\), \(L_r(u)\to-1\) as \(u\downarrow0\), and \(L_r(u)\to+\infty\) as \(u\to\infty\). Moreover
\[
L'_r(u)=r\{1-r[\coth u-u\operatorname{csch}^2u]\}>0.
\]
Indeed \(0<\coth u-u\operatorname{csch}^2u<1\) for \(u>0\): this function increases from 0 to 1, as its derivative is \(2\operatorname{csch}^2u(u\coth u-1)>0\). Consequently the endpoint derivative at \(z=s=F/2\) crosses zero at exactly \(t_c=u_c/\omega(s)\). Strict convexity implies the global optimum is \(z=s\) when \(t\leq t_c\), and otherwise is the unique interior root of the displayed derivative equation, with \(0<z_*(t)<s\).

For the long-time law, strict convexity and the derivative equation ensure \(z_*(t)\to0\), because for any fixed \(z>0\) the positive leading term \(t z(1-z/\omega(z))\) eventually dominates. At the optimum, write \(r=z_*(t)/\omega(z_*(t))\). Then \(t z_*(t)=(1-r^2)/(1-r\coth(t\omega(z_*(t))))=1+O(z_*(t))\), since \(r=O(z_*(t))\) and \(\coth(t\omega)\leq\coth(tk)\) is bounded as \(t\to\infty\). This first gives \(z_*(t)=O(t^{-1})\), and substitution yields \(z_*(t)=t^{-1}+O(t^{-2})\). The factor \(Qe^{-ct}\) shows independence of baseline removal and initial magnitude.

## Verification
A standalone Python standard-library checker, `check.py`, evaluates the closed-form matrix-exponential concentrations and uses bisection to solve the analytic endpoint and interior equations. It tests an exact parameter choice \(k=1\), \(F=2\), for which \(t_c\approx1.76533153566341\); 3,500 reproducibly seeded parameter draws, each compared against 21 alternative allocations for both objectives; transition classifications; and long-time scaling. The checker reports 154,010 successful supplementary assertions. These finite numerical checks supplement, but do not establish, the all-parameter proof.

For \(k=1\), \(F=2\), \(a=0.2\), \(Q=1\): at \(t=1\) the unique source-room optimum is \((f_1,f_2)=(2,0)\); at \(t=2\), approximately \((1.8373825769,0.1626174231)\); the remote-room optimum is \((1,1)\) at both times.

## Relationship to prior work
Matthews and colleagues (2024) measured room-to-room tracer exchange and pollutant persistence in a multizone home; that empirical work motivates the two-room abstraction but does not give its optimal fixed-budget split. Pei and colleagues (2024) used computational fluid dynamics to examine portable cleaner placement in a classroom rather than a strict two-zone constant-budget concentration pulse. Kikumoto and Ooka (2022) used adjoint concentration fields to study spatial cleaner placement. Blanchini and colleagues (2023) solved a general class of compartmental optimal-control problems with time-dependent controls and different intervention constraints; a time-varying optimum or unconstrained control does not supply the theorem about time-*constant* sink rates whose sum is fixed. Related exact two-box tracer studies have optimized exchange speed, not the distribution of removal capacity. The hyperbolic identities and stochastic representation use established mathematics; the result concerns their combined fixed-budget terminal-optimum classification. The novelty claim is limited to the inspected literature.

## Limitations
The model neglects particle-size distributions, nonuniform mixing, room volume disparities, occupancy, time-varying sources, fan-induced exchange changes, concentration-dependent capture, stochastic variability, uncertainty and measurement noise. The result compares two distinct terminal objectives, not integrated exposure or realistic comfort/cost objectives. The unrestricted time-dependent-control problem is different. No claim of environmental calibration, field effectiveness, human health impact, or historical uniqueness is made. Independent external validation is not available.

## References
1. Matthews et al., “Indoor Exchange Rates and Penetration From Outdoors in an Instrumented Terraced House (Townhouse) Using Gas Tracers: Implications for Particles and Gases Indoors,” *Indoor Air* (2024), first published October 21, 2024. https://doi.org/10.1155/2024/9204433.
2. Pei, Azimi, Rim, and Allen, “A CFD study on the effect of portable air cleaner placement on airborne infection control in a classroom,” *Environmental Science: Processes & Impacts* (2024), first published July 4, 2024. https://doi.org/10.1039/D4EM00114A.
3. Kikumoto and Ooka, “Study on influence of air cleaner on room dispersion field and its optimal placement using adjoint concentration,” (2022). https://onlinelibrary.wiley.com/doi/full/10.1002/2475-8876.12318.
4. Blanchini et al., “Optimal control of compartmental models: The exact solution,” *Automatica* (2023), DOI https://doi.org/10.1016/j.automatica.2022.110680; open manuscript https://giuliagiordano.dii.unitn.it/docs/papers/Journal/J061_2023_Automatica.pdf.

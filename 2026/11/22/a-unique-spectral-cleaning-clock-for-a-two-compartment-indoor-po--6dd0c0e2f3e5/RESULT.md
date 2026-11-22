# A unique spectral cleaning clock for a two-compartment indoor pollutant reservoir

## Finding

Consider an indoor pollutant that exchanges linearly between well-mixed air and one sorbing surface reservoir after a short air-only pollution pulse. Suppose a single instantaneous cleaning removes any fixed positive fraction of the reservoir at a chosen time during a finite exposure horizon. There is exactly **one** optimal cleaning time. It is determined by the two uncleaned exponential decay rates alone, not by cleaning efficacy or the initial dose. The optimum grows strictly with the monitoring horizon, starts asymptotically one-third of the way through very short horizons, and approaches the time of maximum surface burden for long horizons.

Writing the fast and slow decay rates as \(r>s>0\), define
\[
f(t)=e^{-st}-e^{-rt},\qquad L(t)=\int_0^t f(u)\,du.
\]
The cleaning-induced reduction in time-integrated airborne concentration is an explicit positive multiple of \(f(\tau)L(T-\tau)\). Consequently, its unique maximizing time \(\tau_*(T)\) is the solution in \((0,T)\) of
\[
\frac{f'(\tau_*)}{f(\tau_*)}=\frac{f(T-\tau_*)}{L(T-\tau_*)}.
\]
This provides a one-dimensional, strictly monotone root problem without dynamic optimization over interventions.

## Assumptions and scope

Let \(v,a,d,Q,T\) be strictly positive constants, and let cleaning efficacy satisfy \(0<q\le1\). Airborne pollutant mass per unit reference volume \(G\) and surface-associated mass in the same units \(W\) satisfy, between interventions,
\[
\dot G=-(v+a)G+dW,\qquad \dot W=aG-dW,\qquad (G(0),W(0))=(Q,0).
\]
At one chosen \(\tau\in[0,T]\), instantaneous physical removal changes \((G(\tau^-),W(\tau^-))\) into \((G(\tau^-),(1-q)W(\tau^-))\). No pollutant is added by this operation. Subsequent kinetics and all rate constants are unchanged. The cost to minimize is cumulative gas-phase burden \(J_T(\tau)=\int_0^T G_\tau(t)\,dt\), including both sides of the intervention. An intervention at either endpoint has zero effect on this finite-horizon objective.

The two positive decay rates \(r>s\) are the roots of
\[
z^2-(v+a+d)z+vd=0.
\]
The discriminant is strictly positive, and \(0<s<d<r\). Set \(k=r-s\), and write
\[
L(u)=\frac{1-e^{-su}}s-\frac{1-e^{-ru}}r,\qquad
 t_0=\frac{\log(r/s)}{r-s}.
\]
The quantity \(t_0\) is the unique peak time of the uncleaned surface concentration.

**Theorem.** For every choice of the parameters above, the reduction \(B_T(\tau)=J_T(\text{no cleaning})-J_T(\tau)\) equals
\[
B_T(\tau)=\frac{qQad}{(r-s)^2}\bigl(e^{-s\tau}-e^{-r\tau}\bigr)
\left[\frac{1-e^{-s(T-\tau)}}s-\frac{1-e^{-r(T-\tau)}}r\right].
\]
For each \(T>0\), it has exactly one maximizer, \(0<\tau_*(T)<\min\{T,t_0\}\). The mapping \(T\mapsto\tau_*(T)\) is strictly increasing. Moreover,
\[
\tau_*(T)=\frac T3-\frac{r+s}{81}T^2+O(T^3)
\qquad(T\downarrow0),
\]
and
\[
t_0-\tau_*(T)\sim\frac{e^{-s(T-t_0)}}{r-s}
\qquad(T\to\infty).
\]
In particular, \(\tau_*(T)\) is independent of \(Q\), \(q\) and every change of \((v,a,d)\) preserving both modal rates \((r,s)\). The expression concerns one removable reservoir and one post-pulse cleaning, not a general multi-event or continuously controlled system.

## Proof

1. **Decay modes and positivity.** For the generator
\[
M=\begin{pmatrix}-(v+a)&d\\a&-d\end{pmatrix},
\]
its eigenvalues are \(-r\) and \(-s\). The polynomial defining the rates has positive value at \(0\), negative value at \(d\), and positive leading coefficient; hence \(0<s<d<r\). Direct matrix-exponential evaluation gives the uncleaned surface state
\[
W(t)=\frac{Qa}{k}f(t),
\]
and the air response at lag \(u\) to one unit initially on the surface,
\[
(e^{Mu})_{12}=\frac d k f(u).
\]
For completeness, the uncleaned airborne state is
\[
G(t)=\frac Qk\left[(r-d)e^{-rt}+(d-s)e^{-st}\right].
\]
Both modal coefficients in this air formula are positive, so the two rates are, in principle, observable from an ideal noiseless decay trace.

2. **Exact finite-horizon benefit.** Cleaning at time \(\tau\) removes \(qW(\tau)\) from the surface. By linearity the removed portion would have produced extra air concentration \(qW(\tau)d f(t-\tau)/k\) at future time \(t>\tau\). Integration proves
\[
B_T(\tau)=\frac{qQad}{k^2}f(\tau)L(T-\tau).
\]
Both factors are positive for \(0<\tau<T\); the benefit vanishes at \(\tau=0,T\).

3. **Strict logarithmic concavity and uniqueness.** The function
\[
\log f(t)=-st+\log(1-e^{-kt}),\qquad t>0,
\]
has second derivative \(-k^2e^{kt}/(e^{kt}-1)^2<0\). Also \(\log L(t)\) is strictly concave. To verify the latter without a closure theorem, note that \(L'=f\) and \(L''=f'\), so the required inequality is \(f'L-f^2<0\). It is immediate if \(f'\le0\). If \(f'(t)>0\), strict concavity of \(\log f\) gives, with \(c=f'(t)/f(t)>0\),
\[
f(x)<f(t)e^{c(x-t)}\quad(0<x<t).
\]
Thus \(L(t)<f(t)(1-e^{-ct})/c<f(t)/c\), implying \(f'(t)L(t)<f(t)^2\). Therefore \(\log B_T(\tau)=\log f(\tau)+\log L(T-\tau)+\text{constant}\) is strictly concave. Its endpoint behavior gives one and only one interior maximum, characterized by the stated stationarity equation.

4. **Position and horizon monotonicity.** The derivative \(f'\) changes sign only at \(t_0=\log(r/s)/k\), and the right-hand side of the stationarity equation is strictly positive. Therefore \(\tau_*(T)<t_0\). Define \(g=f'/f\) and \(h=f/L\). Strict log-concavity yields \(g'<0\), \(h'<0\). The optimum is the zero of \(F(\tau,T)=g(\tau)-h(T-\tau)\), with
\[
\partial_\tau F=g'(\tau)+h'(T-\tau)<0,\qquad
\partial_TF=-h'(T-\tau)>0.
\]
Implicit differentiation gives \(d\tau_*/dT=-F_T/F_\tau>0\). Since the optimum is below \(t_0\), it remains bounded as \(T\) grows. As \(T\to\infty\), \(h(T-\tau)\to0\), so its limit is the unique zero \(t_0\) of \(g\).

5. **Endpoint asymptotics.** The expansions
\[
f(t)=kt\left(1-\frac{r+s}{2}t+O(t^2)\right),\quad
L(u)=\frac{k u^2}{2}\left(1-\frac{r+s}{3}u+O(u^2)\right)
\]
inserted into the first-order equation yield \(\tau_*(T)=T/3-(r+s)T^2/81+O(T^3)\). For the other limit, \(h(u)\sim sr\,e^{-su}/k\) as \(u\to\infty\) and \(g'(t_0)=-sr\). Linearizing the stationarity equation at \(t_0\) gives \(t_0-\tau_*(T)\sim e^{-s(T-t_0)}/k\). The assertions follow.

## Verification

The accompanying standalone `verify.py` uses only Python standard-library functions and directly checks the modal benefit against independently integrated two-compartment ODE trajectories (fourth-order Runge–Kutta), as well as global comparisons over randomized parameter grids, spectral invariance, both asymptotic laws and a reproducible numerical example. Running `python3 verify.py` gave `PASS 31536 numerical comparisons`. These finite numerical checks are supplements to the analytic proof and do not establish an infinite-parameter theorem by themselves.

For illustration only, take rates (per hour) \(v=0.2\), \(a=1\), \(d=0.1\), horizon \(T=12\) hours, initial normalized pulse \(Q=1\) and cleaning efficacy \(q=0.5\). Then \((r,s)=(1.284428877022476,0.015571122977524)\) per hour and \(t_0=3.477656437926\) hours. The unique minimizing cleaning time is \(\tau_*=1.954697195672\) hours. The baseline integrated air burden is \(1.455061340407\) (normalized concentration-hours), with a cleaning benefit of \(0.235189905680\) or \(16.16\%\); cleaning at hour \(6\) instead yields benefit \(0.139947055534\). No parameters here are asserted to have been fitted to a building or pollutant species.

## Relationship to prior work

Li and colleagues (2023) experimentally demonstrate persistent smoke-derived volatile organic compounds in indoor air due to gas–surface partitioning and describe the same linear adsorption–desorption/ventilation differential equations. Their experiments establish the relevance of physically removing reservoirs and report consequences of different cleaning actions. They do not state the above one-intervention finite-horizon optimum, strict uniqueness, spectral-only invariance, or the one-third short-horizon law in the inspected main text.

Lei, Jones and Li (2017) studied surface-cleaning timing in a multicompartment hospital contact-transmission model, including cleaning-frequency and efficacy effects; their objective and state transition are not the source-free gas–surface airborne integral considered here. Blanchini and colleagues (preprint 2022; subsequent journal version 2023) solve a broad class of optimal positive-compartmental models with *continuously varying controlled arc flows* and associated optimal switching, not a one-time instantaneous reset of one state in an otherwise fixed two-compartment generator. These works establish the modeling and positive-system/control context and are not superseded by the present special-purpose theorem. Earlier general convolution and log-concavity facts are used as standard proof techniques, not claimed as new.

No inspected primary result gave the same exact one-wipe objective or proved the finite-horizon uniqueness and two asymptotic laws. This is a best-knowledge literature comparison, not a proof of exhaustive historical novelty. The general observation that surface cleaning reduces pollutant reservoirs is known and is not part of the originality claim.

## Limitations

This theorem is restricted to a well-mixed, source-free, *single-surface* linear exchange model with constant rates, an initial air-only pulse and exactly one instantaneous removal event of fixed fractional effectiveness. The action does not release new chemicals, change adsorption sites or rates, involve worker exposure during cleaning, or incur timing-dependent cost. Those assumptions may fail in occupied or highly heterogeneous real buildings. The optimum maximizes reduction of the total gas-phase integral over a predetermined horizon, rather than instantaneous concentration, acute peak, final concentration, or a full health-risk metric. Data-fitting identifiability and practical feasibility with noisy measurements are not proved. Long-horizon asymptotics concern positive fixed rate constants and are not uniform over parameter limits where a rate vanishes or modes merge. Independent external validation has not been conducted.

## References

1. J. Li et al., “The persistence of smoke VOCs indoors: Partitioning, surface cleaning, and air cleaning in a smoke-contaminated house,” *Science Advances* **9** (2023), eadh8263, first public issue October 13, 2023. https://doi.org/10.1126/sciadv.adh8263 . Full open article: https://pmc.ncbi.nlm.nih.gov/articles/PMC10575580/ . Equations (1)–(2), gas/surface dynamics; Results and Discussion, surface cleaning.
2. H. Lei, R. M. Jones and Y. Li, “Exploring surface cleaning strategies in hospital to prevent contact transmission of methicillin-resistant Staphylococcus aureus,” *BMC Infectious Diseases* **17** (2017), 85. https://doi.org/10.1186/s12879-016-2120-z . Full open text, Methods and Results.
3. F. Blanchini, P. Bolzern, P. Colaneri, G. De Nicolao and G. Giordano, “Optimal control of compartmental models: the exact solution,” *Automatica* **147** (2023), 110680. https://doi.org/10.1016/j.automatica.2022.110680 . Lawful author preprint, September 2022: https://iris.unitn.it/retrieve/cd15dadf-d327-4a44-9014-aac0cddefec4/Automatica_OptimalControl.pdf . Model and finite-horizon control sections.

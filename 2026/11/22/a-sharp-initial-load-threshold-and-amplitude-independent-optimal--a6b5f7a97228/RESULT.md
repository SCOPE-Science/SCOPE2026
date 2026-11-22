# A sharp initial-load threshold and amplitude-independent optimal air-cleaning window

## Finding
For a well-mixed indoor contaminant with constant emission and removal, one prescribed-duration cleaning window has an exact, globally unique best start time for minimizing total concentration exposure. Its timing does not depend on how much stronger the cleaning rate is than baseline, as long as it is strictly stronger. An exact initial-concentration threshold separates starting immediately from delaying the cleaner, and exact regret identities quantify every mistimed window.

Set the duration left outside the cleaning window to \(U=T-h\). For positive baseline removal \(b>0\), if \(C_0\ge (q/b)(1-e^{-bU})\), the unique optimum is \(\tau_*=0\). Otherwise it is the unique interior point
\[
\tau_* = \frac{U}{2}+\frac{\log(1-bC_0/q)}{2b}.
\]
For zero baseline removal \(b=0\), the unique optimum is \(\tau_*=\max\{0,(U-C_0/q)/2\}\). These formulas apply to every stronger cleaning rate \(a>b\), without approximation.

## Assumptions and scope
Let \(q>0\) be constant volumetrically normalized emission, \(C_0\ge0\) initial indoor concentration, \(0<h<T\) a fixed cleaning duration, and \(a>b\ge0\) constant augmented and baseline first-order removal rates. For each start \(\tau\in[0,T-h]\), define \(C_\tau:[0,T]\to[0,\infty)\) to be the unique continuous, piecewise differentiable solution of
\[
\dot C_\tau(t)=q-r_\tau(t)C_\tau(t),\qquad C_\tau(0)=C_0,
\]
where \(r_\tau(t)=a\) for \(\tau\le t<\tau+h\), and \(r_\tau(t)=b\) otherwise. Minimize \(J(\tau)=\int_0^T C_\tau(t)\,dt\). Nonnegative concentration is automatic. A constant breathing or dose factor rescales \(J\) and does not alter the optimizer. No claims are made about arbitrary switching calendars, changing emission, multiple zones, or energy objectives.

## Proof
Define for \(r\ge0\) and \(s\ge0\)
\[
A_r(s)=\begin{cases}(1-e^{-rs})/r,&r>0,\\s,&r=0,\end{cases}\quad
B_r(s)=\begin{cases}(s-A_r(s))/r,&r>0,\\s^2/2,&r=0.\end{cases}
\]
An interval of length \(s\) and rate \(r\), entering with concentration \(z\), exits at \(e^{-rs}z+qA_r(s)\) and contributes exactly \(zA_r(s)+qB_r(s)\) to integrated exposure. Compose the three intervals \((b,\tau),(a,h),(b,U-\tau)\). Direct differentiation of these elementary expressions yields, for \(G=(1-b/a)(1-e^{-ah})>0\),
\[
J'(\tau)=G\begin{cases}
(C_0-q/b)e^{-b\tau}+(q/b)e^{-b(U-\tau)},&b>0,\\
C_0+q(2\tau-U),&b=0.
\end{cases}
\]
This identity extends continuously to either endpoint by one-sided differentiation. It can also be checked using the exact segment formula without any asymptotic argument.

For \(b>0\), put \(E=q/b>0\). If \(C_0\ge E\), both terms in the expression for \(J'\) make its sum strictly positive: equivalently \(J'/G=C_0e^{-b\tau}+E(e^{-b(U-\tau)}-e^{-b\tau})\), and the equality case \(C_0=E\) directly gives positivity. More generally, when \(C_0<E\), the derivative is strictly increasing because
\[
J''(\tau)=Gb\big[(E-C_0)e^{-b\tau}+E e^{-b(U-\tau)}\big]>0.
\]
At \(\tau=U\), the derivative is strictly positive in this case. At \(\tau=0\), it is nonnegative exactly when \(C_0\ge E(1-e^{-bU})\). Therefore above or at that threshold the unique minimum is at zero; below it, a unique derivative zero occurs inside \((0,U)\). Solving \((E-C_0)e^{-b\tau}=Ee^{-b(U-\tau)}\) gives the displayed logarithmic formula. The threshold is strictly below \(E\), so the logarithm is defined throughout its intended regime. At the threshold the derivative vanishes only at zero, and strict convexity for \(C_0<E\) proves uniqueness.

For \(b=0\), the derivative is affine with strictly positive slope \(2Gq\), and it is positive at \(\tau=U\). Its unique constrained minimizer is exactly \(\max\{0,(U-C_0/q)/2\}\), including the borderline case. Since the multiplicative factor \(G>0\) never affects the sign of the derivative, the optimum is independent of the enhanced rate \(a\). Only \(a>b\) and \(h>0\) are required.

For completeness, the full cost of mistiming is also exact. If \(b>0\) and \(\tau_*>0\), let \(k=E e^{-b(U-\tau_*)}\); then every admissible \(\tau\) obeys
\[
J(\tau)-J(\tau_*)=\frac{2Gk}{b}\big[\cosh(b(\tau-\tau_*))-1\big].
\]
For \(b=0\) and \(\tau_*>0\), the regret is \(Gq(\tau-\tau_*)^2\). When \(\tau_*=0\), the identities become, respectively,
\[
J(\tau)-J(0)=\frac{G}{b}\big[(C_0-E)(1-e^{-b\tau})+Ee^{-bU}(e^{b\tau}-1)\big]
\]
and \(J(\tau)-J(0)=G[(C_0-qU)\tau+q\tau^2]\). The derivative analysis proves these are positive for every \(\tau>0\). Integration of \(J'\) proves each regret formula and closes the global argument.

## Verification
The self-contained `check.py` implements both exact interval-composition formulas and the independent closed-form derivative, optimum, and regret identities. Running `python check.py` makes 71,003 deterministic assertions against 1,000 pseudorandom parameter configurations, including zero and positive baseline removal, global comparison with 63 candidate times per configuration, finite-difference derivative checks, exact regrets, and independence of the enhanced rate. Its canonical instance \((q,b,a,T,h,C_0)=(1,1,3,4,1,0)\) has unique \(\tau_*=1.5\), with exposures \(J(0)\approx2.578509392222\) and \(J(1.5)\approx2.196190111820\), a reduction of approximately \(14.8271\%\) relative to an immediate cleaning window. The infinite-parameter theorem is justified by the analytic identities above; finite tests are only diagnostics.

## Relationship to prior work
Kusiak and Li (2009) use a one-room carbon-dioxide mass balance and optimize binary ventilation scheduling through multiobjective evolutionary computation, trading off fan operating time and concentration-threshold violations. Their scheduling objectives are different from minimizing exact total concentration exposure with one fixed-duration enhanced-removal window, and their analyzed model does not supply the rate-independent start-time rule and global regret identities proved here. The earlier NIST simulations (2003) evaluate indoor pollutant impacts under alternative demand-controlled ventilation strategies, rather than a complete single-window analytic optimum. Risbeck and colleagues (2021) develop a richer dynamic HVAC and airborne-exposure optimization framework; its model and objectives are more general but its reported optimization does not explicitly solve the fixed-source, single-window all-rate start-time problem. This special-case theorem is not asserted to be a discovery of the mass-balance model itself or a general characterization of optimal HVAC systems.

## Limitations
The idealization assumes perfect mixing, continuous observation exposure over a fixed horizon, a truly constant emission rate, known initial load, constant baseline and boosted removal, no contaminant introduced by ventilation, and a single mandatory cleaning window with prescribed length. Noise, uncertain occupancy, time-varying emissions or breathing, multiple cleanings, instantaneous peak constraints, infection-dose nonlinearity, device energy or actuation costs, and spatial heterogeneity are outside the claim. Historical priority is provisional; similar results may occur under other optimal-control terminology, and mathematical exactness does not imply operational efficacy in real buildings.

## References
1. A. Kusiak and M. Li, "Optimal decision making in ventilation control," *Energy* **34** (2009), 1835–1845, doi:10.1016/j.energy.2009.07.039. First publicly available online 2009-08-15, as stated in the article's publication history. https://www.academia.edu/14159901/Optimal_decision_making_in_ventilation_control
2. NIST, "Simulations of Indoor Air Quality and Ventilation Impacts of Demand Controlled Ventilation in Commercial and Institutional Buildings," NISTIR 7042 (2003). https://www.nist.gov/publications/simulations-indoor-air-quality-and-ventilation-impacts-demand-controlled-ventilation-0
3. M. J. Risbeck et al., "Modeling and multiobjective optimization of indoor airborne disease transmission risk and associated energy consumption for building HVAC systems," *Energy and Buildings* **253** (2021), 111497, doi:10.1016/j.enbuild.2021.111497. https://pmc.ncbi.nlm.nih.gov/articles/PMC8457902/

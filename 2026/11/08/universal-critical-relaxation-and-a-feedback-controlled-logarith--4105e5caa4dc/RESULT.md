# Universal critical relaxation and a feedback-controlled logarithmic correction in the SIRCm flow

## Finding

At the exact epidemic threshold \(\beta=\mu+\alpha\), both the prevalence-driven and transmission-driven four-compartment SIRCm flows have globally attracting disease-free dynamics. Every solution with initially positive infection satisfies a universal two-term critical expansion, independently of the initial susceptible, recovered, and cross-immune fractions:

\[
\frac{1}{I(t)}=Kt+\frac{L}{K}\log t+H+o(1),\qquad t\to\infty,
\]

where \(H\) depends on the initial state, but the coefficients \(K>0\) and \(L\) are explicit in the model parameters and **identical for the two nonlinear feedback choices**. The leading extinction amplitude is feedback-independent, \(tI(t)\to K^{-1}\), while the logarithmic term is feedback-sensitive and can reverse sign.

Put \(A=\mu+\delta\), \(B=\mu+\gamma\), and define

\[
\begin{aligned}
a&=\frac{\alpha}{A},&c&=\frac{\delta a}{B},\\
K&=\beta[1+a+(1-\sigma)c],\\
b&=\frac{aK+(1-\sigma)\beta c-\varepsilon_1\delta a}{A},\\
d&=\frac{cK+\delta b+\varepsilon_1\delta a-\beta c-\varepsilon_2\gamma c}{B},\\
L&=\beta[b+(1-\sigma)d].
\end{aligned}
\]

For every initially infected solution, the following expansions hold along its trajectory:

\[
\begin{aligned}
R(t)&=aI(t)+bI(t)^2+O(I(t)^3),\\
C(t)&=cI(t)+dI(t)^2+O(I(t)^3),\\
I(t)&=\frac{1}{Kt}-\frac{L}{K^3}\frac{\log t}{t^2}+O(t^{-2}).
\end{aligned}
\]

For the concrete rate choice \(\mu=\alpha=\delta=\gamma=1\), \(\beta=2\), \(\sigma=1\), and arbitrary \(\varepsilon_1,\varepsilon_2\geq0\), one obtains \(K=3\), \(L=(3-\varepsilon_1)/2\), and hence

\[
\frac1{I(t)}=3t+\frac{3-\varepsilon_1}{6}\log t+H+o(1).
\]

The logarithmic correction is positive for \(\varepsilon_1<3\), zero at \(\varepsilon_1=3\), and negative for \(\varepsilon_1>3\), for **both** feedback choices. In particular, \(\varepsilon_2\) may be arbitrary in this example.

## Assumptions and scope

The state is \((S,I,R,C)\) in the nonnegative unit simplex \(\Omega=\{S+I+R+C=1\}\). Let \(\mu,\alpha,\delta,\gamma>0\), \(\beta=\mu+\alpha\), \(0\le\sigma\le1\), and finite \(\varepsilon_1,\varepsilon_2\ge0\). Choose either \(g(S,I,R,C)=I\) (prevalence-driven) or \(g(S,I,R,C)=SI\) (transmission-driven). The autonomous differential equations are

\[
\begin{aligned}
\dot S&=\mu(1-S)-\beta SI+\gamma(1+\varepsilon_2g)C,\\
\dot I&=\beta SI+\sigma\beta CI-(\mu+\alpha)I,\\
\dot R&=(1-\sigma)\beta CI+\alpha I-\mu R-\delta(1+\varepsilon_1g)R,\\
\dot C&=\delta(1+\varepsilon_1g)R-\beta CI-\mu C-\gamma(1+\varepsilon_2g)C.
\end{aligned}
\]

The conserved simplex is forward invariant by quasipositivity and the mass balance. All asymptotic expansions assume \(I(0)>0\); if \(I(0)=0\), infection remains absent and the other coordinates converge exponentially to the disease-free equilibrium. No uniformity over unbounded feedback parameters or claims for \(\beta\ne\mu+\alpha\) are asserted. The asymptotic variable \(t\) is the model's physical continuous time.

## Proof

**1. Global extinction, including the nonhyperbolic threshold.** Write \(Q=I+R+(1-\sigma)C\). Conservation and \(\beta=\mu+\alpha\) give the exact identity

\[
\dot I=-\beta I Q,\qquad Q\ge I.
\]

For \(I(0)>0\), positivity is preserved for all finite times. Thus \(\dot I\le-\beta I^2\), so \(I(t)\le[I(0)^{-1}+\beta t]^{-1}\to0\). The recovered coordinate obeys \(\dot R\le(\alpha+\beta)I-AR\), because \(0\le C\le1\). Variation of constants gives \(R(t)\to0\). Since \(0\le g\le I\le1\), one also has \(\dot C\le\delta(1+\varepsilon_1)R-BC\), hence \(C(t)\to0\) and \(S(t)\to1\). If \(I(0)=0\), then \(g=0\), \(\dot R=-AR\), and \(\dot C=\delta R-BC\), giving exponential disease-free convergence. The only stationary point at threshold is therefore the disease-free point.

**2. Derive the leading amplitude without assuming center-manifold attraction.** Because \(Q(t)\to0\), for any sufficiently small \(\eta\in(0,\min\{A,B\})\) and large enough \(t_0\) we have \(-\dot I/I\le\eta\) on \([t_0,\infty)\). Consequently, for \(t\ge s\ge t_0\),

\[
I(s)\le I(t)e^{\eta(t-s)}.
\]

Apply variation of constants to \(\dot R\le(\alpha+\beta)I-AR\). The inequality above yields \(R(t)=O(I(t))\), including the decaying initial transient. Applying the same argument to \(\dot C\le\delta(1+\varepsilon_1)R-BC\) yields \(C(t)=O(I(t))\). In particular, \(g=I+O(I^2)\) for either definition of feedback.

Set \(u_0=R/I\), \(v_0=C/I\); both remain bounded. Dividing the recovered and cross-immune equations by \(I\), and using \(\dot I/I=O(I)\), gives

\[
\dot u_0=\alpha-Au_0+o(1),\qquad
\dot v_0=\delta u_0-Bv_0+o(1).
\]

Stable linear variation of constants shows \(u_0\to a\), \(v_0\to c\). Therefore \(\dot I=-K I^2+o(I^2)\), and \(\frac{d}{dt}(1/I)\to K>0\). Cesàro integration implies \(I(t)\sim1/(Kt)\), yielding the universal leading coefficient.

**3. Exact second-order slaving of the immune coordinates.** Let \(u=R-aI\) and \(v=C-cI\). Their exact equations obtained by subtraction, together with \(R,C=O(I)\), imply \(\dot u=-Au+O(I^2)\) and \(\dot v=\delta u-Bv+O(I^2)\). Since \(I(t)\sim1/(Kt)\), exponentially weighted convolutions of \(O(I^j)\) are \(O(I(t)^j)\) for each fixed \(j\ge1\). It follows that \(u,v=O(I^2)\) and

\[
\dot I=-KI^2+O(I^3).
\]

Inserting the expansions \(R=aI+O(I^2)\), \(C=cI+O(I^2)\), \(g=I+O(I^2)\) into the exact equations gives

\[
\dot u=-Au+[aK+(1-\sigma)\beta c-\varepsilon_1\delta a]I^2+O(I^3).
\]

By the definition of \(b\), the defect \(u-bI^2\) satisfies \(\frac{d}{dt}(u-bI^2)=-A(u-bI^2)+O(I^3)\), because \(\frac{d}{dt}(I^2)=O(I^3)\). Hence \(u=bI^2+O(I^3)\). Similarly

\[
\dot v=-Bv+[cK+\delta b+\varepsilon_1\delta a-\beta c-\varepsilon_2\gamma c]I^2+O(I^3),
\]

so \(v=dI^2+O(I^3)\). The only feedback fact used through this order is \(g=I+O(I^2)\); consequently **both choices produce the same coefficients** \(a,b,c,d\).

**4. Integrate the cubic normal form with an integrable remainder.** From the exact infection equation,

\[
\dot I=-KI^2-LI^3+O(I^4).
\]

Thus, for \(J=1/I\),

\[
\dot J=K+LI+O(I^2).
\]

The leading estimate \(I=O(t^{-1})\) first gives \(J=Kt+O(\log t)\) by integration. Inverting this gives

\[
I(t)=\frac1{Kt}+O\!\left(\frac{\log t}{t^2}\right).
\]

Both the difference \(I(t)-(Kt)^{-1}\) and \(I(t)^2\) are absolutely integrable on \([t_0,\infty)\). Therefore \(\frac{d}{dt}[J-Kt-(L/K)\log t]\) is integrable, so its argument converges to a finite constant \(H\). Expanding the reciprocal proves the displayed infection expansion. Direct substitution into the coefficients yields the sample \(K=3\) and \(L=(3-\varepsilon_1)/2\), proving the exact sign change. \(\square\)

## Verification

A standalone SymPy checker is supplied as `verify.py`, with its single dependency specified in `requirements.txt`. It verifies six universal symbolic coefficient identities, 576 exact rational polynomial-jet residual checks spanning both feedback definitions, the quadratic and cubic infection coefficients, and the exact sign-reversal family. Run `python verify.py` in a directory containing the files. The symbolic computation checks algebraic identities, while the universal convergence and asymptotic error estimates follow from the analytical proof above. A separate numerical initial-value trial at finite time was used as a plausibility check, not as proof; its output is not necessary to reconstruct the theorem.

## Relationship to prior work

Ramírez-Gutiérrez, Lóczi, Muñoz-Moncayo and Ketcheson [1] introduce this exact SIRCm system and both feedback choices. Their Proposition 2.4 treats strict subcritical and supercritical local disease-free stability and explicitly records nonhyperbolicity at equality; their main equilibrium and Hopf results focus on \(\mathcal R_0>1\), not the universal threshold decay law. Their original model and proofs are the starting point for this calculation, not newly rediscovered material.

The original zero-feedback SIRC system of Casagrandi, Bolzoni, Levin and Andreasen [2] is a strict special case. The accessible abstract describes bifurcation and seasonal behavior, but its full text was not available for comparison; a previously known zero-feedback critical decay statement cannot be excluded. Even such a result would not directly supply the two independent feedback parameters, agreement of the two distinct feedback mechanisms through the cubic coefficient, or their explicit logarithmic sign reversal.

A separately published published-finding corpus statement [3] treats the same SIRCm equations for endemic equilibrium uniqueness and independent-feedback monotonicity **when \(\beta>\mu+\alpha\)**. Its detailed proof excludes endemic equilibria at or below threshold but does not establish trajectory convergence or a second-order extinction law, and its scope explicitly excludes stability. Related critical-decay findings for nonlinear SIRS and other multi-compartment diseases use different vector fields and do not imply the parameter-specific constants here. Elementary center-manifold and scalar Riccati asymptotics are standard tools; the exact four-compartment all-initial-state coefficients, comparison of feedback laws, and sign-reversal boundary are the particular contributions established here. Exhaustive historical priority is not claimed.

## Limitations

The result assumes the autonomous four-state SIRCm polynomial vector field, exact threshold, and finite feedback strengths. The expansion applies individually to initially infected solutions; the orbit-dependent constant \(H\) is not given in closed form. The special sign-reversal example has \(\sigma=1\), although the general formula applies throughout \([0,1]\). The statement gives no uniform error constants as feedback becomes unbounded, and it does not classify oscillations or attraction above threshold. It is a mathematical asymptotic statement, not an inference about observed epidemic outcomes. Independent validation and definitive historical-priority assessment are outstanding.

## References

1. D. R. Ramírez-Gutiérrez, L. Lóczi, C. Muñoz-Moncayo, and D. I. Ketcheson, *Compartmental epidemiological models with infection-driven immune escape*, arXiv:2610.01111v1, first posted 2026-10-01. https://arxiv.org/html/2610.01111v1
2. R. Casagrandi, L. Bolzoni, S. A. Levin, and V. Andreasen, *The SIRC model and influenza A*, Mathematical Biosciences 200 (2006), 152–169. DOI:10.1016/j.mbs.2005.12.029.
3. *All-feedback endemic uniqueness and separate monotonicity in the prevalence-driven SIRCm system*, public published-finding corpus research record (2026), `2026/10/11/SCOPE-all-feedback-endemic-uniqueness-and-separate-monotonicity-in-the--c54c540be342`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-all-feedback-endemic-uniqueness-and-separate-monotonicity-in-the--c54c540be342.

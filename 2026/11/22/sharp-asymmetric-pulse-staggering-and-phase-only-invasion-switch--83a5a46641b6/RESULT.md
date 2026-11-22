# Sharp asymmetric pulse staggering and phase-only invasion switches under bilinear pest suppression

## Finding

Two agents applied periodically at a common interval need not have a half-period stagger that minimizes their simultaneous residual activity. In a two-agent pest-control proxy with first-order residue loss and a positive bilinear interaction, the exact least-overlap phase is
\[
\phi_* = \frac{1}{a+b}\log\!\left(\frac{a(e^{bT}-1)}{b(1-e^{-aT})}\right),\qquad 0<\phi_*<T.
\]
It equals \(T/2\) if and only if the two decay rates agree. Synchronizing applications uniquely maximizes the joint activity, whereas the unique phase above minimizes it. Fixing all doses, the mean exposure to each agent remains unchanged, yet the pest's one-period invasion multiplier can cross unity at exactly two phases. An additional universal high-frequency law is
\[
\lim_{T\downarrow0}\frac{I_T(0)-I_T(\phi_*)}{T}=\frac{PQ}{8},
\]
independent of both decay constants. For large \(T\), the least-overlap phase occupies the fraction \(b/(a+b)\) of the cycle and least overlap decays exponentially at rate \(ab/(a+b)\).

## Assumptions and scope

Let \(T,a,b,P,Q,\kappa>0\), let \(u,v\ge0\), and let \(r>0\). Each period one dose \(P\) of the first agent is delivered at time \(0\bmod T\), and one dose \(Q\) of the second at time \(\phi\bmod T\), \(\phi\in[0,T)\). Between jumps the respective concentrations decay at rates \(a,b\). On their uniquely determined periodic residue orbits,
\[
X(t)=\frac{P e^{-a(t\bmod T)}}{1-e^{-aT}},\qquad
Y_\phi(t)=\frac{Q e^{-b((t-\phi)\bmod T)}}{1-e^{-bT}}.
\]
Here \(x\bmod T\in[0,T)\), including the right-continuous post-application value. Set \(I_T(\phi)=\int_0^T X(t)Y_\phi(t)\,dt\). The rare-pest linear growth equation is
\[
\dot N(t)=\bigl(r-uX(t)-vY_\phi(t)-\kappa X(t)Y_\phi(t)\bigr)N(t).
\]
The joint term is a *hypothesized* positive interaction, not an experimentally estimated coefficient. The conclusions concern the scalar invasion multiplier, not pesticide safety, field optimization, interactions with natural enemies, or nonlinear established-pest stability.

## Proof

Write \(A=e^{-bT}(1-e^{-aT})\), \(B=1-e^{-bT}\) and
\[
C=\frac{PQ}{(a+b)(1-e^{-aT})(1-e^{-bT})}>0.
\]
Integration on \([0,\phi)\) and \([\phi,T)\), retaining the periodic wrap-around for the second residue, gives the exact identity
\[
I_T(\phi)=C\left(Ae^{b\phi}+Be^{-a\phi}\right),\quad 0\le\phi\le T,
\]
where endpoints \(0\) and \(T\) represent the same physical phase. In particular,
\[
I_{\max}=I_T(0)=I_T(T)=\frac{PQ(1-e^{-(a+b)T})}{(a+b)(1-e^{-aT})(1-e^{-bT})}.
\]
On the open phase interval, \(I_T''=C(b^2Ae^{b\phi}+a^2Be^{-a\phi})>0\). Moreover \(I_T'(0)<0\) because \(1-e^{-aT}<aT\) while \(e^{bT}-1>bT\); and \(I_T'(T)>0\) by the same inequalities with reversed signs. Hence there is exactly one interior minimum, defined by \(bAe^{b\phi_*}=aBe^{-a\phi_*}\). Solving proves the formula in the Finding, together with
\[
I_{\min}=I_T(\phi_*)=\frac{PQe^{-a\phi_*}}{b(1-e^{-aT})}<I_{\max}.
\]
Another form of its exact location is
\[
\phi_*=\frac T2+\frac{1}{a+b}\log\left(\frac{a\sinh(bT/2)}{b\sinh(aT/2)}\right).
\]
Because \(\sinh z/z\) is strictly increasing for \(z>0\), \(\phi_*<T/2\) precisely when \(a>b\), and \(\phi_*>T/2\) precisely when \(a<b\).

Every phase has the same separate time integrals, \(\int_0^T X=P/a\) and \(\int_0^T Y_\phi=Q/b\). Thus the exact one-period growth multiplier is
\[
M(\phi)=\exp\{L-\kappa I_T(\phi)\},\qquad L=rT-uP/a-vQ/b.
\]
For \(L<\kappa I_{\min}\), every phase yields \(M<1\); at equality only \(\phi_*\) is neutral and all others suppress. For \(\kappa I_{\min}<L<\kappa I_{\max}\), there are exactly two distinct neutral phases, one on either side of \(\phi_*\); phases between these give \(M>1\) and phases near simultaneous application give \(M<1\). For \(L=\kappa I_{\max}\), only simultaneous application is neutral and all other phases yield \(M>1\); for \(L>\kappa I_{\max}\), every phase gives \(M>1\). These exhaustive cases follow from strict convexity, the equal endpoint maxima, and monotonicity of the exponential. The threshold \(M=1\) is neutral and is not labeled asymptotically stable or unstable.

For the short-period assertion, set \(S(s)=1/2-s\) for \(0\le s<1\), extended periodically. Uniformly in \(s\),
\[
X(Ts)=P/(aT)+P S(s)+O(T),\qquad
Y_\phi(Ts)=Q/(bT)+Q S(s-\phi/T)+O(T).
\]
Since the integral of the difference \(Y_0-Y_\phi\) is exactly zero, subtracting its product with the constant \(P/(aT)\) before integration gives, uniformly in the relative phase \(\delta=\phi/T\),
\[
I_T(0)-I_T(\phi)=PQ T\left[\frac{\delta(1-\delta)}2\right]+O(T^2),
\]
using \(\int_0^1S(s)S(s-\delta)\,ds=1/12-\delta(1-\delta)/2\). The exact minimizer satisfies \(\phi_*/T\to1/2\), proving the universal coefficient \(PQ/8\).

For \(T\to\infty\), the exact phase formula gives
\[
\phi_*=\frac{bT+\log(a/b)}{a+b}+o(1),\qquad
I_{\min}\sim \frac{PQ}{b}\left(\frac ba\right)^{a/(a+b)}e^{-abT/(a+b)},\qquad
I_{\max}\to\frac{PQ}{a+b}.
\]
The period asymptotics fix the pulse amounts \(P,Q\); they are not fixed-mean-input asymptotics.

## Verification

Run `python3 verify.py` from a directory containing this result and the attached script; it uses only the Python standard library. It checks the independent midpoint-integration identity over random positive parameter sets, endpoint and minimizer inequalities, finite-period examples, and both asymptotic regimes. A rigorous rational interval certificate is included for \(a=3,b=1,T=P=Q=\kappa=1,u=v=1/100,r=1/3\), for which \(L=8/25\). Rational Taylor remainders enclose the exact overlaps and establish
\[
I_T(1/2)<8/25<I_T(0),
\]
so the same fixed dosing and mean exposures admit invasion with the stagger and suppression with synchrony. The exact minimizer is \(\phi_*=0.4227515810559\ldots\), not \(T/2\); the witness at \(1/2\) is used only to make the strict opposite signs rigorously easy to certify. Numerical checks support, but do not replace, the proof above.

## Relationship to prior work

Al Basir, Chowdhury and Torres (2023) model separately decaying pulsed chemical and biological interventions and analyze extinction thresholds. Tang, Liang, Tan and Cheke (2011) treat residual pesticide effects in classical integrated pest management, while Ackleh, Jahangir and Veprauskas (2023) analyze interacting chemical and biological controls in a different discrete stage-structured setting. These results motivate the intervention framework but the inspected equations and claims do not state a two-residue bilinear interaction, the unequal-rate least-overlap phase, the exact two-neutral-phase regime, or its universal short-period overlap gap. Known circular cross-correlation and one-dimensional Floquet integration underlie the computation and are not claimed as new mathematical mechanisms. A published two-patch pulse-culling phase law has a distinct noncommuting spatial mechanism and does not imply the asymmetric two-residue formula. Priority beyond inspected material is not independently certified.

## Limitations

Bilinear interaction is an explicit model assumption, not derived or calibrated from field data; interactions could instead be antagonistic, saturating or concentration-dependent. The two concentrations have independent first-order loss and fixed equal periods, with no feedback on their clearance. The infestation is infinitesimal and modeled by one scalar; no claims about nonlinear persistence, absolute safety, crop yield, toxicity, resistance, or practical scheduling follow. One related 2012 delayed-residual IPM study was not available in full through authorized sources; its abstract and bibliographic description were inspected. The result does not claim invention of circular correlation, convexity, or the standard scalar invasion criterion.

## References

1. F. Al Basir, J. Chowdhury and D. F. M. Torres, *Dynamics of a Double-Impulsive Control Model of Integrated Pest Management Using Perturbation Methods and Floquet Theory*, Axioms 12 (2023), 391. First public release April 18, 2023. https://doi.org/10.3390/axioms12040391
2. S. Tang, J. Liang, Y. Tan and R. A. Cheke, *Threshold conditions for integrated pest management models with pesticides that have residual effects*, Journal of Mathematical Biology 66 (2013), 1–35. First online December 29, 2011. https://doi.org/10.1007/s00285-011-0501-x
3. A. S. Ackleh, J. Jahangir and A. Veprauskas, *The interplay between multiple control mechanisms in a host–parasitoid system: a discrete-time stage-structured modelling approach*, Journal of Biological Dynamics 17 (2023). First online August 17, 2023. https://doi.org/10.1080/17513758.2023.2241483
4. J. Liang, S. Tang and R. A. Cheke, *An integrated pest management model with delayed responses to pesticide applications and its threshold dynamics*, Nonlinear Analysis: Real World Applications 13 (2012), 2352–2374. https://doi.org/10.1016/j.nonrwa.2012.02.003
5. L. Wu and Z. Xiang, *A study of integrated pest management models with instantaneous and non-instantaneous impulse effects*, Mathematical Biosciences and Engineering 21 (2024), 3063–3094. https://doi.org/10.3934/mbe.2024136

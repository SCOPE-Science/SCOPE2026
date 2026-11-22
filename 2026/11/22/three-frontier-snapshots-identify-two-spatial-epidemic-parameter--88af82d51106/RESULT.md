# Three frontier snapshots identify two spatial-epidemic parameters with a sharp data bound

## Finding

In the arctangent-saturated aggregated spatial SIR model, three ordered observations of the unexposed-district population and cumulative recovered population determine both positive spatial spread parameters uniquely, independently of the transmission and district-clearance parameters. The same observations obey a sharp, parameter-free inequality. Precisely, put \(P_j=P(t_j)\), \(C_j=C(t_j)\), where \(t_0<t_1<t_2\), and assume \(P_0>P_1>P_2>0\), \(C_0<C_1<C_2\). Define
\[
H=\frac{C_1-C_0}{C_2-C_1},\qquad
L=\frac{\log(P_0/P_1)}{\log(P_1/P_2)},\qquad
U=\frac{P_0-P_1}{P_1-P_2}.
\]
Then every positive finite saturation scale satisfies \(L<H<U\). Moreover, if \(N,\gamma>0\) are known, the reduced observation equations admit exactly one pair \((\alpha,\rho)\in(0,\infty)^2\) whenever \(L<H<U\). The strict endpoints are sharp limits of that pair-identification problem; neither is attained for finite positive parameters. In particular, an exact observed ratio outside \((L,U)\) falsifies the model's assumed arctangent frontier law, provided the specified observables are measured correctly.

## Assumptions and scope

Use the deterministic five-compartment equations of Aronna, Bergonzi and Kofman (2026), with \(P=p_{\mathrm S}\) for the population in unreached districts, \(Q=p_{\mathrm R}\) for the population in completed districts, \(S,I,R\) for susceptible, infectious and recovered populations in active districts, and \(p_{\mathrm I}=S+I+R\). Fix \(N>0\), \(\gamma>0\), \(\rho>0\), \(\alpha>0\), \(\beta>0\), \(\beta_R>0\), and \(0<S_\infty<1\), \(R_\infty=1-S_\infty\). The relevant equations, with the paper's smooth saturation function, are
\[
\begin{aligned}
\dot P&=-\rho I\,\operatorname{sat}(\alpha P/N),
&\operatorname{sat}(z)&=\frac2\pi\arctan\!\left(\frac\pi2z\right),\\
\dot R&=\gamma I-\frac{\beta_RR_\infty}{S_\infty}\frac{SR}{S+I+R},
&\dot Q&=\frac{\beta_R}{S_\infty}\frac{SR}{S+I+R}.
\end{aligned}
\]
The remaining two equations govern \(S\) and \(I\) as in the cited source. Assume a nonnegative classical solution over the observation interval, with positive active population, \(I(t)>0\), and \(P(t)>0\). The cumulative recovered population \(C=R+R_\infty Q\) includes recoveries in completed districts and is *not* simply the active-district compartment \(R\). Three simultaneous pairs \((P,C)\) are observed without noise; neither their observation times nor \(S,I,R,Q\) individually need be known to apply the reduced relation, provided \(C\) is measured.

The theorem asserts identifiability **from the frontier--recovery relationship** conditional on this model, not identifiability from prevalence alone, sufficiency for arbitrary points to be part of a full solution, or statistical accuracy with finite noisy data.

## Proof

**1. Eliminate transmission and district-completion dynamics.** Adding the two recovery equations after multiplying the second by \(R_\infty\) gives the exact identity
\[
\dot C=\dot R+R_\infty\dot Q=\gamma I.
\]
Since \(I>0\), \(C\) strictly increases while \(P\) strictly decreases. Put \(k=\pi\alpha/(2N)>0\). Dividing the two derivatives and integrating gives, for any \(a>b>0\) taken from two frontier observations,
\[
C(b)-C(a)=\frac{\gamma\pi}{2\rho}F_k(a,b),\qquad
F_k(a,b)=\int_b^a\frac{du}{\arctan(ku)}.
\tag{1}
\]
Consequently
\[
H=\Phi(k):=\frac{F_k(P_0,P_1)}{F_k(P_1,P_2)}.
\tag{2}
\]

**2. Strict increase of the integral ratio.** Set \(w_k(u)=1/\arctan(ku)\) and \(\eta(z)=z/[(1+z^2)\arctan z]\). Direct differentiation yields
\[
\frac{\partial}{\partial k}\log w_k(u)=-\frac1k\eta(ku),\qquad
\eta'(z)=\frac{(1-z^2)\arctan z-z}{(1+z^2)^2(\arctan z)^2}<0\quad(z>0).
\]
Indeed, for \(z\ge1\) the numerator is negative, and for \(0<z<1\) it is strictly less than \((1-z^2)z-z<0\). Differentiating the logarithm of (2) gives
\[
\frac{\Phi'(k)}{\Phi(k)}
=\frac1k\left(\langle\eta(ku)\rangle_{(P_2,P_1),k}
-\langle\eta(ku)\rangle_{(P_1,P_0),k}\right)>0,
\]
where each bracket denotes the normalized weighted mean with density proportional to \(w_k(u)>0\). Every value of \(u\) in the lower interval is strictly smaller than every interior value in the upper interval; the strict decrease of \(\eta\) proves the displayed inequality. Thus \(\Phi\) is continuous and strictly increasing on \((0,\infty)\).

**3. Compute the two exact endpoint limits.** Since all frontier observations stay above zero, the limits are uniform over each compact integration interval:
\[
\arctan(ku)\sim ku\quad(k\to0^+),\qquad
\arctan(ku)\longrightarrow\pi/2\quad(k\to\infty).
\]
Hence
\[
\lim_{k\to0^+}\Phi(k)=L,
\qquad
\lim_{k\to\infty}\Phi(k)=U.
\]
Strictly \(L<U\): the logarithmic mean \((a-b)/\log(a/b)\) of \(a>b>0\) lies strictly between \(b\) and \(a\), so the logarithmic mean of \((P_0,P_1)\) exceeds that of \((P_1,P_2)\). Their ratio is \(U/L>1\).

**4. Invert the observations.** Given the two positive measured increments and \(L<H<U\), the intermediate value theorem and strict increase of \(\Phi\) produce exactly one \(k>0\) solving (2). The unique parameters are
\[
\boxed{\alpha=\frac{2Nk}{\pi}},\qquad
\boxed{\rho=\frac{\gamma\pi}{2(C_1-C_0)}F_k(P_0,P_1)}.
\tag{3}
\]
Equation (2) then enforces the second increment as well. In contrast, using a single pair of snapshots gives only (1); each \(k>0\) has a corresponding positive \(\rho\) from (3), so that relation alone has infinitely many fitting parameter pairs. No assertion is made that arbitrary compatible snapshot triples automatically occur along the other three equations of the full epidemic model. This completes the proof.

## Verification

The included standard-library `checker.py` verifies the exact analytic expression for \(\eta'(z)\) against finite differences at eight positive arguments; verifies strict endpoint bounds and ratio monotonicity across four separated frontier triples and nine saturation scales; reconstructs an arbitrarily chosen interior parameter by scalar bisection; and checks a full five-compartment illustrative trajectory using an independent fourth-order Runge--Kutta integration. Finite computations corroborate, but do not establish, the quantified theorem; its proof is the monotonicity argument above.

For a concrete trajectory use \(N=1\), \(\beta=3\), \(\gamma=1\), \(\rho=\pi/2\), \(\alpha=2/\pi\), \(\beta_R=0.05\), \(R_\infty\) the positive solution of \(R_\infty=1-e^{-3R_\infty}\), and initial \((P,S,I,R,Q)=(0.8,0.199,0.001,0,0)\). At the first two subsequent frontier levels \(P=0.78\) and \(P=0.76\), the respective cumulative recoveries are approximately \(0.02991393691\) and \(0.06039483806\). Their successive-increment ratio is approximately \(0.98139936108\), strictly between \(0.97468080448\) and \(1\). Inversion recovers the original \(\alpha\) and \(\rho\) (up to numerical quadrature error). The example uses floating-point integration and is not an exact symbolic trajectory.

## Relationship to prior work

Aronna, Bergonzi and Kofman introduce precisely this spatially aggregated SIR system, specify the smooth arctangent saturation in their equation (5), and fit the spatial parameters numerically. Their principal analytical result is \(\mathcal R_0=\beta/\gamma\). They do not establish the exact parameter-free three-snapshot interval or uniqueness of its two-parameter inverse. The finite-snapshot inverse theorem above is a mathematically nontrivial consequence of their model, not a new epidemic mechanism or a claim that their model itself is new.

Bergström, Favero and Britton study structural identifiability of a *different*, under-reporting/prior-immunity SIR model and show how supplementary epidemic observations can restore identifiability; that work supplies general motivation, not the arctangent spatial-frontier formula. Classical logarithmic-mean inequalities are used in the endpoint comparison but do not themselves determine \(k\) or \(\rho\) from the epidemic observations.

## Limitations

This is a deterministic noise-free identifiability and model-consistency statement for the specified smooth arctangent law. Population \(N\) and recovery rate \(\gamma\) are taken as known; otherwise only \(\rho/\gamma\) is identified by the frontier--recovery curve. The three pairs must have strictly declining, positive \(P\) and increasing \(C\). Cumulative recovered population needs to include the completed districts, not just active-district \(R\). The strict map has weak sensitivity near the small- and large-\(\alpha\) limits, so practical identifiability may be poor. The converse is about first-integral consistency rather than guaranteed feasibility for all other full-model coordinates; no new claim about incidence peaks, final size or epidemic extinction follows. Independent experimental or third-party mathematical validation has not been performed.

## References

1. M. S. Aronna, M. Bergonzi, E. Kofman, *An Aggregated SIR Model for Spatial Epidemic Propagation*, arXiv:2602.23449v1, first public 2026-02-26. https://arxiv.org/html/2602.23449
2. F. Bergström, M. Favero, T. Britton, *Identifiability in Epidemic Models with Prior Immunity and Under-Reporting*, Bulletin of Mathematical Biology 88, Article 90 (2026), https://doi.org/10.1007/s11538-026-01656-w; earlier preprint arXiv:2506.07825.
3. G. Massonis, J. R. Banga, A. F. Villaverde, *Structural identifiability and observability of compartmental models of the COVID-19 pandemic*, Annual Reviews in Control 51 (2021), 441–459, https://doi.org/10.1016/j.arcontrol.2020.12.001.

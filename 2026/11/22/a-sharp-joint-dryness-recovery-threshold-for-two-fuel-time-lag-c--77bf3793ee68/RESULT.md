# A sharp joint-dryness recovery threshold for two fuel time-lag classes

## Finding

For each ratio \(\rho>1\) of fast to slow fuel-moisture relaxation rates, there is a strictly positive and sharp normalized dryness threshold \(c_*(\rho)\). In the periodically forced, common-equilibrium, two-class model defined below, let \(J_\rho(x,c)\) be the fraction of one forcing cycle during which **both** classes lie below the same absolute moisture threshold. Here \(x\geq0\) is forcing angular frequency measured in units of the slow rate and \(0<c<1\) is the distance of the dry threshold below mean equilibrium, divided by forcing amplitude.

**Theorem.** For every \(\rho>1\), a uniquely determined number \(c_*(\rho)\) satisfies
\[
0<c_*(\rho)<\frac{\sqrt\rho}{1+\rho}.
\]
For \(c\geq c_*(\rho)\), \(J_\rho(\cdot,c)\) is strictly decreasing until it becomes zero, and remains zero thereafter. For \(0<c<c_*(\rho)\), it is **not** nonincreasing: it first decreases, increases on at least one nonempty interval, and ultimately decreases to zero. The last assertion is a recovery of *simultaneous* dry exposure despite the fact that the individual dry exposures both shrink with frequency. No assertion is made that there are only two turning points for every parameter choice.

The threshold has an exact one-dimensional, root-and-maximum definition. For \(x>\sqrt\rho\), write
\[
\begin{aligned}
\alpha&=\sqrt{1+x^2},\qquad \beta=\sqrt{1+x^2/\rho^2},\\
g_\rho(x)&=\frac1{\alpha\beta},\\
B_\rho(x)&=\frac{(\rho-1)(x^2-\rho)}{(1+x^2)(\rho^2+x^2)},\\
S_\rho(x,c)&=\frac{cx}{\alpha\sqrt{1-c^2\alpha^2}}+
\frac{cx}{\rho^2\beta\sqrt{1-c^2\beta^2}}.
\end{aligned}
\]
There is a unique \(c_\rho(x)\in(0,g_\rho(x))\) satisfying \(S_\rho(x,c_\rho(x))=B_\rho(x)\), and
\[
\boxed{c_*(\rho)=\max_{x>\sqrt\rho}c_\rho(x).}
\]
This is an exact characterization, not a closed elementary formula for the maximum.

For almost equal relaxation rates, the threshold has the **sharp contrast law**
\[
\lim_{\rho\downarrow1}\frac{c_*(\rho)}{\rho-1}
=K=\frac{z-1}{2\sqrt z(1+z)^{3/2}},\qquad
z=\frac{5+\sqrt{33}}4,
\]
with \(K\approx0.0726844611\). Every choice of maximizing frequencies tends to \(\sqrt z\) in the same limit.

For the concrete rate ratio \(\rho=2\), the nonmonotone regime contains \(c=1/50\). A numerical search of the explicit one-dimensional definition gives \(c_*(2)\approx0.04338\); this displayed approximation is only an illustration, not a certified enclosure.

## Assumptions and scope

At each fixed frequency \(\omega>0\), the atmospheric equilibrium moisture is the sinusoid
\[
E(t)=\bar m+A\cos(\omega t),\qquad A>0.
\]
Two independent fuel classes share that prescribed equilibrium but have different constant relaxation rates \(a>0\) and \(b=\rho a>a\):
\[
\dot m_1=a(E-m_1),\qquad \dot m_2=b(E-m_2).
\]
We work on the unique attracting periodic solutions. Both are classified as dry when \(m_i(t)<m_{\mathrm{crit}}=\bar m-cA\) for the **same** \(0<c<1\). The statistic \(J_\rho(x,c)\), with \(x=\omega/a\), is the Lebesgue fraction of forcing phases for which both inequalities hold. Transient initial conditions, nonsinusoidal equilibria, rainfall impulses, adsorption/desorption hysteresis, different thresholds between classes and fire-spread mechanisms are excluded. The physical threshold \(m_{\mathrm{crit}}\) and amplitude \(A\) are held fixed while frequency is varied; the normalization merely records their ratio.

## Proof

**1. Exact periodic response and intersection formula.** For phase \(\theta=\omega t\), the periodic solutions are
\[
\begin{aligned}
 m_1-\bar m&=\frac A\alpha\cos(\theta-\phi_1),&\phi_1&=\arctan x,\\
 m_2-\bar m&=\frac A\beta\cos(\theta-\phi_2),&\phi_2&=\arctan(x/\rho).
\end{aligned}
\]
If \(x\geq X_c:=\sqrt{c^{-2}-1}\), the slow class cannot fall strictly below threshold, so \(J_\rho=0\). For \(0\leq x<X_c\), set
\[
h_1=\arccos(c\alpha),\quad h_2=\arccos(c\beta),\quad
d=\phi_1-\phi_2=\arctan x-\arctan(x/\rho).
\]
Here \(0<h_1\leq h_2<\pi/2\) and \(0\leq d<\pi/2\). The two dry-phase arcs are centered at \(\pi+\phi_i\), with half-widths \(h_i\). Their lower intersection edge always belongs to the slower class. Comparing their upper edges yields the exact fraction
\[
\boxed{J_\rho(x,c)=\frac1{2\pi}\min\{2h_1,h_1+h_2-d\}.}
\]
The second expression is positive whenever it is selected. Indeed, the two formulas meet at \(c=g_\rho(x)=1/(\alpha\beta)\), where direct trigonometry gives \(h_1=\arctan(x/\rho)\), \(h_2=\arctan x\), hence \(h_2-h_1=d\) and both expressions equal \(2h_1>0\). For smaller \(c\), both half-widths increase. Furthermore, \(h_2-h_1\) is strictly increasing in \(c\): its derivative is \(\alpha/\sqrt{1-c^2\alpha^2}-\beta/\sqrt{1-c^2\beta^2}>0\). Consequently, for \(c<g_\rho(x)\) the second (partially overlapping) branch is active; for \(c\geq g_\rho(x)\) the slow dry arc lies inside the fast one and the first branch is active.

**2. Frequency derivative.** In the nested branch, \(J_\rho=h_1/\pi\) and \(h_1'<0\). On the partially overlapping branch,
\[
2\pi\,\frac{\partial J_\rho}{\partial x}
=h_1'+h_2'-d'=B_\rho(x)-S_\rho(x,c),
\]
using the definitions in the finding. The quantity \(S_\rho(x,c)>0\) is strictly increasing in \(c\in(0,g_\rho(x))\). For \(x\leq\sqrt\rho\), \(B_\rho(x)\leq0\), hence the derivative is negative. For \(x>\sqrt\rho\), \(B_\rho(x)>0\) and \(S_\rho(x,0)=0\). At the upper branch endpoint \(c=g_\rho(x)\), direct substitution gives
\[
B_\rho(x)-S_\rho(x,g_\rho(x))
=-\frac{\rho+1}{1+x^2}+\frac{\rho-1}{\rho^2+x^2}<0.
\]
The intermediate-value theorem and strict monotonicity therefore give exactly one \(c_\rho(x)\in(0,g_\rho(x))\), with a **positive** frequency derivative precisely when \(c<c_\rho(x)\). Importantly, the derivative root occurs before the arc-nesting transition; it is not an artifact of differentiating the wrong branch.

**3. Sharp global transition.** Implicit monotonicity makes \(c_\rho(x)\) continuous for \(x>\sqrt\rho\). As \(x\downarrow\sqrt\rho\), \(B_\rho(x)\to0\), forcing \(c_\rho(x)\to0\). As \(x\to\infty\), the strict bound \(c_\rho(x)<g_\rho(x)\sim\rho/x^2\) again forces convergence to zero. Thus a positive interior maximum \(c_*(\rho)\) is attained. Because \(g_\rho(x)\) is strictly decreasing in positive \(x\), this maximum is strictly below \(g_\rho(\sqrt\rho)=\sqrt\rho/(\rho+1)\).

For \(c\geq c_*\), neither smooth branch of \(J\) has positive derivative. The partial-branch derivative is negative except possibly at isolated stationary points at \(c=c_*\), because an interval of such points would force the analytic function \(c_\rho(x)\) to be constant, contradicting its endpoint limits. The nested branch is strictly decreasing, as are all low-frequency partial branches. Therefore \(J\) decreases strictly until \(X_c\), then stays zero. If \(0<c<c_*\), a frequency \(x>\sqrt\rho\) has \(c<c_\rho(x)\), so \(J'(x)>0\). On the other hand, near \(x=0\), the partial-branch right derivative equals \(-(1-1/\rho)/(2\pi)<0\); sufficiently near the cutoff \(X_c\), the nested branch is strictly decreasing. Hence there is an actual intermediate recovery interval bounded by decreases. This proves both directions and includes equality \(c=c_*\).

**4. Small-contrast limit.** Put \(\varepsilon=\rho-1\) and fix \(x>1\). The defining equality, uniformly on compact \(x\)-intervals away from \(1\), gives
\[
\frac{c_\rho(x)}{\varepsilon}\longrightarrow
f(x):=\frac{x^2-1}{2x(1+x^2)^{3/2}}.
\]
The roots cannot escape to infinity when taking maxima: from \(S_\rho(x,c)\geq cx/\sqrt{1+x^2}\) and the defining equality,
\[
0\leq\frac{c_\rho(x)}{\varepsilon}
\leq\frac{1}{x\sqrt{1+x^2}},
\]
which vanishes uniformly for large \(x\). The explicit numerator \(x^2-\rho\) in \(B_\rho\) similarly ensures uniform vanishing as \(x\downarrow1\). Hence maximization commutes with the limit. Writing \(z=x^2\), differentiation of \(f\) gives the unique positive maximizer \(z=(5+\sqrt{33})/4\) (its stationary equation is \(2z^2-5z-1=0\)). This proves the constant and convergence of every maximizing-frequency choice.

**5. Strict concrete witness.** At \(\rho=2\), \(x=2\), \(c=1/50\), the partial-overlap condition holds since \(c<1/\sqrt{10}\), and \(B_2(2)=1/20\). Using \(\sqrt5>2\), \(\sqrt2>1\) and both square-root factors in \(S_2(2,1/50)\) greater than \(99/100\), one obtains
\[
S_2(2,1/50)<\frac{(1/50)\cdot2}{2(99/100)}+
\frac{(1/50)\cdot2}{4(99/100)}
=\frac1{33}<\frac1{20}.
\]
Thus the recovery derivative is **strictly positive** without relying on a floating-point computation.

## Verification

Run `python3 verify.py` from the directory containing this document and the embedded checker. The checker independently computes the exact phase-intersection fraction, compares it with deterministic phase enumeration, solves the defining scalar roots by bisection for several rate ratios, checks both sides of the transition numerically, and checks the explicit rational recovery witness. In the recorded execution it passed 17,475 deterministic checks. Finite numerical checks establish none of the infinite quantifiers in the theorem: those are established by the five analytical proof steps above. The approximate decimal for \(c_*(2)\) is not used in the proof and is not a rigorously rounded interval.

## Relationship to prior work

A first-order equilibrium moisture-relaxation model and phase lag under diurnally changing atmosphere are established components of fuel-moisture modeling (Viney and Catchpole 1991; Catchpole et al. 2001; Nelson, *Water Relations of Forest Fuels*, Section IV). Kochanski et al. (2012) represent multiple fuel time-lag classes and aggregate their moisture by positive weighted averaging. Matthews (2013) reviews equilibrium and response-time models. Those results give the component responses or calibrate them. They do not, in the inspected sections and full accessible texts, state a frequency-and-threshold classification for the **conjunction** of two classwise dry events, nor the contrast asymptotic of its sharp threshold. The conjunction is not the ordinary weighted-average moisture criterion. Mathematical single-pole filter phase formulas themselves are standard and are not claimed as new. Published work on distinct-frequency threshold correlation and on frequency-domain Debye loss peaks addresses different objects and does not imply the same-time, same-frequency joint-excursion result.

## Limitations

The result uses an idealized deterministic harmonic equilibrium, constant relaxation rates and a common absolute dryness cutoff. Dryness of both components is only a diagnostic proxy; it is not an ignition-probability or spread-rate model. It does not account for rain, nonlinear sorption, asymmetric adsorption/desorption, transport, stochastic weather, empirical calibration, or transient history. The threshold \(c_*\) is defined by a scalar maximization, not an elementary closed form; no general uniqueness of its maximizing frequency or of the numbers of local minima/maxima is asserted. The 1991 Viney–Catchpole article and 2001 Catchpole et al. article could not be read completely through open-access routes or institutional access in this inspection; this is a residual historical-priority risk, not proof of novelty. Independent validation has not been performed.

## References

1. Viney, N. R., and Catchpole, E. A. (1991), *Estimating fuel moisture response times from field observations*, International Journal of Wildland Fire 1, 211–214. DOI: https://doi.org/10.1071/WF9910211 (publisher preview and historical review consulted).
2. Catchpole, E. A., et al. (2001), *Estimating fuel response time and predicting fuel moisture content from field data*, International Journal of Wildland Fire 10, 215–222. DOI: https://doi.org/10.1071/WF01011 (public listing dated 13 July 2001; abstract consulted).
3. Nelson, R. M., Jr., *Water Relations of Forest Fuels*, chapter 4 in *Forest Fires*, https://research.fs.usda.gov/download/treesearch/80005.pdf (relevant harmonic response and diffusion sections inspected).
4. Kochanski, A. K., Beezley, J. D., Mandel, J., and Kim, M. (2012), *WRF fire simulation coupled with a fuel moisture model and smoke transport by WRF-Chem*, arXiv:1208.1059, https://arxiv.org/abs/1208.1059 (full five-page manuscript inspected; first arXiv posting 5 August 2012).
5. Matthews, S. (2013), *Dead fuel moisture research: 1991–2012*, https://doi.org/10.1071/WF13005 (full accessible HTML, relevant modeling and sources sections inspected; online 10 September 2013).

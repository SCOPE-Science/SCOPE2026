# Exact activation and midpoint-crossing laws for two fixed water pulses under saturating uptake

## Finding
Consider two prescribed positive water additions to a linearly draining root-zone store, the first at the beginning of a finite season and the second at a freely chosen time. With a saturating instantaneous response, there is a unique globally optimal second-pulse time. The optimum switches from coincident application to strictly staggered application at one exact season-length threshold. A second, different threshold for scheduling the optimal pulse *after* the season midpoint exists if and only if the first pulse exceeds the second pulse by more than the response half-saturation storage.

Precisely, define the dimensionless first and second pulse magnitudes \(a=A/K>0\) and \(b=B/K>0\), the dimensionless season length \(h=\kappa H>0\), and \(q=e^{-h}\). Put
\[
 x_*(q)=q+\sqrt{q^2+q(1+b)/a},\qquad
 \kappa\tau_*=-\log\bigl(\min\{1,x_*(q)\}\bigr).
\]
Then \(\tau_*\) is the **unique** maximizer of cumulative response over all \(0\le\tau\le H\), and it always satisfies \(\tau_*<H\). Define
\[
 h_0=\log\left(2+\frac{1+b}{a}\right).
\]
For \(h\le h_0\), the optimum is exactly \(\tau_*=0\); for \(h>h_0\), it lies strictly inside \((0,H)\). If \(a\le1+b\), every interior optimum precedes the midpoint \(H/2\). If \(a>1+b\), set
\[
 h_{1/2}=2\log\left(\frac{2a}{a-b-1}\right)>h_0.
\]
For \(h_0<h<h_{1/2}\), the optimum precedes the midpoint; it occurs exactly at the midpoint for \(h=h_{1/2}\); and it follows the midpoint for \(h>h_{1/2}\). On the interior branch,
\[
 \frac{d\tau_*}{dH}=\frac12\left(1+\sqrt{\frac{q}{q+(1+b)/a}}\right)\in\left(\tfrac12,1\right),
 \qquad
 \kappa\tau_*=\frac h2+\frac12\log\frac{a}{1+b}+o(1)\quad(h\to\infty).
\]
These inequalities and transition boundaries are strict except at the displayed equality cases.

## Assumptions and scope
Let \(K,\kappa,H,A,B>0\). An initially empty, non-capacity-constrained deterministic water store \(S(t)\) receives an instantaneous input \(A\) at time \(0\) and an input \(B\) at a selected time \(\tau\in[0,H]\). Between inputs, \(\dot S(t)=-\kappa S(t)\). Simultaneous inputs are added. A normalized, instantaneous water-limited assimilation proxy is \(g(S)=S/(K+S)\). The objective is exactly
\[
 J(\tau)=\int_0^H g(S(t))\,dt.
\]
There is no rainfall other than these two inputs, no capacity overflow, no additional water treatment, and no feedback from instantaneous assimilation into the draining-store equation. The pulse magnitudes, their order, and the first pulse date are fixed. The result is a **mathematical benchmark**, not a calibrated agricultural yield prediction or a claim about unrestricted irrigation optimal control.

## Proof
For \(0<t<\tau\), \(S(t)=A e^{-\kappa t}\); for \(\tau<t<H\),
\[
 S(t)=A e^{-\kappa t}+B e^{-\kappa(t-\tau)}.
\]
Let \(x=e^{-\kappa\tau}\), so that \(q\le x\le1\). Since the antiderivative of \(g(Ce^{-\kappa t})\) is \(-\kappa^{-1}\log(K+Ce^{-\kappa t})\), integrating the two segments yields the exact identity
\[
 \kappa J(\tau)=\log\left[\frac{(1+a)(1+a x+b)}{(1+a x)(1+a q+bq/x)}\right]. \tag{1}
\]
Set \(F(x)=\frac{1+a x+b}{(1+a x)(1+a q+bq/x)}\). Its derivative is
\[
 F'(x)=-\frac{b\{a x^2-2a qx-q(1+b)\}}{(1+a x)^2(x+a qx+bq)^2}. \tag{2}
\]
The quadratic numerator has exactly one positive zero,
\(x_*=q+\sqrt{q^2+q(1+b)/a}\), and its other zero is negative. Consequently \(F\) increases strictly for \(x<x_*\) and decreases strictly for \(x>x_*\). Also \(x_*>q\), excluding a terminal optimum. The constrained maximum is uniquely at \(x=\min\{1,x_*\}\). As \(x_*\le1\) is equivalent to \(q\le a/(2a+b+1)\), the exact activation threshold is \(h_0=\log[(2a+b+1)/a]\). At equality \(x_*=1\), uniqueness still follows from the strict sign on the interior.

For interior optima, \(\tau_*>H/2\) is equivalent to \(x_*<\sqrt q\). Evaluating the quadratic numerator at \(\sqrt q\) gives
\[
 a q\left(1-2\sqrt q\right)-q(1+b).
\]
Since the numerator increases through its unique positive zero, \(x_*<\sqrt q\) precisely when \(a(1-2\sqrt q)>1+b\). This is impossible for \(a\le1+b\). For \(a>1+b\), it holds precisely when \(q<[(a-b-1)/(2a)]^2\), giving \(h_{1/2}\) and the strict three-regime classification. Moreover \(h_{1/2}>\log4>h_0\) when \(a>1+b\), because then \(h_0<\log3\).

Finally rewrite \(x_*=\sqrt q(\sqrt q+\sqrt{q+c})\), with \(c=(1+b)/a>0\). Differentiating \(-\log x_*\) with respect to \(h=-\log q\) gives \(\frac12[1+\sqrt{q/(q+c)}]\), strictly between one half and one. As \(q\downarrow0\), \(x_*/\sqrt q\to\sqrt c\), which proves the asymptotic midpoint offset.

## Verification
The standalone `verify.py` evaluates the exact antiderivative against independent numerical quadrature, checks the closed-form optimizer against competing times over a fixed-seed parameter grid, checks the analytic activation and midpoint regimes, and symbolically verifies the derivative identity (2). At packaging, it completed 36,369 assertions. Those finite checks are supplementary: uniqueness, all-parameter validity and the strict transitions are established by the proof above, not by enumeration.

For the illustrative dimensionless parameters \(a=4\), \(b=1\), \(h=4\), the optimal normalized delay is \(\kappa\tau_*=2.156330240472\ldots\); the integrated dimensionless response \(\kappa J\) is \(1.922098393379\ldots\), versus \(1.704134935351\ldots\) for two coincident pulses, a relative increase of about \(12.79\%\). Here \(h_0=\log(5/2)\) and \(h_{1/2}=\log16\), so this example lies beyond the midpoint-crossing threshold.

## Relationship to prior work
The formulation is motivated by classic ecohydrological accounts of transient soil-moisture depletion and plant-water response. Shani, Tsur and Zemel (2004) optimize a continuously adjustable irrigation rate in a coupled biomass-moisture system and obtain a turnpike policy; they do not impose exactly two prescribed, ordered instantaneous pulses or state the closed-form delay and midpoint transitions above. Viola and collaborators (2008) analyze transient stochastic soil moisture and linear-loss regimes rather than scheduling two fixed inputs to optimize a saturating time integral. Vico and Porporato (2013) derive yield distributions for rainfall-driven and demand-triggered irrigation regimes, including instantaneous refill at a moisture intervention threshold, but not the fixed two-input calendar optimization of (1).

The underlying exponential decay and rational saturation are established modeling devices, and the derivative calculation is elementary once the exact objective is written down. No general priority claim is made about impulse control or continuous irrigation scheduling. The contribution assessed here is the *complete exact classification* for this fixed-pulse finite-horizon objective, including the distinct midpoint crossing and sensitivity law.

## Limitations
A leaky, unbounded, single-store response is not a field-calibrated crop system. Real root zones can exhibit upper storage capacity, nonlinear hydraulic losses, evapotranspiration coupling, variable solar input, phenological stages, spatial heterogeneity, and rewetting delays. Different response laws or variable dosing can invalidate the thresholds. The evidence does not establish novelty against all historical optimal impulse scheduling theorems; Hall and Butcher (1968), *Optimal Timing of Irrigation*, was located but its complete primary text was inaccessible, so its potential implications remain unresolved. That work appears to use a crop-deficit dynamic-programming formulation, but abstract and discussion alone cannot establish full non-coverage. Computations do not provide independent mathematical certification or ecological validation.

## References
1. Shani, U., Tsur, Y., and Zemel, A. *Optimal dynamic irrigation schemes*. Optimal Control Applications and Methods (2004), DOI: https://doi.org/10.1002/oca.740 ; accessible author manuscript: https://www.academia.edu/102278562/Optimal_dynamic_irrigation_schemes . First published online 11 May 2004.
2. Viola, F., Daly, E., Vico, G., Cannarozzo, M., and Porporato, A. *Transient soil-moisture dynamics and climate change in Mediterranean ecosystems*. Water Resources Research (2008), https://doi.org/10.1029/2007WR006371 . First published 11 November 2008.
3. Vico, G., and Porporato, A. *Probabilistic description of crop development and irrigation water requirements with stochastic rainfall*. Water Resources Research (2013), https://doi.org/10.1002/wrcr.20134 . First published 13 February 2013.
4. Hall, W. A., and Butcher, W. S. *Optimal Timing of Irrigation*. Journal of the Irrigation and Drainage Division 94(2) (1968), 267–275, https://doi.org/10.1061/JRCEA4.0000569 . Full text not inspected.

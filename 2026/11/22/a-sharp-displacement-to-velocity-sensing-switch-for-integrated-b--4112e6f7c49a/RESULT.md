# A sharp displacement-to-velocity sensing switch for integrated Brownian-bridge recovery

## Finding
Let \(B\) be the standard centered Brownian bridge on \([0,1]\), and set \(X(s)=\int_0^s B(u)\,du\). Exactly one scalar observation is permitted, with freely chosen time \(t\in[0,1]\) and one of two modes: displacement \(X(t)\) or velocity \(B(t)\). Add independent centered Gaussian noise of the **same prescribed variance** \(\eta>0\) in whichever calibrated mode is selected. Optimize the integrated posterior variance of the **entire** displacement trajectory \(X\).

There are exactly two transitions, with no additional optimal designs:

1. At \(\eta_{\mathrm{p}}=11/336\), the uniquely optimal *displacement-mode* observation reaches the terminal time \(t=1\), continuously from the interior. For all larger noise values it remains at \(t=1\).
2. There is one and only one *modality* transition, at
   \[
   \eta_* = 0.03486395077318212468\ldots>\eta_{\mathrm{p}}.
   \]
   For \(0<\eta<\eta_*\), the unique global mode is displacement: its optimal time is interior when \(\eta<\eta_{\mathrm{p}}\), and exactly \(1\) when \(\eta\ge\eta_{\mathrm{p}}\). At \(\eta=\eta_*\), terminal displacement and one unique interior velocity observation tie. For \(\eta>\eta_*\), only the velocity observation is optimal; its optimal time is strictly increasing with \(\eta\), always in \((2/5,\sqrt6-2)\).

The velocity time at the switch is \(t_*=0.415468520035678\ldots\), the unique root in \((41/100,42/100)\) of
\[
P(t)=336t^7+84t^6-3150t^5+5530t^4-3780t^3+1092t^2-138t+13.
\]
Writing
\[
J_{\mathrm v}(t)=\frac{t^2(1-t)^2(8-4t-t^2)}{60},\quad
V_{\mathrm v}(t)=t(1-t),\quad
J_{\mathrm p}(1)=\frac{13}{5040},\quad V_{\mathrm p}(1)=\frac1{12},
\]
the threshold is specified *exactly* by
\[
\eta_* = \frac{J_{\mathrm v}(t_*)V_{\mathrm p}(1)-J_{\mathrm p}(1)V_{\mathrm v}(t_*)}{J_{\mathrm p}(1)-J_{\mathrm v}(t_*)}.
\]

## Assumptions and scope
The covariance of \(B\) is \(\operatorname{Cov}(B(s),B(t))=\min(s,t)-st\). The time horizon and both output scales are fixed by the stated normalization; equal additive variance is an assumption on **calibrated readouts**, not invariant under arbitrary rescaling of position relative to velocity. Observation noise is independent of \(B\). The estimator is the conditional mean, and the risk is
\[
\mathcal R=\int_0^1\operatorname{Var}(X(s)\mid Y)\,ds.
\]
No cost, delay, or mode-switching penalty is included. The result covers one observation, exactly these two scalar modes, and every finite \(\eta>0\); it does not address estimating \(B\) itself, repeated observations, other kernels, or unequal sensor-noise variances.

## Proof
**1. Exact posterior reductions.** For \(s\le t\), the covariance of integrated bridge values is
\[
C_{\mathrm p}(s,t)=\frac{s^2(3t-s)}6-\frac{s^2t^2}4,
\]
and for \(s\ge t\), exchange \(s,t\). The covariance between \(X(s)\) and \(B(t)\) is
\[
C_{\mathrm v}(s,t)=\begin{cases}s^2(1-t)/2,&s\le t,\\ts-t^2/2-ts^2/2,&s\ge t.\end{cases}
\]
Direct integration gives
\[
\begin{aligned}
V_{\mathrm p}(t)&=\frac{t^3(4-3t)}{12},&J_{\mathrm p}(t)&=\frac{t^4(168-280t+140t^2-8t^3-7t^4)}{5040},\\
V_{\mathrm v}(t)&=t(1-t),&J_{\mathrm v}(t)&=\frac{t^2(1-t)^2(8-4t-t^2)}{60}.
\end{aligned}
\]
Here \(J\) is the integral of the square of the relevant cross-covariance, and \(V\) its observation variance without noise. Gaussian conditioning yields
\[
\mathcal R_m(t,\eta)=\frac1{30}-\frac{J_m(t)}{\eta+V_m(t)},\qquad m\in\{\mathrm p,\mathrm v\}.
\]
Thus each mode maximizes its own positive gain \(G_m(t,\eta)=J_m(t)/(\eta+V_m(t))\).

**2. Complete displacement timing.** Put
\[
A(t)=2016-2184t+336t^2+168t^3,\quad
D(t)=21t^4+4t^3-238t^2+392t-168.
\]
The sign of \(\partial_tG_{\mathrm p}\) is the sign of
\[
\eta A(t)-t^3D(t),\qquad 0<t<1,
\]
since its derivative numerator is \(t^3(1-t)[\eta A(t)-t^3D(t)]/15120\). On \([0,1]\), \(A\) is positive and strictly decreasing, with \(A(1)=336\). The polynomial \(D\) is strictly increasing: \(D''(t)<0\) and \(D'(1)=12>0\); \(D(0)=-168\), \(D(1)=11\). Therefore \(D\) has one zero \(t_{\mathrm p,0}=0.744149246585911\ldots\). The function \(t^3D(t)/A(t)\) is strictly increasing from zero to \(11/336\) on \((t_{\mathrm p,0},1]\). This proves the unique interior maximizer for \(\eta<11/336\) and the unique terminal maximizer otherwise, including equality.

**3. Complete velocity timing.** Set \(b(t)=4t^3+9t^2-24t+8\). Direct differentiation gives
\[
\frac{d}{dt}\left(\frac{J_{\mathrm v}}{V_{\mathrm v}}\right)=\frac{b(t)}{60},\qquad
J_{\mathrm v}'(t)=\frac{t(1-t)(3t-4)(t^2+4t-2)}{30}.
\]
The polynomial \(b\) has its only zero in \((0,1)\) at \(t_{\mathrm v,0}=0.406490758540456\ldots\); it is positive before and negative after. The derivative \(J_{\mathrm v}'\) is positive before \(t_{\mathrm v,\infty}=\sqrt6-2\) and negative after. Consequently the derivative of \(G_{\mathrm v}\), proportional to
\(\eta J_{\mathrm v}'+V_{\mathrm v}^2(J_{\mathrm v}/V_{\mathrm v})'\), is positive before \(t_{\mathrm v,0}\) and negative after \(t_{\mathrm v,\infty}\). In between its zero condition is
\[
\eta=H_{\mathrm v}(t):=\frac{t(1-t)[-b(t)]}{2(4-3t)(2-4t-t^2)}.
\]
On \((t_{\mathrm v,0},t_{\mathrm v,\infty})\), the positive numerator factors are strictly increasing while the positive denominator factors are strictly decreasing. Moreover \(H_{\mathrm v}\) runs from zero to infinity. Hence a unique global velocity maximizer \(t_{\mathrm v}(\eta)\) exists and increases strictly from \(t_{\mathrm v,0}\) to \(t_{\mathrm v,\infty}\) as \(\eta\) grows. In particular \(2/5<t_{\mathrm v}(\eta)<\sqrt6-2<1/2\).

**4. Exactly one modality crossover.** Let \(F_m(\eta)=\max_{0\le t\le1}G_m(t,\eta)\). The unique time optima imply the envelope identity
\[
\frac{d}{d\eta}\log\frac{F_{\mathrm p}(\eta)}{F_{\mathrm v}(\eta)}
=-\frac1{\eta+V_{\mathrm p}(t_{\mathrm p}(\eta))}
+\frac1{\eta+V_{\mathrm v}(t_{\mathrm v}(\eta))}<0,
\]
because \(V_{\mathrm p}\le1/12<6/25<V_{\mathrm v}(t_{\mathrm v}(\eta))\). Thus the gain ratio is strictly decreasing; multiple crossovers are impossible.

For small noise, the displacement gain at \(t=3/4\) tends to \(7977/250880>13/500\), while the optimal velocity gain tends to at most \(13/500\), because its time lies above \(2/5\) and below \(1/2\). For large noise, \(\eta F_{\mathrm p}(\eta)\to J_{\mathrm p}(1)=13/5040\), since \(J_{\mathrm p}\) increases with time: its derivative is \(2\int_0^1 C_{\mathrm p}(s,t)C_{\mathrm v}(s,t)\,ds>0\) for \(0<t<1\). Meanwhile \(\liminf\eta F_{\mathrm v}(\eta)\ge J_{\mathrm v}(2/5)=468/78125>13/5040\). Therefore exactly one positive crossover exists.

It occurs **strictly after** \(\eta_{\mathrm p}=11/336\). At that value \(F_{\mathrm p}=1/45\). Exact derivative signs localize \(t_{\mathrm v}(\eta_{\mathrm p})\) inside \((41/100,42/100)\), where
\[
F_{\mathrm v}(\eta_{\mathrm p})
\le \frac{J_{\mathrm v}(42/100)}{\eta_{\mathrm p}+V_{\mathrm v}(41/100)}
=\frac{39874528953}{1802312500000}<\frac1{45}.
\]
At \(\eta=1/25\), evaluating velocity at \(t=5/12\) already gives a gain strictly larger than the optimal terminal displacement gain. At \(\eta=1/25\) the velocity gain derivative at \(t=42/100\) is still negative, so that mode’s unique optimal time is below \(42/100\). Thus \(11/336<\eta_*<1/25\), and its velocity time lies in \((41/100,42/100)\).

**5. Algebraic isolation.** On this last time interval, equality of the two optimal gains (displacement is now at \(1\)) and the velocity first-order condition eliminate \(\eta\). Cancelling factors that are nonzero there leaves precisely \(P(t)=0\), with \(P\) given in the Finding. Exact rational arithmetic verifies \(P(41/100)>0>P(42/100)\). Under \(t=41/100+u/100\), all seven degree-six Bernstein coefficients of \(P'(t)\) lie strictly between \(-53\) and \(-52\), proving strict negativity throughout the interval and hence exactly one root. Substituting it into the gain-equality equation gives the exact \(\eta_*\) above. The two distinct optima at equality and all strict regimes follow.

## Verification
Run `python verification.py` with SymPy and SciPy installed. The checker symbolically rederives both squared-covariance integrals, derivative factorizations, algebraic elimination and rational comparison inequalities. It checks the Bernstein derivative sign and gives rational enclosures for the root and noise threshold before conversion to floating point for the numerical illustrations. It also performs 32 independently integrated covariance-square numerical checks and 10 numerical modality comparisons. The infinite-domain assertions rely on the analytic sign and monotonicity arguments above, **not** on numerical grids or sampled parameter values.

## Relationship to prior work
Lachal (arXiv:1108.2132, Sections 4–5) treats the integrated Brownian bridge as a Gaussian process, supplies its covariance and examines conditional prediction. Ji and Müller (arXiv:1604.05375, Section 2 and Appendix A.3) give the general integrated posterior-risk design criterion for noisy functional observations. These are essential precursors: the covariance and general criterion themselves are **not** new. Their inspected results do not state the competing displacement/velocity optimization, the strict single-crossing rule, or the exact algebraic threshold.

Mukherjee's dissertation discusses integrated prediction design for product-type covariance kernels, including Brownian motion and Brownian bridge. The integrated bridge covariance here is *not* a single product \(u(s)v(t)\) for \(s<t\), and choosing between a process and its derivative is not included in that abstract. Its full dissertation was not accessible for a complete comparison. A result on derivative-only placement is also closely related; derivative-only timing is supporting context, not the new point of this claim. The new finding is the unique **cross-modality** decision together with its displacement endpoint stage and rigorously isolated switch.

## Limitations
The numeric crossover is specific to the stated time horizon, process amplitude, unweighted integrated trajectory loss, and common additive-noise variance in calibrated displacement/velocity readouts. Arbitrarily changing the relative units or noise intensities changes the decision and may eliminate or move the crossover. This is not a theorem for arbitrary kernels, continuous real-time filtering, multiple observations, or physical actuators. Published-priority completeness is limited by the inaccessible dissertation and potentially unindexed equivalent formulations.

## References
- A. Lachal, *A class of bridges of iterated integrals of Brownian motion related to various boundary value problems involving the one-dimensional polyharmonic operator*, arXiv:1108.2132v1 (public 10 August 2011), especially Sections 4–5. https://arxiv.org/abs/1108.2132
- H. Ji and H.-G. Müller, *Optimal Designs for Longitudinal and Functional Data*, arXiv:1604.05375v1 (public 18 April 2016), especially Section 2 and Appendix A.3. https://arxiv.org/abs/1604.05375
- B. Mukherjee, *Optimal designs for estimating the path of a stochastic process*, doctoral dissertation, Purdue University, abstract and bibliographic record. https://docs.lib.purdue.edu/dissertations/AAI3043760/

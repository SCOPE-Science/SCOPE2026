# A sharp exponent-gap phase diagram for apparent Omori decay in two coeval components

## Finding

Consider two positive, coeval modified-Omori intensities with the **same** offset time but distinct power-law exponents:
\[
\lambda(t)=\frac{A}{(t+c)^p}+\frac{B}{(t+c)^q},\quad t\ge0,\quad A,B,c>0,\quad0<p<q.
\]
Set \(\delta=q-p\) and the dimensionless relative amplitude \(k=(A/B)c^\delta\). Define the instantaneous log-time decay exponent \(E(t)=-d\log\lambda(t)/d\log t\) for \(t>0\), with \(E(0)=0\) by continuity. Then the **complete phase diagram of strict local extrema of \(E\)** is:

- For \(0<\delta<1\), \(E\) has exactly one stationary time, a strict local (indeed global) maximum, for every \(k>0\).
- For \(\delta=1\), \(E\) has exactly one strict global maximum if \(0<k<1/p\), and is strictly increasing for \(k\ge1/p\).
- For \(\delta>1\), there is an explicit sharp amplitude ratio \(k_*\) such that \(0<k<k_*\) gives exactly two stationary times, first a strict local maximum and then a strict local minimum. At \(k=k_*\) there is one non-extremal stationary time of multiplicity two; for \(k>k_*\), \(E\) is strictly increasing. Thus two-turn apparent decay occurs for some amplitude ratio **if and only if the two Omori exponents differ by more than one**.

To specify the sharp ratio for \(\delta>1\), let
\[
a=\frac{p}{\delta^2},\qquad b=\frac{p+\delta}{\delta^2},\qquad C=1+\frac{2p+\delta}{\delta^2},\qquad g(u)=C+au+\frac bu,
\]
\[
u_* = \frac{C+\sqrt{C^2+4ab(\delta^2-1)}}{2a(\delta-1)},\qquad
k_* = \frac{u_*}{g(u_*)^\delta},\qquad t_*=c(g(u_*)-1).
\]
At the equality threshold, \(t_*\) is the unique, double stationary time. For \(0<k<k_*\), the two stationary times are reconstructed by solving \(u/g(u)^\delta=k\) for the unique two roots \(u_-<u_*<u_+\) and setting \(t_\pm=c(g(u_\pm)-1)\).

An exact rational instance is \(p=1,q=3,c=1\). Here \(u_*=9\), \(t_*=10/3\), and \(k_*=81/169\). At \(A/B=k=1/3\), the local maximum occurs exactly at \(t=2\), with \(E(2)=1\); the subsequent local minimum lies at \(t\approx8.419900819340\), with \(E(t)\approx0.952304494038\). The original intensity \(\lambda\) is strictly decreasing throughout: the turning behavior concerns **its apparent decay exponent**, not aftershock counts themselves.

## Assumptions and scope

All parameters \(A,B,c,p,q\) are real and strictly positive with \(p<q\). Both components begin at the same origin \(t=0\), share one positive offset \(c\), and are added linearly. The local exponent is differentiated with respect to elapsed time \(t\), not shifted time \(t+c\); the latter choice would make the instantaneous exponent monotone and would be a different observable. A stationary time is any finite \(t>0\) with \(E'(t)=0\). No smooth stochastic fit, physical causal separation of subpopulations, or parameter identifiability from finite counts is claimed.

## Proof

**1. Dimensionless reduction.** Put \(y=1+t/c>1\), \(u=ky^\delta>0\). Factoring the faster term from \(\lambda\) and differentiating gives
\[
E(t)=\left(1-\frac1y\right)\left(p+\frac{\delta}{1+u}\right),\qquad
\frac{dE}{dt}=\frac{H(y,u)}{c y^2(1+u)^2},
\]
where
\[
H(y,u)=p(1+u)^2+\delta(1+u)-\delta^2(y-1)u.
\]
The denominator is positive, so the sign and multiplicity of the derivative are exactly those of \(H\). At \(t=0\), \(H(1,k)>0\).

**2. Exact stationary parametrization.** Solving \(H=0\) for \(y\) gives \(y=g(u)=C+au+b/u\). Conversely every \(u>0\) satisfying
\[
k=\kappa(u):=\frac{u}{g(u)^\delta}
\]
yields exactly one positive stationary time \(t=c(g(u)-1)\) because \(g(u)>1\), \(u=k g(u)^\delta\), and \(y\mapsto u=ky^\delta\) is strictly increasing. Thus counting stationary times is *equivalent* to counting positive solutions of \(\kappa(u)=k\); there are no additional branches. Direct differentiation shows
\[
\operatorname{sgn}\kappa'(u)=\operatorname{sgn}\left(C+a(1-\delta)u+\frac{b(1+\delta)}u\right).
\]

**3. Complete classification.** If \(0<\delta<1\), the parenthesis is positive, while \(\kappa(0+)=0\) and \(\kappa(+\infty)=+\infty\); there is exactly one stationary time. If \(\delta=1\), the same strict positivity holds, but \(\kappa(+\infty)=1/p\); precisely the positive \(k<1/p\) have a stationary time. If \(\delta>1\), the parenthesis has exactly one positive zero \(u_*\), because after multiplication by \(u\) it is a strictly concave quadratic with positive intercept and negative leading coefficient. The formula for \(u_*\) above is its positive root. Furthermore \(\kappa(0+)=\kappa(+\infty)=0\), so \(\kappa\) rises strictly to its unique positive maximum \(k_*\), then falls strictly. Every horizontal level below, equal to or above \(k_*\) therefore has respectively two, one tangent, or zero positive intersections.

**4. Type and multiplicity of stationary times.** The derivative has positive sign at \(t=0\). At large \(y\), \(H(y,ky^\delta)\) is negative for \(0<\delta<1\) because its dominant term is \(-\delta^2k y^{\delta+1}\); it is positive for \(\delta>1\) because \(p k^2y^{2\delta}\) dominates. For \(\delta=1\), the zero count and the strict positivity at the origin force a maximum when a zero exists and no decrease otherwise. In the \(\delta>1,0<k<k_*\) case the two intersections are simple and, by continuity, the signs must alternate \(+,-,+\), giving a strict maximum followed by a strict minimum. At the unique critical level, \(\kappa''(u_*)<0\); hence the derivative has a double zero without sign change. The function remains strictly increasing despite this isolated stationary point. This exhausts all finite \(t>0\) and all allowed parameters.

**5. Rational exact witness.** For \(p=1,\delta=2\), \(a=1/4\), \(b=3/4\), \(C=2\), and the maximum of \(\kappa\) occurs at \(u_*=9\), with \(g(9)=13/3\) and \(k_*=81/169\). For \(k=1/3\), writing \(y=t+1\) gives
\[
9H\left(y,y^2/3\right)=(y-3)(y^3-9y^2-3y-9).
\]
The cubic has exactly one positive root (Descartes' rule of signs, or strict increase for \(y>3+\sqrt{10}\)); it lies strictly between \(9\) and \(10\). Thus \(y=3\) is the unique local maximum and the cubic root is the unique local minimum. Substituting \(y=3\) into the closed expression gives \(E=1\). The numerical values above are only approximations of exact implicitly defined times and values.

## Verification

The bundled standard-library-only `checker.py` independently evaluates the derivative identity by central differences, exhaustively certifies the rational polynomial factorization over a finite exact-integer test set, directly checks the rational critical point, and samples the sign structure in all three exponent-gap regimes. A fresh replay from the embedded file passed **3,668 assertions**. The analytic reduction to the one-variable function \(\kappa\), not these finite tests, proves the infinite-parameter theorem. To reproduce: run `python3 checker.py` from a directory containing the extracted file.

## Relationship to prior work

Utsu, Ogata and Matsu’ura (1995), Section 2, reproduce Omori's original additive expansion in powers one and two at a *shared* offset; that is a natural motivating boundary \(\delta=1\), precisely where two-turn apparent decay is impossible under the present theorem. In Section 4.1 they also model superposed *secondary* aftershock sequences with distinct onset times, unlike the present coeval shared-offset components. Their survey supplies historical model context but does not in these materially inspected sections establish the present exact global log-time slope phase diagram. Sornette and Sornette (1999) derive two different effective exponent regimes from a branching integral equation: an *emergent* crossover, not the positive sum of two fixed coeval components whose instantaneous exponent develops a maximum and a minimum. Lolli, Boschi and Gasperini (2009) compare single Omori, stretched-exponential and band-limited decay laws and fitting performance, rather than the sharp shared-offset two-component threshold. A closely relevant published mathematical classification treats equal exponents with **different offsets** and does not subsume the present equal-offset/different-exponent analysis. Similarity of the qualitative word “reentrant” alone is not a statement-level implication.

## Limitations

This is a structural result for the declared two-term idealization only. It does not validate a physical two-source hypothesis, identify component parameters from noisy data, quantify discretization or estimator bias, or imply that real catalogues exhibit the turn sequence. Derivatives of noisy log rates can be unstable. Adding a constant background, unequal offsets, further components, or rate-dependent censoring can change the extremum count. Prior mathematical work on generalized mixture log-slopes might contain a stronger equivalent theorem; a targeted literature search and the comparisons above are not a proof of first publication. The literature review did not inspect every page of the long 1995 survey, and independent scholarly priority validation remains to be done.

## References

1. T. Utsu, Y. Ogata and R. S. Matsu’ura, “The centenary of the Omori formula for a decay law of aftershock activity,” *Journal of Physics of the Earth* **43** (1995), 1–33. https://doi.org/10.4294/jpe1952.43.1 ; inspection copy: https://earthjay.com/earthquakes/20180928_indonesia/utsu_etal_1995_centenary_omoris_law.pdf .
2. A. Sornette and D. Sornette, “Renormalization of earthquake aftershocks,” arXiv:cond-mat/9905314, publicly submitted 21 May 1999. https://arxiv.org/abs/cond-mat/9905314 .
3. B. Lolli, E. Boschi and P. Gasperini, “A comparative analysis of different models of aftershock rate decay by maximum likelihood estimation of simulated sequences,” *J. Geophys. Res. Solid Earth* **114** (2009), B01303. https://doi.org/10.1029/2008JB005614 .

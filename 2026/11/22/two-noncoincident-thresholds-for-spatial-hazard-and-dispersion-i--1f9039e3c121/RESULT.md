# Two noncoincident thresholds for spatial hazard and dispersion in an Erlang-two resetting diffusion

## Finding
A reflected Brownian particle whose Poisson resets replace the current position \(X\) by \((B-X)^+\), with independently sampled two-stage Erlang capacity \(B\), has a stationary spatial-tail hazard that changes sharply from bathtub-shaped to increasing, but the coefficient of variation crosses its exponential reference value at a strictly *smaller* and distinct parameter threshold. Thus an interval of strictly underdispersed stationary position laws nevertheless has a decreasing-then-increasing spatial exceedance hazard.

Put \(t=\beta\sqrt{D/q}\), where \(D\) is diffusivity, \(q\) is reset-alarm rate, and \(\beta\) is Erlang capacity rate. The two exact boundaries are the unique positive roots
\[
P_v(t)=256t^7+1088t^6+1776t^5+1280t^4+184t^3-308t^2-191t-34=0,
\]
\[
P_h(t)=128t^7+448t^6+464t^5-160t^4-720t^3-604t^2-217t-28=0.
\]
They are \(t_v=0.524162084373\ldots\) and \(t_h=1.171586043499\ldots\). For \(0<t<t_h\) the spatial-tail hazard has exactly one strictly positive minimum; for \(t\ge t_h\) it is strictly increasing on positive positions. The stationary squared coefficient of variation is above one for \(t<t_v\), equal to one at \(t=t_v\), and below one for \(t>t_v\). These are statements about *stationary position*, not temporal failure times.

## Assumptions and scope
Fix \(D,q,\beta>0\). Between independent Poisson alarms of rate \(q\), \(X\) is Brownian motion reflected at the origin on \([0,\infty)\), with infinitesimal generator \(D\partial_{xx}\). At each alarm, independently draw \(B\) with density \(\beta^2 b e^{-\beta b}\) on \(b>0\), and replace the pre-alarm position \(x\) by \((B-x)^+=\max(B-x,0)\). All driving randomness is independent. Write \(k=\sqrt{q/D}\), \(Y=kX\), and \(t=\beta/k\). The dimensionless stationary density is \(g_t(y)\), survival \(S_t(y)=\int_y^\infty g_t(z)\,dz\), and spatial exceedance hazard \(h_t(y)=g_t(y)/S_t(y)\) for \(y\ge0\). A bathtub hazard strictly decreases then strictly increases with one positive minimum. The squared coefficient of variation is \(\operatorname{CV}^2(Y)=\operatorname{Var}(Y)/(\mathbb EY)^2\).

## Proof
**Existence and uniqueness.** Let \(Z_n\) be positions just before successive independent Poisson alarms. Its transition consists of the reset to \((B-Z_n)^+\) followed by independent reflected Brownian diffusion for an exponential time \(T\). In dimensionless units the update has law \(Z_{n+1}=|(B-Z_n)^+ +\sqrt{2T}\,G|\), where \(G\) is standard normal and \(T\) has unit exponential law. Its second moment obeys \(\mathbb E[Z_{n+1}^2\mid Z_n=z]\le \mathbb E[B^2]+2\), uniformly in \(z\). The one-step transition has strictly positive continuous density on positive positions; a compact-set minorization together with the uniform moment drift gives positive Harris recurrence and a unique invariant law. Independent Poisson arrivals sample the continuous-time stationary law, so stationarity is unique at arbitrary times.

**Stationary resolvent.** Define \(v=\mathbb E e^{-tY}\) and \(v_1=-\mathbb E(Ye^{-tY})\). The quantity \(v_1\) is a derivative of the spatial Laplace transform with the stationary measure held fixed, **not** a total derivative of \(v\) as model parameter \(t\) varies. The reset location has an atom of size \(1-v+tv_1\) at zero and density \(t^2e^{-ty}(yv-v_1)\) on \(y>0\), because \(\Pr((B-Y)^+>y)=e^{-ty}[(1+ty)v-tv_1]\). Consequently the invariant density satisfies
\[
g''-g+t^2e^{-ty}(yv-v_1)=0\quad(y>0),\qquad -g'(0)=1-v+tv_1,\quad\int_0^\infty g(y)\,dy=1.
\]
Set \(Q(t)=16t^4+64t^3+120t^2+96t+23\). When \(t\ne1\), the unique normalized solution obtained from the affine-exponential ansatz is
\[
g_t(y)=Ae^{-y}+(C+Ey)e^{-ty},
\]
\[
A=\frac{(t+1)^2(16t^4-8t^2+7)}{(t-1)^2Q},\qquad
C=\frac{-4t(12t^3+8t^2-4t-1)}{(t-1)^2Q},\qquad
E=\frac{-4t^2(2t+1)(2t+3)}{(t-1)Q}.
\]
This expression is a probability density despite cancellations among the separate coefficients, as it is the unique invariant density of the positive recurrent process. At the removable resonance \(t=1\), the limiting solution is
\[
g_1(y)=\frac{30y^2+68y+191}{319}e^{-y},\qquad
S_1(y)=\frac{30y^2+128y+319}{319}e^{-y}.
\]
For \(t\ne1\) the survival is \(S_t(y)=Ae^{-y}+[C/t+E(y/t+1/t^2)]e^{-ty}\).

**Unique spatial-hazard minimum.** Put
\[
K_0=\frac{4(8t^3-4t^2-15t-4)}{Q},\qquad
K_1=\frac{4t(t-1)(2t+1)(2t+3)}{Q}.
\]
Direct differentiation gives the nonasymptotic exact identity
\[
S_t(y)^2h'_t(y)=Ae^{-(1+t)y}(K_0+K_1y)+\frac{E^2}{t^2}e^{-2ty}.
\]
Its sign equals the sign of \(F_t(y)=Ae^{(t-1)y}(K_0+K_1y)+E^2/t^2\). Since \(A>0\) for all \(t>0\), and
\[
K_1+(t-1)K_0=\frac{16(t-1)^2(t+1)(3t+1)}{Q}>0,\qquad
(t-1)K_1\ge0,
\]
one has \(F'_t(y)>0\) for \(t\ne1\) and all \(y\ge0\). Moreover \(F_t(y)\to E^2/t^2>0\) if \(t<1\), and \(F_t(y)\to+\infty\) if \(t>1\). The origin sign is \(F_t(0)=4P_h(t)/Q(t)^2\). Descartes' rule of signs gives exactly one positive root of \(P_h\); direct evaluation shows it exceeds one. Thus for \(t<t_h\), \(h'_t\) changes sign precisely once, from negative to positive; for \(t>t_h\), it is everywhere positive, while at \(t=t_h\) it vanishes only at the origin. At \(t=1\), direct differentiation yields
\[
h_1'(y)=\frac{4(450y^2+1920y-689)}{(30y^2+128y+319)^2},
\]
which also has exactly one positive zero with the required sign switch.

**Independent dispersion threshold.** Integrating \(g_t\), define \(M(t)=16t^5+64t^4+120t^3+160t^2+119t+28\); the exact mean is \(\mathbb EY=M(t)/(tQ(t))\). The second moment is \(\mathbb EY^2=2A+2C/t^3+6E/t^4\), and simplification gives the global identity
\[
\operatorname{CV}^2(Y)-1=-\frac{8P_v(t)}{M(t)^2}.
\]
Each polynomial \(P_v,P_h\), in descending order, has exactly one coefficient sign change, negative value at zero and positive leading coefficient; hence each has exactly one positive root. As \(P_v(1)>0>P_h(1)\), these roots satisfy \(t_v<1<t_h\). Therefore the entire interval \(t_v<t<t_h\) has a bathtub spatial hazard and strictly subunit squared coefficient of variation.

## Verification
The accompanying self-contained \(\texttt{checker.py}\) uses exact symbolic identities (density normalization, Laplace self-consistency, reflecting boundary flux, first two stationary moments, hazard derivative and both defining polynomials). It verifies the removable resonance and one-sign-change positive-root certificates, numerically brackets each threshold, and independently compares stationary moments with simulated Poisson-alarm chains at four values of \(t\) (120000 steps per value, with 3000 burn-in). Simulation supplements the proof and is not used to certify global signs. Reproduce with \(\texttt{python checker.py}\); dependencies are Python, NumPy, SymPy and SciPy.

## Relationship to prior work
Palmowski and Vlasiou (2026), Section 3 on reflected Lévy resetting, develop the map \((B-X)^+\) under exponentially distributed \(B\), including explicit exponential-capacity transforms. The present two-stage Erlang-capacity model is different: it creates affine-exponential resetting densities and an exact separation between spatial-hazard and dispersion thresholds. Classical reflected-Lévy collapse literature analyzes multiplicative mechanisms, which do not imply the present finite-capacity two-stage classification. Elementary positive-root counting is used as a tool, not itself claimed as a new theorem.

## Limitations
The proof assumes a zero-drift reflecting Brownian process, rate-two Erlang capacity and independent Poisson review alarms; it does not claim analogous phase diagrams for arbitrary Lévy jumps, other Erlang orders, drifts, or finite-time transients. The hazard is a spatial tail hazard, not a temporal event hazard. The stated novelty is conditional on the inspected primary literature and indexed records; unindexed equivalent calculations may exist. Independent review has not been performed.

## References
1. Z. Palmowski and M. Vlasiou, *Steady-state of Lévy process with general resetting: unreflected and reflected cases*, arXiv:2611.14692v1 (first publicly available 2026-11-10), https://arxiv.org/abs/2611.14692.
2. O. Boxma, O. Kella, and D. Perry, *On reflected Lévy processes with collapse*, Journal of Applied Probability (2026), https://doi.org/10.1017/jpr.2026.10073.

# A unique horizon reversal for two unequal irrigation pulses under saturating moisture response

## Finding

In the idealized single-store setting below, an earlier large irrigation pulse is strictly better for an initially short cumulative-response horizon, but an earlier small pulse is strictly better for every sufficiently long horizon. The transition occurs **once and only once** for every strictly positive choice of the parameters. Its exact time is

\[
T_* = \frac{1}{k}\log\!\left(\frac{(K+A+B)(K+e^{-k\tau}(A+B))+AB(1-e^{-k\tau}+e^{-2k\tau})}{ABe^{-2k\tau}}\right)>\tau.
\]

For every \(A>B>0\), \(K,k,\tau>0\), and every \(T\ge\tau\), the cumulative score from the larger pulse first exceeds that from the smaller pulse first exactly when \(\tau\le T<T_*\); equality holds exactly at \(T=T_*\); and the smaller-pulse-first schedule wins exactly when \(T>T_*\). The post-second-pulse **instantaneous** response always favors the smaller-pulse-first schedule, so the cumulative reversal is not an instantaneous crossover.

## Assumptions and scope

Let \(A>B>0\) be two prescribed moisture increments applied at times \(0\) and \(\tau>0\), respectively, in either order. The moisture proxy \(M(t)\) starts at zero, has instantaneous upward jumps equal to pulse amounts, and obeys \(\dot M=-kM\) between jumps with \(k>0\). No hard storage ceiling, capillary redistribution, feedback from uptake, precipitation or further input is imposed. The observations end at \(T\ge\tau\). The monotone saturating performance score is \(f_K(m)=m/(K+m)\) for \(K>0\), and total performance is \(U(T)=\int_0^T f_K(M(t))\,dt\). This is a phenomenological response measure, **not** a physically calibrated root-uptake law or a sink term in the water balance.

For an ordering \((a,b)\), where \((a,b)=(A,B)\) or \((B,A)\), the complete trajectory is

\[
M_{a,b}(t)=\begin{cases}ae^{-kt},&0\le t<\tau,\\(ae^{-k\tau}+b)e^{-k(t-\tau)},&t\ge\tau.\end{cases}
\]

The strict claim needs unequal positive pulses, strictly positive gap, finite positive saturation parameter, and no prespecified finite upper horizon. Equal pulses or coincident applications produce identical trajectories; they are not part of the strict claim.

## Proof

Put \(y=e^{-k\tau}\in(0,1)\) and \(z=e^{-kT}\in(0,y]\). Since \(f_K(m)=1-K/(K+m)\), the elementary integral of a decaying moisture level is

\[
\int_0^s f_K(ce^{-kt})\,dt=\frac1k\log\!\left(\frac{K+c}{K+ce^{-ks}}\right),\qquad c\ge0.
\]

Splitting at the second pulse yields

\[
 kU_{a,b}(T)=\log R_{a,b}(z),\qquad
 R_{a,b}(z)=\frac{(K+a)(K+ay+b)}{(K+ay)\bigl(K+(ay+b)z/y\bigr)}.
\]

All factors are strictly positive. Hence the sign of \(U_{A,B}(T)-U_{B,A}(T)\) is the sign of \(R_{A,B}(z)-R_{B,A}(z)\). A direct common-denominator expansion and factorization gives

\[
R_{A,B}(z)-R_{B,A}(z)=
\frac{Ky(A-B)(1-y)\bigl(zD-ABy^2\bigr)}{(Ay+K)(By+K)(Az+Byz+Ky)(Ayz+Bz+Ky)},
\]

where

\[
D=(K+A+B)(K+y(A+B))+AB(1-y+y^2).
\]

Each factor outside the last parenthesis is positive. In particular, \(D>0\), and

\[
D-ABy=(K+A+B)(K+y(A+B))+AB(1-y)^2>0.
\]

Consequently the unique root \(z_*=ABy^2/D\) belongs strictly to \((0,y)\). Because \(z=e^{-kT}\) decreases strictly from \(y\) to \(0\) as \(T\) increases from \(\tau\) to infinity, there is exactly one root \(T_*=k^{-1}\log(D/(ABy^2))>\tau\). The positive-factor identity supplies every strict sign, proves uniqueness, and establishes the announced classification for **all** permitted real parameters. No finite enumeration is used for the universal conclusion.

Moreover, at \(t>\tau\),

\[
M_{A,B}(t)-M_{B,A}(t)=(A-B)(y-1)e^{-k(t-\tau)}<0.
\]

As \(f_K\) is strictly increasing, \(d(U_{A,B}-U_{B,A})/dt<0\) for every \(t>\tau\). This separately explains why a strictly monotone cumulative difference crosses its zero exactly once and why observing only the late instantaneous advantage cannot determine the sign of earlier cumulative performance.

## Verification

A fully reproducible standalone `verify.py` accompanies this statement. Its symbolic checks independently expand the rational difference, verify the factorization and the threshold inequality, and check an infinite-horizon numerator identity. The test also cross-checks the logarithmic score formulas against independent numerical quadrature for 768 parameter/order cases. These finite checks are diagnostics; the proof above is the reason the theorem applies to all positive parameters.

A rational demonstration uses \(A=2\), \(B=1\), \(K=k=1\), \(\tau=\log 2\), so \(y=1/2\), \(D=23/2\), \(z_*=1/23\) and **exactly** \(T_*=\log 23\). Writing \(R_{a,b}=e^{U_{a,b}}\) in this normalization, one obtains

\[
\begin{array}{c|ccc}
T & \log 2 & \log 23 & \log64\\\hline
R_{2,1} &3/2&23/6&72/17\\
R_{1,2} &4/3&23/6&896/207
\end{array}
\]

The order advantage is positive, zero and negative, respectively, with all entries exact rational numbers.

## Relationship to prior work

Berardi, Difonzo and Guglielmi study irrigation control through a spatial Richards-equation formulation with nonlinear hydraulic constitutive laws and Feddes-type root water uptake. Their analysis addresses a different, more realistic model and motivates asking which horizon effects persist in an analytically tractable benchmark; their results do **not** transfer automatically to the scalar model here. Lopes et al. study a linear hydrological balance and constrained irrigation-control optimization, without the two-pulse saturating-response comparison proved here. Established logarithmic integration of saturating responses is elementary; the claim is the complete and sharp all-parameter ordering/horizon classification rather than that integration identity itself. Published studies of storm reordering, irrigation scheduling and pulse-shaped inputs furnish related but distinct comparators; no exhaustive historical-priority search is claimed.

## Limitations

The model does not include physical soil-water saturation, hydraulic transport between depths, infiltration losses at dosing, evaporation feedback, actual plant transpiration, dose bounds beyond those stipulated, or state-dependent drainage. Its performance functional is an idealized indicator, not measured agricultural yield or a replacement for Feddes' uptake function. Discrete impulses and a freely extended observation horizon may be operationally unrealistic. The classification makes no assertion for other nonlinear response functions, interacting soil layers, or continuous controls. No independent external mathematical validation has been completed.

## References

1. M. Berardi, F. V. Difonzo and R. Guglielmi, *A preliminary model for optimal control of moisture content in unsaturated soils*, arXiv:2307.06217, initial public submission 2023-07-12. https://arxiv.org/abs/2307.06217 ; full HTML https://arxiv.org/html/2307.06217v1 .
2. S. O. Lopes, F. A. C. C. Fontes, R. M. S. Pereira, MdR de Pinho and A. M. Gonçalves, *Optimal Control Applied to an Irrigation Planning Problem*, Mathematical Problems in Engineering (2016), article 5076879. https://doi.org/10.1155/2016/5076879 .

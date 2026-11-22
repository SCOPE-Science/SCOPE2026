# Two reactive uptake measurements determine an exponentially mixed streambed

## Finding

**Theorem (exact two-rate identification and feasibility).** Fix known numbers \(0<k_1<k_2\), stream-to-interface transfer velocity \(k_m>0\), and sediment porosity \(\theta>0\). In a semi-infinite reactive bed let the unknown reference diffusivity \(D_0>0\) and mixing length \(\ell>0\) be shared by two equilibrium experiments that differ **only** in the known first-order reaction constants \(k_1,k_2\). Write \(v_j\) for the measured bulk-normalized nutrient uptake velocity in experiment \(j\).

A **unique** pair \((D_0,\ell)\) realizes the data if and only if \(0<v_1,v_2<k_m\) and

\[
\sqrt{\frac{k_2}{k_1}}<\frac{v_2/(1-v_2/k_m)}{v_1/(1-v_1/k_m)}<\frac{k_2}{k_1}.
\]

Both inequalities are strict and sharp. Neither endpoint is attained by positive finite parameters. In contrast, **one** uptake measurement admits a continuous one-parameter family of distinct positive \((D_0,\ell)\) pairs, even when its reaction constant, porosity and water-column transfer coefficient are known. Thus two appropriately perturbed measurements are necessary and sufficient within this design.

## Assumptions and scope

For each experiment, the normalized sediment concentration \(C_j:[0,\infty)\to[0,1]\) is the decaying classical solution of

\[
\bigl(D_0e^{-z/\ell}C_j'(z)\bigr)'-k_j C_j(z)=0\quad(z>0),\qquad C_j(0)=1,\qquad \lim_{z\to\infty}C_j(z)=0.
\]

The intrinsic sediment admittance is \(U_j=-D_0C_j'(0)>0\). The water-side and porous-bed resistances act in series, with measured uptake velocities

\[
v_j=\left(\frac1{k_m}+\frac1{\theta U_j}\right)^{-1}=\frac{k_m\theta U_j}{k_m+\theta U_j}.
\]

All six quantities \(k_1,k_2,k_m,\theta,v_1,v_2\) are treated as exact positive scalars, with the first four known in advance and the two observations determining the last two. The two experiments share the **same** \(D_0,\ell,k_m,\theta\). In particular, changing reaction kinetics must not alter effective diffusivity or the external mass-transfer coefficient. The bed extends to infinite depth and there is no advective bed flux, finite bottom boundary, heterogeneity outside the assumed exponential profile, or in-bed sorption beyond the modeled first-order loss.

## Proof

**1. Exact forward map.** Put \(x_j=2\ell\sqrt{k_j/D_0}\), and let \(K_\nu\) denote the modified Bessel function of the second kind. Direct substitution in the differential equation and the identities \(K_1'(x)=-K_0(x)-K_1(x)/x\) gives

\[
C_j(z)=e^{z/(2\ell)}\frac{K_1(x_je^{z/(2\ell)})}{K_1(x_j)},\qquad
U_j=\sqrt{D_0k_j}\,F(x_j),\qquad F(x)=\frac{K_0(x)}{K_1(x)}.
\]

The alternative independent Bessel solution grows super-exponentially and cannot satisfy the far-field condition. Since \(K_0,K_1>0\), this is the unique decaying solution. Define the corrected uptake \(T_j=k_mv_j/(k_m-v_j)=\theta U_j\), a strictly increasing transformation for \(0<v_j<k_m\).

**2. The essential Bessel-ratio lemma.** On \((0,\infty)\), the function \(F(x)=K_0(x)/K_1(x)\) lies strictly between zero and one. Indeed, the positive integral representation \(K_\nu(x)=\int_0^\infty e^{-x\cosh t}\cosh(\nu t)\,dt\) gives \(K_1(x)>K_0(x)>0\). Standard Bessel differentiation yields

\[
F'(x)=F(x)^2+\frac{F(x)}x-1.
\]

Set \(E(x)=xF'(x)/F(x)\). Direct differentiation, using the preceding Riccati equation, shows

\[
E'(x)=-\frac{H(x)}{F(x)^2},\qquad H(x)=x\bigl(1-F(x)^4\bigr)-2F(x)^3.
\]

We prove \(H(x)>0\) on \((0,\infty)\) without assuming the desired monotonicity. The small-argument asymptotics \(K_0(x)=\log(2/x)-\gamma+o(1)\) and \(K_1(x)=x^{-1}+O(x\log(1/x))\) imply \(H(x)=x+o(x)>0\) near zero. The large-argument expansion \(F(x)=1-(2x)^{-1}+3(8x^2)^{-1}-3(8x^3)^{-1}+O(x^{-4})\) implies \(H(x)=(2x^2)^{-1}+O(x^{-3})>0\) for large \(x\). At **any** hypothetical positive zero \(H(x_0)=0\), substitute \(x_0=2F(x_0)^3/(1-F(x_0)^4)\) into the derivative of \(H\). It gives

\[
H'(x_0)=-\frac{2\bigl(1-F(x_0)^2\bigr)^2}{1+F(x_0)^2}<0.
\]

Every zero would therefore cross from positive to negative. A continuously differentiable function positive near both endpoints cannot have any zero if all its zeros are strictly downward crossings: to return to a positive value, it would need a zero that does not cross downward. Thus \(H>0\), so **the logarithmic elasticity \(E\) is strictly decreasing**.

**3. The admissible interval.** Put \(r=\sqrt{k_2/k_1}>1\), \(x=x_1\), so \(x_2=rx\). Dividing the corrected measurements removes the scale parameter:

\[
R(x)=\frac{T_2}{T_1}=r\frac{F(rx)}{F(x)}.
\]

The elasticity lemma gives

\[
\frac{R'(x)}{R(x)}=\frac{E(rx)-E(x)}x<0.
\]

As \(x\downarrow0\), \(F(x)\sim x\log(1/x)\) and \(R(x)\to r^2\). As \(x\to\infty\), \(F(x)\to1\) and \(R(x)\to r\). Therefore \(R\) is a continuous, strictly decreasing bijection of \((0,\infty)\) onto \((r,r^2)\). This proves necessity, sufficiency and strictness of the displayed measured-data inequalities.

**4. Explicit inversion.** Given compatible data, solve the unique scalar equation

\[
r\frac{F(rx)}{F(x)}=\frac{T_2}{T_1}
\]

for \(x>0\); monotone bisection suffices. Then the **only** positive parameters are

\[
D_0=\left(\frac{T_1}{\theta\sqrt{k_1}F(x)}\right)^2,
\qquad \ell=\frac{x\sqrt{D_0}}{2\sqrt{k_1}}.
\]

Substitution in the exact forward map verifies both measurements, proving existence as well as uniqueness.

**5. Minimality.** Given just one admissible uptake \(v_1\), fix an arbitrary \(x>0\), take the just-displayed formulas with \(T_1=k_mv_1/(k_m-v_1)\), and obtain a positive pair producing that same uptake. Distinct \(x\) yield distinct parameter pairs because \(x=2\ell\sqrt{k_1/D_0}\). Therefore one scalar uptake never identifies both parameters.

## Verification

The standalone `verify.py` independently implements the exact forward formula using scaled Bessel functions, transforms the water-side resistance, reconstructs parameters by bracketed monotone root-finding, checks the strict feasibility region and tests the sign of the proof's \(H\) function. With a deterministic seed, it passed **18,012 supplementary assertions**, including 2,000 randomized positive-parameter inversions, several logarithmic grids, and an explicit fixed example. These finite tests are not used to establish the infinite-domain monotonicity or minimality proofs above.

For an illustrative exactly specified input \(D_0=1,\ell=1/2,k_1=1,k_2=4,\theta=1,k_m=3\), the forward conductances are \(U_1\approx0.699483935594\), \(U_2\approx1.62861551753\) and uptake velocities \(v_1\approx0.567228252187\), \(v_2\approx1.05557407697\). The inverse equations recover \(D_0=1\) and \(\ell=1/2\). Numerical outputs are supplementary checks, not a certificate of global identification.

## Relationship to prior work

Monofy et al. (2024, open full text, Section 2.1, Equations 3–6) establish the exponentially attenuated streambed diffusivity and the forward reactive-flux Bessel formula used here, including two series resistances and porosity. Their Section 4.2.2 estimates **reaction constants**, taking diffusivity and mixing length from independent regressions; it does not state the exact two-known-reaction-rate inverse, its global uniqueness, the feasible uptake-ratio interval or one-measurement minimality. The distinct inverse question is the present contribution, not the forward Bessel formula.

Bottacin-Busolin (2019) studies exponential depth attenuation, conservative tracer breakthrough curves and an equifinality result with unknown reach geometry. This neither proves nor negates the two-reaction, fixed-external-transfer, steady surface-uptake inverse. Segura (2021) studies general Bessel-ratio Riccati monotonicity and bounds; the Bessel identities and their theory are prior mathematics. Kaltenbacher and Rundell (2021) establish recovery of conductivity and nonlinear reaction terms under richer *time-dependent* data, not the two-scalar steady surface-flux design or its sharp feasible range. A statement-equivalence comparison with accessible published mathematical research records found no directly covering statement; this is not a proof of historical priority.

## Limitations

The result requires exact distinct and independently known reaction rates, constant \(k_m\) and \(\theta\), and a shared positive exponential sediment diffusivity profile. If external transfer or porosity is unknown, or the intervention changes sediment mixing, two scalar measurements need not identify both parameters. Near either endpoint of the strict feasible ratio interval the inversion can be ill-conditioned, and the endpoints themselves correspond only to singular parameter limits. Finite noisy sampling, model misspecification, and experimental feasibility are not treated. This is a conditional analytic benchmark and makes no claim that real streams meet the assumptions. Its historical originality remains subject to independently checking older equivalent inverse boundary-response results.

## References

1. Monofy, A., Grant, S. B., Boano, F., et al., *Toward a Universal Model of Hyporheic Exchange and Nutrient Cycling in Streams*. First-public preprint 2024-07-11, DOI: https://doi.org/10.22541/essoar.172073028.80888968/v1 ; open full article *AGU Advances* 5 (2024), https://doi.org/10.1029/2024AV001373 . Preprint date corroborated by https://orcid.org/0000-0001-9641-327X .
2. Bottacin-Busolin, A., *Modeling the Effect of Hyporheic Mixing on Stream Solute Transport*, *Water Resources Research* 55 (2019), https://doi.org/10.1029/2019WR025697 .
3. Segura, J., *Monotonicity Properties for Ratios and Products of Modified Bessel Functions and Sharp Trigonometric Bounds*, *Results in Mathematics* 76 (2021), https://doi.org/10.1007/s00025-021-01531-1 .
4. Kaltenbacher, B., and Rundell, W., *On the simultaneous recovery of the conductivity and the nonlinear reaction term in a parabolic equation* (2021), https://arxiv.org/abs/2101.06656 .

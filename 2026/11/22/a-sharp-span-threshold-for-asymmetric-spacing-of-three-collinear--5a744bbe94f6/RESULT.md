# A sharp span threshold for asymmetric spacing of three collinear wind turbines

## Finding

A fixed-length row of three turbines has a sharp, unique change of its power-maximizing layout under a simple inverse-square wake-recovery law and **linear** superposition of upstream velocity deficits. Below the critical total span, the second turbine should be placed as far downstream as the minimum-separation constraint permits. Above it, the second turbine has a unique interior optimal position, strictly *downstream of the geometric midpoint*. In the long-row limit the displacement from the midpoint is asymptotically \(\delta/(6\kappa^2 L)\).

Precisely, fix a wake amplitude \(0<\delta<3/10\), a recovery coefficient \(\kappa>0\), and a minimum pairwise successive spacing \(\ell\ge0\). Let the turbine locations along the prevailing wind direction be \(0,x,L\), where \(L>2\ell\) and \(\ell\le x\le L-\ell\). Define

\[
h(t)=(1+\kappa t)^{-2},\qquad
u_1=1,\quad
u_2=1-\delta h(x),\quad
u_3=1-\delta h(L)-\delta h(L-x),
\]

and normalized total power

\[
P_L(x)=u_1^3+u_2^3+u_3^3.
\]

There exists exactly one critical span \(L_c=L_c(\delta,\kappa,\ell)>2\ell\), characterized by

\[
\frac{1-\delta h(L_c-\ell)}{(1+\kappa(L_c-\ell))^{3/2}}
=
\frac{1-\delta h(L_c)-\delta h(\ell)}{(1+\kappa\ell)^{3/2}}.
\]

For \(2\ell<L\le L_c\), the **unique** global maximizer is \(x=L-\ell\). For \(L>L_c\), the **unique** global maximizer is a point \(x_L\in(L/2,L-\ell)\) solving

\[
\frac{1-\delta h(x_L)}{(1+\kappa x_L)^{3/2}}
=
\frac{1-\delta h(L)-\delta h(L-x_L)}{(1+\kappa(L-x_L))^{3/2}}.
\]

In particular, equally dividing the span into two gaps is **never optimal** for a finite \(L>2\ell\). For fixed \(\delta,\kappa,\ell\), the long-span asymptotic is

\[
x_L=\frac L2+\frac{\delta}{6\kappa^2 L}+o(L^{-1})\quad(L\to\infty).
\]

The result applies to the stated idealized wake model only, not to arbitrary wake-merging prescriptions.

## Assumptions and scope

The model assumes three identical aligned turbines with a single prevailing wind direction, unchanged thrust-related wake amplitude \(\delta\), a top-hat fully overlapping wake, no terrain or directional variability, and operation in a below-rated regime in which power is proportional to the cube of inflow speed. The velocity deficit of a turbine at distance \(t\) is \(\delta h(t)\) **relative to the freestream**, with deficits from every upstream turbine added linearly. The decay \(h(t)=(1+\kappa t)^{-2}\) is the one-dimensional centerline form commonly associated with Jensen/Park-type wake expansion. The two endpoints are fixed; the middle location is movable subject to minimum gap \(\ell\). The admissible case \(\ell=0\) is a mathematical limiting case; practical turbines require a positive minimum distance.

Because \(u_3\ge 1-2\delta>0\), the cubic-power objective is well-defined and positive on the entire closed feasible interval. There is no cost term, power-curve cut-out, wake-induced turbulence constraint, or claim of empirical calibration. The restriction \(\delta<3/10\) is a *sufficient* parameter range for the uniqueness theorem; its optimality is not claimed.

## Proof

Write \(t=L-x\), and introduce two nonnegative derivative terms

\[
A(x)=\frac{2\kappa[1-\delta h(x)]^2}{(1+\kappa x)^3},\qquad
B_L(x)=\frac{2\kappa[1-\delta h(L)-\delta h(L-x)]^2}{(1+\kappa(L-x))^3}.
\]

Direct differentiation, with \(h'(t)=-2\kappa(1+\kappa t)^{-3}\), gives the **exact identity**

\[
P_L'(x)=3\delta[A(x)-B_L(x)].
\]

Next, differentiating these two terms again gives

\[
A'(x)=\frac{2\kappa^2[1-\delta h(x)]}{(1+\kappa x)^4}
\big[-3+7\delta h(x)\big]<0,
\]

because \(\delta<3/10<3/7\), and

\[
B_L'(x)=\frac{2\kappa^2[1-\delta h(L)-\delta h(t)]}{(1+\kappa t)^4}
\big[3-3\delta h(L)-7\delta h(t)\big]>0.
\]

Indeed the last bracket is strictly larger than \(3-10\delta>0\). All other factors are positive. Therefore \(A(x)-B_L(x)\) is strictly decreasing on the entire feasible interval; hence \(P_L'\) has at most one zero, and every interior zero is a strict global maximum.

At the midpoint \(x=L/2\), the denominator and the distance-decay factors in \(A\) and \(B_L\) coincide, but the positive speed factor in \(A\) exceeds the one in \(B_L\) by \(\delta h(L)>0\). Thus

\[
P_L'(L/2)>0.
\]

It follows that the objective is strictly increasing throughout the feasible interval up to \(L/2\). In particular, neither the left endpoint nor the midpoint can maximize the objective.

At the right endpoint the derivative is controlled by

\[
E(L)=A(L-\ell)-B_L(L-\ell).
\]

As \(L\) varies over \((2\ell,\infty)\), the first term is strictly decreasing, since \(A\) is strictly decreasing and its argument \(L-\ell\) increases. The second term is strictly increasing, since it equals

\[
\frac{2\kappa}{(1+\kappa\ell)^3}
\big[1-\delta h(L)-\delta h(\ell)\big]^2,
\]

whose positive speed factor increases with \(L\). Consequently \(E\) is continuous and strictly decreasing. At \(L=2\ell\), the limiting two terms have the same denominator but the first speed factor is larger by \(\delta h(2\ell)\), so \(E(2\ell)>0\). As \(L\to\infty\), the first term tends to zero and the second tends to a strictly positive constant, so \(E(L)<0\) for all sufficiently large \(L\). The intermediate-value theorem and strict monotonicity give one and only one \(L_c>2\ell\) with \(E(L_c)=0\).

Both speeds in the endpoint condition are positive, so equality of the two squared quantities is equivalent to the displayed square-root equation for \(L_c\). If \(L\le L_c\), then \(P_L'(L-\ell)\ge0\); strict decrease of \(P_L'\) shows the derivative is positive at every smaller admissible point. Thus the unique maximizer is the right endpoint. If \(L>L_c\), then \(P_L'(L/2)>0\) and \(P_L'(L-\ell)<0\). Strict decrease gives exactly one zero in \((L/2,L-\ell)\), the unique global maximizer \(x_L\). The displayed interior equation follows by taking positive square roots of \(A=B_L\).

For the asymptotic, fix \(\delta,\kappa,\ell\) and let \(L\to\infty\). The maximizer is interior for all sufficiently large \(L\). Set \(r=1+\kappa L/2\), \(\varepsilon_L=x_L-L/2>0\), \(r_+=r+\kappa\varepsilon_L\), and \(r_-=r-\kappa\varepsilon_L\). At the critical point,

\[
3\log\frac{r_+}{r_-}
=2\log\frac{1-\delta r_+^{-2}}{1-\delta(1+\kappa L)^{-2}-\delta r_-^{-2}}.
\]

The two positive speed factors are bounded below by \(1-2\delta\), so this identity bounds \(r_+/r_-\) independently of \(L\); since \(x_L>L/2\), both \(x_L\) and \(L-x_L\) tend to infinity. The two factors tend to one, implying \(r_+/r_-\to1\) and hence \(\varepsilon_L=o(L)\). The difference of the two factors is \(\delta(1+\kappa L)^{-2}+O(\varepsilon_L L^{-3})\). Expanding the logarithms in the identity, first using \(\varepsilon_L=o(L)\), yields \(\varepsilon_L=O(L^{-1})\). Substitution back into the logarithmic identity gives

\[
\frac{6\kappa\varepsilon_L}{r}
=\frac{2\delta}{(1+\kappa L)^2}+o(L^{-2}),
\]

and therefore \(\varepsilon_L=\delta/(6\kappa^2L)+o(L^{-1})\). This proves all assertions.

## Verification

The analytical proof above is valid for every real parameter in the specified domain and is not a finite enumeration. The included standalone file `verification/wake_layout_check.py` uses Python standard-library rational arithmetic and seeded floating-point tests as supplementary diagnostics. Running `python3 verification/wake_layout_check.py` from the package root reports **19,724 passed assertions** in the recorded run, including exact-rational monotonicity probes, finite-difference sign comparisons, uniqueness/endpoint tests, direct sampled-objective comparisons, and long-span checks. Reproducibility requires Python 3 only.

For the dimensionless instance \(\delta=1/5\), \(\kappa=1\), and \(\ell=1/2\), bisection gives \(L_c\approx1.0617970425831\). At \(L=3\), the unique optimum is \(x_L\approx1.5113339039885\), rather than \(1.5\); the gain in normalized total power over equal spacing is approximately \(1.0464271885\times10^{-5}\). This small gain is intentionally **not** represented as a practically significant wind-farm yield increase.

## Relationship to prior work

Stevens, Gayme, and Meneveau (2015; first online 2 March 2015) analyze LES-based spanwise and streamwise spacing effects in *extended* aligned and staggered farms. They use regular array spacings, not the one-free-middle-turbine, fixed-total-span, weak-deficit layout problem here. Peña, Réthoré, and van der Laan (2015; first online 7 May 2015) analyze Jensen wake prediction and observations, using **quadratic** rather than the **linear** sum of deficits. Stevens et al. (2016; first online 4 August 2016) optimize spacing and costs for very large wind farms, again not this finite three-turbine threshold.

Ma, Archer, and Vasel-Be-Hagh (2022) explicitly state the standard linear sum of velocity deficits (their method M1), but evaluate wake parameterizations rather than proving the above fixed-span optimization. Historical wind-farm layout literature, including Grady, Hussaini, and Abdullah (2005), already treats numerical global placement optimization; that general problem is not claimed to be new. The specific analytical phase boundary and strict asymmetry for the fully stated simple model have not been identified in the inspected material. This is a *qualified prior-work comparison*, not proof of priority.

## Limitations

This result concerns a reduced mathematical model, not a field-calibrated design rule. In particular, linear wake-deficit superposition can underpredict velocities in multiple-wake arrays; some wake models use root-sum-square deficits, inflow-normalized deficits, dynamic atmospheric replenishment, or non-top-hat profiles. Those models may have different optima. Fixed positive \(\ell\) is important for physical layouts, and the theorem ignores cabling, turbulence loads, bidirectional winds, local power control, and terrain. The strict condition \(\delta<3/10\) is sufficient but not proven sharp. The small observed numerical power gain must not be extrapolated to real installations. Historical publication priority remains uncertain because not all earlier layout papers were read in full. No independent scientific audit has been performed.

## References

1. Stevens, R. J. A. M., Gayme, D. F., and Meneveau, C. (2015 online). *Effects of turbine spacing on the power output of extended wind-farms*. Wind Energy 19 (2016), 359–370. First published 2 March 2015. https://doi.org/10.1002/we.1835
2. Peña, A., Réthoré, P.-E., and van der Laan, M. P. (2015 online). *On the application of the Jensen wake model using a turbulence-dependent wake decay coefficient: the Sexbierum case*. Wind Energy 19 (2016), 763–776. First published 7 May 2015. https://doi.org/10.1002/we.1863
3. Stevens, R. J. A. M., Hobbs, B. F., Ramos, A., and Meneveau, C. (2016 online). *Combining economic and fluid dynamic models to determine the optimal spacing in very large wind farms*. Wind Energy 20 (2017), 465–477. First published 4 August 2016. https://doi.org/10.1002/we.2016
4. Ma, Y., Archer, C. L., and Vasel-Be-Hagh, A. (2022). *The Jensen wind farm parameterization*. Wind Energy Science 7, 2407–2431. https://doi.org/10.5194/wes-7-2407-2022
5. Grady, S. A., Hussaini, M. Y., and Abdullah, M. M. (2005). *Placement of wind turbines using genetic algorithms*. Renewable Energy 30, 259–270. https://doi.org/10.1016/j.renene.2004.05.007

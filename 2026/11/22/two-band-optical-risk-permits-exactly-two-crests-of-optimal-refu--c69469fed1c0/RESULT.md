# Two-band optical risk permits exactly two crests of optimal refuge depth

## Finding

A strictly convex ecological depth-choice objective can have a uniquely selected refuge depth at **every** fixed water-attenuation coefficient, while that selected depth has **two distinct strict local maxima** as attenuation increases. For nonnegative dimensionless depth \(z\) and relative attenuation \(k>0\), consider

\[
J_k(z)=e^z+e^{-kz}+e^{-20kz},\qquad z\ge 0.
\]

Write \(z_*(k)\) for its global minimizer. Then \(z_*(k)=0\) for \(0<k\le1/21\). On \(k>1/21\), the minimizer is positive, smooth and unique. It increases, decreases, increases, and finally decreases as \(k\) passes through precisely three positive critical values \(k_1<k_2<k_3\), approximately

\[
(k_1,k_2,k_3)=(0.1851505200285,\ 1.2893711244255,\ 3.5911135158906).
\]

The critical optimal depths are approximately \((0.3076289050983,\ 0.1889471869879,\ 0.2784645671687)\). The first and third critical points are strict local maxima, and the second is a strict local minimum. The optimal depth tends to zero as \(k\to\infty\). In the same class of models with only one exponential optical-risk band, the optimal depth has **exactly one** positive local maximum, for every positive band strength and attenuation multiplier. Thus two bands are the smallest number permitting two crests of the optimal-depth response within this family.

## Assumptions and scope

Depth \(z\ge0\) is dimensionless, increasing downwards. The term \(e^z\) is an increasing opportunity or physiological cost of descending. The terms \(e^{-kz}\) and \(e^{-20kz}\) are two nonnegative optical-risk contributions attenuating at distinct rates as depth increases. The parameter \(k>0\) scales both attenuation rates proportionally, with their ratio held fixed at \(20\); the risk amplitudes are one. All terms have been normalized to a common cost unit. No finite bottom depth, movement cost, wavelength-dependent predator-response law or population dynamics is assumed. The model is deliberately stylized and not calibrated to a particular species or water body.

For the one-band comparison, allow arbitrary fixed \(a,b>0\) and minimize \(e^z+a e^{-bkz}\) over \(z\ge0\), varying the common attenuation coefficient \(k>0\). The one-band comparison asserts a universal one-crest limit; the two-band result asserts existence and an exact critical-point count for the specified two-band parameters, **not** a classification of every two-band mixture.

## Proof

**1. Unique depth for each attenuation.** Direct differentiation gives

\[
\partial_z J_k=e^z-k e^{-kz}-20k e^{-20kz},\qquad
\partial_{zz}J_k=e^z+k^2e^{-kz}+400k^2e^{-20kz}>0.
\]

Because \(\partial_zJ_k(0)=1-21k\), strict convexity gives the unique minimum \(z_*(k)=0\) for \(k\le1/21\). For \(k>1/21\), the derivative starts negative, tends to infinity with depth, and is strictly increasing, so its unique root is the unique strictly positive global minimizer. The implicit-function theorem makes \(z_*(k)\) smooth for all \(k>1/21\).

**2. A global increasing coordinate.** Set \(y=kz_*(k)\) and \(G(y)=e^{-y}+20e^{-20y}>0\). The first-order condition becomes

\[
e^{y/k}=kG(y),\qquad H(k,y)=\log k+\log G(y)-y/k=0.
\]

The partial derivatives satisfy

\[
\partial_kH=1/k+y/k^2>0,\qquad
\partial_yH=G'(y)/G(y)-1/k<0.
\]

Consequently \(y'(k)=-\partial_kH/\partial_yH>0\) throughout \(k>1/21\). At its left endpoint, continuity of the strictly convex minimizer gives \(y\to0\). As \(k\to\infty\), \(y\) must diverge: otherwise \(e^{y/k}\to1\) while \(kG(y)\to\infty\). Therefore \(k\mapsto y(k)\) is a strictly increasing bijection from \((1/21,\infty)\) onto \((0,\infty)\).

**3. Exact sign reduction and root count.** Differentiating the stationarity equation with respect to \(k\) and using its strictly positive depth derivative gives

\[
\operatorname{sgn}(z_*'(k))=-\operatorname{sgn}\left(e^{-y}(y-1)+20e^{-20y}(20y-1)\right)
=-\operatorname{sgn}f(y),
\]

where

\[
f(y)=(y-1)e^{19y}+20(20y-1).
\]

The four certified sign witnesses are

\[
f(0)=-21<0,\qquad
f(1/10)=20-\tfrac9{10}e^{19/10}>0,\qquad
f(1/2)=180-\tfrac12e^{19/2}<0,\qquad
f(1)=380>0.
\]

For example, \(e^{19/10}<e^2<8\) establishes the second sign, and the first five nonnegative Taylor terms of \(e^{19/2}\) already exceed \(360\), establishing the third. Furthermore,

\[
f''(y)=(361y-323)e^{19y}
\]

has precisely one positive zero. If \(f\) had four distinct positive zeros, Rolle's theorem would force at least two distinct positive zeros of \(f''\), a contradiction. Thus the three disjoint sign-changing intervals \((0,1/10)\), \((1/10,1/2)\), and \((1/2,1)\) each contain exactly one root, and there are no others. Each root is simple: a multiple odd-order root would give an additional zero of \(f'\), beyond the two already forced by Rolle between the three roots; and a tangential even-order root cannot change sign. The sign pattern of \(f\) is therefore \(-,+,-,+\) in the four successive regions. As \(y(k)\) increases through all positive values, the derivative of \(z_*(k)\) has signs \(+,-,+,-\), proving exactly the stated two maxima and intervening minimum.

**4. Large-attenuation limit.** At the interior optimum, \(e^{z_*}=k(e^{-kz_*}+20e^{-20kz_*})\le21k e^{-kz_*}\). Hence

\[
0<z_*(k)\le\frac{\log(21k)}{1+k}\longrightarrow0
\]

as \(k\to\infty\). The three critical values are uniquely defined without numerical approximations: take the three roots \(y_i\) of \(f\) in the isolating intervals above, and let \(k_i\) be the unique positive solution of \(e^{y_i/k_i}=k_iG(y_i)\).

**5. One-band impossibility.** For \(J^{(1)}_k(z)=e^z+a e^{-bkz}\), its unique minimizer is

\[
z_*^{(1)}(k)=\begin{cases}0,&abk\le1,\\[2pt]\dfrac{\log(abk)}{1+bk},&abk>1.\end{cases}
\]

Writing \(t=bk\), the sign of its derivative in the interior is the sign of \(h(t)=1+t^{-1}-\log(at)\). But \(h'(t)=-t^{-2}-t^{-1}<0\), \(h(1/a)=1+a>0\), and \(h(t)\to-\infty\). Therefore \(h\) has exactly one zero and the one-band optimal depth has precisely one positive strict local maximum. This proves the asserted minimality of two bands for a two-crest effect.

## Verification

The standalone, standard-library-only script `verify_two_band.py` evaluates the three bracketed roots, converts them to the corresponding attenuation and optimal-depth values, verifies first-order and curvature formulas, and checks numerical derivatives at randomly selected attenuation coefficients. Its deterministic seed gives a reproducible supplementary check. In the reviewed execution it passed **32,145 assertions**. These finite tests do not establish the global root count or asymptotic statements; those follow from the analytic arguments above.

## Relationship to prior work

Matthews and Ohman (2023) find that light attenuation helps explain shifts in zooplankton vertical habitat use; their study compares environments and functional traits, rather than proving extrema counts for the stated two-component analytical loss. Barth, Johnson and Stone (2023) investigate morphology and transparency effects on diel vertical migration but do not present this spectral-mixture response classification. Ohman and Romagnan (2015) report that clearer water is associated with greater migration depth in observed copepods; that empirical association is not contradicted, because the present normalized model makes no calibration claim. Aksnes and Giske (1990) analyze the predation/feeding trade-off in habitat profitability without the specific two-band optical objective or its derivative-based three-reversal result. A prior mathematical result concerning a depth-averaged, photoinhibited phytoplankton model optimizes attenuation rather than an individual animal's optimal depth, so it does not imply the claim by specialization.

## Limitations

This is a structural possibility result for a narrowly specified objective, not evidence that two-crest migrations are present in nature. The attenuation ratio \(20\) and equal risk amplitudes are an illustrative construction. The local maxima are extrema of the **selected depth as attenuation varies**: the objective itself is strictly convex in depth and has no competing local depth minima. Different physiology, food profiles, explicit hypoxia ceilings, motion costs, finite water-column depth, predation saturation or independently varying optical bands may alter the response. The literature comparison does not establish exhaustive historical priority; specifically, other analytical visual-predation models may be relevant.

## References

- Matthews, S. A. and Ohman, M. D. (2023). *A space-for-time framework for forecasting the effects of ocean stratification on zooplankton vertical habitat use and trait composition*. *Limnology and Oceanography*. First public date: 2023-11-03. https://doi.org/10.1002/lno.12450
- Barth, A., Johnson, R., and Stone, J. (2023). *Size and transparency influence diel vertical migration patterns in copepods*. *Limnology and Oceanography*. First published 2023-11-21. https://doi.org/10.1002/lno.12461
- Ohman, M. D. and Romagnan, J.-B. (2015). *Nonlinear effects of body size and optical attenuation on Diel Vertical Migration by zooplankton*. *Limnology and Oceanography*. First published 2015-12-29. https://doi.org/10.1002/lno.10251
- Aksnes, D. L. and Giske, J. (1990). *Habitat profitability in pelagic environments*. *Marine Ecology Progress Series*, 64, 209–215. https://doi.org/10.3354/meps064209
- Aksnes, D. L. and Giske, J. (1993). *A theoretical model of aquatic visual feeding*. *Ecological Modelling*. https://doi.org/10.1016/0304-3800(93)90007-F (abstract inspected; detailed priority remains a residual uncertainty)

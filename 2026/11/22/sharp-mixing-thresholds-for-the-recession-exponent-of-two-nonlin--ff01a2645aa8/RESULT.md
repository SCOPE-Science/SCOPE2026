# Sharp mixing thresholds for the recession exponent of two nonlinear groundwater stores

## Finding

Let two noninteracting stores empty after recharge ends, with outlet discharges
\[
Q(t)=\frac{A}{(t+a)^p}+\frac{B}{(t+b)^p},\qquad t\geq0,\quad p>1,\quad A,B>0,\quad 0<a<b.
\]
Define the *instantaneous recession-slope exponent* (the local log-log slope of the recession rate versus discharge) by
\[
\beta(t)=\frac{d\log(-Q'(t))}{d\log Q(t)}=\frac{Q(t)Q''(t)}{Q'(t)^2}.
\]
Set \(r_0=a/b\), and let \(r_*\) denote the unique root in \((0,p/(p+2))\) of
\[
A\bigl[p-(p+2)r\bigr]=B r^{p+1}\bigl[p+2-pr\bigr]. \tag{1}
\]
Then the following complete classification holds.

1. The apparent exponent satisfies \(\beta(t)>(p+1)/p\) at every finite \(t\geq0\), and tends to \((p+1)/p\) as \(t\to\infty\). Each isolated store has the *constant* exponent \((p+1)/p\).
2. If \(r_0<r_*\), the exponent increases strictly up to its **unique** positive-time maximum at \(t_*=(br_*-a)/(1-r_*)\), then decreases strictly. If \(r_0\geq r_*\), it decreases strictly for all positive times (with an endpoint horizontal tangent when equality holds). In particular a positive-time maximum exists exactly when
\[
\frac ab<\frac p{p+2}\quad\text{and}\quad
\frac AB>\frac{(a/b)^{p+1}\bigl[p+2-p(a/b)\bigr]}{p-(p+2)(a/b)}. \tag{2}
\]
The offset contrast \(b/a>(p+2)/p\) is **sharp for the possibility** of a positive-time maximum over positive amplitudes \(A,B\).
3. For the hydrologically common square-law case \(p=2\), there exist positive amplitudes and a positive observation time with \(\beta(t)>2\) **if and only if** \(b/a>3\). Thus two stores, each having exact exponent \(3/2\), can together display an apparent exponent greater than two, but not without this sharp offset contrast.

For \(p=2\), \((a,b,A,B)=(1,4,5,27)\) gives \(r_*=1/3\), \(t_*=1/2\), and \(\beta(t_*)=16/9\). Separately, \((a,b,A,B)=(1,4,27,1000)\) gives \(\beta(2/7)=169/80>2\).

## Assumptions and scope

Time and offsets use one consistent time unit, while amplitudes include the required discharge dimensions. The two reservoirs have independent outflows and no input, evapotranspiration or exchange for \(t\geq0\). For \(p>1\), each reservoir has finite positive storage
\[
S_i(t)=\int_t^\infty Q_i(u)\,du=\frac{A_i}{p-1}(t+a_i)^{1-p},
\]
and consequently the nonlinear storage–discharge law
\[
S_i=\frac{A_i^{1/p}}{p-1}\,Q_i^{(p-1)/p},\qquad -S_i'=Q_i.
\]
Thus the model is mass-conserving during its rainless recession. The quantity \(\beta(t)\) is a *pointwise differential diagnostic*, not a regression slope over a finite data window. Positive \(A,B\) and distinct positive offsets are essential for the strict statements.

## Proof

Put \(u=(t+a)^{-1}\), \(v=(t+b)^{-1}\), and \(r=v/u=(t+a)/(t+b)\). Then \(r\) increases strictly from \(r_0\) to one. Direct differentiation gives
\[
Q'=-p(Au^{p+1}+Bv^{p+1}),\qquad
Q''=p(p+1)(Au^{p+2}+Bv^{p+2}).
\]
The cross-term identity
\[
(Au^p+Bv^p)(Au^{p+2}+Bv^{p+2})-(Au^{p+1}+Bv^{p+1})^2
=ABu^pv^p(u-v)^2
\]
therefore proves the exact formula
\[
\beta(t)=\frac{p+1}{p}\left[1+\frac{ABr^p(1-r)^2}{(A+Br^{p+1})^2}\right]. \tag{3}
\]
This gives both strict inequality and late-time limit. The sign of the derivative of its nonconstant term with respect to \(r\) is the sign of
\[
H(r)=A\bigl[p-(p+2)r\bigr]-Br^{p+1}\bigl[p+2-pr\bigr], \tag{4}
\]
because the omitted factors are strictly positive on \((0,1)\). On \((0,p/(p+2))\), the first summand decreases strictly from \(Ap\) to zero while \(r^{p+1}(p+2-pr)\) increases strictly: its derivative is \((p+2)r^p[(p+1)-pr]>0\). Above \(p/(p+2)\), both terms in \(H\) are negative (the first is nonpositive). Thus \(H\) has exactly one root \(r_*\in(0,p/(p+2))\), with positive sign before and negative sign after. Since \(r(t)\) is increasing, the monotonicity and formula for \(t_*\) follow. Evaluating \(H\) at \(r_0\) yields (2). As \(A/B\to\infty\), the root \(r_*\) approaches \(p/(p+2)\) from below, giving sharpness of the contrast condition.

For the superquadratic statement, write \(x=Br^{p+1}/A\). At a fixed \(r\), equation (3) becomes
\[
\beta=\frac{p+1}{p}\left[1+\frac{x}{(1+x)^2}\frac{(1-r)^2}{r}\right]
\leq\frac{p+1}{p}\left[1+\frac{(1-r)^2}{4r}\right], \tag{5}
\]
with equality precisely when \(x=1\). For \(p=2\), the right-hand side is greater than two exactly when \(r<1/3\), because \(3(1-r)^2>4r\) is equivalent, for \(0<r<1\), to \(r<1/3\). Since \(r(t)\) increases from \(a/b\), a positive time with \(r<1/3\) exists precisely when \(b/a>3\); in that case, choose any \(r\in(a/b,1/3)\) and amplitudes such that \(Br^3=A\). This proves both directions, including the boundary. Finally, in the first example (1) holds at \(r=1/3\) because \(5(2-4/3)=27(1/27)(4-2/3)\); substitution in (3) gives \(16/9\). In the second, (5) is attained at \(r=3/10\), realized by \(t=2/7\), giving \(169/80\).

## Verification

The standalone standard-library `checker.py` uses exact rational arithmetic for integer exponents \(p\in\{2,3,4,5\}\), positive rational offsets and amplitudes, comparing equation (3) to direct derivatives and checking the derivative sign against equation (4). It also checks both claimed rational examples and the \(p=2\) envelope. Run `python checker.py`; the expected output is `PASS 14412 exact assertions`. The checks are supplementary finite diagnostics; the proof above covers every real \(p>1\) and every permitted positive parameter tuple.

## Relationship to prior work

Wittenberg (1999) develops nonlinear storage–discharge models, including the square-root storage law. Kirchner (2009) and Harman, Sivapalan and Kumar (2009) analyze recession-slope exponents and the effect of heterogeneity, with the latter treating ensembles of *linear* reservoirs. McMillan and coauthors (2011) recommend multiple nonlinear reservoirs as one way to represent sharply curved recession behavior, while Gao and coauthors (2017) analyze *two parallel linear* reservoirs. Jachens and coauthors (2020) *already explicitly superimpose nonlinear power-law recession events and show variable, sometimes large fitted recession slopes*. That qualitative mixing phenomenon is known and is not claimed here; their work does not identify the necessary-and-sufficient, amplitude-uniform threefold offset threshold or unique instantaneous maximum. Roques and coauthors (2022) model compartmentalized hillslope drainage and discuss multi-component linear recession benchmarks rather than this equal-power nonlinear threshold. Those results motivate the present two-nonlinear-store problem but do not, in the inspected materials, give the unique-maximum criterion (2) or the sharp threefold offset contrast for exceeding exponent two. The classical log-slope identity and the general mixture inequality are not claimed as new in isolation; the contribution is their sharp classification in the hydrologic model.

## Limitations

No rainfall during the modeled recession, identical drainage-power exponents across stores, no store interactions, and exact differentiability are assumed. Changes under distinct powers, evapotranspiration, noise, or finite-window regression are not established. Exceeding exponent two is possible for some amplitudes if and only if the offset contrast exceeds three; it is **not** asserted to occur for every choice of amplitudes above that contrast. The literature review does not constitute independent priority verification. The full text of Wittenberg (1999) and Gao and coauthors (2017) was not obtained; their publicly accessible abstracts and metadata were consulted, and the remaining historical-coverage risk should be considered before external publication.

## References

- H. Wittenberg (1999), *Baseflow recession and recharge as nonlinear storage processes*, Hydrological Processes 13, 715–726. DOI: https://doi.org/10.1002/(SICI)1099-1085(19990415)13:5%3C715::AID-HYP775%3E3.0.CO;2-N (first published 1999-04-29).
- J. W. Kirchner (2009), *Catchments as simple dynamical systems: Catchment characterization, rainfall-runoff modeling, and doing hydrology backward*, Water Resources Research 45, W02429. https://doi.org/10.1029/2008WR006912.
- C. J. Harman, M. Sivapalan and P. Kumar (2009), *Power law catchment-scale recessions arising from heterogeneous linear small-scale dynamics*, Water Resources Research 45, W09404. https://doi.org/10.1029/2008WR007392.
- H. K. McMillan, M. P. Clark, W. B. Bowden, M. Duncan and R. A. Woods (2011), *Hydrological field data from a modeller's perspective: Part 1. Diagnostic tests for model structure*, Hydrological Processes 25, 511–522. Open author manuscript: https://www.hilandtom.com/hilarymcmillan/McMillanClark_ModelStructure_1_Proof.pdf.
- M. Gao, X. Chen, J. Liu, Z. Zhang and Q. Cheng (2017), *Using Two Parallel Linear Reservoirs to Express Multiple Relations of Power-Law Recession Curves*, Journal of Hydrologic Engineering 22. https://doi.org/10.1061/(ASCE)HE.1943-5584.0001518.
- C. Roques et al. (2022), *Recession discharge from compartmentalized bedrock hillslopes*, Hydrology and Earth System Sciences 26, 4391–4410. https://doi.org/10.5194/hess-26-4391-2022.
- E. R. Jachens, D. E. Rupp, C. Roques and J. S. Selker (2020), *Recession analysis revisited: impacts of climate on parameter estimation*, Hydrology and Earth System Sciences 24, 1159–1170. https://doi.org/10.5194/hess-24-1159-2020.

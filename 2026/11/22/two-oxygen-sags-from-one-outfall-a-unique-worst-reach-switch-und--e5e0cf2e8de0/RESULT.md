# Two oxygen sags from one outfall: a unique worst-reach switch under a reaeration drop

## Finding

**Theorem (two-reach oxygen-sag and critical-location law).** Let \(f:[0,\infty)\to(0,\infty)\) be continuously differentiable, satisfy \(f'(t)<0\) for every \(t\ge0\), and have **nondecreasing fractional decay hazard** \(h(t)=-f'(t)/f(t)\) (equivalently, \(\log f\) is concave). Fix constants \(b>c>0\) and, for each interface location \(d>0\), define the unique continuous nonnegative deficit \(D_d\) by
\[
D_d(0)=0,\qquad D_d'(t)=f(t)-r_d(t)D_d(t),\qquad
r_d(t)=\begin{cases}b,&0\le t<d,\\c,&t>d.\end{cases}
\]
The source \(f\) remains unchanged at \(d\): there is **one initial pollutant input and no second outfall**. Let \(U(t)=\int_0^t e^{-b(t-s)}f(s)\,ds\), and denote by \(t_0>0\) its unique maximizer. Define
\[
\ell=\lim_{t\to\infty}\frac{f(t)}{U(t)}\in[0,b),\qquad
 d_{\mathrm{end}}=\begin{cases}
 \text{the unique }d>t_0\text{ satisfying } f(d)=cU(d),&c>\ell,\\
 +\infty,&c\le\ell.
 \end{cases}
\]
Then \(D_d\) has **exactly two distinct strict local maxima** (two oxygen minima) if and only if
\[
\boxed{\quad t_0<d<d_{\mathrm{end}}.\quad}
\]
In that regime, the first maximum is at \(t_0\) and the second is at a unique \(t_2(d)>d\), with a strict corner minimum at \(d\). There exists **exactly one** \(d_*\in(t_0,d_{\mathrm{end}})\) where the two maxima have equal height. For \(d<d_*\), the downstream maximum is the unique global maximum; for \(d>d_*\), the upstream maximum at \(t_0\) is the unique global maximum; at \(d=d_*\), both are global maxima. When the first maximum does not yet occur before the interface, “upstream maximum” in this comparison means the fixed reference height \(U(t_0)\), not an actual separate peak.

For the concrete single-exponential input \(f(t)=e^{-t}\), upstream rate \(b=3\), and downstream rate \(c=1\), the two maxima occur for **every** \(d>\frac12\log3\), yet the global worst oxygen-sag position switches **exactly once** at \(d_*\) defined by
\[
\boxed{\quad d_*+\frac{1+e^{-2d_*}}2=\frac32\log3,\qquad
1.091575<d_*<1.091576.\quad}
\]
Thus two oxygen minima can persist at arbitrarily large interface distance although the **worst** minimum moves back to the upstream site.

## Assumptions and scope

Travel-time coordinate \(t\ge0\) is proportional to downstream distance only when plug-flow velocity is constant. The model has complete cross-sectional mixing, zero initial deficit, a strictly positive decreasing oxygen-consumption input \(f\) originating at one upstream wastewater discharge, first-order reaeration, no pollutant source or oxygen shock at the interface, and two **constant** reaeration coefficients \(b>c>0\) on the respective reaches. The interface changes the kinetic coefficient, not pollutant concentration, hydraulic travel speed, water volume, or oxygen saturation. The deficit \(D_d\) is continuous but may have a derivative jump at \(t=d\); extrema there use the ordinary local-value definition. Scaling \(f\) by a positive constant scales all deficits without changing the extrema or thresholds. Choose the amplitude sufficiently small to maintain oxygen concentration above zero for a chosen positive saturation level.

The general hypothesis permits nonexponential \(f\), such as \(f(t)=A\exp(-at-pt^2)\) for \(A,a>0\) and \(p\ge0\), and expresses a nondecreasing fractional decay hazard. It excludes inputs whose fractional decay rate oscillates; those may have a more complicated interface count. The claim concerns an **infinite ideal downstream reach**, and never infers actual field minima or regulatory compliance.

## Proof

**1. A unique stationary maximum on every constant-rate reach.** For any \(r>0\), the equation \(Y'=f-rY\) gives \((e^{rt}Y')'=e^{rt}f'(t)<0\). Hence the derivative has at most one zero on a constant-rate interval, and any such zero crosses strictly from positive to negative. The upstream solution \(U\) is initially increasing since \(U'(0)=f(0)>0\). The hypotheses imply \(f(t)\to0\) exponentially fast: because \(h\) is nondecreasing and positive at zero, \(f(t)\le f(0)e^{-h(0)t}\). Consequently \(U(t)\to0\), so \(U\) must have precisely one strict maximum at \(t_0\), where \(f(t_0)=bU(t_0)\). The same argument applies downstream, where \(D_d(t)\to0\) for each fixed \(d\).

**2. A strictly decreasing critical ratio.** Let \(Q(t)=U(t)/f(t)\) for \(t>0\). Changing variables in its integral representation yields
\[
Q(t)=\int_0^t e^{-bu}\frac{f(t-u)}{f(t)}\,du
=\int_0^t e^{-bu}\exp\!\left(\int_{t-u}^{t} h(v)\,dv\right)du.
\]
For fixed \(u\), the integrand is nondecreasing as \(t\) increases, because \(h(t)-h(t-u)\ge0\); the integration interval also increases and the added part is positive. Therefore \(Q\) is **strictly increasing**, so \(R(t)=f(t)/U(t)\) is strictly decreasing from \(+\infty\) to some limit \(\ell\ge0\). Since \(R(t_0)=b\), strict decrease forces \(\ell<b\). Consequently the equation \(R(d)=c\), for \(c<b\), has at most one solution past \(t_0\), and it has exactly one if and only if \(c>\ell\). This establishes the stated definition and ordering of \(d_{\mathrm{end}}\).

**3. The exact local-extremum phase diagram.** At the interface, continuity gives \(D_d(d)=U(d)>0\), while the one-sided derivatives satisfy
\[
D_d'(d-)=f(d)-bU(d),\qquad D_d'(d+)=f(d)-cU(d).
\]
For \(d\le t_0\), the upstream branch is increasing up to \(d\), and the downstream right derivative is positive because \(c<b\); the downstream branch has exactly one maximum and there is no upstream maximum. For \(t_0<d<d_{\mathrm{end}}\), the upstream branch already peaked at \(t_0\), its left derivative at \(d\) is negative, and its right derivative is positive. By Step 1, the downstream derivative then has exactly one zero, a strict maximum, while \(d\) is a strict corner minimum. For \(d\ge d_{\mathrm{end}}\) when this endpoint is finite, the right derivative is nonpositive and the downstream branch decreases for all \(t>d\). At equality, \((e^{ct}D_d')'<0\) rules out a second maximum. Hence the two-maximum condition is **necessary and sufficient**, with all boundary cases covered.

**4. A unique global-worst-site switch.** For any \(0<d_1<d_2\) and \(t>d_2\), the profile with the earlier interface has strictly **greater** deficit:
\[
D_{d_1}(t)>D_{d_2}(t).
\]
Indeed, the two profiles are equal through \(d_1\); on \((d_1,d_2)\) the first loses deficit at the smaller rate \(c\) instead of \(b\), giving strict comparison by the scalar variation-of-constants formula. Their subsequent evolution under the same \(c\) preserves that positive difference. For \(d\in(t_0,d_{\mathrm{end}})\), let \(P(d)=D_d(t_2(d))\) be the downstream peak height. If \(d_1<d_2\) both lie in this interval, then
\[
P(d_1)\ge D_{d_1}(t_2(d_2))>D_{d_2}(t_2(d_2))=P(d_2),
\]
so \(P\) is strictly decreasing. Continuity of \(P\) follows from continuous parameter dependence and the transversal downstream zero of \(D_d'\), for which \(D_d''=f'<0\) at stationarity.

At \(d=t_0\), the downstream coefficient drop makes the deficit increase immediately after \(t_0\), hence \(P(t_0)>U(t_0)\). If \(d_{\mathrm{end}}<\infty\), define the weighted downstream slope, for \(t\ge d\), by
\[
G(d,t)=e^{cd}(f(d)-cU(d))+\int_d^t e^{cs}f'(s)\,ds.
\]
It is strictly decreasing in \(t\), and at fixed \(t\) its derivative in \(d\) is \(c(b-c)e^{cd}U(d)>0\), using \(U'=f-bU\). Thus \(G(d,d_{\mathrm{end}})<G(d_{\mathrm{end}},d_{\mathrm{end}})=0\) for \(d<d_{\mathrm{end}}\). Since \(G(d,d)>0\) in the two-peak regime, \(d<t_2(d)<d_{\mathrm{end}}\); in particular \(t_2(d)\to d_{\mathrm{end}}\) from below as \(d\uparrow d_{\mathrm{end}}\). The stationary height is \(f(t_2(d))/c\), so \(P(d)\to f(d_{\mathrm{end}})/c=U(d_{\mathrm{end}})<U(t_0)\). If \(d_{\mathrm{end}}=\infty\), then the representation
\[
D_d(d+s)=U(d)e^{-cs}+\int_d^{d+s}e^{-c(d+s-u)}f(u)\,du
\]
gives \(P(d)\le U(d)+f(d)/c\to0\) as \(d\to\infty\). By strict monotonicity and continuity there is exactly one \(d_*\) with \(P(d_*)=U(t_0)\). The stated global-maximality regimes follow together with Step 3.

**5. Exact single-exponential example.** Put \(f(t)=e^{-t}\), \(b=3\), \(c=1\). Then
\[
U(t)=\frac{e^{-t}-e^{-3t}}2,\quad
 t_0=\frac{\log3}{2},\quad U(t_0)=\frac1{3\sqrt3},\quad
\ell=2>c.
\]
Thus \(d_{\mathrm{end}}=+\infty\). For \(t=d+s\), direct integration yields
\[
D_d(d+s)=e^{-d-s}\left(\frac{1-e^{-2d}}2+s\right),\qquad
s_2(d)=\frac{1+e^{-2d}}2.
\]
The downstream maximum is at \(t_2(d)=d+s_2(d)\), with height \(P(d)=e^{-t_2(d)}\). Equating this to \(1/(3\sqrt3)\) gives exactly the boxed scalar equation. Its left side is strictly increasing since its derivative is \(1-e^{-2d}>0\). At \(d=t_0\) the left side is smaller than \(\frac32\log3\); at large \(d\) it is larger. Uniqueness also follows from Step 4. The stated six-decimal bracket is certified by exact rational Taylor and inverse-hyperbolic-tangent inequalities in the standalone verifier; no plotted or finite grid evidence is used to infer uniqueness.

## Verification

Run `python3 verify.py` with only the Python standard library. The verifier checks the exact exponential solution, downstream peak conditions, strict upstream/downstream ordering, 20,000 reproducible random exponential-rate/interface instances, and 3,750 ratio comparisons for nonexponential positive log-concave demand functions. It also uses rational arithmetic and explicit one-sided Taylor-remainder bounds for the exponential and the series \(\log 3=2\sum_{j\ge0}2^{-(2j+1)}/(2j+1)\) to **certify** \(1.091575<d_*<1.091576\). This certifies only the specified rational sign inequalities; it is not a machine proof of the quantified theorem. The general theorem rests on the analytical arguments above.

For the displayed exponential example, \(d=1\) yields an upstream peak approximately \(0.192450089730\) and a downstream peak approximately \(0.208530984594\), while \(d=1.2\) gives the same upstream peak and a downstream peak approximately \(0.174582306746\). Both interfaces lie in the **two-peak** regime, but their global-worst locations are opposite.

## Relationship to prior work

The classical Streeter–Phelps oxygen-deficit balance and its one-peak constant-coefficient solution are established mathematics. Wu and Yu (2021) model how channel cross-section changes affect reaeration and dissolved oxygen through coupled hydrodynamics, including spatially varying regions, but their inspected model and results do not state the one-outfall, two-reach extrema classification or unique global-worst-site switch proved here. Pathak and colleagues (2022) study reach-specific oxygen metabolism and reaeration in a river network; their more detailed calibrated numerical model does not imply the sharp interface phase law as a stated mathematical result. D'Agostino and Eberl (2025) allow variable reaeration in the Streeter–Phelps framework and prove differential inequalities; the inspected time-dependent-parameter analysis does not give the asserted strict-ratio criterion, double-sag classification or global-worst-site crossover.

Related published mathematical results on two **separate** BOD outfalls derive multiple sag regimes by injecting additional pollutant, and work on one in-stream aerator modifies oxygen deficit by an instantaneous **state reset**. Neither is the same model: here pollutant input never jumps, deficit remains continuous, and only its **future removal coefficient** changes at a single interface. In particular the former's fixed downstream reaeration rate and extra input cannot simply be specialized to the present coefficient-jump model; the latter assumes a downward state jump, absent here. The theorem's claimed contribution is the combined, hazard-general phase classification and unique global-maximizer switch, **not** the classical ODE, known comparison principles or a claim that multi-reach water-quality modeling itself is new.

## Limitations

An abrupt reaeration interface is an idealization. No mixing/dispersion, hydrodynamic discontinuity, extra tributary flow, sediment oxygen demand, photosynthesis, nitrification, nonlinear oxygen-limited consumption, or uncertain parameters are modeled. The input must be strictly decreasing with nondecreasing fractional decay hazard, and the two reach coefficients must satisfy \(0<c<b\). A general time-varying river is not proved to have two sags at most. The model's extrema and their heights are not a field-calibrated oxygen prediction. Historical priority remains provisional in view of older reach-by-reach engineering treatments and limited access to some relevant papers.

## References

1. J. Wu and X. Yu, *Numerical Investigation of Dissolved Oxygen Transportation through a Coupled SWE and Streeter–Phelps Model*, Mathematical Problems in Engineering (first published 8 February 2021), DOI: https://doi.org/10.1155/2021/6663696 . Full text inspected: https://onlinelibrary.wiley.com/doi/10.1155/2021/6663696 .
2. D. Pathak et al., *High-resolution water-quality and ecosystem-metabolism modeling in lowland rivers*, Limnology and Oceanography 67 (first published 13 April 2022), DOI: https://doi.org/10.1002/lno.12079 . Full text inspected: https://aslopubs.onlinelibrary.wiley.com/doi/10.1002/lno.12079 .
3. G. D'Agostino and H. J. Eberl, *Uncertainty Analysis of a Simple River Quality Model Using Differential Inequalities*, SIAM Review (2025), DOI: https://doi.org/10.1137/23M1616406 . Full text inspected: https://epubs.siam.org/doi/full/10.1137/23M1616406 .
4. H. W. Streeter and E. B. Phelps, *A Study of the Pollution and Natural Purification of the Ohio River*, U.S. Public Health Bulletin 146 (1925); classical oxygen-sag model.
5. *Reentrant double-sag regimes for two separated biochemical oxygen-demand sources* (published mathematical result, 2026), https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-reentrant-double-sag-regimes-for-two-separated-biochemical-oxyge--92e4f7efeacb .
6. *Finite-reach saturation and a quadratic placement law for one fractional river aerator* (published mathematical result, 2026), https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-finite-reach-saturation-and-a-quadratic-placement-law-for-one-fr--0af40980b939 .

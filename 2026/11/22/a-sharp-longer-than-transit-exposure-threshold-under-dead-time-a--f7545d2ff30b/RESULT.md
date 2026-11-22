# A sharp longer-than-transit exposure threshold under dead time and independent noise floors

## Finding

**Theorem (complete phase-averaged cadence classification).** Fix a positive isolated box-shaped transit duration \(L\), a positive dead time \(H\) after every exposure, positive photon-noise parameter \(v\), and a nonnegative independent per-exposure flux-variance floor \(w\). Let the exposure length \(E>0\) be freely selected. Assume the baseline flux and transit timing are known, the unknown parameter is only transit depth, and the phase of the exposure lattice relative to the transit is uniform over one exposure cycle. Normalize

\[
x=E/L,\qquad h=H/L>0,\qquad r=wL/v\geq0.
\]

The expected Fisher information about transit depth, divided by the positive constant \(L/v\), is

\[
J_{h,r}(x)=\begin{cases}
\dfrac{x(1-x/3)}{(x+h)(1+rx)},&0<x\leq1,\\[4pt]
\dfrac{1-1/(3x)}{(x+h)(1+rx)},&x\geq1.
\end{cases}
\]

For every \(h>0\) and \(r\geq0\), this function has exactly one global maximizer \(x_*(h,r)>0\), strictly increasing in \(h\) and strictly decreasing in \(r\). Define

\[
Q(h,r)=h(1-r)-(1+3r).
\]

The optimum is shorter than, equal to, or longer than the whole transit precisely as \(Q<0\), \(Q=0\), or \(Q>0\), respectively. In particular, an optimal exposure longer than the transit exists **if and only if** \(0\leq r<1\) and

\[
 h>\frac{1+3r}{1-r}.
\]

For \(Q\leq0\), the optimizer has the closed form

\[
 x_*=\frac{3h}{h+\sqrt{h^2+3h(1+3r+hr)}}.
\]

For \(Q>0\), it is the unique root \(x>1\) of

\[
 h+2x-3x^2+r(2hx-3hx^2+3x^2-6x^3)=0.
\]

The asymptotics are sharp:

\[
 x_*\sim\sqrt{\frac{3h}{1+3r}}\quad(h\downarrow0),
\]

and, when \(h\to\infty\),

\[
 x_*\longrightarrow\begin{cases}
\dfrac{1+\sqrt{1+3/r}}{3},&0<r<1,\\[4pt]
\dfrac{\sqrt{1+3r}-1}{r},&r\geq1,
\end{cases}
\]

whereas for \(r=0\) the optimizer is \((1+\sqrt{1+3h})/3\) when \(h>1\), and grows like \(\sqrt{h/3}\). Thus every strictly positive independent noise floor bounds the optimal exposure as dead time grows without bound, while purely photon-limited exposures do not.

## Assumptions and scope

A single idealized transit has unit-depth template \(s(t)=\mathbf1_{[0,L]}(t)\). Each exposure integrates the flux for \(E\) time units and is followed by a dead time \(H>0\). Exposure starts lie on an infinite lattice \(\theta+k(E+H)\), where \(\theta\) is uniform over one cycle and the observation campaign covers the entire isolated event. The fitted parameter is a scalar depth \(d\), with normalized expected flux \(1-dq_E(t)\), where

\[
q_E(t)=\frac1E\int_t^{t+E}s(u)\,du.
\]

Errors in different exposures are independent zero-mean Gaussian variables with known variance \(v/E+w\), where \(v>0\) and \(w\geq0\). Transit duration and ephemeris are known; the out-of-transit baseline is fixed. The objective is phase-averaged *depth* Fisher information, not the multivariate information matrix for depth, timing, duration, impact parameter, and stellar limb darkening. The model explicitly excludes time-correlated stellar variability, saturation, finite observing boundaries and integer constraints on the number of exposures.

## Proof

**1. Phase-averaged information.** For fixed lattice phase \(\theta\), the Gaussian depth information is

\[
\mathcal I(\theta,E)=\frac{1}{v/E+w}\sum_{k\in\mathbb Z}q_E(\theta+k(E+H))^2.
\]

The template has compact support, so only finitely many summands are nonzero for each phase. Integrating \(\theta\) over one lattice period and tiling the real line gives exactly

\[
\mathbb E_\theta\mathcal I=\frac{1}{(E+H)(v/E+w)}\int_{\mathbb R}q_E(t)^2\,dt.
\]

**2. Exact convolution energy.** The overlap of two intervals has two linear wings and, when their lengths differ, a constant central section. Direct integration gives

\[
\int_{\mathbb R}q_E(t)^2\,dt=\begin{cases}L-E/3,&0<E\leq L,\\[3pt]L^2/E-L^3/(3E^2),&E\geq L.\end{cases}
\]

Substitution proves the stated two-piece formula for \(J_{h,r}\); the two branches and their first derivatives agree at \(x=1\).

**3. Unique global maximizer and threshold.** Put \(D(x)=(x+h)(1+rx)>0\). On \(0<x\leq1\), direct differentiation gives

\[
3D(x)^2J'(x)=P_1(x):=3h-2hx-(1+3r+hr)x^2.
\]

The polynomial \(P_1\) strictly decreases from \(3h>0\) to \(Q(h,r)\). On \(x\geq1\),

\[
3x^2D(x)^2J'(x)=P_2(x):=h+2x-3x^2+r(2hx-3hx^2+3x^2-6x^3).
\]

Here \(P_2(1)=Q(h,r)\) and

\[
P_2'(x)=2-6x+r(2h-6hx+6x-18x^2)<0\quad(x\geq1).
\]

Moreover \(P_2(x)\to-\infty\). Hence the derivative changes sign exactly once, from positive to negative; there are no competing local or boundary maxima. The branch test follows from the common derivative sign at \(x=1\). Solving \(P_1=0\) gives the explicit root, while the strictly decreasing polynomial \(P_2\) supplies the unique root beyond one. The criterion \(Q>0\) is equivalent to \(r<1\) and the asserted strict threshold on \(h\). Equality at the threshold makes \(x_*=1\) the *unique* optimum.

**4. Comparative statics and limits.** At a root of \(P_1\), the derivatives \(\partial_xP_1<0\), \(\partial_rP_1=-(h+3)x^2<0\) and \(\partial_hP_1=3-2x-rx^2=(1+3r)x^2/h>0\) establish strict decrease with \(r\) and strict increase with \(h\). At the root of \(P_2\), \(\partial_xP_2<0\), while

\[
\partial_rP_2=h(2x-3x^2)+3x^2-6x^3<0,
\]

and \(\partial_hP_2=1+2rx-3rx^2>0\), the last inequality following from \(P_2=0\) and \(2x-3x^2+r(3x^2-6x^3)<0\). The same strict monotonicity extends across \(x=1\) by continuity and uniqueness. Expanding the positive quadratic root at small \(h\) proves the first asymptotic. As \(h\to\infty\), divide the appropriate stationarity polynomial by \(h\) and solve its positive limiting root. When \(r=0\), the large-exposure root is the displayed quadratic formula. All limit constants are attained as limits and therefore sharp.

## Verification

Run `python CHECKER.py` with Python, NumPy, SciPy and SymPy. The checker independently integrates the exposure-overlap geometry on 200 logarithmically spaced exposure lengths; compares the analytic optimizer against a direct bounded numerical maximization at 2000 randomized parameter pairs; tests regime boundaries, monotonicity and high-dead-time limits; and symbolically checks both derivative polynomials and the branch join. It reports 2283 passing checks. These computations corroborate, but do not replace, the analytic universal proof.

## Relationship to prior work

Hernandez Camero, Ho and Van Eylen (2023) establish empirical and numerical Fisher-information comparisons of exoplanet transit cadences, motivating exact exposure design. Price and Rogers (2014) derive analytic information formulas for integrated trapezoidal transits and explicitly discuss readout dead time and noise models, so the foundational information technique and the importance of overhead are *not* new here. Kipping (2023) proves that exposure-time smearing alone decreases transit signal-to-noise ratio and gives full top-hat-convolved transit expressions. The contribution asserted here is narrower and different: under an independent photon-plus-floor noise law and positive dead time, it proves a complete, globally unique optimizer for a box event and the exact condition for the optimizer to **exceed the entire event duration**, together with monotone comparative statics and limiting saturation. Existing general information formulas are relevant prior frameworks, not evidence by themselves of that exact optimizer classification. Broader historical priority remains subject to literature beyond the inspected items.

## Limitations

A rectangular transit is not a realistic limb-darkened light curve; an independently redrawn white-noise floor is not the same as correlated astrophysical jitter; and known timing/depth-only information is not joint transit-parameter precision. Extrapolating the longer-than-transit regime to a real telescope without instrument-specific noise, readout constraints, and phase behavior would be unjustified. The mathematical claim is exact only under the stated statistical model. Independent scientific validation has not been performed.

## References

1. Hernandez Camero, J., Ho, C. S. K., and Van Eylen, V., *Understanding and predicting cadence effects in the characterization of exoplanet transits*, MNRAS 520 (2023), 4103–4117. First public version: 2023-02-06. https://arxiv.org/abs/2302.02897 ; https://doi.org/10.1093/mnras/stad408.
2. Kipping, D., *The SNR of a Transit*, MNRAS 523 (2023), 1182–1191. First public version: 2023-05-11. https://arxiv.org/abs/2305.06790 ; https://doi.org/10.1093/mnras/stad1492.
3. Price, E. M., and Rogers, L. A., *Transit Light Curves with Finite Integration Time: Fisher Information Analysis*, ApJ 794 (2014), 92. First public preprint: 2014-08-18. https://arxiv.org/abs/1408.4124 ; https://doi.org/10.1088/0004-637X/794/1/92.

# Sharp variance thresholds for flowering-overlap duration and occurrence

## Finding

Two equally long flowering windows can react in opposite directions to additional year-to-year uncertainty about their relative onset. Let their common duration be \(L>0\), their deterministic onset separation \(d\geq0\), and their Gaussian relative-onset variance \(s\geq0\). Write \(F(s)\) for expected overlap duration and \(P(s)\) for the probability of any positive-duration overlap.

**Sharp duration threshold.** If \(0\leq d\leq L/2\), then \(F\) is strictly decreasing on \((0,\infty)\), with maximum at \(s=0\). If \(d>L/2\), it instead has precisely one maximizer \(s_F>0\), is strictly increasing before \(s_F\) and strictly decreasing after it. Define \(a=2d/L>1\) and let \(z_F\) be the unique positive solution to
\[
\log\cosh(az_F)=z_F.
\]
Then \(s_F=L^2/(2z_F)\), and the optimum emerges from zero at the sharp boundary according to
\[
s_F\sim\frac{L(2d-L)}{2\log2}\quad(d\downarrow L/2).
\]

**Distinct occurrence threshold.** If \(0\leq d<L\), the overlap probability \(P\) is strictly decreasing for all \(s>0\), and is maximized at zero variance. If \(d>L\), it instead has one maximizer
\[
s_P=\frac{2dL}{\log((d+L)/(d-L))}.
\]
For \(d=L\), the deterministic windows only touch, so \(P(0)=0\); however, \(P(s)\) strictly decreases on \(s>0\), with limit \(1/2\) as \(s\downarrow0\). This is a discontinuity at the zero-variance boundary, not an attained global maximum. When \(d>L\), the two positive optima obey the strict order
\[
0<s_P<s_F<d^2.
\]
Consequently, for \(L/2<d<L\), an initial increase of uncertainty **increases expected co-flowering duration but decreases the chance of co-flowering in a given year**.

For example, with \(L=1\), \(d=3/4\), optimum duration occurs at standard deviation \(\sqrt{s_F}=0.608141703088\ldots\). Its expected overlap is \(0.324475634104\ldots\), versus \(1/4\) without timing variability, while the overlap probability falls from one to \(0.657492697428\ldots\).

## Assumptions and scope

Work on a nonperiodic real time axis. The first species flowers uniformly (present/absent, not abundance-weighted) on \([0,L]\); the second flowers on \([d+\sqrt{s}Z,d+\sqrt{s}Z+L]\), where \(Z\) is standard normal. Both widths are fixed and nonrandom. The year-to-year variation is solely the Gaussian *relative* onset displacement (any shared calendar shift cancels). The overlap duration is \(O_s=(L-|d+\sqrt{s}Z|)_+\), where \((x)_+=\max\{x,0\}\); \(F(s)=\mathbb E O_s\); and \(P(s)=\Pr(O_s>0)\). At \(s=0\) the displacement is deterministic. The claimed global classifications range over all \(L>0\), \(d\geq0\), and \(s\geq0\), subject to the explicitly stated touching-boundary exception for \(P\). The terms "optimal" and "increase" refer separately to these two mathematical metrics, not to ecological fitness or an intervention choice.

## Proof

For \(s>0\) let \(\phi_s(x)=\exp(-x^2/(2s))/\sqrt{2\pi s}\) and \(k(x)=(L-|x|)_+\). Then
\[
F(s)=\int_{\mathbb R}k(x)\phi_s(x-d)\,dx.
\]
The heat-kernel identity \(\partial_s\phi_s=\tfrac12\partial_x^2\phi_s\) holds. The distributional second derivative of the triangular function \(k\) is \(k''=\delta_{-L}-2\delta_0+\delta_L\). Integrating by parts (or differentiating the explicit Gaussian integrals) gives the exact derivative
\[
F'(s)=\frac12[\phi_s(d-L)-2\phi_s(d)+\phi_s(d+L)]
=\phi_s(d)\left[e^{-L^2/(2s)}\cosh(dL/s)-1\right].
\]
Put \(z=L^2/(2s)>0\) and \(a=2d/L\). The sign is the sign of \(h_a(z)=\log\cosh(az)-z\). If \(a\leq1\), then \(\log\cosh(az)<az\leq z\) for every \(z>0\), so \(F'(s)<0\). If \(a>1\), \(h_a(0)=0\), \(h'_a(0)=-1\), \(h''_a(z)=a^2\operatorname{sech}^2(az)>0\), and \(h_a(z)\sim(a-1)z-\log2\) as \(z\to\infty\). Thus there is exactly one positive zero \(z_F\), with \(h_a(z)>0\) above and \(h_a(z)<0\) below it. Because \(z\) decreases as \(s\) increases, \(F'\) changes exactly once from positive to negative. Continuity at \(s=0\) and the vanishing limit as \(s\to\infty\) make it the unique global maximum. At \(a\downarrow1\), the exact identity
\[
h_a(z)=(a-1)z-\log2+\log(1+e^{-2az})
\]
shows \((a-1)z_F\to\log2\), yielding the asserted sharp onset asymptotic.

Write \(\Phi\) for the standard normal distribution function. For \(s>0\),
\[
P(s)=\Phi\!\left(\frac{L-d}{\sqrt{s}}\right)
-\Phi\!\left(\frac{-L-d}{\sqrt{s}}\right),
\]
with derivative
\[
P'(s)=\frac{(d-L)\varphi((d-L)/\sqrt{s})-(d+L)\varphi((d+L)/\sqrt{s})}{2s^{3/2}},
\]
where \(\varphi\) is the standard normal density. For \(0\leq d\leq L\), this derivative is strictly negative. For \(d>L\), its sign equals that of
\[
(d-L)\exp(-(d-L)^2/(2s))-(d+L)\exp(-(d+L)^2/(2s)),
\]
which is strictly positive precisely when \(s<s_P\), zero when \(s=s_P\), and strictly negative afterward. This yields the unique positive maximum. Directly from the formula and the strict-overlap definition, \(P(0)=\mathbf{1}_{\{d<L\}}\); for \(d=L\), its right-hand limit is \(1/2\), proving the exceptional endpoint statement.

To order the optima for \(d>L\), use the layer-cake identity
\[
F(s)=\int_0^L\Pr\{|d+\sqrt{s}Z|<u\}\,du.
\]
For every \(0<u<L<d\), the integrand is strictly unimodal in \(s\), with maximizer
\[
q(u)=\frac{2du}{\log((d+u)/(d-u))}
=d^2\frac{u/d}{\operatorname{artanh}(u/d)}.
\]
The function \(x/\operatorname{artanh}x\) is strictly decreasing on \((0,1)\), since \(\operatorname{artanh}x<x/(1-x^2)\), and is strictly less than one. Hence \(q(u)>q(L)=s_P\), and \(q(u)<d^2\) for every \(u\in(0,L)\). Differentiation under the integral on compact positive \(s\)-ranges now gives \(F'(s_P)>0\) and \(F'(d^2)<0\). The already-proved unique-maximum classification forces \(s_P<s_F<d^2\). Finally, in \(L/2<d<L\) the duration derivative is initially positive and the occurrence derivative always negative, yielding the claimed opposing responses. All inequalities are strict where asserted.

## Verification

The accompanying `verify_overlap.py` evaluates \(F\) by an independent Gaussian-moment formula and by Simpson integration of the triangular overlap kernel. It compares both to the derivative formula and checks the optimum ordering over fixed-seed random positive parameters, plus the numerical examples. Run with `python3 verify_overlap.py` (Python standard library only). Its finite numerical tests supplement the proof above and are not used to establish global uniqueness or asymptotics.

For reproducibility without the program, use the displayed formulas for \(F'(s)\) and \(P'(s)\). The strictly convex scalar equation for \(z_F\) has a unique positive root, so bisection after bracketing the positive crossing gives \(s_F\); the expression for \(s_P\) is explicit. The example is calculated using \(F(s)=\int_{-L}^L(L-|x|)\phi_s(x-d)dx\).

## Relationship to prior work

Austin et al. (2024) quantify changes in flowering duration and pairwise co-flowering in a long-term plant community, explicitly noting that species-specific variability in shifts can reassemble phenological overlap. They do not establish a Gaussian onset-variance classification or distinguish the two sharp metric thresholds here. Rudolf (2018) already shows that interannual phenology variation can produce nonlinear species-interaction responses in a different experimental/simulation setting; such qualitative nonlinear responses are **not** claimed as new. Buckley et al. (2021) compare duration, abundance-area overlap, and peak timing across grasshopper communities using empirical methods; this paper does not analyze the stated Gaussian fixed-width model. Weis et al. (2014) investigate flowering schedule variance and assortative mating, rather than the two exact random-interval metrics. Stemkovski et al. (2023) analyze skewed bee/flower abundance distributions and overlap coefficients. Montes-Perez et al. (2025) analyze annual plant–pollinator overlap days empirically. None of the inspected portions proves the joint sharp \(L/2\) versus \(L\) thresholds, unique variance optima, or their strict ordering. Standard Gaussian heat smoothing and normal-tail calculus are explicitly used as known tools, not original discoveries.

## Limitations

These are mathematical properties of two equal-length, binary, nonperiodic flowering windows with one Gaussian relative timing error. The theorem does not cover unequal or variable durations, abundance-weighted floral availability, environmental autocorrelation, truncated seasonal calendars, changing interaction partners, or population fitness. An optimum of either mathematical overlap metric is not necessarily an ecologically favorable policy or climate outcome. The positive overlap indicator has a genuine discontinuity at zero timing variance when windows exactly touch; that exceptional case is kept explicit. Broader historical mathematical literature on Gaussian smoothing and random-interval intersections may contain equivalent statements; no claim of absolute priority is made.

## References

1. Austin, M. W. et al. (2024), *Climate change increases flowering duration, driving phenological reassembly and elevated co-flowering richness*, New Phytologist. First public date 2024-07-24. https://doi.org/10.1111/nph.19994
2. Rudolf, V. H. W. (2018), *Nonlinear effects of phenological shifts link interannual variation to species interactions*, Journal of Animal Ecology. https://doi.org/10.1111/1365-2656.12850
3. Buckley, L. B. et al. (2021), *Grasshopper species' seasonal timing underlies shifts in phenological overlap in response to climate gradients, variability and change*, Journal of Animal Ecology. https://doi.org/10.1111/1365-2656.13451
4. Weis, A. E. et al. (2014), *The strength of assortative mating for flowering date and its basis in individual variation in flowering schedule*, Journal of Evolutionary Biology. https://doi.org/10.1111/jeb.12465
5. Stemkovski, M. et al. (2023), *Skewness in bee and flower phenological distributions*, Ecology. https://doi.org/10.1002/ecy.3890
6. Montes-Perez, N. et al. (2025), *Generalized plant–pollinator phenological climate-driven advances still lead to a decline in phenological overlap*, Ecological Monographs. https://doi.org/10.1002/ecm.70046

# A sharp tidal-amplitude threshold for false double salinity gradients in a single diffusive interface

## Finding

**Theorem (exact gradient-peak bifurcation).** Fix an interface midpoint \(m\in\mathbb R\), intrinsic diffusion width \(\sigma>0\), tidal-translation amplitude \(A\ge0\), and periodic phase \(\theta\in[0,2\pi]\). Let \(\Phi\) be the standard normal cumulative distribution function and define the *instantaneous normalized salinity front*
\[
S_\theta(x)=\Phi\!\left(\frac{x-m-A\cos\theta}{\sigma}\right),\qquad x\in\mathbb R.
\]
Its complete-cycle mean is \(\overline S_A(x)=(2\pi)^{-1}\int_0^{2\pi} S_\theta(x)\,d\theta\). Every instantaneous gradient \(S'_\theta\) has exactly one strict maximum. Nevertheless, the averaged gradient \(p_A(x)=\overline S_A'(m+x)\) has the following **complete** classification:

1. If \(0\le A/\sigma<a_*\), \(p_A\) has exactly one (strict) maximum, at \(x=0\).
2. If \(A/\sigma=a_*\), \(p_A\) still has exactly one strict maximum, at \(x=0\), but its quadratic curvature vanishes and its fourth derivative is strictly negative.
3. If \(A/\sigma>a_*\), \(p_A\) has exactly two strict maxima, one at positive \(x\) and one at its negative reflection, separated by a strict minimum at \(x=0\).

The universal, sharp threshold is
\[
a_*=2\sqrt{u_*}=1.777614605412\ldots,
\quad (2u_*-1)I_0(u_*)=2u_*I_1(u_*),
\quad u_*\in(1/2,1),
\]
where \(I_0,I_1\) are standard modified Bessel functions of the first kind. This equation has **exactly one** solution in \((1/2,1)\), and no other positive solution. The numerical root satisfies the certified rational enclosure \(0.7899784<u_*<0.7899785\).

For every amplitude, \(\overline S_A\) is strictly increasing with a **single** 50%-salinity crossing, \(\overline S_A(m)=1/2\). Thus two gradient peaks in a time-averaged profile do *not* require two simultaneous salinity interfaces in this model.

## Assumptions and scope

The result is a theorem for the stated translated Gaussian-error-function fronts on the **whole real depth axis**, sampled uniformly over a full sinusoidal phase cycle. It assumes unchanged intrinsic width, a spatially rigid sinusoidal translation, and linear concentration averaging (not averaging electrical resistivity). Each normalized profile lies strictly between zero and one and is increasing in \(x\). Reversing physical depth orientation reverses monotonicity but preserves the **magnitudes** and number of gradient peaks. A finite monitoring well must cover both outer maxima before two peaks can be observed. The translation model is a deliberately idealized kinematic proxy, not the governing density-dependent coastal groundwater PDE or the fitted van-Genuchten profile of the motivating field study.

A fixed-time diffusing step under constant scalar diffusivity \(D>0\) has an error-function interface of the stated form with \(\sigma=\sqrt{2Dt}\); the externally imposed translation is an additional modeling assumption. The threshold is independent of the phase period and of \(m\).

## Proof

**1. Shape and arcsine reduction.** Write \(\varphi_\sigma(x)=\exp(-x^2/(2\sigma^2))/(\sqrt{2\pi}\sigma)\). Differentiation under the phase integral gives
\[
p_A(x)=\frac1{2\pi}\int_0^{2\pi}\varphi_\sigma(x-A\cos\theta)\,d\theta.
\]
For \(A>0\), this is the convolution of the Gaussian density with the arcsine law \(g_A(y)=\mathbf1_{|y|<A}/(\pi\sqrt{A^2-y^2})\). Consequently \(p_A\) is even, positive, real analytic, and tends to zero at infinity. For \(x>A\), every integrand in \(p'_A(x)\) is negative, hence \(p'_A(x)<0\). Also \(\overline S_A(m)=1/2\) by \(\Phi(-z)=1-\Phi(z)\), and \(\overline S'_A>0\) everywhere.

**2. At most two gradient peaks.** Gaussian convolution is variation diminishing (the one-dimensional heat-kernel zero-crossing theorem). Here is its precise application: for \(\varepsilon>0\), replace the arcsine law by the normalized bounded density \(g_{A,\varepsilon}(y)=c_\varepsilon\mathbf1_{|y|<A}(A^2-y^2+\varepsilon)^{-1/2}\). Its distributional derivative has the ordered sign pattern \(+,-,+,-\): an upward atom at \(-A\), negative density on \((-A,0)\), positive density on \((0,A)\), and a downward atom at \(A\). It thus has only three sign changes. Gaussian convolution cannot increase the number of sign changes of this signed measure. As \(\varepsilon\downarrow0\), the densities converge to \(g_A\) in \(L^1\), and their Gaussian-convolved first derivatives converge uniformly to \(p'_A\), which therefore has at most three sign changes. The exceptional case \(A=0\) is a centered Gaussian.

In particular, if \(p''_A(0)<0\) then \(p'_A\) is negative just to the right of zero and beyond \(A\); any positive interval on the right would, by odd reflection, require at least five sign changes globally, impossible. Thus the center is the unique maximum. If \(p''_A(0)>0\), the center is a local minimum and \(p'_A>0\) immediately to its right, while \(p'_A<0\) beyond \(A\); exactly one sign-changing positive zero and its negative reflection are possible. These are exactly two strict maxima. An analytic stationary point without a derivative sign change cannot create another local extremum.

**3. Central curvature and the exact threshold.** Put \(u=A^2/(4\sigma^2)\). The Gaussian central density is
\[
p_A(0)=\frac{e^{-u}I_0(u)}{\sqrt{2\pi}\sigma}.
\]
For circular phase averages, direct integration by parts gives \(\partial_A^2p_A(0)+A^{-1}\partial_Ap_A(0)=p_A''(0)\) for \(A>0\), with a continuous limit at zero. Applying this identity and the Bessel recurrences \(I'_0=I_1\), \(I'_1=I_0-I_1/u\), yields
\[
p_A''(0)=\frac{e^{-u}}{\sqrt{2\pi}\sigma^3}
\left[(2u-1)I_0(u)-2u I_1(u)\right].
\]
For \(u\le1/2\), the bracket is negative. For \(u>1/2\), define \(r(u)=I_1(u)/I_0(u)\) and \(d(u)=1-1/(2u)-r(u)\). Standard Bessel identities give \(r'=1-r^2-r/u\). At every zero of \(d\), substitution gives
\[
d'(u)=\frac1{4u^2}>0.
\]
At \(u=1/2\), \(d<0\). At \(u=1\), \(d>0\), because \(I_0(1)>2I_1(1)\): subtracting their positive series produces \(\sum_{k\ge1}4^{-k}k/((k+1)(k!)^2)>0\). Thus there is at least one root in \((1/2,1)\). Since every possible zero crosses strictly from negative to positive, there is exactly one zero on the entire positive axis. Its sign splits the three regimes above.

**4. Degenerate threshold is still unimodal.** Let \(B(u)=(2u-1)I_0(u)-2uI_1(u)\). At its unique root, the Bessel identities yield \(B'(u_*)=I_0(u_*)/(2u_*)\) and \(B''(u_*)=-I_0(u_*)/(2u_*^2)\). Apply the same circular-mean differential operator once again to the expression for \(p_A''(0)\). It follows that
\[
p_A^{(4)}(0)=-\frac{p_A(0)}{\sigma^4}<0
\quad\text{when }A/\sigma=a_*.
\]
Hence \(p'_A(x)<0\) for sufficiently small positive \(x\), despite its vanishing quadratic curvature. The sign-variation argument in step 2 excludes any outer maxima at equality. This proves the full classification.

## Verification

The standalone standard-library script `CHECK.py` proves with exact rational interval bounds that \(0.7899784<u_*<0.7899785\), by bounding truncated positive Bessel series and their remainders. It also numerically checks Bessel recurrences' predicted curvature signs, center symmetry, and the two-peak witness at \(A/\sigma=2\). At that amplitude the two maxima occur at approximately \(x/\sigma=\pm0.849788389492\); the central derivative density is approximately \(0.185811200/\sigma\), versus approximately \(0.189261680/\sigma\) at each outer peak. These numerical checks are *supplementary*, not a substitute for the global proof of modal completeness.

To reproduce, save `CHECK.py` alongside this document and run `python CHECK.py` with standard Python 3. No external dataset is required.

## Relationship to prior work

Huang, Werner, Solórzano-Rivas, and Jazayeri (2024) analyze coastal aquifer conductivity profiles using a flexible van-Genuchten-type sigmoid, reporting that the midpoint gradient and mixing-zone width carry information beyond the 50%-salinity interface and discussing tidal effects as a motivating physical influence. Their fitted family and field measurements are **not** the translated Gaussian front here, and no sharp phase-averaging gradient-modal threshold is supplied by their investigated methods or conclusions.

Laurel-Castillo and Valle-Levinson (2023) provide a tidal/subtidal estuarine salinity-decomposition framework, involving physical advection–diffusion and two exponential signals rather than the full-cycle average of one translating error-function front. Kim and collaborators (2008) document tidal variation in coastal conductivity and interface width; their available abstract does not resolve the mathematical modal classification here. Genda, Fidlin, and Gendelman (2024) prove a general fast-oscillation averaging/cross-correlation representation and derive arcsine-distribution Bessel moments, which **already cover the basic averaging and arcsine reduction**; their investigated results do not provide the present Gaussian-front modality threshold. The Gaussian sign-variation theorem (e.g. Evans and Williams, 1998) is **classical prior mathematics**, used only for the upper bound on modes. Neither this general theorem alone nor the hydrological studies alone yields the displayed Bessel threshold without the specific convolution and curvature analysis. Other potentially relevant signal-processing treatments of Gaussian-blurred sinusoidal distributions may exist, so historical novelty is not independently established.

## Limitations

The theorem concerns a fully averaged, spatially translated Gaussian-CDF interface, not dynamically coupled tides, density-driven circulation, vertical heterogeneity, unequal sampling times, non-Gaussian fronts, finite spatial boundaries, or direct electrical-conductivity measurements with nonlinear instrument response. The two outer peaks may be outside an actual screened interval. The theorem is a diagnostic warning for model interpretation, not a claim that a particular coastal aquifer has this artifact. The cited 2008 field study was compared at the abstract level rather than in full text. Independent audit and field validation have not been performed.

## References

- Huang, X., Werner, A. D., Solórzano-Rivas, S. C., and Jazayeri, A. (2024). *Salinity Profiles in Coastal Aquifers: A Characterization Framework for Field Measurements*. Water Resources Research. First published 19 June 2024. https://doi.org/10.1029/2024WR037244
- Laurel-Castillo, J. A., and Valle-Levinson, A. (2023). *A Statistics-Based Analytical Framework for Intratidal and Tidally Averaged Salinity Distribution in Estuaries*. JGR Oceans. First published 18 December 2023. https://doi.org/10.1029/2023JC019813
- Genda, A., Fidlin, A., and Gendelman, O. (2024). *An alternative approach to averaging in nonlinear systems using classical probability density*. ZAMM. First published 22 March 2024. https://doi.org/10.1002/zamm.202300432
- Kim, K.-Y. et al. (2008). *Multi-depth monitoring of electrical conductivity and temperature of groundwater at a multilayered coastal aquifer: Jeju Island, Korea*. Hydrological Processes. https://doi.org/10.1002/hyp.6976
- Evans, S. N., and Williams, R. J. (1998). *Transition operators of diffusions reduce zero-crossing*. https://arxiv.org/abs/math/9801146
- *Applications of total positivity theory to 1D prescribed curvature problems*. Journal of Mathematical Analysis and Applications (2015). DOI: https://doi.org/10.1016/j.jmaa.2015.03.002 (variation-diminishing theorem used as standard background)

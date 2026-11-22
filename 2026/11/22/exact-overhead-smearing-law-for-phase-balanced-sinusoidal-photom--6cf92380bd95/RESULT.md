# Exact overhead–smearing law for phase-balanced sinusoidal photometry

## Finding

Let a single periodic photometric signal of known angular frequency \(\omega>0\) be observed by equal-width exposures with a positive fixed overhead \(h>0\) per exposure. Under the photon-limited, independent Gaussian, phase-balanced model specified below, the information per unit charged observing time for either sinusoidal quadrature, normalized to the zero-overhead zero-exposure limit, is
\[
J_h(t)=\frac{t}{t+h}\left[\frac{\sin(\omega t/2)}{\omega t/2}\right]^2,\qquad t>0.
\]
It has exactly one global maximizing exposure \(t_*(h)>0\). With \(a=\omega h/2\), the dimensionless optimizer \(x_*(a)=\omega t_*(h)/2\) is the unique root in \((0,\pi/2)\) of
\[
2\cot x-\frac1x-\frac1{x+a}=0.
\]
The optimal exposure increases strictly with the overhead, but it always satisfies \(0<t_*(h)<(x_\infty/\pi)P\), where \(P=2\pi/\omega\) and \(x_\infty=1.1655611852072113068\ldots\) is the unique root of \(\tan x=2x\) on \((0,\pi/2)\). In particular, \(x_\infty/\pi=0.3710096482035515904\ldots\). The bounds and asymptotic laws are sharp:
\[
t_*(h)\sim(6h/\omega^2)^{1/3}\quad(h\downarrow0),\qquad
\frac{t_*(h)}P\longrightarrow\frac{x_\infty}{\pi}\quad(h\to\infty),
\]
\[
1-\max_{t>0}J_h(t)\sim(3\omega h/4)^{2/3}\quad(h\downarrow0),\qquad
\lim_{a\to\infty}a\max_{t>0}J_h(t)=\frac{\sin^2 x_\infty}{x_\infty}.
\]
The zero-overhead boundary \(h=0\) has a supremum of one as \(t\downarrow0\) and no positive maximizing exposure. These results concern a single harmonic, not arbitrary light curves.

## Assumptions and scope

For an integer \(N\ge3\), exposure midpoints \(s_j\) have phases \(\omega s_j\equiv2\pi j/N\pmod {2\pi}\). Midpoints may be placed on different orbital cycles. Each exposure of length \(t\) measures the arithmetic mean of \(c_0+c_1\cos(\omega s)+c_2\sin(\omega s)\), plus independent, centered Gaussian noise of variance \(\nu/t\), with \(\nu>0\). All exposures have the same width. The charged telescope allocation is exactly \(N(t+h)\); waiting for phase opportunities is not charged. Frequency, overhead, and noise scale are known. All three linear coefficients may be unknown and are jointly estimated. The Fisher information for each quadrature is \(Nt\operatorname{sinc}^2(\omega t/2)/(2\nu)\); the baseline and both quadratures have mutually orthogonal design columns. The maximizing result applies to information per charged observing time, not to a finite-calendar or continuously staring survey with phase-availability restrictions.

## Proof

**1. Reduction to the scalar objective.** Integrating either quadrature over a centered exposure multiplies it by \(\operatorname{sinc}(x)=\sin x/x\) with \(x=\omega t/2\). The phase-balance identities for \(N\ge3\) are \(\sum_j\cos\theta_j=\sum_j\sin\theta_j=\sum_j\sin\theta_j\cos\theta_j=0\) and \(\sum_j\cos^2\theta_j=\sum_j\sin^2\theta_j=N/2\). Since the observation variance is \(\nu/t\), both amplitude Fisher-information diagonal entries are \(Nt\operatorname{sinc}^2(x)/(2\nu)\). Division by \(N(t+h)\), followed by normalization by \(1/(2\nu)\), gives \(J_h\). Writing \(a=\omega h/2\), it becomes \(j_a(x)=\sin^2x/[x(x+a)]\).

**2. Existence, global first-lobe optimality, and uniqueness.** For \(a>0\), \(j_a(x)\to0\) as \(x\downarrow0\) and as \(x\to\infty\); the objective is positive on \((0,\pi)\). On \((0,\pi)\), its logarithmic derivative is \(g_a(x)=2\cot x-1/x-1/(x+a)\). On \((0,\pi/2)\),
\[
g_a'(x)=-2\csc^2x+\frac1{x^2}+\frac1{(x+a)^2}<0,
\]
because \(\sin x<x\) and \(a>0\). Also \(g_a(x)\to+\infty\) as \(x\downarrow0\), while \(g_a(\pi/2)<0\). Therefore there is one critical point on \((0,\pi/2)\), which is a strict maximum. On \([\pi/2,\pi)\), \(g_a<0\). For all \(x\ge\pi\),
\[
j_a(x)\le\frac1{\pi(\pi+a)}<\frac1{(\pi/2)(\pi/2+a)}=j_a(\pi/2)<j_a(x_*(a)).
\]
Thus the first-lobe maximum is the unique global maximum across all positive exposure lengths, including every possible later sinc lobe.

**3. Dependence on overhead.** The partial derivative \(\partial g_a/\partial a=1/(x+a)^2>0\). Since \(g_a'(x_*)<0\), implicit differentiation gives \(dx_*/da>0\). The optimizer is bounded above by the unique positive root \(x_\infty\) of \(2\cot x=1/x\), equivalently \(\tan x=2x\): indeed \(g_a(x_\infty)=-1/(x_\infty+a)<0\). As \(a\to\infty\), the root increases to \(x_\infty\), by uniform convergence on compact subsets. Hence \(t_*(h)<2x_\infty/\omega=(x_\infty/\pi)P\).

**4. Sharp small- and large-overhead laws.** Since \(x_*(a)\to0\) as \(a\downarrow0\), the root equation can be rewritten
\[
2\left(\frac1x-\cot x\right)=\frac{a}{x(x+a)}.
\]
As \(x\to0\), \(1/x-\cot x=x/3+O(x^3)\). The equation first forces \(a/x\to0\) (otherwise the right side is of order \(1/x\)); then it gives \(x_*^3\sim3a/2\). Substitution into \(j_a(x)=(x/(x+a))(\sin x/x)^2\) yields
\[
1-j_a(x_*)=\frac{a}{x_*}+\frac{x_*^2}{3}+o(a/x_*+x_*^2)\sim x_*^2\sim(3a/2)^{2/3}.
\]
For \(a\to\infty\), the limiting root above gives \(a j_a(x_*)\to\sin^2(x_\infty)/x_\infty\). The exposure and efficiency expansions follow after substituting \(a=\omega h/2\). When \(h=0\), \(J_0(t)=\operatorname{sinc}^2(\omega t/2)<1\) for \(t>0\) and approaches one as \(t\downarrow0\).

## Verification

Run \`python check.py\` (Python 3 with mpmath). It solves the defining scalar equation with high-precision bisection, checks stationarity, verifies 4,000 sampled competitor exposure lengths for each of nine overheads, checks 181 logarithmically distributed overheads, and tests both asymptotic regimes. The included checker reports 36,583 assertions passing and \(x_\infty/\pi\approx0.37100964820355\). For \(h/P=0.01\), it obtains \(t_*(h)/P\approx0.11142003026557\) and normalized information efficiency \(\max J_h\approx0.88077007150578\). These finite diagnostics supplement, but do not establish, the infinite-range inequalities proved above.

## Relationship to prior work

Watson and Dhillon (2001, arXiv:astro-ph/0101513, §3.6) describe orbital velocity smearing and a practical exposure-width rule, without optimizing a photon-limited, setup-overhead-charged phase-balanced Fisher objective. Kipping (2010, arXiv:1004.3741) quantifies transit-light-curve binning biases. Price and Rogers (2014, arXiv:1408.4124, §§VI–VII) analyze finite integration Fisher information for trapezoidal transits, explicitly treating readout time and effective sampling. Morello, Dyrek and Changeat (2022, arXiv:2210.14194, §§2–3) derive the sinusoidal sinc amplitude response and phase-curve uncertainty behavior. Thus the sinc factor, photon-noise scaling, readout accounting and survey-design motivation are prior ingredients. The contribution claimed here is restricted to the exact global optimizer, monotone overhead law, nonanalytic small-overhead scaling and universal long-overhead ceiling for the explicitly stated *single-harmonic* Fisher information rate. This is not an empirical generalization to transit signals or resolved radial-velocity line profiles.

## Limitations

Uniformly spaced orbital phases and independent Gaussian measurement noise are idealizations. The observational charge excludes calendar waiting and the availability of night-time phase slots. Detector read noise, saturation, correlated stellar variability, additional harmonics, orbital-parameter uncertainty, spectral-line broadening and simultaneous optimization over integer campaign lengths can change the answer. No field performance, instrumental validation, universality beyond the stated model, or historical-first claim is made. The literature search cannot rule out a mathematically equivalent unpublished or differently named result; the construction also builds on previously published sinc and readout-efficiency formulas. Numerical tests do not prove global maximality.

## References

1. Watson, C. A. and Dhillon, V. S. (2001), *Roche tomography of cataclysmic variables: I. artefacts and techniques*, arXiv:astro-ph/0101513 (first posted 2001-01-29), §3.6. https://arxiv.org/abs/astro-ph/0101513
2. Kipping, D. M. (2010), *Binning is sinning: morphological light-curve distortions due to finite integration time*, arXiv:1004.3741. https://arxiv.org/abs/1004.3741
3. Price, E. M. and Rogers, L. A. (2014), *Transit Light Curves with Finite Integration Time: Fisher Information Analysis*, arXiv:1408.4124 (posted 2014-08-18), §§VI–VII. https://arxiv.org/abs/1408.4124
4. Morello, G., Dyrek, A. and Changeat, Q. (2022), *Is binning always sinning? The impact of time-averaging for exoplanet phase curves*, arXiv:2210.14194, §§2–3. https://arxiv.org/abs/2210.14194

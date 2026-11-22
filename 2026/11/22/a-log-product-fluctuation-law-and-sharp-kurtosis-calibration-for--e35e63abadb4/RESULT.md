# A log-product fluctuation law and sharp kurtosis calibration for strongly sluggish resetting diffusion

## Finding

Consider stationary one-dimensional **Itô sluggish diffusion**, with generator \(\mathcal L f(x)=|x|^{-\alpha}f''(x)\), symmetric nonsticky continuation through zero, and independent complete Poisson resets to zero at rate \(r>0\). The exponent satisfies \(\alpha\ge 0\). Put \(\mu=1/(\alpha+2)\), let \(X\) have its stationary distribution, and write \(\sigma^2=\mathbb E[X^2]\). Define

\[
A_\mu=\frac{\Gamma(1+2\mu)\Gamma(1+\mu)}{\Gamma(1-\mu)}.
\]

**Exact stationary representation and moment inversion.** If \(E\) is unit exponential, \(G_\mu\) is independent Gamma with shape \(1-\mu\) and unit scale, and \(S\) is an independent fair sign, then

\[
X\ \stackrel d=\ S\left(\frac{(\alpha+2)^2}{r} E G_\mu\right)^\mu,
\qquad
\sigma^2=\left(\frac{(\alpha+2)^2}{r}\right)^{2\mu} A_\mu.
\]

For every real \(p\ge0\),

\[
\mathbb E|X|^p=\left(\frac{(\alpha+2)^2}{r}\right)^{p\mu}
\frac{\Gamma(1+p\mu)\Gamma(1+(p-1)\mu)}{\Gamma(1-\mu)}.
\]

**A sharp shape classification.** The normalized fourth moment

\[
K(\mu)=\frac{\mathbb E[X^4]}{(\mathbb E[X^2])^2}
=\frac{\Gamma(1+4\mu)\Gamma(1+3\mu)\Gamma(1-\mu)}
{\Gamma(1+2\mu)^2\Gamma(1+\mu)^2}
\]

is **strictly increasing** on \(0<\mu\le 1/2\). Hence for the finite sluggishness range \(\alpha\ge0\), its attainable interval is \(1<K\le6\), with \(K=6\) exactly at ordinary Brownian diffusivity \(\alpha=0\), and \(K\downarrow1\) only as \(\alpha\to\infty\). A stationary second and fourth moment uniquely identify both \(\alpha\) and \(r\): solve the strictly monotone displayed formula for \(\mu\), set \(\alpha=1/\mu-2\), then

\[
r=(\alpha+2)^2\left(\frac{A_\mu}{\sigma^2}\right)^{1/(2\mu)}.
\]

**Strong-sluggishness fluctuation law.** For \(\alpha\to\infty\), with an arbitrary positive reset rate \(r=r(\alpha)\), the variance-standardized stationary position \(Z=X/\sigma\) converges weakly to a fair two-point distribution on \(\{-1,+1\}\). Its collapsing radial fluctuations have a **non-Gaussian** universal boundary layer:

\[
\frac{|Z|-1}{\mu}\ \Longrightarrow\ W=\log(E_1E_2)+2\gamma,
\]

where \(E_1,E_2\) are independent unit exponentials and \(\gamma\) is Euler's constant. Its characteristic function and density are, respectively,

\[
\mathbb E[e^{itW}]=e^{2i\gamma t}\Gamma(1+it)^2,
\quad
f_W(w)=2e^{w-2\gamma}K_0\!\left(2e^{(w-2\gamma)/2}\right).
\]

In particular, \(\mathbb E W=0\), \(\operatorname{Var}(W)=\pi^2/3\), and the normalized kurtosis obeys the **sharp** collapse law

\[
K(\mu)-1=\frac{4\pi^2}{3}\mu^2+O(\mu^3)
=\frac{4\pi^2}{3(\alpha+2)^2}+O((\alpha+2)^{-3}).
\]

All conclusions concern stationary one-time statistics of the specified continuum process, not temporal correlations, path extrema, or the underlying lattice at fixed spacing.

## Assumptions and scope

The free diffusion is the symmetric, nonsticky solution of the Itô Fokker–Planck equation \(\partial_t p=\partial_x^2(|x|^{-\alpha}p)\), started at zero. For \(\alpha>0\), specifying the symmetric continuation through the singular origin is essential; a different extension or stochastic convention may give a different answer. Complete resets are instantaneous, independent and Poisson with positive rate \(r\), and the system is in its stationary renewal regime. The coefficient of \(|x|^{-\alpha}\) is one in the given dimensionless units. The claim holds for every \(\alpha\in[0,\infty)\), and its limiting assertions are as \(\alpha\to\infty\), equivalently \(\mu\downarrow0\). The dependence \(r=r(\alpha)>0\) is arbitrary because standardization cancels \(r\) exactly.

## Proof

**1. Excursion mixture and normalization.** The known free transition density from the origin [1, Eq. (6)] is proportional to \(|x|^\alpha t^{-(1-\mu)}\exp[-|x|^{1/\mu}/((\alpha+2)^2t)]\) and is symmetric in the sign. At a fixed free age \(t>0\), the change of variable

\[
y=\frac{|x|^{1/\mu}}{(\alpha+2)^2t}\]

has gamma density \(y^{-\mu}e^{-y}/\Gamma(1-\mu)\) on \(y>0\). Thus \(|X_t|=((\alpha+2)^2tG_\mu)^\mu\), with sign independent and fair. A stationary independent Poisson reset clock has backward age \(E/r\), where \(E\) is unit exponential; independent fresh excursions imply the stated product representation. Gamma moments yield the general moment formula. This derivation independently recovers the known stationary Bessel-density law [1, Eq. (21)] by gamma-product integration, so it does not assume a new stationary density.

**2. Strict monotonicity and inversion.** Let

\[
h(x)=\frac{(1+2x)^2(1+x)^2}{(1+4x)(1+3x)(1-x)},\quad0<x\le1/2.
\]

The Weierstrass product for \(\Gamma\), with cancellation of linear terms, gives the convergent product \(K(\mu)=\prod_{j=1}^\infty h(\mu/j)\). Direct exact polynomial algebra gives

\[
(1+2x)^2(1+x)^2-(1+4x)(1+3x)(1-x)
=4x^2(x^2+6x+2)>0,
\]

and the derivative's numerator is

\[
-8x(x+1)(2x+1)(3x+2)(x^2-3x-1)>0
\quad(0<x\le1/2).
\]

The denominator is strictly positive. Hence each \(h(\mu/j)\) is strictly increasing in \(\mu\); so is their product (already its first factor increases strictly, and all others are nondecreasing). At \(\mu=1/2\), direct gamma values give \(K=6\), while \(K\to1\) as \(\mu\downarrow0\). The inverse formulas follow algebraically from the second moment, proving global injectivity of the two-moment map within this model.

**3. Limit law and its fluctuations.** From step 1, the standardized absolute position is

\[
|Z|=\frac{(EG_\mu)^\mu}{\sqrt{A_\mu}}.
\]

The gamma shape \(1-\mu\to1\), so \(G_\mu\Rightarrow E_2\), a unit exponential independent of \(E=E_1\). The small-argument expansion \(\log\Gamma(1+z)=-\gamma z+O(z^2)\) gives \(\log A_\mu=-4\gamma\mu+O(\mu^2)\). Consequently

\[
\frac{\log|Z|}{\mu}
=\log E+\log G_\mu-\frac{\log A_\mu}{2\mu}
\Rightarrow\log E_1+\log E_2+2\gamma=W.
\]

The random variables on the left are tight, so the mean-value theorem or continuous mapping yields \((|Z|-1)/\mu\Rightarrow W\). The independent symmetric sign gives \(Z\Rightarrow\frac12(\delta_{-1}+\delta_{+1})\). Multiplication of gamma characteristic functions yields \(\mathbb E e^{itW}=e^{2i\gamma t}\Gamma(1+it)^2\). The standard gamma-product/Bessel integral \(f_{E_1E_2}(z)=2K_0(2\sqrt z)\), for \(z>0\), and a logarithmic change of variable yield \(f_W\) above. Digamma/trigamma values at one yield its mean and variance.

**4. Sharp fourth-moment collapse.** For \(x\downarrow0\), \(\log h(x)=8x^2+O(x^3)\). The expansion is uniform termwise after summation because \(\sum j^{-3}<\infty\). Therefore

\[
\log K(\mu)=8\mu^2\sum_{j=1}^\infty j^{-2}+O(\mu^3)
=\frac{4\pi^2}{3}\mu^2+O(\mu^3).
\]

Since \(K\to1\), exponentiation gives the stated equivalent. No finite-sample simulation is used to justify the distributional or asymptotic theorems.

## Verification

The provided standalone `checker.py` uses only Python's standard library. It verifies the two exact integer-polynomial identities supporting monotonicity, the gamma moment/kurtosis identity at multiple finite exponents, strict numerical monotonicity on a dense test grid, the Brownian endpoint \(K=6\), and the predicted small-\(\mu\) coefficient. It also samples independent exponential and gamma factors, using a fixed reproducible seed, and compares the large-\(\alpha\) radial fluctuation mean and variance to \(0\) and \(\pi^2/3\). These checks are supplementary finite numerical checks; the analytical derivation above is the proof.

Run with `python3 checker.py` from a directory containing the exact accompanying file. The code intentionally does not simulate the singular Itô SDE with an Euler step; it samples its rigorously derived free-age/gamma mixture instead.

## Relationship to prior work

Frimpong, Bresque and Roldán [1] establish the stationary Bessel density, scale collapse, passage-time and occupation-time behavior, and reset costs for this very continuum model. Their stationary density and the earlier free propagator are fundamental inputs, not new claims. Their qualitative sharpening of the bimodal density does **not** state a centered high-\(\alpha\) non-Gaussian fluctuation law, an exact universal Bessel-\(K_0\) limit, a sharp kurtosis coefficient, or a proof of global shape-to-exponent inversion. Frimpong [2] studies trajectory extrema and global times of the same reset process, including a different Gumbel limit over a long observation window; that result does not address the stationary one-sample large-\(\alpha\) layer. Boyer and Majumdar [3] study memory-dependent resetting to past sites; it does not have the independent Poisson regenerative stationary law used here. The rigorous global gamma-product monotonicity and near-frozen boundary-layer law are the proposed new combination.

## Limitations

All moments and weak limits concern a particular singular continuum Itô diffusion with symmetric nonsticky origin extension; no universality beyond that class is asserted. The high-\(\alpha\) result is a one-point stationary distributional limit, not a dynamic limit or a statement about extremal statistics. The stated calibration presupposes the model family and the unit coefficient of diffusivity; observational noise, uncertain diffusion prefactors and finite-sample inference are not analyzed. Earlier general Mellin-transform and product-Gamma results could implicitly subsume parts of the calculation, although the located model-specific sources do not explicitly formulate this inverse/asymptotic theorem. No independent scientific audit is represented.

## References

1. T. D. Frimpong, L. Bresque, E. Roldán, *Sluggish random walks with resetting: nonequilibrium aspects*, arXiv:2610.21962, first public 2026-10-15, https://arxiv.org/abs/2610.21962 .
2. T. D. Frimpong, *Extremal and global-time statistics of sluggish random walks with stochastic resetting*, arXiv:2610.34568, first public 2026-10-25, https://arxiv.org/abs/2610.34568 .
3. D. Boyer, S. N. Majumdar, *Ultra slow sub-logarithmic diffusion of a sluggish random walker subject to resetting with memory*, arXiv:2603.01149, first public 2026-03-01, https://arxiv.org/abs/2603.01149 .

# Exact one-bit optimal sampling for Brownian occupation under relative Gaussian noise

## Finding
Let \(B\) be standard Brownian motion on \([0,1]\), and let \(Q=\int_0^1\mathbf{1}_{\{B_t>0\}}\,dt\). For one predetermined observation time \(x\in(0,1]\), suppose the only recorded datum is the bit \(S=\operatorname{sgn}(B_x+\sqrt{\eta x}\,Z)\), where \(Z\sim N(0,1)\) is independent of the path, and \(0\leq\eta<\infty\) is known. This fixes the prequantization signal-to-noise ratio across possible times. An estimator may be any square-integrable function of the recorded bit.

Set \(a=(1+\eta)^{-1/2}\) and define
\[
k(a)=\frac{\arcsin a-a(1-2a^2)\sqrt{1-a^2}}{2a^3},\qquad 0<a\leq1.
\]
Then the **unique** global minimum of \(\mathbb E[(Q-\widehat Q)^2]\), over all sampling times and all admissible estimators, occurs at
\[
\boxed{x_\eta=\frac{1}{a^2+k(a)^2}}.
\]
Its optimal estimator and risk are
\[
\boxed{\widehat Q=\frac12+\frac{\arctan(a/k(a))}{\pi}S},\qquad
\boxed{R_\eta=\frac18-\frac{\arctan^2(a/k(a))}{\pi^2}}.
\]
At exact (unnoisy) sign measurements, \(\eta=0\), these specialize to
\[
x_0=\frac{16}{16+\pi^2}=0.6184864581588362\ldots,\qquad
R_0=\frac18-\left(\frac{\arctan(4/\pi)}{\pi}\right)^2=0.04201127713216669\ldots.
\]
Thus an optimally placed, noiseless **single bit** explains \(66.3909782943\ldots\%\) of the variance of the full occupation fraction. As \(\eta\to\infty\), the optimal location approaches \(9/16\), while the information gained tends to zero, with
\[
x_\eta=\frac9{16}+\frac{27}{1280(1+\eta)}+O((1+\eta)^{-2}),\qquad
\frac18-R_\eta=\frac9{16\pi^2(1+\eta)}+O((1+\eta)^{-2}).
\]

## Assumptions and scope
The observation is taken at exactly one deterministic \(x\) chosen before sampling. The recorded bit has zero comparator threshold; Gaussian noise is injected **before** quantization, with variance proportional to the Brownian marginal variance at the selected time. The noise and Brownian motion are independent. There are no other observations or auxiliary path information. The squared-error loss is unconditional over the Brownian path, sensor noise, and any estimator randomness. Randomized estimators cannot outperform the conditional expectation. The endpoint \(x=1\) is allowed. At \(x=0\), the signal is identically zero and the natural zero-information convention has risk \(1/8\); it cannot be optimal when \(\eta\) is finite. Infinite noise is discussed only as a limit, not as a uniqueness assertion.

## Proof
**1. Gaussian sign covariance.** For standard jointly Gaussian \(U,V\) with correlation \(\rho\),
\[
\mathbb E[\operatorname{sgn}(U)\operatorname{sgn}(V)]=\frac2\pi\arcsin\rho.
\]
Indeed, differentiating the bivariate positive-orthant probability with respect to the correlation, or differentiating its Gaussian density and integrating, gives derivative \(1/(2\pi\sqrt{1-\rho^2})\) for the positive-orthant probability. At \(\rho=0\) that probability is \(1/4\), establishing the displayed sign formula. The correlation between \(B_t\) and the noisy prequantization observation equals \(a\sqrt{t/x}\) for \(0<t\leq x\) and \(a\sqrt{x/t}\) for \(x\leq t\leq1\).

**2. Exact Bayes risk.** By path reflection \(\mathbb EQ=1/2\), and by the sign-covariance identity,
\[
\mathbb E[(Q-1/2)S]=\frac1\pi F(x,a),\qquad
F(x,a)=\int_0^x\arcsin\!\left(a\sqrt{t/x}\right)dt+\int_x^1\arcsin\!\left(a\sqrt{x/t}\right)dt.
\]
Since \(S\) is a fair sign, the conditional mean is exactly \(\mathbb E[Q\mid S]=1/2+S F(x,a)/\pi\). Applying the same covariance identity to the two signs within \(Q\) gives
\[
\operatorname{Var}(Q)=\frac1{2\pi}\int_0^1\!\int_0^1\arcsin\sqrt{\frac{\min(s,t)}{\max(s,t)}}\,ds\,dt=\frac18.
\]
For the last equality, symmetry and \(s=tu\) reduce the double integral to \(\int_0^1\arcsin\sqrt{u}\,du=\pi/4\). Orthogonal projection in \(L^2\) therefore yields \(R(x,a)=1/8-F(x,a)^2/\pi^2\). The integrands in \(F\) are nonnegative and \(F>0\) for \(x,a>0\), so maximizing \(F\) is equivalent to minimizing risk.

**3. Exact integration and unique global maximizer.** Elementary integration by parts, separately over \((0,x)\) and \((x,1)\), gives
\[
F(x,a)=\arcsin(a\sqrt{x})+a\sqrt{x(1-a^2x)}-a k(a)x.
\]
A useful positive representation is \(k(a)=\sqrt{1-a^2}+\int_0^1 u^2(1-a^2u^2)^{-1/2}\,du>0\), valid even at \(a=1\) as an integrable improper integral. On \(0<x<1\), differentiation gives
\[
\partial_x F=a\left(\sqrt{1/x-a^2}-k(a)\right),\quad
\partial_{xx}F=-\frac{a}{2x^2\sqrt{1/x-a^2}}<0.
\]
The first derivative tends to positive infinity as \(x\downarrow0\). At \(x=1\), its left derivative is
\[
\partial_xF(1-,a)=\frac{a\sqrt{1-a^2}-\arcsin a}{2a^2}<0,
\]
using \(\arcsin a>a\sqrt{1-a^2}\) for \(a>0\). Consequently there is precisely one maximizer on the full admissible interval, and its strictly decreasing first derivative vanishes only when \(1/x=a^2+k(a)^2\). At this \(x\), the radical and linear terms in \(F\) cancel, leaving
\[
F(x_\eta,a)=\arcsin\!\left(\frac{a}{\sqrt{a^2+k(a)^2}}\right)=\arctan\!\left(\frac{a}{k(a)}\right).
\]
Substituting this value in the Bayes estimator and risk proves the formulas.

**4. Boundary and high-noise laws.** At \(a=1\), \(k(1)=\pi/4\). Expanding at \(a=0\),
\[
k(a)=\frac43-\frac25a^2-\frac1{14}a^4+O(a^6).
\]
Substitution into the exact optimizer and exact risk gives the stated limits and corrections because \(a^2=(1+\eta)^{-1}\). These are asymptotic formulas as the finite-noise designs approach the no-information limit.

## Verification
A standalone Python 3 checker is included as `check.py`, with its sole dependency pinned in `requirements.txt`. Run `python check.py`. It checks the exact closed form against independent split numerical integration of the original Gaussian-sign covariance integral; the exact optimizer's stationarity and risk formula; endpoint inequalities; 2,400 supplemental off-optimum randomized comparisons; and the two limiting cases. The run reported residual at most \(6.5\times10^{-40}\) on the checked integrations at 40 decimal digits. These numerical comparisons are corroboration, **not** the proof of global optimality, which is the strict-concavity and boundary-sign argument above.

## Relationship to prior work
Altmeyer (2017) studies discretization error and sharp high-frequency rates for occupation integrals from **unquantized observations on prescribed grids**, not one-bit single-time Gaussian-noisy design. Ivanovs and Podolskij (2020) and Altmeyer and Le Guével (2021) analyze optimal conditional-mean estimation from full high-frequency Lévy-process samples, rather than the present one-bit finite-information choice. Fesl, Koller and Utschick (2022) analyze one-bit Gaussian channel estimation with Gaussian signal targets and pilots; the nonlinear Brownian occupation functional and its optimal observation location are not their objective. The general Gaussian orthant/arcsine identity is classical and is used as a lemma, not claimed as new. The newly derived part is the complete signal-to-noise-dependent **time design and exact occupation-risk** characterization for one recorded bit. An earlier obscure or unindexed derivation of this specific design remains possible.

## Limitations
No global optimality is claimed over nonzero comparator thresholds, alternative sensor modalities, non-Gaussian noise, absolute (time-independent) noise variance, multiple observations, or adaptive designs. The constant-relative-noise model is an assumption, not a consequence of Brownian dynamics. The formula provides optimal estimation under a specified stochastic prior, not a worst-path deterministic quadrature guarantee. The literature comparison is not a proof of historical priority. Independent verification has not been performed.

## References
1. R. Altmeyer, *Approximation of occupation time functionals*, first public 11 June 2017, arXiv:1706.03418 (v1), https://arxiv.org/abs/1706.03418 .
2. J. Ivanovs and M. Podolskij, *Optimal estimation of some random quantities of a Lévy process*, first public 8 January 2020, arXiv:2001.02517, https://arxiv.org/abs/2001.02517 .
3. R. Altmeyer and R. Le Guével, *Optimal L2-approximation of occupation and local times for symmetric stable processes*, first public 26 August 2021, arXiv:2108.11632, https://arxiv.org/abs/2108.11632 .
4. B. Fesl, M. Koller and W. Utschick, *On the Mean Square Error Optimal Estimator in One-Bit Quantized Systems*, first public 8 December 2022, arXiv:2212.04470, https://arxiv.org/abs/2212.04470 .

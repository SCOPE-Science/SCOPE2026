# A sharp location-information transition for wrapped Linnik laws

## Finding

Let the wrapped symmetric Linnik density have shape \(1<\alpha\le2\), scale \(\sigma>0\), and unknown circular location \(\mu\). Its squared Hellinger shift discrepancy, with the **non-halved** convention, is
\[
\mathcal H_{\alpha,\sigma}^2(h)=\int_{-\pi}^{\pi}
\bigl(\sqrt{f_{\alpha,\sigma}(x-h)}-\sqrt{f_{\alpha,\sigma}(x)}\bigr)^2\,dx.
\]
Define \(\beta=\alpha-1\), \(f_0=f_{\alpha,\sigma}(0)\), and the positive constants
\[
 B_{\alpha,\sigma}=\frac{\sigma^{-\alpha}}{2\Gamma(\alpha)\sin(\pi(\alpha-1)/2)},\qquad
 A_{\alpha,\sigma}=\frac{B_{\alpha,\sigma}}{2\sqrt{f_0}}.
\]
For \(0<\beta<1/2\), put
\[
 J_\beta=\int_{\mathbb R}\bigl(|u-1|^\beta-|u|^\beta\bigr)^2\,du\in(0,\infty).
\]
Then the *complete sharp small-shift classification* is
\[
\mathcal H_{\alpha,\sigma}^2(h)\sim
\begin{cases}
 A_{\alpha,\sigma}^2 J_{\alpha-1}|h|^{2\alpha-1},&1<\alpha<3/2,\\
 \tfrac12 A_{\alpha,\sigma}^2 h^2\log(1/|h|),&\alpha=3/2,\\
 \tfrac14 I_{\alpha,\sigma}h^2,&3/2<\alpha\le2,
\end{cases}
\qquad h\to0,
\]
where \(I_{\alpha,\sigma}=\int_{-\pi}^{\pi}f'_{\alpha,\sigma}(x)^2/f_{\alpha,\sigma}(x)\,dx\) is the circular location Fisher information, defined as an extended nonnegative integral. In particular, **finite location Fisher information and differentiability in quadratic mean occur if and only if \(\alpha>3/2\)**.

Moreover, with \(I_\varepsilon=\int_{\varepsilon<|x|\le\pi}f'(x)^2/f(x)\,dx\),
\[
I_\varepsilon\sim
\begin{cases}
\dfrac{8A_{\alpha,\sigma}^2(\alpha-1)^2}{3-2\alpha}\,\varepsilon^{2\alpha-3},&1<\alpha<3/2,\\
2A_{3/2,\sigma}^2\log(1/\varepsilon),&\alpha=3/2.
\end{cases}
\]
The scale \(\sigma\) changes the constants but **not** the critical shape \(3/2\).

## Assumptions and scope

The circle is \(\mathbb R/(2\pi\mathbb Z)\) with Lebesgue length measure, not normalized Haar measure; the density is normalized with respect to length. For every fixed \(1<\alpha\le2\), \(\sigma>0\), and \(\mu\in[0,2\pi)\), set
\[
f_{\alpha,\sigma,\mu}(x)=f_{\alpha,\sigma}(x-\mu),\quad
f_{\alpha,\sigma}(x)=\frac1{2\pi}\left[1+2\sum_{k=1}^{\infty}
\frac{\cos(kx)}{1+(\sigma k)^\alpha}\right].
\]
The Fourier series converges uniformly because \(\alpha>1\). All asymptotics fix \(\alpha,\sigma\) first, and take \(h\to0\) or \(\varepsilon\downarrow0\); they are not asserted uniform at the shape boundary. The location parameter alone varies; neither scale nor shape is treated as an estimated nuisance parameter. The critical case \(\alpha=1\), for which the central density may be singular, is excluded explicitly.

## Proof

**1. Genuine positive density.** For integers \(k\), the coefficient satisfies
\[
\frac1{1+(\sigma|k|)^\alpha}=\int_0^\infty e^{-t}\,e^{-t\sigma^\alpha|k|^\alpha}\,dt.
\]
The inner Fourier coefficients define a wrapped, symmetric \(\alpha\)-stable transition density. For every \(t>0\), its density is strictly positive around the entire circle: this follows by periodizing the strictly positive real stable density (at \(\alpha=2\), the Gaussian). Hence the exponential mixture is positive at every location. Uniform Fourier convergence makes \(f\) continuous, and compactness yields \(\inf_x f(x)>0\). It is even, has total integral one, and is smooth away from integer multiples of \(2\pi\).

**2. The cusp with its actual coefficient.** Write
\[
a_k=\frac1{1+(\sigma k)^\alpha}=\sigma^{-\alpha}k^{-\alpha}+r_k,
\qquad |r_k|\le\sigma^{-2\alpha}k^{-2\alpha}.
\]
Because \(\sum_{k\ge1} k|r_k|<\infty\), the cosine series of \(r_k\) has a continuous derivative that vanishes at zero; its density decrement is \(o(|x|)\) and its derivative is \(o(1)\). The principal decrement is
\[
\frac{\sigma^{-\alpha}}\pi\sum_{k\ge1}\frac{1-\cos(kx)}{k^\alpha}
\sim\frac{\sigma^{-\alpha}}\pi |x|^{\alpha-1}
\int_0^\infty\frac{1-\cos t}{t^\alpha}\,dt.
\]
The integral is \(\pi/[2\Gamma(\alpha)\sin(\pi(\alpha-1)/2)]\), by integration against the Laplace integral for \(t^{-\alpha}\) followed by the reflection identity. Thus
\[
f_0-f(x)\sim B_{\alpha,\sigma}|x|^\beta.
\]
For \(1<\alpha<2\), differentiation away from zero and the sine-series asymptotic
\[
\sum_{k\ge1}\frac{\sin(kx)}{k^{\alpha-1}}
\sim \Gamma(2-\alpha)\cos(\pi(\alpha-1)/2)\,\operatorname{sgn}(x)|x|^{\alpha-2}
\]
(which follows by Dirichlet summation and a rescaled oscillatory-integral comparison) give
\[
f'(x)\sim-\beta B_{\alpha,\sigma}\operatorname{sgn}(x)|x|^{\beta-1}.
\]
For \(\alpha=2\), use the exact identity \(\sum_{k\ge1}\sin(kx)/k=(\pi-x)/2\) for \(0<x<2\pi\); the same one-sided formula follows. Since \(f_0>0\), letting \(g=\sqrt f\) gives
\[
g(0)-g(x)\sim A_{\alpha,\sigma}|x|^\beta,\qquad
g'(x)\sim-\beta A_{\alpha,\sigma}\operatorname{sgn}(x)|x|^{\beta-1}.
\]
The estimates also provide an integrable envelope away from zero: for sufficiently small nonzero \(x\), \(|g'(x)|\le C|x|^{\beta-1}\).

**3. Subcritical Hellinger shift.** For \(0<\beta<1/2\), the change of variables \(x=hu\), the cusp above, and evenness imply on each bounded rescaled interval
\[
|h|^{-\beta}\{g(hu-h)-g(hu)\}
\longrightarrow-A\bigl(|u-1|^\beta-|u|^\beta\bigr)
\]
for positive \(h\) (negative \(h\) gives the same squared integral by symmetry). For \(|x|\ge2|h|\) in a small fixed neighborhood of zero, the mean-value theorem and the derivative envelope bound the difference by \(C|h||x|^{\beta-1}\); after rescaling its square is dominated by \(C(1+|u|)^{2\beta-2}\), integrable exactly for \(\beta<1/2\). For \(|x|\le2|h|\), the cusp provides a bounded rescaled envelope. Away from the cusp, the entire squared increment is \(O(h^2)=o(|h|^{2\beta+1})\). Dominated convergence therefore proves the first displayed constant \(A^2J_\beta\) and its positivity and finiteness.

**4. Critical logarithm.** When \(\beta=1/2\), split the circle into \(|x|\le M|h|\), \(M|h|<|x|<\delta\), and \(|x|\ge\delta\), with fixed large \(M\) and small \(\delta\). The inner and outer parts contribute respectively \(O_M(h^2)\) and \(O_\delta(h^2)\). Uniformly in the middle after first choosing \(M\) large and \(\delta\) small, \(g(x-h)-g(x)=-hg'(x)(1+o(1))\) and \(g'(x)^2\sim A^2/(4|x|)\). The two sides yield
\[
 h^2\,2\int_{M|h|}^{\delta}\frac{A^2}{4x}\,dx
\sim\frac{A^2}{2}h^2\log(1/|h|).
\]
The limiting relative error can be made arbitrarily small, proving the second case.

**5. Regular case and the exact information threshold.** For \(\beta>1/2\), the derivative envelope implies \(g\in H^1(\mathbb R/(2\pi\mathbb Z))\), so translation difference quotients converge in \(L^2\) to \(-g'\). Consequently \(\mathcal H^2(h)/h^2\to\|g'\|_2^2=I/4\). Conversely, for \(\beta\le1/2\), the local expression for \(g'\) is not square-integrable, and steps 3–4 directly show \(\mathcal H^2(h)/h^2\to\infty\). The Sobolev characterization of differentiability of translations in \(L^2\) proves the stated DQM equivalence; where it exists, the location score is \(-f'/f\). Finally, \(f'^2/f=4g'^2\sim4A^2\beta^2|x|^{2\beta-2}\), and integration on both sides of zero gives both asserted truncated-information constants. This completes all cases.

## Verification

The accompanying standalone `verify.py` requires Python 3 and `mpmath==1.3.0` (declared in `requirements.txt`); running `python verify.py` performs 106 numerical assertions across four shape values, two scales, asymptotic cusp and derivative checks, and exponential-mixture coefficient identities. The checker is independent of any external data files. These are finite consistency checks; the all-parameter theorem is established by the preceding analytic argument, **not** by finite computation.

## Relationship to prior work

SenGupta and Roy (11 September 2023) explicitly develop the wrapped Linnik characteristic-function family and estimation of its shape index; their subsequently published open-access work (online 21 November 2023) gives the Fourier density and asymptotic distribution of moment-based shape estimators. Neither investigated full-text treatment identifies the location DQM transition or the three sharp Hellinger constants. The real-line generalized Linnik asymptotic expansions by Lim and Teo (2009) address near-origin behavior of the *unwrapped* law, a useful ingredient, but they do not determine the normalized **circular location experiment's** Hellinger shift or Fisher-information boundary. A later review by Bell and Nadarajah (2024, §2.24) gives the equivalent Fourier weights under a reparameterized scale and the circular moments, but does not address location Hellinger shifts. General Hellinger-information frameworks, including Shemyakin (2023), explain the regular/nonregular distinction without these model-specific threshold and constants. Standard Fourier cusp and Sobolev translation facts are used here as tools, not claimed as novel in isolation.

## Limitations

This is a self-reviewed mathematical claim, not independently audited. The limiting statements concern small **deterministic parameter shifts**, not minimax estimation rates, confidence intervals, or an asymptotically optimal location estimator. The cutoff at \(\alpha=1\) is excluded, and no joint nuisance-parameter information matrix is asserted. Earlier equivalent results under fractional Bessel-potential, circular translation, or nonregular location-family terminology remain possible despite the specified overlap review.

## References

- A. SenGupta and M. Roy, “Circular-Statistics-Based Estimators and Tests for the Index Parameter α of Distributions for High-Volatility Financial Markets,” *Journal of Risk and Financial Management* 16 (2023), article 405, first public 11 September 2023. https://doi.org/10.3390/jrfm16090405
- A. SenGupta and M. Roy, “A characteristic function based circular distribution family and its goodness of fit: The flexible wrapped Linnik family,” *Journal of Applied Statistics* 51 (2024), 2364–2381, online 21 November 2023. https://doi.org/10.1080/02664763.2023.2283689 ; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC11389635/
- S. C. Lim and L. P. Teo, “Analytic and asymptotic properties of multivariate generalized Linnik's probability densities,” 2009. https://arxiv.org/abs/0903.5344
- A. Shemyakin, “Hellinger Information Matrix and Hellinger Priors,” *Entropy* 25 (2023), 344. https://doi.org/10.3390/e25020344
- W. Bell and S. Nadarajah, “A Review of Wrapped Distributions for Circular Data,” *Mathematics* 12 (2024), 2440, §2.24. https://doi.org/10.3390/math12162440

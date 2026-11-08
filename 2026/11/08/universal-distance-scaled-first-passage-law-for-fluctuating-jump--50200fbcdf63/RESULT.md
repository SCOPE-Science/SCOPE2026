# Universal distance-scaled first-passage law for fluctuating jump rates

## Finding

Consider the continuous-time symmetric nearest-neighbor walk on the nonnegative integers, absorbed at the origin, with a jump clock whose nonnegative rate is independently resampled at deterministic times separated by \(\tau>0\). Suppose its rate Laplace transform satisfies
\[
\mathbb E e^{-s\lambda}=1-Cs^{\alpha}+o(s^{\alpha})\quad(s\downarrow0),\qquad 0<\alpha<1,\quad C>0.
\]
The departure position is an integer \(n\ge1\), and \(T_n\) denotes physical first passage to zero. Set \(c=C\tau^{\alpha-1}\), let \(H\) be the first hitting time of zero by standard Brownian motion starting at one (variance parameter one), and independently let \(U_\alpha\) have the positive stable law
\[
\mathbb E e^{-sU_\alpha}=e^{-s^{\alpha}},\qquad s\ge0.
\]
Then, as \(n\to\infty\),
\[
\boxed{\quad n^{-2\alpha}T_n\ \Longrightarrow\ T_{\alpha,c}:=c^{-1}(H/U_\alpha)^{\alpha}.\quad}
\]
This limit is universal across all rate distributions satisfying the indicated small-Laplace-variable condition. Its complete survival curve, for every \(t>0\), is the absolutely convergent integral
\[
\boxed{\quad \Pr(T_{\alpha,c}>t)=\frac2\pi\int_0^\infty\frac{\sin k}{k}
\exp\!\left[-ct(k^2/2)^\alpha\right]\,dk.\quad}
\]
For every real \(q\) satisfying \(0<q<1/(2\alpha)\), the moments converge and have the exact value
\[
\boxed{\quad \lim_{n\to\infty}\mathbb E\left[(T_n/n^{2\alpha})^q\right]
=\mathbb E T_{\alpha,c}^q
=c^{-q}2^{-\alpha q}\frac{\Gamma(\tfrac12-\alpha q)}{\sqrt\pi}
\frac{\Gamma(1+q)}{\Gamma(1+\alpha q)}.\quad}
\]
The limiting law has the sharp higher-moment boundary: \(\mathbb E T_{\alpha,c}^q=\infty\) for all \(q\ge 1/(2\alpha)\). Its survival tail is
\[
\boxed{\quad \Pr(T_{\alpha,c}>t)\sim
\frac{\sqrt2\,\Gamma(1/(2\alpha))}{\pi\alpha}
 c^{-1/(2\alpha)}t^{-1/(2\alpha)}\quad(t\to\infty).\quad}
\]
In particular, for the Mittag--Leffler rate law with \(\mathbb E e^{-s\lambda}=(1+s^\alpha)^{-1}\), the case \(q=1\), \(\alpha<1/2\), reproduces the previously known large-distance mean constant; the complete limiting distribution and its fractional-moment spectrum are the claims here.

## Assumptions and scope

At time \(j\tau\), \(j=0,1,\ldots\), independently sample a finite nonnegative random variable \(\lambda_j\), all with the same distribution and independent of the spatial walk. During \([j\tau,(j+1)\tau)\), jumps occur at total rate \(\lambda_j\), each being \(+1\) or \(-1\) with probability \(1/2\). Stop at the first visit to zero. The first draw occurs at time zero. There is no resetting of position and no bias or boundary reflection. The small-\(s\) transform condition above is the sole tail condition; it entails \(\Pr(\lambda>0)>0\), so the integrated clock diverges almost surely and absorption occurs almost surely. All limits have fixed \(\alpha\), \(C\) and \(\tau\) with integer starting distance \(n\to\infty\). A standard Brownian motion has generator \(\frac12\partial_{xx}\).

The classification of positive moments concerns the scaled *limiting* law, and convergence of the finite-distance scaled moments only in the stated open range. Nothing is asserted about pathwise convergence of the inverses at every sample path, nor about a uniform approximation when \(\alpha\), \(C\) or \(\tau\) vary with \(n\).

## Proof

**1. Independent operational-time representation.** Let \(Y_u\) be the continuous-time simple symmetric walk with total rate one, started at \(n\), and let \(H_n\) be its hitting time of zero. Construct \(Y\) independently of the rate sequence and set \(\Lambda_t=\int_0^t\lambda_{\lfloor v/\tau\rfloor}\,dv\). The physical walk is equal in distribution to \(Y_{\Lambda_t}\), and for every \(t\ge0\),
\[
\Pr(T_n>t)=\Pr(H_n>\Lambda_t).
\]
The two random variables on the right are independent. Brownian scaling and the random-walk invariance principle, including continuity of the first-hit functional at almost every Brownian trajectory, yield
\[
H_n/n^2\Longrightarrow H,\qquad H\stackrel d=Z^{-2},\quad Z\sim N(0,1).
\]

**2. Stable clock.** Write \(t_n=n^{2\alpha}t\), \(m_n=\lfloor t_n/\tau\rfloor\), and \(\delta_n=t_n-m_n\tau\). For each fixed \(s,t>0\), independent rates give
\[
\mathbb E e^{-s\Lambda_{t_n}/n^2}
=\bigl[\widetilde g(\tau s/n^2)\bigr]^{m_n}
\widetilde g(\delta_n s/n^2)
\longrightarrow\exp[-C\tau^{\alpha-1}t s^\alpha].
\]
Thus \(\Lambda_{n^{2\alpha}t}/n^2\Longrightarrow (ct)^{1/\alpha}U_\alpha\). Joint convergence with the independently sampled \(H_n/n^2\), plus continuity of the strict comparison event (the Brownian hitting time has a continuous density), gives
\[
\lim_{n\to\infty}\Pr(T_n/n^{2\alpha}>t)
=\Pr(H>(ct)^{1/\alpha}U_\alpha).
\]
The right-hand survival function is continuous for \(t>0\), and its limit as \(t\downarrow0\) is one. By independence and positive-stable self-similarity it equals \(\Pr(c^{-1}(H/U_\alpha)^\alpha>t)\). This proves weak convergence and identifies its exact distribution, without any continuity assertion for sample-path inverse maps across jumps.

**3. Integral representation.** By the Brownian reflection principle and Fourier-sine representation, for \(u>0\),
\[
\Pr(H>u)=\operatorname{erf}(1/\sqrt{2u})
=\frac2\pi\int_0^\infty\frac{\sin k}{k}e^{-uk^2/2}\,dk.
\]
Substitute \(u=(ct)^{1/\alpha}U_\alpha\), average over \(U_\alpha\) and use its Laplace transform. The resulting integral is absolutely convergent when \(t>0\), and gives the stated full survival curve. To justify interchange, one may first use the positive half-line heat-kernel representation, or introduce an exponential regulator and then remove it by bounded convergence of the Brownian survival function.

**4. Exact moment spectrum.** For \(v<1/2\), the Gaussian representation implies
\[
\mathbb E H^{v}=2^{-v}\Gamma(\tfrac12-v)/\sqrt\pi.
\]
For any \(r>0\), the elementary gamma integral and the stable Laplace transform give
\[
\mathbb E U_\alpha^{-r}
=\frac1{\Gamma(r)}\int_0^\infty s^{r-1}e^{-s^\alpha}ds
=\frac{\Gamma(1+r/\alpha)}{\Gamma(1+r)}.
\]
Set \(v=r=\alpha q\) and multiply the independent moments to get the formula for \(0<q<1/(2\alpha)\). The Gaussian factor diverges at and above this boundary, and \(\mathbb E U_\alpha^{-r}\) remains finite, proving the sharp limiting threshold.

**5. Uniform integrability below the threshold.** A reflection argument for the total-rate-one walk shows
\[
\Pr(H_n>u)\le A\min\{1,n(1+u)^{-1/2}\},\qquad u\ge0,
\]
with an absolute constant \(A\). Indeed the half-line survivor mass is bounded by the probability of an interval of at most \(2n\) sites for a free symmetric walk, whose single-site heat kernel is at most \(A(1+u)^{-1/2}\). From the gamma identity for \((1+\Lambda_t)^{-1/2}\),
\[
\mathbb E(1+\Lambda_t)^{-1/2}
=\frac1{\sqrt\pi}\int_0^\infty s^{-1/2}e^{-s}
[\widetilde g(\tau s)]^{\lfloor t/\tau\rfloor}
\widetilde g((t-\tau\lfloor t/\tau\rfloor)s)\,ds.
\]
The assumption gives \(-\log\widetilde g(\tau s)\ge b s^\alpha\) for small positive \(s\), with \(b>0\). Outside this small interval \(\widetilde g(\tau s)\le\rho<1\). Splitting the integral shows, uniformly for sufficiently large integer \(n\) and \(v\ge1\),
\[
\Pr(T_n/n^{2\alpha}>v)\le A'v^{-1/(2\alpha)}.
\]
Here \(\lfloor n^{2\alpha}v/\tau\rfloor\) is bounded below by a fixed positive multiple of \(n^{2\alpha}v\). This uniform integrable tail bound and the already proved weak convergence imply convergence of every positive moment \(q<1/(2\alpha)\) by tail integration.

**6. Sharp tail.** Since \(\operatorname{erf}(x)\sim 2x/\sqrt\pi\) as \(x\downarrow0\), and \(\operatorname{erf}(x)\le 2x/\sqrt\pi\), dominated convergence using \(\mathbb E U_\alpha^{-1/2}<\infty\) yields
\[
\Pr(T_{\alpha,c}>t)\sim\sqrt{2/\pi}(ct)^{-1/(2\alpha)}
\frac{\Gamma(1+1/(2\alpha))}{\Gamma(3/2)}.
\]
The gamma recurrence gives the displayed coefficient.

## Verification

The supplied standalone script `check.py` checks the exact gamma duplication identity equating the \(q=1\) Mittag--Leffler specialization with the previously published mean coefficient; compares the original finite-site sine-kernel integral (with the exact independent-rate Laplace product) to the proposed limiting survival integral for several indices and distances; and checks monotonicity, normalization ranges and the large-time tail numerically. All numerical tests are finite consistency checks, not replacements for the distributional and moment arguments above. Use `python check.py`; it requires Python, SciPy and mpmath.

## Relationship to prior work

Levit and Reuveni, arXiv:2609.26925 (first public September 22, 2026), establish the exact half-line survival spectral integral, the fixed-start large-time tail \(t^{-1/(2\alpha)}\), the mean-passaging threshold \(\alpha=1/2\), and the large-start first-moment asymptotic for the Mittag--Leffler clock when \(\alpha<1/2\). These are not claimed here. In that special case, taking \(q=1\), \(C=1\), and \(c=\tau^{\alpha-1}\) recovers their known constant. The additional claim is the *complete simultaneous large-start distributional limit*, its universal sine-transform curve for general Laplace-domain tails, and its entire convergent fractional-moment spectrum. Arutkin and Reuveni, arXiv:2302.07041, provide the doubly stochastic clock model and finite-interval exit spectral framework; this is treated as methodological prior art. Uchida, Miyoshi and Washizu, arXiv:2502.20705, treat stochastic diffusivity with ergodic finite-mean regimes and hence do not imply the infinite-mean stable clock considered here. General Brownian invariance and positive-stable subordination are classical ingredients, not claims of invention.

## Limitations

The result is annealed, applies to independent nonnegative rates refreshed on a deterministic grid, symmetric nearest-neighbor motion and a single absorbing half-line target. It does not establish a quenched theorem, a varying-refresh-interval limit or a finite-distance error rate. It does not assert uniform approximations at the moment boundary. In the motivating paper the exact spectral identity already gives a formal starting point for the scaling calculation, and known stable-process invariance principles provide the principal machinery; accordingly, an earlier general theorem specialized to this exact problem could affect priority. Full numerical inference with noisy observations and finite-distance corrections are outside scope.

## References

1. B. Levit and S. Reuveni, *First Passage in the Presence of Jump Rate Fluctuations: A Transition from Infinite to Finite Mean*, arXiv:2609.26925v1 (2026), https://arxiv.org/abs/2609.26925 .
2. M. Arutkin and S. Reuveni, *Doubly stochastic continuous time random walk*, arXiv:2302.07041 (2023), https://arxiv.org/abs/2302.07041 .
3. G. Uchida, H. Miyoshi and H. Washizu, *First passage time properties of diffusion with a broad class of stochastic diffusion coefficients*, arXiv:2502.20705 (2025), https://arxiv.org/abs/2502.20705 .
4. M. M. Meerschaert and P. Straka, *Inverse Stable Subordinators*, Mathematical Modelling of Natural Phenomena 8 (2013), https://pmc.ncbi.nlm.nih.gov/articles/PMC4102015/ (standard stable-subordination background).

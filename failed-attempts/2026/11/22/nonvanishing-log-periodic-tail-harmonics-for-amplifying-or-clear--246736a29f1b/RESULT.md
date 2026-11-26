# Nonvanishing log-periodic tail harmonics for amplifying-or-clearing Poisson resets

## Finding
Consider a process \(Z(t)\ge0\) with deterministic unit upward drift between the epochs of an independent rate-one Poisson process. At each epoch apply, independently, either \(z\mapsto2z\) with probability \(p\in(0,1)\) or \(z\mapsto0\) with probability \(1-p\). Write \(\kappa=-\log_2p\) and \(h=\log2\).

There is a unique stationary law \(Z\), and
\[
\Pr(Z>x)=x^{-\kappa}(H_p(x)+o(1)),\qquad x\to\infty,
\]
where \(H_p>0\) is continuous, \(H_p(2x)=H_p(x)\), and \(H_p\) is **not constant**. For \((a;q)_\infty=\prod_{j\ge0}(1-aq^j)\) it has the explicit absolutely convergent expansion
\[
H_p(e^t)=\frac{1-p}{h}\frac{(p/2;1/2)_\infty}{(1/2;1/2)_\infty}
\sum_{\ell\in\mathbb Z}\Gamma\left(\kappa-\frac{2\pi i\ell}{h}\right)e^{2\pi i\ell t/h}.
\]
Every coefficient in this expansion is nonzero. Moreover, for real \(s>0\), \(\mathbb E Z^s<\infty\) if and only if \(p2^s<1\).

## Assumptions and scope
The Poisson epochs, Bernoulli reset decisions, and inter-epoch holding times are mutually independent. Growth has rate one and Poisson rate one, fixing units without loss for the ratio of drift and epoch intensity. All claims hold for every fixed \(p\in(0,1)\); no asymptotic in \(p\) is asserted. Stationarity is for the continuous-time process at a stationary observation time, equivalently the pre-epoch law by Poisson arrivals seeing time averages.

## Proof
**Regeneration and the stationary perpetuity.** At each clearing epoch the process returns exactly to zero, and the number of subsequent amplification epochs before the next clearing has geometric law. Since independent clearing epochs form a positive-rate thinned Poisson process, the process is regenerative and has a unique proper stationary law. The pre-epoch stationary fixed-point equation is \(Z\overset d=E+CZ'\), where \(E\sim\operatorname{Exp}(1)\), \(C\in\{0,2\}\) with probabilities \(1-p,p\), and the three terms are independent. Thus, letting \(N\) be independent with \(\Pr(N=n)=(1-p)p^n\),
\[
Z\overset d=\sum_{j=0}^N 2^j E_j,\qquad E_j\stackrel{\rm iid}\sim\operatorname{Exp}(1).
\]
At an arbitrary stationary time, the elapsed holding time has the same exponential distribution, establishing the continuous-time interpretation.

**Geometric-window limit.** Put \(q=1/2\), \(Y_n=\sum_{j=0}^nq^j E_j\), and \(Y=\sum_{j=0}^\infty q^j E_j<\infty\) almost surely. Reversing the iid summands gives \(\sum_{j=0}^n2^j E_j\overset d=2^nY_n\). Let \(S(y)=\Pr(Y>y)\). For every fixed \(z>0\),
\[
\begin{aligned}
\lim_{m\to\infty}p^{-m}\Pr(Z>2^mz)&=(1-p)\sum_{k\in\mathbb Z}p^kS(2^{-k}z)=:F_p(z),\\
H_p(z)&=z^\kappa F_p(z).
\end{aligned}
\]
To justify interchange, for \(k\ge0\) dominate each term by \(p^k\). For \(k<0\), \(Y_n\le Y\) under the natural coupling and \(\mathbb E e^{aY}=\prod_{j\ge0}(1-aq^j)^{-1}<\infty\) for \(0<a<1\); hence the terms are dominated by \(Mp^ke^{-a2^{-k}z}\). Both bounds sum uniformly for \(z\) in compact subintervals of \((0,\infty)\), proving locally uniform convergence. Index-shifting gives \(F_p(2z)=pF_p(z)\), hence \(H_p(2z)=H_p(z)\). Passing from dyadic subsequences to arbitrary \(x\to\infty\) using \(x=2^mz\) with \(z\in[1,2)\) and uniformity yields the asserted tail with additive \(o(x^{-\kappa})\). Strict positivity follows from every strictly positive summand in \(F_p\).

**Exact Mellin transform.** For finite \(n\), the hypoexponential survival function is
\[
\Pr(Y_n>y)=\sum_{j=0}^n\frac{(-1)^jq^{j(j+1)/2}}{(q;q)_j(q;q)_{n-j}}e^{-q^{-j}y}.
\]
Indeed, these are the partial-fraction coefficients of \(\prod_{j=0}^n(1+sq^j)^{-1}\) when inverted at its simple poles \(-q^{-j}\). Since \((q;q)_n\ge(q;q)_\infty>0\), the coefficients have a summable envelope proportional to \(q^{j(j+1)/2}\). Taking \(n\to\infty\) yields
\[
S(y)=\frac{1}{(q;q)_\infty}\sum_{j=0}^\infty
\frac{(-1)^jq^{j(j+1)/2}}{(q;q)_j}e^{-q^{-j}y}.
\]
For complex \(s\) with \(\Re s>0\), integrating the survival function termwise is justified by absolute convergence, and Euler's product identity gives
\[
\mathbb E Y^s=\Gamma(s+1)\frac{(q^{s+1};q)_\infty}{(q;q)_\infty}.
\]
The Euler identity used is \((a;q)_\infty=\sum_{j\ge0}(-1)^jq^{j(j-1)/2}a^j/(q;q)_j\), valid here because \(|q|<1\).

**All Fourier harmonics, including nonvanishing.** Write \(G(t)=e^{\kappa t}S(e^t)\). It is integrable over \(\mathbb R\): at \(-\infty\) it is bounded by \(e^{\kappa t}\), and at \(+\infty\) by an exponentially small tail from \(\mathbb E e^{aY}<\infty\). The previous formula implies
\[
H_p(e^t)=(1-p)\sum_{k\in\mathbb Z}G(t-kh).
\]
Its \(\ell\)-th Fourier coefficient, with \(\omega_\ell=2\pi\ell/h\), is
\[
\begin{aligned}
\widehat H_p(\ell)&=\frac{1-p}{h}\int_{\mathbb R}G(t)e^{-i\omega_\ell t}\,dt\\
&=\frac{1-p}{h}\frac{\mathbb E Y^{\kappa-i\omega_\ell}}{\kappa-i\omega_\ell}\\
&=\frac{1-p}{h}\frac{(q^{\kappa+1};q)_\infty}{(q;q)_\infty}\Gamma(\kappa-i\omega_\ell).
\end{aligned}
\]
We used \(q^{\kappa+1-i\omega_\ell}=q^{\kappa+1}\), because \(\omega_\ell h\in2\pi\mathbb Z\). Each product factor is strictly positive and the gamma function has no zeros, so **every coefficient is nonzero**. The standard vertical-line gamma bound decays exponentially as \(|\ell|\to\infty\), giving absolute and uniform Fourier convergence. Consequently \(H_p\) is real analytic as a function of \(\log x\) and strictly nonconstant.

**Moment threshold.** For every real \(s>0\), \(2^{Ns}E_N^s\le(\sum_{j=0}^N2^jE_j)^s\). Conversely, the sum is at most \(2^NY\) in distribution, with \(\mathbb EY^s<\infty\). Summing with \(\Pr(N=n)=(1-p)p^n\) shows \(\mathbb E Z^s<\infty\) exactly when \(\sum_n(p2^s)^n<\infty\).

## Verification
A standalone finite-precision independent checker, `VERIFY.py`, evaluates the hypoexponential mixture and Fourier phases and compares exact finite-mixture probabilities with the predicted asymptotics over a dyadic sequence; it also tests the periodicity identity and nonzero first Fourier coefficient. Its successful execution is supplementary to the analytical proof; no numerical sample establishes the infinite theorem. Run with Python 3 and `mpmath`: `python VERIFY.py`.

## Relationship to prior work
Palmowski and Vlasiou, arXiv:2611.14692v1, Section 2.9, derive a two-point affine-reset transform for \(C\in\{0,c\}\) under \(0\le c<1\) and a perpetuity representation; the explicit amplified \(c=2\) exponential-driving case and its oscillation spectrum are not addressed there. Kevei's arithmetic implicit-renewal theory (arXiv:1609.07339v1, especially Theorem 1 and Section 2.4) already provides general log-periodic-tail principles and examples, so the **existence of arithmetic tail oscillations is not claimed as new**. The assertion here is the exact closed gamma-product Fourier spectrum, including provable nonvanishing of every harmonic for this concrete regenerating process.

## Limitations
The result treats deterministic drift and rate-one Poisson epochs, with a two-point reset factor specifically equal to two or zero; it does not cover general Lévy drivers or arbitrary reset-amplification distributions. Historical priority for specialized exponential perpetuity identities remains a residual risk despite the inspected comparisons. The new spectral formula has not been independently audited.

## References
1. Z. Palmowski and M. Vlasiou, *Steady-state of Lévy process with general resetting: unreflected and reflected cases*, arXiv:2611.14692v1, first submitted 10 November 2026, https://arxiv.org/html/2611.14692v1 .
2. P. Kevei, *Implicit renewal theory in the arithmetic case*, arXiv:1609.07339v1, preprint first submitted 23 September 2016; *Journal of Applied Probability* 54 (2017), 732–749, https://arxiv.org/abs/1609.07339 .
3. American Mathematical Society, MSC2020 classification 60J05, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?t=60J05 .

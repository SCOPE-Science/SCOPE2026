# A Gaussian logarithmic law for consecutive-integer LCM quotients

## Finding
For integers \(k\ge2\) and \(n\ge1\), put
\[
g_k(n)=\frac{\prod_{i=0}^{k}(n+i)}{\operatorname{lcm}(n,n+1,\dots,n+k)},\qquad L_k=\operatorname{lcm}(1,\dots,k).
\]
Choose \(N_k\) uniformly from \(\{1,\dots,L_k\}\) and set \(Z_k=\log(k!/g_k(N_k))\). With \(\gamma\) Euler's constant, the following hold as \(k\to\infty\):
\[
\boxed{\quad \mathbb EZ_k=\gamma k+o(k),\qquad \operatorname{Var}(Z_k)=(2-\log(2\pi))k\log k+o(k\log k).\quad}
\]
Moreover,
\[
\boxed{\quad\frac{Z_k-\mathbb EZ_k}{\sqrt{\operatorname{Var}(Z_k)}}\ \Longrightarrow\ \mathcal N(0,1).\quad}
\]
The centering and scaling in the Gaussian assertion use the *exact* finite-\(k\) moments. The result describes an increasing-window limit; it does not claim the previously established finite-window frequency formula as new.

## Assumptions and scope
The integer \(k\) tends to infinity through all positive integers. Uniform sampling over \(L_k\) is legitimate because \(g_k\) is periodic modulo \(L_k\); the same law results from sampling over the least period. All logarithms are natural. Prime variables below refer to the prime factorization of the quotient, not independent choices of integers. For every \(n\), \(g_k(n)\mid k!\); the proof below also shows this directly.

## Proof
**Exact local valuation reduction.** Fix a prime \(p\le k\) and put \(e=\lfloor\log_p k\rfloor\). Write \(m_j(n)=\#\{0\le i\le k:p^j\mid n+i\}\). For \(j\le e\), every interval of \(k+1\) consecutive integers contains a multiple of \(p^j\); for \(j>e\), at most one. Consequently
\[
\nu_p(g_k(n))=\sum_{j=1}^{e}(m_j(n)-1),
\quad m_j(n)=\left\lfloor\frac{k+1}{p^j}\right\rfloor+I_j(n),
\]
where \(I_j(n)\) is a zero-one indicator. Thus the local exponent is between \(\sum_{j\le e}(\lfloor(k+1)/p^j\rfloor-1)\) and \(\nu_p(k!)\), establishing \(g_k(n)\mid k!\). The exponent depends only on \(n\bmod p^e\). The Chinese remainder theorem therefore makes all prime-local exponents independent for \(N_k\) uniform modulo \(L_k\).

**Large primes give independent Bernoulli variables.** If \(\sqrt k<p\le k\), then \(e=1\). Put \(r_p=(k+1)\bmod p\). Direct counting of multiples of \(p\) in a window gives
\[
\nu_p(k!)-\nu_p(g_k(N_k))\ \sim\ \operatorname{Bernoulli}(q_{p,k}),
\qquad q_{p,k}=\frac{p-1-(k\bmod p)}p
=1-\{k/p\}-1/p.
\]
In the exceptional case \(p\mid k+1\), the parameter above equals zero, as required. All these Bernoulli variables are independent. The sum of contributions from primes \(p\le\sqrt k\) obeys the *deterministic* bound
\[
0\le \sum_{p\le\sqrt k}\bigl(\nu_p(k!)-\nu_p(g_k(N_k))\bigr)\log p
\le \pi(\sqrt k)\log k=O(\sqrt k),
\]
using \(\nu_p(k!)-\nu_p(g_k(N_k))\le e\) and \(e\log p\le\log k\). This is \(o(\sqrt{k\log k})\) and \(o(k)\). Its variance is \(O(k)\).

**Prime-sum limits and the constants.** For bounded, piecewise continuous \(F:[1,\infty)\to\mathbb R\) with suitable integrable tail, the prime number theorem, after splitting into intervals \(k/(m+1)<p\le k/m\), and then truncating at a fixed \(m=M\), gives
\[
\frac1k\sum_{\sqrt k<p\le k}(\log p)F(k/p)
\longrightarrow \int_1^\infty\frac{F(x)}{x^2}\,dx,
\]
\[
\frac1{k\log k}\sum_{\sqrt k<p\le k}(\log p)^2F(k/p)
\longrightarrow \int_1^\infty\frac{F(x)}{x^2}\,dx.
\]
For the functions used below, which are piecewise polynomial in \(\{x\}\), these follow from the ordinary prime number theorem on finitely many intervals and uniform tail bounds \(O(1/M)\). The errors from replacing \(q_{p,k}\) by \(1-\{k/p\}\) and \(q_{p,k}(1-q_{p,k})\) by \(\{k/p\}(1-\{k/p\})\) are negligible: both replacements have pointwise error at most \(1/p\), and their weighted sums are \(o(k)\) and \(o(k\log k)\).

With \(F_1(x)=1-\{x\}\) and \(F_2(x)=\{x\}(1-\{x\})\), the two required integrals are
\[
\int_1^\infty\frac{1-\{x\}}{x^2}\,dx
=\sum_{m\ge1}\bigl(m^{-1}-\log(1+m^{-1})\bigr)=\gamma,
\]
\[
\int_1^\infty\frac{\{x\}(1-\{x\})}{x^2}\,dx
=\sum_{m\ge1}\bigl((2m+1)\log(1+m^{-1})-2\bigr)
=2-\log(2\pi)>0.
\]
The final equality follows by summing through \(M\), obtaining \((2M+1)\log(M+1)-2\log(M!)-2M\), and applying Stirling's formula. Independence and the small-prime bound now give the claimed exact-moment asymptotics.

**Gaussian limit.** The centered large-prime variables form a triangular array of independent variables bounded in absolute value by \(\log k\). Its variance is asymptotic to \((2-\log(2\pi))k\log k\), so the Lindeberg condition follows from \(\log k=o(\sqrt{k\log k})\). Lindeberg–Feller yields a standard Gaussian limit. The centered small-prime contribution is deterministically \(O(\sqrt k)=o(\sqrt{k\log k})\). Slutsky's theorem completes the proof with the exact mean and variance.

## Verification
`verification/verify.py` independently constructs the quotient by integer products and least common multiples, exhaustively checks each prime-local valuation distribution and its exact first two moments for \(2\le k\le10\), and compares the analytic moment formulas with direct enumeration. It performs 6,467 finite checks and prints larger-\(k\) moment ratios through \(k=10000\). The finite computations do **not** establish the prime-number-theorem asymptotics or the infinite Gaussian convergence; those rest on the displayed analytic argument.

## Relationship to prior work
Huang and Yang (arXiv:2611.15379v1, 11 November 2026) determine least periods for a broader family of multiplicative quotients, including this case; they do not state a growing-window central limit theorem or these asymptotic mean and variance constants. Hong and Qian (arXiv:0903.0530) previously developed prime-adic period formulas. A separately published 2026 exact value-frequency theorem for arithmetic-progression LCM quotients supplies a complete *finite-parameter* carry-matrix law and all finite moments. That theorem is a strong precursor: the new contribution is the explicit increasing-window asymptotics, the two universal constants, and the Gaussian theorem requiring prime-number-theorem analysis. Existing finite-frequency methods are not claimed as new.

## Limitations
No bound on convergence rate or local limit theorem is asserted. The law is for a uniform complete period, not an arbitrary shorter interval. Neither independence nor the Gaussian conclusion is claimed for a nonuniform choice of \(n\). The precise centering cannot be replaced by \(\gamma k\) within the Gaussian conclusion without a separate sufficiently strong error estimate. Earlier unindexed asymptotic treatments of the same quotient are a residual originality risk. No independent mathematical audit has been performed.

## References
- Wen-Jie Huang and Quan-Hui Yang, *On least periods of a class of arithmetic functions*, arXiv:2611.15379v1, first publicly posted 2026-11-11, https://arxiv.org/html/2611.15379v1.
- Shaofang Hong and Guoyou Qian, *The least common multiple of consecutive arithmetic progression terms*, arXiv:0903.0530, https://arxiv.org/abs/0903.0530.
- *Exact value-frequency law for consecutive arithmetic-progression LCM quotients*, public mathematical research record dated 2026-10-26, https://github.com/published-finding corpus/2026.
- Bakir Farhi and Daniel Kane, *New results on the least common multiple of consecutive integers*, arXiv:0808.1507, https://arxiv.org/abs/0808.1507.

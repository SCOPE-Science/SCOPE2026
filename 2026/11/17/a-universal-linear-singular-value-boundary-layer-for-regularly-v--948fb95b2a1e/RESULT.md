# A universal linear singular-value boundary layer for regularly varying Aluthge shifts

## Finding

Let \(\beta>0\), let \(0<t<1\), and let \((w_j)_{j\ge0}\) be a positive, nonincreasing, regularly varying sequence of index \(-\beta\): for every \(u>0\),
\[
\frac{w_{\lfloor nu\rfloor}}{w_n}\longrightarrow u^{-\beta}.
\]
On complex \(\ell^2(\mathbb N_0)\), define the compact unilateral weighted shift \(We_j=w_je_{j+1}\). With \(\Delta_t(T)=|T|^tU|T|^{1-t}\) for \(T=U|T|\), write \(W_n=\Delta_t^n(W)\), and let \(s_j\) denote the decreasing singular values. For every fixed \(R<\infty\),
\[
\boxed{\ \sup_{0\le u\le R}\left|\frac{s_{\lfloor nu\rfloor+1}(W_n)}{w_n}-(t+u)^{-\beta}\right|\longrightarrow0.\ }
\]
In particular, the operator norm has the sharp asymptotic \(\|W_n\|\sim t^{-\beta}w_n\).

This convergence determines the complete normalized high-singular-value counting law. For every fixed \(0<\theta<1\),
\[
\boxed{\ \frac1n\#\{j\ge1:s_j(W_n)>\theta\|W_n\|\}\longrightarrow t(\theta^{-1/\beta}-1).\ }
\]
For every fixed \(0<p<\infty\) with \(\beta p>1\), the precise Schatten asymptotics are
\[
\boxed{\ \|W_n\|_{\mathcal S_p}^{p}\sim n w_n^p\frac{t^{1-\beta p}}{\beta p-1},\qquad
\frac{\|W_n\|_{\mathcal S_p}^{p}}{\|W_n\|^{p}}\sim\frac{tn}{\beta p-1}.\ }
\]
Thus the effective number of leading singular values grows linearly with the iteration count and has a universal coefficient independent of the slowly varying factor. For any \(p>0\) and any finite \(n\), \(W_n\in\mathcal S_p\) if and only if \(W\in\mathcal S_p\); membership is automatic for \(\beta p>1\), impossible for \(\beta p<1\), and at \(\beta p=1\) depends on the slowly varying factor.

## Assumptions and scope

All operators act on the complex separable Hilbert space \(\ell^2(\mathbb N_0)\); \(n\) is a nonnegative integer and \(j\) is a nonnegative integer, with singular-value indexing beginning at one. The weights are strictly positive and nonincreasing, not necessarily strictly decreasing. Regular variation is assumed as the exact ratio condition above, and is equivalent to \(w_j=(j+1)^{-\beta}L(j+1)\) for a positive slowly varying sequence \(L\). The operator is compact since \(\beta>0\). All limits hold for fixed \(\beta,t,p\); the Schatten formula is asserted only when \(\beta p>1\). No differentiability or rate of variation is assumed for \(L\). When \(0<p<1\), \(\mathcal S_p\) is the usual Schatten quasi-ideal and the displayed \(p\)-th power is the sum of the \(p\)-th powers of singular values.

## Proof

**1. Exact transformed weights.** As all weights are positive, \(|W|\) is diagonal and the polar partial isometry is the ordinary unilateral shift. Thus one transform replaces \(w_j\) by \(w_j^{1-t}w_{j+1}^t\). Induction by the binomial identity shows, writing \(B_n\sim\operatorname{Bin}(n,t)\),
\[
W_ne_j=\exp\{\mathbb E\log w_{j+B_n}\}\,e_{j+1}.
\]
This binomial averaging identity is known; it is not the new contribution. Because \((w_j)\) is nonincreasing, the transformed weights are likewise nonincreasing. The displayed weights therefore give precisely the ordered nonzero singular values, including multiplicities.

**2. Uniform logarithmic scaling at linear ranks.** The regular-variation uniform convergence theorem states that for any \(0<a<b<\infty\),
\[
\sup_{a\le v\le b}\left|\log\frac{w_{\lfloor nv\rfloor}}{w_n}+\beta\log v\right|\longrightarrow0.
\]
Choose a fixed \(0<R<\infty\), and let \(E_n=\{|B_n/n-t|\le t/2\}\). A binomial Chernoff bound gives \(\mathbb P(E_n^c)\le Ce^{-cn}\). For \(0\le j\le nR\) on \(E_n\), the ratio \((j+B_n)/n\) belongs to \([t/2,R+1]\), so uniform regular variation yields
\[
\log(w_{j+B_n}/w_n)=-\beta\log((j+B_n)/n)+o(1)
\]
with the error uniform in \(j\) and in the binomial outcome on \(E_n\). Since \(B_n/n\to t\) in probability and the logarithm is uniformly Lipschitz on this compact positive interval,
\[
\sup_{0\le j\le nR}\left|\mathbb E[\log(w_{j+B_n}/w_n)\mathbf1_{E_n}]+\beta\log(t+j/n)\right|\longrightarrow0.
\]
For the exceptional event, monotonicity bounds the absolute logarithmic ratio by \(\max\{\log(w_0/w_n),\log(w_n/w_{n+\lfloor nR\rfloor+1})\}\). Regular variation gives \(\log(w_0/w_n)=O(\log n)\) and \(\log(w_n/w_{n+\lfloor nR\rfloor+1})=O(1)\), so multiplication by \(\mathbb P(E_n^c)=O(e^{-cn})\) makes this term vanish uniformly. Therefore
\[
\sup_{0\le j\le nR}\left|\log\frac{s_{j+1}(W_n)}{w_n}+\beta\log(t+j/n)\right|\longrightarrow0.
\]
Exponentiation is uniform because the logarithms stay in a bounded interval. The floor choice \(j=\lfloor nu\rfloor\) then proves the asserted singular-value profile. Taking \(j=0\) proves the operator-norm formula.

**3. Exact high-level counting limit.** Divide the profile from Step 2 by its value at \(u=0\), and note that \((1+u/t)^{-\beta}\) is continuous and strictly decreasing from one to zero. At a fixed threshold \(0<\theta<1\), its unique crossing is \(u_\theta=t(\theta^{-1/\beta}-1)\). Uniform convergence on every bounded rank interval and monotonicity of the entire singular-value sequence squeeze the number of singular values strictly above \(\theta\|W_n\|\) between \(n(u_\theta-\varepsilon)\) and \(n(u_\theta+\varepsilon)\), up to additive rounding errors. Let \(n\to\infty\) and then \(\varepsilon\downarrow0\).

**4. Full Schatten mass, including infinite tails.** For \(\beta p>1\), the local profile and Riemann summation give, for each fixed \(R>0\),
\[
\frac1{nw_n^p}\sum_{0\le j\le\lfloor Rn\rfloor}s_{j+1}(W_n)^p
\longrightarrow\int_0^R(t+u)^{-\beta p}du.
\]
It remains to control the infinitely many indices \(j>Rn\). As every binomial outcome is nonnegative and weights are nonincreasing, \(s_{j+1}(W_n)\le w_j\). Choose \(0<\varepsilon<\beta-1/p\). A Potter estimate for regularly varying sequences gives, for all sufficiently large \(n\) and all \(j\ge n\),
\[
\frac{w_j}{w_n}\le C_\varepsilon (j/n)^{-\beta+\varepsilon}.
\]
Consequently, for \(R\ge1\),
\[
\limsup_{n\to\infty}\frac1{nw_n^p}\sum_{j>Rn}s_{j+1}(W_n)^p
\le C_\varepsilon^p\int_R^\infty u^{-p(\beta-\varepsilon)}du,
\]
which tends to zero as \(R\to\infty\). Hence the limiting mass is the convergent integral
\[
\int_0^\infty(t+u)^{-\beta p}du=\frac{t^{1-\beta p}}{\beta p-1}.
\]
Dividing this result by \(\|W_n\|^p\sim t^{-\beta p}w_n^p\) gives the normalized effective-rank coefficient \(t/(\beta p-1)\).

**5. Exact ideal-membership preservation.** By monotonicity, for each fixed \(n\ge0\), every transformed weight obeys \(w_{j+n}\le s_{j+1}(W_n)\le w_j\). Summing \(p\)-th powers proves that \(W_n\in\mathcal S_p\) exactly when \(\sum_{j\ge0}w_j^p<\infty\). The standard convergence test for regularly varying sequences gives the claimed two strict index regimes; at equality the series is \(\sum (j+1)^{-1}L(j+1)^p\), whose convergence is not determined by the index alone. This completes the theorem.

## Verification

The proof establishes infinite-dimensional limits analytically; finite calculations are supplementary. The companion standalone `check.py` reproduces the binomial geometric-mean formula against direct finite transforms for power-law weights, checks monotone ordering and ideal membership comparisons, and tests the scaling and Schatten coefficients for several increasing iteration counts using elementary finite sums. A finite computation cannot substitute for the Potter-tail and concentration arguments above. The script requires only Python 3 and its standard library; run `python3 check.py`.

## Relationship to prior work

Stanković [1] proves convergence of each singular value of iterated generalized Aluthge transforms for compact operators and qualitative ideal convergence under stronger hypotheses. The exact binomial formula is known in that setting; no novelty is claimed for it. The new statement is the **uniform macroscopic rank profile** for an entire regularly varying family, the sharp integrated Schatten coefficient, the linear effective-rank asymptotic, and the full normalized counting law. The publicly accessible 2026 sharp stretched-exponential unilateral result [2] has weights \(e^{-c(j+1)^\alpha}\), which are rapidly varying rather than regularly varying with finite negative index; its \(n^{1-\alpha}\) boundary layer cannot imply the linear profile above. The bilateral stretched-exponential result [3] has a different shift domain and asymptotics. Benhida and Curto [4] describe classical one-variable Aluthge weight averaging in the course of studying two-variable shifts, but do not give a polynomial-rate spectral profile. Antezana, Massey and Stojanoff [5] study general Schatten-ideal properties, not the stated sharp regular-variation constants.

## Limitations

The monotonicity hypothesis is essential to identifying weights with **ordered** singular values; arbitrary oscillatory regularly varying weights are not covered without further work. All parameters are fixed; the theorem does not assert uniformity as \(t\to0\), \(t\to1\), \(p\to1/\beta\), or \(\beta\to0\). At the critical ideal exponent only the exact membership-preservation statement is proved, not a universal Schatten asymptotic. The first source [1] was available for comparison at abstract level, not full text, leaving residual possibility of a more general quantitative theorem not reflected by the abstract. Equivalence with older regular-variation smoothing theorems is also a priority risk. Independent audit has not been performed.

## References

1. H. Stanković, *Singular values of iterated Aluthge transforms of compact operators*, arXiv:2611.07728, first publicly posted 2026-11-05. https://arxiv.org/abs/2611.07728
2. *A sharp singular-value boundary layer for stretched-exponential Aluthge iterates*, published research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-singular-value-boundary-layer-for-stretched-exponential--8ed808d0b606
3. *Two-scale Aluthge asymptotics of compact bilateral stretched-exponential shifts*, published research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-two-scale-aluthge-asymptotics-of-compact-bilateral-stretched-exp--304047bdec1c
4. C. Benhida and R. E. Curto, *Iterates of the Spherical Aluthge Transform of 2-Variable Weighted Shifts*, accessible preprint, section 2.2 on one-variable shifts. https://arxiv.org/abs/1706.03285
5. J. Antezana, P. Massey and D. Stojanoff, *\(\lambda\)-Aluthge transforms and Schatten ideals*, Linear Algebra and Its Applications 405 (2005), 177–199. https://doi.org/10.1016/j.laa.2005.03.016

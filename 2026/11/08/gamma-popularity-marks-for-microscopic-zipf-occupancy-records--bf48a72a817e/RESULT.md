# Gamma popularity marks for microscopic Zipf occupancy records

## Finding

**Theorem (conditional marked Poisson limit, with a compact-test rate).** Fix \(a>1\), \(\gamma=1/a\), \(c=1/\zeta(a)\), \(\lambda>0\), and a positive integer \(R\). Let \(X_1,X_2,\ldots\) be independent with \(\Pr(X_k=j)=p_j=cj^{-a}\) for \(j\ge1\). Put \(m_n=\lfloor\lambda n^{1-\gamma}\rfloor\) and \(\mathcal F_n=\sigma(X_1,\ldots,X_n)\). For each \(1\le r\le R\) and label \(j\), place a point \((r,j/n^\gamma,k/m_n)\) if the \(r\)-th occurrence of label \(j\) in the *entire* sequence happens at draw \(n+k\), with \(1\le k\le m_n\). Let \(\Xi_n\) be the resulting point measure on \(E=\{1,\ldots,R\}\times(0,\infty)\times[0,1]\).

Conditionally on \(\mathcal F_n\), the laws of \(\Xi_n\) converge **in probability** to the law of a Poisson point process with nonrandom intensity
\[
\nu(\{r\}\times dx\times dt)=\frac{\lambda c^r}{(r-1)!}\,x^{-ar}\exp(-cx^{-a})\,dx\,dt.
\]
For every nonnegative bounded function \(f:E\to\mathbb R\) that is Lipschitz in rank and time and vanishes off some rank interval \([\varepsilon,L]\subset(0,\infty)\), there is a finite constant \(C_f\) such that
\[
\mathbb E\left|\mathbb E\bigl[e^{-\Xi_n(f)}\mid\mathcal F_n\bigr]-\exp\left\{-\int_E(1-e^{-f})\,d\nu\right\}\right|
\le C_f\bigl(n^{-\gamma/2}+n^{-(1-\gamma)}\bigr).
\]
The number of \(r\)-records converges jointly to independent Poisson variables with means
\[
\Lambda_r=\frac{\lambda\gamma c^\gamma\Gamma(r-\gamma)}{(r-1)!}.
\]
Within each limiting \(r\)-class, the time marks are independent uniform variables on \([0,1]\); the transformed popularity marks \(Y=cX^{-a}\), where \(X\) denotes the positive rank coordinate, are independent of time and have the Gamma distribution with shape \(r-\gamma\) and unit rate. Different classes are independent.

## Assumptions and scope

All probabilities are fixed, deterministic, exactly Zipf, and independent across draws; the exponent \(a\), window coefficient \(\lambda\), and maximal multiplicity \(R\) are fixed as \(n\to\infty\). The conditional law is taken after observing the entire first \(n\) draws (not merely their number of distinct labels). Point-process convergence uses the usual vague topology on \(E\), followed by tightness of the total number of points; it does not assert total-variation convergence to a continuously marked law. The quantitative estimate concerns the stated compact-rank Lipschitz tests, not arbitrary unbounded marks or test functions.

## Proof

Write \(N_j(n)=\sum_{k\le n}\mathbf1\{X_k=j\}\), \(x_{n,j}=j/n^\gamma\), and \(y_{n,j}=np_j=cx_{n,j}^{-a}\). For \(r\le R\), set
\[
V_{n,r}=m_n\sum_{j\ge1}p_j\mathbf1\{N_j(n)=r-1\}\,\delta_{x_{n,j}}.
\]
We first prove that these random measures converge in probability to \(\nu_r(dx)=\lambda c^r x^{-ar}e^{-cx^{-a}}dx/(r-1)!\).

**1. Mean measures and conditional intensity concentration.** On any fixed compact \([\varepsilon,L]\subset(0,\infty)\), \(p_j\le C/n\) and the exact binomial identity gives, uniformly for \(x_{n,j}\) in the compact,
\[
\Pr\{N_j(n)=r-1\}=\binom n{r-1}p_j^{r-1}(1-p_j)^{n-r+1}
=\frac{e^{-y_{n,j}}y_{n,j}^{r-1}}{(r-1)!}+O(n^{-1}).
\]
Since \(m_np_j=(\lambda+O(n^{\gamma-1}))c n^{-\gamma}x_{n,j}^{-a}\), compactly supported Riemann sums show that \(\mathbb EV_{n,r}(h)\to\int h\,d\nu_r\) for every bounded continuous compactly supported \(h\). If \(h\) is Lipschitz, the mean error is \(O(n^{-\gamma}+n^{\gamma-1})\).

For distinct labels \(i\ne j\), and \(k,\ell\in\{0,\ldots,R-1\}\), the exact multinomial probability is
\[
\Pr\{N_i(n)=k,N_j(n)=\ell\}=\frac{(n)_{k+\ell}}{k!\ell!}p_i^kp_j^\ell(1-p_i-p_j)^{n-k-\ell}.
\]
On a compact rank interval this differs from the product of the two binomial probabilities by \(O(n^{-1})\), uniformly in \(i,j\), including when \(k=0\) or \(\ell=0\). There are \(O(n^\gamma)\) relevant labels and each coefficient \(m_np_j\) is \(O(n^{-\gamma})\). Summing diagonal terms and the displayed off-diagonal covariance gives
\[
\operatorname{Var}\bigl(V_{n,r}(h)\bigr)
=O(n^{-\gamma}+n^{-1})=O(n^{-\gamma}).
\]
The same bound holds for any fixed bounded test involving several classes. Thus \(\mathbb E|V_{n,r}(h)-\nu_r(h)|=O(n^{-\gamma/2}+n^{\gamma-1})\) for compact Lipschitz \(h\).

For completeness, the estimates also control mass outside compacts. For sufficiently large \(n\) and \(0\le k\le R-1\),
\[
\Pr\{N_j(n)=k\}\le\frac{(np_j)^k}{k!}e^{-np_j/2}.
\]
Consequently \(m_np_j\Pr\{N_j(n)=r-1\}\le C n^{-\gamma}y_{n,j}^{r}e^{-y_{n,j}/2}\). The corresponding rank-coordinate function is integrable both at zero (exponential cutoff) and infinity (because \(ar>1\)). Dominated rank-Riemann sums imply \(\sup_n\mathbb EV_{n,r}((0,\infty))<\infty\) and
\[
\lim_{\varepsilon\downarrow0,\,L\uparrow\infty}\limsup_n
\mathbb EV_{n,r}\bigl((0,\varepsilon)\cup(L,\infty)\bigr)=0.
\]
In particular, the full \(V_{n,r}\) have asymptotically deterministic finite masses.

**2. One-hit coupling.** Construct a surrogate marked measure by recording a point \((r,x_{n,j},k/m_n)\) *whenever* a future draw at position \(n+k\) hits a label \(j\) for which \(N_j(n)=r-1\). The surrogate and the genuine \(\Xi_n\) agree unless some label with \(N_j(n)<R\) is hit at least twice in the future window. A union bound over future draw pairs yields
\[
\Pr\{\Xi_n\ne\widetilde\Xi_n\}
\le\binom{m_n}{2}\sum_{j\ge1}p_j^2\Pr\{N_j(n)<R\}.
\]
The last sum is \(O(n^{\gamma-2})\) by the preceding binomial bound and the same integrable rank-Riemann sum; hence the mismatch probability is \(O(n^{-\gamma})\). For a compact rank interval, the simpler unconditional bound \(\binom{m_n}{2}\sum_{\varepsilon\le x_{n,j}\le L}p_j^2=O(n^{-\gamma})\) suffices.

**3. Conditional Laplace functionals.** Set \(g=1-e^{-f}\). Given \(\mathcal F_n\), future symbols are independent, so the surrogate Laplace functional is exactly
\[
\mathbb E[e^{-\widetilde\Xi_n(f)}\mid\mathcal F_n]
=\prod_{k=1}^{m_n}\left(1-\sum_{r=1}^R\sum_{j:N_j(n)=r-1}p_jg(r,x_{n,j},k/m_n)\right).
\]
For compact-rank support, each inner sum is bounded deterministically by \(C n^{\gamma-1}\), so the logarithm differs from minus the corresponding sum by \(O(m_n n^{2\gamma-2})=O(n^{\gamma-1})\). If \(f\) is Lipschitz in time, replacing \(m_n^{-1}\sum_k g(r,x,k/m_n)\) by \(\int_0^1g(r,x,t)dt\) has error \(O(m_n^{-1})\) after integration against \(V_{n,r}\). Part 1 then replaces these measures by \(\nu_r\), with expected error \(O(n^{-\gamma/2}+n^{\gamma-1})\). Exponentiation on the nonnegative half-line is 1-Lipschitz; the coupling error on the test support is \(O(n^{-\gamma})\). These estimates give exactly the quantitative Laplace bound in the finding.

Compact-rank continuous tests follow by uniform approximation with Lipschitz tests. The tail estimate in Part 1 and the coupling imply tightness of the total number of actual records and vanishing probabilities of records at exceptionally small or large scaled ranks. Conditional Laplace convergence in probability therefore proves the asserted finite-intensity conditional Poisson point-process limit, with independent class restrictions.

**4. Identification of the marks.** Under \(y=cx^{-a}\), we have \(|dx|=\gamma c^\gamma y^{-1-\gamma}dy\), hence
\[
\nu_r(dx\,dt)=\frac{\lambda\gamma c^\gamma}{(r-1)!}
y^{r-1-\gamma}e^{-y}\,dy\,dt.
\]
Integrating gives \(\Lambda_r\), and normalization gives \(Y\sim\operatorname{Gamma}(r-\gamma,1)\), independent of uniform time. This concludes the proof.

## Verification

The accompanying `CHECK.py` verifies exact finite multinomial occupancy identities against explicit four-category enumeration, checks a finite-window one-hit inequality using rational arithmetic, and compares numerical intensity and Gamma-transform integrals with their closed forms. It executes entirely with the Python standard library. These finite/numerical tests do **not** establish the asymptotic theorem; Parts 1–4 give the mathematical proof. Run with `python3 CHECK.py`.

## Relationship to prior work

Derbazi, Gnedin and Marynych (2023, arXiv:2308.01739), especially Proposition 5 and Theorems 2–3, already establish unmarked short-window Poisson \(r\)-record processes, asymptotic independence of record classes, and a conditional (quenched) Poisson statement in the Poissonized setting. Those results and their record-intensity asymptotics are **not claimed** here. The new object retains the normalized label/rank of each record and establishes the explicit joint rank-time intensity, the \(r\)-dependent Gamma law of its label popularity, and the quantitative conditional compact-test Laplace bound for a fixed-size future window.

Abebe, Chebunin and Kovalevskii (2026, arXiv:2602.13938) develop large-sample Gaussian functional limits for urn counts indexed by subsets and unions of intervals. Their object neither resolves the microscopic post-history rank marks nor supplies a Gamma popularity composition law. The present result uses the same classical infinite-urn setting but addresses a different observable and scaling.

## Limitations

The theorem requires exact deterministic Zipf probabilities, fixed \(R\), and \(a>1\). It does not cover arbitrary regularly varying weights with oscillating slowly varying factors, random normalized weights, dependent draws, a growing multiplicity cutoff, or a time interval of macroscopic length. Total variation to a continuous-rank point-process law is impossible at finite \(n\) because its rank marks are discrete. The priority comparison with the full range of older marked-occupancy literature remains provisional; the theorem should not be described as the first record-process Poisson limit or the first quenched record law.

## References

1. B. Abebe, M. Chebunin and A. Kovalevskii (2026), *Limit theorems for a class of random outer measures in infinite urn schemes*, arXiv:2602.13938, https://arxiv.org/abs/2602.13938 (first public release 2026-02-15).
2. Z. Derbazi, A. Gnedin and A. Marynych (2023), *Records in the Infinite Occupancy Scheme*, arXiv:2308.01739, https://arxiv.org/abs/2308.01739; especially Sections 5, 7 and 8.
3. S. Karlin (1967), *Central limit theorems for certain infinite urn schemes*, Journal of Mathematics and Mechanics 17, 373–401; classical infinite-urn regular variation.

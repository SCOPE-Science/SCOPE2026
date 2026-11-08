# Second-order recoding fluctuations distinguish identical Brownian limits

## Finding
Fix an integer \(d\ge1\) and \(\lambda>0\). Independently recode a fair random walk by selecting each inclusion-induced Boolean monomial of **exact degree** \(d\) at level \(n\) with probability \(p_n=\min\{\lambda/n^d,1/2\}\). Put

\[
\rho=\exp\!\left(-\frac{\lambda}{2^{d-1}d!}\right),\qquad
 a=\frac{\rho\lambda}{2^{d-1}(d-1)!}=-d\rho\log\rho.
\]

The recoded pair of walks has, for almost every coefficient environment, a joint Brownian functional limit with correlation \(\rho\). Yet its empirical predictable cross-covariation \(H_N\) has the **second-order annealed Gaussian limit**

\[
\boxed{\left(\frac{X_N}{\sqrt N},\frac{H_N-N\rho}{\sqrt N}\right)
\ \Longrightarrow\ N_2\!\left(0,
\begin{pmatrix}1&a\\a&1-\rho^2+2a^2\end{pmatrix}\right).}
\]

Moreover,
\[
\lim_{N\to\infty}\frac{\operatorname{Var}(H_N)}{N}=1-\rho^2+2a^2,
\qquad
\lim_{N\to\infty}\frac{\operatorname{Cov}(X_N,H_N)}{N}=a.
\]

**Consequently, at any fixed correlation \(\rho\in(0,1)\), choosing different degrees \(d\) and adjusting \(\lambda\) to keep \(\rho\) fixed gives the same first-order two-walk Brownian limit but different second-order cross-covariation variances \(1-\rho^2+2d^2\rho^2(\log\rho)^2\).** This distinguishes sparsity mechanisms that are invisible to the Brownian covariance.

## Assumptions and scope
Let \(\xi_1,\xi_2,\ldots\) be independent fair signs. Independently let \(\beta_{n,K}\), for every \(n\ge d\) and \(K\subseteq\{1,\ldots,n\}\) with \(|K|=d\), be mutually independent \(\operatorname{Bernoulli}(p_n)\) variables; all other inclusion-induced coefficients are zero. Define \(A_n=\{i\le n:\xi_i=-1\}\), \(S_n=|A_n|\), \(\zeta_0=1\), and

\[
\zeta_n=(-1)^{\sum_{\substack{K\subseteq A_n\\|K|=d}}\beta_{n,K}},\qquad
X_N=\sum_{i=1}^{N}\xi_i,\quad
Y_N=\sum_{i=1}^{N}\zeta_{i-1}\xi_i,\quad
H_N=\sum_{n=1}^{N}\zeta_n.
\]

Set \(\zeta_n=1\) when \(n<d\). The coefficient array is an independent environment. For every fixed environment, \(X\) and \(Y\) individually have independent fair increments and their predictable cross-covariation through time \(N\) is \(H_{N-1}+1\). The shift by one is bounded and immaterial to the fluctuations. The **second-order** distribution and moments above are **annealed**, averaging over both increments and coefficients; they are not asserted conditionally on an arbitrary fixed environment. The first-order functional statement is quenched in the environment.

## Proof
**1. Exact conditional mean.** Given the entire increment sequence, the \(\binom{S_n}{d}\) visible degree-\(d\) coefficients are independent. Therefore

\[
m_n:=\mathbb E_\beta[\zeta_n\mid\xi]
=(1-2p_n)^{\binom{S_n}{d}}.
\]

Since \(S_n/n\to1/2\) almost surely and \(p_n=\lambda n^{-d}\) for sufficiently large \(n\), one has \(m_n\to\rho\) almost surely. Conditional on \(\xi\), the centered signs \(U_n=\zeta_n-m_n\) are independent across \(n\), mean zero and bounded by two. Hoeffding--Borel--Cantelli implies \(N^{-1}\sum_{n\le N}U_n\to0\) jointly almost surely, so \(N^{-1}\sum_{n\le N}\zeta_n\to\rho\). By Fubini, this also holds almost surely for the increment law in almost every fixed coefficient environment. The predictable covariance of the martingale \((X,Y)\) consequently tends to the matrix with off-diagonal \(\rho\); bounded jumps give the asserted quenched Brownian functional limit by the martingale functional central limit theorem.

**2. Linearization of the quenched sign expectation.** Define \(f(x)=\exp(-2\lambda x^d/d!)\). The elementary polynomial expansion of \(\binom{s}{d}\) and the logarithmic expansion of \(\log(1-2\lambda n^{-d})\) give, uniformly for \(0\le s\le n\),

\[
(1-2\lambda n^{-d})^{\binom{s}{d}}=f(s/n)+O(n^{-1})
\]

for large \(n\). Taylor expansion around \(1/2\) and \(S_n-n/2=-X_n/2\) then yield

\[
m_n-\rho=a\frac{X_n}{n}+R_n,
\qquad \|R_n\|_2=O(n^{-1}),
\]

because \(\mathbb E(S_n/n-1/2)^4=O(n^{-2})\). Thus \(N^{-1/2}\sum_{n\le N}R_n\to0\) in \(L^2\): the numerator has \(L^2\) norm at most \(O(\log N)\).

**3. The history-dependent Gaussian term.** Introduce

\[
Q_N=\sum_{n=1}^{N}\frac{X_n}{n}
=\sum_{j=1}^{N}w_{N,j}\xi_j,
\qquad w_{N,j}=\sum_{n=j}^{N}\frac1n.
\]

Double summation gives the exact identities

\[
\sum_{j=1}^{N}w_{N,j}=N,\qquad
\sum_{j=1}^{N}w_{N,j}^{2}=2N-h_N,\qquad
h_N=\sum_{j=1}^{N}\frac1j.
\]

In particular the normalized second sum tends to \(2\).

Since \(\max_j|w_{N,j}|=O(\log N)=o(\sqrt N)\), the multivariate independent-increment Lindeberg theorem gives

\[
\left(\frac{X_N}{\sqrt N},\frac{Q_N}{\sqrt N}\right)
\Longrightarrow N_2\!\left(0,\begin{pmatrix}1&1\\1&2\end{pmatrix}\right).
\]

**4. Independent coefficient noise.** Conditional on the entire \(\xi\)-sequence, \(U_n\) are independent centered bounded variables with variances \(1-m_n^2\). Since \(m_n\to\rho\) almost surely, the conditional Lindeberg CLT implies that \(N^{-1/2}\sum_{n\le N}U_n\) tends to a centered normal of variance \(1-\rho^2\), with conditional characteristic functions converging almost surely to a nonrandom limit. Consequently this Gaussian component is asymptotically independent of every \(\xi\)-measurable statistic, in particular of \((X_N,Q_N)/\sqrt N\). Combining Steps 2–4 with

\[
H_N-N\rho=\sum_{n=1}^{N}U_n+aQ_N+\sum_{n=1}^{N}R_n
\]

proves the displayed joint limit. Orthogonality \(\mathbb E[U_nF(\xi)]=0\), the conditional variance identity, and the \(L^2\)-small remainder further give the stated variance/covariance limits. Substituting \(a=-d\rho\log\rho\) proves the distinction at fixed \(\rho\).

## Verification
The standalone `verify.py` checks exact conditional parity identities, multidegree convolution checks and subset counting, and now checks the harmonic weight covariance identities and second-order limiting constants; it uses standard-library rational arithmetic where possible. The assertions test finite formulas and limiting numerical examples, not the analytic central limit theorems. The proof above independently establishes all infinite statements.

## Relationship to prior work
Hamza and Tournier, *Are random random walks normal?* (arXiv:2610.01658v1, first public 2026-10-01), provide the inclusion-induced representation, Brownian-normality criteria, a zero-correlation theorem under uniformly elliptic coefficients, and a general row-independent coefficient comparison (Proposition 10). Our critically thinned degree-\(d\) model lies within the broad row-independence framework but violates the full uniform-ellipticity hypothesis; the first-order correlation is a special calculable application of their general approach. **The contribution here is instead the second-order joint CLT for the empirical cross-covariation and the explicit degree-dependent variance inflation at fixed Brownian correlation**, neither given by their first-order criteria nor Proposition 10.

Collevecchio, Hamza, Shi and Williams, *Limit theorems and ergodicity for general bootstrap random walks* (arXiv:2010.16000; published 2022), establish general Brownian criteria for deterministic recodings. Their results concern first-order invariance principles and do not determine the second-order fluctuation law of the predictable covariance under a sparse random coefficient ensemble.

## Limitations
The degree \(d\) is fixed, the activation intensity is exactly \(p_n=\min\{\lambda/n^d,1/2\}\), and coefficient rows and within-row subsets are independent. The second-order limit is annealed, not asserted to be quenched, and it does not describe non-Gaussian higher-order fluctuations or the rate of functional convergence. No definitive priority assertion over inaccessible general literature is made.

## References
1. K. Hamza and L. Tournier, *Are random random walks normal?*, arXiv:2610.01658v1, first posted 2026-10-01, https://arxiv.org/html/2610.01658v1.
2. A. Collevecchio, K. Hamza, M. Shi and R. J. Williams, *Limit theorems and ergodicity for general bootstrap random walks*, arXiv:2010.16000, first posted 2020-10-30, https://arxiv.org/abs/2010.16000; Electronic Journal of Probability 27 (2022), no. 92, https://doi.org/10.1214/22-EJP818.

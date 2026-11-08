# The square-exponential transition for Knuth cycle counts of multiset permutations

## Finding

Fix real \(c>0\) and \(\beta>1\). For each integer \(j\ge1\), set
\[
n_j=\lceil \exp(cj^\beta)\rceil,
\qquad N_j=\sum_{h=1}^{j}n_h,
\qquad a_j=\frac{n_j}{N_{j-1}}\quad(j\ge2).
\]
Choose uniformly one word containing exactly \(n_j\) occurrences of symbol \(j\), for each \(1\le j\le t\). Let \(K_t\) be the number of cycles in the **canonical Knuth factorization** (not the number of cyclic vertices of the associated functional digraph), and let \(\mu_t=\mathbb E K_t\).

**Theorem (sharp three-regime transition).** For \(1<\beta<2\),
\[
\operatorname{Var}(K_t)\sim
\frac{a_t^2t^{2-\beta}}{2c\beta(\beta-1)},
\qquad
\frac{K_t-\mu_t}{a_t\sqrt{t^{2-\beta}/[2c\beta(\beta-1)]}}
\Longrightarrow\operatorname{N}(0,1).
\]
At \(\beta=2\), let \(q=e^{-2c}\) and let \(E_0,E_1,\ldots\) be independent mean-one exponential random variables. Then
\[
\frac{K_t}{a_t}\Longrightarrow
S_c=\sum_{k=0}^\infty q^kE_k,
\quad
\mathbb E e^{-sS_c}=\prod_{k=0}^\infty\frac{1}{1+s q^k}
\quad(s\ge0).
\]
In particular \(\mathbb ES_c=(1-q)^{-1}\) and \(\operatorname{Var}S_c=(1-q^2)^{-1}\). For \(\beta>2\),
\[
\frac{K_t}{a_t}\Longrightarrow E_0\sim\operatorname{Exp}(1).
\]
In both non-Gaussian regimes the convergence holds for **every fixed positive absolute moment**. At the integral critical example \(c=\log 2\), \(\beta=2\), the multiplicities are \(n_j=2^{j^2}\) and the limiting mean and variance are respectively \(4/3\) and \(16/15\).

## Assumptions and scope

All multiplicities are positive integers and the sampling distribution is **uniform over multiset words** (the cycle-weight parameter of the multiset restaurant process is \(\theta=1\)). The constant \(c\) and power \(\beta\) do not depend on \(t\); \(\beta\le1\), variable cycle-weight, growing or random parameters, and joint cycle-length statistics are not asserted. The finite initial increment is \(X_1=n_1\). The exact finite mean is
\[
\mu_t=\sum_{j=1}^t\frac{n_j}{N_{j-1}+1},\qquad N_0=0.
\]
The results identify the distribution of the *number* of Knuth cycles, not the cycle sizes or the ordinary symmetric-group cycle decomposition of a multiset word.

## Proof

**1. Independent increments (established input).** Stark [1], Section 4, proves that \(K_t=\sum_{j=1}^tX_j\) for independent random variables. For \(j\ge2\), writing \(m=N_{j-1}\) and \(n=n_j\),
\[
\Pr(X_j=k)=\frac{\binom{m-1+n-k}{n-k}}{\binom{m+n}{n}},
\quad 0\le k\le n,
\]
while \(X_1=n_1\) deterministically. Equivalently, \(X_j\) counts failures before the first success in a uniformly randomized list of \(n\) failures and \(m\) successes. In particular,
\[
\mathbb EX_j=\frac{n}{m+1},\qquad
\operatorname{Var}(X_j)=\frac{n(m+n+1)m}{(m+1)^2(m+2)}.
\]
These exact identities are credited to [1].

**2. The exponential increment lemma.** Suppose \(m\to\infty\) and \(a=n/m\to\infty\). Then
\[
\Pr(X\ge k)=\prod_{h=0}^{k-1}\frac{n-h}{m+n-h}
\le\left(\frac{n}{m+n}\right)^k
\le e^{-k/(1+a)}.
\]
For each fixed \(x\ge0\), take \(k=\lfloor ax\rfloor\). The logarithm of the product equals \(-x+o(1)\): at \(h\le O(a)\), the depletion correction has total magnitude \(O(k^2m/n^2)=O(1/m)\), while \(k\log[n/(m+n)]\to-x\). Therefore \(X/a\Rightarrow\operatorname{Exp}(1)\). The exponential tail bound implies, uniformly for sufficiently large \(m,a\), \(\mathbb E(X/a)^r\le C_r\) for every fixed real \(r>0\); all positive moments converge. The same tail bound gives \(\mathbb E|X-\mathbb EX|^3\le C a^3\). The exact formula above also yields \(\operatorname{Var}(X)\sim a^2\).

**3. Deterministic growth and endpoint weights.** Define \(g_j=c(j^\beta-(j-1)^\beta)\). Because \(\beta>1\), \(g_j\to\infty\), and a geometric-last-term bound gives
\[
\frac{N_{j-1}}{n_{j-1}}\longrightarrow1,
\qquad
\log a_j=g_j+o(1).
\]
Indeed the ratio of the earlier-multiplicity sum to \(n_{j-1}\) is at most \((j-2)\exp[-c((j-1)^\beta-(j-2)^\beta)]+o(1)\). The rounding error in \(n_j\) is negligible. The gap between neighboring growth exponents is
\[
g_j-g_{j-1}\sim c\beta(\beta-1)j^{\beta-2}.
\]
For \(1<\beta<2\), set \(L_t=t^{2-\beta}\). The moving-endpoint relation
\[
\frac{a_{t-\lfloor uL_t\rfloor}^2}{a_t^2}
\longrightarrow e^{-2c\beta(\beta-1)u}
\quad (u\ge0)
\]
is uniform on bounded \(u\)-intervals. The contribution of \(k\gg L_t\) is negligible: on \(0\le k\le t/2\) an exponentially decaying majorant \(\exp[-Ck/L_t]\) follows from the mean-value theorem, and on \(k>t/2\) there is an additional exponentially small factor in \(t^{\beta-1}\). Hence a Riemann-sum argument gives
\[
\sum_{j=2}^ta_j^2
\sim a_t^2L_t\int_0^\infty e^{-2c\beta(\beta-1)u}\,du
=\frac{a_t^2t^{2-\beta}}{2c\beta(\beta-1)}.
\]
The increment variance asymptotic is uniform across the moving endpoint and the finitely many early terms are negligible; consequently the same relation holds for \(V_t=\operatorname{Var}(K_t)\).

For \(\beta=2\), \(g_j=c(2j-1)\), so for each fixed \(k\ge0\), \(a_{t-k}/a_t\to q^k\), where \(q=e^{-2c}\). Moreover there are constants \(A<\infty\) and \(q_0\in(q,1)\) with \(a_{t-k}/a_t\le A q_0^k\) for every sufficiently large \(t\) and all \(0\le k\le t-2\). This follows from \(\log a_j=g_j+o(1)\) and a uniform adjustment for finitely many initial indices. For \(\beta>2\), the growth gap diverges and
\[
\sum_{j=2}^{t-1}\frac{a_j}{a_t}
\le O(t)\exp[-(g_t-g_{t-1})]\longrightarrow0.
\]

**4. Gaussian regime.** For \(1<\beta<2\), the variance identity from step 1 and the endpoint estimate imply \(V_t\sim a_t^2L_t/[2c\beta(\beta-1)]\). The moment bound in step 2, eventual monotonicity of \(a_j\), and the negligible finite prefix yield
\[
\frac{\sum_{j=2}^t\mathbb E|X_j-\mathbb EX_j|^3}{V_t^{3/2}}
\le O\left(\frac{a_t}{\sqrt{V_t}}\right)
=O(L_t^{-1/2})\longrightarrow0.
\]
Lyapunov's triangular-array theorem applies to the independent row \((X_1,\ldots,X_t)\); \(X_1\) is deterministic. This proves the asserted centered normal limit.

**5. Non-Gaussian regimes.** At \(\beta=2\), step 2 and the fixed-lag ratios imply joint convergence of each finite vector \((X_t/a_t,\ldots,X_{t-K}/a_t)\) to \((E_0,qE_1,\ldots,q^KE_K)\). The independent limiting exponentials follow from independence of the original increments. For any fixed \(r\ge1\), Minkowski's inequality and the geometric weight majorant imply
\[
\sup_{t\text{ sufficiently large}}
\left\|\sum_{j=2}^{t-K-1}\frac{X_j}{a_t}\right\|_{L^r}
\le C_r\sum_{k>K}q_0^k\longrightarrow0.
\]
The deterministic \(X_1/a_t\) vanishes. Finite-block convergence plus uniform tail control yields the claimed distributional and all positive moment limits (use any integer moment larger than a desired fractional exponent). Absolute convergence of \(S_c\) holds in every \(L^r\), and multiplying independent exponential Laplace transforms gives the infinite product.

For \(\beta>2\), step 3 and the moment bound give \(\|\sum_{j<t}X_j/a_t\|_{L^r}\to0\) for each fixed \(r\ge1\). Step 2 yields \(X_t/a_t\Rightarrow E_0\), with convergence of every positive moment, proving the final regime.

## Verification

The standalone `verify.py` checks the credited negative-hypergeometric mass function against exact urn-word enumeration, verifies its exact first two moments over a finite parameter grid, independently convolves several increments, checks geometric-exponential product moments, and performs finite endpoint-asymptotic diagnostics in each of the three regimes. It also uses exact large integers for the example \(n_j=2^{j^2}\). To replay, run `python3 verify.py` with Python 3 and no third-party dependencies. The latest replay produced `PASS 347 exact and diagnostic assertions`. The unbounded-limit assertions and the moment convergence are proved in the preceding analytic argument; finite checks are not offered as proofs of infinite statements.

## Relationship to prior work

Stark [1] supplies the independent negative-hypergeometric increment law, a Gaussian theorem under bounded multiplicity ratios, and a cubic-exponential example where Gaussian convergence fails. Those results do not state the square-exponential critical product law or the trichotomy for arbitrary \(\beta>1\); in particular the new Gaussian regime has unbounded multiplicity ratios. Buchanan, Burghart, Wagner and Yin [2] instead define cycles through the functional digraph of a multiset word, a different statistic from the canonical Knuth-factorization cycle count. The ordinary-permutation cycle correlations studied in [3] also address a different object. The present result claims no novelty for negative-hypergeometric moment identities, elementary Lyapunov theory, exponential waiting-time laws, or Euler's infinite-product algebra.

## Limitations

No statement is made for \(\beta\le1\), nonuniform word sampling, other definitions of multiset cycles, or multivariate cycle statistics. The proofs use standard triangular-array methods after the exact decomposition of [1]. The checks establish correctness conditional on the cited source identity and the displayed analytic estimates; a separate independent mathematical review has not been performed. Historical-priority uncertainty remains for other formulations of growing-multiplicity multiset statistics or broad triangular-array theorems specialized to this setting. The critical law is not Gaussian and has an entire positive support, but no new density formula is asserted.

## References

[1] Dudley Stark, *A Chinese restaurant process for multiset permutations*, arXiv:2509.13979, first publicly posted 2025-09-17; Modern Stochastics: Theory and Applications 13 (2026), 289–301. https://arxiv.org/abs/2509.13979 ; https://doi.org/10.15559/26-VMSTA294 . Relevant material: Sections 2–4, particularly the independent-increment formula and the end of Section 4.

[2] Calum Buchanan, Fabian Burghart, Stephan Wagner and Mei Yin, *On Cycles in Multiset Permutations, Parking Functions, and Related Structures*, arXiv:2606.19500, first posted 2026-06-17; AofA 2026. https://arxiv.org/abs/2606.19500 ; https://doi.org/10.4230/LIPIcs.AofA.2026.16 . Relevant material: Sections 1, 2 and 6.

[3] Published mathematical research record on uniform-permutation cycle-count/inversion covariance (different statistic), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-linear-inversion-gap-profile-for-cycle-count-in-a-uniform-random--efaa92233051 .

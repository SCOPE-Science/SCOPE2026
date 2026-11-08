# Positive descent–inversion dependence and a joint Gaussian law for random-to-top shuffles

## Finding

Start with the identity deck of \(n\ge 2\) distinct cards. In each of \(r\ge 1\) independent steps, choose one of the \(n\) card labels uniformly and move that card to the top, including steps that leave the deck unchanged. Write \(D_{r,n}\) for the number of descents in the resulting one-line permutation, \(I_{r,n}\) for its inversion count, and \(K_{r,n}\) for the number of distinct labels selected during the \(r\) steps. All statistics refer to the same resulting deck.

**Finite-size statement.** Conditional on \(K_{r,n}=k\), where \(1\le k\le n\), define
\[
 d_n(k)=\frac{k+1}{2}-\frac{1}{n-k+1},\qquad
 m_n(k)=\frac{k(2n-k-1)}4.
\]
Then
\[
 \mathbb E[D_{r,n}\mid K_{r,n}=k]=d_n(k),\qquad
 \mathbb E[I_{r,n}\mid K_{r,n}=k]=m_n(k),
\]
and, more strongly,
\[
 \boxed{\operatorname{Cov}(D_{r,n},I_{r,n}\mid K_{r,n}=k)=\tfrac12d_n(k).}
\]
Consequently the exact finite-time identity
\[
 \boxed{\operatorname{Cov}(D_{r,n},I_{r,n})
 =\tfrac12\mathbb E[D_{r,n}]
 +\operatorname{Cov}\bigl(d_n(K_{r,n}),m_n(K_{r,n})\bigr)>0}
\]
holds for every \(n\ge2\) and \(r\ge1\). The second covariance is nonnegative because both functions are nondecreasing on the allowed integers.

**Critical joint limit.** Fix \(c>0\), take \(r_n=\lfloor cn\rfloor\), and put
\[
 b=e^{-c},\qquad a=1-b,\qquad \tau^2=b-(1+c)b^2>0.
\]
As \(n\to\infty\) (using sufficiently large \(n\) that \(r_n\ge1\)),
\[
 \boxed{\left(\frac{D_{r_n,n}-\mathbb E D_{r_n,n}}{\sqrt n},
 \frac{I_{r_n,n}-\mathbb E I_{r_n,n}}{n^{3/2}}\right)
 \Longrightarrow \mathcal N_2(0,\Sigma_c),}
\]
where
\[
 \boxed{\Sigma_c=
 \begin{pmatrix}
 \dfrac{a}{12}+\dfrac{\tau^2}{4}&\dfrac{b\tau^2}{4}\\[6pt]
 \dfrac{b\tau^2}{4}&\dfrac{1-b^3}{36}+\dfrac{b^2\tau^2}{4}
 \end{pmatrix}.}
\]
The limiting Gaussian correlation is strictly positive, whereas the two fluctuations become asymptotically independent when the number of distinct selected cards is held fixed at its deterministic first-order value. The positive cross-covariance \(b\tau^2/4\) comes entirely from fluctuations of the number of distinct selected cards.

## Assumptions and scope

The sampling of card labels is i.i.d. uniform across time, without any conditioning on the final deck. A descent is a position \(i<n\) whose card label exceeds the label in position \(i+1\); an inversion is a pair of positions \(i<j\) whose card labels appear in decreasing order. The finite claim covers every integer \(n\ge2\), \(r\ge1\); the limit covers every fixed \(c>0\). In particular it does not claim a central limit theorem when \(c\) itself varies with \(n\).

## Proof

**1. Conditional uniform-prefix representation.** Conditional on \(K_{r,n}=k\), the selected labels form a uniformly random \(k\)-subset, whose order at the top is uniform, while all unselected labels stay in increasing order below. Equivalently, draw a uniform permutation \(\pi\) of \([n]\), keep its first \(k\) entries and sort its final \(n-k\) entries increasingly. The same representation is obtained by ranking i.i.d. atomless uniform random variables \(U_1,\ldots,U_n\). Let \(A_{ij}=\mathbf 1\{U_i>U_j\}\), and set
\[
 H_k=\sum_{i=1}^{k-1}A_{i,i+1},\qquad
 V_k=\sum_{1\le i\le k<j\le n}A_{ij}
     +\sum_{1\le i<j\le k}A_{ij}.
\]
The conditional inversion count is \(V_k\). The conditional descent count is \(H_k+B_k\), where \(B_k=\mathbf 1\{U_k>\min_{j>k}U_j\}\) for \(k<n\), and \(B_n=0\). Writing \(m=n-k\), a given \(U_k\) is the minimum of \(U_k,U_{k+1},\ldots,U_n\) with probability \(1/(m+1)\). Thus \(\mathbb E B_k=m/(m+1)\), and \(\mathbb E[H_k+B_k]=d_n(k)\). Each ordered pair with its first index at most \(k\) is inverted with probability \(1/2\), giving \(\mathbb EV_k=m_n(k)\).

**2. Exact conditional covariance.** For every \(i<k\), only inversions containing index \(i\) or \(i+1\) contribute to \(\operatorname{Cov}(A_{i,i+1},V_k)\). The inversion \((i,i+1)\) contributes \(1/4\); all other contributing terms cancel in pairs by the elementary three-uniform identities \(\operatorname{Cov}(A_{ij},A_{i\ell})=1/12\) and \(\operatorname{Cov}(A_{ij},A_{j\ell})=-1/12\) for \(i<j<\ell\), together with their reversed-index analogues. Thus
\[
 \operatorname{Cov}(H_k,V_k)=\frac{k-1}{4}.
\]
To treat the boundary, let \(m=n-k>0\) and \(J_k=1-B_k\), the event that \(U_k\) is smallest among itself and all \(m\) unselected entries. Conditioned on \(J_k=1\), \(\mathbb E U_k=1/(m+2)\), and for each \(j>k\), \(\mathbb E U_j=(m+3)/(2(m+2))\). Relative to their unconditioned means, the inversion probabilities for pairs \((i,k)\) with \(i<k\) rise by \(m/(2(m+2))\), and those for pairs \((i,j)\) with \(i<k<j\) fall by \(1/(2(m+2))\). Their aggregate differences cancel. All \(m\) inversions \((k,j)\) disappear, giving \(\mathbb E[V_k\mid J_k=1]-\mathbb EV_k=-m/2\). Since \(\mathbb P(J_k=1)=1/(m+1)\),
\[
 \operatorname{Cov}(B_k,V_k)=\frac{m}{2(m+1)}.
\]
For \(m=0\) this covariance is zero. Therefore
\[
 \operatorname{Cov}(H_k+B_k,V_k)
 =\frac{k-1}{4}+\frac{m}{2(m+1)}
 =\frac12\left(\frac{k+1}{2}-\frac1{m+1}\right).
\]
The law of total covariance gives the finite identity. For \(1\le k<n\),
\[
 d_n(k+1)-d_n(k)=\frac12-\frac1{(n-k)(n-k+1)}\ge0,
\quad m_n(k+1)-m_n(k)=\frac{n-k-1}{2}\ge0.
\]
Both are nondecreasing. If \(K'\) is an independent copy of \(K\), then twice the covariance of \(d_n(K),m_n(K)\) is the expectation of their two same-signed differences. Moreover \(d_n(k)>0\) for all \(n\ge2\), \(k\ge1\), so the full covariance is strictly positive.

**3. Joint conditional Gaussian fluctuations.** Fix integers \(k_n\) with \(k_n/n\to a\in(0,1)\). A one-dependent central limit theorem for
\[
 H_{k_n}-\frac{k_n-1}{2}
 =\sum_{i<k_n}\left(A_{i,i+1}-\frac12\right)
\]
gives a normal limit on scale \(\sqrt n\) of variance \(a/12\); the bounded boundary term is negligible. For inversions, the first-order Hoeffding projection of \(V_{k_n}-\mathbb EV_{k_n}\) is
\[
 L_{n,k_n}=\sum_{i=1}^{n}w_{n,k_n}(i)\left(U_i-\frac12\right),\qquad
 w_{n,k}(i)=\begin{cases}n-2i+1,&i\le k,\\-k,&i>k.\end{cases}
\]
The remainder is a sum of centered, first-order-degenerate pair kernels; its summands are mutually uncorrelated unless they use exactly the same unordered pair. Thus its variance is \(O(n^2)\), which is negligible on the \(n^{3/2}\) scale. Directly,
\[
 \frac{\operatorname{Var}L_{n,k_n}}{n^3}
 =\frac{\sum_{i\le k_n}(n-2i+1)^2+(n-k_n)k_n^2}{12n^3}
 \longrightarrow\frac{1-(1-a)^3}{36}.
\]
The pair consisting of the centered descent sum and \(L_{n,k_n}\) can be written as a bounded triangular array of one-dependent, two-dimensional summands, each of size \(O(n^{-1/2})\) after normalization. The standard blocking proof of the one-dependent triangular-array CLT, applied to every Cramér–Wold combination, gives joint normality. Its limiting cross-covariance vanishes: directly \(\operatorname{Cov}(H_{k_n},V_{k_n})=(k_n-1)/4=O(n)\), whereas the cross-normalization is \(n^2\). Hence the two limiting Gaussian coordinates are independent.

**4. Random occupancy index.** For \(r_n=\lfloor cn\rfloor\), classical uniform occupancy gives
\[
 \frac{K_{r_n,n}-\mathbb E K_{r_n,n}}{\sqrt n}
 \Longrightarrow Z\sim\mathcal N(0,\tau^2),\qquad
 \mathbb E K_{r_n,n}=an+O(1),\quad
 \operatorname{Var}K_{r_n,n}=O(n).
\]
The exact mean is \(n(1-(1-1/n)^{r_n})\). Coupling the conditional decks to a permutation independent of \(K_{r_n,n}\), changing the prefix length from \(K_{r_n,n}\) to \(\lfloor an\rfloor\) changes the variance of the centered descent sum by at most \(O(\mathbb E|K_{r_n,n}-\lfloor an\rfloor|)=O(\sqrt n)=o(n)\). The corresponding centered inversion sum changes by variance at most \(O(n^2\mathbb E|K_{r_n,n}-\lfloor an\rfloor|)=O(n^{5/2})=o(n^3)\): its inverse-Lehmer rows are independent, each with variance \(O(n^2)\). The boundary descent is always bounded by one.

The independent occupancy fluctuation therefore adds \(Z/2\) to the normalized descent coordinate. Taylor-expanding the exact quadratic conditional inversion mean \(m_n(k)\) at \(k=\mathbb E K_{r_n,n}\) adds \((1-a)Z/2=bZ/2\) to the normalized inversion coordinate; the centered quadratic remainder is negligible. The two conditional Gaussian fluctuations and \(Z\) are independent in the limit. Their sum has covariance matrix \(\Sigma_c\) displayed above. Since \(a>0\), \(1-b^3>0\), and \(\tau^2=b(1-(1+c)b)>0\), this covariance matrix is positive definite, with strictly positive off-diagonal entry. This completes the proof.

## Verification

The accompanying `check.py` enumerates every uniform permutation through seven cards and every card-choice history through five cards and four shuffle steps, comparing two independent descriptions of the resulting joint statistic. It verifies the exact conditional means, variance, covariance identity, and total-covariance law using rational arithmetic, as well as exact finite polynomial identities needed for the limit. The saved run passed 75,033 exact assertions. A separately seeded `sample_check.py` checks the critical-window covariance matrix numerically at \(n=500\) and \(c=1\); its three moment diagnostics passed, with Monte Carlo deviations explicitly reported in the program output. Neither finite enumeration nor simulation is used as a proof of the asymptotic theorem; the argument above is the proof.

## Relationship to prior work

Clay (2026) derives the uniform-prefix decomposition and proves separate central limit theorems for descents and inversions in critical random-to-top shuffles. These existing marginal formulas are not claimed as new here. Dörr and Heiny (2025; first preprint 2023) develop the joint descent–inversion limit and exact covariance for a single uniform random permutation; their uniform-permutation results do not directly give the time-dependent shuffle mixture or its nonzero occupancy-induced limiting correlation. The present claim supplies a finite-time joint covariance identity and the coupled bivariate critical limit. The conditional uniform-permutation covariance \((k-1)/4\) is an established pattern; the conditional sorted-suffix and mixture identities are the distinctive steps here.

## Limitations

No quantitative rate of bivariate normal approximation or critical-window extension to varying \(c\) is asserted. The theorem does not characterize joint tails or fixed-point dependence. Historical priority remains subject to broader specialized literature beyond the sources accessible in this study. Finite exact checks and numerical trials are verification aids, not substitutes for the full argument.

## References

1. Alexander Clay, *On the statistics of random-to-top shuffles*, arXiv:2603.09008, first public posting 2026-03-09. https://arxiv.org/abs/2603.09008
2. Philip Dörr and Johannes Heiny, *Joint Extremes of Inversions and Descents of Random Permutations*, *Journal of Theoretical Probability* 38, article 42 (2025); preprint arXiv:2309.17314 (2023). https://doi.org/10.1007/s10959-025-01407-y
3. Persi Diaconis, James Allen Fill and Jim Pitman, *Analysis of top to random shuffles*, *Combinatorics, Probability and Computing* 1(2), 135–155 (1992). https://doi.org/10.1017/S0963548300000158

# A two-index thinning self-decomposability criterion with reentrant negative-transmutation phases

## Finding

The Poisson–transmuted geometric count family has a complete **two-index** criterion for Bernoulli-thinning self-decomposability in its negative-transmutation range. Fix \(0<q<1\), \(-1\le\alpha<0\), and \(\lambda\ge0\); let \(P\) be Poisson with mean \(\lambda\), let \(T\) have the transmuted geometric distribution defined below, and take \(X=P+T\) independently. Write
\[
\rho=\frac{q(q+\alpha)}{1+\alpha q},\qquad
D_j=q^j(1-q)+q^{2j}(1-q^2)-\rho^j(1-\rho),\quad j=1,2.
\]
Then \(X\) is compound Poisson throughout the full stated parameter domain, but it is **discrete self-decomposable under independent Bernoulli thinning if and only if**
\[
\boxed{D_2\ge0\quad\text{and}\quad\lambda+D_1\ge0.}
\]
These two comparisons alone control the infinitely many canonical-sequence inequalities. If \(D_2<0\), no added independent Poisson intensity can restore the property; if \(D_2\ge0\), the exact permissible intensities are \(\lambda\ge\max\{0,-D_1\}\).

The admissible negative-transmutation parameters need not form an interval. At \(q=99/100\) and \(\lambda=1\), successive values \(\alpha=-1,-99/100,-19/20,-1/10\) give the strict statuses **not self-decomposable, self-decomposable, not self-decomposable, self-decomposable**, respectively. This is a genuine reentrant phase pattern for a family which remains compound Poisson in all four cases.

## Assumptions and scope

The transmuted geometric law has support \(\mathbb N_0\) and mass
\[
\Pr(T=k)=(1-\alpha)(1-q)q^k+\alpha(1-q^2)q^{2k},\qquad k=0,1,2,\ldots.
\]
Although the second algebraic weight is negative when \(\alpha<0\), every probability is positive, because after removing the positive factor \((1-q)q^k\), the remaining factor is \((1-\alpha)+\alpha(1+q)q^k\ge1+\alpha q>0\). Summation gives total mass one. The endpoint \(\alpha=-1\) is included by continuity and is the maximum of two independent zero-based geometric observations; \(\lambda=0\) is an allowed Poisson point mass. The upper endpoint \(\alpha=0\) and positive-transmutation range are not new claims here.

For each \(c\in(0,1)\), let \(c\circ X'\) be an independent Bernoulli thinning of a copy \(X'\) of \(X\). Discrete self-decomposability means that \(X\) can be written in law as \(c\circ X'+R_c\) for an independent nonnegative-integer remainder \(R_c\), **for every** such \(c\). Ordinary compound-Poisson infinite divisibility is weaker.

The primary classification is MSC2020 60E07, concerning infinitely divisible distributions and their refinements. All statements hold for the continuum of parameters shown, without restrictions on rationality or on a finite number of sequence indices.

## Proof

**1. Exact factorization and positivity.** Direct summation of the transmuted geometric series and independent Poisson convolution yields
\[
G_X(z)=e^{\lambda(z-1)}\frac{(1-q)(1+\alpha q)(1-\rho z)}{(1-qz)(1-q^2z)},
\qquad |z|\le1,
\]
with \(\rho=q(q+\alpha)/(1+\alpha q)\). Since \(\rho\) is strictly increasing in \(\alpha\), its range here is \(-q\le\rho<q^2\). In particular \(|\rho|\le q<1\). Expansion of the analytic logarithm gives
\[
\log G_X(z)=\log G_X(0)+\sum_{k=1}^{\infty}\nu_k z^k,\qquad
\nu_k=\lambda\mathbf1_{\{k=1\}}+\frac{q^k+q^{2k}-\rho^k}{k}.
\]
Every \(\nu_k\) is nonnegative: when \(\rho\ge0\), \(q^k-\rho^k\ge0\); when \(\rho<0\), odd powers increase the numerator, while for even powers \(q^k-|\rho|^k\ge0\). The series is absolutely summable. Because \(G_X(1)=1\), its constant log term is \(-\sum\nu_k\). Hence \(G_X(z)=\exp\{\sum_{k\ge1}\nu_k(z^k-1)\}\), the generating function of a genuine compound-Poisson law. No infinite-divisibility assertion rests on numerical truncation.

**2. The known canonical criterion reduces the problem.** The discrete Steutel–van Harn self-decomposability theorem says that a nondegenerate compound-Poisson law on \(\mathbb N_0\) is self-decomposable under every Bernoulli retention probability exactly when its canonical sequence \(a_k=k\nu_k\), \(k\ge1\), is nonincreasing. Here
\[
 a_k=\lambda\mathbf1_{\{k=1\}}+q^k+q^{2k}-\rho^k.
\]
The comparison \(a_1\ge a_2\) is precisely \(\lambda+D_1\ge0\). For each integer \(k\ge2\), comparison \(a_k\ge a_{k+1}\) is precisely \(d_k\ge0\), where
\[
 d_k=q^k(1-q)+q^{2k}(1-q^2)-\rho^k(1-\rho).
\]
Thus \(D_2=d_2\ge0\) is necessary and the remaining task is to prove that it implies every \(d_k\ge0\) for \(k\ge3\).

**3. Nonnegative auxiliary root.** Suppose \(0\le\rho<q^2\). Put \(t=\rho/q\), so \(0\le t<q\), and \(m_k=(1-q)+(1-q^2)q^k\). Then
\[
 d_k=q^k\{m_k-(1-\rho)t^k\},\qquad
 m_{k+1}-q m_k=(1-q)^2>0.
\]
Consequently if \(d_k\ge0\), then \(m_{k+1}>q m_k\ge t m_k\ge(1-\rho)t^{k+1}\), so \(d_{k+1}>0\). Start at \(k=2\). The endpoint \(\rho=0\) is included directly.

**4. Negative auxiliary root and a two-index cutoff.** Suppose \(\rho=-s\) with \(0<s\le q\). For odd \(k\), \(d_k>0\) since the last term becomes positive. For even \(k=2j\), define
\[
 u=(s/q)^2,\qquad m_j=(1-q)+(1-q^2)q^{2j}.
\]
Then \(d_{2j}=q^{2j}\{m_j-(1+s)u^j\}\). The condition \(d_2\ge0\) is \(m_1\ge(1+s)u\). The positive two-exponential sequence \(m_j\) is strictly log-convex, with
\[
 m_jm_{j+2}-m_{j+1}^2=(1-q)(1-q^2)q^{2j}(1-q^2)^2>0.
\]
Moreover, direct expansion gives
\[
 m_2-m_1^2=q(1-q)\bigl(q^6+q^5+2q^3-2q+1\bigr)>0.
\]
For the strict sign, \(q^6+q^5\ge0\) and \(1-2q+2q^3\ge1-4/(3\sqrt3)>0\) throughout \(0<q<1\). By log-convexity, the ratios \(m_{j+1}/m_j\) are increasing, with \(m_2/m_1>m_1\); induction gives \(m_j\ge m_1^j\) for every \(j\ge1\). Therefore
\[
 m_j\ge m_1^j\ge(1+s)^j u^j\ge(1+s)u^j,
\]
which proves \(d_{2j}\ge0\) for every \(j\ge1\). All odd and even indices are covered. Together with Step 3, this proves the exact two-index criterion.

**5. Sharp parameter witnesses.** At \(q=9/10\), \(\alpha=-7/10\), the auxiliary root is \(\rho=18/37\) and exact arithmetic gives
\[
 D_1=-\frac{81009}{13690000}<0,\qquad
 D_2=\frac{4261245327}{50653000000}>0.
\]
Consequently the exact Poisson threshold for the property is \(\lambda=81009/13690000\), with equality included. At \(q=1/2\), \(\alpha=-9/10\), \(\rho=-4/11\) and \(D_2=-719/85184<0\), so no \(\lambda\) suffices. For the reentrant example at \(q=99/100\), \(\lambda=1\), the four indicated transmutation values give respectively \(D_2<0,D_2>0,D_2<0,D_2>0\); the first-index condition is automatically satisfied because \(D_1> -1\) for every \(-q\le\rho<q^2\): \(D_1=q(1-q)+q^2(1-q^2)-\rho(1-\rho)>-1\), as \(\rho(1-\rho)\le1/4\) for \(\rho\ge0\), while for \(\rho<0\) it is negative. The stated strict signs are certified as exact rationals by the accompanying checker. Since \(D_2\) depends continuously on \(\alpha\), these four signs force at least three distinct parameter-transition points at this fixed \(q,\lambda\). No assertion of exactly three roots is made.

## Verification

The standalone standard-library script `verify.py` checks, over a deterministic exact-rational parameter grid, the probability-generating coefficient recurrence, the logarithmic canonical coefficients, all displayed explicit witness fractions, and long finite segments of the adjacent-difference inequalities. Execute `python3 verify.py` in the directory containing the script. Its output reports the count of exact checks. The universal all-index statements are proved by Steps 1–4; finite checks do not substitute for those proofs or certify the number of all real transition points.

## Relationship to prior work

Nandi, Chakraborty and Biswas (2023) introduced the Poisson–transmuted geometric convolution for positive transmutation and analyzed its masses, moments, dispersion, reliability and estimation. Chakraborty and Bhati (2016) introduced the parent transmuted geometric distribution on the larger range that includes negative transmutation and noted its geometric sample-maximum endpoint. The model, its parameterization, and its mass formula are all prior work. Earlier work on positive transmutation already establishes thinning self-decomposability in that different parameter half-line; the present classification addresses the negative half-line and does not repackage the positive result.

Steutel and van Harn (1979), Theorem 2.2, establish the general nonincreasing-canonical-sequence characterization. This theorem is taken as a **known** tool; the contribution is the explicit negative-transmutation compound-Poisson representation, reduction of the infinite family to two inequalities, and the new reentrant parameter behavior. A published classification of ordinary infinite divisibility for two-sample geometric maxima covers the endpoint \(\alpha=-1\) at the weaker additive-divisibility level. The full text of that related claim was inspected: it does not assert the negative-transmutation thinning phase diagram. A related classification for folded differences of heterogeneous geometric observations concerns a different operation and different generating function. Other work on seasonal transmuted-geometric INAR models studies integer autoregression without giving this self-decomposability classification.

## Limitations

This is an exact theorem for \(-1\le\alpha<0\), \(0<q<1\), \(\lambda\ge0\); it is not a complete solution for every possible transmutation sign in one new result. It does not identify the exact number of distinct reentrant phase transitions or characterize all possible connected components in the parameter space. Continuous parameters are treated analytically; rational computations provide diagnostics and witnesses, not a substitute for proof. The general discrete self-decomposability criterion and the geometric maximum infinite-divisibility result belong to prior literature. Historical priority beyond the inspected and searchable sources is not guaranteed, and independent mathematical validation has not occurred.

## References

1. A. Nandi, S. Chakraborty and A. Biswas, *A new count model based on Poisson-Transmuted Geometric convolution*, arXiv:2306.07219v1, first publicly posted 12 June 2023. https://arxiv.org/abs/2306.07219
2. S. Chakraborty and D. Bhati, *Transmuted geometric distribution with applications in modelling and regression analysis of count data*, SORT 40 (2016), 153–176. https://www.idescat.cat/sort/sort401/40.1.7.chakraborty-bhati.pdf
3. F. W. Steutel and K. van Harn, *Discrete analogues of self-decomposability and stability*, Annals of Probability 7 (1979), 893–899, Theorem 2.2. https://doi.org/10.1214/aop/1176994950
4. *A sharp infinite-divisibility cutoff for maxima of geometric samples* (2026), published mathematical result; exact two-sample jump intensities and the additive-divisibility boundary for geometric maxima.
5. *Sharp thinning self-decomposability phase diagram for folded skew discrete Laplace laws* (2026), published mathematical result; a separate geometric difference/folding model.
6. *A Seasonal Transmuted Geometric INAR Process: Modeling and Applications in Count Time Series*, Mathematics 13 (2025), 2334. https://www.mdpi.com/2227-7390/13/15/2334

# Exact harmonic dependence of the longest uniform spacing and Greenwood concentration

## Finding

Fix an integer \(m\ge2\). Draw \(m-1\) independent uniform points in \((0,1)\), and let \(X_1,\ldots,X_m\) be the consecutive spacings, including the two boundary gaps. Put
\[
M=\max_{1\le i\le m}X_i,\qquad Q=\sum_{i=1}^m X_i^2.
\]
Here \(Q\) is the unscaled Greenwood statistic, and \(M\) is the longest-spacing statistic. Define \(H_m=\sum_{j=1}^m 1/j\) and \(H_m^{(2)}=\sum_{j=1}^m 1/j^2\). The exact mixed moment and covariance are
\[
\mathbb E[M Q]=\frac{H_m^2+H_m^{(2)}+2(m+1)H_m}{m(m+1)(m+2)},
\]
\[
\boxed{\operatorname{Cov}(M,Q)=\frac{H_m^2+H_m^{(2)}-2H_m}{m(m+1)(m+2)}>0.}
\]
The exact correlation is
\[
\boxed{\rho_m=\frac{H_m^2+H_m^{(2)}-2H_m}{2}
\sqrt{\frac{(m+1)(m+3)}{(m+2)(m-1)(mH_m^{(2)}-H_m^2)}}.}
\]
It has the sharp first-order decay
\[
\boxed{\rho_m\sim\frac{\sqrt6}{2\pi}\frac{(\log m)^2}{\sqrt m}\to0,\qquad m\to\infty.}
\]
Thus these two standard measures of irregular spacing are positively correlated at every finite sample size, yet their Pearson correlation vanishes unusually slowly. For example, \(\rho_{10}\approx0.93413\) and \(\rho_{100}\approx0.78896\).

## Assumptions and scope

The spacings form a uniform random point of the simplex \(\{x_i\ge0:\sum_i x_i=1\}\), equivalently \(X\sim\operatorname{Dirichlet}(1,\ldots,1)\). The number \(m\) of spacings is one more than the number of uniform sample points. All formulas are finite-sample identities for integers \(m\ge2\). By the probability-integral transform they also give the null correlation for spacings between consecutive transformed observations from any completely specified continuous distribution function.

## Proof

**Step 1 (simplex moments).** Uniform-simplex moments yield
\[
\mathbb E Q=\frac2{m+1},\quad
\operatorname{Var}(Q)=\frac{4(m-1)}{(m+1)^2(m+2)(m+3)}.
\]
For example, \(\mathbb E X_i^2=2/[m(m+1)]\), \(\mathbb E X_i^4=24/[m(m+1)(m+2)(m+3)]\), and \(\mathbb E X_i^2X_j^2=4/[m(m+1)(m+2)(m+3)]\) when \(i\ne j\).

**Step 2 (a shifted-face identity).** Fix a subset of \(k\) coordinates. For \(0\le t\le1/k\), the event that all these coordinates exceed \(t\) has probability \((1-kt)^{m-1}\). Conditional on the event, subtracting \(t\) from the designated coordinates and dividing every coordinate by \(1-kt\) produces another uniform-simplex vector. Consequently,
\[
\mathbb E\bigl[Q\,\mathbf1\{X_1>t,\ldots,X_k>t\}\bigr]
=(1-kt)^{m-1}\left[kt^2+\frac{2kt(1-kt)}m+\frac{2(1-kt)^2}{m+1}\right].
\]
For \(t>1/k\) the left side vanishes.

**Step 3 (tail integration and inclusion–exclusion).** Since \(M\in[0,1]\),
\[
\mathbb E[M Q]=\int_0^1\mathbb E[Q\,\mathbf1\{M>t\}]\,dt.
\]
Inclusion–exclusion over the \(m\) exceedance events, followed by \(u=kt\) and elementary beta integrals, gives
\[
\int_0^{1/k}\mathbb E\bigl[Q\,\mathbf1\{X_1>t,\ldots,X_k>t\}\bigr]dt
=\frac{2}{m(m+1)(m+2)}\left(\frac1{k^2}+\frac{m+1}k\right).
\]
Use the binomial–harmonic identities
\[
\sum_{k=1}^m(-1)^{k+1}\binom mk\frac1k=H_m,\qquad
\sum_{k=1}^m(-1)^{k+1}\binom mk\frac1{k^2}
=\frac{H_m^2+H_m^{(2)}}2.
\]
They follow by integrating \([1-(1-z)^m]/z\) once and with weight \(-\log z\), respectively. The second weighted integral equals \(\sum_{j=1}^mH_j/j\) by the beta derivative formula. Substitution proves the displayed mixed moment. Also, the same tail integration without \(Q\) gives \(\mathbb E M=H_m/m\). Subtracting \(\mathbb E M\,\mathbb E Q\) proves the covariance formula.

**Step 4 (strict sign).** Set \(F_m=H_m^2+H_m^{(2)}-2H_m\). Then \(F_1=0\) and
\[
F_m-F_{m-1}=\frac{2}{m}\left(H_{m-1}-1+\frac1m\right)>0
\quad(m\ge2).
\]
Thus the covariance is strictly positive in every stipulated dimension.

**Step 5 (correlation and limit).** The same longest-spacing tail calculation gives
\[
\mathbb E M^2=\frac{H_m^2+H_m^{(2)}}{m(m+1)},\quad
\operatorname{Var}(M)=\frac{mH_m^{(2)}-H_m^2}{m^2(m+1)}.
\]
Combining both variances with the covariance gives the exact correlation. As \(m\to\infty\), the covariance is asymptotic to \((\log m)^2/m^3\), the variance of \(M\) is asymptotic to \(\pi^2/(6m^2)\), and the variance of \(Q\) is asymptotic to \(4/m^3\). Their ratio yields the stated sharp decay.

## Verification

The standalone program `greenwood_max_check.py` separately evaluates the inclusion–exclusion beta integrals and the closed harmonic expression with exact rational arithmetic for every \(m=2,\ldots,160\). It additionally verifies the two first moments of the longest spacing, the first two moments of Greenwood concentration, positivity, and the covariance for those dimensions. The program prints `PASS: 159 exact rational checks, m=2,...,160` when all assertions hold. Independent seeded normalized-exponential simulations at \(m=2,5,10,30\) produced covariance estimates within two estimated standard errors of the formula. These computations corroborate, but do not replace, the all-dimension proof above.

## Relationship to prior work

Pyke's classical 1965 survey describes statistics based on the extreme gaps and on sum-functions of spacings, but only its abstract and indexed excerpts were accessible for this comparison. Royen's complete 2010 preprint studies the marginal law and quantiles of \(Q\), including the uniform-spacing specialization. Its derivations concern the square sum rather than the mixed moment with the largest component. Darling's 1953 work gives transform methods for sum-functions of spacings, a related but distinct statistic class.

A published calculation for the range and sample variance of **unnormalized exponential observations** yields a different harmonic covariance and the same order of slow correlation decay; it does not state the normalized Dirichlet largest-coordinate/Greenwood mixed moment. Likewise, covariance results for fixed-threshold exceedance counts involve \(\sum_i\mathbf1\{X_i>t\}\), not the event that *at least one* coordinate exceeds \(t\), which is needed to integrate the maximum. Thus these results do not directly supply the displayed joint finite-sample formula. A general classical joint-moment identity could nevertheless subsume it; historical priority has not been independently certified.

## Limitations

This theorem is specific to the uniform simplex, not to arbitrary unequal-parameter Dirichlet distributions. It establishes covariance and Pearson correlation, not asymptotic independence of the full joint law, conditional stochastic monotonicity, or a new calibrated combined test. The complete 1965 survey could not be checked because its publisher full text was unavailable, leaving a real priority risk. The computations are finite checks and are not substitutes for the proof.

## References

1. T. Royen, "The distribution of the square sum of Dirichlet random variables and a table with quantiles of Greenwood's statistic," arXiv:1008.4059, submitted 2010-08-24, https://arxiv.org/abs/1008.4059 .
2. R. Pyke, "Spacings," *Journal of the Royal Statistical Society, Series B* **27** (1965), 395–436, https://doi.org/10.1111/j.2517-6161.1965.tb00602.x .
3. D. A. Darling, "On a Class of Problems Related to the Random Division of an Interval," *Annals of Mathematical Statistics* **24** (1953), 239–253, https://doi.org/10.1214/aoms/1177729030 .
4. "Exact harmonic covariance of range and sample variance in exponential sampling," published-finding corpus (2026), public research record `90264ed7a2e8`.

# Sharp order-dependent null-calibration distortion of a Tsallis uniformity statistic

## Finding

For the complete-data cumulative-residual Tsallis entropy (CRTE) uniformity statistic of Mohamed, Barakat, Alyami and Abd Elgawad (2022), the exact null variance and the asymptotic variance differ from the variance printed in the original article. More specifically, for each fixed \(\theta>0\), \(\theta\ne1\), and integer \(n\ge2\), let \(X_1,\ldots,X_n\) be independent \(\operatorname{Uniform}(0,1)\) variables and put

\[
 a_\theta(u)=\frac{u-u^\theta}{\theta-1},\quad
 w_{i,n}=a_\theta(1-i/n),\quad
 R_{n,\theta}=\sum_{i=1}^{n-1} w_{i,n}(X_{(i+1)}-X_{(i)}).
\]

Writing \(A_n=\sum_{i=1}^{n-1}w_{i,n}\) and \(B_n=\sum_{i=1}^{n-1}w_{i,n}^2\), the exact null moments are

\[
 \mathbb E R_{n,\theta}=\frac{A_n}{n+1},\qquad
 \operatorname{Var}(R_{n,\theta})
 =\frac{(n+1)B_n-A_n^2}{(n+1)^2(n+2)}.
\]

The variance \(V^{\mathrm{printed}}_{n,\theta}=nB_n/[(n+1)^2(n+2)]\) from the original article exceeds the true variance whenever \(n\ge3\); equality holds at \(n=2\). For every **fixed** allowed \(\theta\),

\[
 \sqrt n\left(R_{n,\theta}-\mathbb E R_{n,\theta}\right)
 \xrightarrow{d} N(0,v_\theta),\qquad
 v_\theta=\frac{2\theta^2+\theta+2}
 {12(\theta+1)^2(\theta+2)(2\theta+1)}.
\]

The asymptotic inflation of the **printed variance relative to the true variance** is exactly

\[
 \rho(\theta)=\lim_{n\to\infty}
 \frac{V^{\mathrm{printed}}_{n,\theta}}{\operatorname{Var}(R_{n,\theta})}
 =\frac{8(\theta+1)^2}{2\theta^2+\theta+2}.
\]

Its sharp range is \(4<\rho(\theta)<32/5\) for the stated parameter domain; the supremum \(32/5\) is approached at the excluded order \(\theta=1\), while the infimum \(4\) is approached as \(\theta\downarrow0\) or \(\theta\to\infty\). Thus the complete order dependence and its unique limiting worst case are determined.

Consequently, the two-sided normal critical values explicitly formed from \(\mathbb E R_{n,\theta}\) and \(V^{\mathrm{printed}}_{n,\theta}\), at nominal \(0<\alpha<1\), have actual asymptotic null rejection probability

\[
 2\Phi\!\left(-z_{1-\alpha/2}\sqrt{\rho(\theta)}\right),
\]

not \(\alpha\). In particular, at order \(\theta=2\), the limiting rejection probability for nominal \(5\%\) is \(1.57944924024\times10^{-6}\), compared with \(0.05\). This is a statement solely about the source's **printed-variance normal calibration**, not Monte Carlo calibration or a separately corrected normal approximation.

## Assumptions and scope

The null law is fully specified continuous uniformity on \([0,1]\); no parameters are estimated. The source statistic uses consecutive **interior** ordered gaps, not the two endpoint gaps, exactly as in its displayed equation (8). The sample size is any integer \(n\ge2\); the Tsallis order is fixed with \(\theta>0\) and \(\theta\ne1\). The Gaussian limit is not asserted uniformly for moving orders. The normal calibration is centered at the exact finite-sample mean, as in the source's equation (11). The limiting \(\theta\to1\) ratio is an analytic continuation only: the source's stated parameter set excludes \(1\).

## Proof

### Joint spacing law and exact moments

Include the endpoint spacings \(D_0=X_{(1)}\), \(D_i=X_{(i+1)}-X_{(i)}\) for \(1\le i\le n-1\), and \(D_n=1-X_{(n)}\). The full \((n+1)\)-vector is \(\operatorname{Dirichlet}(1,\ldots,1)\). Hence for any indices \(i\ne j\),

\[
 \mathbb ED_i=\frac1{n+1},\quad
 \operatorname{Var}(D_i)=\frac{n}{(n+1)^2(n+2)},\quad
 \operatorname{Cov}(D_i,D_j)=-\frac1{(n+1)^2(n+2)}.
\]

Extending weights to \(w_{0,n}=w_{n,n}=0\) and expanding the quadratic variance exactly gives

\[
 \operatorname{Var}\!\left(\sum_{i=0}^n w_{i,n}D_i\right)
 =\frac{nB_n-\sum_{i\ne j}w_{i,n}w_{j,n}}{(n+1)^2(n+2)}
 =\frac{(n+1)B_n-A_n^2}{(n+1)^2(n+2)}.
\]

All interior weights are strictly positive for every permitted \(\theta\). Thus \(A_n^2-B_n=2\sum_{1\le i<j\le n-1}w_{i,n}w_{j,n}\) is positive exactly when \(n\ge3\). The printed formula omits these negative off-diagonal covariances.

### Asymptotic variance and central limit theorem

The elementary integrals are

\[
 m_\theta=\int_0^1a_\theta(u)\,du=\frac1{2(\theta+1)},\qquad
 b_\theta=\int_0^1a_\theta(u)^2\,du
 =\frac2{3(\theta+2)(2\theta+1)}.
\]

For fixed \(\theta\), \(a_\theta\) is bounded and continuous on \([0,1]\), so \(A_n/n\to m_\theta\) and \(B_n/n\to b_\theta\). It follows from the exact formula that

\[
 n\operatorname{Var}(R_{n,\theta})\to b_\theta-m_\theta^2
 =\frac{2\theta^2+\theta+2}{12(\theta+1)^2(\theta+2)(2\theta+1)}>0,
\]

while \(nV^{\mathrm{printed}}_{n,\theta}\to b_\theta\).

For the distributional assertion, let \(E_0,\ldots,E_n\) be independent \(\operatorname{Exp}(1)\) variables, \(S_n=\sum_{j=0}^n E_j\), and \(D_i=E_i/S_n\). Put \(\mu_n=A_n/(n+1)\). The exact identity

\[
 R_{n,\theta}-\mu_n
 =\frac1{S_n}\sum_{i=0}^n(w_{i,n}-\mu_n)(E_i-1)
\]

holds because the centered deterministic weights sum to zero. Their maximum absolute value stays bounded. Their normalized squared sum converges to \(b_\theta-m_\theta^2>0\). The Lindeberg theorem for the independent, uniformly bounded-coefficient exponential triangular array gives the asserted Gaussian limit for \(n^{-1/2}\) times its numerator; \(S_n/n\to1\) in probability yields the claim by Slutsky's theorem. No independence of the Dirichlet spacings is asserted.

### Sharp inflation law and calibration

Dividing the two integrated variance coefficients gives \(\rho(\theta)\). Direct algebra proves

\[
 \rho(\theta)-4=\frac{12\theta}{2\theta^2+\theta+2},\qquad
 \frac{32}{5}-\rho(\theta)=
 \frac{24(\theta-1)^2}{5(2\theta^2+\theta+2)}.
\]

Both are strictly positive on the permitted domain. Furthermore \(\rho'(\theta)=-24(\theta-1)(\theta+1)/(2\theta^2+\theta+2)^2\), proving increase for \(0<\theta<1\), decrease for \(\theta>1\), and the stated endpoint limits. The positive variance limits allow standardization, so the source's nominal Gaussian \(\alpha/2\) two-sided cutoffs yield the stated actual asymptotic probability by continuity of the Gaussian distribution.

### Exact rational example

At \(\theta=2\), \(w_{i,n}=i(n-i)/n^2\) and power sums give

\[
 A_n=\frac{(n-1)(n+1)}{6n},\qquad
 B_n=\frac{(n-1)(n+1)(n^2+1)}{30n^3}.
\]

Thus, for every \(n\ge2\),

\[
 \mathbb E R_{n,2}=\frac{n-1}{6n},\quad
 \operatorname{Var}(R_{n,2})=\frac{(n-1)(n+3)}{180n^3},\quad
 \frac{V^{\mathrm{printed}}_{n,2}}{\operatorname{Var}(R_{n,2})}
 =\frac{6n(n^2+1)}{(n+1)(n+2)(n+3)}.
\]

The ratio tends to \(6\) and the stated significance value follows from \(2\Phi(-z_{0.975}\sqrt6)\).

## Verification

The included `checker.py` runs using only Python 3's standard library. It independently evaluates the full Dirichlet covariance formula and the exact rational \(\theta=2\) sums for all \(2\le n\le300\), checks the all-order asymptotic variance and sharp ratio at eleven positive entropy orders, and draws \(25{,}000\) reproducible raw uniform samples at \(n=100\). It produced \(1607\) successful deterministic assertions and sample variance \(5.67705965508\times10^{-5}\), against the exact \(5.665\times10^{-5}\). Simulations do not establish the central limit theorem; the proof above does.

For \(n=100\) and \(\theta=2\), exact-variance normal cutoffs at nominal \(5\%\) are \([0.15024810,0.17975190]\). The source's Table 1 Monte Carlo cutoffs \([0.1497,0.1792]\) are close, whereas its printed-variance normal cutoffs \([0.1299,0.20008]\) are substantially wider. This comparison checks that the same statistic and tails are being used; it does not certify finite-sample normal accuracy at other sizes/orders.

## Relationship to prior work

The statistic, printed variance and normal calibration appear in Mohamed et al. (2022), equations (8), (11), Theorem 7 and Table 1. The source reports simulated percentiles but does not supply the covariance-corrected variance, the explicit sharp inflation curve, or its Gaussian nominal-size implications. General uniform-spacing laws, including work of Huffer, provide established tools for calculating arbitrary linear-spacing distributions. Accordingly, the joint spacing law and general variance identity are **not claimed as new**. The specific quantitative consequence for the published Tsallis-order family, including its sharp universal distortion bound and limiting test size, is the assessed contribution. The earlier fractional-entropy uniformity paper (Mohamed et al., 2021) has different score weights; a 2024 fractional-generalized paper uses a different entropy profile. Neither inspected discussion states the present Tsallis-order ratio or resulting size formula.

## Limitations

The result is about the reported analytical normal approximation with its particular printed variance; an implementation using Monte Carlo-calibrated null quantiles is not subject to the same variance-based miscalibration. The result does not establish consistency or power against nonuniform alternatives, composite-null calibration, multivariate analogues, or validity for entropy orders changing with sample size. The general spacing technology is classical; whether an earlier correction elsewhere already derives the same specific sharp order-dependent ratio is a residual historical-priority question. No independent mathematical audit has been performed.

## References

1. M. S. Mohamed, H. M. Barakat, S. A. Alyami and M. A. Abd Elgawad (2022), *Cumulative Residual Tsallis Entropy-Based Test of Uniformity and Some New Findings*, Mathematics **10**, 771. DOI: https://doi.org/10.3390/math10050771 (first public journal version 2022-02-28).
2. M. S. Mohamed, H. M. Barakat, S. A. Alyami and M. A. Abd Elgawad (2021), *Fractional Entropy-Based Test of Uniformity with Power Comparisons*, Journal of Mathematics, 5331260. DOI: https://doi.org/10.1155/2021/5331260.
3. F. Huffer (1988), *Divided differences and the joint distribution of linear combinations of spacings*, Journal of Applied Probability **25**, 346–354; https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/divided-differences-and-the-joint-distribution-of-linear-combinations-of-spacings/F1EB7BE22C2395CFBCC8A2BE1EA7D96B.
4. A. M. Abd El-Latif, H. H. Sakr and M. S. Mohamed (2024), *Fractional generalized cumulative residual entropy: properties, testing uniformity, and applications to Euro Area daily smoker data*, AIMS Mathematics **9**, 18064–18082. DOI: https://doi.org/10.3934/math.2024881.

# Exact circular nearest-neighbor log-covariance and finite entropy-calibration variance

## Finding

Let \(n\ge3\) independent points be uniform on the unit-circumference circle. Choose one of the original sampling labels before seeing the point locations, and index the points in clockwise order starting from that point. Write \(\rho_i\) for the shortest circular distance from cyclic position \(i\) to another sample point, and set \(L_i=\log(2\rho_i)\). Define the universal constant
\[
C=\frac{\pi^2}{6}+2\operatorname{Li}_2(-1/2)
 =0.748105653000934\ldots,
\]
where \(\operatorname{Li}_2(z)=\sum_{k\ge1}z^k/k^2\) for \(|z|<1\). Let \(\psi_1(n)=\sum_{r=n}^{\infty}1/r^2\) denote the trigamma function at a positive integer, let \(I_n\) be the identity matrix, and let \(A_n\) be the adjacency matrix of the simple cycle on \(n\) vertices (for \(n=3\), the triangle). The complete covariance matrix is
\[
\operatorname{Cov}(L_1,\ldots,L_n)
 =\frac{\pi^2}{6}I_n+C A_n-\psi_1(n)\mathbf1\mathbf1^{\mathsf T}.
\tag{1}
\]
In particular, its diagonal entries are \(\pi^2/6-\psi_1(n)\), entries at distinct neighboring positions are \(C-\psi_1(n)>0\), and entries at distinct nonneighboring positions are \(-\psi_1(n)<0\) (the latter exist when \(n\ge4\)). Its Fourier eigenvalues are
\[
\lambda_0=\frac{\pi^2}{6}+2C-n\psi_1(n),\qquad
\lambda_j=\frac{\pi^2}{6}+2C\cos(2\pi j/n)
\quad(1\le j<n),
\tag{2}
\]
all strictly positive.

The finite-null corrected first-nearest-neighbor entropy estimator
\[
\widehat H_n=H_{n-1}+\frac1n\sum_{i=1}^n\log(2\rho_i),
\qquad H_{n-1}=\sum_{r=1}^{n-1}\frac1r,
\tag{3}
\]
is exactly unbiased for the uniform density (whose entropy in unit-circumference coordinates is zero), and
\[
\operatorname{Var}(\widehat H_n)
=\frac{\pi^2/2+4\operatorname{Li}_2(-1/2)}{n}-\psi_1(n),\qquad n\ge3.
\tag{4}
\]
Furthermore,
\[
\sqrt n\,\widehat H_n\ \xrightarrow{\mathrm d}\
N\!\left(0,\frac{\pi^2}{2}+4\operatorname{Li}_2(-1/2)-1\right),
\tag{5}
\]
with limiting variance \(2.141145372850094\ldots\). At \(n=2\), the two nearest-neighbor distances coincide, \(2\rho_1\sim\operatorname{Uniform}(0,1)\), and \(\operatorname{Var}(\widehat H_2)=1\).

## Assumptions and scope

Sampling is i.i.d. Haar-uniform on the circle \(\mathbb R/\mathbb Z\). The observations are distinct almost surely; the shortest geodesic distance is measured in units of circumference, not Euclidean chord distance. Equations (1) and (2) use an anchor chosen by sample label independently of the observed locations; deterministic cyclic shifts give the same matrix. The formula need not hold for an anchor picked by the geometry of the realized sample. For example, if position 1 is the clockwise initial endpoint of the shortest gap, then \(L_1=L_2\) almost surely, contrary to the strictly positive contrast variance in (1). Equation (4), and the centering and limit for the average, are unaffected by the choice of anchor. Equations (1), (2), and (4) apply to every integer \(n\ge3\), with the separately stated \(n=2\) case. No claim is made for nonuniform densities or higher-order nearest neighbors.

## Proof

**1. Uniform spacings and exact centering.** Conditional on the anchored point, the clockwise offsets of the other \(n-1\) points are independent uniform positions in \((0,1)\). Sorting them and taking differences, including the gaps to 0 and 1, gives a constant joint density on the gap simplex. Thus the clockwise gaps \(G_1,\ldots,G_n\) have the Dirichlet\((1,\ldots,1)\) law, represented by \(G_i=E_i/S\) with independent \(E_i\sim\operatorname{Exp}(1)\) and \(S=\sum_iE_i\sim\operatorname{Gamma}(n,1)\). The normalized vector \((G_i)\) is independent of \(S\). Let \(Y_i=\min(E_{i-1},E_i)\), with cyclic indices. Then \(\rho_i=Y_i/S\), and \(Y_i\sim\operatorname{Exp}(2)\). Consequently \(\mathbb E\log Y_i=-\gamma-\log2\) and \(\mathbb E\log S=\psi(n)=H_{n-1}-\gamma\), proving \(\mathbb EL_i=-H_{n-1}\). Independently, the Dirichlet simplex-volume identity yields
\[
\mathbb P(2\rho_i>t)=(1-t)^{n-1}\quad(0\le t\le1),
\]
so that \(2\rho_i\sim\operatorname{Beta}(1,n-1)\) for every \(n\ge2\). This also proves exact centering.

**2. The only local shared-exponential covariance.** \(\operatorname{Var}(\log Y_i)=\psi_1(1)=\pi^2/6\). Nonneighboring \(Y_i,Y_j\) involve disjoint exponentials and are independent; for neighbors, put \(Y=\min(A,B)\), \(Z=\min(B,D)\) for independent rate-one exponentials \(A,B,D\). Their joint survival function is \(\exp[-u-v-\max(u,v)]\), while the product of marginal survivals is \(\exp[-2u-2v]\). To obtain the logarithmic covariance identity, first use the representation \(\int_1^x du/u\) with \(x\) clipped to \([\epsilon,M]\) for \(0<\epsilon<1<M\). The resulting bounded indicator integrals give the survival covariance over \([\epsilon,M]^2\). The clipped logarithms converge in \(L^2\), and the survival covariance is nonnegative, so the double integral follows by monotone convergence. Splitting the integral into \(v\le u\) and \(u\le v\) and setting \(v=xu\) on the first region gives
\[
\begin{aligned}
\operatorname{Cov}(\log Y,\log Z)
&=\int_0^\infty\!\int_0^\infty
\frac{e^{-u-v-\max(u,v)}-e^{-2u-2v}}{uv}\,du\,dv\\
&=2\int_0^1\frac{\log(1+x)-\log(1+x/2)}{x}\,dx\\
&=2[-\operatorname{Li}_2(-1)+\operatorname{Li}_2(-1/2)]
=C,
\end{aligned}
\tag{6}
\]
using \(\operatorname{Li}_2(-1)=-\pi^2/12\).

**3. Removing the common random normalization.** Let \(Z_i=\log(Y_i/S)\). Since \(Z_i\) is a function of the Dirichlet vector, it is independent of \(S\). Hence \(\operatorname{Cov}(\log Y_i,\log S)=\operatorname{Var}(\log S)=\psi_1(n)\). Expanding the covariance of \(Z_i=\log Y_i-\log S\) and \(Z_j\) therefore subtracts exactly \(\psi_1(n)\) from every entry of the covariance matrix of the unnormalized \(\log Y_i\). For \(n\ge3\), the shared-exponential pairs are exactly the cycle neighbors, proving (1). Circulant diagonalization gives (2). A simple strict positivity argument is available: the alternating series gives \(\operatorname{Li}_2(-1/2)<-7/16\), so \(\pi^2/6-2C>7/4-\pi^2/6>0\). The constant eigenvalue is positive since \(n\psi_1(n)\le n/(n-1)\le3/2<\pi^2/6+2C\) for \(n\ge3\). Also \(C>\pi^2/6-1>\psi_1(3)\ge\psi_1(n)\), giving the strict neighboring-sign assertion. Nonneighbor covariance is strictly negative because \(\psi_1(n)>0\).

**4. Variance and Gaussian limit.** Averaging (1) proves (4), since each of the \(n\) rows has one diagonal and two neighbor terms. For the limit, write \(Y_i=\min(E_{i-1},E_i)\) and observe that \(\log S=\log n+(S-n)/n+o_{\mathbb P}(n^{-1/2})\). After centering, \(\sqrt n\widehat H_n\) equals, up to \(o_{\mathbb P}(1)\), the normalized sum of the stationary one-dependent variables \(W_i=\log Y_i-\mathbb E\log Y_i-(E_i-1)\). The cyclic closing term changes this sum by \(O_{\mathbb P}(1)\). Standard blocking proves the one-dependent central limit theorem because \(W_i\) has finite second moment. To evaluate its long-run variance, note that \(\operatorname{Cov}(\log\min(A,B),A+B)=1\) for independent rate-one exponentials (condition on the exponential minimum and independent excess, or differentiate the gamma Laplace transform). By symmetry, each cross-covariance with \(A\) or \(B\) is \(1/2\). Thus the long-run variance is \(\pi^2/6+2C+1-2=\pi^2/6+2C-1\), proving (5). Finally \(\psi_1(n)\sim1/n\), consistently giving \(n\operatorname{Var}(\widehat H_n)\to\pi^2/6+2C-1\).

## Verification

The standalone program `verify.py` evaluates \(\operatorname{Li}_2(-1/2)\) by its absolutely convergent power series and evaluates the shared-minimum covariance by an independent one-dimensional Simpson quadrature. It checks the closed forms and the strict spectral lower bound, then simulates independent exponential representations at \(n=2,3,4,5,10,25\), comparing empirical means and variances to the theorem. It separately checks all six cyclic covariance lags at \(n=6\). With its documented fixed seed, all checks pass. These Monte Carlo and quadrature checks are corroboration, not the proof of the statements for every \(n\); the preceding algebra and one-dependent limit argument supply that proof. Execute with `python3 verify.py` (Python standard library only).

## Relationship to prior work

Jiao, Gao and Han (2017) study nearest-neighbor entropy estimation on a torus and establish distribution-class risk bounds; their analysis does not provide this exact uniform-null finite covariance matrix. Misra, Singh and Hnizdo (2010) define circular nearest-neighbor entropy estimators and prove consistency (and vanishing variance), not the complete finite-null log-distance covariance matrix. Delattre and Fournier (2016) prove general asymptotic normality for Euclidean nearest-neighbor entropy estimators and evaluate the dimension-one inflation constant numerically near \(2.14\). Berrett, Samworth and Yuan (2019) also tabulate that already-known asymptotic constant near \(2.14\); its numerical value, the estimator family, and generic CLT methodology are explicitly **not** claimed as new. Cadirci and coauthors (2022) address consistency and Monte Carlo calibration for generalized Gaussian entropy-based tests. The precise proposed advance is the **finite-sample circular covariance matrix**, its opposite-sign local/global dependence and Fourier spectrum, and the corresponding exact finite-null variance and closed analytic specialization; no claim of a new general theory of nearest-neighbor entropy is made.

## Limitations

The statistic uses intrinsic circular arc length. The exact formulas assume i.i.d. uniform sampling, and a density-dependent generalization is not established. The variance and Gaussian limit characterize the estimator under the null, not exact finite-sample quantiles, nominal coverage, or performance under alternatives. The nearest-neighbor estimator and the asymptotic variance constant around \(2.14\) predate this result; their rediscovery is not the novelty claim. Historical priority against any overlooked earlier exact formulas remains open pending independent literature assessment. Numerical tests have finite scope, but the proof is analytical. No independent scientific audit is claimed.

## References

- Jiao, J., Gao, W. and Han, Y. (2017), *The Nearest Neighbor Information Estimator is Adaptively Near Minimax Rate-Optimal*, first posted 2017-11-23, https://arxiv.org/abs/1711.08824.
- Misra, N., Singh, H. and Hnizdo, V. (2010), *Nearest Neighbor Estimates of Entropy for Multivariate Circular Distributions*, *Entropy* 12, 1125–1144, https://doi.org/10.3390/e12051125.
- Delattre, S. and Fournier, N. (2016), *On the Kozachenko-Leonenko entropy estimator*, first posted 2016-02-24, https://arxiv.org/abs/1602.07440.
- Berrett, T. B., Samworth, R. J. and Yuan, M. (2019), *Efficient multivariate entropy estimation via k-nearest neighbour distances*, *Annals of Statistics* 47, 288–318, https://doi.org/10.1214/18-AOS1688.
- Cadirci, M. S., Evans, D., Leonenko, N. and Makogin, V. (2022), *Entropy-based test for generalized Gaussian distributions*, *Computational Statistics & Data Analysis* 173, 107502, https://doi.org/10.1016/j.csda.2022.107502.

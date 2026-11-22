# A universal three-observation chi-square limit for a spherical characteristic-function test

## Finding

Consider the sphere-integrated normality-and-independence statistic of Ejsmont, Milošević and Obradović, with column-wise sample standardization as in the published formulation. Divide the original surface integral by the surface area of its integration sphere; this positive deterministic normalization leaves every right-tail test and its critical-value decisions unchanged. At a fixed number \(N\geq2\) of observations, with the coordinate dimension \(m\to\infty\), its normalized statistic converges to the same explicit constant for **every atomless i.i.d. coordinate law**.

At the smallest sample size with nonconstant sample-shape geometry, \(N=3\), the first nonvanishing fluctuation is also universal. With \(c=e^{-1/2}\), \(h=e^{-1/3}\), put

\[
C_3=3\left[\left(\frac{1+2c}{3}\right)^2-2ch+c^2\right],\qquad
\beta=c\left(-\frac16-\frac{2c}{3}+\frac h3\right),\qquad
\gamma=\frac c{24}(1+2c-h)>0.
\]

For the sphere-area-normalized statistic \(T_{m,3}\),

\[
\boxed{\quad m(T_{m,3}-C_3)\ \xrightarrow{d}\ \beta+\gamma\chi_2^2\quad}
\]

under every atomless i.i.d. scalar coordinate distribution, Gaussian or not. Numerically \(C_3=0.128595873650625\ldots\), \(\beta=-0.201475334564041\ldots\), and \(\gamma=0.037820472231185\ldots\). Thus any Gaussian-null-calibrated right-tail rejection rule using this statistic with asymptotic size \(\alpha\in(0,1)\) has limiting rejection probability **exactly \(\alpha\)** against each fixed atomless i.i.d. non-Gaussian marginal, including the product uniform distribution. Nevertheless the full Gaussian and product-uniform samples are asymptotically perfectly separable in total variation as dimension grows.

## Assumptions and scope

Fix an integer \(N\geq2\). Let \(X_{ik}\), \(1\leq i\leq N\), \(1\leq k\leq m\), be independent with a common atomless distribution \(F\) on \(\mathbb R\). No population moments are required. For each coordinate \(k\), define

\[
\bar X_k=N^{-1}\sum_iX_{ik},\qquad
s_k^2=(N-1)^{-1}\sum_i(X_{ik}-\bar X_k)^2,\qquad
z_{ik}=(X_{ik}-\bar X_k)/s_k.
\]

Atomlessness implies \(s_k>0\) almost surely. Write \(z_i=(z_{i1},\ldots,z_{im})\), and let \(d\omega_{2m-1}\) be ordinary Euclidean surface measure on the unit sphere \(S^{2m-1}\subset\mathbb R^{2m}\), with area \(A_m=2\pi^m/\Gamma(m)\). Set

\[
T_{m,N}=\frac{N}{A_m}\int_{S^{2m-1}}
\left|\frac1{N^2}\sum_{i,j=1}^N
\exp\{i(\langle a,z_i\rangle+\langle b,z_j\rangle)\}-e^{-1/2}\right|^2d\omega_{2m-1}(a,b).
\]

This is the published \(M_m\) divided by \(A_m\); if one uses normalized surface measure in the definition instead, it is already \(T_{m,N}\). Only this fully spherical, coordinate-wise sample-standardized statistic is considered, with \(N\) fixed and \(m\to\infty\). The original paper instead studies fixed dimension with growing sample size.

For general \(N\), define \(p=(N-1)/N\), \(q=1/N\) and \(c=e^{-1/2}\). The deterministic limit is

\[
\boxed{\quad C_N=N\big[(q+pc)^2-2c\exp(-p/2)+c^2\big].\quad}
\]

The \(N=3\) law above is a sharper, second-order assertion. It is not claimed for \(N>3\), for dependent coordinates, or for \(N\) growing with \(m\).

## Proof

**1. Exact spherical kernel.** Let \(G=m^{-1}ZZ^\top\) be the \(N\times N\) Gram matrix of the standardized rows, \(d_i=G_{ii}\), and \(D_{ij}=d_i+d_j-2G_{ij}\). If \(U\) is uniform on \(S^{2m-1}\), rotational invariance and the spherical moment expansion give

\[
H_m(x)=\mathbb E\exp\bigl(i\sqrt{mx}\,U_1\bigr)
={}_0F_1(;m;-mx/4)
=\sum_{r=0}^\infty\frac{(-mx/4)^r}{r!(m)_r}.
\]

Expansion of the squared absolute value in the definition of \(T_{m,N}\), without any independence assumption on the two sphere blocks \(a,b\), gives the **exact finite-dimensional identity**

\[
T_{m,N}=N\left[\frac1{N^4}\sum_{i,j,k,l}
H_m(D_{ij}+D_{kl})
-\frac{2c}{N^2}\sum_{i,j}H_m(d_i+d_j)+c^2\right].\tag{1}
\]

To control the dimension limit, observe that each standardized column has zero sum and squared length \(N-1\). Hence \(G\mathbf1=0\), \(\operatorname{tr}G=N-1\), and \(0\leq d_i,D_{ij}\leq4(N-1)\) (a crude uniform bound suffices). Writing \((m)_r=m^r\prod_{j=0}^{r-1}(1+j/m)\), Taylor's theorem and the bound \(|\frac{d^2}{dt^2}\prod_{j=0}^{r-1}(1+jt)^{-1}|\leq C r^4\) for \(t\geq0\) yield, uniformly on every bounded interval of \(x\geq0\),

\[
H_m(x)=e^{-x/4}\left(1-\frac{x^2}{32m}\right)+O(m^{-2}).\tag{2}
\]

The bound is valid after summing the absolutely convergent exponential series, since \(\sum_r r^4B^r/r!<\infty\) for every finite \(B\).

**2. The universal leading limit.** The standardized columns are independent and exchangeable across their \(N\) rows. Their second-moment matrix has diagonal \((N-1)/N\) and off-diagonal \(-1/N\), solely because every column sums to zero, has squared length \(N-1\), and its law is row-exchangeable. Consequently the strong law for bounded matrices gives

\[
G\ \xrightarrow{\mathrm{a.s.}}\ P_N=I_N-\frac1N\mathbf1\mathbf1^\top.
\]

At this limit \(d_i=p\), and \(D_{ij}=2\) if \(i\ne j\), or \(0\) if \(i=j\). Applying (1) and (2) yields \(T_{m,N}\to C_N\) almost surely. For \(N=2\) the Gram matrix is exactly \(P_2\) at every dimension, explaining why \(N=3\) is the first nonconstant sample-shape case.

**3. Exact two-dimensional Gram tangent at three observations.** Now \(N=3\) and \(P=P_3\). Since \(G-P\) is symmetric with zero row sums and zero trace, it has the exact form

\[
G-P=\begin{pmatrix}
 a&d&b\\ d&b&a\\ b&a&d
\end{pmatrix},\qquad a+b+d=0.
\]

In particular \(\|G-P\|_F^2=3(a^2+b^2+d^2)\) and, for the three unordered off-diagonal pairs, \(D_{ij}=2-3d,2-3b,2-3a\), respectively. Define

\[
A(G)=\frac1{9}\sum_{i,j}e^{-D_{ij}/4},\qquad
B(G)=\frac13\sum_i e^{-d_i/4},\qquad
\mathcal F(G)=3[A(G)^2-2cB(G)^2+c^2].
\]

At \(P\), \(A(P)=(1+2c)/3\) and \(B(P)^2=h\). Direct Taylor expansion using \(a+b+d=0\) gives

\[
A(G)=\frac{1+2c}{3}+\frac c{16}(a^2+b^2+d^2)+O(\|G-P\|_F^3),
\]

\[
B(G)=e^{-1/6}\left[1+\frac1{96}(a^2+b^2+d^2)
+O(\|G-P\|_F^3)\right].
\]

Therefore

\[
\mathcal F(G)=C_3+\frac c8(1+2c-h)(a^2+b^2+d^2)
+O(\|G-P\|_F^3)
=C_3+\gamma\|G-P\|_F^2+O(\|G-P\|_F^3).\tag{3}
\]

**4. Universal Gram central limit theorem.** A single standardized column \(z=(z_1,z_2,z_3)^\top\) belongs to the plane \(\mathbf1^\perp\) and satisfies \(\|z\|^2=2\). Let \(W=zz^\top-P\). It is a symmetric, trace-zero endomorphism of that plane. Exactly, \(\mathbb EW=0\), and \(\|W\|_F^2=2\) for every column. The real space of such endomorphisms is two-dimensional. Cyclic row permutation rotates \(\mathbf1^\perp\) by \(120^\circ\), so conjugation rotates this two-dimensional endomorphism space by \(240^\circ\). Row exchangeability forces the covariance of \(W\) to commute with this nontrivial rotation. Because covariance is symmetric, it must be a scalar matrix; the fixed expected squared Frobenius norm \(2\) forces that scalar to be exactly \(1\). Thus in any Frobenius-orthonormal basis the two coordinates of \(W\) have covariance \(I_2\), regardless of \(F\). Independence across columns and the bounded-vector central limit theorem give

\[
\sqrt m\,(G-P)=\frac1{\sqrt m}\sum_{k=1}^mW_k\ \xrightarrow{d}\ Z,
\qquad \|Z\|_F^2\sim\chi_2^2.\tag{4}
\]

Here \(Z\) is a standard Gaussian element in that two-dimensional space, not a Gaussian sample matrix.

**5. Spherical-curvature term and final limit.** Substituting (2) into (1) gives

\[
T_{m,3}=\mathcal F(G)+m^{-1}\mathcal B(G)+O(m^{-2}),
\]

uniformly over all attainable Gram matrices. The function \(\mathcal B\) is continuous and at \(G=P\) is evaluated by counting the diagonal and off-diagonal pairs. With \(p=2/3,q=1/3\),

\[
\mathcal B(P)=3\left[-\frac{8pq c+16p^2c^2}{32}
+\frac{8cp^2h}{32}\right]
=c\left(-\frac16-\frac{2c}{3}+\frac h3\right)=\beta.\tag{5}
\]

From (3), (4), (5), \(G-P=O_p(m^{-1/2})\) and the continuous-mapping theorem,

\[
m(T_{m,3}-C_3)=\beta+\gamma\|\sqrt m(G-P)\|_F^2+o_p(1)
\xrightarrow{d}\beta+\gamma\chi_2^2.
\]

The limit has a continuous strictly increasing distribution on its support because \(\gamma>0\). If \(t_{m,\alpha}\) is a Gaussian-null right-tail cutoff with rejection probability approaching \(\alpha\), then

\[
m(t_{m,\alpha}-C_3)\longrightarrow\beta-2\gamma\log\alpha.
\]

Applying the same distributional limit under any atomless \(F\) shows that its limiting rejection probability is \(\alpha\). For an explicit separated alternative, take \(F=\mathrm{Unif}[-\sqrt3,\sqrt3]\). Its one-coordinate Hellinger affinity with \(N(0,1)\) is

\[
\rho=\frac{2\sqrt\pi\,\operatorname{erf}(\sqrt3/2)}{
\sqrt{2\sqrt3\sqrt{2\pi}}}=0.937530249142826\ldots<1.
\]

The full samples consist of \(3m\) independent scalar observations, so their total-variation distance is at least \(1-\rho^{3m}\to1\). This proves the stated complete separation without affecting the test-statistic conclusion.

## Verification

The standalone `check.py` evaluates the exact finite-dimensional spherical kernel by both a hypergeometric series interface and Jacobi quadrature, compares the one-dimensional integral with the published Bessel formula, checks the Gram tangent identities and second-order expansion, and numerically compares the two-dimensional column covariance under Gaussian, uniform, and Laplace sampling. Reproduction command from the extracted package directory: `python check.py` (Python 3 with NumPy and SciPy). An actual replay returned `CHECKS PASSED: 267` with constants \(C_3=0.128595873650625\), \(\beta=-0.201475334564041\), and \(\gamma=0.037820472231185\). The analytic identities and bounded-vector central limit theorem, not simulations or finite checks, prove the infinite-dimensional claim.

## Relationship to prior work

The statistic is defined in Ejsmont, Milošević and Obradović (2021 preprint; 2022 online journal version), specifically the column-standardized sphere integral. The authors establish a distributional characterization, study fixed-dimensional/sample-size asymptotics and finite-dimensional simulated power. Those results do not imply the fixed-three-observation, growing-coordinate second-order \(\chi^2_2\) limit or its alternative-side power statement. Baringhaus and Henze (1988) study a different Gaussian empirical-characteristic-function test using covariance-matrix whitening; Chen and Xia (2019) propose a different high-dimensional nearest-neighbor normality test. Neither gives this statistic's dimension-growth calibration. General spherical concentration and standard multivariate CLTs are mathematical ingredients rather than pre-existing statements of the explicit test-specific constants.

## Limitations

The result assumes independently and identically distributed scalar coordinates, independent across columns as well as observations. It does not address cross-coordinate dependence, unequal coordinate marginal laws, plug-in or approximate sphere integration, or simultaneous growth of sample size and dimension. The universal \(\chi^2_2\) second-order law is only established for three observations; for four or more observations, normalized-column fourth moments can vary with the marginal law. The asymptotic power statement concerns the right-tail test calibrated from its exact Gaussian null (or an asymptotically equivalent cutoff) and does not assert finite-dimensional equality of distributions. The observed-nulling phenomenon does not contradict ordinary fixed-dimension consistency as observation count grows. Historical priority beyond the specifically inspected texts remains open to independent scrutiny.

## References

1. W. Ejsmont, B. Milošević, M. Obradović, *A test for normality and independence based on characteristic function*, arXiv:2107.04845, first submitted 2021-07-10. https://arxiv.org/abs/2107.04845
2. W. Ejsmont, B. Milošević, M. Obradović, same work, *Statistical Papers* **64** (2023), 1861–1889, online published 2022-10-08. https://doi.org/10.1007/s00362-022-01365-1
3. L. Baringhaus and N. Henze, *A consistent test for multivariate normality based on the empirical characteristic function*, *Metrika* **35** (1988), 339–348. https://doi.org/10.1007/BF02613322
4. H. Chen and Y. Xia, *A Normality Test for High-dimensional Data based on a Nearest Neighbor Approach*, arXiv:1904.05289 (2019). https://arxiv.org/abs/1904.05289

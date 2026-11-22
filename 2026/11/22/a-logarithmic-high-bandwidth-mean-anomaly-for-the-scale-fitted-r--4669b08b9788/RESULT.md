# A logarithmic high-bandwidth mean anomaly for the scale-fitted Rayleigh Stein test

## Finding

Let \(n\ge2\) be fixed, let \(X_1,\ldots,X_n\) be independent Rayleigh observations with an arbitrary common scale \(\theta>0\), and set
\[
\widehat\theta^2=\frac1{2n}\sum_{i=1}^n X_i^2,\qquad Y_i=\frac{X_i}{\widehat\theta}.
\]
For \(t>0\), define the scale-fitted empirical Rayleigh fixed-point discrepancy
\[
\widehat\psi_n(t)=\frac1n\sum_{i=1}^n\left[\left(Y_i-Y_i^{-1}\right)\min(Y_i,t)-\mathbf 1_{\{Y_i\le t\}}\right]
\]
and the exponentially weighted goodness-of-fit statistic of Grobler, Bothma and Allison (2022),
\[
R_{n,a}=n\int_0^\infty\widehat\psi_n(t)^2e^{-at}\,dt,\qquad a>0.
\]
Define the random variable
\[
Z_n=\frac2n\left(\sum_{i=1}^n\left(Y_i-Y_i^{-1}\right)\right)^2,
\qquad c_n=\frac{n-1}{n}.
\]
Under this composite Rayleigh null, the following three statements hold:
\[
\boxed{a^3R_{n,a}\longrightarrow Z_n\quad\text{almost surely as }a\to\infty,}
\]
\[
\boxed{\lim_{z\to\infty}z\,\mathbb P(Z_n>z)=c_n,\quad
\mathbb E Z_n^q<\infty\ \Longleftrightarrow\ 0<q<1,}
\]
\[
\boxed{\mathbb E R_{n,a}=\frac{2c_n\log a+O_n(1)}{a^3}\quad (a\to\infty).}
\]
The null expectation of \(R_{n,a}\) is finite at every fixed \(a>0\). Hence the almost-sure high-bandwidth limit is not an \(L^1\) limit; the normalized means diverge logarithmically although the almost-sure limiting variable is finite.

## Assumptions and scope

The sample size is any fixed integer \(n\ge2\); the Rayleigh scale \(\theta\) is arbitrary but common to all independent observations; the estimator is exactly the maximum-likelihood scale estimator above. There is no approximation in the definition of the statistic. The bandwidth tends to infinity with \(n\) held fixed. All probabilistic statements refer to the fully specified *family* of Rayleigh null distributions after scale fitting, and are invariant under its unknown scale. They do not cover an alternative scale estimator or simultaneous growth of bandwidth and sample size. Only positive fractional moments are classified.

## Proof

**1. Exact normalized null distribution.** Under a Rayleigh law, \(E_i=X_i^2/(2\theta^2)\) are independent mean-one exponential variables. Consequently \(U_i=E_i/\sum_j E_j\) has the \(\operatorname{Dirichlet}(1,\ldots,1)\) distribution, with
\[
Y_i=\sqrt{2nU_i},\qquad 0<Y_i<\sqrt{2n},\qquad \sum_iY_i^2=2n.
\]
For \(n\ge2\), each marginal has density
\[
f_n(y)=c_n y\left(1-\frac{y^2}{2n}\right)^{n-2}\mathbf1_{\{0<y<\sqrt{2n}\}},
\qquad c_n=\frac{n-1}{n}.
\]
In particular, \(f_n(y)=c_ny+O_n(y^3)\) at the origin and
\[
\mathbb P(Y_i<\varepsilon)=\frac{c_n}{2}\varepsilon^2+O_n(\varepsilon^4).
\]
For distinct coordinates, \(\mathbb P(Y_i<\varepsilon,Y_j<\varepsilon)=O_n(\varepsilon^4)\): if \(n\ge3\), use the bounded two-coordinate Dirichlet density \((n-1)(n-2)(1-u-v)^{n-3}\) on \(u,v>0,u+v<1\); if \(n=2\), simultaneous small coordinates are impossible for sufficiently small \(\varepsilon\).

**2. Almost-sure normalization.** Set
\[
g_y(t)=(y-y^{-1})\min(y,t)-\mathbf1_{\{y\le t\}}.
\]
For \(t<y\), \(g_y(t)=t(y-y^{-1})\); for \(t\ge y\), \(g_y(t)=y^2-2\). Given a positive sample, there is a strictly positive minimum observation \(m=\min_iY_i\), so
\[
\widehat\psi_n(t)=\frac tn\sum_i(Y_i-Y_i^{-1})\qquad(0<t<m).
\]
Furthermore, for fixed \(n\), the ratio \(|g_y(t)|/t\) is bounded by \(C_n(1+y^{-1})\) for all \(0<y<\sqrt{2n}\), \(t>0\). Thus after the change of variable \(s=at\), dominated convergence yields
\[
a^3R_{n,a}=n\int_0^\infty s^2\left(\frac{\widehat\psi_n(s/a)}{s/a}\right)^2 e^{-s}\,ds
\longrightarrow\frac{n}{n^2}\left(\sum_i(Y_i-Y_i^{-1})\right)^2\int_0^\infty s^2e^{-s}\,ds=Z_n.
\]

**3. Sharp inverse-square tail.** Let \(W_i=Y_i^{-1}\). The marginal density expansion gives
\[
\mathbb P(W_i>r)=\frac{c_n}{2r^2}+O_n(r^{-4}),\qquad
\mathbb P(W_i>r,W_j>r)=O_n(r^{-4})\quad(i\ne j).
\]
For fixed \(n\), these bounds show the one-large-coordinate rule
\[
\mathbb P\left(\sum_iW_i>r\right)\sim\sum_i\mathbb P(W_i>r)
=\frac{nc_n}{2r^2}.
\]
For completeness, the lower bound follows from the union of \(\{W_i>r\}\). For any fixed \(\delta>0\), on the event that \(\sum_i W_i>r\) but \(\max_iW_i\le(1-\delta)r\), at least two distinct coordinates exceed fixed positive multiples of \(r\). Its probability is \(O_{n,\delta}(r^{-4})\). The upper bound therefore uses \(\max_iW_i>(1-\delta)r\), and letting \(\delta\downarrow0\) proves the equivalence. Since \(0<\sum_iY_i\le n\sqrt{2n}\), the random sum \(\sum_i(Y_i-Y_i^{-1})\) differs from \(-\sum_iW_i\) by a bounded quantity, which does not change its tail constant. Substituting \(r=\sqrt{nz/2}\) proves
\[
\mathbb P(Z_n>z)\sim \frac{c_n}{z}.
\]
For positive \(q\), the layer-cake identity \(\mathbb E Z_n^q=q\int_0^\infty z^{q-1}\mathbb P(Z_n>z)\,dz\) proves precisely the asserted moment threshold.

**4. Logarithmic mean asymptotic.** For fixed \(t>0\), use \(\widehat\psi_n(t)=n^{-1}\sum_ig_{Y_i}(t)\). The diagonal second moment is
\[
\mathbb E[g_{Y_i}(t)^2]=t^2\int_t^{\sqrt{2n}}(y-y^{-1})^2f_n(y)\,dy
+\int_0^t(y^2-2)^2f_n(y)\,dy
=c_nt^2\log(1/t)+O_n(t^2)
\]
as \(t\downarrow0\). The logarithm comes solely from \(y^{-2}f_n(y)\sim c_n/y\); the remaining terms are integrable. Every off-diagonal second moment is \(O_n(t^2)\). Indeed, \(|g_y(t)|/t\le C_n(1+y^{-1})\), while \(\mathbb E[(1+Y_i^{-1})(1+Y_j^{-1})]<\infty\) for \(i\ne j\). For \(n\ge3\), this follows from the bounded two-coordinate Dirichlet density and integrability of \((uv)^{-1/2}\). For \(n=2\), it follows from \(U_2=1-U_1\) and the beta integral \(\int_0^1[u(1-u)]^{-1/2}\,du<\infty\). Thus
\[
\mathbb E[\widehat\psi_n(t)^2]=\frac{c_n}{n}t^2\log(1/t)+O_n(t^2).
\]
All \(g_y(t)\), and hence \(\widehat\psi_n(t)\), are uniformly bounded in \(t\) and \(y\) for fixed \(n\). Tonelli's theorem and an elementary Laplace estimate now give
\[
\begin{aligned}
\mathbb E R_{n,a}&=n\int_0^\infty e^{-at}\mathbb E\widehat\psi_n(t)^2\,dt\\
&=c_n\int_0^\infty e^{-at}t^2\log(1/t)\,dt+O_n(a^{-3})\\
&=\frac{2c_n\log a+O_n(1)}{a^3}.
\end{aligned}
\]
The integral in the middle line is understood with any fixed small cut-off, whose complement is exponentially negligible; extending \(t^2\log(1/t)\) to the full positive axis changes only the exponentially negligible remainder. More precisely, its complete Laplace integral is \(a^{-3}(2\log a-\Gamma'(3))\). Since \(\mathbb E Z_n=\infty\) by step 3 but \(\mathbb E R_{n,a}<\infty\) for each \(a\), convergence in \(L^1\) is impossible. This completes the proof.

## Verification

The standalone file `checker.py` numerically integrates the exactly normalized \(n=2\) Dirichlet law, checks small-\(t\) diagonal and cross contributions through direct one-dimensional integration, checks the logarithmic expectation coefficient at four increasing bandwidths, verifies the almost-sure scaling on four deterministic samples, and checks the limiting tail coefficient through one-dimensional root finding. It completed 25 numerical assertions in the recorded run. These are finite corroborations; the all-\(n\) proof is given above. Run with `python checker.py` using Python, NumPy and SciPy.

For \(n=2\), the independent quadrature gave \(a^3\mathbb E R_{2,a}/\log a=1.05857006,1.04553800,1.03766581,1.03211248\) at \(a=30,80,200,500\) respectively, compared with the proven limiting coefficient \(2c_2=1\). Independent inversion of the exact \(n=2\) tail gave \(z\,\mathbb P(Z_2>z)=0.454918246,0.485236969,0.498502375\) at \(z=10^3,10^4,10^6\), compared with the proven limit \(c_2=1/2\).

## Relationship to prior work

Grobler, Bothma and Allison (2022), Section 2, equation (5), define exactly the scale-fitted weighted statistic and, in Section 3, obtain its null limit as \(n\to\infty\) at fixed positive bandwidth. The statistic, its Stein characterization, and the MLE normalization are not new. Their paper does not establish the fixed-\(n\), high-bandwidth asymptotic mean, the heavy-tailed sample-path endpoint, or their non-interchangeability. Betsch and Ebner (2018) developed the more general fixed-point characterization framework and weighted goodness-of-fit methodology, without specifying this Rayleigh statistic's sharp high-bandwidth moment law. The gamma and normal fixed-point goodness-of-fit papers address different statistical models and do not imply the three numerical coefficients for this normalized Rayleigh null without the Dirichlet and singular-boundary calculations above. A general Abelian Laplace argument, if applied, handles the integration step but not the model-specific small-\(t\) expansion and one-large-coordinate tail coefficient.

## Limitations

The limit concerns fixed sample size and tuning parameter tending to infinity; it is not a simultaneous large-sample theorem or an assertion about power. The almost-sure limit is not a valid finite-mean calibration reference. The \(O_n(1)\) remainder in the mean is not claimed uniform in \(n\). No claim is made about optimal bandwidth selection, resampling calibration, or tests using a different scale estimator. Historical priority under more general singular Stein-discrepancy theory remains to be independently checked.

## References

1. G. L. Grobler, E. Bothma and J. S. Allison, "Testing for the Rayleigh Distribution: A New Test with Comparisons to Tests for Exponentiality Based on Transformed Data," *Mathematics* **10** (2022), 1316, published 15 April 2022. https://doi.org/10.3390/math10081316 ; https://www.mdpi.com/2227-7390/10/8/1316 .
2. S. Betsch and B. Ebner, "Fixed point characterizations of continuous univariate probability distributions and their applications," arXiv:1810.06226, first posted 15 October 2018; *Annals of the Institute of Statistical Mathematics* **73** (2021), 31–59. https://arxiv.org/abs/1810.06226 .
3. S. Betsch and B. Ebner, "A new characterization of the Gamma distribution and associated goodness of fit tests," arXiv:1806.06028, first posted 15 June 2018. https://arxiv.org/abs/1806.06028 .
4. S. Betsch and B. Ebner, "Testing normality via a distributional fixed point property in the Stein characterization," arXiv:1803.07069, first posted 19 March 2018. https://arxiv.org/abs/1803.07069 .

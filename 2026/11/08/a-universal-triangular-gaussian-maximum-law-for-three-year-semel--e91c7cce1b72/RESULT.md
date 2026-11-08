# A universal triangular Gaussian-maximum law for three-year semelparous cohorts

## Finding

For a three-stage semelparous population in a stationary two-state Markov environment, the centered logarithm of total population at times divisible by three converges, after square-root scaling, to **an independent Gaussian plus the maximum of three Gaussian rays separated by exactly \(120^\circ\)**. Its non-Gaussian part has a universal triangular-extreme law and exact universal expected-growth correction.

Write \(\pi_0=b/(a+b)\), \(\pi_1=a/(a+b)\), \(\theta=1-a-b\) for the environment defined below. Define the environmental log-rate contrasts
\[
u=\log(F_1/F_0),\quad v=\log(s_1/s_0),\quad w=\log(t_1/t_0),\quad \bar d=(u+v+w)/3,
\]
\[
D=(u-\bar d)^2+(v-\bar d)^2+(w-\bar d)^2,
\qquad\mu=\sum_{e=0}^1\pi_e\log(F_es_et_e).
\]
Set
\[
\sigma_0^2=\frac{\pi_0\pi_1}{9}(u+v+w)^2\frac{1+\theta}{1-\theta},\qquad
\sigma_1^2=\frac{\pi_0\pi_1D}{3}\frac{1-\theta^2}{1+\theta+\theta^2}.
\]
For every positive initial three-stage population, as \(n\to\infty\) through multiples of three,
\[
\boxed{\frac{\log M_n-n\mu/3}{\sqrt n}\xrightarrow{d}\sigma_0Z_0+\sigma_1\max\!\left\{Z_1,-\frac{Z_1}{2}+\frac{\sqrt3Z_2}{2},-\frac{Z_1}{2}-\frac{\sqrt3Z_2}{2}\right\}},
\]
where \(Z_0,Z_1,Z_2\) are independent standard normals. Furthermore,
\[
\lim_{3\mid n,\ n\to\infty}\frac{\log M_n}{n}=\frac\mu3\quad\text{almost surely},
\qquad\boxed{\mathbb E\log M_n=\frac{n\mu}{3}+\frac{3\sqrt3}{2\sqrt{2\pi}}\,\sigma_1\sqrt n+o(\sqrt n)}.
\]
When \(D>0\), the limiting distribution is non-Gaussian; when \(D=0\), it is Gaussian (possibly a point mass). Both static environments may be exactly growth-neutral even though \(D>0\), causing a nontrivial universal positive fluctuation correction invisible to the leading exponential growth rate.

## Assumptions and scope

Let \(\xi_1,\xi_2,\ldots\) be a stationary Markov chain on \(\{0,1\}\) with row-stochastic transition matrix
\[
P=\begin{pmatrix}1-a&a\\b&1-b\end{pmatrix},\qquad0<a,b<1.
\]
For each state \(e\), take fecundity \(F_e>0\) and stage survivals \(0<s_e,t_e\le1\). The population vector \((X_n,Y_n,Z_n)^\top\) evolves from strictly positive initial coordinates under
\[
A_e=\begin{pmatrix}0&0&F_e\\s_e&0&0\\0&t_e&0\end{pmatrix},\qquad z_n=A_{\xi_n}z_{n-1},\qquad M_n=X_n+Y_n+Z_n.
\]
Each stage advances exactly one year, while the final stage reproduces once and does not persist. Positive initial coordinates avoid exceptional single-brood behavior. Only observations after complete three-year life cycles are covered. There is no demographic sampling noise or density dependence.

## Proof

**1. Exact three-cohort product.** For \(n=3m\), multiply each successive triple of off-diagonal matrices. The initial \(X\)-brood multiplies in years \(3j-2,3j-1,3j\) by \(s_{\xi_{3j-2}}t_{\xi_{3j-1}}F_{\xi_{3j}}\). The initial \(Y\)-brood multiplies by \(t_{\xi_{3j-2}}F_{\xi_{3j-1}}s_{\xi_{3j}}\), and the initial \(Z\)-brood by \(F_{\xi_{3j-2}}s_{\xi_{3j-1}}t_{\xi_{3j}}\). Thus the logarithms of the three contributions are exact additive sums with three cyclically rotated period-three coefficient vectors.

**2. Centering and Markov spectral covariance.** Put \(h_j=\boldsymbol1_{\{\xi_j=1\}}-\pi_1\). The three branch logarithms, minus \(n\mu/3\), have a common term \(C_n=\bar d\sum_{j=1}^n h_j\) plus three contrast terms \(U_{k,n}\). The contrast weight sequences, indexed by year modulo three, are cyclic rotations of \((u-\bar d,v-\bar d,w-\bar d)\), so their coordinatewise sum is zero. For the stationary two-state chain,
\[
\operatorname{Cov}(h_j,h_{j+k})=\pi_0\pi_1\theta^{|k|}.
\]
The Fourier power spectrum of this covariance at frequency \(0\) is \((1+\theta)/(1-\theta)\), whereas at frequencies \(\pm2\pi/3\) it is \((1-\theta^2)/(1+\theta+\theta^2)\). Orthogonality of the periodic weights therefore yields limiting covariance per year \(\sigma_0^2\) for the common term, \(\sigma_1^2\) for each contrast, \(-\sigma_1^2/2\) for distinct contrasts and zero for every common/contrast pair.

For completeness, the three-coordinate central limit theorem follows by the bounded Markov martingale differences \(\eta_j=h_j-\theta h_{j-1}\). Any weighted sum with period-three deterministic coefficients is a bounded-coefficient linear combination of these martingale differences plus a uniformly bounded boundary term. The three-step skeleton of the chain is ergodic, so normalized conditional quadratic variations converge to the covariance values above. The bounded martingale vector CLT then gives an independent common normal and a planar isotropic normal with three equally spaced projections. This proves the joint limit of the three branch logarithms.

**3. Total population and non-Gaussian shape.** Since each initial brood is strictly positive, its fixed initial logarithmic weight is negligible at square-root scale. For any three real branch logarithms, the logarithm of their exponential sum differs from their maximum by a number between zero and \(\log3\). The continuous mapping theorem gives the displayed Gaussian-plus-triangular-maximum limit. If \(D>0\), the maximum is nondegenerate and supported on the positive half-line (the three projections sum to zero), hence it is not Gaussian; by independence and the Gaussian decomposition theorem, adding the independent Gaussian does not make it Gaussian.

**4. Mean correction and rate.** The covariance identity above makes the centered, square-root-scaled branch sums uniformly bounded in second moment; the maximum and bounded log-sum remainder consequently give uniform integrability. In polar coordinates \((Z_1,Z_2)=R(\cos\phi,\sin\phi)\), \(\mathbb ER=\sqrt{\pi/2}\), and the largest of the three projections equals \(R\cos\delta\), where the angular distance \(\delta\) to the nearest of three rays is uniform over \([-\pi/3,\pi/3]\). Its mean is therefore
\[
\sqrt{\frac\pi2}\,\frac3{2\pi}\int_{-\pi/3}^{\pi/3}\cos\delta\,d\delta=\frac{3\sqrt3}{2\sqrt{2\pi}}.
\]
The expectation expansion follows. Ergodicity on each residue class modulo three yields \(C_n/n\to0\), \(U_{k,n}/n\to0\) almost surely; the leading log growth is \(\mu/3\).

**5. Neutral-static example.** Choose \((F_0,s_0,t_0)=(4,1/2,1/2)\), \((F_1,s_1,t_1)=(8,1/4,1/2)\), with \(a=b=2/5\). Each static projection has spectral radius \((F_es_et_e)^{1/3}=1\), so \(\mu=0\), but \((u,v,w)=(\log2,-\log2,0)\) gives \(D=2(\log2)^2>0\), hence a strictly positive triangular-maximum correction to the expected log population. The expression is nontrivial despite neutral stationary growth in both constituent environments.

## Verification

Run `python verify3.py` with Python 3 standard library. Exhaustive rational arithmetic verifies the exact three-cohort path products for two parameter configurations and every binary environmental word of lengths three, six, nine and twelve (9,360 paths). Separate exact-rational enumeration verifies all nine entries of the Markov period-three contrast covariance matrix for lengths three, six and nine (27 identities). The executable reports 9,387 passing checks. These finite checks do not replace the all-horizon Markov spectral and martingale proof.

## Relationship to prior work

Logofet, Golubyatnikov and Ulanova (2020) analyze weather-calibrated Markov selection of annual population projection matrices and its effect on numerical stochastic-growth estimation. Sanz (2019) studies growth/extinction bounds for stochastic Leslie matrices. Diekmann and Planqué (2019) identify ecological mechanisms of brood synchronization in semelparous life cycles. A previous two-cohort fluctuation result concerns a two-stage model whose non-Gaussian law is folded normal; it does not imply the triple-cohort limiting covariance geometry, its universal triangular maximum or its \(3\sqrt3/(2\sqrt{2\pi})\) expected-value constant. Ordinary Markov additive-functional CLTs are proof ingredients rather than prior theorems about this three-branch total-population observable.

## Limitations

Only a two-state stationary Markov environment, positive three-stage semelparous life cycle, and observation times divisible by three are proved. The result does not cover brood competition from density dependence, irregular life-cycle durations or demographic stochasticity. There may be unindexed or differently named general theorems on imprimitive random matrix products; independent expert priority and correctness audits have not been performed.

## References

1. D. O. Logofet, L. L. Golubyatnikov and N. G. Ulanova, “Realistic Choice of Annual Matrices Contracts the Range of \(\lambda_S\) Estimates”, *Mathematics* **8** (2020), 2252. https://doi.org/10.3390/math8122252 (first public December 20, 2020).
2. L. Sanz, “Conditions for growth and extinction in matrix models with environmental stochasticity”, *Ecological Modelling* **411** (2019), 108797. https://doi.org/10.1016/j.ecolmodel.2019.108797 ; full text https://arxiv.org/abs/2402.03827 .
3. O. Diekmann and R. Planqué, “The winner takes it all: how semelparous insects can become periodical”, *Journal of Mathematical Biology* **80** (2020), 283–301; first published April 27, 2019. https://doi.org/10.1007/s00285-019-01362-3 .

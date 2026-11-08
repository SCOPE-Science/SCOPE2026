# Sharp Gaussian importance scales for independently stratified quadratic integration

## Finding

Let the target be the standard normal distribution, and estimate its second moment with one independently randomized point in each of \(N\) equal probability strata of a centered Gaussian proposal of variance \(s>0\). For \(N\ge1\), set \(U_j\sim\operatorname{Unif}((j-1)/N,j/N)\), independently for \(j=1,\ldots,N\), let \(z_j=\Phi^{-1}(U_j)\), and define
\[
Q_{N,s}=\frac1N\sum_{j=1}^{N}s^{3/2}z_j^2\exp\!\left(\frac{1-s}{2}z_j^2\right).
\]
Here \(\Phi\) is the standard normal cumulative distribution function. This is the ordinary importance-weighted estimate of \(\int_{\mathbb R}x^2\phi(x)\,dx=1\), using proposal \(N(0,s)\). It is unbiased for every \(s>0\) and \(N\ge1\).

The exact asymptotic variance classification is
\[
\begin{cases}
\operatorname{Var}(Q_{N,s})=+\infty\quad\text{for every }N,&0<s\le\tfrac12,\\[2mm]
\lim_{N\to\infty}N^3\operatorname{Var}(Q_{N,s})=+\infty,&\tfrac12<s\le\tfrac32,\\[2mm]
\lim_{N\to\infty}N^3\operatorname{Var}(Q_{N,s})=C(s),&s>\tfrac32,
\end{cases}
\]
where, in the finite regime,
\[
\boxed{C(s)=\frac{\pi s^3(7s^2-18s+15)}{48\sqrt2\,(s-\frac32)^{7/2}}.}
\]
The unique scale attaining the smallest finite asymptotic coefficient over **all fixed Gaussian proposal variances** is
\[
\boxed{s_*=3.77107268073615\ldots,\qquad 7s_*^3-41s_*^2+67s_*-45=0,}
\]
with \(s_*>3/2\) and \(C(s_*)=6.56138232719992\ldots\). By contrast, the unstratified independent importance-sampling estimator for the same quadratic observable has its unique minimum single-draw variance at proposal variance \(s=3\). Hence the Gaussian variance minimizing ordinary importance sampling differs strictly from the Gaussian variance minimizing the leading stratified error; at the latter optimum the leading stratified coefficient is approximately \(9.563\%\) below that at \(s=3\).

## Assumptions and scope

The target density is \(\phi(x)=(2\pi)^{-1/2}e^{-x^2/2}\). The proposal is the centered normal density \(q_s(x)=(2\pi s)^{-1/2}e^{-x^2/(2s)}\), with fixed variance \(s>0\) independent of \(N\). Every \(U_j\) is uniform in its own stratum, and all \(U_j\) are mutually independent. The estimator uses exactly \(N\) function evaluations; no sample-dependent normalization, adaptive scale choice, or correlated scrambling is included. All variances are unconditional over the independent random points. This is a benchmark for the second-moment observable, not a claim that randomization is necessary when that Gaussian moment is already analytically known. Rates are fixed-\(s\) asymptotics; nothing is claimed uniformly for \(s\) varying with \(N\).

## Proof

**1. Importance representation and unbiasedness.** Substitute \(x=\sqrt s\,z\) into the Gaussian importance identity. The target/proposal density ratio at \(x=\sqrt s\,z\) is \(\sqrt s\exp((1-s)z^2/2)\), and \(x^2=s z^2\), giving the transformed integrand
\[
f_s(u)=s^{3/2}[\Phi^{-1}(u)]^2\exp\!\left(\frac{1-s}{2}[\Phi^{-1}(u)]^2\right).
\]
The sum over all equally weighted strata integrates \(f_s\) exactly in expectation: \(\mathbb E Q_{N,s}=\int_0^1 f_s(u)\,du=1\). This identity requires only integrability, which holds for every \(s>0\).

**2. An exact cell-variance identity and its sharp limit.** Partition \((0,1)\) into \(I_{j,N}=((j-1)/N,j/N)\), and let \(P_Nf\) be the function equal to the mean of \(f\) on each cell. Independence gives the exact identity
\[
\operatorname{Var}\!\left(\frac1N\sum_j f(U_j)\right)=\frac1N\lVert f-P_Nf\rVert_{L^2(0,1)}^2.
\]
For every \(f\in H^1(0,1)\),
\[
\lim_{N\to\infty}N^2\lVert f-P_Nf\rVert_2^2=\frac1{12}\int_0^1|f'(u)|^2\,du.
\]
To prove the last statement first take \(f\in C^1([0,1])\): uniform first-order Taylor expansion on each interval reduces the within-cell squared error to \(\lvert f'(\xi_j)\rvert^2/(12N^3)+o(N^{-3})\); summation gives the Riemann integral. The cellwise Poincare inequality yields \(N^2\lVert f-P_Nf\rVert_2^2\le K\lVert f'\rVert_2^2\) for a universal \(K\), and the triangle inequality for \(N\lVert f-P_Nf\rVert_2\) extends convergence from smooth functions to \(H^1\) by density. Conversely, if \(f\) is differentiable with continuous derivative on each compact subinterval of \((0,1)\), nonnegative local cell variances and the same compact-interval Riemann argument give
\[
\liminf_{N\to\infty}N^3\operatorname{Var}(Q_N)\ge\frac1{12}\int_\delta^{1-\delta}|f'(u)|^2\,du
\]
for all \(0<\delta<1/2\). Thus divergence of \(\int_0^1|f'|^2\) forces \(N^3\operatorname{Var}(Q_N)\to\infty\) whenever the individual variances exist.

**3. The exact Gaussian threshold.** Write \(z=\Phi^{-1}(u)\). Differentiating yields
\[
f_s'(u)=\frac{s^{3/2}e^{(1-s)z^2/2}[2z-(s-1)z^3]}{\phi(z)}.
\]
Consequently,
\[
\int_0^1|f_s'(u)|^2\,du=s^3\sqrt{2\pi}\int_{\mathbb R}[2z-(s-1)z^3]^2e^{-(s-3/2)z^2}\,dz.
\]
This integral is finite exactly for \(s>3/2\). For those scales \(f_s\in H^1(0,1)\) (its square is integrable), so Step 2 applies. The standard even Gaussian integrals
\[
\int_{\mathbb R}z^{2k}e^{-az^2}\,dz=\frac{(2k-1)!!\sqrt\pi}{2^k a^{k+1/2}},\qquad a>0,
\]
with \(k=1,2,3\), give
\[
\int_0^1|f_s'|^2\,du=\frac{\pi s^3(7s^2-18s+15)}{4\sqrt2\,(s-3/2)^{7/2}}.
\]
Dividing by twelve proves the finite coefficient \(C(s)\). For \(1/2<s\le3/2\), \(f_s\in L^2\) but \(f_s'\notin L^2\), hence the compact lower bound in Step 2 proves normalized-variance divergence. For \(0<s\le1/2\), a direct substitution shows
\[
\int_0^1 f_s(u)^2\,du=\frac{s^3}{\sqrt{2\pi}}\int_{\mathbb R}z^4e^{-(s-1/2)z^2}\,dz=+\infty.
\]
Every \(N\)-stratification includes the two endpoint cells, so at least one cell retains infinite second moment and the estimator has infinite variance for each \(N\).

**4. Unique asymptotic optimum.** For \(s>3/2\), the positive function \(C(s)\) tends to infinity both as \(s\downarrow3/2\) and as \(s\to\infty\). Its logarithmic derivative is
\[
\frac{C'(s)}{C(s)}=\frac{3(7s^3-41s^2+67s-45)}{s(2s-3)(7s^2-18s+15)}.
\]
The quadratic denominator factor is strictly positive for all real \(s\), since its discriminant is negative. With \(t=s-3/2>0\), the cubic numerator becomes
\[
7t^3-\frac{19}{2}t^2-\frac{35}{4}t-\frac{105}{8}.
\]
By Descartes' rule of signs it has exactly one positive root; by its endpoint signs that root is attained. Therefore \(C\) has exactly one global minimizer in the finite regime, and none of the excluded scales has a finite \(N^3\)-normalized limit. Numeric root evaluation only supplies displayed decimals, not uniqueness.

**5. Ordinary importance-sampling comparison.** One unstratified draw \(X\sim N(0,s)\) contributes \(X^2\phi(X)/q_s(X)\) with mean one and second moment, when \(s>1/2\),
\[
M_2(s)=\frac{3s^3}{(2s-1)^{5/2}}.
\]
Its variance is \(M_2(s)-1\), with logarithmic derivative \((s-3)/(s(2s-1))\); hence it has the unique optimum \(s=3\). At scales \(s\le1/2\), its second moment is infinite. Comparing the exact constants completes the strict separation of the two proposal optima.

## Verification

The standalone `check.py` uses independent symbolic simplification, direct Gaussian quadrature in \(z\)-space, conditional-variance quadrature in probability strata, and the closed-form ordinary importance-sampling moments. The executable was run successfully, and `check_output.txt` contains its observed output. In particular, the three estimators at \(N=32,128,512\) for \(s=3\) and for the optimized scale approach the distinct predicted \(N^3\)-variance constants. Near the threshold \(s=3/2\), convergence is exceptionally slow; those computations are used only as consistency checks. The exact all-\(N\) infinite-variance statements and the asymptotic boundary are proved analytically, not inferred from experiments.

## Relationship to prior work

He, Zheng and Wang (arXiv:2203.03220, first posted March 7, 2022) examine Gaussian importance proposals in randomized quasi-Monte Carlo and establish broad boundary-growth convergence guarantees, including the importance of proposal covariance. Their Theorem 3.5 and Corollary 3.6 do not specify independent one-point-per-stratum asymptotic coefficients or the Gaussian proposal scale optimal for this quadratic observable. The classical independently stratified \(N^{-3}\) variance principle for square-integrable derivatives is **background**, not claimed as original. Chopin and Gerber (arXiv:2210.01554, first posted October 4, 2022) discuss classical Haber stratification and higher-order randomized quadratures, including importance examples; their estimator constructions and general smooth-function rate bounds do not give this quadratic Gaussian proposal-variance minimization and exact Sobolev threshold. He, Wang and Wang (arXiv:2403.11374, first posted March 17, 2024) study importance proposals with randomly shifted lattice rules for Bayesian inverse problems, not this independent-stratum quadratic Gaussian model. The specific contribution here is the exact all-scale classification and the uniquely optimized Gaussian importance scale, in sharp contrast to ordinary importance sampling.

## Limitations

The result applies only to the fixed, centered Gaussian proposal family, the standard-normal quadratic observable, and independent one-point-per-equal-probability-stratum sampling. It does not optimize all importance densities, adaptive or \(N\)-dependent Gaussian scales, stratification boundaries, correlated randomizations, general function classes, or multidimensional integration. Analytic knowledge of the target moment makes this a benchmark for method choice rather than a practical computation of an unknown constant. The explicit asymptotic constants are not finite-\(N\) optimality guarantees. Publication precedence in specialized literature remains a risk; no independent audit or external certification was performed.

## References

- Z. He, Z. Zheng and X. Wang, *On the Error Rate of Importance Sampling with Randomized Quasi-Monte Carlo*, arXiv:2203.03220 (2022), https://arxiv.org/abs/2203.03220; SIAM J. Numer. Anal. 61 (2023), 515–538.
- N. Chopin and M. Gerber, *Higher-order Monte Carlo through cubic stratification*, arXiv:2210.01554 (2022), https://arxiv.org/abs/2210.01554; SIAM J. Numer. Anal. 62 (2024), 229–247.
- Z. He, H. Wang and X. Wang, *Quasi-Monte Carlo and importance sampling methods for Bayesian inverse problems*, arXiv:2403.11374 (2024), https://arxiv.org/abs/2403.11374.
- P. Glasserman, P. Heidelberger and P. Shahabuddin, *Asymptotically optimal importance sampling and stratification for pricing path-dependent options*, Math. Finance 9 (1999), 117–152, https://doi.org/10.1111/1467-9965.00065 (contextual abstract only).

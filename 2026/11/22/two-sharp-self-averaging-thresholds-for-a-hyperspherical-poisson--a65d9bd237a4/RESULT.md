# Two sharp self-averaging thresholds for a hyperspherical Poisson-kernel uniformity statistic

## Finding

Fix \(0<\rho<1\) and \(\alpha>0\). For each ambient dimension \(d\ge2\), let \(n_d=\lceil e^{\alpha d}\rceil\), and independently sample \(X_1,\ldots,X_{n_d}\) uniformly from the sphere \(\mathbb S^{d-1}\subset\mathbb R^d\). Put \(m_d=\binom{n_d}{2}\) and define
\[
P_{d,\rho}(s)=\frac{1-\rho^2}{(1+\rho^2-2\rho s)^{d/2}},\qquad
A_d=\frac1{m_d}\sum_{1\le i<j\le n_d}P_{d,\rho}(\langle X_i,X_j\rangle).
\]
This is the uncentered pair average of the Poisson kernel appearing in the uniformity statistic of Fernández-de-Marcos and García-Portugués: their centered statistic is exactly \(T_{n_d,2}=(n_d-1)(A_d-1)\).

Define the distinct positive thresholds and the extreme-correlation boundary
\[
\alpha_{\mathrm P}=-\tfrac14\log(1-\rho^2),\qquad
\alpha_{\mathrm V}=-\tfrac12\log(1-\rho^2)=2\alpha_{\mathrm P},\qquad
t_\alpha=\sqrt{1-e^{-4\alpha}}.
\]
Then, for **every** fixed \(\rho\in(0,1)\) and \(\alpha>0\),
\[
\frac{\log A_d}{d}\xrightarrow{\mathsf P}
\begin{cases}
\frac12\log\!\left(\frac{1-t_\alpha^2}{1+\rho^2-2\rho t_\alpha}\right)<0,&0<\alpha<\alpha_{\mathrm P},\\[3pt]
0,&\alpha\ge\alpha_{\mathrm P}.
\end{cases}
\]
In particular, \(A_d\to0\) in probability below \(\alpha_{\mathrm P}\), but \(A_d\to1\) in probability above \(\alpha_{\mathrm P}\). At the equality point \(\alpha=\alpha_{\mathrm P}\), only the logarithmic-speed limit is asserted.

Furthermore the **exact finite-dimensional null variance** is
\[
\operatorname{Var}(A_d)=\binom{n_d}{2}^{-1}
\left[\frac{1+\rho^2}{(1-\rho^2)^{d-1}}-1\right],
\]
a known consequence of the Poisson-semigroup identity and existing spherical-kernel moment theory. Hence
\[
\operatorname{Var}(A_d)\sim 2(1-\rho^4)\exp\{2d(\alpha_{\mathrm V}-\alpha)\}.
\]
For \(\alpha_{\mathrm P}<\alpha<\alpha_{\mathrm V}\), the average converges to one in probability **despite its variance diverging exponentially**; at \(\alpha=\alpha_{\mathrm V}\), the variance converges to \(2(1-\rho^4)>0\); and for \(\alpha>\alpha_{\mathrm V}\), the convergence to one is in mean square. In the lower regime, \(\mathbb E A_d=1\) exactly even though \(A_d\to0\) in probability.

## Assumptions and scope

The ambient dimension tends through positive integers \(d\to\infty\). The concentration parameter \(\rho\) and exponential sample-rate \(\alpha\) stay fixed, and the sampling distribution is the **fully specified uniform null** on each sphere. The normalized uniform surface measure is used in defining the Poisson kernel and its expectations. Only unordered *distinct* pairs are included; diagonal terms would change the limit. There are no assumptions about independence of all pairwise inner products: the proof uses only their pairwise independence, which holds under the stated null.

## Proof

**1. Angular large deviations and pairwise independence.** If \(S_d=\langle X_1,X_2\rangle\), then \(S_d\) has density
\[
p_d(s)=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}(1-s^2)^{(d-3)/2},\quad -1<s<1.
\]
On every fixed subinterval of \((-1,1)\), its exponential rate is \(-I(s)\), where \(I(s)=-\tfrac12\log(1-s^2)\). In particular, for intervals whose closure lies in \((-1,1)\), \(\lim_{d\to\infty}d^{-1}\log\Pr(S_d\in B)=-\inf_{s\in B} I(s)\). The same rate estimates yield exponentially small probabilities outside any sufficiently wide compact subinterval.

For two distinct unordered pairs of sample labels, their inner products are independent. Disjoint pairs are independent by sampling. If the pairs share one sample point, condition on that point: both remaining points are independent uniform directions, and each conditional inner-product law equals the unconditional law, irrespective of the conditioned point. Thus for any interval \(B\), the count \(N_d(B)=\sum_{i<j}\mathbf1\{\langle X_i,X_j\rangle\in B\}\) obeys
\[
\mathbb EN_d(B)=m_dp_d(B),\quad \operatorname{Var}N_d(B)=m_dp_d(B)(1-p_d(B)).
\]
Consequently, if \(\inf_B I<2\alpha\), then \(N_d(B)/(m_dp_d(B))\to1\) in probability. If \(\inf_B I>2\alpha\), then \(\Pr\{N_d(B)>0\}\to0\). These conclusions require no joint independence of triangles.

**2. Exponential rate of the pair average.** Write \(f_\rho(s)=-\tfrac12\log(1+\rho^2-2\rho s)\); then \(P_{d,\rho}(s)=(1-\rho^2)e^{df_\rho(s)}\). Set
\[
F_\alpha=\sup_{I(s)\le2\alpha}\{f_\rho(s)-I(s)\}.
\]
For the lower bound, take an interior point \(s\) with \(I(s)<2\alpha\) and a sufficiently small interval \(B\) containing \(s\). The preceding pair-count variance estimate shows that with probability tending to one, the contribution of pairs inside \(B\) to \(A_d\) has exponential rate at least \(\inf_B f_\rho-\inf_B I\), up to an arbitrarily small error. Shrinking \(B\) and approaching the admissible boundary establishes \(\liminf d^{-1}\log A_d\ge F_\alpha\) in probability.

For the upper bound, choose \(b<1\) sufficiently close to one that \(I(b)>2\alpha\). With probability tending to one, no pair has \(|\langle X_i,X_j\rangle|>b\), by the union bound and angular large deviations. Partition \([-b,b]\) into finitely many intervals \(B\) of mesh \(\delta\). For each, the exponential Markov bound gives \(N_d(B)/m_d\le\exp[-d\inf_B I+2\varepsilon d]\) with probability tending to one; intervals with \(\inf_B I>2\alpha+\varepsilon\) are empty with probability tending to one. On each remaining interval, the normalized weighted contribution is at most \((1-\rho^2)\exp[d(\sup_B f_\rho-\inf_B I+2\varepsilon)]\). Taking the maximum over finitely many intervals, then letting \(\delta,\varepsilon\downarrow0\), proves \(\limsup d^{-1}\log A_d\le F_\alpha\) in probability. Thus \(d^{-1}\log A_d\to F_\alpha\) in probability.

The variational problem has an explicit solution. The identity
\[
(1+\rho^2-2\rho s)-(1-s^2)=(s-\rho)^2
\]
shows that \(G_\rho(s)=f_\rho(s)-I(s)\le0\), with equality only at \(s=\rho\). Its derivative is
\[
G_\rho'(s)=\frac{(\rho-s)(1-\rho s)}{(1-s^2)(1+\rho^2-2\rho s)},
\]
which is strictly positive to the left of \(\rho\) and strictly negative to its right. The constraint \(I(s)\le2\alpha\) is \(|s|\le t_\alpha\). Therefore \(F_\alpha=G_\rho(t_\alpha)<0\) when \(t_\alpha<\rho\), and \(F_\alpha=0\) otherwise. The equality \(t_\alpha=\rho\) is equivalent to \(\alpha=\alpha_{\mathrm P}\). This proves the log-scale assertion and \(A_d\to0\) in the lower regime.

**3. Probability convergence above the first threshold.** For every dimension and fixed unit direction, the normalized Poisson kernel integrates to one over the sphere; hence \(\mathbb EA_d=1\). Tilt the law of \(S_d\) by the factor \(P_{d,\rho}(S_d)\). Its exponential density is governed by \(G_\rho(s)\), uniquely maximized at \(s=\rho\). By Laplace concentration, its mass on \((b,1)\) tends to zero for each fixed \(b>\rho\).

Given \(\alpha>\alpha_{\mathrm P}\), select \(b>\rho\) sufficiently near \(\rho\) such that
\[
J_\rho(b):=\sup_{-1<s\le b}\{2f_\rho(s)-I(s)\}<2\alpha.
\]
This is possible because the supremum at \(b=\rho\) equals \(I(\rho)=2\alpha_{\mathrm P}\); indeed \(2f_\rho-I\) increases on \((-1,\rho]\). Let \(Y_{ij}=P_{d,\rho}(S_{ij})\mathbf1\{S_{ij}\le b\}\), and let \(\bar Y_d=m_d^{-1}\sum_{i<j}Y_{ij}\). The tilting concentration gives \(\mathbb E\bar Y_d\to1\). Pairwise independence gives
\[
\operatorname{Var}(\bar Y_d)\le m_d^{-1}\mathbb E[Y_{12}^2]
=\exp\{d[J_\rho(b)-2\alpha+o(1)]\}\to0.
\]
Thus \(\bar Y_d\to1\) in \(L^2\). The remainder \(A_d-\bar Y_d\ge0\) has expectation \(1-\mathbb E\bar Y_d\to0\), so Markov's inequality gives \(A_d-\bar Y_d\to0\) in probability. It follows that \(A_d\to1\) in probability for every \(\alpha>\alpha_{\mathrm P}\).

**4. The second threshold and non-uniform integrability.** Poisson-kernel convolution on normalized spherical surface measure gives
\[
\mathbb E[P_{d,\rho}(S_d)^2]=P_{d,\rho^2}(1)=\frac{1+\rho^2}{(1-\rho^2)^{d-1}}.
\]
The preceding pairwise independence therefore yields the displayed exact variance of \(A_d\). Since \(m_d\sim\frac12e^{2\alpha d}\), direct substitution proves its exponential equivalent and the three \(L^2\) regimes. Finally, \(T_{n_d,2}=(n_d-1)(A_d-1)\), so \(T_{n_d,2}/(n_d-1)\to-1\) below the first threshold and \(0\) above it.

## Verification

The supplied standalone Python checker evaluates the first and second Poisson-kernel moments using normalized Gauss–Jacobi quadrature for multiple dimensions and kernel parameters; checks the exact quadratic identity, critical-rate identities and the derivative sign formula; and checks the strict second-moment truncation inequality at multiple supercritical rates. It reports 2,566 passed assertions. All infinite-dimensional convergence statements follow from the proof, **not** from numerical calculations. The checker requires Python, NumPy and SciPy and can be run as `python checker.py`.

For \(\rho=1/2\), the thresholds are \(\alpha_{\mathrm P}=0.07192051811294523\ldots\) and \(\alpha_{\mathrm V}=0.14384103622589045\ldots\). At \(\alpha=0.05\), the logarithmic limit is \(-0.003354895695560328\ldots\).

## Relationship to prior work

Fernández-de-Marcos and García-Portugués introduced this centered hyperspherical Poisson-kernel uniformity statistic and analyzed its exact null moments and classical fixed-dimensional large-sample distribution. Ding, Markatou and Saraceno independently studied the same spherical Poisson kernel, its convolution and quadratic-distance statistics, with exact moment and spectral identities. **Neither the kernel nor its finite-dimensional variance is claimed as new here.** Cai, Fan and Jiang established empirical and extreme-angle laws for exponentially many random spherical points; their extreme-angle law supplies an important geometric predecessor but does not itself give the exponentially weighted pair-average law or the separation of probability and mean-square thresholds. The new result combines the Poisson-kernel tilt with pair-count concentration and gives two explicit thresholds for this specific published statistic.

## Limitations

The theorem concerns the simple uniform null, the off-diagonal pair average, fixed \(\rho\in(0,1)\), and sample size growing as \(\lceil e^{\alpha d}\rceil\). It does not identify the limiting distribution or probability limit of \(A_d\) at the first critical boundary \(\alpha=\alpha_{\mathrm P}\); only the logarithmic rate there is established. At the second boundary, the theorem identifies the limiting **variance** but does not assert a nondegenerate distributional limit. No conclusions are drawn for data-dependent \(\rho\), nonuniform alternatives, a fixed or subexponential sample size, or diagonal-inclusive V-statistics. The classical general large-deviation and random-energy techniques are closely related; historical novelty is assessed specifically for the two-threshold Poisson-kernel statistical statement.

## References

1. A. Fernández-de-Marcos and E. García-Portugués, *On new omnibus tests of uniformity on the hypersphere*, arXiv:2304.04519, first submitted 2023-04-10; 2023 journal version in *TEST* 32, 1508–1529. https://arxiv.org/abs/2304.04519
2. Y. Ding, M. Markatou and G. Saraceno, *Poisson Kernel-Based Tests for Uniformity on the d-Dimensional Sphere*, *Statistica Sinica* 35 (2025), 1947–1969, preprint SS-2022-0347. https://doi.org/10.5705/ss.202022.0347
3. T. T. Cai, J. Fan and T. Jiang, *Distributions of Angles in Random Packing on Spheres*, *Journal of Machine Learning Research* 14 (2013), 1837–1864. https://arxiv.org/abs/1306.0256

# Universal subprobability weights for exponential-kernel quadrature and a sharp smoothness obstruction

## Finding

Let \(\lambda>0\), let \(x_1<\cdots<x_n\) be any \(n\ge1\) distinct real sites, and let \(\nu\) be **any finite nonnegative Borel measure on \(\mathbb R\)**. Define
\[
K_{ij}=e^{-\lambda|x_i-x_j|},\quad b_i=\int_{\mathbb R}e^{-\lambda|x_i-y|}\,\nu(dy),\quad D=\operatorname{diag}(d_1,\ldots,d_n),\qquad d_i\ge0.
\]
Then the unconstrained (possibly heteroscedastically regularized) kernel quadrature weights \(w=(K+D)^{-1}b\) satisfy the **subprobability property**
\[
\boxed{\qquad w_i\ge0\quad(1\le i\le n),\qquad \sum_{i=1}^n w_i\le\nu(\mathbb R).\qquad}
\]
If \(\nu\) gives positive mass to every nonempty open interval, every weight is strictly positive, even when some \(d_i=0\). Alternatively, if \(\nu\ne0\) and every \(d_i>0\), every weight is strictly positive. The total-mass bound is best possible: with zero nuggets and \(\nu=\delta_{x_j}\), its left side is exactly one.

This phenomenon is sharp within the commonly used power-exponential family \(k_{\alpha,\lambda}(x,y)=e^{-\lambda|x-y|^\alpha}\) for \(1\le\alpha\le2\). **The universal assertion across all sites, nonnegative target measures and finite nonnegative diagonal nuggets holds if and only if \(\alpha=1\)**. For every \(\alpha>1\), two sites and one target atom beyond the sites give a strictly negative first quadrature weight, regardless of the preassigned finite nuggets.

## Assumptions and scope

All matrices and integrals are in exact real arithmetic. The covariance amplitude is normalized to one; a positive common amplitude can be divided out together with the nugget units. The target measure may have atoms, may be supported outside the nodes and need not have a density. The diagonal nugget entries are arbitrary prescribed finite real numbers \(d_i\ge0\); no off-diagonal observation noise is covered. Distinct sites and \(\lambda>0\) guarantee strict positive definiteness of \(K\). The computed weights are the standard unconstrained Gaussian-process kernel-mean weights and are not artificially clipped. The comparison to power-exponential kernels asserts universal positivity only in the restricted \(1\le\alpha\le2\) range, not a classification for \(0<\alpha<1\).

## Proof

**1. Nonnegative cardinal basis with a strict subpartition of unity.** Put \(k_y=(e^{-\lambda|x_i-y|})_{i=1}^n\), and \(L(y)=K^{-1}k_y\). If \(y\le x_1\), the identity \(k_y=e^{-\lambda(x_1-y)}Ke_1\) gives \(L_1(y)=e^{-\lambda(x_1-y)}\) and all other cardinal functions zero. A symmetric statement holds when \(y\ge x_n\). For \(y\in[x_i,x_{i+1}]\), set \(\Delta_i=x_{i+1}-x_i\). Multiplicativity of the exponential along ordered points yields
\[
L_j(y)=0\ (j\notin\{i,i+1\}),\quad
L_i(y)=\frac{\sinh(\lambda(x_{i+1}-y))}{\sinh(\lambda\Delta_i)},\quad
L_{i+1}(y)=\frac{\sinh(\lambda(y-x_i))}{\sinh(\lambda\Delta_i)}.
\]
Indeed these two coefficients reproduce \(k(x_j,y)\) for both neighboring nodes and hence every farther node, so multiplication by \(K\) verifies the identity. The functions are nonnegative and, within that gap, satisfy
\[
\sum_jL_j(y)=\frac{\cosh(\lambda(y-(x_i+x_{i+1})/2))}{\cosh(\lambda\Delta_i/2)}\le1.
\]
Outside the nodes, the sum is a single exponential \(\le1\); at a node it equals one. For \(n=1\), the single formula \(L_1(y)=e^{-\lambda|x_1-y|}\) suffices. Consequently the noiseless quadrature vector
\[
v=K^{-1}b=\int_{\mathbb R}L(y)\,\nu(dy)
\]
is componentwise nonnegative and has \(\mathbf1^Tv\le\nu(\mathbb R)\). Positive mass on every open interval implies \(v_i>0\) for every \(i\), since each \(L_i\) is positive in a neighborhood of \(x_i\).

**2. Strictly positive row sums of the Markov precision.** For \(n\ge2\), write \(\rho_i=e^{-\lambda(x_{i+1}-x_i)}\in(0,1)\) and \(Q=K^{-1}\). The exact Gaussian Markov factorization is
\[
z^{\mathsf T}Qz=z_1^2+\sum_{i=1}^{n-1}\frac{(z_{i+1}-\rho_i z_i)^2}{1-\rho_i^2},\qquad z\in\mathbb R^n.
\]
It proves positive definiteness and tridiagonality, with strictly negative nearest-neighbor entries \(Q_{i,i+1}=-\rho_i/(1-\rho_i^2)\), all other off-diagonals zero. Direct row summation gives
\[
(Q\mathbf1)_1=\frac1{1+\rho_1},\quad
(Q\mathbf1)_n=\frac1{1+\rho_{n-1}},\quad
(Q\mathbf1)_i=\frac{1-\rho_{i-1}\rho_i}{(1+\rho_{i-1})(1+\rho_i)}>0\quad(1<i<n).
\]
The case \(n=1\) has \(Q=[1]\), again with positive row sum.

**3. Heteroscedastic nuggets preserve positivity and do not increase total weight.** Since \((K+D)w=b\), multiplication by \(Q\) gives
\[
(I+QD)w=v.
\]
For a strictly positive diagonal \(D\), the matrix \(I+QD\) is diagonally similar to \(S=I+D^{1/2}QD^{1/2}\), which is symmetric positive definite with nonpositive off-diagonal entries. Its inverse is entrywise nonnegative: if \(Sz=f\ge0\), write \(z=z_+-z_-\) with disjoint nonnegative supports. If \(z_-\ne0\), then \(z_-^{\mathsf T}f=z_-^{\mathsf T}Sz_+-z_-^{\mathsf T}Sz_-<0\), a contradiction, because the first term is nonpositive while the second is strictly positive. Thus \(S^{-1}\ge0\), and diagonal similarity yields \((I+QD)^{-1}\ge0\). When some \(d_i=0\), replace \(D\) by \(D+\varepsilon I\) and let \(\varepsilon\downarrow0\); invertibility persists since \(K+D\) is positive definite. Hence \(w=(I+QD)^{-1}v\ge0\) for every permitted diagonal. The inverse has positive diagonal entries; consequently \(v_i>0\) gives \(w_i>0\). If instead all \(d_i>0\) and \(\nu\ne0\), then \(v\ne0\) and irreducibility of the tridiagonal Stieltjes matrix \(S\) makes \(S^{-1}\) strictly positive (for example via a positive Neumann series for a suitable scalar shift), giving \(w>0\).

Finally, \(v-w=QDw\), and symmetry of \(Q\) implies
\[
\mathbf1^{\mathsf T}v-\mathbf1^{\mathsf T}w=(Q\mathbf1)^{\mathsf T}Dw\ge0.
\]
Together with Step 1 this proves the claimed total-mass bound.

**4. Sharp failure for every smoother power-exponential kernel.** Fix any \(1<\alpha\le2\), \(\lambda>0\), sites \(0,a\) with \(a>0\), nonnegative finite nuggets \(d_1,d_2\), and target \(\nu=\delta_{a+b}\) with \(b>0\). The positive determinant of the two-site nugget matrix is \((1+d_1)(1+d_2)-e^{-2\lambda a^\alpha}>0\). Its first weight has numerator
\[
(1+d_2)e^{-\lambda(a+b)^\alpha}-e^{-\lambda a^\alpha}e^{-\lambda b^\alpha}.
\]
After multiplication by \(e^{\lambda(a+b)^\alpha}\), this has the sign of
\[
(1+d_2)-\exp\{\lambda[(a+b)^\alpha-a^\alpha-b^\alpha]\}.
\]
For any fixed \(a>0\) and \(\alpha>1\), the exponent tends to \(+\infty\) as \(b\to\infty\), so the first weight becomes strictly negative for sufficiently large \(b\). It stays negative for a target with a sufficiently concentrated smooth positive bump near \(a+b\), by continuity of the kernel mean; a sufficiently small full-support positive background can be added if desired. At \(\alpha=1\) Steps 1–3 already prove positivity for every allowed instance. Thus the stated interval classification is exact.

## Verification

The standalone file `verify_ou_weight_positivity.py` constructs rational-correlation exponential Gram matrices for all sizes \(1\le n\le8\), forms explicit on-site, interior and exterior kernel-mean atoms, and solves the regularized linear systems with **exact rational arithmetic** under multiple heterogeneous diagonal-nugget patterns. It checks nonnegativity, the total-mass bound, the Stieltjes structure and positive row sums; it also checks mixtures of target atoms. Command: `python verify_ou_weight_positivity.py`, requiring SymPy. Its recorded output reports **1,299 checks**, including the exact negative Gaussian-kernel comparison (two sites at 0,1, target at 5, \(d_2=1\)). Finite tests verify algebra and examples, not the infinite theorem; Steps 1–4 provide that proof.

## Relationship to prior work

Huszár and Duvenaud (2012) explain the unconstrained optimally weighted Bayesian quadrature framework; they do not state the exponential-kernel sign-and-mass theorem. Karvonen, Kanagawa and Särkkä (2018/2019) develop positivity results for smooth totally positive kernels under special design conditions, and note explicitly that their argument does **not** establish positivity for Matérn kernels, including the exponential covariance \(\nu_{\rm Mat\acute ern}=1/2\). The proof here uses the Markov precision and a sparse, nonnegative interpolation basis instead. Published analysis of optimal Ornstein–Uhlenbeck integral designs uses the same classical Markov covariance decomposition but does not determine the all-site nugget-robust sign-and-mass property; published exponential-kernel inverse-matrix collision laws concern conditioning rather than quadrature signs. A separate two-node power-exponential random-quadrature study analyzes noise tails and a different \(\alpha=3/2\) moment boundary, not the universal \(\alpha=1\) sign boundary here. The Markov tridiagonal inverse, positivity of Stieltjes inverses and two-node matrix inversion are classical ingredients and are not individually claimed as discoveries.

## Limitations

The result is one-dimensional and uses the stationary exponential covariance kernel with precisely diagonal, nonnegative observation noise. It does not establish analogous positivity for higher-dimensional Matérn kernels, off-diagonal noise covariance, arbitrary continuous kernels or likelihood models other than kernel-mean linear weights. A subprobability rule is not generally exactly normalized for constant functions; its sum can be strictly below one. Nor does positivity alone imply a favorable integration error or conditioning. The archival source fixes the topic's first-public chronology; subsequent literature comparisons do not change that date. Publication priority is assessed on inspected sources rather than certified exhaustively: classical generalized spline or Gaussian-Markov interpolation results may contain equivalent formulations not indexed under quadrature terminology. No independent scientific validation has been performed.

## References

1. F. Huszár and D. Duvenaud, *Optimally-Weighted Herding is Bayesian Quadrature*, arXiv:1204.1664v1, first submitted 2012-04-07, https://arxiv.org/abs/1204.1664.
2. T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, arXiv:1812.08509v1, 2018-12-20; *Statistics and Computing* 29 (2019), https://arxiv.org/abs/1812.08509; https://doi.org/10.1007/s11222-019-09901-0.
3. *Exact optimal nodes and stratification penalty for Ornstein–Uhlenbeck Bayesian quadrature* (2026), published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-optimal-nodes-and-stratification-penalty-for-ornstein-uhle--971795799fba.
4. *Universal collision-tail and nugget moment laws for random exponential-kernel matrices* (2026), published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-universal-collision-tail-and-nugget-moment-laws-for-random-expon--2bac4e280898.
5. *A roughness threshold and exact noise tails for colliding-node kernel quadrature* (2026), published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-roughness-threshold-and-exact-noise-tails-for-colliding-node-k--841cfe0433d1.

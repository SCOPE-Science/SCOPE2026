# Spectral minimax calibration and unavoidable fourth-order dependence in random-order Langevin splitting

## Finding

Let \(A\in\mathbb R^{d\times d}\) be symmetric positive definite, let \(h>0\), and let the target be the Gaussian equilibrium \(\mathcal N(0,A^{-1})\) of \(dX=-AX\,dt+\sqrt2\,dW\). Independently at each numerical step, use exact drift for time \(h\) followed by exact free diffusion with probability \(p\in[0,1]\), or use the reverse order otherwise. The resulting Markov chain has a unique stationary law \(\pi_{h,p}\).

Write the eigenvalues of \(A\) as \(\lambda_i>0\), and define
\[
 f(t)=\frac1{2t}-\frac1{e^{2t}-1},\qquad t>0.
\]
If \(X\sim\pi_{h,p}\), its covariance eigenvalue in mode \(i\) is exactly
\[
 \mathbb E[X_i^2]=\frac1{\lambda_i}+2h\bigl(p-f(h\lambda_i)\bigr).
\]
The function \(f\) is strictly decreasing from \(1/2\) to \(0\). Hence the **unique** choice of \(p\) minimizing the operator-norm covariance error is
\[
 p_*=\tfrac12\bigl(f(h\lambda_{\min})+f(h\lambda_{\max})\bigr),
 \qquad
 \min_{p\in[0,1]}\|\operatorname{Cov}_{\pi_{h,p}}(X)-A^{-1}\|_2
 =h\bigl(f(h\lambda_{\min})-f(h\lambda_{\max})\bigr).
\]
Exact covariance calibration by a single ordering probability is possible if and only if \(A\) is a scalar multiple of the identity. Even in that isotropic case, exact invariant-*law* calibration is **impossible** for every \(h>0\): at the covariance-calibrating probability the stationary law is not Gaussian.

More precisely, let \(r_i=e^{-h\lambda_i}\). For \(0<p<1\), each marginal has strictly positive fourth cumulant
\[
 \operatorname{cum}_4(X_i)
 =\frac{12h^2p(1-p)(1-r_i^2)^2}{1-r_i^4}
 =12h^2p(1-p)\tanh(h\lambda_i)>0.
\]
For two distinct orthonormal eigenmodes, even though \(\mathbb E[X_iX_j]=0\), their squares are positively correlated:
\[
 \operatorname{Cov}(X_i^2,X_j^2)
 =\frac{4h^2p(1-p)(1-r_i^2)(1-r_j^2)}{1-r_i^2r_j^2}>0.
\]
At \(p=0\) or \(p=1\), the stationary distribution is Gaussian but has incorrect covariance. Therefore **no** probability \(p\in[0,1]\) makes this random-order splitting sampler exactly preserve \(\mathcal N(0,A^{-1})\) at a finite positive stepsize.

## Assumptions and scope

The exact drift substep maps \(x\mapsto T x\) with \(T=e^{-hA}\), and the exact free-diffusion substep maps \(x\mapsto x+\sqrt{2h}\,Z\), with \(Z\sim\mathcal N(0,I_d)\). At each step an independent Bernoulli variable \(B\) equals one with probability \(p\), indicating *drift followed by diffusion*; fresh standard Gaussian \(Z\) is independent of \(B\), the past and all other steps. The complete update is
\[
 X_{n+1}=T X_n+\sqrt{2h}\,[B_nI+(1-B_n)T]Z_n.
\]
Every claim is for finite \(d\ge1\), arbitrary SPD \(A\), \(h>0\), and \(p\in[0,1]\). Covariance minimaxity refers solely to the spectral/operator norm of stationary covariance error, not Wasserstein distance, total variation, asymptotic variance of sample averages, or mixing speed. The random ordering variable is shared across all coordinates of each step; Gaussian noises are independent across coordinates and steps. The fluctuation temperature is normalized to one.

## Proof

**1. Existence and Gaussian-mixture representation.** Since the spectral norm \(\|T\|_2=e^{-h\lambda_{\min}}<1\) and innovations have bounded second moments, the stationary series
\[
 X\;\overset{d}=\;\sqrt{2h}\sum_{k=0}^\infty T^k[B_kI+(1-B_k)T]Z_k
\]
converges in \(L^2\). Coupling two initial states with the same innovations makes their difference \(T^n(x-y)\), proving convergence to and uniqueness of the invariant law. Diagonalize \(A\) orthogonally; then, conditional on the entire Bernoulli sequence, the coordinates \(X_i\) are independent centered Gaussians with conditional variances
\[
 V_i=\frac{2hr_i^2}{1-r_i^2}
    +2h(1-r_i^2)\sum_{k=0}^\infty r_i^{2k}B_k.
\]
These series converge even at the endpoint probabilities.

**2. Covariance and its exact minimax calibration.** Taking expectations and summing geometric series yields
\[
 m_i:=\mathbb EV_i=2h\left(p+\frac{r_i^2}{1-r_i^2}\right).
\]
As \(r_i^2/(1-r_i^2)=1/(e^{2h\lambda_i}-1)\), subtracting \(1/\lambda_i\) yields \(m_i-1/\lambda_i=2h(p-f(h\lambda_i))\). The derivative
\[
 f'(t)=\frac1{2\sinh^2t}-\frac1{2t^2}<0
\]
uses \(\sinh t>t\) for \(t>0\). The identities \(f(t)>0\) and \(f(t)<1/2\) follow respectively from \(e^{2t}-1>2t\) and \(t\coth t>1\); limits at zero and infinity are \(1/2\) and zero. The mode-wise errors are \(2h(p-f(h\lambda_i))\), so their largest absolute value is governed by the two endpoints of the range of \(f\). The unique minimax choice is their midpoint, giving the displayed exact value. All mode errors vanish precisely when all eigenvalues of \(A\) coincide.

**3. Fourth-order obstruction and cross-mode dependence.** Independence of the \(B_k\) gives
\[
 \operatorname{Cov}(V_i,V_j)
 =4h^2p(1-p)(1-r_i^2)(1-r_j^2)
   \sum_{k=0}^\infty(r_i^2r_j^2)^k,
\]
which is the stated positive expression. For \(i=j\), conditional Gaussian fourth moments give \(\mathbb EX_i^4=3\mathbb EV_i^2\), so \(\operatorname{cum}_4(X_i)=3\operatorname{Var}(V_i)\). For \(i\ne j\), conditional independence gives \(\mathbb E[X_i^2X_j^2]=\mathbb E[V_iV_j]\). These establish the formulas, strictly positive for \(0<p<1\). At \(p=0,1\), every conditional covariance is deterministic and the resulting stationary distribution is Gaussian, but \(f(h\lambda_i)\in(0,1/2)\) makes its covariance error nonzero. The Gaussian target is therefore never exactly invariant.

**4. Leading-order consequences.** Taylor expansion at zero gives \(f(t)=1/2-t/6+O(t^3)\). Thus, for fixed SPD \(A\) and \(h\downarrow0\),
\[
 p_*=\frac12-\frac{\lambda_{\min}+\lambda_{\max}}{12}h+O(h^3),\quad
 \min_p\|\operatorname{Cov}_{\pi_{h,p}}(X)-A^{-1}\|_2
 =\frac{\lambda_{\max}-\lambda_{\min}}6h^2+O(h^4).
\]
For a single mode with \(p=f(h\lambda)\), the fourth cumulant is \(3\lambda h^3+O(h^4)\). This last assertion concerns the stationary marginal fourth cumulant, not the error in all observables.

## Verification

Run the included standard-library verifier with `python verify.py`. It checks the covariance and fourth-moment recursions against the closed forms over extensive exact rational parameter sets, checks cross-coordinate fourth moments independently through their stationarity recurrence, checks finite random-order prefixes by exhaustive Bernoulli enumeration with a rigorous geometric-series remainder identity, and compares the minimax formula with a discrete grid of ordering probabilities. Its recorded result is included as `checks.txt`. The real-parameter proof above is independent of enumeration.

For an illustrative \(h=1\), \(\lambda_{\min}=1/2\), \(\lambda_{\max}=2\), the exact minimax formula gives \(p_*\approx0.3246829664\) and covariance operator-norm error \(\approx0.1866806535\), compared with \(\approx0.5373147207\) for fair random ordering. This is a covariance calibration improvement, not evidence of a reduction in distributional or Monte Carlo estimator error.

## Relationship to prior work

Leimkuhler and Sachs (arXiv:2012.04245v1, 2020-12-08), especially sections 2 and 3.2.1, analyze symmetric splitting methods for generalized Langevin equations and obtain exact quadratic-target Gaussian marginal sampling for a different fixed symmetric scheme. The present result instead treats an *asymmetric* two-subflow random-order scheme and pinpoints the distinction between matching the Gaussian covariance and matching the law.

Cho, Berry and Hsieh (arXiv:2210.11281v1, 2022-10-20) establish randomized product-formula error control for quantum-unitary simulation, not a stationary Gaussian diffusion or minimax ordering-probability problem. Li, Wang and Wang (arXiv:2510.07676v1, 2025-10-09) directly analyze random-order Langevin splitting, using equal ordering probabilities and deriving distributional approximation and ergodicity bounds. Their algorithm section, principal statements and experiments do not state the all-spectrum covariance minimax formula, exact fourth-cumulant law, or cross-mode square dependence proved here. These comparisons do not certify publication priority: an unlocated specialist derivation of the harmonic random-splitting invariant law remains possible.

## Limitations

This is an exact benchmark for a linear Gaussian target with exact drift and diffusion subflows. It does not show that covariance-calibrating \(p_*\) optimizes Wasserstein error, overall bias, mixing, wall-clock cost or an estimator mean-squared error. It does not extend unchanged to nonlinear drift, non-isotropic diffusion, numerically approximated drift, correlated order choices or coordinate-specific order randomization. Positive fourth cumulant rules out exact Gaussian stationary law but alone does not quantify total variation distance. The existing literature comparisons are not independent expert validation.

## References

- B. Leimkuhler and M. Sachs, *Efficient Numerical Algorithms for the Generalized Langevin Equation*, arXiv:2012.04245v1 (first public 2020-12-08), https://arxiv.org/html/2012.04245v1 .
- C.-H. Cho, D. W. Berry, and M.-H. Hsieh, *Doubling the order of approximation via the randomized product formula*, arXiv:2210.11281v1 (first public 2022-10-20), https://arxiv.org/abs/2210.11281 .
- L. Li, C. Wang, and M. Wang, *Ergodicity and error estimate of laws for a random splitting Langevin Monte Carlo*, arXiv:2510.07676v1 (first public 2025-10-09), https://arxiv.org/abs/2510.07676 .

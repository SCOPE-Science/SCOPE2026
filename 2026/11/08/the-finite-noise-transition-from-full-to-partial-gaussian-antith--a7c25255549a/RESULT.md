# The finite-noise transition from full to partial Gaussian antithetics

## Finding

**Theorem (finite-noise Gaussian coupling and a sharp cross-validation phase boundary).** Fix an integer \(K\geq2\). Consider jointly Gaussian standard-normal replicas \(Z_1,\ldots,Z_K\) with an arbitrary positive-semidefinite correlation matrix \(R\) having unit diagonal. For real \(a\) and \(b\ne0\), let
\[
Q_K=\frac1K\sum_{j=1}^K\{aZ_j+b(Z_j^2-1)\}.
\]
Among **all** such Gaussian correlation matrices, the unique minimizer of \(\operatorname{Var}(Q_K)\) is the equicorrelation matrix with off-diagonal coefficient
\[
\rho_*=-\min\left\{\frac1{K-1},\frac{a^2}{4b^2}\right\}.
\]
Thus maximally antithetic (zero-sum) coupling is optimal precisely when \(a^2\geq 4b^2/(K-1)\); otherwise the unique optimum is strictly less anticorrelated. When \(a=0\), independence is uniquely optimal. The restriction \(b\ne0\) matters: if \(b=0\) and \(a\ne0\), the optimum is zero but every feasible \(R\) satisfying \(R\mathbf1=0\) minimizes variance, so uniqueness generally fails.

**Exact randomized-cross-validation consequence.** Let \(Y\sim N(\mu,\sigma^2)\), where \(\mu\in\mathbb R\) and \(\sigma>0\). For \(0<c<1\), \(\alpha>0\), and \(K\ge2\), take Gaussian randomizations \(\omega_j\sim N(0,\sigma^2)\) independent of \(Y\), with arbitrary jointly Gaussian correlation matrix \(R\). Use the linear predictor \(g(y)=cy\), randomized training/testing views \(Y_j^{\rm tr}=Y+\sqrt\alpha\,\omega_j\), \(Y_j^{\rm te}=Y-\omega_j/\sqrt\alpha\), and the bias-corrected score
\[
\widehat{\mathrm{CV}}_\alpha=\frac1K\sum_{j=1}^K\left\{\bigl(cY_j^{\rm tr}-Y_j^{\rm te}\bigr)^2-\frac{\omega_j^2}{\alpha}\right\}.
\]
Its finite-\(\alpha\) **expected conditional variance**, unconditional variance, and mean-squared error for prediction error are uniquely minimized by the equicorrelation matrix with
\[
\boxed{\quad \rho_*(\alpha)=-\min\left\{\frac1{K-1},\ S(\alpha)\right\},\qquad
S(\alpha)=\frac{(1-c)^2(\mu^2+\sigma^2)}{c^2\sigma^2}\,\frac{(1+c\alpha)^2}{\alpha(2+c\alpha)^2}.\quad}
\]
There is exactly one \(\alpha_{\rm crit}>0\) defined by \((K-1)S(\alpha_{\rm crit})=1\). Full antithetics uniquely minimize the criterion when \(0<\alpha\le\alpha_{\rm crit}\); for \(\alpha>\alpha_{\rm crit}\), the unique optimum satisfies \(-1/(K-1)<\rho_*(\alpha)<0\), tending to zero as \(\alpha\to\infty\). This does not contradict the previously proved small-\(\alpha\) necessity of maximal antithetics.

At \(K=2\), \(c=1/2\), \(\mu=0\), \(\sigma^2=1\), and \(\alpha=4\), the unique optimal correlation is \(-9/64\). The expected conditional variance is exactly \(5167/1024\) at this optimum, versus \(8\) for full antithetics and \(41/8\) for independent replicas. All three schemes have identical single-replica marginal laws and identical bias.

## Assumptions and scope

This is an exact-arithmetic, finite-replica variance optimization over the class of **jointly Gaussian** couplings with fixed standard-normal marginals. Singular Gaussian laws (including the zero-sum boundary) are included. The optimization permits nonsymmetric correlation matrices only in the usual symmetric positive-semidefinite sense; exchangeability is not assumed *a priori*. The cross-validation result uses one scalar normal observation with known variance, a fixed shrinkage \(0<c<1\), and the stated bias correction. A universal claim over non-Gaussian joint couplings, arbitrary predictors, higher-dimensional data, or approximate covariance construction is not made.

## Proof

**1. Exact second-chaos covariance.** Isserlis' Gaussian fourth-moment identity gives, for any jointly standard-normal pair with correlation \(r\),
\[
\operatorname{Cov}(Z_i,Z_j)=r,\quad
\operatorname{Cov}(Z_i^2-1,Z_j^2-1)=2r^2,\quad
\operatorname{Cov}(Z_i,Z_j^2-1)=0.
\]
Consequently,
\[
\operatorname{Var}(Q_K)=\frac{a^2}{K^2}\mathbf1^\top R\mathbf1
+\frac{2b^2}{K^2}\operatorname{tr}(R^2).
\tag{1}
\]
This identity holds even when \(R\) is singular.

**2. Symmetrization and uniqueness.** The feasible set of correlation matrices is compact and convex, and invariant under simultaneous permutation of rows and columns. Since \(b\ne0\), the right-hand side of (1) is strictly convex in \(R\): its quadratic part has positive coefficient and equals the squared Frobenius norm on symmetric matrices. Averaging \(R\) over every permutation yields an equicorrelation matrix and cannot increase the objective; strict convexity makes this symmetrized matrix the unique global minimizer whenever its scalar correlation is minimizing. Every equicorrelation matrix is feasible exactly for \(-1/(K-1)\le\rho\le1\).

**3. One-dimensional exact optimization.** Substitution into (1) yields
\[
V(\rho)=\frac{a^2}{K}\{1+(K-1)\rho\}
+\frac{2b^2}{K}\{1+(K-1)\rho^2\}.
\]
Its strictly positive second derivative is \(4b^2(K-1)/K\), and its unconstrained critical point is \(\rho=-a^2/(4b^2)\). Projection onto the feasible interval proves the displayed optimizer and uniqueness. At \(a=0\), this point is \(0\). If \(b=0\) and \(a\ne0\), equation (1) reduces to a nonnegative quadratic form with zero precisely when \(R\mathbf1=0\) (because \(R\) is positive semidefinite), as asserted.

**4. Exact cross-validation reduction.** Write \(A_Y=2(c-1)(c\sqrt\alpha+\alpha^{-1/2})Y\) and \(B=c^2\alpha+2c\). Direct expansion yields
\[
\widehat{\mathrm{CV}}_\alpha=(c-1)^2Y^2+\frac1K\sum_{j=1}^K\{A_Y\omega_j+B\omega_j^2\}.
\]
Therefore \(\mathbb E[\widehat{\mathrm{CV}}_\alpha\mid Y]=(c-1)^2Y^2+B\sigma^2\), independent of \(R\). On subtracting this conditional mean, apply equation (1) to \(\omega_j/\sigma\) with linear coefficient \(a=A_Y\sigma\) and quadratic coefficient \(b=B\sigma^2\), then average over \(Y\). This gives
\[
\mathbb E\left[\operatorname{Var}(\widehat{\mathrm{CV}}_\alpha\mid Y)\right]
=\frac{P}{K^2}\mathbf1^\top R\mathbf1+\frac{Q}{K^2}\operatorname{tr}(R^2),
\]
where
\[
P=4(1-c)^2(c\sqrt\alpha+\alpha^{-1/2})^2\sigma^2(\mu^2+\sigma^2),
\qquad Q=2(c^2\alpha+2c)^2\sigma^4>0.
\]
For equicorrelation \(\rho\), the expression is
\[
\frac{P}{K}\{1+(K-1)\rho\}+\frac{Q}{K}\{1+(K-1)\rho^2\}.
\tag{2}
\]
Its unique minimizer is \(\rho_*=-\min\{1/(K-1),P/(2Q)\}\), with \(P/(2Q)=S(\alpha)\) as stated. Strict convexity again proves global uniqueness over arbitrary feasible \(R\), not only exchangeable ones.

**5. Exact boundary and unchanged MSE bias.** The scalar function \(H(\alpha)=(1+c\alpha)^2/[\alpha(2+c\alpha)^2]\) is strictly decreasing, because
\[
H'(\alpha)=-\frac{(1+c\alpha)(c^2\alpha^2+c\alpha+2)}{\alpha^2(2+c\alpha)^3}<0.
\]
Its limits as \(\alpha\downarrow0\) and \(\alpha\to\infty\) are \(+\infty\) and \(0\); hence the unique threshold exists. The true prediction error of \(g(Y)=cY\), evaluated at an independent test copy, is \((c-1)^2\mu^2+(c^2+1)\sigma^2\). The bias of the score is exactly \(c^2\alpha\sigma^2\), independent of \(R\). By total variance, the only \(R\)-dependent term in its MSE is (2); in particular, the optimum is unchanged when variance is replaced by MSE. Direct rational substitution proves the numerical example.

## Verification

Run `python3 verify.py` using Python's standard library. This checker tests 136,111 exact-rational inequalities and identities, random nonexchangeable positive-semidefinite correlation matrices, and direct finite-sample simulations of the original train/test score at three correlations. The exact-rational parameter sweeps are finite diagnostics only: the proof above, using Gaussian moments, strict convexity, and monotonicity, establishes the universal statements.

## Relationship to prior work

Liu, Panigrahi, and Soloff (2024, arXiv:2412.14423) introduce zero-sum Gaussian-randomization cross-validation and show bounded variance as perturbation size tends to zero. Chattopadhyay, Liu, and Panigrahi (2026, arXiv:2608.08089) prove necessity of the zero-sum correlation for bounded reducible variance **as perturbation vanishes** and compare joint distributions within the zero-sum class. Neither of those results implies the exact optimizer over all Gaussian correlation matrices **at each fixed positive perturbation**: an asymptotic requirement cannot distinguish full versus partial antithetics at finite noise. Their formulas and assumptions were compared through full accessible source text, including theorem statements, discussion, and relevant proof sections. Abkin and Daripa (2026, arXiv:2610.01120) establish variance-optimal signed pairwise couplings in numerical random-walk solvers; their indicator-based particle model is neither this Gaussian quadratic-coupling problem nor the finite-perturbation cross-validation score. Standard Gaussian fourth-moment and convex-symmetrization facts are used as established tools, not asserted as new.

## Limitations

The result does **not** establish optimality against arbitrary non-Gaussian dependence with fixed normal marginals, except within the stated jointly Gaussian class. The finite-noise threshold is proved only for scalar linear shrinkage; extension to nonlinear thresholding, general multivariate predictors, and non-Gaussian perturbations is open. The correlation optimization depends on \(\mu^2/\sigma^2\), so an implementable oracle-free tuning rule is not provided. Independence of the randomization from \(Y\), known \(\sigma\), and exact Gaussian marginals are essential hypotheses. The historical-priority search cannot exclude equivalent formulas in unindexed literature on quadratic Gaussian Monte Carlo couplings.

## References

- S. Liu, S. Panigrahi, and J. A. Soloff, *Cross-Validation with Antithetic Gaussian Randomization*, arXiv:2412.14423, originally submitted 2024-12-19, https://arxiv.org/abs/2412.14423.
- S. Chattopadhyay, S. Liu, and S. Panigrahi, *On the Optimality of Antithetic Randomization for Cross-Validation*, arXiv:2608.08089, originally submitted 2026-08-08, https://arxiv.org/abs/2608.08089.
- S. Abkin and P. Daripa, *Sign-switched antithetic coupling in gradient random-walk methods for convection–diffusion equations*, arXiv:2610.01120, originally submitted 2026-10-01, https://arxiv.org/abs/2610.01120.
- L. Isserlis, *On a formula for the product-moment coefficient of any order of a normal frequency distribution in any number of variables*, Biometrika 12 (1918), 134–139. Gaussian fourth-moment identity (classical).

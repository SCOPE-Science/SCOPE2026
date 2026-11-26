# A universal one-half noise-correlation transition in two-query Gaussian quadrature

## Setting and result

Let \(X(t)\), \(t\in T\), be a centered Gaussian process with continuous covariance \(K\) on a compact metric set, and let \(J\) be a scalar linear target jointly Gaussian with the process. Write \(g(t)=\operatorname{Cov}(J,X(t))\). Assume \(g\ge0\), its positive maximum \(M\) is attained at a unique point \(t_*\), and its zero set \(Z\) is nonempty. We make two predetermined queries \(Y_i=X(t_i)+\epsilon_i\); repetitions are allowed. The error vector is **jointly Gaussian** with mean zero and covariance \(\eta R_\rho\), where \(\eta>0\), \(-1<\rho<1\), and
\[
R_\rho=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}.
\]
The error vector is independent of \((J,X)\), and its law is the same at all pairs of sites, including repeated ones. Define \(G_\eta=\operatorname{Var}(J)-\operatorname{Var}(J\mid Y_1,Y_2)\); under these hypotheses the conditional variance is deterministic.

For fixed \(\rho\) and \(\eta\to\infty\),
\[
\max_{t_1,t_2\in T}G_\eta(t_1,t_2)=
\frac{M^2}{\eta}\max\left\{\frac{2}{1+\rho},\frac{1}{1-\rho^2}\right\}+O(\eta^{-2}).
\]
If \(\rho<1/2\), every sequence of globally optimal pairs converges to \((t_*,t_*)\). If \(\rho>1/2\), its distance to \((\{t_*\}\times Z)\cup(Z\times\{t_*\})\) tends to zero. At equality the leading objectives tie; no finer selection is asserted. A zero of \(g\) need not be a deterministic process value: it serves as a reference through the correlation of its observation error with the signal observation's error.

For example, the zero-endpoint Brownian bridge on \([0,1]\) with \(J=\int_0^1X(t)\,dt\) has \(g(t)=t(1-t)/2\), giving \(t_*=1/2\), \(M=1/8\), and \(Z=\{0,1\}\). The Brownian-bridge high-noise limit is an illustration, not a separate originality claim. The result does not rely on pinned reference sites: if \(X=B+U\) with \(B\) a bridge and \(U\sim N(0,\tau^2)\) an independent random constant, the target \(J=\int_0^1 X(t)\,dt-X(0)=\int_0^1 B(t)\,dt\) has the same \(g\). For \(\tau>0\) even the endpoint readings contain nonzero latent variance.

## Proof

Let \(\mathbf g=(g(t_1),g(t_2))^{\mathsf T}\) and \(K_2=(K(t_i,t_j))_{i,j=1}^2\). Joint Gaussian conditioning gives
\[
G_\eta(t_1,t_2)=\mathbf g^{\mathsf T}(\eta R_\rho+K_2)^{-1}\mathbf g.
\]
The cross-covariance is continuous by Cauchy–Schwarz and mean-square continuity of \(X\), which follows from continuity of \(K\). Therefore the gain is continuous and has a maximum on \(T^2\). On that compact domain, \(K_2\) is uniformly bounded. Since \(K_2\succeq0\) and \(\lambda_{\min}(R_\rho)=1-|\rho|\), the resolvent identity gives the uniform bound
\[
\left\|(\eta R_\rho+K_2)^{-1}-\eta^{-1}R_\rho^{-1}\right\|
\le \frac{\sup_{T^2}\|K_2\|}{\eta^2(1-|\rho|)^2}.
\]
This implies \(\eta G_\eta=Q(g(t_1),g(t_2))+O(\eta^{-1})\) uniformly, with
\[
Q(x,y)=\frac{x^2-2\rho xy+y^2}{1-\rho^2}.
\]
The Hessian \(2R_\rho^{-1}\) is positive definite. Any point in \([0,M]^2\) other than a vertex is a nontrivial convex combination of vertices and, by strict convexity, gives strictly less than the maximum vertex value. All vertices are attained by site pairs. The origin is not a maximizer; the difference \(Q(M,0)-Q(M,M)\) equals \(M^2(2\rho-1)/(1-\rho^2)\) and \(Q(0,M)=Q(M,0)\). Maximizing the uniform estimate proves the gain expansion. A cluster point of maximizing pairs must maximize the continuous limiting objective by uniform convergence. Compactness then implies convergence in distance to its maximizing set, whose description follows from the hypotheses on \(g\).

## Scope, verification, and prior work

The posterior result does not hold for arbitrary independent-of-process errors with just the same covariance. The matrix formula still gives the explained variance of the best *linear* predictor for such errors, but the true conditional expectation can be nonlinear. For example, at \(\rho=0\) let the errors be independent symmetric \(\pm\sqrt{\eta}\) variables. A noisy midpoint observation \(Y\) of a Brownian bridge admits the reconstruction \(Y-\sqrt\eta\operatorname{sign}(Y)\), which equals the midpoint value \(X(1/2)\) on \(|X(1/2)|<\sqrt\eta\) and otherwise has error at most \(2\sqrt\eta\). Its mean squared error tends to zero by the Gaussian tail. Since \(\mathbb E[J\mid X(1/2)]=X(1/2)/2\), the explained variance of the true conditional expectation using a midpoint and an endpoint tends to \(1/16\), not zero: the second reading contains only independent noise, and the component of \(J\) orthogonal to \(X(1/2)\) is independent of both readings. The high-noise result also does not address site-dependent noise, \(\rho\) tending to \(\pm1\) with \(\eta\), adaptive queries, more than two queries, or complete finite-noise optimality.

The unchanged companion `verify.py` checks the leading quadratic and its vertex comparison symbolically, and tests 1,200 rational samples of the resolvent bound. It also contains Brownian-bridge finite-noise calculations from the original comparison, separate from the theorem asserted here. These finite checks corroborate but do not prove the theorem.

The covariance-aware conditioning and design framework is established. Attia and Constantinescu treat optimal design with correlated observations in inverse problems; Cai, Lam and Scarlett analyze average-case and noisy Bayesian quadrature. The record *A sharp finite-noise symmetry-breaking frontier in two-query Brownian-bridge quadrature* gives the complete finite-noise Brownian-bridge optimizer geometry for nonnegative correlation, including its limiting half-correlation boundary. The surviving assertion here is the fixed two-query high-noise geometry transition for general latent covariances and nonnegative target cross-covariance; no distinct finite-noise Brownian-bridge result or priority for the Brownian-bridge instance is asserted.

1. A. Attia and E. Constantinescu, *Optimal Experimental Design for Inverse Problems in the Presence of Observation Correlations*, https://arxiv.org/abs/2007.14476.
2. X. Cai, C. T. Lam and J. Scarlett, *On Average-Case Error Bounds for Kernel-Based Bayesian Quadrature*, https://arxiv.org/abs/2202.10615.
3. M. Naslidnyk, J. Gonzalez and M. Mahsereci, *Invariant Priors for Bayesian Quadrature*, https://arxiv.org/abs/2112.01578.
4. *A sharp finite-noise symmetry-breaking frontier in two-query Brownian-bridge quadrature*, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-a-sharp-finite-noise-symmetry-breaking-frontier-in-two-query-bro--f9e14ae9ff03/RESULT.md.

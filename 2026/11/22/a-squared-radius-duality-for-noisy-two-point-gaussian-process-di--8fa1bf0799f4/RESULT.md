# A squared-radius duality for noisy two-point Gaussian-process differentiation

## Finding

Let \(\eta>0\). Under the two stationary, unit-variance Gaussian-process priors
\[
k_G(s,t)=\exp(-(s-t)^2/2),\qquad
k_M(s,t)=(1+|s-t|)\exp(-|s-t|),
\]
observe the two noisy function values at \(-h\) and \(h\), with independent centered Gaussian noise of variance \(\eta\) per observation. Estimate the mean-square derivative at the origin by its posterior conditional mean, and minimize its posterior mean-square error over all \(h>0\), within the class of symmetric two-site experiments.

There is one and only one optimal positive half-spacing for each prior. Write \(t=t(\eta)\) for the unique solution in \((0,1)\) of
\[
\frac{(1+t)\exp(-2t)}{1-t}=1+\eta.
\]
Then the optimal half-spacings obey the exact cross-kernel identity
\[
\boxed{h_M=t,\qquad h_G=\sqrt t,\qquad h_M=h_G^2.}
\]
The two optimal posterior derivative variances, normalized by the common prior derivative variance \(1\), are
\[
\boxed{R_M=t,\qquad R_G=1-(1-t)e^t.}
\]
Consequently \(0<R_G<R_M<1\), and the strict risk gap is \((1-t)(e^t-1)\). Both optimal half-spacings increase strictly with \(\eta\), approaching \(0\) at small noise and \(1\) at large noise. As \(\eta\downarrow0\),
\[
t\sim (3\eta/2)^{1/3},\quad
h_M\sim(3\eta/2)^{1/3},\quad h_G\sim(3\eta/2)^{1/6},
\]
\[
R_M\sim(3\eta/2)^{1/3},\qquad
R_G\sim\tfrac12(3\eta/2)^{2/3}.
\]
Here all comparisons concern two different normalized stochastic prior models; the risks are not two estimators applied to the same law.

## Assumptions and scope

Each real-valued process is centered and stationary on \(\mathbb R\), with one of the kernels displayed above. Both mean-square derivatives \(D=X'(0)\) exist, and \(\operatorname{Var}(D)=-k''(0)=1\). There are exactly two measurements \(Y_+=X(h)+\epsilon_+\), \(Y_-=X(-h)+\epsilon_-\), where \(\epsilon_\pm\) are mutually independent \(N(0,\eta)\), independent of \(X\). The two designs have equal measurement noise relative to unit process variance. The objective is the exact Bayes risk of the posterior conditional mean of \(D\), which is a deterministic posterior variance. Only symmetric sampling times \(\pm h\) with finite \(h>0\) are optimized. The stationary mean is assumed known as zero, and kernel lengthscales have been normalized to one.

## Proof

**Conditional-variance reduction.** Write \(k(r)=k(r,0)\), \(g(h)=-k'(h)\). Stationarity and evenness give \(\operatorname{Cov}(D,Y_\pm)=\pm g(h)\), while the measurement covariance is
\[
\Sigma_Y=\begin{pmatrix}1+\eta&k(2h)\\ k(2h)&1+\eta\end{pmatrix}.
\]
Since \(\eta>0\), it is strictly positive definite. The conditional mean and risk therefore are
\[
\widehat D=\frac{g(h)}{1+\eta-k(2h)}(Y_+-Y_-),\quad
R(h)=1-\frac{2g(h)^2}{1+\eta-k(2h)}.
\]
Thus only the antisymmetric observation mode matters.

**The two normalized gain functions.** Set \(c=1+\eta>1\). In the Gaussian case \(g_G(h)=he^{-h^2/2}\). In the Matérn case \(g_M(h)=he^{-h}\). With a common positive auxiliary variable \(z\), equal to \(h^2\) for the Gaussian kernel and \(h\) for the Matérn kernel, the reductions in posterior variance are
\[
E_G(z)=\frac{2ze^{-z}}{c-e^{-2z}},\qquad
E_M(z)=\frac{2z^2e^{-2z}}{c-(1+2z)e^{-2z}},\qquad z>0.
\]
The denominators are positive because \(c>1\) and \((1+2z)e^{-2z}\le1\).

**Identical stationarity equation and uniqueness.** Direct differentiation, with positive multipliers removed, yields for *both* gains the derivative sign
\[
\operatorname{sign}(E_G'(z))=\operatorname{sign}(E_M'(z))
=\operatorname{sign}\big(c(1-z)e^{2z}-(1+z)\big).
\]
For \(z\ge1\), this sign is strictly negative. For \(0<z<1\), define
\[
F(z)=\frac{1+z}{1-z}e^{-2z},\qquad
\frac{F'(z)}{F(z)}=\frac{2z^2}{1-z^2}>0.
\]
Moreover \(F(0)=1<c\) and \(F(z)\to\infty\) as \(z\uparrow1\). Therefore there is exactly one \(t\in(0,1)\) such that \(F(t)=c\). Each gain increases on \((0,t)\) and decreases on \((t,\infty)\). Their limits at \(0\) and \(\infty\) are zero, so the global maxima are attained uniquely at this shared \(t\). Returning to physical half-spacings gives \(h_M=t\) and \(h_G=\sqrt t\).

**Exact risks and strict ordering.** Substituting \(c=e^{-2t}(1+t)/(1-t)\) into the two gains yields \(E_M(t)=1-t\) and \(E_G(t)=(1-t)e^t\). Subtracting from prior variance one proves the two risk formulas. The Gaussian risk is strictly smaller since \((1-t)(e^t-1)>0\) for \(0<t<1\).

**Noise monotonicity and asymptotics.** Strict increase of \(F\) makes \(t(\eta)=F^{-1}(1+\eta)\) strictly increasing. Expansion near zero gives
\[
F(t)=1+\frac23t^3+O(t^4),\qquad
1-(1-t)e^t=\frac12t^2+O(t^3),
\]
which implies every small-noise asymptotic above. At the other endpoint, \(1-t\sim2e^{-2}/(1+\eta)\), proving approach to unit half-spacing. These are asymptotics within the specified symmetric, unit-lengthscale models.

## Verification

The accompanying `verify_symbolic.py` symbolically factors both derivatives and substitutes the common stationary equation to reproduce each risk. The standalone `verify_numeric.py` checks the conditional covariance identities, the unique bracketed root, the squared-radius identity and risk formulas across multiple noise levels. Execute from this directory with `python3 verify_numeric.py`; for exact symbolic algebra install SymPy and run `python3 verify_symbolic.py`. The infinite-domain uniqueness and limiting statements follow from the analytic proof; finite computations are corroboration, not a substitute.

## Relationship to prior work

Berahas, Cao, Choromanski and Scheinberg (2019, first public May 3) analyze finite-difference, interpolation and random-smoothing gradient estimates from noisy function values and derive sampling-radius guarantees under objective-function assumptions. Their results do not imply this two-prior exact Bayesian spacing identity. Zhou and Wang (2020, first public November 22) use Gaussian-process conditional derivative models to infer differential-equation parameters from noisy observations; their displayed regression methodology does not give these exact two-point, cross-kernel design optima. Classical Gaussian-process covariance differentiation supplies the first conditional-variance step, not the shared stationarity equation or its unusual squared-radius consequence. Comparison is claim-level and historical priority is provisional.

## Limitations

The theorem does not optimize over arbitrary asymmetric pairs, more measurements, unknown lengthscale, hyperparameter estimation, non-Gaussian noise, or misspecified priors. Both kernels have different smoothness, so the risk ordering is a comparison under separately normalized Bayesian models, not an estimator dominance result on a fixed distribution. Exact equality of radii depends on the stated normalization and equal relative noise. A specialist design paper might contain an equivalent result not found in the inspected primary material; independent historical-priority verification is not performed.

## References

1. A. S. Berahas, L. Cao, K. Choromanski, and K. Scheinberg, *A Theoretical and Empirical Comparison of Gradient Approximations in Derivative-Free Optimization*, arXiv:1905.01332v1 (May 3, 2019), https://arxiv.org/abs/1905.01332 .
2. Y. Zhou and H. Wang, *Inferring the unknown parameters in Differential Equation by Gaussian Process Regression with Constraint*, arXiv:2011.10971v1 (November 22, 2020), https://arxiv.org/abs/2011.10971 .

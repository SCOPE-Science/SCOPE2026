# Globally optimal precision budgets and observation meshes for Ornstein–Uhlenbeck Bayesian quadrature

## Finding

Let \(X\) be a centered stationary Gaussian process on \([0,1]\) with covariance \(K(s,t)=e^{-\lambda|s-t|}\), where \(\lambda>0\). To estimate \(J=\int_0^1 X(t)\,dt\), make at most \(n\ge1\) predetermined noisy point observations \(Y_i=X(t_i)+\epsilon_i\), with independent centered Gaussian noises of variances \(1/p_i\), independent of \(X\), and nonnegative precisions satisfying \(\sum_i p_i=P>0\). Zero precision represents an unused sensor. Minimize the unconditional mean-square error of the Gaussian conditional-mean estimator, jointly over times, precision allocations, and estimators.

**Theorem.** For every \(n\ge1\), \(\lambda>0\), and \(P>0\), the unique optimum up to permutation uses \(n\) distinct interior sites, equal precision \(p_i=P/n\), and equal positive quadrature weights. For \(n=1\), its time is \(1/2\). For \(n\ge2\), define \(d\) as the unique root in \((0,1/(n-1))\) of
\[
\frac{1-e^{-\lambda g}}{1+n/P}
=\frac{\tanh(\lambda d/2)}{1+(n/P)\tanh(\lambda d/2)},
\qquad g=\frac{1-(n-1)d}{2}.
\]
Then the optimal times and their common conditional-mean weight are
\[
\boxed{t_i=g+(i-1)d,\quad p_i=P/n,\quad
w_i=w=\frac{2(1-e^{-\lambda g})}{\lambda(1+n/P)},\qquad 1\le i\le n.}
\]
For \(n=1\) the same weight formula holds with \(g=1/2\). Set
\[
V_0=\frac{2(\lambda-1+e^{-\lambda})}{\lambda^2},\qquad
b(t)=\frac{2-e^{-\lambda t}-e^{-\lambda(1-t)}}{\lambda}.
\]
The exact minimum Bayes mean-square error is
\[
\boxed{R_{n,\lambda,P}=V_0-w\sum_{i=1}^{n}b(t_i).}
\]
For \(n\ge2\), the sum can be evaluated without a matrix inversion:
\[
\sum_{i=1}^n b(t_i)
=\frac2\lambda\left[n-e^{-\lambda g}\frac{1-e^{-\lambda nd}}{1-e^{-\lambda d}}\right].
\]

**Universal spacing transition.** If \(P<n\), then \(g>d\); if \(P>n\), then \(g<d\). At exactly \(P=n\), independently of \(\lambda\), the sites are \(t_i=i/(n+1)\). Thus equal gaps *including the two boundary margins* occur at precisely one precision budget. For fixed \(\lambda,P>0\), \(R_{n+1,\lambda,P}<R_{n,\lambda,P}\).

## Assumptions and scope

All covariance parameters are known, observations are scalar and predetermined, and the Gaussian noises have independently adjustable positive precisions (one observation with precision \(p\) has noise variance \(1/p\)). The total precision \(P\), not each individual observation variance, is constrained. Co-located observations can be combined by adding precisions. The estimator is unrestricted among square-integrable functions of the observations: Gaussian conditioning makes the posterior mean globally mean-square optimal, with deterministic weights. A zero-precision observation is ignored, not interpreted as an infinite-variance random variable in a Gaussian density. No adaptive, nonlinear measurement functional or sensor-dependent acquisition cost is permitted.

The covariance normalization is \(K(t,t)=1\). If the covariance is \(\sigma^2 e^{-\lambda|s-t|}\), the same optimal sites and precision allocations follow from the unit-variance theorem with effective budget \(\sigma^2P\); the resulting minimum risk is \(\sigma^2\) times the unit-variance risk at that effective budget, while its conditional-mean weights are unchanged. The theorem is stated only for the unit-variance normalization to avoid ambiguity.

## Proof

**1. Reduction to a kernel-energy problem.** For any distinct sites and nonzero precisions \(p_i\), write \(K_T=(K(t_i,t_j))\), \(b_T=(b(t_i))\), and \(V_0=\operatorname{Var}(J)\). A linear estimator with weights \(w_i\) has mean-square error
\[
E(T,w,p)=V_0-2b_T^{\mathsf T}w+w^{\mathsf T}K_Tw
+\sum_i w_i^2/p_i.
\]
Gaussian conditioning minimizes this over weights and in fact minimizes the risk over all square-integrable estimators. By Cauchy–Schwarz, jointly minimizing independent-noise contribution over \(p_i\ge0\), \(\sum_i p_i=P\), yields
\[
\min_p\sum_i\frac{w_i^2}{p_i}=\frac{(\sum_i|w_i|)^2}{P},
\qquad p_i=P\frac{|w_i|}{\sum_j|w_j|}
\]
for every nonzero weight (zero weight allows zero precision). Thus optimize the continuous coercive objective
\[
F(T,w)=V_0-2b_T^{\mathsf T}w+w^{\mathsf T}K_Tw
+\frac{\|w\|_1^2}{P}.
\]
A minimizer exists: sites range over a compact cube and the last term bounds the weights. As \(b(t)>0\) everywhere and an observation can reduce variance, the optimal weight vector is nonzero.

**2. Strict positivity at every distinct active site.** Fix distinct ordered sites and positive precisions, and let \(N=\operatorname{diag}(1/p_i)\). The Gaussian-optimal weights solve \((K_T+N)w=b_T\). The exponential covariance is Gauss–Markov. Its inverse \(Q=K_T^{-1}\) is symmetric positive definite and tridiagonal with negative off-diagonal entries, because the Gaussian density factorizes through the transitions \(X(t_{i+1})=e^{-\lambda(t_{i+1}-t_i)}X(t_i)+\zeta_i\). Also \(\alpha=Qb_T\) is strictly positive componentwise: \(\alpha_i\) equals the integral of the nonnegative, nonzero Markov interpolation basis for \(X(t_i)\), given all the sites. On a gap of length \(\ell\), the adjacent endpoint basis contributes \(\tanh(\lambda\ell/2)/\lambda>0\); a terminal interval of length \(\ell\) contributes \((1-e^{-\lambda\ell})/\lambda\). Therefore
\[
(I+QN)w=\alpha>0.
\]
The matrix \(I+N^{1/2}QN^{1/2}\) is a symmetric positive definite matrix with nonpositive off-diagonals, so it has an entrywise nonnegative inverse (the standard Stieltjes-matrix property). Similarity gives \((I+QN)^{-1}\ge0\) entrywise and has positive diagonal. Hence every \(w_i>0\). This holds for arbitrary positive precision allocations. At a joint optimum with distinct active sites, therefore, \(p_i=Pw_i/W\), where \(W=\sum_iw_i\), and the common penalty-gradient constant is \(c=W/P\).

**3. Full use of the sensor count and exclusion of endpoints.** If two observations share a site, replacing them with one observation whose precision is their sum leaves their joint information unchanged. Assume an optimal design uses \(m\le n\) distinct positive-weight sites. At a used site \(t_i\), the stationarity in \(w_i\) from Step 1 gives the residual kernel potential
\[
r(t)=b(t)-\sum_{j=1}^m w_j e^{-\lambda|t-t_j|},\qquad r(t_i)=c>0.
\]
If the smallest site is at \(0\), move that site to the right while keeping weights and total weight fixed. The one-sided derivative of \(F\) equals \(-2\lambda w_1(c+w_1)<0\). Likewise, moving a right-endpoint site left decreases \(F\). Thus every active site is interior. If \(m<n\), split one interior atom of weight \(w>0\) at \(t\) into two atoms of weights \(w/2\) at \(t\pm\varepsilon\), leaving all other weights fixed. The term \(\|w\|_1^2/P\) stays unchanged; the smooth external potential and interactions with other distinct sites change by \(O(\varepsilon^2)\), whereas the atom's self-energy decreases by
\[
\frac{w^2}{2}(1-e^{-2\lambda\varepsilon})
=\lambda w^2\varepsilon+O(\varepsilon^2)>0.
\]
Hence \(F\) strictly decreases for small \(\varepsilon>0\), a contradiction. Every optimal design therefore uses all \(n\) distinct, interior, positive-weight sites, and the optimum is in the differentiable interior of the ordered-site domain.

**4. Equal weights and equal interior gaps from the residual differential equation.** Since all optimal weights are positive, differentiation in \(w_i\) gives \(r(t_i)=c=W/P\) at each site. Differentiating the site location in \(F\) gives \((r'(t_i^-)+r'(t_i^+))/2=0\). The exponential kernel makes \(r'\) jump upward by \(2\lambda w_i\) at \(t_i\), so
\[
r'(t_i^-)=-\lambda w_i,\qquad r'(t_i^+)=\lambda w_i.
\]
On every open gap, \(r''-\lambda^2r=-2\lambda\). Moreover \(0<c<2/\lambda\), because \(b(t_i)=c+\sum_jK(t_i,t_j)w_j<2/\lambda\). Set \(\alpha_*=2/\lambda-c>0\). On an interior gap of length \(d_i=t_{i+1}-t_i>0\), the unique solution with both endpoint values \(c\) is
\[
r(t)=\frac2\lambda-\alpha_*\frac{\cosh(\lambda(t-(t_i+t_{i+1})/2))}{\cosh(\lambda d_i/2)}.
\]
Its endpoint derivatives give the identity
\[
w_i=w_{i+1}=\alpha_*\tanh(\lambda d_i/2).
\]
Consequently all weights are equal, and since the hyperbolic tangent is strictly increasing, all interior gaps equal one common \(d>0\).

**5. Symmetric margins and scalar characterization.** Since \(b'(0)=\lambda b(0)\) and \(b'(1)=-\lambda b(1)\), the residual obeys the same Robin conditions \(r'(0)=\lambda r(0)\), \(r'(1)=-\lambda r(1)\). Solving its inhomogeneous ODE on the left terminal interval of length \(g_L=t_1\), with \(r(t_1)=c\), \(r'(t_1^-)=-\lambda w\), gives
\[
w=\frac2\lambda-c-\frac2\lambda e^{-\lambda g_L}.
\]
The right terminal interval similarly gives the formula with \(g_R=1-t_n\). Hence \(g_L=g_R=g\), and \(2g+(n-1)d=1\). Since \(c=nw/P\), the terminal equation and the interior-gap equation respectively become
\[
w=\frac{2(1-e^{-\lambda g})}{\lambda(1+n/P)},\qquad
w=\frac{(2/\lambda)\tanh(\lambda d/2)}{1+(n/P)\tanh(\lambda d/2)}.
\]
Their equality is precisely the scalar equation in the theorem. For \(n\ge2\), as \(d\) increases from zero to \(1/(n-1)\), \(g\) strictly decreases from \(1/2\) to zero; the equation's left side strictly decreases from a positive value to zero, while the right side strictly increases from zero to a positive value. There is exactly one root. Every global optimum must have this unique ordered configuration. Existence from Step 1 then proves global optimality and uniqueness. For \(n=1\), symmetry and strict decrease of \(b(t)\) away from \(1/2\) show the sole optimal time is \(1/2\). The optimum weights are \(w=(K_T+\operatorname{diag}(n/P))^{-1}b_T\) and agree with the displayed scalar formulas by stationarity; consequently its posterior risk is \(V_0-w\sum_i b(t_i)\).

**6. Sharp spacing transition and strict improvement with more sensors.** At \(d=g\), use \(\tanh(z)=(1-e^{-2z})/(1+e^{-2z})\). The sign of the left side minus the right side of the defining equation is exactly the sign of \(P-n\). Since that difference is strictly decreasing in \(d\), its root satisfies \(d>g\) if \(P>n\), and \(d<g\) if \(P<n\). Equality holds exactly at \(P=n\), where \(d=g=1/(n+1)\). The splitting argument in Step 3 applies to an optimum with \(n\) sensors when one more sensor is available, proving strict decrease of risk in sensor count at fixed total precision.

## Verification

The standalone file `verify_ou_budget.py` independently solves the scalar equation and compares the resulting uniform-weight formula against Gaussian Schur complements. It tests 96 combinations of \(n\), \(\lambda\), and \(P\), checks the universal uniform-grid identity in 32 additional cases, and compares 4,788 randomly generated competing node/precision allocations or numerically optimized precision allocations at random node sets. Its finite checks do not prove global optimality; Steps 1–6 supply the proof. Run `OPENBLAS_NUM_THREADS=1 python verify_ou_budget.py` with the dependencies stated in `requirements.txt`.

For a concrete example take \(n=P=3\), \(\lambda=2\). The unique sites are \(1/4,1/2,3/4\); each sensor has precision 1 and each quadrature coefficient is \((1-e^{-1/2})/2\). The posterior risk is \(0.2130613194252669\ldots\) for the unit-variance covariance normalization.

## Relationship to prior work

Pronzato and Zhigljavsky (2018) give the kernel-energy and Bayesian-quadrature framework and treat the exponential covariance in an example, but not the present simultaneous fixed-budget precision and arbitrary-node optimization. Karvonen, Kanagawa and Särkkä (2018) establish criteria for positive Bayesian quadrature weights, but not this global fixed-precision-budget classification; the independent Markov/Stieltjes argument here accommodates the exponential kernel's diagonal cusp and measurement noise. Cai, Lam and Scarlett (2022) analyze noisy kernel-quadrature error rates, not exact finite-budget sensor allocations. An accessible published theorem on noiseless Ornstein–Uhlenbeck Bayesian quadrature already proves the equal-internal-gap, symmetric-margin grid when evaluations are exact; that regime is not claimed as new. A separate previously established two-noisy-site equal-variance theorem gives the \(n=2\) special case but does not imply global precision allocation or the all-\(n\) result. The present theorem adds finite arbitrary \(n\), freely distributed positive measurement precision, exact risk, and the universal \(P=n\) spacing transition.

## Limitations

The noise precisions are continuously divisible, and the process is centered with known stationary exponential covariance. The result does not cover discrete integer replicates without precision interpolation, observation-dependent sampling, unknown covariance parameters, nonstationary OU initial conditions, correlated noise, non-Gaussian estimators outside the stated Gaussian model, or alternative kernels. A remaining scientific-priority risk is an earlier equivalent treatment in optimal-design literature not surfaced by the accessible comparisons, especially older dissertations that discuss integral estimation. The self-review are not independent mathematical validation.

## References

1. L. Pronzato and A. Zhigljavsky, *Bayesian quadrature and energy minimization for space-filling design*, arXiv:1808.10722v1, first public 2018-08-31, https://arxiv.org/abs/1808.10722.
2. T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, arXiv:1812.08509v1, first public 2018-12-20, https://arxiv.org/abs/1812.08509.
3. X. Cai, C. T. Lam and J. Scarlett, *On Average-Case Error Bounds for Kernel-Based Bayesian Quadrature*, arXiv:2202.10615v1, first public 2022-02-22, https://arxiv.org/abs/2202.10615.
4. K. Sikolya and S. Baran, *On the optimal designs for the prediction of complex Ornstein–Uhlenbeck processes*, arXiv:1808.03444, https://arxiv.org/abs/1808.03444 (related integrated pointwise prediction criterion, not posterior integral variance).

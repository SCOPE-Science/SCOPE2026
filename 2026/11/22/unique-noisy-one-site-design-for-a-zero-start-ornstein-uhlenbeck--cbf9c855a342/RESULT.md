# Unique noisy one-site design for a zero-start Ornstein–Uhlenbeck integral

## Finding

Let \(B\) be standard Brownian motion and \(\lambda>0\). Consider the nonstationary zero-start Ornstein–Uhlenbeck process
\[
X_\lambda(t)=\int_0^t e^{-\lambda(t-u)}\,dB(u),\qquad 0\le t\le1,
\]
its integral \(I_\lambda=\int_0^1 X_\lambda(s)\,ds\), and a single observation \(Y_t=X_\lambda(t)+\varepsilon\), where \(\varepsilon\sim N(0,\eta)\) is independent of \(B\) and \(\eta\ge0\) (degenerate Gaussian at zero allowed).

**Theorem.** For every \(\lambda>0\) and every finite \(\eta\ge0\), the posterior mean-square error of the optimal estimator \(\mathbb E[I_\lambda\mid Y_t]\) has exactly one minimizing observation time \(t_*=t_*(\lambda,\eta)\) on the whole closed interval \([0,1]\), and \(1/2<t_*<1\). Define
\[
L=e^\lambda,\quad a=(2L)^{-1},\quad b=1-a,\quad T=2\lambda\eta,
\quad F(y)=a(1+T)y^3-[2a+b(1+T)]y+1.
\]
Then the unique root of \(F(y)=0\) in \((1,L)\) is \(y_*=e^{\lambda t_*}\), so \(t_*=\lambda^{-1}\log y_*\). At zero noise,
\[
y_*(\lambda,0)=\frac{\sqrt{1+8e^\lambda}-1}{2}.
\]
For fixed \(\lambda\), the optimal time increases strictly with \(\eta\) and converges as \(\eta\to\infty\) to the still-interior time
\[
t_\infty(\lambda)=\frac{\log(2e^\lambda-1)}{2\lambda}.
\]
The following damping asymptotic is uniform over **all** finite \(\eta\ge0\):
\[
t_*(\lambda,\eta)=\frac12+\frac{\log2}{2\lambda}
+O\!\left(\frac{e^{-\lambda/2}}{\lambda}\right),\qquad\lambda\to\infty.
\]
For fixed finite \(\eta\), as \(\lambda\downarrow0\), the optimal time converges to the noisy Brownian-motion placement
\[
t_B(\eta)=\frac{1-2\eta+\sqrt{(1-2\eta)^2+12\eta}}3.
\]

## Assumptions and scope

The Brownian diffusion coefficient is exactly one; \(X_\lambda(0)=0\) is deterministic (not drawn from its stationary distribution). The target is the Lebesgue time integral over exactly \([0,1]\). Exactly one observation is allowed at any deterministic \(t\in[0,1]\). Measurement noise is independent, centered Gaussian, with known finite variance \(\eta\); the variance can equal zero. We optimize posterior integrated **scalar-functional** mean-square error, not pointwise path reconstruction, model-parameter estimation, or computation time. The conditional-mean estimator is automatically the minimum-MSE estimator over all measurable functions of the observation because the joint law is Gaussian.

Write
\[
v(t)=\operatorname{Var}X_\lambda(t)=\frac{1-e^{-2\lambda t}}{2\lambda},\qquad
c(t)=\operatorname{Cov}(I_\lambda,X_\lambda(t))
=\frac{1-e^{-\lambda t}-\tfrac12e^{-\lambda(1-t)}+\tfrac12e^{-\lambda(1+t)}}{\lambda^2}.
\]
For \(t>0\) or \(\eta>0\), the optimal quadrature weight is \(w_t=c(t)/(v(t)+\eta)\); at \((t,\eta)=(0,0)\), the observation is deterministically zero and gives no information. The minimum posterior error at the optimizing time is
\[
V_*=V_0-\frac{c(t_*)^2}{v(t_*)+\eta},\qquad
V_0=\frac1{\lambda^2}\left[1-\frac{2(1-e^{-\lambda})}{\lambda}
+\frac{1-e^{-2\lambda}}{2\lambda}\right].
\]

## Proof

**1. Covariance reduction.** By stochastic Fubini,
\[
I_\lambda=\int_0^1\frac{1-e^{-\lambda(1-u)}}\lambda\,dB(u).
\]
Itô isometry gives \(v(t)\), \(c(t)\), and \(V_0\) displayed above. Gaussian conditioning gives
\[
\operatorname{Var}(I_\lambda\mid Y_t)=V_0-H(t),\qquad H(t)=\frac{c(t)^2}{v(t)+\eta}.
\]
At zero noise, the continuous extension \(H(0)=0\) follows because \(c(t)=O(t)\) and \(v(t)\sim t\). This handles the only degenerate denominator.

**2. A cubic with exactly one admissible stationary point.** Set \(y=e^{\lambda t}\), and use \(a,b,T\) from the theorem. Direct substitution yields
\[
H(t)=\frac2{\lambda^3}\frac{Q(y)^2}{D(y)},\qquad
Q(y)=y-a y^2-b=(y-1)\left(1-\frac{y+1}{2L}\right),
\quad D(y)=(1+T)y^2-1.
\]
For every \(1<y\le L\), \(Q(y)>0\), \(D(y)>0\), and
\[
\frac{d}{dy}\left(\frac{Q(y)^2}{D(y)}\right)
=-\frac{2Q(y)F(y)}{D(y)^2}.
\]
Now \(F(1)=-(1-L^{-1})T\le0\), \(F(L)=(L-1)^2(1+T)/2>0\), and \(F''(y)=6a(1+T)y>0\) for \(y>0\). If \(T>0\), strict convexity implies precisely one crossing of zero on \((1,L)\), with the sign negative beforehand and positive afterward. If \(T=0\), factorization gives
\[
F(y)=\frac{(y-1)(y^2+y-2L)}{2L},
\]
so again there is exactly one root inside \((1,L)\), namely \(y_0=(\sqrt{1+8L}-1)/2\). Therefore \(H\) strictly increases to that root and strictly decreases thereafter. The unique global maximizer of \(H\), and hence minimizer of posterior error, lies strictly inside the observation window.

**3. Exact location and noise monotonicity.** The zero-noise root satisfies \(y_0^2+y_0=2L\), which implies \(y_0>\sqrt L\) since \(L+\sqrt L<2L\) for \(L>1\). Define \(y_\infty=\sqrt{2L-1}\). Then \(y_0<y_\infty<L\), and
\[
F(y_\infty)=1-y_\infty/L>0,
\quad \partial_TF(y)=y(ay^2-b)<0\quad(1<y<y_\infty).
\]
For positive \(T\), \(F(y_0)<0\) and \(F(y_\infty)>0\); hence \(y_0<y_*<y_\infty\). At its (upward) crossing \(F_y(y_*)>0\), so implicit differentiation gives \(dy_*/dT=-F_T(y_*)/F_y(y_*)>0\). The limiting equation after division by \(T\) has its unique positive root \(y_\infty\). Thus all finite-noise times are strictly between \(1/2\) and \(t_\infty<1\), and increase strictly with noise.

**4. Boundary limits.** The closed-form endpoints satisfy
\[
y_0=\sqrt{2L}+O(1),\qquad y_\infty=\sqrt{2L}+O(L^{-1/2})
\quad(L\to\infty).
\]
The sandwich \(y_0\le y_*<y_\infty\), uniform in \(T\ge0\), therefore proves the uniform stiff limit given above. As \(\lambda\downarrow0\), Itô isometry gives convergence of \(v(t)\) and \(c(t)\) to the Brownian values \(t\) and \(t-t^2/2\), uniformly for \(t\in[0,1]\). In the zero-noise case the ratio extends continuously at zero and converges uniformly as well (use the Itô-integral representations); the unique maximizer therefore converges to the unique maximizer of \((t-t^2/2)^2/(t+\eta)\). Its stationary polynomial \(3t^2+(4\eta-2)t-4\eta=0\) has precisely one positive admissible root, giving \(t_B(\eta)\). This completes every asserted quantifier.

## Verification

`verify.py` uses only the Python standard library. Run `python verify.py` after extracting the package. It computes the unique cubic root by bisection; independently calculates Itô covariance through composite Simpson quadrature and the direct covariance formula; compares conditional variance against a dense deterministic observation-time grid; tests zero and positive noise, and verifies analytic monotonicity and asymptotic brackets. The reported discrete comparisons are supplementary **finite tests**, not a proof of global uniqueness or the asymptotic statements. The four analytic proof steps above are required for the general theorem.

## Relationship to prior work

Pronzato and Zhigljavsky (first public 2018) derive the general Bayesian quadrature posterior-variance/energy criterion (their Sections 2–4) and discuss covariance classes; those general formulas motivate the precise question but do not explicitly give the all-noise zero-start Ornstein–Uhlenbeck cubic, its unique root, or the uniform stiff-damping time law. Cai, Lam and Scarlett (2022) give noisy Bayesian quadrature error bounds with Matérn and squared-exponential kernels; these are error-rate results, not an exact one-observation nonstationary Ornstein–Uhlenbeck design classification. Mukherjee (2003) and the associated dissertation consider exact covariance-design problems including Ornstein–Uhlenbeck and Brownian processes, but full primary text was not available for line-by-line exclusion. Their accessible abstracts concern uncorrupted observations and/or path-IMSE criteria; no claim is made that all historical integral-design theorems were exhaustively ruled out. Published stationary Ornstein–Uhlenbeck node designs do not directly imply this zero-initialized, noisy design theorem because their covariance contains a stationary component absent here.

## Limitations

The theorem is for one observation only, fixed known damping and noise, a deterministic zero initial state, and the scalar time integral. It does not characterize optimal multiple-sensor layouts, correlated observation noise, unknown process parameters, adaptive schedules or worst-case deterministic integrands. The \(\eta\to\infty\) limiting time does not mean useful information survives infinite noise: the posterior variance reduction vanishes there. External independent mathematical review and conclusive historical publication-priority verification have not been performed. A plausible historical source (Mukherjee 2003) could not be fully inspected, leaving residual originality risk.

## References

1. L. Pronzato and A. Zhigljavsky, *Bayesian quadrature and energy minimization for space-filling design*, arXiv:1808.10722 (first publicly posted 2018-08-31); later *SIAM/ASA Journal on Uncertainty Quantification* 8 (2020), 959–1011, DOI:10.1137/18M1210332. https://arxiv.org/abs/1808.10722
2. X. Cai, C. T. Lam and J. Scarlett, *On Average-Case Error Bounds for Kernel-Based Bayesian Quadrature*, arXiv:2202.10615 (first posted 2022-02-22). https://arxiv.org/abs/2202.10615
3. B. Mukherjee, *On Sampling Designs for Integral Estimation of a Random Process*, *Communications in Statistics—Theory and Methods* (2003), DOI:10.1081/STA-120022249; abstract only inspected. https://doi.org/10.1081/STA-120022249
4. B. Mukherjee, *Optimal designs for estimating the path of a stochastic process*, Purdue dissertation (abstract consulted). https://docs.lib.purdue.edu/dissertations/AAI3043760/

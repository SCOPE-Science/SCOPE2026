# A sharp regularity-dependent endpoint transition in one-sample Gaussian Volterra quadrature

## Finding
For every real \(\alpha\geq 0\), let \(B\) be standard Brownian motion and define
\[
X_\alpha(t)=\frac{1}{\Gamma(\alpha+1)}\int_0^t(t-s)^\alpha\,dB(s),\qquad 0\leq t\leq1.
\]
We wish to estimate the random integral \(J_\alpha=\int_0^1X_\alpha(t)\,dt\) from exactly one observation \(Y_t=X_\alpha(t)+\varepsilon\), where \(\varepsilon\sim N(0,\eta)\) is independent, \(\eta\geq0\), and the observation location \(t\in[0,1]\) is chosen in advance. We minimize the posterior mean-square error of the Gaussian conditional-mean estimator, including the endpoint \(t=1\).

**Theorem.** There is a unique optimal observation time \(t_\alpha(\eta)\). For every \(\alpha>0\), put
\[
\eta_c(\alpha)=\frac{1}{4\alpha(\alpha+1)(2\alpha+1)\Gamma(\alpha+1)^2}.
\]
If \(0\leq\eta<\eta_c(\alpha)\), the optimum is interior; if \(\eta\geq\eta_c(\alpha)\), it is exactly the terminal time \(1\). For fixed \(\alpha>0\), the interior optimum moves strictly rightward with \(\eta\) and reaches the endpoint continuously at \(\eta_c(\alpha)\). In contrast, for \(\alpha=0\), the unique optimum is interior at **every finite** \(\eta\geq0\), moves strictly rightward, and tends to \(1\) only as \(\eta\to\infty\). The transition is sharp and has no additional local or global optimizers.

At an interior optimum, let
\[
c_\alpha(t)=\frac{1}{\Gamma(\alpha+1)\Gamma(\alpha+2)}\int_0^t(t-s)^\alpha(1-s)^{\alpha+1}\,ds,
\qquad
v_\alpha(t)=\frac{t^{2\alpha+1}}{(2\alpha+1)\Gamma(\alpha+1)^2}.
\]
The optimal location is equivalently the **unique** solution in \((0,1)\) of
\[
2t\,\frac{c_\alpha'(t)}{c_\alpha(t)}=(2\alpha+1)\frac{v_\alpha(t)}{v_\alpha(t)+\eta}.
\]
The exact optimal posterior variance is
\[
\frac{1}{(2\alpha+3)\Gamma(\alpha+2)^2}
-\frac{c_\alpha(t_\alpha(\eta))^2}{v_\alpha(t_\alpha(\eta))+\eta}.
\]
For \(\alpha=0\), the location has the closed form
\[
t_0(\eta)=\frac{1-2\eta+\sqrt{(1-2\eta)^2+12\eta}}{3},\qquad \eta\geq0.
\]
For \(\alpha=1\), the zero-noise optimum is \((6-\sqrt6)/5\), and terminal sampling becomes optimal **exactly** at \(\eta=1/24\). For \(\alpha=2\), that threshold is \(1/480\). As \(\alpha\downarrow0\), \(\eta_c(\alpha)\sim1/(4\alpha)\), explaining the absence of a finite threshold in the Brownian case.

## Assumptions and scope
The normalization of the Volterra kernel and measurement noise is fixed by the displayed definitions; the white-noise driving intensity is one and \(\eta\) is an **absolute variance** in those units. The parameter \(\alpha\) is any fixed real number in \([0,\infty)\), not merely an integer. For integer \(\alpha=r\), \(X_r\) is \(r\)-fold time-integrated Brownian motion. For noninteger \(\alpha\), it is the Riemann--Liouville Gaussian Volterra process of that order. Locations are deterministic and nonadaptive. The Gaussian estimator is the conditional expectation, with no restrictions on its scalar weight. The conclusion concerns exactly one observation, not several sites, unknown covariance, colored noise, or alternative losses. At \(t=0\), \(X_\alpha(0)=0\) is deterministic; observing it has no information about \(J_\alpha\), also when \(\eta=0\).

## Proof
**1. Conditional variance.** Stochastic Fubini, justified by the square-integrability of the deterministic Volterra kernel for \(\alpha\geq0\), gives
\[
J_\alpha=\frac{1}{\Gamma(\alpha+2)}\int_0^1(1-s)^{\alpha+1}\,dB(s).
\]
Ito isometry yields \(\operatorname{Var}(J_\alpha)=1/[(2\alpha+3)\Gamma(\alpha+2)^2]\), \(\operatorname{Cov}(J_\alpha,X_\alpha(t))=c_\alpha(t)\), and \(\operatorname{Var}(X_\alpha(t))=v_\alpha(t)\). Gaussian conditioning therefore makes the best predictor \(c_\alpha(t)Y_t/[v_\alpha(t)+\eta]\), with variance reduction
\[
G_{\alpha,\eta}(t)=\frac{c_\alpha(t)^2}{v_\alpha(t)+\eta},\quad t>0;
\qquad G_{\alpha,\eta}(0)=0.
\]
The extension at zero is continuous: since \(c_\alpha(t)\asymp t^{\alpha+1}\) and \(v_\alpha(t)\asymp t^{2\alpha+1}\), the gain is \(O(t)\) even at \(\eta=0\). Thus a global maximizer exists away from zero.

**2. Strict logarithmic-time concavity of the covariance.** Put \(t=e^x\) with \(x\leq0\) and substitute \(s=e^y\). Apart from a positive normalization factor,
\[
c_\alpha(e^x)=\int_{-\infty}^{x}e^y(e^x-e^y)^\alpha(1-e^y)^{\alpha+1}\,dy.
\]
The logarithm of the integrand, on the convex domain \(y<x\leq0\), is
\[
y+\alpha\bigl[x+\log(1-e^{y-x})\bigr]
+(\alpha+1)\log(1-e^y).
\]
It is jointly concave in \((x,y)\): \(z\mapsto\log(1-e^z)\) is concave for \(z<0\), and the remaining terms are affine. Extending by zero outside that convex domain preserves log-concavity. Prékopa's marginal log-concavity theorem now gives that \(x\mapsto\log c_\alpha(e^x)\) is concave. Hence
\[
u_\alpha(t)=t\frac{c_\alpha'(t)}{c_\alpha(t)}
\]
is nonincreasing in \(t\in(0,1)\). It is in fact **strictly decreasing**: it is real analytic in the open interval, and its endpoint limits are unequal (calculated in step 3). A nonincreasing real-analytic function taking an equal value at two different points would be constant on an interval, hence identically constant, a contradiction. This gives a global shape theorem, not a local numerical stationarity argument.

**3. Endpoint slopes.** The small-time kernel scaling gives \(u_\alpha(0+)=\alpha+1\). At \(t=1\), for \(\alpha>0\), differentiation under the integral (with integrable power \(\alpha-1\)) yields
\[
c_\alpha(1)=\frac{1}{(2\alpha+2)\Gamma(\alpha+1)\Gamma(\alpha+2)},\quad
c_\alpha'(1)=\frac{\alpha}{(2\alpha+1)\Gamma(\alpha+1)\Gamma(\alpha+2)}.
\]
Consequently \(u_\alpha(1)=2\alpha(\alpha+1)/(2\alpha+1)\). For \(\alpha=0\), direct use of \(c_0(t)=t-t^2/2\) gives \(u_0(1)=0\), agreeing with that formula by continuity. For all \(\alpha\geq0\), the difference between the two limiting slopes is \((\alpha+1)/(2\alpha+1)>0\), completing strictness in step 2.

**4. Global optimization and sharp activation.** For \(t\in(0,1)\), differentiation of the gain gives
\[
\frac{d\log G_{\alpha,\eta}(t)}{d\log t}
=2u_\alpha(t)-(2\alpha+1)\frac{v_\alpha(t)}{v_\alpha(t)+\eta}
=:H_{\alpha,\eta}(t).
\]
The first term is strictly decreasing by step 2. The subtracted term is nondecreasing in \(t\) (strictly for \(\eta>0\)). Therefore \(H_{\alpha,\eta}\) is strictly decreasing throughout \((0,1)\), with \(H_{\alpha,\eta}(0+)>0\). It has at most one zero; that zero, if present, is the unique global maximum of the gain. Otherwise the gain increases strictly up to the unique endpoint maximum.

For \(\alpha>0\), evaluate \(H\) at the right endpoint and denote \(a_\alpha=v_\alpha(1)=1/[(2\alpha+1)\Gamma(\alpha+1)^2]\):
\[
H_{\alpha,\eta}(1)
=\frac{4\alpha(\alpha+1)}{2\alpha+1}
-(2\alpha+1)\frac{a_\alpha}{a_\alpha+\eta}.
\]
This is nonnegative if and only if \(\eta\geq a_\alpha/[4\alpha(\alpha+1)]\), exactly the stated \(\eta_c(\alpha)\). At equality, \(H(t)>H(1)=0\) for all \(t<1\), so the endpoint remains the unique optimum. At \(\alpha=0\), \(H_{0,\eta}(1)=-1/(1+\eta)<0\) for every finite \(\eta\), hence the optimum is always interior. Increasing \(\eta\) strictly increases \(H_{\alpha,\eta}(t)\) at each fixed interior \(t\); uniqueness forces the interior maximizing location to move strictly rightward until endpoint activation, or indefinitely toward \(1\) in the Brownian case. Continuity of the unique root gives convergence to the endpoint at the stated transition. This proves all cases.

**5. Checks and examples.** For \(\alpha=0\), substitute \(c_0(t)=t-t^2/2\), \(v_0(t)=t\) into the stationarity equation. The positive quadratic root gives the stated closed form. For \(\alpha=1\), \(c_1(t)=t^2(t^2-4t+6)/24\) and \(v_1(t)=t^3/3\); at zero noise the interior stationarity polynomial factors to \(5t^2-12t+6\), giving \((6-\sqrt6)/5\). Substituting \(\alpha=1\) and \(2\) into the sharp threshold yields \(1/24\) and \(1/480\). Finally \(\alpha\Gamma(\alpha+1)^2\to0\) linearly in \(\alpha\), so \(\eta_c(\alpha)\sim1/(4\alpha)\).

## Verification
Run `python standalone/verify.py` after installing the dependency in `standalone/requirements.txt`. In the packaged source, the verifier independently evaluates the stochastic-integral covariance and variances by numerical quadrature, cross-checks their hypergeometric formulas, tests logarithmic derivatives and strict monotonicity for representative real orders, bisects the unique stationarity equation, and checks the claimed global maximum against fixed finite grids. A local replay passed 3,653 assertions for seven integer and fractional orders. These finite checks support reproducibility; the all-order uniqueness and threshold are established by the analytic proof above and the stated Prékopa theorem.

## Relationship to prior work
Cai, Lam, and Scarlett (arXiv:2202.10615, first publicly posted 2022-02-22) analyze noisy kernel-based Bayesian quadrature and general error rates, supplying the motivating noisy-integration framework. Their stated theorems do not characterize an optimal **single** location for the Volterra covariance family or its exact regularity-dependent terminal activation threshold. Zhang, Stringer, Brown, and Stafford (arXiv:2302.02053, first publicly posted 2023-02-04) develop integrated-Wiener process models and approximation methods, establishing the modeling relevance of these covariance families but not this design classification. Plaskota, Ritter, and Wasilkowski (2004) studied optimal approximation and integration designs for integrated Brownian processes on a half-line, and Mukherjee (2003) studied integration designs for product-form covariances. Those older, closely related articles were accessible here only through their abstracts: their full theorems have **not** been ruled out as possibly implying a special case, and literature priority remains uncertain. The present claim depends essentially on independently noisy one-site observations and includes all real nonnegative Volterra orders; no novelty is claimed for Gaussian conditioning itself, Prékopa's marginal theorem, or the standalone noiseless Brownian optimum.

## Limitations
No independent mathematical audit or publication-priority certification has been performed. The proof assumes a known unit-diffusion Gaussian Volterra prior, known additive **independent** Gaussian observation noise, a fixed interval, and one freely chosen location. It does not cover unknown smoothness, multiple sensors, sensor-placement cost, different noise scaling, non-Gaussian priors, or arbitrary integrand classes. Related older primary full texts were not obtained, so equivalent statements under other terminology remain a publication-priority risk. Numerical tests sample finitely many \(\alpha\), \(\eta\), and \(t\) values and cannot certify the continuum theorem.

## References
- X. Cai, C. T. Lam, J. Scarlett, *Order-Optimal Error Bounds for Noisy Kernel-Based Bayesian Quadrature*, initial arXiv posting 2022-02-22, https://arxiv.org/abs/2202.10615 (the full text was inspected).
- Z. Zhang, A. Stringer, P. Brown, J. Stafford, *Model-based Smoothing with Integrated Wiener Processes and Overlapping Splines*, initial arXiv posting 2023-02-04, https://arxiv.org/abs/2302.02053 (the full text was inspected).
- L. Plaskota, K. Ritter, G. W. Wasilkowski, *Optimal designs for weighted approximation and integration of stochastic processes on \([0,\infty)\)*, J. Complexity 20 (2004), 108–131, https://doi.org/10.1016/j.jco.2003.10.002 (abstract inspected; full text unavailable).
- B. Mukherjee, *On Sampling Designs for Integral Estimation of a Random Process*, Comm. Statist. Theory Methods 32 (2003), https://doi.org/10.1081/STA-120022249 (abstract inspected; full text unavailable).
- A. Prékopa, *On logarithmic concave measures and functions*, Acta Sci. Math. (Szeged) 34 (1973), 335–343 (marginal log-concavity theorem). See also A. Figalli and D. Jerison, *How to recognize convexity of a set from its marginals*, J. Funct. Anal. 266 (2014), https://doi.org/10.1016/j.jfa.2013.05.040.

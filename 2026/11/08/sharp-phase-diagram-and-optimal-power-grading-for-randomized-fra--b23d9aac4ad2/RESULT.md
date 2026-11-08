# Sharp phase diagram and optimal power grading for randomized fractional Brownian occupation quadrature

## Finding

Let \(0<H<1\), let \(B^H\) be standard centered fractional Brownian motion on \([0,1]\) with \(B_0^H=0\), and consider estimating its positive occupation time
\[
I_H=\int_0^1\mathbf1_{\{B^H_t>0\}}\,dt.
\]
For \(\gamma>0\) and integer \(n\ge1\), set \(t_i=(i/n)^\gamma\), independently draw \(T_i\) uniformly from each interval \([t_{i-1},t_i]\), independently of the entire process, and form
\[
Q_{n,\gamma}=\sum_{i=1}^n(t_i-t_{i-1})\mathbf1_{\{B^H_{T_i}>0\}}.
\]
This quadrature estimator is conditionally unbiased for every measurable sample path. Its unconditional mean-square error \(V_{n,\gamma}=\mathbb E[(Q_{n,\gamma}-I_H)^2]\) has the following complete asymptotic phase diagram.

Define \(c_{H,\gamma}=\gamma^{H+2}/[\pi(H+1)(H+2)]\) and \(a_j=\frac1{2\pi}\int_{(j-1)^\gamma}^{j^\gamma}\int_{(j-1)^\gamma}^{j^\gamma}\arccos(\rho_H(s,t))\,ds\,dt\), where
\[
\rho_H(s,t)=\frac{s^{2H}+t^{2H}-|s-t|^{2H}}{2s^Ht^H}\qquad(s,t>0).
\]
The integrand has its continuous limiting interpretation on the diagonal; its value on the measure-zero coordinate axes does not affect the integral. Then the exact finite-sample identity is
\[
V_{n,\gamma}=n^{-2\gamma}\sum_{j=1}^n a_j.
\]
The three regimes are:
\[
\begin{aligned}
2\gamma>H+1:&\quad \lim_{n\to\infty}n^{H+1}V_{n,\gamma}=\frac{c_{H,\gamma}}{2\gamma-H-1};\\
2\gamma=H+1:&\quad \lim_{n\to\infty}\frac{n^{H+1}V_{n,\gamma}}{\log n}=c_{H,\gamma};\\
2\gamma<H+1:&\quad \lim_{n\to\infty}n^{2\gamma}V_{n,\gamma}=\sum_{j=1}^{\infty}a_j\in(0,\infty).
\end{aligned}
\]
Among all power meshes in the optimal-rate regime, the leading mean-square error constant has a **unique** minimizing grading exponent
\[
\boxed{\gamma_*=1+H/2,\qquad K_H(\gamma_*)=\frac{(1+H/2)^{H+2}}{\pi(H+1)(H+2)}.}
\]
By comparison, the uniform mesh has \(K_H(1)=1/[\pi(1-H)(H+1)(H+2)]\), so the optimal-to-uniform limiting mean-square error ratio is \((1-H)(1+H/2)^{H+2}<1\).

## Assumptions and scope

The Hurst parameter is any fixed \(H\in(0,1)\); the grading exponent is any fixed \(\gamma>0\). The process is the centered **nonstationary** standard fractional Brownian motion started at zero, with covariance
\[
\mathbb E[B_s^HB_t^H]=\tfrac12(s^{2H}+t^{2H}-|t-s|^{2H}).
\]
Uniform draws are independent across distinct panels and independent of the path. The number of panels tends to infinity at fixed \(H,\gamma\). All expectations include both the process and the sampling randomization. No path discretization or conditional interpolation is assumed.

## Proof

**1. Exact conditional sampling variance.** Write \(\Delta_i=t_i-t_{i-1}\) and \(p_i=\Delta_i^{-1}\int_{t_{i-1}}^{t_i}\mathbf1_{\{B_t^H>0\}}dt\). Conditional on the complete path, each sampled sign is Bernoulli with parameter \(p_i\), so \(\mathbb E[Q_{n,\gamma}\mid B^H]=I_H\) and
\[
V_{n,\gamma}=\sum_{i=1}^n\Delta_i^2\mathbb E[p_i(1-p_i)].
\]
For two independent uniform times on a given panel, the expected disagreement indicator equals \(2\mathbb E[p_i(1-p_i)]\). For a nondegenerate centered bivariate normal pair with correlation \(\rho\), its sign disagreement probability is \(\arccos(\rho)/\pi\). Thus the panel contribution is \(\frac1{2\pi}\int\int\arccos(\rho_H(s,t))dsdt\). Since \(\rho_H(\lambda s,\lambda t)=\rho_H(s,t)\) for \(\lambda>0\), applying \(\lambda=n^{-\gamma}\) gives the displayed exact finite-sample identity.

**2. Sharp local panel asymptotics.** Fix \(H,\gamma\). For \(j\ge2\), put \(A=(j-1)^\gamma\), \(h=j^\gamma-(j-1)^\gamma\), and \(\eta=h/A\). Then \(\eta\to0\) and \(h\sim\gamma j^{\gamma-1}\), \(A\sim j^\gamma\). For \(A\le s<t\le A+h\), the algebraic covariance identity gives
\[
1-\rho_H(s,t)=\frac{|t-s|^{2H}-(t^H-s^H)^2}{2s^Ht^H}.
\]
By the mean-value theorem and \(0<H<1\),
\[
0\le \frac{(t^H-s^H)^2}{|t-s|^{2H}}\le H^2\eta^{2-2H}.
\]
Also \(s^Ht^H/A^{2H}\to1\) uniformly on a panel, and \(\arccos(1-z)/\sqrt{2z}\to1\) as \(z\downarrow0\). Consequently, uniformly over distinct \(s,t\) in the panel,
\[
\frac{A^H\arccos(\rho_H(s,t))}{|t-s|^H}\longrightarrow1.
\]
The integral identity \(\int_0^h\int_0^h|u-v|^Hdu\,dv=2h^{H+2}/[(H+1)(H+2)]\) now proves
\[
a_j\sim\frac{h^{H+2}}{\pi(H+1)(H+2)A^H}\sim\frac{\gamma^{H+2}}{\pi(H+1)(H+2)}j^{2\gamma-H-2}.
\]
The contribution \(a_1\) is finite and positive because the sign-disagreement probability is bounded and is positive almost everywhere off the diagonal.

**3. Summation and optimal exponent.** Summing positive terms asymptotic to \(c_{H,\gamma}j^{2\gamma-H-2}\) yields a polynomial sum if the power exceeds \(-1\), a harmonic logarithm at \(-1\), and an absolutely convergent series below \(-1\). Multiply by \(n^{-2\gamma}\) to obtain all three limits. In the supercritical regime, \(K_H(\gamma)=c_{H,\gamma}/(2\gamma-H-1)\), and direct differentiation gives
\[
\frac{d}{d\gamma}\log K_H(\gamma)
=\frac{(H+1)(2\gamma-H-2)}{\gamma(2\gamma-H-1)}.
\]
Its sign changes exactly once, from negative to positive, at \(\gamma=1+H/2\). This proves global uniqueness within the family of fixed power-graded meshes. The strict improvement over the uniform mesh follows from uniqueness since \(1+H/2>1\), with the stated ratio obtained by substitution.

## Verification

The companion standalone standard-library Python script `verify.py` recomputes double-panel Gaussian sign integrals by independent midpoint quadrature, checks the one-panel Brownian arcsine benchmark \(\mathbb E[p(1-p)]=1/8\), compares supercritical asymptotic constants numerically at multiple mesh sizes, and checks the analytic minimizer identity at several Hurst values. Its deterministic finite-resolution checks supplement, but do not replace, the uniform local-asymptotic argument and the infinite power-sum proof above. Run with `python3 verify.py`.

## Relationship to prior work

A more direct methodological predecessor is Abramowicz and Seleznjev [5], who prove exact asymptotic errors and an optimal sampling-density principle for stratified Monte Carlo quadrature of **quadratic-mean continuous** locally stationary random fields. Their regular-grid density formula formally predicts an interior-optimal density proportional to \(t^{-H/(H+2)}\) when inserted into the local sign-crossing coefficient. But the positivity indicator of fractional Brownian motion started at zero **has no quadratic-mean limit at time zero**: \(\mathbb E[\mathbf1_{\{B^H_t>0\}}^2]=1/2\) for all \(t>0\), while the indicator at zero is zero; indeed \(\mathbb E|X_t-X_0|^2=1/2\) for every \(t>0\). Moreover \(\mathbb E|X_t-X_{2t}|^2=\arccos(\rho_H(1,2))/\pi>0\) for all \(t>0\), so the sign process is not even quadratic-mean Cauchy as time tends to zero. Their Theorems 3–4 require global positive-order quadratic-mean Hölder regularity at the singular point and hence do not directly establish the present all-mesh phase classification, especially its critical logarithmic and subcritical regimes. The present exact panel scaling separately resolves those regimes. The optimal-density philosophy itself is **not claimed as new**.

Altmeyer's 2017 preprint [1] analyzes occupation-time estimation by **fixed equispaced Riemann sums** at observed process times, including fractional Brownian motion, and provides \(L^2\) upper and lower bounds for indicator integrands. It does not give the random-within-panel independent sampling design, its exact mean-square error identity, or a full power-mesh phase diagram. Altmeyer and Le Guével [2] study deterministic-time observation and optimal \(L^2\) approximation for symmetric stable Lévy processes, not this fractional Brownian randomized quadrature. Cui and Chronopoulou [3] optimize sampling for recovery of the fractional Brownian trajectory itself, a different objective. Aurzada, Döring and Pitters [4] use random times to characterize occupation-time distributions via moments and persistence, not numerical quadrature error of independent stratification. The same broad word “sampling” does not make these statements imply the present theorem. No claim of exhaustive historical novelty is made.

## Limitations

This classification is for one independent uniform draw per panel, power meshes, the sign occupation functional, and fixed \(H,\gamma\). It does not determine the globally optimal arbitrary partition, optimal estimators using all Gaussian path correlations, finite-sample exact optimizer, or minimax optimality. The rate constants are mean-square error constants, not root-mean-square error constants. The singular start at zero is essential to the phase diagram. The classical stratified Monte Carlo error-density principle is already known [5]; the contribution here is its sharp analysis for a fractional Brownian sign process that lacks quadratic-mean continuity at the origin, including critical and subcritical boundaries. Publication precedence beyond the inspected cited sources remains a risk.

## References

[1] R. Altmeyer, *Approximation of occupation time functionals*, arXiv:1706.03418, first public June 11, 2017. https://arxiv.org/abs/1706.03418

[2] R. Altmeyer and R. Le Guével, *Optimal \(L^2\)-approximation of occupation and local times for symmetric stable processes*, arXiv:2108.11632, 2021. https://arxiv.org/abs/2108.11632

[3] X. Cui and A. Chronopoulou, *Optimal Sampling for Estimation of Fractional Brownian Motion*, arXiv:2304.07661, 2023. https://arxiv.org/abs/2304.07661

[4] F. Aurzada, L. Döring and H. H. Pitters, *Occupation times and areas derived from random sampling*, arXiv:2406.09886, 2024. https://arxiv.org/abs/2406.09886

[5] K. Abramowicz and O. Seleznjev, *Stratified Monte Carlo quadrature for continuous random fields*, arXiv:1104.4920, first public April 26, 2011. https://arxiv.org/abs/1104.4920

# Sharp Gaussian ridge-risk law for two-point Anderson mixing

## Finding

A two-point scalar Anderson extrapolation can have infinite absolute first moment and infinite mean-square error under arbitrarily weak independent Gaussian evaluation noise. A symmetric ridge on its two mixing coefficients removes the singularity, with an exact \(\lambda^{-1/2}\) risk blow-up as the penalty vanishes. For nonzero midpoint error, the first nontrivial small-noise risk correction has a **unique, explicit ridge calibration** on the natural noise-variance scale.

Write \(\sigma>0\) for evaluation-noise standard deviation, \(\lambda>0\) for the ridge penalty in the centered coefficient parameterization, \(r\in(0,1)\) for the fixed-point contraction and \(d>0\) for the gap between evaluation points. Let \(\theta\in\mathbb R\) be their midpoint's signed offset from the fixed point.

For fixed \(\sigma>0\), define
\[
p_\sigma(0)=\frac{1}{2\sigma\sqrt{\pi}}
\exp\left(-\frac{(1-r)^2d^2}{4\sigma^2}\right),\qquad
m_2=(1-r)^2\theta^2+\frac{\sigma^2}{2}.
\]
Then the regularized output's expected squared error \(R_\sigma(\lambda)\) satisfies
\[
\lim_{\lambda\downarrow0}\sqrt{\lambda}\,R_\sigma(\lambda)
=\frac{\pi d^2}{2}p_\sigma(0)m_2>0.
\]
The unregularized error \(E_0\) has the sharper tail law
\[
\lim_{z\to\infty}z\,\Pr(|E_0|>z)
=2d\,p_\sigma(0)\,\mathbb E|W|>0,
\qquad W\sim N((1-r)\theta,\sigma^2/2).
\]
Thus \(\mathbb E|E_0|^p\) is finite exactly for \(0<p<1\).

If also \(\theta\ne0\), then, for each fixed \(c>0\), as \(\sigma\downarrow0\),
\[
R_\sigma(c\sigma^2)
=A\sigma^2+\sigma^4 Q(c)+o(\sigma^4),
\]
where
\[
A=\frac{d^2+4\theta^2}{2d^2(1-r)^2}
\]
and
\[
Q(c)=
\frac{r^2\theta^2c^2-[rd^2+(12r+4)\theta^2]c+
3(d^2+12\theta^2)}
{d^4(1-r)^4}.
\]
Because \(Q\) is strictly convex, its unique minimizer over \(c>0\) is
\[
\boxed{c_*=\frac{r d^2+(12r+4)\theta^2}{2r^2\theta^2}.}
\]
This states a sharp minimizer of the **fourth-order coefficient among fixed positive scale factors** \(\lambda=c\sigma^2\); it does not claim global finite-noise optimality over arbitrary \(\lambda\).

## Assumptions and scope

Fix \(x_*\in\mathbb R\), \(0<r<1\), \(d>0\), a midpoint offset \(\theta\in\mathbb R\), and \(\sigma>0\). Consider the affine fixed-point map
\[
g(x)=x_*+r(x-x_*).
\]
At the two distinct *deterministic* evaluation sites
\[
x_0=x_*+\theta-d/2,\qquad x_1=x_*+\theta+d/2,
\]
observe \(Y_j=g(x_j)+\varepsilon_j\), where \(\varepsilon_0,\varepsilon_1\) are independent \(N(0,\sigma^2)\) variables. Let \(F_j=Y_j-x_j\).

Use the centered, ridge-regularized, depth-one Anderson output
\[
Z_\lambda=w_0Y_0+w_1Y_1,\qquad
w_0=\tfrac12+\gamma_\lambda,\quad
w_1=\tfrac12-\gamma_\lambda,
\]
with \(\gamma_\lambda\) minimizing
\[
\left[(\tfrac12+\gamma)F_0+
(\tfrac12-\gamma)F_1\right]^2+\lambda\gamma^2.
\]
This is the two-coefficient least-squares form with a symmetric minimum-norm ridge: the alternative penalty \(\eta(w_0^2+w_1^2)\) differs only by a constant and has \(\lambda=2\eta\). The analysis concerns this single extrapolation from two noisy evaluations, **not** an adaptive sequence of iterates with noise-dependent sites.

## Proof

Define independent Gaussian variables
\[
U=(\varepsilon_0+\varepsilon_1)/2\sim N(0,\sigma^2/2),\quad
V=\varepsilon_1-\varepsilon_0\sim N(0,2\sigma^2)
\]
and set
\[
T=F_1-F_0=-(1-r)d+V,\qquad
W=(1-r)\theta-U.
\]
The centered residual is \((F_0+F_1)/2=-W\). The least-squares expression is \((-W-\gamma T)^2+\lambda\gamma^2\), hence its unique minimizer for \(\lambda>0\) is
\[
\gamma_\lambda=-\frac{WT}{T^2+\lambda}.
\]
Substituting \(Y_0-Y_1=-(T+d)\) gives the **exact error representation**
\[
\boxed{E_\lambda:=Z_\lambda-x_*=
\theta+W\frac{dT-\lambda}{T^2+\lambda}.}
\]
The same identity holds almost surely at \(\lambda=0\), where \(E_0=\theta+dW/T\) and \(\Pr(T=0)=0\).

Independence gives the exact one-dimensional risk formula
\[
R_\sigma(\lambda)=\theta^2+
2\theta(1-r)\theta\,\mathbb E h_\lambda(T)+
\left((1-r)^2\theta^2+\frac{\sigma^2}{2}\right)
\mathbb E h_\lambda(T)^2,\quad
h_\lambda(t)=\frac{dt-\lambda}{t^2+\lambda}.
\]
For \(\lambda>0\), \(|h_\lambda(t)|\le1+d/(2\sqrt{\lambda})\), proving finite moments of all orders.

Since \(T\) has a positive smooth normal density at zero and is independent of \(W\), the length of the interval near zero satisfying \(|\theta+dW/T|>z\) is asymptotic to \(2d|W|/z\). Integrating first conditionally on \(W\), then using its Gaussian integrability, proves the exact displayed tail coefficient. The moment threshold follows by tail integration.

For fixed \(\sigma>0\), write \(h_\lambda^2=(d^2T^2-2d\lambda T+\lambda^2)/(T^2+\lambda)^2\). The leading contribution is
\[
\int_{\mathbb R}\frac{d^2t^2}{(t^2+\lambda)^2}p_\sigma(t)\,dt
\sim \frac{\pi d^2}{2\sqrt{\lambda}}p_\sigma(0).
\]
Indeed, substitute \(t=\sqrt{\lambda}s\) and use
\(\int_{\mathbb R}s^2(1+s^2)^{-2}\,ds=\pi/2\).
The mixed and \(\lambda^2\) terms are \(O(1)\) and \(O(\sqrt\lambda)\). The linear expectation \(\mathbb E h_\lambda(T)\) is \(O(1)\), using symmetric cancellation around zero and differentiability of the Gaussian density. Multiplying the complete risk by \(\sqrt{\lambda}\) proves the sharp square-root constant.

For small-noise tuning put \(t_0=-(1-r)d\ne0\) and \(a=(1-r)\theta\). In a neighborhood of \(t_0\), \(h_\lambda(t)\) is jointly analytic in \(t\) and \(\lambda\). For \(T=t_0+\sqrt2\sigma G\) with \(G\sim N(0,1)\),
\[
\mathbb E f(T)=f(t_0)+\sigma^2f''(t_0)+
\frac{\sigma^4}{2}f^{(4)}(t_0)+o(\sigma^4)
\]
for the needed smooth local functions. With \(\lambda=c\sigma^2\), the complement of a fixed neighborhood of \(t_0\) contributes only an exponentially small term times a polynomial in \(1/\sigma\); this is \(o(\sigma^4)\) for each fixed \(c>0\).

At \(\lambda=0\), the local functions and first ridge derivative are
\[
h_0(t)=d/t,\qquad
\left.\partial_\lambda h_\lambda(t)\right|_{\lambda=0}
=-t^{-2}-dt^{-3}.
\]
The deterministic ridge bias is
\[
\theta+a h_\lambda(t_0)=
\frac{r\theta\lambda}{t_0^2+\lambda}.
\]
Applying the Gaussian expansion to the exact risk, collecting the \(\sigma^2\) and \(\sigma^4\) terms, yields the displayed \(A\) and \(Q(c)\). In particular the coefficient of \(c^2\) is \(r^2\theta^2/[d^4(1-r)^4]>0\), and differentiation gives the stated unique \(c_*\). The expansion is uniform for \(c\) in any fixed compact subset of \((0,\infty)\).

## Verification

`verify.py` separately evaluates the two-residual ridge minimization, proves the error identity and Taylor coefficients symbolically, checks 120 direct update identities with separately generated noises, compares one-dimensional Gaussian quadrature methods, and tests both the heavy-tail constant and the fourth-order scaling. Its recorded execution completed 155 assertions.

For \(r=1/2\) and \(\theta=d=1\), the sharp coefficient is \(c_*=21\), and
\[
R_\sigma(21\sigma^2)=10\sigma^2-1140\sigma^4+o(\sigma^4).
\]
At \(\sigma=0.02\), direct Gaussian integration gives \(R_\sigma(0.0084)\approx0.00382631\), compared with \(0.00402400\) at \(\lambda=0.0012\). These numbers illustrate finite-noise behavior, but the proof of the asymptotic classification is analytic.

Reproduce with Python 3, NumPy, SciPy, and SymPy:
```
python verify.py
```
The Gaussian tail and symbolic constants are claims about exact probability laws; no finite set of calculations is used as a substitute for proof.

## Relationship to prior work

The general Anderson mixing and regularized nonlinear acceleration principles predate this result. Scieur, d'Aspremont and Bach (2017) analyze regularized extrapolation of noisy optimization iterates and give broad noise-dependent stability bounds; their two-coefficient minimum-norm ridge leads to the same symmetric coefficient penalty after reparameterization, but their estimates do not give the one-step exact Gaussian risk, moment threshold, square-root blow-up coefficient or fourth-order optimal calibration in this fixed-evaluation model.

Toth et al. (2017) analyze Anderson acceleration with inaccurate function evaluations under bounded coefficient hypotheses and finite-horizon probabilistic control, rather than this unconditional one-step moment classification. Wei, Bao and Liu (2021) introduce regularization and damping in stochastic Anderson mixing, but analyze convergence of a different adaptive algorithm. Pollock and Rebholz (2022) control conditioning by filtering instead of deriving the Gaussian one-step risk.

The elementary fact that ratios of normal variables can have Cauchy-type tails is established mathematics, not independently claimed as a novelty. What is assessed here is the explicit risk identity for the stated regularized two-point Anderson update, the exact singular coefficient and the fourth-order parameter calibration in its small-noise limit.

## Limitations

The evaluation sites are fixed rather than generated by the noisy iteration, and the errors are independent, identically distributed Gaussians. The claim does not cover higher-dimensional nonlinear fixed-point maps, correlated or bounded noise, multi-step stability, adaptive history selection, or global optimality of the ridge parameter at finite \(\sigma\). The fourth-order coefficient optimum applies only to \(\lambda=c\sigma^2\) with \(c>0\) fixed and \(\theta\ne0\). Unindexed specialist precedents or equivalent Gaussian-ratio risk calculations remain possible.

## References

- D. Scieur, A. d'Aspremont and F. Bach, *Nonlinear Acceleration of Stochastic Algorithms* (first arXiv submission 22 June 2017), https://arxiv.org/abs/1706.07270.
- A. Toth, J. A. Ellis, T. Evans, S. Hamilton, C. T. Kelley, R. Pawlowski and S. Slattery, *Local Improvement Results for Anderson Acceleration with Inaccurate Function Evaluations* (2017), https://doi.org/10.1137/16M1080677; open manuscript https://www.osti.gov/servlets/purl/1408509.
- F. Wei, C. Bao and Y. Liu, *Stochastic Anderson Mixing for Nonconvex Stochastic Optimization* (first arXiv submission 4 October 2021), https://arxiv.org/abs/2110.01543.
- S. Pollock and L. G. Rebholz, *Filtering for Anderson Acceleration* (first arXiv submission 23 November 2022), https://arxiv.org/abs/2211.12953.

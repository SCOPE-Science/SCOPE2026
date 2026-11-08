# Sharp Euler mean-square stability and covariance bias for reversible-noise Gaussian Langevin sampling

## Finding

Consider the two-dimensional reversible Stratonovich perturbation of an anisotropic Gaussian Langevin process and **Euler–Maruyama applied to its Itô formulation**. The exact boundary between existence and failure of a finite-second-moment stationary law is a closed radical depending only on the target anisotropy and perturbation strength. Inside that boundary the stationary numerical covariance has a closed form and **strictly exceeds the desired Gaussian covariance**. In the strong-perturbation limit the admissible step shrinks as the inverse fourth power of the Stratonovich amplitude.

Put \(S=\operatorname{diag}(1,\lambda)\), \(\lambda>0\), \(J=\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\), and \(\delta\ge0\). Let \(\beta\) be scalar Brownian motion, \(W\) an independent planar Brownian motion, and
\[
 dX_t=-SX_t\,dt+\sqrt2\,\delta JS X_t\circ d\beta_t+\sqrt2\,dW_t.
\]
Its invariant probability is centered Gaussian with covariance \(S^{-1}\). In Itô form the drift is \(-BX_t\), where \(B=\operatorname{diag}(1+a,\lambda+a)\) and \(a=\lambda\delta^2\). Let \(h>0\), and discretize the **Itô equation** by independent standard normal variables \(\xi_k\in\mathbb R\), \(\eta_k\in\mathbb R^2\):
\[
 X_{k+1}=(I-hB)X_k+\sqrt{2h}\,\delta JS X_k\xi_k+\sqrt{2h}\,\eta_k.
\]
Define \(A=1+a\), \(D=\lambda+a\), and the sharp threshold
\[
 \boxed{\displaystyle h_*(\lambda,a)=\frac{A+D-\sqrt{(A-D)^2+4a^2}}{AD}>0.}
\]
For **every** \(\lambda>0\), \(\delta\ge0\), \(h>0\), the following dichotomy holds:

1. If \(0<h<h_*(\lambda,a)\), the chain has a **unique invariant law with finite second moment**, and laws with finite second moments converge toward it in \(W_2\). Its mean is zero. In the scaled coordinates \(Y=S^{1/2}X\), its covariance is \(\operatorname{diag}(u_h,v_h)\), where, with
\[
 \Delta(h)=AD(2-Ah)(2-Dh)-4a^2,
\]
\[
 \boxed{\displaystyle
 u_h=\frac{2[D(2-Dh)+2a\lambda]}{\Delta(h)},\qquad
 v_h=\frac{2[2a+\lambda A(2-Ah)]}{\Delta(h)}.}
\]
In particular \(u_h>1\) and \(v_h>1\), so the numerical stationary covariance is strictly larger in positive-definite Loewner order than the target \(S^{-1}\).
2. If \(h\ge h_*(\lambda,a)\), **no invariant probability with a finite second moment exists**. Starting at \(X_0=0\), the mean-square norm diverges: at the boundary it grows at least linearly; above it it grows exponentially.

The no-perturbation case \(a=0\) is included, giving \(h_*(\lambda,0)=2/\max(1,\lambda)\). For fixed \(\lambda>0\) as \(\delta\to\infty\),
\[
 \boxed{\displaystyle h_*(\lambda,\lambda\delta^2)\sim\frac{1+\lambda}{\lambda^2\delta^4}.}
\]
At the *continuous-time spectral-gap-optimal scaling* \(\delta=\lambda^{-1/2}\) (so \(a=1\)), the boundary is
\[
 \boxed{\displaystyle h_*(\lambda,1)=\frac{\lambda+3-\sqrt{\lambda^2-2\lambda+5}}{2(1+\lambda)},\qquad
 \lim_{\lambda\downarrow0}h_*(\lambda,1)=\frac{3-\sqrt5}{2}.}
\]
For \(0<\lambda\le1\), steps \(0<h<(3-\sqrt5)/2\) enjoy a uniform second-moment contraction margin, whereas any fixed larger step violates mean-square stability for sufficiently small positive \(\lambda\). At the endpoint every \(0<\lambda\le1\) remains stable individually, but no uniform margin survives. In the same anisotropic limit and for fixed \(0<h<(3-\sqrt5)/2\), \(u_h\to(2-h)/[2(1-3h+h^2)]\) and \(v_h\to1/(1-3h+h^2)\).

## Assumptions and scope

All variables are real. Gaussian innovations are independent across steps and between the scalar multiplicative and two-dimensional additive terms; they are independent of the initial state. The step is fixed and strictly positive; all formulas refer to exact arithmetic. The target \(S^{-1}\) is the invariant covariance of the **continuous-time Stratonovich SDE**, not of the discretization. Finite-second-moment invariance and mean-square numerical stability, not almost-sure Lyapunov exponents, are classified. The invariant numerical law is not asserted to be Gaussian.

## Proof

**1. Exact normalization and second-moment transfer.** Let \(Y_k=S^{1/2}X_k\). Since \(S^{1/2}JS^{1/2}=\sqrt\lambda J\), the Euler update is
\[
 Y_{k+1}=\begin{pmatrix}\alpha&0\\0&\beta\end{pmatrix}Y_k+\sqrt{2ha}\,JY_k\xi_k+\sqrt{2h}\,S^{1/2}\eta_k,
 \quad \alpha=1-hA,\ \beta=1-hD.
\]
Thus, writing \(u_k=\mathbb E[Y_{1,k}^2]\), \(v_k=\mathbb E[Y_{2,k}^2]\), and \(c_k=\mathbb E[Y_{1,k}Y_{2,k}]\), even without centering,
\[
 \binom{u_{k+1}}{v_{k+1}}=
 T\binom{u_k}{v_k}+2h\binom{1}{\lambda},\qquad
 T=\begin{pmatrix}\alpha^2&2ha\\2ha&\beta^2\end{pmatrix},\qquad
 c_{k+1}=(\alpha\beta-2ha)c_k.
\]
The nonnegative symmetric matrix \(T\) has spectral radius \(\rho(T)\) equal to its largest eigenvalue. The other second-moment multiplier satisfies
\[
 |\alpha\beta-2ha|\le |\alpha\beta|+2ha\le\frac{\alpha^2+\beta^2}{2}+2ha\le\rho(T),
\]
using the Rayleigh quotient of \(T\) against \((1,1)^\mathsf T\). Hence stability of the complete covariance dynamics is equivalent to \(\rho(T)<1\).

**2. Exact stability boundary.** If \(\rho(T)<1\), then \(\alpha^2<1\) and \(\beta^2<1\); necessarily \(0<h<\min(2/A,2/D)\). In this interval the \(2\times2\) matrix \(I-T\) is positive definite if and only if its determinant is positive. Direct computation gives
\[
 \det(I-T)=h^2\left[AD(2-Ah)(2-Dh)-4a^2\right]=h^2\Delta(h).
\]
As \(h\) increases from zero to \(\min(2/A,2/D)\), \(\Delta\) decreases strictly from \(4(AD-a^2)>0\) to a nonpositive value (strictly negative when \(a>0\)). It therefore has a unique boundary zero in that interval or at its endpoint. Solving its quadratic equation produces the stated smaller radical root \(h_*\). Conversely, for \(0<h<h_*\) both diagonal entries of \(I-T\) and its determinant are positive, hence \(\rho(T)<1\). At \(h=h_*\), \(\rho(T)=1\); no larger step can restore \(\rho(T)<1\), since any such step below the diagonal Euler thresholds has \(\Delta\le0\), while a step above either threshold has a diagonal entry of \(T\) at least one. This also handles \(a=0\) directly.

**3. Existence, covariance and strict bias.** In the stable interval, an infinite-backward affine series converges in \(L^2\), or equivalently synchronous couplings contract sufficiently many steps in the Wasserstein metric \(W_2\). This constructs the unique finite-second-moment invariant law and proves convergence from all finite-second-moment initial laws. Its mean is zero because the deterministic mean multiplier has modulus strictly below one in both components. Since \(|\alpha\beta-2ha|<1\), its off-diagonal covariance vanishes. Solving the diagonal fixed-point equation by the displayed inverse of \(I-T\) yields \(u_h,v_h\) exactly. The continuous target identity covariance in \(Y\) coordinates has one-step defect
\[
 T\binom11+2h\binom1\lambda-\binom11
 =h^2\binom{A^2}{D^2}\succ0.
\]
Consequently
\[
 \binom{u_h-1}{v_h-1}=(I-T)^{-1}h^2\binom{A^2}{D^2}
 =h^2\sum_{j=0}^\infty T^j\binom{A^2}{D^2},
\]
which is strictly positive componentwise. Conjugation by \(S^{-1/2}\) gives the strict Loewner covariance inflation for \(X\).

**4. Failure at and above the boundary.** From zero initial state the nonnegative diagonal second moments are
\[
 \binom{u_k}{v_k}=2h\sum_{j=0}^{k-1}T^j\binom1\lambda.
\]
The Perron eigenvector of \(T\) can be chosen nonnegative, and has strictly positive scalar product with the forcing vector. If \(\rho(T)=1\), the projected sum grows linearly; if \(\rho(T)>1\), it grows exponentially. The trace therefore diverges. In either regime, a finite-second-moment invariant law would have nonnegative diagonal moments solving \(z=Tz+2h(1,\lambda)^\mathsf T\), impossible after left-multiplication by that same Perron eigenvector. This excludes *every* finite-second-moment invariant distribution, not only a Gaussian candidate.

**5. Singular parameter limits.** With \(a=\lambda\delta^2\), expand the radical as \(a\to\infty\) to obtain \(h_*\sim(1+\lambda)/a^2\). At \(a=1\), substitute into the exact root. For \(0<\lambda\le1\) and \(h<(3-\sqrt5)/2\), the entries of \(T\) have fixed nonnegative \(\alpha\) and \(\beta\), and increasing \(\lambda\) decreases the \(T_{22}\) entry while keeping other entries unchanged. The Perron root is therefore greatest in the limit \(\lambda\downarrow0\), which proves the uniform stability margin and its sharpness. Substitution and passage to the limit in \(u_h,v_h\) proves the displayed stationary covariance limits. At \(h=(3-\sqrt5)/2\), each \(0<\lambda\le1\) has smaller Perron root than the limiting \(\lambda=0\) transfer matrix, while the uniform spectral gap vanishes.

## Verification

The standalone Python file `verify.py` rederives the exact rational second-moment transfer, the determinant factorization and the stationary covariance identity for a range of rational inputs. It compares the sharp root with direct Perron eigenvalues on either side, tests the unperturbed and isotropic boundaries and checks the strong-noise and anisotropic limits numerically. It uses only the Python standard library. Execute `python verify.py` from this directory. The output of this test is a finite consistency check; the analytic argument above is the proof of the universal theorem.

## Relationship to prior work

Louis, Pavliotis and Vilmart (2026, arXiv:2610.03191), equation (17), develop this same Itô SDE, prove a continuous-time \(L^2\) spectral-gap acceleration and use an Euler–Maruyama discretization for two-dimensional Gaussian experiments (§6.1). Their §7 identifies rigorous convergence analysis of the discretized sampler as an open direction; the exact \(h_*\), invariant Euler covariance and fourth-power amplitude threshold are not stated there. Abdulle, Pavliotis and Vilmart (2019, arXiv:1903.03024) establish reversible perturbations and simulate small Euler steps, but do not give this discretization boundary. Buckwar and Sickenberger (2009, arXiv:0912.1968) provide generic scalar linear-noise mean-square stability tests; the present skew-coupled two-dimensional drift/noise matrices are not simultaneously reducible to their scalar test. The related Buckwar–Kelly (2010) stochastic-systems stability paper is relevant generic prior art; its full text could not be checked, so an older structural reduction remains a priority risk. The theorem is a model-specific exact numerical parameter classification, not a claim to invent the second-moment spectral-radius method.

## Limitations

The assertion concerns a two-dimensional quadratic target, the **Itô Euler–Maruyama step**, Gaussian iid driving increments and a single reversible noise direction. It does not prove step size robustness for nonlinear or higher-dimensional perturbations, weak convergence to the exact target distribution, almost-sure instability at the second-moment threshold, or superiority in computational cost. The invariant numerical law need not be Gaussian. The result has not undergone independent mathematical audit. Generic earlier matrix-stability criteria may imply parts of the argument without already stating this explicit application.

## References

- G. Louis, G. A. Pavliotis and G. Vilmart, *Reversible Stratonovich perturbations for accelerating convergence to equilibrium of Langevin dynamics* (2026), arXiv:2610.03191, https://arxiv.org/abs/2610.03191, first public 2026-10-02; especially (17), Theorem 2, §§6–7.
- A. Abdulle, G. A. Pavliotis and G. Vilmart, *Accelerated convergence to equilibrium and reduced asymptotic variance for Langevin dynamics using Stratonovich perturbations* (2019), arXiv:1903.03024, https://arxiv.org/abs/1903.03024.
- E. Buckwar and T. Sickenberger, *A comparative linear mean-square stability analysis of Maruyama- and Milstein-type methods* (2011), preprint arXiv:0912.1968, https://arxiv.org/abs/0912.1968.
- E. Buckwar and C. Kelly, *Towards a systematic linear stability analysis of numerical methods for systems of stochastic differential equations*, SIAM J. Numer. Anal. 48 (2010), 298–321, https://doi.org/10.1137/090771843.

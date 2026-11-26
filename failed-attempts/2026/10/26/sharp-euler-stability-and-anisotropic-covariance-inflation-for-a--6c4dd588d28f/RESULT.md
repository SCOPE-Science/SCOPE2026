# Sharp Euler stability and anisotropic covariance inflation for a reversible Stratonovich Langevin sampler

## Finding

For the two-dimensional Gaussian Langevin dynamics with the rate-preserving critical Stratonovich perturbation of Louis, Pavliotis and Vilmart [1], the Euler–Maruyama method has an **exact finite-step mean-square stability frontier**, and its finite-second-moment stationary covariance has an **exactly quantified anisotropic inflation**.

Fix \(0<\lambda\leq 1\), set \(q=1+\lambda\), and define
\[
F_\lambda(h)=q(1-h)(2-qh)-1,\qquad
h_*(\lambda)=\frac{q+2-\sqrt{q^2-4q+8}}{2q}.
\]
For every \(h>0\), the homogeneous stochastic Euler update is asymptotically mean-square stable **if and only if** \(0<h<h_*(\lambda)\). The inhomogeneous Euler sampler admits an invariant probability distribution having finite second moment exactly on this open interval, and that law is unique among probability distributions with finite second moment. The threshold increases with \(\lambda\), with
\[
\lim_{\lambda\downarrow0}h_*(\lambda)=\frac{3-\sqrt5}{2},
\qquad h_*(1)=\frac12.
\]
In its stable range the invariant covariance is diagonal, with variances \(p=\mathbb E[X^2]\) and \(s=\mathbb E[Y^2]\) given by
\[
p=\frac{q(1-qh/2)+\lambda}{F_\lambda(h)},\qquad
\lambda s=\frac{1+2\lambda(1-h)}{F_\lambda(h)}.
\]
In particular,
\[
\boxed{\lambda\mathbb E[Y^2]-\mathbb E[X^2]
=\frac{h(1-\lambda)^2}{2F_\lambda(h)}.}
\]
Both componentwise variances exceed their respective target values \(1\) and \(1/\lambda\) for every positive stable step. If \(0<\lambda<1\), the relative excess is strictly greater in the second coordinate. As \(h\uparrow h_*(\lambda)\), both variances diverge. For \(h\in[h_*(\lambda),1)\), the **mean** update remains asymptotically stable but the **second moment** from zero initialization diverges (linearly at the boundary and geometrically above it).

## Assumptions and scope

Write \(U=(X,Y)^\mathsf T\). The original Itô process from [1, Section 3.1, Equation (17)] with \(S=\operatorname{diag}(1,\lambda)\), skew matrix \(J=\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\), and \(\delta=\lambda^{-1/2}\) is
\[
\mathrm dU_t=-\begin{pmatrix}2&0\\0&1+\lambda\end{pmatrix}U_t\,\mathrm dt
+\sqrt2\begin{pmatrix}0&\sqrt\lambda\\-1/\sqrt\lambda&0\end{pmatrix}U_t\,\mathrm d\beta_t
+\sqrt2\,\mathrm dW_t.
\]
Here \(\beta\) and the two coordinates of \(W\) are independent standard Brownian motions. The exact continuous-time invariant law has covariance \(\operatorname{diag}(1,1/\lambda)\) [1]; we do not assume the numerical invariant distribution is Gaussian. The **Itô** form is discretized; applying a naive Euler rule to the uncorrected Stratonovich equation would be a different scheme.

Let \(\zeta_n\) be independent standard real Gaussians and \(\xi_n\) independent standard two-dimensional Gaussians, mutually independent across all indices. For \(h>0\), define
\[
U_{n+1}=(D_h+\sqrt{2h}\,B_\lambda\zeta_n)U_n+\sqrt{2h}\,\xi_n,
\quad D_h=\operatorname{diag}(1-2h,1-qh),\quad
B_\lambda=\begin{pmatrix}0&\sqrt\lambda\\-1/\sqrt\lambda&0\end{pmatrix}.
\]
Asymptotic mean-square stability refers to this **homogeneous** update with \(\xi_n=0\), requiring \(\mathbb E\|U_n\|_2^2\to0\) for every square-integrable initial state independent of future noise. A finite-second-moment invariant law means an invariant probability with \(\mathbb E\|U\|_2^2<\infty\). The unforced and additive-noise statements are kept distinct.

## Proof

**1. The complete second-moment operator.** Let \(P_n=\mathbb E[U_nU_n^\mathsf T]\). Independence and centered increments give exactly
\[
P_{n+1}=\mathcal T_h(P_n)+2hI,
\quad \mathcal T_h(P)=D_hPD_h^\mathsf T+2hB_\lambda PB_\lambda^\mathsf T.
\]
Write \(P=\begin{psmallmatrix}p&r\\r&s\end{psmallmatrix}\), \(u=1-2h\), and \(v=1-qh\). The diagonal components obey
\[
\begin{pmatrix}p'\\s'\end{pmatrix}
=\begin{pmatrix}u^2&2h\lambda\\2h/\lambda&v^2\end{pmatrix}
\begin{pmatrix}p\\s\end{pmatrix}+2h\begin{pmatrix}1\\1\end{pmatrix},
\qquad r'=(uv-2h)r.
\]
Rescaling the second diagonal coordinate to \(t=\lambda s\), the homogeneous diagonal matrix is similar to the symmetric, strictly positive-off-diagonal matrix
\[
K_h=\begin{pmatrix}u^2&2h\\2h&v^2\end{pmatrix}.
\]
Moreover,
\[
|uv-2h|\leq |uv|+2h\leq\frac{u^2+v^2}{2}+2h\leq\rho(K_h).
\]
Thus the full three-dimensional symmetric-matrix moment operator has spectral radius \(\rho(K_h)\); the off-diagonal mode cannot determine a stricter threshold. Because the diagonal moment cone has an interior Perron eigenvector, the homogeneous mean-square dynamics decay for all square-integrable initial states exactly when \(\rho(K_h)<1\).

**2. Exact frontier.** For \(0<h<1\), the leading principal minor of \(I-K_h\) is \(1-u^2=4h(1-h)>0\). Its determinant is
\[
\begin{aligned}
\det(I-K_h)
&=(1-u^2)(1-v^2)-4h^2\\
&=4h^2\big[(1-h)q(2-qh)-1\big]\\
&=4h^2F_\lambda(h).
\end{aligned}
\]
The matrix \(K_h\) is real symmetric and nonnegative. Hence \(\rho(K_h)<1\) exactly when \(I-K_h\) is positive definite, which on \(0<h<1\) is equivalent to \(F_\lambda(h)>0\). On this interval,
\[
F_\lambda'(h)=-q(q+2-2qh)<0,
\quad F_\lambda(0)=1+2\lambda>0,
\quad F_\lambda(1)=-1.
\]
There is precisely one positive root in \((0,1)\). Solving the quadratic and selecting its smaller root gives the asserted \(h_*(\lambda)\). If \(h\geq1\), the diagonal entry \(u^2=(1-2h)^2\geq1\), and the strictly positive off-diagonal entries make \(\rho(K_h)>1\); no further stability interval can occur. At the threshold the Perron eigenvalue equals one; immediately above and thereafter it exceeds one.

The equation defining the root also shows \(h_*(\lambda)\leq1/2\) (with equality at \(\lambda=1\)); substituting \(q=1\) and \(q=2\) gives the displayed limiting and endpoint values. For \(0<\lambda<1\), \(\partial_q F_\lambda(h)=(1-h)(2-2qh)>0\) at its root, whereas \(\partial_hF_\lambda(h)<0\), so implicit differentiation proves strict increase in \(\lambda\).

**3. Invariant covariance and failure beyond the frontier.** In the stable range, \(\mathcal T_h\) contracts geometrically in a suitable equivalent norm. The affine recursion is an iterated independent random affine map with bounded one-step second moment; its bi-infinite backward series therefore converges in \(L^2\), providing a stationary solution. If two invariant square-integrable solutions are coupled using the same future innovations, their difference follows the homogeneous scheme, so contraction implies equality of invariant laws. The stationary second moment solves
\[
(1-u^2)p-2h\lambda s=2h,
\quad(1-v^2)s-2hp/\lambda=2h,
\quad (1-uv+2h)r=0.
\]
The last factor does not vanish in the stable region, so \(r=0\). Solving the two remaining equations and cancelling \(4h^2F_\lambda(h)\) gives exactly the displayed expressions for \(p\) and \(\lambda s\).

For \(h\geq h_*(\lambda)\), suppose a finite-second-moment stationary law existed, with second-moment vector \(w\geq0\). Its diagonal equation would be \(w=M_hw+2h(1,1)^\mathsf T\), where \(M_h\) is positive and similar to \(K_h\). Multiplication by the strictly positive left Perron eigenvector of \(M_h\) yields \((1-\rho(K_h))\ell^\mathsf Tw=2h\ell^\mathsf T(1,1)^\mathsf T>0\), impossible when \(\rho(K_h)\geq1\). Starting instead at \(U_0=0\), iteration of the positive diagonal moment recurrence shows linear growth at \(\rho=1\) and geometric growth at \(\rho>1\).

**4. Anisotropic bias and mean-versus-moment distinction.** Subtracting the two displayed numerator formulas yields
\[
\lambda s-p=\frac{\big[1+2\lambda(1-h)\big]-\big[q(1-qh/2)+\lambda\big]}{F_\lambda(h)}
=\frac{h(1-\lambda)^2}{2F_\lambda(h)}.
\]
All factors in the denominator are positive in the stable range. Directly subtracting \(F_\lambda(h)\) from the numerators yields
\[
p-1=\frac{qh(q/2+2-qh)}{F_\lambda(h)}>0,
\quad\lambda s-1=\frac{h\big[q(q+2)-2\lambda-q^2h\big]}{F_\lambda(h)}>0,
\]
since \(0<h<h_*(\lambda)\leq1/2\) and \(1<q\leq2\). Their numerators remain strictly positive as \(h\uparrow h_*\), while \(F_\lambda(h)\downarrow0\), proving divergence. Finally the deterministic mean map \(D_h\) is stable for every \(0<h<1\), because its eigenvalues lie strictly between \(-1\) and \(1\) there. Hence \(h_*\leq h<1\) furnishes a nonempty mean-stable, mean-square-unstable window, including the critical linearly growing case.

## Verification

The standalone `verify.py` checks 1,500 randomly generated exact rational parameter pairs against the two stationary moment equations, the anisotropic difference identity, and the strict overdispersion bounds. It separately constructs the full three-dimensional symmetric covariance update (not merely the diagonal restriction) and numerically checks the threshold and closed-form covariance in 72 parameter/step configurations. Run with Python 3, NumPy, and `python verify.py`; `verification-output.txt` contains the actual output. The computations corroborate the formulas but are not used as infinite-domain proofs; the four analytic steps above establish every stated parameter range and boundary.

## Relationship to prior work

Louis, Pavliotis and Vilmart [1, Section 3.1, Theorem 2] establish accelerated **continuous-time** convergence for this critically scaled reversible perturbation. Their Section 4.2 derives the continuous-time second-moment dynamics; Section 6.1 uses Euler–Maruyama at a fixed small step, and Section 7 explicitly leaves rigorous analysis of discretized perturbed Langevin dynamics as a question. The new statement concerns the discrete second-moment operator, its **sharp global timestep frontier**, exact invariant covariance and normalized anisotropy, none of which are asserted in those inspected sections or appendices. The foundational earlier paper [2] gives the continuous-time Stratonovich sampler and asymptotic-variance properties, not this exact discrete boundary. Lang, Petersson and Thalhammer [3] give a general tensor-product mean-square stability framework for SDE discretizations; its criterion is compatible with the moment-operator method here, but does not evaluate this particular model's sharp root or stationary bias. Other published studies of harmonic Langevin integrators concern different methods and update matrices. An independently discovered equivalent expression in general stochastic-recursion literature cannot be excluded.

## Limitations

This is a statement about the specified two-dimensional Gaussian target with \(0<\lambda\leq1\), the specific critical perturbation \(\delta=\lambda^{-1/2}\), and explicit Euler–Maruyama applied to the **Itô** form. It proves second-moment stability and finite-second-moment invariant-law statements, not convergence in total variation, Gaussianity of the numerical invariant law, higher moment bounds, multidimensional analogues, or the behavior of splitting, implicit, or Metropolized schemes. Beyond the threshold there may still exist invariant laws without finite second moments; none are ruled out here. Numerical checks are finite corroboration, not a substitute for proof. Priority remains subject to independent literature verification, particularly against equivalent general noncommuting linear-SDE stability formulas.

## References

1. G. Louis, G. A. Pavliotis, and G. Vilmart, *Reversible Stratonovich perturbations for accelerating convergence to equilibrium of Langevin dynamics*, arXiv:2610.03191, first publicly posted 2026-10-02. https://arxiv.org/abs/2610.03191 . Sections 3.1, 4.2, 6.1, 7 and appendices inspected from the full accessible arXiv text.
2. A. Abdulle, G. A. Pavliotis, and G. Vilmart, *Accelerated convergence to equilibrium and reduced asymptotic variance for Langevin dynamics using Stratonovich perturbations*, arXiv:1903.03024 (2019). https://arxiv.org/abs/1903.03024 . All six PDF pages inspected.
3. A. Lang, A. Petersson, and A. Thalhammer, *Mean-square stability analysis of approximations of stochastic differential equations in infinite dimensions*, BIT Numerical Mathematics **57** (2017), 963–990; DOI:10.1007/s10543-017-0684-7. https://link.springer.com/article/10.1007/s10543-017-0684-7 . Abstract, stability definitions, operator criterion, and relevant introduction inspected.

# A sharp reentrant stationary-noise transition for semi-implicit NAG-GS

## Finding

Consider the fixed-damping NAG-GS update on an SPD quadratic with isotropic Brownian velocity noise, specified below. Write \(t=\lambda/\mu\ge1\) for a Hessian eigenvalue divided by the smallest eigenvalue, \(a>0\) for the dimensionless step, and \(\sigma>0\) for the velocity-noise amplitude. In its Schur-stable domain the stationary variance of the position coordinate in this mode is exactly

\[
V_t(a)=\frac{\sigma^2(a^2+2a+2)}{t(a+2)[4+4a+(2-t)a^2]}.
\]

There is a **sharp curvature-ratio transition**
\[
t_{\mathrm c}=\frac{4+12\sqrt3}{13}=1.906508437755886\ldots.
\]
For \(1\le t\le t_{\mathrm c}\), \(V_t\) is strictly decreasing on all positive steps (at equality its derivative vanishes at one point without changing sign). For \(t_{\mathrm c}<t<2\), despite deterministic stability at *every* positive step, the curve decreases, increases, and decreases again, with exactly one strict local minimum and one strict local maximum. For \(t=2\), it has one global minimum, at \(a=\sqrt2\), with value \(\sigma^2(\sqrt2-1)/4\). For \(t>2\), it has one global minimum on its finite stable interval and diverges at the upper Schur boundary.

This mode-level transition can survive summation over all modes of a true strongly convex problem: for \(H=\operatorname{diag}(1,99/50,\ldots,99/50)\) with ten copies of \(99/50\), unit noise amplitude, and damping \(\gamma=\mu=1\), the entire iteration is Schur stable for **every** \(a>0\), yet its total stationary position mean-square error \(J(a)=\mathbb E\|x_\infty\|_2^2\) satisfies \(J'(1)<0\), \(J'(4)>0\), and \(J'(20)<0\). Thus its stationary error is not monotone in the step even though deterministic stability is unrestricted.

## Assumptions and scope

Let \(H=H^\mathsf T\succ0\) be an \(n\times n\) real matrix, \(\mu=\lambda_{\min}(H)>0\), and \(f(x)=\tfrac12x^\mathsf THx\). Fix constant \(a>0\), constant NAG-GS damping \(\gamma=\mu\), and \(\sigma>0\). With independent increments \(\Delta W_k\sim N(0,aI_n)\), independent of the initial state, set

\[
\begin{aligned}
x_{k+1}&=\frac{x_k+a v_k}{1+a},\\
v_{k+1}&=\frac{v_k+a(I-H/\mu)x_{k+1}}{1+a}+\frac{\sigma\Delta W_k}{1+a}.
\end{aligned}
\]

This is the particular **Brownian-increment velocity-noise discretization**, not an arbitrary stochastic-gradient oracle. For a mode \(t=\lambda/\mu\), put \(\Delta_t(a)=4+4a+(2-t)a^2\). The claimed stationary law exists uniquely when every mode satisfies \(\Delta_t(a)>0\). For \(t\le2\), all positive steps are admissible. For \(t>2\), the admissible range is \(0<a<a_{\rm stab}(t)\), where

\[
a_{\rm stab}(t)=\frac{2(1+\sqrt{t-1})}{t-2}=\frac2{\sqrt{t-1}-1}.
\]

All formulas refer to the limit as \(k\to\infty\) from any deterministic finite initial state, not to finite-step errors, objective function accuracy, or nonquadratic problems. Orthogonal diagonalization of \(H\) makes the stationary covariance of the positions diagonal in the Hessian eigenbasis.

## Proof

**Step 1: the scalar recurrence and stable domain.** On an eigenmode \(t\), write the scalar positions as \(X_k\) and velocities as \(Y_k\). Eliminate \(Y_k\) from the two state updates. The resulting AR(2) recurrence is

\[
X_{k+2}=\phi X_{k+1}-bX_k+\eta_k,
\qquad b=(1+a)^{-2},\quad
\phi=\frac{2(1+a)+a^2(1-t)}{(1+a)^2},
\quad\mathbb E\eta_k^2=\frac{a^3\sigma^2}{(1+a)^4}.
\]

The innovations \(\eta_k=a\sigma\Delta W_k/(1+a)^2\) are independent centered Gaussians. Its characteristic polynomial is \(z^2-\phi z+b\). Since \(0<b<1\), the Jury conditions reduce to \(1+b-\phi>0\) and \(1+b+\phi>0\). The first is \(a^2t/(1+a)^2>0\); the second is \(\Delta_t(a)/(1+a)^2>0\). This proves the stated domain and the existence and uniqueness of a stationary centered Gaussian state in it. At a finite Schur boundary the AR(2) is not stable, so the stationary formula below does not apply.

**Step 2: exact stationary variance.** Let \(r_j=\mathbb E(X_{k+j}X_k)\) in stationarity. The Yule–Walker relations give \(r_1=\phi r_0/(1+b)\) and \(r_2=\phi r_1-br_0\). Inserting these into \(r_0=\phi r_1-br_2+\mathbb E\eta_k^2\) yields

\[
r_0=\frac{\mathbb E\eta_k^2(1+b)}{(1-b)((1+b)^2-\phi^2)}
=\frac{\sigma^2(a^2+2a+2)}{t(a+2)\Delta_t(a)}=V_t(a).
\]

The denominators are positive throughout the stable domain. The full position mean-square error is \(J(a)=\sum_{i=1}^n V_{\lambda_i/\mu}(a)\) because the stationary mean is zero, eigenmodes decouple under isotropic innovations, and the eigenvectors form an orthonormal basis.

**Step 3: sharp turning-point classification.** Differentiation with respect to \(a\) gives

\[
V_t'(a)=\frac{\sigma^2 F_t(a)}{t(a+2)^2\Delta_t(a)^2},\qquad
F_t(a)=(t-2)a^4+4(t-2)a^3+(10t-16)a^2+(8t-16)a-8.
\]

For \(a>0\), factor its sign as

\[
F_t(a)=B(a)[t-T(a)],\quad B(a)=a^4+4a^3+10a^2+8a>0,
\]

\[
T(a)=\frac{2(a^4+4a^3+8a^2+8a+4)}{a^4+4a^3+10a^2+8a}.
\]

A direct factorization proves

\[
T'(a)=\frac{8(a+2)(a^2-2a-2)(a^2+2a+2)}{a^2(a^3+4a^2+10a+8)^2}.
\]

Thus \(T\) decreases strictly from \(+\infty\) to its unique minimum at \(a_0=1+\sqrt3\), then increases strictly toward \(2\) from below. Substitution gives \(T(a_0)=t_{\rm c}\). It follows, by the sign of \(t-T(a)\), that \(1\le t<t_{\rm c}\) has no stationary step; \(t=t_{\rm c}\) has exactly one horizontal tangent without a sign change; and \(t_{\rm c}<t<2\) has exactly two stationary steps, a first local minimum and a second local maximum. For \(t=2\), \(F_2(a)=4(a^2-2)\) and the unique minimum is \(a=\sqrt2\). For \(t>2\), the stable interval ends at the zero of \(\Delta_t\), where \(V_t\to+\infty\); the unique solution of \(T(a)=t\) on the decreasing branch gives its strict global minimum, since \(T(a)<2<t\) on the increasing branch and no second root exists.

**Step 4: a fully stable multidimensional reversal.** Take \(\sigma^2=1\) and the eleven eigenvalue ratios \(1\) and ten copies of \(99/50\). Every ratio is strictly less than \(2\), hence \(J(a)=V_1(a)+10V_{99/50}(a)\) is well defined for every \(a>0\). Substituting the rational points into the exact derivative of Step 3 gives

\[
J'(1)=-\frac{10881433}{143273691}<0,\qquad
J'(4)=\frac{40729}{114967512}>0,\qquad
J'(20)=-\frac{2559661}{557646408}<0.
\]

Continuity proves the existence of at least one strict local minimum between the first two points and a strict local maximum between the last two (analyticity rules out a constant interval). This exhibits reentrant total stationary error entirely inside the unbounded Schur-stability region. The proof does not assert uniqueness of those multidimensional extrema.

## Verification

The standalone `verify.py` (Python standard library only) independently solves the actual \(2\times2\) state-space covariance equations in rational arithmetic for a finite grid of stable parameters and checks its position variance against the derived rational formula. It separately checks the rational derivative, the three exact sign certificates, positive-definiteness of the stationary state covariance, and two finite stochastic-simulation diagnostics. Run from an extracted package with `python verify.py`; `CHECKS.txt` is a recorded example output. It reports `PASS: 299 checks`. These computational diagnostics do not prove the infinite-domain turning-point classification; Steps 1–4 provide the analytic proof.

## Relationship to prior work

Leplat et al., *NAG-GS: A Semi-Implicit Stochastic Optimizer with Large-Step Stability*, arXiv:2209.14937, Section 2.3, supply the semi-implicit update. Their Section 3.2 already establishes the general quadratic Schur boundary; their Section 3.5 supplies the stationary Lyapunov framework, and Appendix D remarks that explicit modal rational covariance expressions are obtainable but not pursued. Their paper and these already-known facts are **not** claimed as new. The present result computes the relevant modal expression and then proves a sharp parameter-dependent **number and type of extrema** and a strictly stable whole-system sign-reversal witness; neither is stated by the inspected sections or appendix.

Mohammadi, Razaviyayn and Jovanović, *Tradeoffs between convergence rate and noise amplification for momentum-based accelerated optimization algorithms*, arXiv:2209.11920, Section IV-C and Appendix E, establish general two-step stationary noise-amplification formulas. This broad framework contains the linear-recursion machinery needed to recover the variance after algorithm-specific substitution. It does not state the curvature-ratio bifurcation or the eleven-mode counterexample. The claim is **not** that the Lyapunov or AR(2) variance technique is original; the candidate new fact is its exact step-size phase diagram in this semi-implicit parameter family. General framework coverage is a meaningful residual originality risk.

Aybat, Fallah, Gürbüzbalaban and Ozdaglar, *Robust Accelerated Gradient Methods for Smooth Strongly Convex Functions*, arXiv:1805.10579, analyze robustness to stochastic errors for different accelerated-gradient parameterizations. Their results motivate separating deterministic convergence from stationary stochastic error, but do not establish this specific phase transition. Direct archival and semantic-database overlap checks found related stochastic methods, not the stated threshold or stable reentrant witness.

## Limitations

Only quadratic, SPD, constant-step NAG-GS with damping exactly \(\gamma=\mu\) and the specified independent Gaussian velocity increments is covered. The stable-domain restriction is essential and is not extended by analytic continuation of a covariance formula. The result does not quantify time-to-stationarity or endorse taking arbitrarily large steps in practice. The eleven-dimensional example proves a nonmonotonic total stationary mean-square error, not a global minimax optimum over arbitrary algorithms or noise models. General momentum noise-amplification literature is a substantial prior foundation; specialist precedence or an uninspected equivalent formulation remains possible. No independent external scientific audit has been performed.

## References

1. V. Leplat, D. Merkulov, A. Katrutsa, D. Bershatsky, O. Tsymboi and I. Oseledets. *NAG-GS: A Semi-Implicit Stochastic Optimizer with Large-Step Stability*. arXiv:2209.14937, first posted 29 September 2022. https://arxiv.org/abs/2209.14937 ; accessible version examined: https://arxiv.org/html/2209.14937v3 .
2. H. Mohammadi, M. Razaviyayn and M. R. Jovanović. *Tradeoffs between convergence rate and noise amplification for momentum-based accelerated optimization algorithms*. arXiv:2209.11920, 2022. https://arxiv.org/html/2209.11920v3 .
3. N. S. Aybat, A. Fallah, M. Gürbüzbalaban and A. Ozdaglar. *Robust Accelerated Gradient Methods for Smooth Strongly Convex Functions*. arXiv:1805.10579. https://arxiv.org/abs/1805.10579 .

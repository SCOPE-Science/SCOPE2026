# Sharp two-regime minimax shifts for write-noisy diagonal inverse preconditioning

## Finding

Consider one use of a diagonally shifted inverse programmed with independent centered additive entrywise errors. The worst-direction expected squared correction error relative to the *unshifted* inverse has an exact, unique minimizing shift. The optimum switches once, as the effective write-noise level varies, between a stationary high-eigenvalue branch and a crossing of low- and high-eigenvalue errors. In particular, a shift minimizing correction error can violate a simultaneously available signal-to-noise feasibility criterion for implementing the *shifted* inverse. These are distinct design objectives.

## Assumptions and scope

Fix an integer \(n\ge2\), a real diagonal positive-definite matrix \(A=\operatorname{diag}(\theta_1,\ldots,\theta_n)\), and its attained extreme eigenvalues \(0<a=\min_i\theta_i<b=\max_i\theta_i\). Set \(\kappa=b/a>1\). For each shift \(\beta\ge0\), let \(G_\beta=(A+\beta I)^{-1}\). Fix a weight scale \(w_r>0\), independent-copy count \(D\in\mathbb N\), and write standard deviation \(\sigma_w>0\). For every copy \(d\), \(\Phi_d\) has independent real entries of mean zero and variance \(\sigma_w^2\), and the copies are independent. There is no read noise, clipping, quantization, or subsequent solver iteration. The programmed operator is

\[
\widetilde G_\beta=G_\beta+\frac{\mu_\beta}{D}\sum_{d=1}^{D}\Phi_d,
\qquad \mu_\beta=\frac{\|G_\beta\|_{\max}}{w_r}=\frac{1}{w_r(a+\beta)}.
\]

For a deterministic unit exact correction \(v\), the corresponding input is \(r=Av\). Define the preconditioned relative solution risk

\[
\mathcal R(\beta)=\sup_{\|v\|_2=1}\mathbb E_\Phi\|\widetilde G_\beta Av-v\|_2^2.
\]

Write \(t=\beta/a\) and \(c=n\sigma_w^2/(Dw_r^2)>0\). Define

\[
 f_1(t)=\frac{t^2+c}{(1+t)^2},\qquad
 f_\kappa(t)=\frac{t^2}{(\kappa+t)^2}+\frac{c\kappa^2}{(1+t)^2}.
\]

Let \(x>0\) be the unique solution of

\[
 H_\kappa(x)=(\kappa+1)c,\qquad
 H_\kappa(t)=\frac{t^2(\kappa+1+2t)}{(\kappa+t)^2},
\]

and \(m>0\) the unique solution of

\[
 Q_\kappa(m)=\kappa c,\qquad
 Q_\kappa(t)=\frac{t(1+t)^3}{(\kappa+t)^3}.
\]

**Theorem.** For every parameter combination above,

\[
 \mathcal R(at)=\max\{f_1(t),f_\kappa(t)\},\qquad
 \boxed{\ \beta_*=a\min\{m,x\}\ }
\]

is the **unique** globally minimizing shift on \([0,\infty)\). There is exactly one positive root \(s_\kappa\) of

\[
 P_\kappa(s)=(\kappa+1)(1+s)^3-\kappa s(\kappa+s)(\kappa+1+2s)=0.
\]

Putting \(c_*(\kappa)=H_\kappa(s_\kappa)/(\kappa+1)\), the minimizer is \(\beta_*=am\) for \(0<c<c_*(\kappa)\), equals \(as_\kappa\) at the boundary, and is \(\beta_*=ax\) for \(c>c_*(\kappa)\). The last regime is a genuine nonsmooth equal-risk transition: both extreme eigendirections achieve the worst risk at the optimum.

For the exact example \(\kappa=2\) and \(c=7/12\), the unique minimizer is \(\beta_*=2a\), with

\[
\mathcal R(\beta_*)=\frac{55}{108},\qquad
\mathcal R(0)=\frac73.
\]

Nevertheless, the worst-direction root-mean-square *implementation-to-shifted-target* noise ratio squared at the minimizer is \(28/27>1\). This violates the strict signal-to-noise feasibility condition, while feasible sufficiently large finite shifts exist because \(c<1\).

## Proof

**Exact risk and endpoint reduction.** Centering and independent equal-variance entries imply for every deterministic vector \(z\)

\[
\mathbb E_\Phi\left\|\frac{\mu_\beta}{D}\sum_{d=1}^D\Phi_dz\right\|_2^2
=\frac{n\sigma_w^2\mu_\beta^2}{D}\|z\|_2^2.
\]

The cross term between the centered write error and the deterministic shift bias vanishes. As \(G_\beta A-I=-\beta(A+\beta I)^{-1}\), with \(\lambda_i=\theta_i/a\),

\[
\mathbb E_\Phi\|\widetilde G_\beta Av-v\|_2^2
=\sum_{i=1}^n|v_i|^2\left[\frac{t^2}{(\lambda_i+t)^2}+\frac{c\lambda_i^2}{(1+t)^2}\right].
\]

For each fixed \(t>0\) the bracketed function of \(\lambda>0\) has strictly positive second derivative

\[
\frac{6t^2}{(\lambda+t)^4}+\frac{2c}{(1+t)^2}>0.
\]

It is therefore convex on \([1,\kappa]\) and attains its maximum at an endpoint. At \(t=0\), the bracket equals \(c\lambda^2\), again maximized at the high endpoint. Both extremes occur among the eigenvalues; maximizing a diagonal quadratic form over unit vectors proves the first formula.

**Unique crossing.** Direct subtraction and factorization yield

\[
f_\kappa(t)-f_1(t)
=\frac{\kappa-1}{(1+t)^2}\bigl[(\kappa+1)c-H_\kappa(t)\bigr].
\]

The function \(H_\kappa\) increases strictly from zero to infinity, since its logarithmic derivative for positive \(t\) is \(2/t+2/(\kappa+1+2t)-2/(\kappa+t)>0\). Thus \(f_\kappa>f_1\) before the unique crossing \(x\), and \(f_1>f_\kappa\) afterwards. Also \(x>c\): after inserting \(t=c\), the positive difference needed for \(H_\kappa(c)<c(\kappa+1)\) is

\[
(\kappa+1)(\kappa+c)^2-c(\kappa+1+2c)
=\kappa^2(\kappa+1)+(2\kappa^2+\kappa-1)c+(\kappa-1)c^2>0.
\]

Consequently \(f_1'(t)=2(t-c)/(1+t)^3>0\) everywhere at or to the right of \(x\).

**Unimodality on the left branch.** Differentiating the higher-eigenvalue risk gives

\[
f_\kappa'(t)=\frac{2\kappa t}{(\kappa+t)^3}-\frac{2c\kappa^2}{(1+t)^3}.
\]

It has the sign of \(Q_\kappa(t)-\kappa c\). The function \(Q_\kappa\) increases strictly from zero to infinity, because

\[
\frac{Q_\kappa'(t)}{Q_\kappa(t)}=\frac1t+\frac3{1+t}-\frac3{\kappa+t}>0.
\]

Therefore the active risk strictly decreases up to \(\min\{m,x\}\), then strictly increases: until \(x\) this follows from \(f_\kappa\), and from \(x\) onward from \(f_1\). This proves existence and **uniqueness** of the global minimizer (including the possibility \(m=x\)).

**Single phase transition.** At the crossing, use \(c=H_\kappa(x)/(\kappa+1)\) to obtain

\[
Q_\kappa(x)-\kappa c
=\frac{xP_\kappa(x)}{(\kappa+1)(\kappa+x)^3}.
\]

In descending powers of \(s\), the cubic \(P_\kappa\) has coefficients

\[
1-\kappa,\quad -3\kappa^2+2\kappa+3,\quad
(\kappa+1)(3-\kappa^2),\quad \kappa+1.
\]

For \(\kappa>1\), their signs have exactly one change, ignoring possible zero coefficients: the quadratic coefficient changes sign at \((1+\sqrt{10})/3\), before the linear coefficient changes sign at \(\sqrt3\). Descartes' sign rule gives at most one positive root. Since \(P_\kappa(0)>0\) and its leading coefficient is negative, continuity gives exactly one, and the sign is positive before it and negative after it. Since \(H_\kappa\) is strictly increasing in \(x\), the sign of \(P_\kappa(x)\) switches precisely when \(c=c_*(\kappa)\). Below the boundary, \(Q_\kappa(x)>\kappa c\) and hence \(m<x\); above it, \(m>x\). This establishes the claimed phase classification.

**Exact feasibility counterexample.** For \(\kappa=2\), \(c=7/12\), direct substitution gives \(H_2(2)=7/4=3c\), and \(P_2(2)=-31<0\). Hence \(x=2<m\). The two endpoint risks at \(t=2\) both equal \(55/108\), and at \(t=0\) the worst risk is \(4c=7/3\). On the other hand, the worst implementation-to-shifted-target noise ratio squared is

\[
\frac{n\sigma_w^2}{Dw_r^2}\left(\frac{b+\beta}{a+\beta}\right)^2
=c\left(\frac{\kappa+t}{1+t}\right)^2,
\]

which at \(t=2\) equals \(28/27\), above its strict feasibility limit \(1\). Because \(c=7/12<1\), this ratio tends to \(c<1\) as \(t\to\infty\), so some finite shifts are feasible. Thus failure at the minimax shift is not caused by universal infeasibility.

## Verification

The companion `verify.py` uses only Python's standard library. It checks the risk identity against exact enumeration of independent symmetric two-point write errors on two- and three-dimensional diagonal matrices, including averaging two copies; it tests the exact rational counterexample, and it checks the analytic minimizer against finite parameter grids and perturbations with floating-point arithmetic. Its reported run result is `VERIFY_OK 1056 exact moment identities and numerical root/inequality checks`. The finite numerical tests are diagnostics; strict inequalities, uniqueness and the every-dimension result follow from the proof above, not from sampling or an exhaustive parameter search.

## Relationship to prior work

Shah, Li, Kalantzis and Xi's *Noise-Adaptive Analog–Digital Preconditioning* (arXiv:2611.17251v1, especially §3.3, Theorem 4 and equations (60)–(62)) supplies the identical centered independent-entry write model and a condition comparing programming noise with the **shifted** target. That criterion is not a minimax solution-accuracy optimization; the authors separately exhibit the regularization bias. Here those two error contributions are combined into one explicit worst-direction objective, and its global optimizer, spectral phase switch, and an infeasible-optimum example are determined.

Shah et al.'s earlier *Hybrid Digital-Analog Approximate Inverse Preconditioning for Krylov Methods* (arXiv:2606.17227) studies analog-aware damping and preconditioner design, not this diagonal objective's exact minimax phase law. Etter and Ying's *Operator Shifting for General Noisy Matrix Systems* (SIAM J. Math. Data Sci. 4 (2022), DOI 10.1137/21M1416849) optimizes an additive correction to the inverse of a **noisy coefficient matrix**; the estimator, parameterization, and matrix-noise mechanism differ from the present shifted deterministic inverse with independently programmed entry errors. The paper's general motivation for reducing inverse risk does not supply this particular root classification or the implementation-feasibility counterexample.

## Limitations

The analysis is for a diagonal SPD block, additive centered independent equal-variance programming errors, and one application measured in the Euclidean norm. The diagonal assumption is essential for \(\|G_\beta\|_{\max}=1/(a+\beta)\); an arbitrary orientation can change the scaling and the optimizer. The results do not address noncommuting blocks, read noise, clipping, quantization, rank corrections, outer Krylov convergence, wall-clock speed, or hardware energy. The effective noise parameter may be larger than typical simulated engineering values. Full historical priority and hardware-level usefulness are not independently established.

## References

1. S. Shah, R. P. Li, V. Kalantzis, Y. Xi, *Noise-Adaptive Analog–Digital Preconditioning*, arXiv:2611.17251v1 (2026-11-12), https://arxiv.org/html/2611.17251v1.
2. S. Shah, R. P. Li, T. Gokmen, V. Kalantzis, L. Horesh, Y. Xi, *Hybrid Digital-Analog Approximate Inverse Preconditioning for Krylov Methods*, arXiv:2606.17227 (2026-06-15), https://arxiv.org/abs/2606.17227.
3. P. A. Etter, L. Ying, *Operator Shifting for General Noisy Matrix Systems*, SIAM Journal on Mathematics of Data Science 4(4), 1320–1346 (2022), https://doi.org/10.1137/21M1416849.

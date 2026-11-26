# Exact fixed-step minimax noise tuning of signed heavy-ball momentum

## Finding
For any \(0<a\le b<4\) and nonzero innovation variance \(\sigma^2\), consider the scalar recurrences
\[
 z_{k+1}=(1+\beta-h)z_k-\beta z_{k-1}+\xi_{k+1},\qquad h\in[a,b],
\]
where innovations are independent across time, have mean zero and variance \(\sigma^2\). The same real momentum is used for every unknown curvature, and the stepsize is held fixed. All modes are Schur stable exactly when \(b/2-1<\beta<1\). The stationary variance is
\[
 V(h,\beta)=\frac{\sigma^2(1+\beta)}{(1-\beta)h\,[2(1+\beta)-h]}.
\]
The exact worst-mode design \(\min_{\beta}\sup_{h\in[a,b]}V(h,\beta)\) has the **unique** optimizer
\[
 \boxed{\beta_* =\operatorname{median}\!\left\{\sqrt a-1,\ \frac{a+b}{2}-1,\ \sqrt b-1\right\}.}
\]
In particular, write \(q_a=\sqrt a-1\), \(q_b=\sqrt b-1\), and \(q_c=(a+b)/2-1\). If \(q_c\le q_a\), the worst-mode minimum is achieved at \(q_a\); if \(q_a<q_c<q_b\), it is achieved at the equalizing choice \(q_c\); if \(q_b\le q_c\), it is achieved at \(q_b\). Ties at regime boundaries give the same unique momentum. In the middle regime the two endpoint variances are equal. At either exterior regime one endpoint alone controls the optimum (unless the endpoints coincide).

A sharp performance consequence is obtained for any fixed \(c>1\), \(b=ca\), and \(a\downarrow0\): for all sufficiently small \(a\), \(\beta_*=\sqrt a-1<0\), and
\[
 \min_{\beta\ge0}\sup_{h\in[a,ca]}V(h,\beta)
 \ \bigg/\ \min_{\beta}\sup_{h\in[a,ca]}V(h,\beta)
 =\frac{(2-\sqrt a)^2}{2-a}\longrightarrow 2.
\]
Thus the sign restriction on momentum can cost a factor asymptotically as large as two in robust stationary variance at fixed stepsize.

## Assumptions and scope
The normalized interval is \(h=\eta\lambda\in[a,b]\), for a **fixed** positive gradient stepsize \(\eta\) and an uncertain eigenvalue \(\lambda\). The noise variance concerns the additive term in the iterate recurrence; additive gradient noise of fixed variance \(\tau^2\) produces \(\sigma^2=\eta^2\tau^2\), independent of \(h\), and the same conclusion applies. Modes may belong to any real symmetric positive-definite quadratic Hessian whose spectrum lies inside the interval. The objective is worst **single eigenmode** variance across the complete allowed interval, not total trace covariance for a fixed finite spectrum. All initial conditions with finite covariance are allowed. No stationarity assumption on innovations beyond independence across time, centered second moments and constant variance is needed. There is no claim of optimal deterministic convergence rate.

## Proof
Set \(A_h=1+\beta-h\). The characteristic polynomial is \(r^2-A_hr+\beta\). The degree-two Jury criterion gives \(-1<\beta<1\), \(h>0\), and \(h<2(1+\beta)\). Hence simultaneous Schur stability over the interval is precisely \(b/2-1<\beta<1\). Since \(b<4\), the interval is nonempty.

Let \(s_0=\mathbb E[z_k^2]\) and \(s_1=\mathbb E[z_k z_{k-1}]\) in stationarity. Multiplication of the recurrence by \(z_k\) gives \(s_1=A_hs_0/(1+\beta)\). Squaring and using temporal independence of the innovation gives \(s_0=(A_h^2+\beta^2)s_0-2A_h\beta s_1+\sigma^2\). Substitution yields
\[
 s_0=\frac{\sigma^2(1+\beta)}{(1-\beta)[(1+\beta)^2-A_h^2]}
 =\frac{\sigma^2(1+\beta)}{(1-\beta)h[2(1+\beta)-h]}.
\]
Stationary covariance exists uniquely by Schur stability; the above identities also follow from the convergent covariance Lyapunov series.

For a fixed admissible momentum, the factor \(h[2(1+\beta)-h]\) is strictly concave in \(h\), so its minimum on \([a,b]\) occurs at an endpoint. Consequently
\[\sup_{h\in[a,b]}V(h,\beta)=\max\{V(a,\beta),V(b,\beta)\}.\]
For every fixed \(h\in(0,4)\), direct differentiation of the positive expression shows that \(V(h,\beta)\), on its stability interval, is strictly decreasing until \(\beta=\sqrt h-1\) and strictly increasing afterward: after a positive denominator is cleared, its derivative has the sign of \((1+\beta)^2-h\). This gives the two distinct single-mode minima \(q_a\le q_b\).

For \(a<b\), comparing the endpoint denominators shows that \(V(b,\beta)\ge V(a,\beta)\) exactly when \(\beta\le q_c=(a+b)/2-1\); on the other side \(V(a,\beta)\) is the larger value. Therefore the minimizer of the worst-mode objective is the nearest point to the crossing \(q_c\) in the ordered interval \([q_a,q_b]\): explicitly \(\operatorname{median}\{q_a,q_c,q_b\}\). Both active branches are strictly unimodal, and the piecewise envelope decreases strictly before this point and increases strictly after it. This proves uniqueness. If \(a=b\), the common single-mode minimum is \(\sqrt a-1\), agreeing with the median expression.

For fixed \(c>1\), as \(a\downarrow0\) with \(b=ca\), eventually \(0<a<b<1\) and \(q_c<q_a\). Thus \(\beta_*=q_a=\sqrt a-1<0\) with worst-mode variance \(\sigma^2/[a(2-\sqrt a)^2]\). When momentum is restricted to \(\beta\ge0\), both endpoint modal variances are strictly increasing in \(\beta\), so the best nonnegative choice is \(\beta=0\). Its worst variance equals \(\sigma^2/[a(2-a)]\). Dividing gives the asserted limit \(2\).

## Verification
The companion file `verify.py` recomputes the stationary covariance by directly solving the discrete Lyapunov equation, checks the endpoint reduction and optimizer against bounded scalar optimization over a reproducible parameter grid, checks uniqueness numerically away from the optimizer, and checks the negative-momentum limiting ratio. These finite tests are corroboration: the general proof is the explicit Jury, covariance, and scalar monotonicity argument above. Run `python verify.py` with NumPy and SciPy installed.

## Relationship to prior work
Flammarion and Bach (2015) study noisy second-order accelerated-gradient recurrences and their stability, providing an archival motivation but not this fixed-step stationary minimax tuning. Mohammadi, Razaviyayn and Jovanović (2019) analyze exact mode-by-mode steady-state noise amplification for heavy-ball and acceleration, which supplies already-known variance machinery. Their subsequent (2022) two-step design study proves general noise-amplification formulas and endpoint equalization along an adjustable-stepsize, settling-time-parameterized family; that equalization phenomenon is therefore not claimed as new. The present claim is **only** the complete, unique, three-regime optimum when the stepsize is fixed and signed momentum alone varies, together with the sharp low-curvature cost of disallowing negative momentum. This is not a claim that the stationary variance formula, Schur test, or equalization principle was first discovered here.

## Limitations
The uncertainty interval is known and the noise is additive with curvature-independent variance. For a fixed finite-dimensional Hessian the **sum** of modal variances may favor a different momentum. The result does not optimize the stepsize or transient performance and does not cover correlated or state-dependent noise. General optimization literature may contain an equivalent special-purpose minimax tuning rule not located by the cited comparison; independent validation and comprehensive human literature review have not occurred.

## References
1. N. Flammarion and F. Bach, *From Averaging to Acceleration, There is Only a Step-size*, arXiv:1504.01577, initially submitted 2015-04-07, https://arxiv.org/abs/1504.01577.
2. H. Mohammadi, M. Razaviyayn and M. R. Jovanović, *Robustness of accelerated first-order algorithms for strongly convex optimization problems*, arXiv:1905.11011, initially submitted 2019-05-27, https://arxiv.org/abs/1905.11011.
3. H. Mohammadi, M. Razaviyayn and M. R. Jovanović, *Tradeoffs between convergence rate and noise amplification for momentum-based accelerated optimization algorithms*, arXiv:2209.11920, initially submitted 2022-09, https://arxiv.org/abs/2209.11920.

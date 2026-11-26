# A sharp endpoint-to-interior loading transition for spectral conditioning of a four-site diffusion path

## Finding

For \(\mu,B>0\), let
\[
A(d)=\mu I_4+\begin{pmatrix}1&-1&0&0\\-1&2&-1&0\\0&-1&2&-1\\0&0&-1&1\end{pmatrix}+\operatorname{diag}(d_1,d_2,d_3,d_4),\qquad d_i\ge0,\quad \sum_i d_i=B.
\]
The minimizer of \(\kappa_2(A)=\lambda_{\max}(A)/\lambda_{\min}(A)\) over all four independent loads is unique. Put \(q=B/4\), \(m=\mu+1+q\), \(a(t)=\sqrt{1+t^2}\), \(b(t)=\sqrt{1+(1-t)^2}\), and, on the feasible interval \([-q,q]\), put
\[
F_{\mu,q}(t)=\frac{t}{a(t)[m-a(t)]}-\frac{1-t}{b(t)[m+1+b(t)]}.
\]
There is exactly one \(q_c(\mu)\in(0,1/2)\) with \(F_{\mu,q_c}(q_c)=0\). Let \(B_c(\mu)=4q_c(\mu)\). The unique optimizer is \((q+t_*,q-t_*,q-t_*,q+t_*)\), where

- if \(0<B\le B_c(\mu)\), then \(t_*=q\), so the load is \((B/2,0,0,B/2)\);
- if \(B>B_c(\mu)\), then \(t_*\in(0,\min\{q,1/2\})\) is the unique feasible zero of \(F_{\mu,q}\).

In both cases the optimal condition number is \((m+1+b(t_*))/(m-a(t_*))\). For fixed \(\mu\), once interior sites activate the contrast \(2t_*\) strictly increases with \(B\) and tends to \(1\). Also \(B_c(\mu)\to2\) as \(\mu\to\infty\), and \(B_c(\mu)\sim4\mu/(1+2\sqrt2)\) as \(\mu\downarrow0\).

## Proof

**Strict reflection reduction.** Write \(R\) for coordinate reversal, and let \(\bar A=(A+RAR)/2\). This preserves feasibility and gives \(\lambda_{\max}(\bar A)\le\lambda_{\max}(A)\) and \(\lambda_{\min}(\bar A)\ge\lambda_{\min}(A)\) by the extremal Rayleigh quotients. The smallest eigenvalue of \(\bar A\) has a unique positive unit eigenvector \(v\): a sufficiently large scalar shift of \(-\bar A\) is nonnegative and irreducible, so Perron–Frobenius applies. The uniqueness and \(R\bar A=\bar A R\) imply \(Rv=v\). Thus \(v^TAv=v^T\bar A v=\lambda_{\min}(\bar A)\). If equality held in the minimum-eigenvalue bound then \(v\) would also be an eigenvector of \(A\) at the same eigenvalue, giving \((A-\bar A)v=0\). That is impossible for a nonsymmetric loading because the difference is diagonal and every entry of \(v\) is positive. Since all feasible matrices are positive definite, nonsymmetric loading strictly worsens the condition number relative to its symmetrization.

**Extremal eigenvalues.** The symmetric loads have the form \((q+t,q-t,q-t,q+t)\), with \(|t|\le q\). The even and odd reflection blocks are
\[
S=\begin{pmatrix}m+t&-1\\-1&m-t\end{pmatrix},\qquad
T=\begin{pmatrix}m+t&-1\\-1&m+2-t\end{pmatrix}.
\]
Their spectra are \(m\pm a(t)\) and \(m+1\pm b(t)\). Since \(T-S=\operatorname{diag}(0,2)\) is positive semidefinite, the overall smallest eigenvalue is \(m-a(t)\) and the largest is \(m+1+b(t)\). The smaller one is positive throughout feasibility because \(a(t)\le\sqrt{1+q^2}<1+q<m\).

**Sign of the derivative on the whole feasible interval.** The derivative of the log condition number is \(F_{\mu,q}(t)\). For feasible \(t\le0\) it is negative. For feasible \(0<t<1/2\), the first term strictly increases: \(t/a(t)\) increases and the positive factor \(m-a(t)\) decreases. The positive term being subtracted strictly decreases: set \(s=1-t\) and \(M=m+1\). The derivative of \(s/[\sqrt{1+s^2}(M+\sqrt{1+s^2})]\) with respect to \(s\) has the sign of \(M+\sqrt{1+s^2}(1-s^2)\), positive for \(0<s<1\).

For feasible \(1/2\le t<1\) we have \(t\ge 1-t\ge0\), so \(t/a(t)\ge (1-t)/b(t)\) by monotonicity of \(u/\sqrt{1+u^2}\), while \(0<m-a(t)<m+1+b(t)\). These inequalities give strict positivity of \(F_{\mu,q}(t)\) throughout this range, including \(t=1/2\) when feasible. For feasible \(t\ge1\), its first term is positive and its second contribution is nonnegative. Hence for \(q\ge1/2\) there is exactly one zero between \(0\) and \(1/2\) and it is the strict minimizer. For \(q<1/2\), the minimum is uniquely at \(q\) when \(F_{\mu,q}(q)\le0\), and otherwise at the unique zero in \((0,q)\). The argument involves only feasible points and never requires evaluating at \(1/2\) when \(q<1/2\).

**Boundary activation.** For \(0<q\le1/2\), let \(\alpha=\sqrt{1+q^2}\), \(\beta=\sqrt{1+(1-q)^2}\), and write
\[
F_{\mu,q}(q)=f_\mu(q)-g_\mu(q),\quad
f_\mu(q)=\frac{q}{\alpha(\mu+1+q-\alpha)},\qquad
g_\mu(q)=\frac{1-q}{\beta(\mu+2+q+\beta)}.
\]
With \(h=1+q-\alpha>0\), we have \(f_\mu=\frac{1+q+\alpha}{2\alpha}\frac{h}{h+\mu}\). Both positive factors strictly increase, by the respective derivatives \((1-q)/(2\alpha^3)>0\) and \(h'=1-q/\alpha>0\) for the factor's argument \(h\). The factor \((1-q)/\beta\) in \(g_\mu\) strictly decreases and \(\mu+2+q+\beta\) strictly increases (its derivative is \(1-(1-q)/\beta>0\)). So \(g_\mu\) strictly decreases. At \(q=0\) the difference is negative; at \(1/2\) it is positive by the feasible derivative comparison. The unique crossing and the preceding optimization argument give precisely the two regimes.

**Contrast and threshold limits.** At fixed \(t\in(0,1/2)\), feasible for the budgets compared, the ratio of the positive terms in \(F_{\mu,q}(t)\) is strictly decreasing in \(m\) since its log derivative is \(1/(m+1+b(t))-1/(m-a(t))<0\). At fixed \(m\) that ratio is strictly increasing in \(t\) on the feasible part of \((0,1/2)\). Comparing two budgets above threshold at the smaller budget's root therefore gives strict root increase. At a root,
\[
\frac{t_*}{a(t_*)}\left(1+\frac{1+b(t_*)}{m}\right)=\frac{1-t_*}{b(t_*)}\left(1-\frac{a(t_*)}{m}\right).
\]
As \(q\to\infty\), compactness and the limiting equality \(t/a(t)=(1-t)/b(t)\) force \(t_*	o1/2\).

For each fixed \(q\in(0,1/2)\), \(\mu(f_\mu(q)-g_\mu(q))\to q/\alpha-(1-q)/\beta<0\) as \(\mu\to\infty\), so \(q_c\to1/2\). For each such fixed \(q\), the limit of \(f_\mu(q)\) as \(\mu\downarrow0\) is \((1+q+\alpha)/(2\alpha)>1\), whereas \(g_\mu(q)<1\). It follows that \(q_c\to0\). At the crossing, \(f_\mu(q_c)=(1+o(1))q_c/(\mu+q_c)\) as \(\mu\downarrow0\), and \(g_\mu(q_c)\to1/[\sqrt2(2+\sqrt2)]\). This yields \(q_c/\mu\to1/(1+2\sqrt2)\).

## Verification, prior context and scope

The bundled `CHECKER.py` uses SymPy, NumPy and SciPy to check parity-block identities and finite allocation/root comparisons. These tests corroborate, but do not prove, the all-budget uniqueness and threshold. For \(\mu=1\), \(B_c\approx0.6698541123203\); at \(B=1\), the optimal loading is approximately \((0.42542745718,0.07457254282,0.07457254282,0.42542745718)\) and \(\kappa_*\approx3.68187390675\).

Z. Lu and T. K. Pong, [*Minimizing Condition Number via Convex Programming*](https://doi.org/10.1137/100795097), treat general convex feasible sets. That framework includes the present problem but a general convex reformulation is not the explicit four-path activation classification proven here. Compare M. Maréchal and J. Ye, [*Optimizing Condition Numbers*](https://doi.org/10.1137/080740544), and the trace-preserving diagonal-perturbation work of [J. A. Torres and S. Roy](https://doi.org/10.1109/CDC.2015.7402875) and [P. van den Driessche](https://doi.org/10.1016/0024-3795(94)90415-4), which consider a single dominant eigenvalue rather than the ratio of both extremes. Related exact graph allocations include the [unit-star hub activation](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-sharp-hub-activation-threshold-for-budgeted-diagonal-condition--7eae57d4d0a9) and [weighted four-path single-pin comparison](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-reentrant-optimal-single-pin-conditioning-on-a-four-vertex-weigh--cb2cd1385531); their graph or feasible allocation family is different. No exhaustive priority claim is made.

The theorem concerns additive loading with equal prices, unit conductances and a uniform scalar shift, not multiplicative Jacobi preconditioning, general weighted paths, or simply maximizing the smallest eigenvalue. The activation cutoff is implicit, not a claim of an elementary radical formula.

# Sharp ambient-extension stability frontier for Stiefel exponential moving averages

## Finding

The deterministic ambient-gradient RGR-EMA iteration on the circle has a sharp local linearized stability frontier that depends on a *normal derivative* invisible to the constrained objective. Fix any \(\theta>0\) and \(c\in\mathbb R\). The smooth ambient objectives
\[
 F_c(x)=x_2+\frac c2(\|x\|_2^2-1)\exp\!\left[-(\|x\|_2^2-1)^2\right]
\]
all restrict to the **same** circle objective \(f(x)=x_2\), with its strict minimizer \(x_\star=(0,-1)\). The ambient EMA fixed state at this minimizer is \(N_\star=(0,1-c)\). Its nonautonomous linearization is asymptotically stable for \(c<1+1/\theta\) and unstable for \(c>1+1/\theta\). The threshold is sharp for the specified linearized iteration; the critical equality is not classified here. Thus two globally smooth ambient representations of one identical constrained problem can have opposite local linearized stability under the same open-loop RGR-EMA method and stepsize.

## Assumptions and scope

Set \(\mathrm{St}(2,1)=S^1\), \(\beta_t=t^{-1/2}\) and \(\mu_t=\theta\beta_t\) for integer \(t\ge1\). The oracle is deterministic, so its variance is zero. With an ambient estimate \(N_{t-1}\in\mathbb R^2\), the update is exactly
\[
 N_t=(1-\beta_t)N_{t-1}+\beta_t\nabla F_c(x_t),\quad S_t=(I-x_tx_t^{\mathsf T})N_t,\quad x_{t+1}=\frac{x_t-\mu_t S_t}{\|x_t-\mu_t S_t\|_2}.
\]
The normalized-step retraction is well defined because \(S_t\perp x_t\). The \(F_c\) are smooth on all of \(\mathbb R^2\), and their first and second derivatives are globally bounded. The claim concerns **linearized local stability of the fixed trajectory** \((x_\star,N_\star)\), under arbitrary sufficiently late small variations in state, not guaranteed convergence of all nonlinear starts.

## Proof

Write \(x(\varphi)=(\sin\varphi,-\cos\varphi)\), with unit tangent \(v(\varphi)=(\cos\varphi,\sin\varphi)\), so \(\varphi=0\) is the strict minimizer. On the circle, differentiation of the ambient extension gives
\[
 \nabla F_c(x(\varphi))=(c\sin\varphi,1-c\cos\varphi),\qquad f(x(\varphi))=-\cos\varphi.
\]
Let \(u_t\) be the first component of \(N_t\), and let \(w_t\) denote its second component minus \(1-c\). The exact EMA components obey
\[
 u_t=(1-\beta_t)u_{t-1}+c\beta_t\sin\varphi_t,\quad
 w_t=(1-\beta_t)w_{t-1}+c\beta_t(1-\cos\varphi_t).
\]
The tangent coefficient is \(q_t=v(\varphi_t)^\mathsf TN_t\). Since normalized tangent retraction rotates the angle by \(-\arctan(\mu_tq_t)\), the exact local angle update is
\[
 \varphi_{t+1}=\varphi_t-\arctan(\theta\beta_tq_t),\quad
 q_t=\cos\varphi_t\,u_t+\sin\varphi_t(1-c+w_t).
\]
At the fixed state \((\varphi,u,w)=(0,0,0)\), the normal-memory derivative is the scalar \(1-\beta_t\), decoupled from the other two coordinates. In the active coordinates \(z_t=(\delta\varphi_t,\delta u_{t-1})^{\mathsf T}\), direct differentiation yields **the exact** linearized matrix
\[
 z_{t+1}=B_tz_t,\quad B_t=I+\beta_t A+\beta_t^2C,
\]
where
\[
 A=\begin{pmatrix}-\theta(1-c)&-\theta\\c&-1\end{pmatrix},\qquad
 C=\begin{pmatrix}-\theta c&\theta\\0&0\end{pmatrix}.
\]
The characteristic polynomial is
\[
 \det(\lambda I-A)=\lambda^2+\bigl(1+\theta(1-c)\bigr)\lambda+\theta.
\]
Because \(\det A=\theta>0\), its eigenvalues have negative real parts exactly when \(1+\theta(1-c)>0\), and positive real parts exactly when the inequality reverses. In the former case, the Lyapunov equation \(A^{\mathsf T}P+PA=-I\) has a positive-definite solution. The exact \(B_t=I+\beta_tA+O(\beta_t^2)\) then gives \(B_t^{\mathsf T}PB_t-P\preceq-\beta_t I/2\) for all sufficiently large \(t\). Since \(\sum_t\beta_t=\infty\), active linear perturbations decay to zero; the independent normal variation is multiplied by \(1-\beta_t\) and also decays. In the latter case, the positive-real-part eigenvalues make \(-A\) Hurwitz. A positive-definite \(P\) then solves \(A^{\mathsf T}P+PA=I\), giving \(B_t^{\mathsf T}PB_t-P\succeq\beta_t I/2\) eventually. Every nonzero active linear perturbation grows in this norm, proving linearized instability. At equality the leading matrix has purely imaginary eigenvalues and the argument does not decide stability.

Since the restrictions of all ambient extensions are identical and \(f''(0)=1\) regardless of \(c\), the change of stability is caused solely by normal-gradient memory. For example \(\theta=1/2\) gives the threshold \(c=3\): \(c=0\) is on the stable side and \(c=4\) on the unstable side, while both use precisely \(f(x)=x_2\) on \(S^1\).

## Verification

The included standalone `verify.py` checks the symbolic Jacobian, characteristic polynomial, normal-memory multiplier and exact finite-step determinant. It also differentiates the original nonlinear recursion numerically at the fixed state for selected parameters and compares the Jacobian to the symbolic expression. These finite checks support, but do not replace, the analytic Lyapunov argument.

## Relationship to prior work

Yuan, Sun and Yuan (2026) introduce the ambient RGR-EMA recurrence and tangent projection used verbatim here. Their convergence result (Theorem 4.3) assumes a sufficiently small \(\theta\) depending on ambient smoothness constants; this finding neither refutes nor weakens that guarantee. The same paper's tangent-space REMA comparator in Appendix B explicitly projects individual gradients and uses parallel transport, thus does not possess this particular normal-component accumulation. Earlier Riemannian momentum methods by Han and Gao (2021) and Alimisis and collaborators (2021) motivate tangent-space alternatives, but the precise normal-extension-dependent linearized frontier is not stated in the inspected source material.

## Limitations

The conclusion concerns deterministic RGR-EMA, a fixed normalized retraction, \(S^1\), and late-time local **linearization**. It does not classify the equality \(c=1+1/\theta\), establish the global nonlinear basin, imply divergence of every start or address stochastic noise. The sufficient global guarantees of the motivating paper use additional small-stepsize restrictions. Historical priority beyond inspected sources remains subject to further human review.

## References

1. Z. Yuan, L. Sun and G. Yuan, *Recursive Gradient Retraction Methods for Stochastic Nonconvex Optimization on Stiefel Manifolds*, arXiv:2610.19944v1, first posted 2026-10-14. https://arxiv.org/html/2610.19944v1
2. A. Han and J. Gao, *Riemannian Stochastic Recursive Momentum Method for non-Convex Optimization*, IJCAI 2021. https://www.ijcai.org/proceedings/2021/345
3. F. Alimisis, A. Orvieto, G. Bécigneul and A. Lucchi, *Momentum Improves Optimization on Riemannian Manifolds*, AISTATS 2021. https://proceedings.mlr.press/v130/alimisis21a.html

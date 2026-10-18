# Exact spectral stability and root geometry for Hessian-corrected heavy ball

## Finding
Consider the constant-parameter Heavy Ball method with Hessian correction
\[
y_k=x_k+\alpha(x_k-x_{k-1})-\theta\bigl(\nabla h(x_k)-\nabla h(x_{k-1})\bigr),
\qquad
x_{k+1}=y_k-\beta\nabla h(x_k),
\]
with \(0\le\alpha\le1\), \(\theta\ge0\), and \(\beta>0\), applied to the symmetric positive-definite quadratic
\[
h(x)=\frac12x^\top Hx,
\qquad
\operatorname{spec}(H)\subset[\mu,L],
\qquad
0<\mu\le L.
\]
For an eigenvector of \(H\) with eigenvalue \(\lambda\), the scalar mode \(z_k\) satisfies
\[
z_{k+1}=igl(1-\beta\lambda+m_\lambda\bigr)z_k-m_\lambda z_{k-1},
\qquad
m_\lambda=\alpha-\theta\lambda.
\]
Hence its characteristic polynomial is
\[
p_\lambda(r)=r^2-\bigl(1-\beta\lambda+m_\lambda\bigr)r+m_\lambda.
\]

The mode is asymptotically stable, meaning both roots satisfy \(|r|<1\), if and only if
\[
|m_\lambda|<1,
\qquad
0<\beta\lambda<2(1+m_\lambda).
\]
Therefore the method is asymptotically stable on every SPD quadratic with spectrum contained in \([\mu,L]\) if and only if
\[
\alpha-\theta\mu<1,
\qquad
L(\beta+2\theta)<2(1+\alpha).
\]
The second inequality already implies \(\alpha-\theta L>-1\), so no additional lower-momentum condition is needed.

The same calculation gives the complete modal root geometry inside the stable region. If \(0<m_\lambda<1\), then the roots are complex conjugates exactly when
\[
(1-\sqrt{m_\lambda})^2
<\beta\lambda<
(1+\sqrt{m_\lambda})^2.
\]
They are both nonnegative exactly when
\[
0\le m_\lambda<1,
\qquad
0<\beta\lambda\le(1-\sqrt{m_\lambda})^2.
\]
For \(0<m_\lambda<1\), the remaining stable real-root branch
\[
(1+\sqrt{m_\lambda})^2\le\beta\lambda<2(1+m_\lambda)
\]
has two negative roots. If \(m_\lambda<0\), the product of the roots is negative, so the roots are real with opposite signs.

Thus the curvature correction has an exact spectral tradeoff. Increasing \(\theta\) replaces the constant Heavy Ball momentum \(\alpha\) by the decreasing modal momentum \(m_\lambda=\alpha-\theta\lambda\). This can move high-curvature modes out of the complex-root band, but after \(\theta\lambda>\alpha\) one real root is necessarily negative. Simultaneously, the exact robust stability ceiling is controlled by \(\beta+2\theta\), so curvature damping consumes step-size margin linearly.

For example, with \(L=4\), \(\mu=1\), \(\alpha=0.9\), \(\theta=0.2\), and \(\beta=0.1\), the exact robust conditions hold because
\[
\alpha-\theta\mu=0.7<1,
\qquad
L(\beta+2\theta)=2<3.8=2(1+\alpha).
\]
The source's general strongly-quasiconvex theorem does not cover this choice because it assumes \(\alpha<1/\sqrt2\). On the quadratic, however, every mode in \([1,4]\) is stable. The curvature-\(4\) mode has \(m_4=0.1\) and \(\beta\lambda=0.4\), which lies below \((1-\sqrt{0.1})^2\), so its two roots are real and positive.

## Assumptions and scope
The statement is exact for symmetric positive-definite quadratic objectives and the constant-parameter Heavy Ball scheme with Hessian correction defined in the source. The spectrum is assumed to lie in a compact positive interval \([\mu,L]\), so there is no zero-curvature mode. The parameters satisfy the source sign conventions \(0\le\alpha\le1\), \(\theta\ge0\), and \(\beta>0\).

The finding is a spectral characterization, not a replacement for the source's nonlinear convergence theorem. The source theorem applies to a broad class of strongly quasiconvex functions under sufficient parameter conditions; the present result gives necessary-and-sufficient conditions only on SPD quadratics. Root sign is used only to describe the linear modal recurrence; it is not asserted that every initial condition visibly oscillates, because an initial state can cancel one eigensolution.

## Proof
Diagonalize \(H=Q\Lambda Q^\top\) with \(Q\) orthogonal. In the eigenbasis, each coordinate evolves independently. For a mode of curvature \(\lambda>0\),
\[
\nabla h(x_k)-\nabla h(x_{k-1})
=
\lambda(z_k-z_{k-1}),
\]
so the source update becomes
\[
\begin{aligned}
z_{k+1}
&=z_k+\alpha(z_k-z_{k-1})-\theta\lambda(z_k-z_{k-1})-\beta\lambda z_k\\
&=(1-\beta\lambda+m_\lambda)z_k-m_\lambda z_{k-1},
\end{aligned}
\]
where \(m_\lambda=\alpha-\theta\lambda\).

Write
\[
A_\lambda=1-\beta\lambda+m_\lambda.
\]
The monic polynomial is \(r^2-A_\lambda r+m_\lambda\). The degree-two Jury criterion says that both roots lie strictly in the unit disk if and only if
\[
|m_\lambda|<1,
\qquad
1-A_\lambda+m_\lambda>0,
\qquad
1+A_\lambda+m_\lambda>0.
\]
The middle expression equals \(\beta\lambda>0\). The last equals
\[
2(1+m_\lambda)-\beta\lambda.
\]
This proves the modal stability condition.

For all \(\lambda\in[\mu,L]\), the upper product condition \(m_\lambda<1\) is strongest at \(\mu\) and gives
\[
\alpha-\theta\mu<1.
\]
The last Jury inequality is affine and decreasing in \(\lambda\):
\[
2(1+\alpha)-(\beta+2\theta)\lambda>0.
\]
It is therefore equivalent to
\[
L(\beta+2\theta)<2(1+\alpha).
\]
This inequality also gives
\[
\theta L<1+\alpha-\frac{\beta L}{2}<1+\alpha,
\]
so \(m_L>-1\), and monotonicity of \(m_\lambda\) then yields \(m_\lambda>-1\) for every \(\lambda\in[\mu,L]\). Hence the two displayed endpoint inequalities are necessary and sufficient for robust SPD stability.

For the root geometry, the discriminant is
\[
\Delta_\lambda
=
(1-\beta\lambda+m_\lambda)^2-4m_\lambda.
\]
If \(m_\lambda<0\), then \(\Delta_\lambda>0\) and the root product is negative, proving the opposite-sign statement. If \(m_\lambda>0\), then \(\Delta_\lambda<0\) exactly when
\[
-2\sqrt{m_\lambda}
<1-\beta\lambda+m_\lambda
<2\sqrt{m_\lambda},
\]
which rearranges to
\[
(1-\sqrt{m_\lambda})^2
<\beta\lambda<
(1+\sqrt{m_\lambda})^2.
\]
On the lower real branch the root sum is positive and the product is nonnegative, so both roots are nonnegative. On the upper real branch the root sum is negative and the product is positive, so both roots are negative. This gives the complete classification stated above, including the boundary case \(m_\lambda=0\).

## Verification
The bundled script `artifacts/verify_hessian_hb_phase.py` independently forms the characteristic roots for random admissible parameters and checks the Jury criterion, the endpoint robust condition, and the complex/positive/negative/opposite-sign root classification. It also replays the explicit \([1,4]\) example.

The numerical replay is a consistency check only. The quantified result follows from diagonalization and the exact degree-two Jury and discriminant calculations above.

## Relationship to prior work
Hadjisavvas, Lara, Marcavillaca, and Vuong introduce exactly the gradient-difference correction analyzed here. Their Heavy Ball theorem proves linear convergence for general strongly quasiconvex objectives under a sufficient parameter region, and their numerical discussion emphasizes reduced oscillations from Hessian-driven damping. The source does not give the quadratic characteristic polynomial, a necessary-and-sufficient SPD stability region, or the modal root-sign/complexity phase diagram.

The immediate strongly-quasiconvex Heavy Ball predecessor of Lara, Marcavillaca, and Vuong analyzes the uncorrected method, corresponding to \(\theta=0\). Classical spectral analyses of Heavy Ball likewise use curvature-independent momentum. A recent exact result on fixed-parameter Heavy Ball shows that requiring real roots uniformly over a spectral interval creates an acceleration barrier, but it concerns the \(\theta=0\) recurrence and therefore does not imply the curvature-dependent momentum law \(m_\lambda=\alpha-\theta\lambda\) or the exact stability budget \(\beta+2\theta\) derived here.

## Limitations
The phase diagram is exact only for SPD quadratics. For nonlinear strongly quasiconvex functions, curvature varies along the trajectory and different eigendirections need not decouple, so the modal conditions are not a nonlinear convergence theorem. The result also does not optimize \((\alpha,\beta,\theta)\) for the best worst-case spectral radius.

The statement that a negative root is an alternating component is modal: a specially chosen initial pair can cancel that root. Likewise, complex roots characterize an underdamped linear mode but do not by themselves quantify objective-value oscillation in a multidimensional superposition.

## References
1. N. Hadjisavvas, F. Lara, R. T. Marcavillaca, P. T. Vuong, *Heavy Ball and Nesterov Accelerations with Hessian-Driven Damping for Nonconvex Optimization*, arXiv:2506.15632v1, first public 2025-06-18; *Applied Mathematics & Optimization* 93 (2026), Article 63, DOI:10.1007/s00245-026-10406-2.
2. F. Lara, R. T. Marcavillaca, P. T. Vuong, *Characterizations, Dynamical Systems and Gradient Methods for Strongly Quasiconvex Functions*, arXiv:2410.03534; *Journal of Optimization Theory and Applications* 206 (2025), Article 60, DOI:10.1007/s10957-025-02728-y.
3. *Uniform real-root barrier for fixed-parameter heavy-ball acceleration*, published mathematical-research record 2026/9/20/SCOPE-heavy-ball-real-root-acceleration-barrier--5f3230b80158.

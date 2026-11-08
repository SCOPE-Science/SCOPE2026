# Exact two-period stability frontiers for two reflected-splitting step conventions

## Finding

For the matched-skew monotone inclusion described below, alternating two arbitrary positive steps has *different sharp stability boundaries* according to which step scales the reused gradient difference. With the current step used everywhere (current-scaled reflection), **all** iterates converge to the unique zero precisely when
\[
4ab<1.
\]
With the previous step used on the gradient difference (history-scaled reflection), **all** iterates converge precisely when
\[
a+b<1.
\]
Here \(a\) and \(b\) are the two positive dimensionless alternating steps. At either equality there is a simple nondecaying two-step multiplier \(-1\); beyond it there is a two-step multiplier strictly outside the unit circle. In particular, for every nonzero starting point with equal initial history, \(x_{-1}=x_0\ne0\), at equality the sequence does not converge, and above equality it diverges geometrically. The current-scaled method can therefore converge with one arbitrarily large step, while the history-scaled method cannot. The boundaries coincide only for equal steps.

## Assumptions and scope

Let \(J:\mathbb R^2\to\mathbb R^2\) be the counterclockwise quarter-turn \(J(u,v)=(-v,u)\). For any fixed \(L>0\), take the maximal monotone operator \(A=LJ\) and the monotone, \(L\)-Lipschitz map \(B=LJ\). Their sum has exactly one zero, the origin. Write \(R_t=(I+tJ)^{-1}\) for \(t>0\). Specify positive dimensionless steps \(t_{2j}=a\), \(t_{2j+1}=b\) and \(t_{-1}=b\), with \(a,b>0\). The actual steps are \(t_k/L\). Both updates start from arbitrary \(x_{-1},x_0\in\mathbb R^2\):

**Current-scaled reflection:**
\[
x_{k+1}=R_{t_k}\bigl(x_k-t_kJ(2x_k-x_{k-1})\bigr).
\]
**History-scaled reflection:**
\[
x_{k+1}=R_{t_k}\bigl(x_k-t_kJx_k-t_{k-1}J(x_k-x_{k-1})\bigr).
\]
The second is the variable-step update formula used in the cited linesearch FRB literature, here with a *prescribed* alternating schedule rather than its adaptive acceptance rule. No convergence guarantee for adaptive linesearch or general monotone inclusions is asserted.

## Proof

Identify \(\mathbb R^2\) with \(\mathbb C\) so that \(J\) acts as multiplication by \(i\). With complex state \((z_k,z_{k-1})\), the two transition matrices are
\[
T_c(t)=\begin{pmatrix}\frac{1-2it}{1+it}&\frac{it}{1+it}\\1&0\end{pmatrix},\qquad
T_h(t,u)=\begin{pmatrix}\frac{1-i(t+u)}{1+it}&\frac{iu}{1+it}\\1&0\end{pmatrix}.
\]
Define \(M_c=T_c(b)T_c(a)\), \(M_h=T_h(b,a)T_h(a,b)\), \(D=(1+ia)(1+ib)\), \(s=a+b\), and \(p=ab\). Straight matrix multiplication gives
\[
\begin{aligned}
\operatorname{tr}M_c&=\frac{1-is-6p}{D},&\det M_c&=-\frac pD,\\
\operatorname{tr}M_h&=\frac{1-is-2(a^2+ab+b^2)}D,&\det M_h&=-\frac pD.
\end{aligned}
\]
For either monodromy, \(|\det M|=p/\sqrt{(1+a^2)(1+b^2)}<1\). For a complex monic quadratic \(z^2-tz+d\) with \(|d|<1\), the Schur–Cohn condition for both roots to lie *strictly* inside the disk is
\[
(1-|d|^2)^2-|t-\overline t d|^2>0.
\]
Substituting the traces and determinant yields the exact factors
\[
\begin{aligned}
\Delta_c&=\frac{8ab(1-4ab)(1+2(a+b)^2)}{(1+a^2)^2(1+b^2)^2},\\
\Delta_h&=\frac{4(1-(a+b)^2)((a+b)^4+a^2+b^2)}{(1+a^2)^2(1+b^2)^2}.
\end{aligned}
\]
Every factor other than the identified stability-sign term is strictly positive. This proves both strict convergence regions. At the boundaries,
\[
\det(I+M_c)=\frac{2(1-4ab)}D,
\qquad
\det(I+M_h)=\frac{2(1-(a+b)^2)}D.
\]
Consequently the boundary eigenvalue is exactly \(-1\); the other has modulus \(|\det M|<1\), proving simplicity. Past either threshold \(\Delta<0\), hence at least one eigenvalue lies strictly outside the disk; because \(|\det M|<1\), exactly one does so and the other lies inside. The two-step dynamics, together with bounded one-step matrices, give the claimed geometric convergence or divergence for initial states with a nonzero expanding component.

For equal-history initial data \(z_{-1}=z_0\ne0\), the first update in **both** conventions is \(z_1/z_0=(1-ia)/(1+ia)\), whose modulus is exactly \(1\). If \((z_0,z_0)\) lay in the one-dimensional stable eigenspace of the two-step monodromy at or beyond its boundary, the second component of \(M(z_0,z_0)\) would force the stable eigenvalue to equal \(z_1/z_0\), an impossibility because its modulus is strictly below \(1\). Thus this natural initialization always excites the neutral or expanding mode. Finally, \(a+b\ge2\sqrt{ab}\) proves the history-stable region is strictly contained in the current-stable region when \(a\ne b\); for example \((a,b)=(1/10,2)\) is current-stable but history-unstable.

## Verification

Run `python verify.py` after installing SymPy. The standalone verifier directly reconstructs both monodromies and checks the trace, determinant, Schur–Cohn discriminant factorization, and boundary eigenvalue identity symbolically; it also checks a grid of parameters and both sides of the phase boundaries numerically. These are checks of the proof algebra, not a replacement for the analytic spectral argument.

## Relationship to prior work

Shehu (2026, arXiv:2609.18373) proves the sharp **constant-step** one-call reflected-splitting threshold \(t=1/2\) on the same matched-skew inclusion and a more general constant-step skew phase diagram. Setting \(a=b=t\) recovers that boundary in both formulas, but constant-step results do not distinguish the two variable-step conventions. Muñoz García and Roldán (2026, arXiv:2607.20113, equations (3.5) and (4.1)) explicitly use the previous-step coefficient on the stored gradient difference and analyze an adaptive linesearch rather than arbitrary prescribed two-period Floquet spectra. Ou, Themelis and Latafat (2026, arXiv:2609.15936) study an adaptive reflected method under the additional requirement that the backward operator be a convex subdifferential, which excludes the nonzero skew \(A=LJ\) used here. The monodromy distinction and paired sharp algebraic thresholds above are the specific addition; Schur–Cohn itself is classical.

## Limitations

The full result is for a single two-dimensional linear, maximally monotone skew inclusion and prescribed positive two-period steps in exact arithmetic. It does not imply corresponding uniform bounds for arbitrary operators, longer step cycles, arbitrary adaptive control, or finite precision. Existing general variable-step convergence results may cover subsets of the history-stable region but do not by themselves yield this exact phase diagram. Specialized older matrix-polynomial or time-periodic splitting literature may contain equivalent formulations not identified by the searches. The work has undergone self-review, not independent validation.

## References

1. Y. Shehu, *The sharp step-size constant for one-call reflection splittings on monotone inclusions* (2026), arXiv:2609.18373, https://arxiv.org/abs/2609.18373 (first public September 16, 2026).
2. F. Muñoz García and F. Roldán, *Forward-Reflected-Backward algorithm with Linesearch* (2026), arXiv:2607.20113, https://arxiv.org/abs/2607.20113 (first public July 22, 2026).
3. H. Ou, A. Themelis, and P. Latafat, *An Adaptive Linesearch-free Method for Monotone Variational Inequalities under Local Lipschitz Continuity* (2026), arXiv:2609.15936, https://arxiv.org/abs/2609.15936 (first public September 14, 2026).
4. Y. Malitsky and M. K. Tam, *A forward-backward splitting method for monotone inclusions without cocoercivity* (2020), SIAM J. Optim., arXiv:1808.04162, https://arxiv.org/abs/1808.04162.

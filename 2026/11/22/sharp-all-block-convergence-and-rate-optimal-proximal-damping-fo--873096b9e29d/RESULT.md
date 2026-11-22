# Sharp all-block convergence and rate-optimal proximal damping for parallel quadratic ADMM

## Finding

For every integer \(m\ge2\), the unrelaxed, fixed-penalty proximal **Jacobi** augmented-Lagrangian iteration on the homogeneous strongly convex quadratic equality problem specified below converges to its unique primal-dual solution from **every** initial state exactly when
\[
 s>\frac{3m-6}{4}.
\]
Its unique worst-case asymptotic spectral-rate-optimal nonnegative common proximal coefficient is
\[
 \boxed{s_m^*=\frac{3m-10+\sqrt{9m^2+4m+4}}{8}},
 \qquad \boxed{\rho_m^*=\frac{s_m^*+1}{s_m^*+2}}.
\]
For every \(m\ge2\), \((3m-6)/4<s_m^*<m-1\), and \(\rho_m^*<m/(m+1)\), the rate of the classical globally sufficient choice \(s=m-1\). In the many-block limit, \(s_m^*=3m/4-7/6+O(m^{-1})\) and \(\rho_m^*=1-4/(3m)+O(m^{-2})\); the sufficient choice has rate \(1-1/m+O(m^{-2})\). Thus, on this benchmark, the sharp leading asymptotic spectral gap is larger by a factor \(4/3\).

## Assumptions and scope

Let \(m\in\{2,3,\ldots\}\), \(x\in\mathbb R^m\), and solve the equality-constrained problem
\[
 \min_{x\in\mathbb R^m}\ \frac12\sum_{i=1}^m x_i^2\quad\text{subject to}\quad\sum_{i=1}^m x_i=0.
\]
The unique primal optimum is zero; the unique equality multiplier is zero. Set augmented-Lagrangian penalty to one, choose fixed common proximal coefficient \(s\ge0\), and use the **plus** dual-sign convention. Given arbitrary \((x^k,\lambda_k)\in\mathbb R^m\times\mathbb R\), each block independently minimizes
\[
 x_i^{k+1}=\mathop{\rm argmin}_{z\in\mathbb R}
 \left\{\frac12 z^2+\lambda_k(z+\sum_{j\ne i}x_j^k)
 +\frac12(z+\sum_{j\ne i}x_j^k)^2+\frac{s}{2}(z-x_i^k)^2\right\},
\]
using only the previous state; then update \(\lambda_{k+1}=\lambda_k+\sum_i x_i^{k+1}\). The block minimizers are unique for every \(s\ge0\). This is a nonadaptive, unrelaxed exact-solve parallel baseline, **not** the adaptive, inexact or safeguard-controlled method of Maia–Monteiro–Silva. The condition applies to convergence from every primal-dual initialization; the rate means the spectral radius of the complete linear iteration, not a Euclidean one-step contraction or uniform time-to-accuracy estimate.

## Proof

**Exact diagonalization.** Put \(S_k=\sum_i x_i^k\), \(D=s+2\), and \(\beta=(s+1)/D\). Differentiating each strictly convex block objective gives
\[
 x_i^{k+1}=\frac{(s+1)x_i^k-S_k-\lambda_k}{D}.
\]
The \(m-1\) independent zero-sum disagreements \(x_i^k-S_k/m\) are multiplied by \(\beta\). The remaining sum/dual pair evolves under
\[
 \begin{pmatrix}S_{k+1}\\\lambda_{k+1}\end{pmatrix}
 =M_{m,s}\begin{pmatrix}S_k\\\lambda_k\end{pmatrix},\qquad
 M_{m,s}=\frac1D\begin{pmatrix}s+1-m&-m\\s+1-m&s+2-m\end{pmatrix}.
\]
Its characteristic polynomial is \(P(z)=z^2-tz+q\), with
\[
 t=\frac{2s+3-2m}{D},\qquad q=\frac{s+1-m}{D}.
\]
Thus the complete spectrum comprises \(\beta\) with multiplicity \(m-1\) and both roots of \(P\).

**Sharp convergence.** The second-degree Schur (Jury) criteria for both roots of a real monic quadratic to lie strictly in the unit disk are \(1-q>0\), \(1-t+q>0\), and \(1+t+q>0\). Here they equal, respectively,
\[
 \frac{m+1}{D},\qquad \frac{m}{D},\qquad\frac{4s+6-3m}{D}.
\]
Since \(0<\beta<1\), all eigenvalues are strictly inside the disk iff \(s>(3m-6)/4\). At equality \(P(-1)=0\) gives a nondecaying \(-1\) mode (and below it a real root less than \(-1\)), proving necessity from an initial state in that eigenmode. Strict spectral containment proves convergence for every initialization, even if a repeated eigenvalue produces a Jordan block.

**Unique optimal parameter.** First take \(0\le s<m-1\); then \(q<0\), so the roots \(\lambda_-<0<\lambda_+\) are real and distinct. Direct substitution yields
\[
 P(\beta)=\frac{ms}{D^2}\ge0,
\]
so \(\lambda_+\le\beta\). Moreover, both \(t'=(2m+1)/D^2\) and \(q'=(m+1)/D^2\) are positive. Implicit differentiation of \(P(\lambda_-)=0\) gives
\[
 \lambda_-'=\frac{t'\lambda_--q'}{2\lambda_--t}>0,
\]
because numerator and denominator are strictly negative. Consequently the spectral radius is \(\max\{\beta,-\lambda_-\}\), the maximum of a strictly increasing and strictly decreasing function. At \(s=0\), \(\lambda_-=1-m\) and \(\beta=1/2\); as \(s\uparrow m-1\), \(\lambda_-\to0\). There is exactly one crossing, characterized by \(P(-\beta)=0\). Multiplying by \(D^2\) gives
\[
 4s^2+(10-3m)s+6-4m=0.
\]
Its unique positive root is the displayed \(s_m^*\), and the crossing minimum is \(\rho_m^*=\beta(s_m^*)\).

For \(s\ge m-1\), \(q\ge0\) and \(t>0\). If the roots of \(P\) are nonreal, their moduli equal \(\sqrt q<\beta\), as
\[
 \beta^2-q=\frac{(m-1)s+2m-1}{D^2}>0.
\]
If they are real, both are nonnegative, and \(P(\beta)>0\) together with \(\beta-t/2=(2m-1)/(2D)>0\) implies their maximum is below \(\beta\). Thus the whole spectral radius is simply \(\beta\) for \(s\ge m-1\), and it strictly increases. The crossing above is therefore the unique global minimizer on \(s\ge0\). Since \(s_m^*<m-1\) and \(\beta\) increases, \(\rho_m^*<\beta(m-1)=m/(m+1)\). At the crossing the two limiting modes are \(+\beta\) (disagreement) and \(-\beta\) (sum/dual); the optimum balances modes of opposite signs, not a repeated-root critical damping condition. The crossing lies above the strict stability boundary because at that boundary \(\lambda_-=-1\), while \(\beta<1\).

**Large-block expansion.** Expand \(\sqrt{9m^2+4m+4}=3m+2/3+O(m^{-1})\). This yields \(s_m^*=3m/4-7/6+O(m^{-1})\) and \(\rho_m^*=1-1/(s_m^*+2)=1-4/(3m)+O(m^{-2})\). The standard sufficient choice has \(\beta(m-1)=m/(m+1)=1-1/m+O(m^{-2})\).

## Verification

Run `python3 verify.py` using the files in this package. It independently constructs exact rational iteration matrices, checks the decomposition, characteristic polynomial, Schur quantities, both polynomial substitutions, and direct parallel block updates on multiple finite rational instances. It also evaluates the claimed optimizer and spectral-radius ordering for multiple dimensions, tests the boundary eigenvalue and large-block trend. Finite tests support, but do not substitute for, the symbolic proof above.

## Relationship to prior work

Maia, Monteiro, and Silva (arXiv:2611.00570, first public 31 October 2026) develop an adaptive Jacobi-type proximal ADMM for a broad nonconvex composite class, including inexact subproblem solves and a safeguarded multiplier/penalty update. Their algorithm is materially different from the fixed, unrelaxed, exact-solve baseline here; their broad iteration-complexity result does not give this specialized rate-optimal spectral coefficient. He, Xu, and Yuan (Optimization Online manuscript 4142, 2013, equation (1.6), Section 3 and conclusions) study exactly the underlying classical proximal Jacobi decomposition and prove the general convex sufficient condition \(s\ge m-1\). They explicitly identify lower coefficients as an open efficiency issue but do not determine the present sharp quadratic threshold or unique all-block optimum. He, Hou, and Yuan (Optimization Online manuscript 3894, 2014 revision) study an under-relaxed full-Jacobian correction, not the unrelaxed proximal family here. Published results on cyclic (sequential) quadratic ADMM optimize a different iteration matrix. This is a restricted sharp spectral statement, not a claim that the classical method or general proximal idea is new.

## Limitations

All coefficients assume unit objective curvature, unit penalty, identical scalar blocks, a single sum equality, and common fixed proximal regularization. No sharp characterization is asserted for heterogeneous blocks, nonlinear/nonconvex objectives, multiple constraint rows, arbitrary penalties without rescaling, the actual adaptive method, finite-horizon transient errors, or nonlinear identification. The usual generic proximal parameter bound remains valuable for broader problems; this scalar example cannot refute the general sufficiency theorem. The optimal parameter minimizes spectral radius and need not minimize a particular finite-iteration loss. Historical priority beyond the inspected sources is not independently certified; full external mathematical audit has not occurred.

## References

1. L. F. Maia, R. D. C. Monteiro, G. N. Silva, *A Parallel Adaptive Proximal ADMM for Linearly Constrained Separable Composite Optimization Problems*, arXiv:2611.00570, version 1 released 31 October 2026, https://arxiv.org/abs/2611.00570 .
2. B. He, H.-K. Xu, X. Yuan, *On the Proximal Jacobian Decomposition of ALM for Multiple-block Separable Convex Minimization Problems and its Relationship to ADMM*, manuscript dated 5 December 2013, https://optimization-online.org/wp-content/uploads/2013/11/4142.pdf .
3. B. He, L. Hou, X. Yuan, *On full Jacobian decomposition of the augmented Lagrangian method for separable convex programming*, manuscript revised 21 March 2014, https://optimization-online.org/wp-content/uploads/2013/05/3894.pdf .

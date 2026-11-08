# Exact no-amplification window for an inhibitory feedback ring

## Finding

Let \(n\ge3\) and let \(a,\mu>0\). Consider a directed chain of \(n\) interacting populations, with equal positive feed-forward interaction strength \(a\), equal local regulation \(\mu\), and one inhibitory feedback interaction of strength \(b\ge0\) from the last population to the first. Its real community matrix is
\[
J_n(b)=-\mu I_n+a\sum_{j=1}^{n-1}e_{j+1}e_j^{\mathsf T}-b e_1e_n^{\mathsf T}.
\]
For \(t\ge0\), let \(T_b(t)=e^{tJ_n(b)}\). We call the system **nonamplifying** when \(\|T_b(t)\|_2\le1\) for every \(t\ge0\). Define \(\theta=\pi/n\) and \(c_n=\cos\theta\).

**Theorem (exact feedback window and unique reactivity optimum).**

1. For every \(b\ge0\), the largest instantaneous Euclidean growth rate
\[
\omega_n(b)=\lambda_{\max}\!\left(\frac{J_n(b)+J_n(b)^{\mathsf T}}2\right)
\]
satisfies \(\omega_n(b)\ge-\mu+a c_n\), with equality **if and only if** \(b=a\). More quantitatively,
\[
\omega_n(b)\ge-\mu+ac_n+
\begin{cases}
\dfrac{(b-a)(1+c_n)}n,& b\ge a,\\
\dfrac{(a-b)(1-c_n)}n,&0\le b\le a.
\end{cases}
\]
2. If \(\mu<a c_n\), no nonnegative feedback strength is nonamplifying. If \(\mu=a c_n\), precisely \(b=a\) is nonamplifying (with a neutral mode). If \(\mu>a c_n\), put \(z=\mu/a\), let \(U_k\) be the Chebyshev polynomial of the second kind normalized by \(U_0(z)=1\), \(U_1(z)=2z\), \(U_{k+1}(z)=2zU_k(z)-U_{k-1}(z)\), and set
\[
b_-(z)=a\max\!\left\{0,\frac{1-U_{n-1}(z)}{U_{n-2}(z)}\right\},\qquad
b_+(z)=a\frac{1+U_{n-1}(z)}{U_{n-2}(z)}.
\]
Then \(J_n(b)\) is nonamplifying **if and only if** \(b_-(z)\le b\le b_+(z)\). Both denominators are positive in this stated range.
3. For every damping rate in the nonempty interval
\[
a\cos(\pi/n)<\mu<a\cos\bigl(\pi/(n+1)\bigr),
\]
the open chain \(b=0\) is asymptotically stable but amplifies some perturbations at short times. In contrast, the inhibitory closure \(b=a\) is asymptotically stable and does **not** amplify any perturbation at any time. Indeed the nonamplifying feedback interval satisfies \(0<b_-<a<b_+\) in this damping regime.

The stability threshold of the closed ring itself is independently explicit: when \(b>0\), its spectral abscissa is
\[
\alpha_n(b)=-\mu+(a^{n-1}b)^{1/n}\cos(\pi/n).
\]
This spectral condition and the no-amplification condition answer different questions.

For example, with \(n=3\), \(a=1\) and \(\mu=3/5\), the open chain has eigenvalues \(-3/5\) but strictly amplifies some perturbations. The exact no-amplification interval after adding inhibitory feedback is \(7/15\le b\le6/5\), which includes the unique reactivity minimizer \(b=1\).

## Assumptions and scope

The result concerns the Euclidean norm of *linear deviations* from an equilibrium; population variables need not remain positive under arbitrary signed infinitesimal deviations. Equal damping and equal feed-forward strengths, a single negative closing interaction, and a fixed \(n\ge3\) are essential hypotheses. Other interaction architectures, nonlinear post-perturbation effects, and empirical population outcomes are not asserted.

## Proof

Write \(H_n(b)=(J_n(b)+J_n(b)^{\mathsf T})/2\). For every real solution \(x'(t)=J_n(b)x(t)\),
\[
\frac{d}{dt}\|x(t)\|_2^2=2x(t)^{\mathsf T}H_n(b)x(t).
\]
Consequently, \(H_n(b)\preceq0\) implies contractivity for all times. Conversely, if \(H_n(b)\) has a positive eigenvalue, its eigenvector strictly gains squared norm for sufficiently small positive time. Thus nonamplification is equivalent to \(\omega_n(b)\le0\), including at the semidefinite boundary.

**Optimal feedback.** At \(b=a\), the off-diagonal part of \(J_n(a)\) is \(aQ\), where \(Q\) is a signed cyclic permutation satisfying \(Q^n=-I_n\) and \(Q^{\mathsf T}Q=I_n\). Therefore \(J_n(a)\) is normal. Its eigenvalues are \(-\mu+a\exp(i(2k+1)\pi/n)\) for \(0\le k<n\); hence \(\omega_n(a)=-\mu+a c_n\). The top eigenspace of \(H_n(a)\) is two-dimensional, spanned by the orthonormal vectors with entries
\[
u_j=\sqrt{2/n}\cos((j-1)\theta),\qquad
v_j=\sqrt{2/n}\sin((j-1)\theta).
\]
The perturbation \(H_n(b)-H_n(a)=(b-a)B\), with \(B=-(e_1e_n^{\mathsf T}+e_ne_1^{\mathsf T})/2\), compresses to this top eigenspace as
\[
\begin{pmatrix}u^{\mathsf T}Bu&u^{\mathsf T}Bv\\v^{\mathsf T}Bu&v^{\mathsf T}Bv\end{pmatrix}
=\frac1n\begin{pmatrix}2c_n&-\sin\theta\\-\sin\theta&0\end{pmatrix}.
\]
Its eigenvalues are \((c_n+1)/n\) and \((c_n-1)/n\), one positive and one negative. The variational principle restricted to this eigenspace gives the two stated lower bounds and proves the unique minimizer \(b=a\).

**Exact feedback window.** If \(\mu\le ac_n\), the preceding minimum proves the first two cases, including uniqueness at equality. Assume \(z=\mu/a>c_n\). The interior principal block of \(-H_n(b)\), indexed by vertices \(2,\ldots,n-1\), is the positive-definite tridiagonal path matrix \(K=\mu I_{n-2}-(a/2)A_{P_{n-2}}\), because its largest path-adjacency eigenvalue after scaling is \(a\cos(\pi/(n-1))<ac_n<\mu\). The standard tridiagonal determinant recurrence gives
\[
(K^{-1})_{11}=\frac2a\frac{U_{n-3}(z)}{U_{n-2}(z)},\qquad
(K^{-1})_{1,n-2}=\frac2a\frac1{U_{n-2}(z)}.
\]
For \(n=3\), these are the same single diagonal entry and both formulas hold with \(U_0=1\). Taking the Schur complement of \(K\) in \(-H_n(b)\) leaves a symmetric matrix with equal diagonal entries
\[
\frac a2\frac{U_{n-1}(z)}{U_{n-2}(z)}
\]
and off-diagonal entry
\[
\frac a2\left(\frac ba-\frac1{U_{n-2}(z)}\right).
\]
A symmetric matrix with equal nonnegative diagonals is positive semidefinite exactly when the absolute value of its off-diagonal does not exceed that diagonal. This yields precisely \(b_-(z)\le b\le b_+(z)\). Positivity of \(U_{n-2}(z)\) follows from the spectral positivity of \(K\). The polynomial \(U_{n-1}(z)\) increases strictly from zero as \(z\) rises above its largest zero \(c_n\), and \(U_{n-1}(\cos(\pi/(n+1)))=1\). Hence the lower endpoint is strictly positive in the damping interval of item 3.

**Asymptotic stability and the rescue.** The characteristic equation is \((\lambda+\mu)^n=-a^{n-1}b\). It gives the claimed spectral abscissa for positive \(b\), while for \(b=0\) every eigenvalue equals \(-\mu\). The path symmetric part at \(b=0\) has top eigenvalue \(-\mu+a\cos(\pi/(n+1))\); thus the open chain is stable but reactive in the claimed damping interval. The closed balanced system is normal and has spectral abscissa \(-\mu+ac_n<0\); hence it is stable and all-time contractive. The window formula implies a strict interval containing \(a\), completing the proof.

## Verification

Run `python verify.py` with Python 3 and NumPy. The checker independently tests exact rational principal-minor positive-semidefinite decisions (including both closed-form endpoints) for six different ring sizes, checks the endpoint determinants exactly, and compares the interval and spectral formulas against direct eigensolvers for sizes \(3\) through \(16\). The finite tests corroborate calculations and do not substitute for the all-order argument above.

## Relationship to prior work

Caravelli and Staniczenko (2015) develop the ecological numerical-abscissa/reactivity framework and discuss transient amplification for several community-matrix ensembles. Arcak and Sontag (2006) give the classical secant condition and diagonal-stability theorem for negative cyclic feedback, including the equal-diagonal Hurwitz boundary. Their Lyapunov metric is allowed to be diagonal and state dependent; this does not give the stated fixed-Euclidean-norm contractivity interval, the unique minimizer of instantaneous Euclidean growth as the closing link varies, or the explicit open-chain-to-closed-ring rescue window. The stability formula alone is prior cyclic-feedback mathematics and is included for comparison, not claimed as an independent new theorem. Snyder (2010) provides general reactivity bounds, but full-text priority comparison remained unavailable.

## Limitations

This is an exact theoretical property of a deliberately symmetric linear chain, not a claim of empirical ecological robustness. The chosen Euclidean metric has biological meaning only if the coordinates share compatible units and scaling. Other weighted metrics yield different feedback intervals. The full Snyder (2010) article could not be inspected; adjacent literature may contain equivalent fixed-metric inequalities, so historical priority remains provisional. No expert or independent validation has been performed.

## References

1. F. Caravelli and P. P. A. Staniczenko, *Bounds on transient instability for complex ecosystems*, arXiv:1506.06971, first public preprint 2015-06-23. https://arxiv.org/abs/1506.06971
2. M. Arcak and E. D. Sontag, *Diagonal stability of a class of cyclic systems and its connection with the secant criterion*, Automatica 42 (2006), 1531–1537, doi:10.1016/j.automatica.2006.04.009. Full text: https://mathweb.ucsd.edu/~toal/READ07/diagonal_stability.pdf
3. R. E. Snyder, *What makes ecological systems reactive?*, Theoretical Population Biology 77 (2010), 243–249, doi:10.1016/j.tpb.2010.03.004. Full text not inspected.

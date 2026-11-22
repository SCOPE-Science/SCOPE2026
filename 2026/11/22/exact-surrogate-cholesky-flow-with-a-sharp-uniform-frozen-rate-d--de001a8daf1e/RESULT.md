# Exact surrogate Cholesky flow with a sharp uniform frozen-rate deficit

## Finding

A finite-time pivot-free Cholesky scheme motivated by a scalar triangular surrogate gradient flow can use an **exact closed-form off-diagonal coefficient** rather than a frozen-terminal-rate expression. The correction has a sharp universal multiplicative comparison, and its rank-one updates preserve the positive-semidefinite Schur-complement invariant.

Write
\[
\Phi(x)=\int_0^1 e^{-xu}\,du=\begin{cases}(1-e^{-x})/x,&x>0,\\1,&x=0,\end{cases}\qquad q=2(1-e^{-1/2}).
\]
For every \(\alpha\ge0\), \(s\ge\alpha\) with \(s>0\), and \(T>0\), let \(\ell\) be the positive logistic solution of \(\ell'=\ell(\alpha-\ell^2)\), \(\ell(0)=\sqrt{s}\). Then the unique solution of
\[
 g'=\ell(1-\ell g),\qquad g(0)=0
\]
is
\[
 g_{\mathrm{exact}}(T)=T\ell(T)\Phi(\alpha T).
\]
For the alternative terminal-frozen coefficient \(g_{\mathrm{fr}}(T)=T\ell(T)\Phi(T\ell(T)^2)\), one has the **sharp universal bound**
\[
 \boxed{q\le \frac{g_{\mathrm{fr}}(T)}{g_{\mathrm{exact}}(T)}\le1},
 \qquad q=0.786938680574733\ldots .
\]
The infimum \(q\) is approached even with \(\alpha>0\). Thus the relative coefficient underestimation is at most \(1-q=0.213061319425267\ldots\). For any nonzero residual vector, the corresponding rank-one subtraction is smaller by at most the sharp relative fraction \(1-q^2=0.380727513015298\ldots\) compared with the corrected subtraction.

## Assumptions and scope

All assertions are in exact real arithmetic. Fix a symmetric positive-semidefinite matrix of arbitrary finite order. At each elimination step, write the current positive-semidefinite trailing matrix as
\[
 S=\begin{pmatrix}\alpha&r^{\mathsf T}\\r&B\end{pmatrix}\succeq0.
\]
Use the initial squared diagonal \(s=\max\{1,\alpha\}\), or more generally any \(s\ge\alpha\) with \(s>0\). For one common finite horizon \(T>0\), define the diagonal output \(\ell(T)\) and the off-diagonal vector \(g_{\mathrm{exact}}(T)r\), and recurse on \(B-g_{\mathrm{exact}}(T)^2rr^{\mathsf T}\). No assertion is made for indefinite inputs or for numerical roundoff.

## Proof

**1. Exact flow.** Put \(p(t)=\ell(t)^2\). Its scalar Riccati equation is \(p'=2p(\alpha-p)\), and separation, with the continuous \(\alpha=0\) interpretation, gives
\[
 p(t)^{-1}=s^{-1}e^{-2\alpha t}+2t\Phi(2\alpha t).
\]
When \(\alpha>0\), differentiating \(\ell(t)(1-e^{-\alpha t})/\alpha\), using \(\ell'/\ell=\alpha-p\), yields \(\ell-pg\) with zero initial value. When \(\alpha=0\), the same verification applies to \(g=t\ell(t)\). Uniqueness of the scalar linear ODE proves the stated exact formula.

**2. Uniform ratio and sharpness.** Since \(s\ge\alpha\), the logistic formula implies \(p(t)\ge\alpha\). For \(\alpha>0\), it also yields
\[
 p(t)\le\frac{\alpha}{1-e^{-2\alpha t}}
 =\alpha+\frac{\alpha}{e^{2\alpha t}-1}\le \alpha+\frac1{2t}.
\]
The same upper bound follows from \(p(t)=s/(1+2st)\) when \(\alpha=0\). Consequently, \(\alpha t\le p(t)t\le\alpha t+1/2\). The positive function \(\Phi\) is strictly decreasing. Moreover, \(\log\Phi\) is strictly convex, since its second derivative is the strictly positive variance of \(u\in[0,1]\) under the probability density proportional to \(e^{-xu}\). Therefore \(\Phi(x+1/2)/\Phi(x)\) is increasing for \(x\ge0\). Setting \(x=\alpha t\) proves
\[
 \frac{\Phi(pt)}{\Phi(\alpha t)}\ge
 \frac{\Phi(\alpha t+1/2)}{\Phi(\alpha t)}\ge\Phi(1/2)=q.
\]
For sharpness with a strictly positive pivot, set \(t=T\to\infty\), \(\alpha=T^{-2}\), \(s=1\). Then \(\alpha T\to0\) and \(p(T)T\to1/2\), giving ratio \(q\). Both the coefficient and squared-update bounds are therefore optimal. The rank-one relative bound is also approached on genuine nonzero updates of positive-semidefinite matrices \(\begin{psmallmatrix}\alpha&\sqrt\alpha\\\sqrt\alpha&1\end{psmallmatrix}\).

**3. Positive-semidefinite recursion.** If \(\alpha>0\), the ordinary Schur complement \(B-\alpha^{-1}rr^{\mathsf T}\) is positive semidefinite. The bound for \(p\) above proves
\[
 \alpha g_{\mathrm{exact}}(T)^2
 =\frac{p(T)}{\alpha}(1-e^{-\alpha T})^2
 \le\frac{1-e^{-\alpha T}}{1+e^{-\alpha T}}<1.
\]
Hence \(B-g_{\mathrm{exact}}(T)^2rr^{\mathsf T}\) is the ordinary positive-semidefinite Schur complement plus a nonnegative rank-one term. If \(\alpha=0\), positive semidefiniteness of \(S\) forces \(r=0\), so the recursive trailing matrix remains \(B\succeq0\). Induction proves that every pivot and every coefficient in the corrected finite-horizon recursion is well defined and every trailing matrix stays positive semidefinite.

## Verification

Run `python verify.py` using the Python 3 standard library. It tests 452 finite numerical conditions, including the exact formula against independently time-stepped fourth-order Runge–Kutta solutions, uniform ratio inequalities, the sharpness sequence and positive-semidefinite trailing updates on deterministic positive-semidefinite matrices. The checker returned `VERIFY_OK 452 finite_checks`. The all-parameter comparison and indefinite-stage recursion are established by the analytic proof above, not by finite testing.

The corrected off-diagonal evaluation \(T\ell\Phi(\alpha T)\) uses one scalar exponential-related evaluation, just as the terminal-frozen version does; its outer matrix elimination remains cubic in dimension. This is an arithmetic-complexity statement, not a runtime or floating-point stability claim.

## Relationship to prior work

Manavalan and Schönlieb (2026) introduce the finite-time pivot-free Cholesky scheme, its logistic diagonal and the terminal-frozen coefficient \(T\ell\Phi(T\ell^2)\), and establish well-definedness for that numerical recursion. The present result concerns the distinct exactly integrated off-diagonal surrogate ODE, a sharp uniform comparison and a positive-semidefinite-compatible replacement. Familiar Schur-complement positivity is used as a proof component, not claimed as independently new. Published work on randomized pivot selection, incomplete Cholesky and related matrix integrators addresses different recurrence or perturbation models; no equivalent universal coefficient comparison was identified in the sources inspected.

## Limitations

The corrected scalar coefficient solves the *surrogate* decoupled ODE, not the original coupled flow. The comparison does not prove smaller final matrix reconstruction error, faster execution, backward stability in floating-point arithmetic or superiority to pivoted Cholesky. The worst-case multiplicative coefficient gap is an infimum approached in a singular perturbation regime. Earlier unindexed equivalent analysis cannot be ruled out without further expert literature review.

## References

- R. Manavalan and C. B. Schönlieb, *Finite-time Cholesky factorization*, arXiv:2611.09706, first public November 6, 2026; version 2 November 9, 2026, especially Section 2.2 and Algorithms 1–2, https://arxiv.org/html/2611.09706v2.
- Standard Schur-complement criterion for positive-semidefinite block matrices, as used in the cited paper's Section 2.3.

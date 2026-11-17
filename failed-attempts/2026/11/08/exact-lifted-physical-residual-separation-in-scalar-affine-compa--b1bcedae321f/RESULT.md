# Exact lifted–physical residual separation in scalar affine companion GMRES

## Finding

Consider the scalar parameterized equation \(A(s)x=1\), where \(A(t)=1+ct\), \(c\geq 0\), and the target parameter \(s>0\). Apply exact-arithmetic, zero-start, right-preconditioned companion infinite GMRES, without parameter rebasing, for \(m\geq1\) Krylov iterations. Write \(R_m\) for the Euclidean residual minimized in the companion linearization, and \(\widetilde{x}_m\) for the recovered approximation to the *original scalar equation*.

For every positive integer \(m\),

\[
R_m^2=\frac{s^{2m}}{s^{2m}+s^{2m-2}+(1+cs)^2\displaystyle\sum_{j=0}^{m-2}s^{2j}},\qquad
1-(1+cs)\widetilde{x}_m=\left(1-\frac cs\right)R_m^2.
\]

The empty sum at \(m=1\) is zero. In particular, for every \(s>0\), choosing \(c=s\) makes **every recovered iterate exact**, even the first one, while \(R_m>0\) for every finite \(m\). More sharply, for every fixed \(s>1\),

\[
\lim_{m\to\infty}R_m^2=
\left(1+s^{-2}+\frac{(1+cs)^2}{s^2(s^2-1)}\right)^{-1}>0.
\]

At \(c=s>1\), this floor simplifies to \((s^2-1)/(2(s^2+1))\); its square root tends to \(1/\sqrt2\) as \(s\to\infty\), although the physical residual is identically zero. Conversely, if \(c\ne s\), the physical residual also has a strictly positive limit for every fixed \(s>1\). The transition in the lifted residual is exact: at \(s=1\), \(R_m^2=[2+(1+c)^2(m-1)]^{-1}\); when \(0<s<1\), \(R_m^2\sim (1-s^2)s^{2m}/(1+cs)^2\).

## Assumptions and scope

The scalar right-hand side is one; the positive affine coefficient \(1+cs\) is nonsingular at the target. The companion equation and recovered approximation are those obtained by right-preconditioning the degree-\(q\) Taylor companion with its constant coefficient matrix, where \(q\ge m\). Since the original matrix function is exactly affine, these \(m\)-step quantities are independent of \(q\). The standard Euclidean least-squares norm is used in the enlarged companion space; there is no residual rescaling, early stopping, truncation during a step, rounding error, inexact preconditioning, restart, or implicit rebasing. The parameter \(s\) is a real positive *expansion coordinate*, not an arbitrary norm-invariant physical parameter.

## Proof

Let \(e_j\) be standard coordinate vectors, numbered from one. In an enlarged companion with at least \(m+1\) coordinates, the affine Taylor coefficient matrices give

\[
L_0=I+c e_1e_2^{\mathsf T},\qquad
L_0^{-1}=I-c e_1e_2^{\mathsf T},\qquad
T=L_1L_0^{-1},
\]

where \(L_1e_j=e_{j+1}\) for all active lower-shift coordinates. Thus \(Te_1=e_2\), \(Te_2=-ce_2+e_3\), and \(Te_j=e_{j+1}\) for \(j\ge3\). Induction shows that the first \(m\) Krylov vectors span exactly \(e_1,\dots,e_m\): the newest nonzero coordinate in \(T^{j-1}e_1\) is at \(j\) with coefficient one. This also rules out an early Krylov breakdown.

For \(v=\sum_{j=1}^m v_je_j\), zero-start GMRES minimizes \(\|e_1-B_mv\|_2\), where the \((m+1)\)-by-\(m\) matrix \(B_m=(I-sT)[e_1,\ldots,e_m]\) has columns

\[
b_1=e_1-se_2,\qquad b_2=(1+cs)e_2-se_3,\qquad b_j=e_j-se_{j+1}\quad (3\le j\le m).
\]

The second and later columns are present only when their indices are at most \(m\). The columns are independent because each has a new last nonzero coordinate with coefficient \(-s\). Their orthogonal complement is therefore one-dimensional. A spanning vector \(w\) has \(w_1=s\), \(w_2=1\), and, for \(3\le j\le m+1\), \(w_j=(1+cs)/s^{j-2}\). Indeed, the equations \(b_j^{\mathsf T}w=0\) are exactly \(w_1=sw_2\), \((1+cs)w_2=sw_3\), and \(w_j=sw_{j+1}\) for \(j\ge3\). The last two relations are simply absent at \(m=1\).

The least-squares residual \(r=e_1-B_mv\) is the orthogonal projection of \(e_1\) onto \(\operatorname{span}(w)\). Consequently,

\[
R_m^2=\|r\|_2^2=\frac{w_1^2}{\|w\|_2^2}
=\frac{s^2}{s^2+1+(1+cs)^2\sum_{j=1}^{m-1}s^{-2j}},
\]

which is the stated finite-sum formula after multiplying numerator and denominator by \(s^{2m-2}\). Because \(r\) is the projection, its first two coordinates satisfy \(r_1=R_m^2\) and \(r_2=R_m^2/s\).

The recovered original solution is the first coordinate of \(L_0^{-1}v\), namely \(\widetilde{x}_m=v_1-cv_2\), with \(v_2=0\) by convention for \(m=1\). From the first two rows of \(r=e_1-B_mv\),

\[
r_1=1-v_1,\qquad r_2=sv_1-(1+cs)v_2.
\]

Here the same second-row identity holds at \(m=1\) with \(v_2=0\). Eliminating the coefficients gives

\[
(1+cs)\widetilde{x}_m=v_1+\frac cs r_2
=1-R_m^2+\frac csR_m^2,
\]

so \(1-(1+cs)\widetilde{x}_m=(1-c/s)R_m^2\). All denominators are positive under the hypotheses. Thus the original residual vanishes for every \(m\) precisely when \(c=s\), since \(R_m>0\) for every finite \(m\).

Finally, summing the geometric series in the expression for \(R_m^2\) proves the three regimes. For \(s>1\), divide numerator and denominator by \(s^{2m}\) and pass to the limit; for \(s=1\), evaluate the sum exactly; for \(0<s<1\), divide by the limiting geometric denominator. At \(c=s>1\), simplifying the limit yields \((s^2-1)/(2(s^2+1))\). Since this limit is positive, the physical residual has a nonzero limit whenever \(c\ne s\).

## Verification

The standalone `verify.py` independently constructs the finite companion operator and computes each least-squares minimizer with exact rational arithmetic, without using the derived projection formula in the minimization. It checks the finite-sum squared residual, the recovered physical residual identity, and the scalar limiting simplification for \(175\) rational parameter/dimension triples. Run `python verify.py` in an environment with SymPy. The finite tests do not establish the all-iteration theorem; that follows from the orthogonal-complement argument above.

## Relationship to prior work

Gao and Jiang's Toeplitz infinite-GMRES analysis defines the right-preconditioned companion residual, the recovered solution, and a strictly positive lower bound for the *lifted* residual outside the normalized unit disk. The exact scalar affine formulas above distinguish that lifted residual from the residual of the recovered original equation. The latter can vanish identically while the former obeys a nonvanishing lower bound; this distinction is not a contradiction because the two norms measure different equations and different components. Jarlebring and Correnty's original infinite-GMRES construction and Correnty, Jarlebring and Soodhalter's preconditioned variant provide the companion-method background; they do not supply the stated affine physical-residual identity or its exceptional cancellation in the inspected material.

## Limitations

This is an exact-arithmetic **scalar affine** analysis of unrestarted, non-rebased companion GMRES. It does not establish a corresponding cancellation for general matrix-valued or nonlinear analytic families, and it does not assess floating-point conditioning or the alternative implicitly rebased scheme. The unusual parameter match \(c=s\) is exact and can be fragile; the formulas also quantify its perturbation through \(1-c/s\). Positive lifted residual is not a certificate of poor physical recovery; neither does this scalar example prove that the lifted residual is irrelevant in general.

## References

- W. Gao and F. Jiang, *Toeplitz Infinite GMRES for Parameterized Linear Systems*, arXiv:2610.01740, 2026, sections 2, 3 and 5. https://arxiv.org/abs/2610.01740
- E. Jarlebring and S. Correnty, *Infinite GMRES for Parameterized Linear Systems*, arXiv:2102.04082, 2021; SIAM J. Matrix Anal. Appl. 43 (2022), 1382–1405. https://arxiv.org/abs/2102.04082
- S. Correnty, E. Jarlebring and K. M. Soodhalter, *Preconditioned Infinite GMRES for Parameterized Linear Systems*, arXiv:2206.05153, 2022; SIAM J. Sci. Comput. 45 (2023). https://arxiv.org/abs/2206.05153

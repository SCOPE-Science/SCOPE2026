# Exact Loewner-order frontier for covariance trapezoids in Lyapunov flows

## Finding

Let \(A\in\mathbb R^{n\times n}\) be any real matrix. Consider the linear differential Lyapunov equation with constant symmetric positive-semidefinite input \(Q\),
\[
 \dot X=AX+XA^{\mathsf T}+Q.
\]
For any \(h>0\), the constant-input second-order integrating-factor SSPRK step is
\[
 \mathcal T_h(X)=e^{hA}Xe^{hA^{\mathsf T}}+\frac h2\bigl(Q+e^{hA}Qe^{hA^{\mathsf T}}\bigr),
\]
while the exact step is
\[
 \mathcal E_h(X)=e^{hA}Xe^{hA^{\mathsf T}}+\int_0^h e^{sA}Qe^{sA^{\mathsf T}}\,ds.
\]
The following are equivalent, with no restriction on the dimension or spectrum of \(A\):

**(i)** For every \(h>0\) and every symmetric \(Q\succeq0\), the step is an upper bound in Loewner order: \(\mathcal T_h(X)-\mathcal E_h(X)\succeq0\).

**(ii)** There exist *real* scalars \(a,b\) with
\[
 A^2=aI+bA,\qquad 4a\ge b^2.
\]

It suffices in (i) to test rank-one inputs \(Q=vv^{\mathsf T}\) and arbitrarily small positive steps. Consequently, if \(A\) is Hurwitz, universal one-sided covariance overestimation holds **if and only if** \(A=cI\) for some \(c<0\). Every nonscalar Hurwitz drift has a fixed rank-one \(Q\succeq0\) for which the numerical covariance fails to upper-bound the exact covariance at **every sufficiently small** positive step. For any drift satisfying (ii), the one-sided order extends to all mesh points of repeated constant-step integration from the same initial covariance.

## Assumptions and scope

All matrices and inputs are real, finite dimensional, and evaluated in exact arithmetic; \(n\ge1\). The Loewner inequality applies to symmetric matrices and is independent of the initial \(X\). Here \(A\), \(Q\), and the positive step size remain constant during integration. The method uses exact matrix exponentials. Positive semidefinite output, which holds for arbitrary \(A\) and positive semidefinite \(X,Q\), is different from upper-bounding the exact covariance.

A Hurwitz matrix has all eigenvalues in the strict open left half-plane. A matrix is **nonscalar** if it is not a multiple of the identity.

## Proof

**1. Exact defect and curvature.** Define
\[
 F_Q(s)=e^{sA}Qe^{sA^{\mathsf T}},\qquad
 \Delta_h(A,Q)=\mathcal T_h(X)-\mathcal E_h(X).
\]
Scalar integration by parts, entrywise, yields the exact Peano-kernel identity
\[
 \Delta_h(A,Q)=\frac12\int_0^h s(h-s)F_Q''(s)\,ds.
\]
Direct differentiation gives
\[
 F_Q''(s)=e^{sA}L_A(Q)e^{sA^{\mathsf T}},\qquad
 L_A(Q)=A^2Q+2AQA^{\mathsf T}+Q(A^{\mathsf T})^2.
\]
Therefore \(L_A(Q)\succeq0\) implies \(\Delta_h(A,Q)\succeq0\) for every \(h>0\). Conversely,
\[
 \Delta_h(A,Q)=\frac{h^3}{12}L_A(Q)+O(h^4)
\]
entrywise as \(h\downarrow0\); nonnegativity for every sufficiently small \(h\) implies \(L_A(Q)\succeq0\), because the positive-semidefinite cone is closed. Thus property (i) is equivalent to positivity of \(L_A\) on the positive-semidefinite cone.

**2. The cyclic-degree obstruction.** It is enough to test \(Q=vv^{\mathsf T}\), since every positive-semidefinite \(Q\) is a nonnegative sum of rank-one matrices. Set \(u=Av\), \(w=A^2v\). Then
\[
 L_A(vv^{\mathsf T})=wv^{\mathsf T}+vw^{\mathsf T}+2uu^{\mathsf T}.
\]
If \(w\notin\operatorname{span}\{v,u\}\), choose a vector \(z\perp\operatorname{span}\{v,u\}\) for which \(w^{\mathsf T}z\ne0\). This gives \(z^{\mathsf T}L_A(vv^{\mathsf T})z=0\), yet \(L_A(vv^{\mathsf T})z=v(w^{\mathsf T}z)\ne0\). A positive-semidefinite symmetric matrix cannot have a zero quadratic form at a vector outside its kernel (diagonalize it, or apply its square root). Therefore \(v,Av,A^2v\) are linearly dependent for **every** \(v\).

The elementary maximal-cyclic-vector lemma states that a finite-dimensional linear operator admits a vector whose annihilating polynomial is its minimal polynomial (for example, take a generator of a largest invariant-factor block in rational canonical form). Hence no minimal polynomial of degree three or higher is possible. If it has degree one, \(A=cI\); if it has degree two, there are unique real \(a,b\) with \(A^2=aI+bA\).

**3. Sharp quadratic condition.** For a nonscalar degree-two matrix, choose \(v\) so that \(v\) and \(Av\) are independent. Then \(w=av+bu\) and
\[
 L_A(vv^{\mathsf T})=
 \begin{pmatrix}v&u\end{pmatrix}
 \begin{pmatrix}2a&b\\b&2\end{pmatrix}
 \begin{pmatrix}v&u\end{pmatrix}^{\mathsf T}.
\]
Independence makes positivity equivalent to positivity of the displayed \(2\times2\) matrix, exactly \(4a\ge b^2\) (which also entails \(a\ge0\)). For scalar \(A=cI\) take \(a=c^2\) and \(b=0\). This proves necessity.

Conversely, if \(A^2=aI+bA\), algebraic completion of squares gives, for every symmetric \(Q\succeq0\),
\[
 L_A(Q)=2\left(A+\frac b2 I\right)Q
       \left(A+\frac b2 I\right)^{\mathsf T}
       +\left(2a-\frac{b^2}{2}\right)Q\succeq0.
\]
The Peano identity proves (i), including at equality \(4a=b^2\).

**4. Hurwitz classification and meshwise propagation.** A nonscalar \(A\) satisfying (ii) has a degree-two minimal polynomial whose roots obey \(\lambda^2-b\lambda-a=0\), with \(a\ge0\). If \(a>0\), these roots are real with opposite signs; if \(a=0\), one root is zero. Either case is incompatible with a Hurwitz matrix. A scalar Hurwitz matrix \(cI\), \(c<0\), satisfies (ii), proving the claimed classification.

For a nonscalar Hurwitz matrix, the preceding equivalence and the rank-one test give some \(v,z\) with \(z^{\mathsf T}L_A(vv^{\mathsf T})z<0\). The \(h^3\) expansion makes \(z^{\mathsf T}\Delta_h(A,vv^{\mathsf T})z<0\) for all sufficiently small \(h>0\).

If (ii) holds and \(D_k=X_k^{\mathrm{num}}-X(kh)\), then \(D_0=0\) and
\[
 D_{k+1}=e^{hA}D_k e^{hA^{\mathsf T}}+\Delta_h(A,Q)\succeq0.
\]
Induction gives \(D_k\succeq0\) at every mesh point \(k\ge0\).

**5. Concrete small-step obstruction.** Let
\[
 A=\begin{pmatrix}-1&0\\0&-2\end{pmatrix},\qquad
 Q=\begin{pmatrix}1&1\\1&1\end{pmatrix}=vv^{\mathsf T},\quad v=(1,1)^{\mathsf T}.
\]
Then
\[
 L_A(Q)=\begin{pmatrix}4&9\\9&16\end{pmatrix},
 \qquad\det L_A(Q)=-17.
\]
Consequently \(\Delta_h(A,Q)\) is indefinite for every sufficiently small \(h>0\), although the exact and numerical covariance matrices are each positive semidefinite for any positive-semidefinite initial covariance.

## Verification

The standalone, standard-library-only `verify.py` checks exact rational versions of the curvature identity, the completion-of-squares certificate for a nonnormal square-zero drift and an opposite-sign diagonal drift, the stable two-mode negative determinant \(-17\), and Cayley–Hamilton boundary cases in dimension two. Floating-point checks of the directly evaluated exponential defect at representative steps supplement the exact algebra. Execute `python3 verify.py` from the directory containing this document. The mathematical proof above, not the finite checks, establishes all quantified statements.

## Relationship to prior work

Zhang, Lan and Jing (2026, arXiv:2606.15703), Section 2 Eq. (5), establish the IF-SSPRK2 update and prove preservation of positive semidefiniteness in their Theorem 3.2; their error theorem supplies a norm bound, not an exact criterion for numerical-minus-exact Loewner order. The present result concerns the constant-input specialization and compares it with the exact variation-of-constants integral.

Dieci and Eirola (1994) study positive-definiteness-preserving numerical methods for Riccati and Lyapunov equations, including a trapezoidal approximation in a different formulation; their positivity argument does not provide this universal Loewner-defect classification. Koskela and Mena (2017) develop comparison monotonicity of numerical Riccati solutions with different data; that order relation is distinct from bounding an exact solution by its same-data quadrature step. These distinctions do not amount to a claim of exhaustive historical priority.

## Limitations

The conclusion is about **universal** one-sided order for *all* positive-semidefinite constant inputs and positive steps. A particular \(A,Q,h\) can have a positive defect even when the universal property fails. The extension to repeated steps requires the same constant \(A,Q\). General nonautonomous or state-dependent forcing, finite-precision exponential evaluation, and nonlinear Riccati terms are not covered. Older literature on matrix-valued trapezoidal inequalities and monotone Riccati discretization may contain equivalent formulations; publication priority is not independently certified.

## References

1. W. Zhang, R. Lan and X. Jing, *Strong Stability Preserving Integrating Factor Runge-Kutta Methods for Differential Lyapunov Equations with Positivity Preservation*, arXiv:2606.15703, first posted June 14, 2026, https://arxiv.org/abs/2606.15703.
2. L. Dieci and T. Eirola, *Positive Definiteness in the Numerical Solution of Riccati Differential Equations*, 1994; accessible preprint https://dieci.math.gatech.edu/preps/LuTiPosDefDRE.pdf.
3. A. Koskela and H. Mena, *Analysis of Krylov Subspace Approximation to Large Scale Differential Riccati Equations*, arXiv:1705.07507, https://arxiv.org/abs/1705.07507.
4. L. Dieci and T. Eirola, *Preserving Monotonicity in the Numerical Solution of Riccati Differential Equations*, 1996; bibliographic abstract at https://research.aalto.fi/en/publications/preserving-monotonicity-in-the-numerical-solution-of-riccati-diff/. The full text of this source was not examined.

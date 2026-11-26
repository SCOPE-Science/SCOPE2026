# Two dimensions protect every exact-line steepest-descent iterate; three dimensions break at step two
## Finding
Consider exact-line steepest descent for the symmetric positive-definite Stieltjes system
\[
Ax=b,
\]
started from \(x_0=0\), with \(b\ge 0\) componentwise. Writing
\[
r_k=b-Ax_k,
\qquad
\alpha_k=\frac{r_k^{\top}r_k}{r_k^{\top}Ar_k},
\qquad
x_{k+1}=x_k+\alpha_k r_k,
\]
all iterates are componentwise nonnegative in dimensions one and two. This dimension bound is sharp: in dimension three the second iterate can already have a negative component even when \(A\) is irreducible and \(A^{-1}b>0\).

An exact witness is
\[
A=\begin{pmatrix}
2&-2&0\\
-2&3&-1\\
0&-1&7
\end{pmatrix},
\qquad
b=\begin{pmatrix}3\\0\\1\end{pmatrix}.
\]
The leading principal minors are \(2\), \(2\), and \(12\), so \(A\) is positive definite; it is also an irreducible Stieltjes matrix. Exact steepest descent gives
\[
\alpha_0=\frac25,
\qquad
x_1=\begin{pmatrix}6/5\\0\\2/5\end{pmatrix},
\qquad
r_1=\begin{pmatrix}3/5\\14/5\\-9/5\end{pmatrix},
\]
then
\[
\alpha_1=\frac{286}{1257},
\qquad
x_2=\begin{pmatrix}560/419\\4004/6285\\-4/419\end{pmatrix}.
\]
Thus \((x_2)_3<0\), although
\[
A^{-1}b=\begin{pmatrix}31/6\\11/3\\2/3\end{pmatrix}>0.
\]
Consequently dimension three and iteration two are jointly minimal for transient componentwise sign loss in this class.

## Assumptions and scope
A Stieltjes matrix here means a real symmetric positive-definite matrix with nonpositive off-diagonal entries. The right-hand side is any componentwise nonnegative vector. Exact line search is taken for the strictly convex quadratic
\[
\phi(x)=\frac12x^{\top}Ax-b^{\top}x.
\]
The statement concerns the signs of the primal iterates, not monotonicity of the objective, residual norm, energy error, or individual residual coordinates. No claim is made for nonsymmetric \(M\)-matrices, inexact line searches, preconditioned steepest descent, or constrained variants.

## Proof
The one-dimensional case terminates at the nonnegative solution in one step. In any dimension the first iterate is
\[
x_1=\alpha_0b\ge0,
\]
so a first-iterate counterexample is impossible.

Now let \(A\) be two dimensional. If \(r_1=0\), the method has already reached \(A^{-1}b\ge0\). Otherwise exact line search gives
\[
r_0^{\top}r_1=0.
\]
Normalize
\[
u=\frac{r_0}{\lVert r_0\rVert_2},
\qquad
v=\frac{r_1}{\lVert r_1\rVert_2}.
\]
Then \(u,v\) form an orthonormal basis, and therefore
\[
\frac1{\alpha_0}=u^{\top}Au,
\qquad
\frac1{\alpha_1}=v^{\top}Av,
\]
so trace invariance yields
\[
\frac1{\alpha_0}+\frac1{\alpha_1}=\operatorname{tr}(A),
\qquad
\alpha_0+\alpha_1=\alpha_0\alpha_1\operatorname{tr}(A).
\]
Using \(r_1=b-\alpha_0Ab\), the second iterate is
\[
\begin{aligned}
x_2
&=\alpha_0b+\alpha_1r_1\\
&=\bigl((\alpha_0+\alpha_1)I-\alpha_0\alpha_1A\bigr)b\\
&=\alpha_0\alpha_1\bigl((\operatorname{tr}A)I-A\bigr)b.
\end{aligned}
\]
For
\[
A=\begin{pmatrix}a&-c\\-c&d\end{pmatrix},
\qquad a,d>0,\quad c\ge0,
\]
one has
\[
(\operatorname{tr}A)I-A=\begin{pmatrix}d&c\\c&a\end{pmatrix}\ge0,
\]
so \(x_2\ge0\).

The same two-dimensional structure controls every later iterate. Cayley--Hamilton gives
\[
A^2-(\operatorname{tr}A)A+(\det A)I=0,
\]
and hence
\[
r_2
=\bigl(I-(\alpha_0+\alpha_1)A+\alpha_0\alpha_1A^2\bigr)b
=\rho b,
\]
where
\[
\rho=1-\alpha_0\alpha_1\det A.
\]
In the orthonormal basis \(u,v\), write
\[
A=\begin{pmatrix}s&t\\t&q\end{pmatrix},
\qquad
s=\frac1{\alpha_0},
\qquad
q=\frac1{\alpha_1}.
\]
Then
\[
\rho=\frac{t^2}{sq},
\qquad 0\le\rho<1.
\]
Because the exact-line-search Rayleigh quotient is unchanged by scaling the residual, the step lengths repeat with period two and
\[
r_{2m}=\rho^m b,
\qquad
r_{2m+1}=\rho^m r_1.
\]
Thus
\[
x_{2m}=(1-\rho^m)A^{-1}b\ge0,
\]
and
\[
x_{2m+1}=x_{2m}+\alpha_0\rho^m b\ge0.
\]
The inverse is nonnegative because a two-dimensional Stieltjes matrix has
\[
A^{-1}=\frac1{ad-c^2}\begin{pmatrix}d&c\\c&a\end{pmatrix}\ge0.
\]
This proves positivity of every two-dimensional iterate.

For the displayed three-dimensional witness, exact rational calculation gives the stated \(\alpha_0\), \(x_1\), \(r_1\), \(\alpha_1\), and \(x_2\), with \((x_2)_3=-4/419<0\). Since dimension one and two are protected and the first iterate is protected in every dimension, the boundary is jointly minimal.

## Verification
The accompanying `verify.py` uses exact rational arithmetic. It verifies the three leading principal minors, the exact inverse and positive solution, both line-search parameters, residual orthogonality, and the negative coordinate \((x_2)_3=-4/419\) of the three-dimensional witness. It also replays the two-dimensional recurrence on several rational Stieltjes examples as a supplementary consistency check. The universal two-dimensional statement is proved algebraically above; the finite replay is not used as a substitute for that proof. The recorded checker output is in `CHECK_OUTPUT.txt`.

## Relationship to prior work
Knyazev and Lashuk analyze steepest descent for symmetric positive-definite linear systems, including the classical exact steepest-descent convergence bound, and their SIAM record lists primary MSC 65F10. Their public arXiv version appeared on 30 May 2006. Their results concern convergence geometry and variable preconditioning, not componentwise order preservation of Stieltjes iterates.

Gonzaga and Schneider give a detailed treatment of the Cauchy algorithm for quadratic functions. They state the exact Cauchy step, residual-gradient orthogonality, and the classical zigzagging/asymptotic behavior toward the extreme eigenspaces. Those spectral facts are compatible with the two-dimensional recurrence used here but do not state the Stieltjes positivity theorem or the sharp three-dimensional second-step obstruction.

Faber, Liesen, and Tichý prove exact and asymptotic recurrence results for the optimum-gradient method, including exact repetition of normalized even subsequences when the Krylov grade is two. This is the closest structural antecedent inspected for the two-dimensional cycle. It does not imply componentwise nonnegativity, because spectral recurrence alone has no cone-order conclusion, and it does not provide the irreducible three-dimensional Stieltjes counterexample or the joint dimension/iteration minimality statement.

A prior published finding on exact steepest descent studies a three-mode perturbation threshold for two-step Euclidean error contraction on diagonal quadratics. Its observable and conclusion are different: Euclidean error deterioration does not imply, and is not implied by, componentwise positivity on Stieltjes systems.

## Limitations
The classification is specific to unpreconditioned exact-line steepest descent from the zero start on real SPD Stieltjes matrices with nonnegative right-hand side. It does not assert coordinatewise monotonicity toward the solution, only nonnegativity in dimensions at most two. The three-dimensional example proves possibility and minimality, not prevalence. The literature comparison leaves a residual risk that older matrix-iteration or monotone-operator literature states the same componentwise boundary under different terminology; no implication-equivalent statement was located in the inspected sources or semantic searches.

## References
1. A. V. Knyazev and I. Lashuk, “Steepest Descent and Conjugate Gradient Methods with Variable Preconditioning,” SIAM Journal on Matrix Analysis and Applications 29 (2007/2008), 1267–1280, DOI: 10.1137/060675290; public preprint arXiv:math/0605767, first submitted 30 May 2006.
2. C. C. Gonzaga and R. M. Schneider, “On the steepest descent algorithm for quadratic functions,” Optimization Online, published 15 June 2015, updated 9 July 2015, https://optimization-online.org/2015/06/4964/.
3. V. Faber, J. Liesen, and P. Tichý, “On the Forsythe conjecture,” BIT Numerical Mathematics 63 (2023), article 49, DOI: 10.1007/s10543-023-00991-x.

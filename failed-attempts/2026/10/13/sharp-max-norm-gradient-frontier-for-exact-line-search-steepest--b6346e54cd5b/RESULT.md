# Sharp max-norm gradient frontier for exact-line-search steepest descent

## Finding
Let
\[
f(x)=\frac12x^{\mathsf T}Ax-b^{\mathsf T}x,
\qquad
A=A^{\mathsf T}>0,
\]
be a strictly convex quadratic in dimension \(n\ge2\), and let
\[
\kappa=
\frac{\lambda_{\max}(A)}
{\lambda_{\min}(A)}.
\]
For one exact-line-search steepest-descent step,
\[
x^+=x-\alpha g,\qquad
g=Ax-b,\qquad
\alpha=
\frac{g^{\mathsf T}g}{g^{\mathsf T}Ag},
\]
the sharp worst-case coordinatewise gradient amplification is
\[
\boxed{
\sup_{\substack{A=A^{\mathsf T}>0\\\kappa_2(A)=\kappa}}
\sup_{g\ne0}
\frac{\|g^+\|_\infty}{\|g\|_\infty}
=
\sqrt{n-1}\,
\frac{\kappa-1}{2\sqrt\kappa}.
}
\]

Therefore every such step is max-norm gradient nonincreasing if and only if
\[
\boxed{
1\le\kappa\le
\frac{\sqrt n+1}{\sqrt n-1}.
}
\]

The boundary depends strongly on dimension. In dimension two it is
\[
3+2\sqrt2,
\]
in dimension three it is
\[
2+\sqrt3,
\]
and it decreases to \(1\) as \(n\to\infty\). Thus there is no nontrivial condition-number-only max-norm safety guarantee uniform in dimension.

An explicit three-dimensional witness has condition number \(4\):
\[
A=
\begin{pmatrix}
\frac{14-4\sqrt2}{5}&-\frac{3+\sqrt2}{5}&-\frac{3+\sqrt2}{5}\\
-\frac{3+\sqrt2}{5}&\frac{8+2\sqrt2}{5}&\frac{3+2\sqrt2}{5}\\
-\frac{3+\sqrt2}{5}&\frac{3+2\sqrt2}{5}&\frac{8+2\sqrt2}{5}
\end{pmatrix}.
\]
Its eigenvalues are \(1,1,4\). For
\[
g=(1,1,1)^{\mathsf T},
\]
the exact step length is
\[
\alpha=\frac58
\]
and
\[
g^+
=
\left(
\frac{3\sqrt2}{4},
-\frac{3\sqrt2}{8},
-\frac{3\sqrt2}{8}
\right)^{\mathsf T}.
\]
Hence
\[
\frac{\|g^+\|_2}{\|g\|_2}=\frac34<1,
\]
while
\[
\frac{\|g^+\|_\infty}{\|g\|_\infty}
=
\frac{3\sqrt2}{4}>1.
\]

## Assumptions and scope
The result concerns exact arithmetic, a real SPD quadratic, the ordinary Euclidean steepest-descent direction, and an exact line search. The max norm is used only to measure the gradient before and after the step; the algorithm itself is not changed to a non-Euclidean steepest-descent method.

The initial gradient is arbitrary and therefore covers every starting point and every linear term \(b\). Multiplying \(A\) by a positive scalar does not affect the condition number or the amplification factor, so the spectrum can be normalized to \([1,\kappa]\).

The theorem is one-step. It does not claim a formula for the maximum over a prescribed multi-step trajectory, finite-precision line searches, inexact gradients, nonquadratic objectives, or non-Euclidean search directions.

## Proof
Exact line search gives the familiar orthogonality
\[
(g^+)^{\mathsf T}g=0.
\]

First derive the sharp Euclidean factor directly. Normalize
\[
\lambda_{\min}(A)=1,\qquad
\lambda_{\max}(A)=\kappa.
\]
In an eigenbasis of \(A\), define
\[
w_i=\frac{g_i^2}{\|g\|_2^2},
\qquad
m_1=\sum_iw_i\lambda_i,
\qquad
m_2=\sum_iw_i\lambda_i^2.
\]
Because
\[
\alpha=\frac1{m_1},
\]
one obtains
\[
\frac{\|g^+\|_2^2}{\|g\|_2^2}
=
\frac{m_2}{m_1^2}-1.
\]
For every \(\lambda\in[1,\kappa]\),
\[
(\lambda-1)(\kappa-\lambda)\ge0,
\]
so
\[
\lambda^2\le(1+\kappa)\lambda-\kappa.
\]
After averaging,
\[
m_2\le(1+\kappa)m_1-\kappa.
\]
Therefore
\[
\frac{\|g^+\|_2^2}{\|g\|_2^2}
\le
\frac{(\kappa-m_1)(m_1-1)}{m_1^2}.
\]
The right-hand side is maximized at
\[
m_1=\frac{2\kappa}{1+\kappa},
\]
and the maximum is
\[
\frac{(\kappa-1)^2}{4\kappa}.
\]
Thus
\[
\frac{\|g^+\|_2}{\|g\|_2}
\le
c_\kappa,
\qquad
c_\kappa=
\frac{\kappa-1}{2\sqrt\kappa}.
\]

Now use the exact-line-search orthogonality. Let \(h=g^+\), and let \(j\) satisfy
\[
|h_j|=\|h\|_\infty.
\]
Because \(h\perp g\),
\[
|h_j|
=
|\langle h,P_{g^\perp}e_j\rangle|
\le
\|h\|_2
\sqrt{
1-\frac{g_j^2}{\|g\|_2^2}
}.
\]
Using the Euclidean bound gives
\[
|h_j|
\le
c_\kappa
\sqrt{
\|g\|_2^2-g_j^2
}.
\]
If
\[
M=\|g\|_\infty,
\]
then
\[
\|g\|_2^2-g_j^2
=
\sum_{i\ne j}g_i^2
\le
(n-1)M^2.
\]
Hence
\[
\|g^+\|_\infty
\le
c_\kappa\sqrt{n-1}\,\|g\|_\infty.
\]

It remains to prove simultaneous sharpness. Let
\[
u=\frac1{\sqrt n}(1,\ldots,1)^{\mathsf T}
\]
and
\[
v=
\frac{P_{u^\perp}e_1}
{\|P_{u^\perp}e_1\|_2}.
\]
Then
\[
u\perp v,\qquad
\frac{\|v\|_\infty}{\|u\|_\infty}
=
\sqrt{n-1}.
\]
On the plane spanned by \(u,v\), define \(A\) in the orthonormal basis \((u,v)\) by
\[
A_{uv}
=
\frac1{\kappa+1}
\begin{pmatrix}
2\kappa&-\sqrt\kappa(\kappa-1)\\
-\sqrt\kappa(\kappa-1)&\kappa^2+1
\end{pmatrix}.
\]
Its trace is \(1+\kappa\) and its determinant is \(\kappa\), so its eigenvalues are \(1\) and \(\kappa\). Extend \(A\) as the identity on the orthogonal complement.

For the unit starting gradient \(g=u\),
\[
u^{\mathsf T}Au
=
\frac{2\kappa}{1+\kappa},
\]
hence
\[
\alpha=
\frac{1+\kappa}{2\kappa}.
\]
Direct substitution gives
\[
g^+=c_\kappa v.
\]
Thus equality holds in both the Euclidean factor and the geometric max-norm factor:
\[
\frac{\|g^+\|_\infty}{\|g\|_\infty}
=
c_\kappa\sqrt{n-1}.
\]

Finally, max-norm nonincrease is universal exactly when
\[
\sqrt{n-1}\,
\frac{\kappa-1}{2\sqrt\kappa}
\le1.
\]
Writing \(s=\sqrt\kappa\) reduces equality to
\[
\sqrt{n-1}(s^2-1)=2s,
\]
whose root above one is
\[
s=
\frac{\sqrt n+1}{\sqrt{n-1}}.
\]
Squaring and simplifying yields
\[
\kappa=
\frac{\sqrt n+1}{\sqrt n-1}.
\]

## Verification
The embedded `verify.py` checks the equality construction with high-precision decimal arithmetic for several dimensions and condition numbers. It also reconstructs the displayed three-dimensional matrix at \(\kappa=4\), verifies the exact line-search step length \(5/8\), its spectrum through the orthonormal two-plane representation, and the resulting Euclidean and max-norm ratios.

The universal inequality is analytic. The finite checks only replay the construction and selected identities.

## Relationship to prior work
Nocedal, Sartenaer, and Zhu study oscillations of the steepest-descent gradient norm on strongly convex quadratics. Their Theorem 4.1 gives the sharp Euclidean one-step estimate
\[
\frac{\|g^+\|_2^2}{\|g\|_2^2}
\le
\frac{(\kappa-1)^2}{4\kappa},
\]
and identifies
\[
3+2\sqrt2
\]
as the Euclidean gradient-norm monotonicity boundary. That Euclidean result is prior work and is rederived above only as an ingredient.

De Klerk, Glineur, and Taylor analyze exact-line-search gradient descent on smooth strongly convex functions, record the orthogonality of successive gradients, and establish tight worst-case objective convergence. Their preprint lists primary AMS classification \(90C25\).

The result here concerns a different diagnostic: the coordinatewise maximum norm of the gradient. Orthogonality sharpens the naive norm-equivalence factor from \(\sqrt n\) to \(\sqrt{n-1}\), and a joint equality construction proves that this improvement is exact. The resulting dimension-dependent condition-number threshold is not implied by the Euclidean theorem.

Targeted searches under max-norm, infinity-norm, componentwise-gradient, exact-line-search, and steepest-descent terminology did not locate the formula
\[
\sqrt{n-1}\frac{\kappa-1}{2\sqrt\kappa}
\]
or the threshold
\[
\frac{\sqrt n+1}{\sqrt n-1}.
\]

## Limitations
The sharp result is specific to max-norm measurement of the gradient after one exact-line-search step on an SPD quadratic. It does not classify other coordinatewise statistics or higher-step path maxima.

The construction uses a dense rotated SPD matrix; additional structural restrictions such as diagonal, banded, sparse, or sign-constrained Hessians can change the sharp factor.

The originality comparison cannot exclude an older result stated purely as a geometric corollary of the Euclidean steepest-descent bound or under terminology such as maximum-component norm. The closest full paper inspected treats the Euclidean norm and component dynamics but does not state this dimension law.

## References
1. J. Nocedal, A. Sartenaer, and C. Zhu, “On the Behavior of the Gradient Norm in the Steepest Descent Method,” Computational Optimization and Applications 22 (2002), 5–35. DOI 10.1023/A:1014897230089.
2. E. de Klerk, F. Glineur, and A. B. Taylor, “On the worst-case complexity of the gradient method with exact line search for smooth strongly convex functions,” arXiv:1606.09365, first submitted 2016-06-30; later Optimization Letters 11 (2017), 1185–1199. DOI 10.1007/s11590-016-1087-4.

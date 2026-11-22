# Two sharp singular limits for damped modal least-squares projection

## Finding
For real parameters \(a,b>0\), let \(E_{a,b}\subset L^2(0,\infty)\) be the real two-dimensional space
\[
E_{a,b}=\operatorname{span}_{\mathbb R}\{e^{-at}\cos(bt),\ e^{-at}\sin(bt)\}.
\]
Let \(P_{a,b}\) be the real orthogonal \(L^2\)-projection onto \(E_{a,b}\), extended canonically to real \(L^\infty(0,\infty)\) using its integrable finite-rank kernel. Let \(r=b/a>0\) and \(\Lambda(r)=\|P_{a,b}\|_{L^\infty\to L^\infty}\). Then
\[
\boxed{\Lambda(r)=\frac8e+O(r^2)\quad(r\downarrow0),\qquad
\Lambda(r)=\frac8\pi+O(r^{-1})\quad(r\to\infty).}
\]
In particular both leading constants are sharp, in the sense of limits of the true global operator norms rather than merely upper bounds. The ordinary cosine/sine coefficient Gram matrix has spectral condition number \(\kappa_2\sim 4/r^2\) as \(r\downarrow0\), although the projector norm remains bounded. The exact norm of endpoint evaluation, a lower bound for \(\Lambda(r)\) at every finite \(r\), is
\[
\boxed{\sup_{\|f\|_\infty\le1}|(P_{a,b}f)(0)|=
\frac{8\exp[-\arctan(r)/r]}{\sqrt{1+r^2}\,[1-\exp(-\pi/r)]}.}
\]
The endpoint bound is attained by the sign of its reproducing kernel. At the exactly collapsed parameter \(b=0\), projection onto \(\operatorname{span}\{e^{-at}\}\) has uniform operator norm \(2\), so \(\lim_{b\downarrow0}\Lambda(b/a)=8/e\ne2\). Thus the nearly coincident real modes have a nontrivial *confluent* rank-two stability limit, not the rank-one limit obtained by setting the frequency to zero first.

## Assumptions and scope
Lebesgue measure on \((0,\infty)\) and real-valued bounded inputs are used. The \(L^2\) projector is initially defined on \(L^2\); its kernel formula gives the unique specified integral extension to bounded inputs (not an assertion that all \(L^\infty\) inputs belong to \(L^2\)). The domain, damping, and frequency are exactly \(a,b>0\). A change of variable \(s=at\) reduces the norm to \(a=1\), so only \(r=b/a\) matters. No assertion is made that endpoint evaluation is globally norming for all finite \(r\); the result gives the exact endpoint norm and the two sharp global asymptotic limits.

## Proof
**1. Exact kernel and its finite-frequency endpoint.** Set \(a=1\) and use the well-conditioned basis
\[
u_r(t)=e^{-t}\cos(rt),\qquad v_r(t)=e^{-t}\frac{\sin(rt)}r.
\]
Direct Laplace integration yields the Gram matrix and inverse
\[
G_r=\frac1{4(1+r^2)}\begin{pmatrix}2+r^2&1\\1&1\end{pmatrix},
\qquad G_r^{-1}=4\begin{pmatrix}1&-1\\-1&2+r^2\end{pmatrix}.
\]
Writing \(c_z=\cos(rz)\) and \(s_z=\sin(rz)/r\), the orthogonal projection kernel is
\[
K_r(x,y)=4e^{-x-y}[c_xc_y-c_xs_y-s_xc_y+(2+r^2)s_xs_y].
\]
For fixed \(x\), the kernel is absolutely integrable in \(y\), uniformly in \(x\), so
\[
\Lambda(r)=\sup_{x\ge0}\int_0^\infty|K_r(x,y)|\,dy.
\]
At \(x=0\),
\[
K_r(0,y)=\frac4r\frac{d}{dy}[e^{-y}\sin(ry)].
\]
The damped sine has successive extrema at \(y_k=(\arctan r+k\pi)/r\), with alternating signs and magnitudes \(r(1+r^2)^{-1/2}\exp[-(\arctan r+k\pi)/r]\). Its total variation from zero back to zero equals twice the sum of these magnitudes. This proves the endpoint formula above. The input \(f(y)=\operatorname{sgn}K_r(0,y)\) attains that endpoint value; it is bounded and the integral extension is well defined.

**2. Coefficient conditioning.** The unrescaled basis \(e^{-t}\cos rt,e^{-t}\sin rt\) has Gram matrix \(rac1{4(1+r^2)}\bigl(\begin{smallmatrix}2+r^2&r\\r&r^2\end{smallmatrix}\bigr)\). Its trace equals \(1/2\), and its determinant is \(r^2/[16(1+r^2)]\). Thus its largest and smallest eigenvalues tend to \(1/2\) and are asymptotic to \(r^2/8\), respectively, so the spectral condition number is \(4/r^2+O(1)\). This is basis-coefficient ill-conditioning, not divergence of the projector itself.

**3. Confluent small-frequency limit, uniformly in evaluation.** Globally for \(z\ge0\) and \(0<r\le1\), elementary Taylor remainder inequalities give
\[
|\cos(rz)-1|\le\tfrac12r^2z^2,
\quad|\sin(rz)/r-z|\le\tfrac16r^2z^3,
\quad |\sin(rz)/r|\le z.
\]
Inserting these into the kernel shows that for some absolute finite constant \(C\),
\[
\sup_{x\ge0}\int_0^\infty|K_r(x,y)-K_0(x,y)|\,dy\le Cr^2,
\]
where the *confluent* kernel is \(K_0(x,y)=4e^{-x-y}(1-x-y+2xy)\). Indeed each difference is bounded by \(r^2e^{-x-y}\) times a fixed polynomial with nonnegative coefficients in \(x,y\), and every \(\sup_{x\ge0}e^{-x}x^m\int_0^\infty e^{-y}y^n\,dy\) is finite. Consequently, \(|\Lambda(r)-\Lambda_0|\le Cr^2\), where \(\Lambda_0=\sup_x\int|K_0(x,y)|dy\).

To compute \(\Lambda_0\) exactly, put
\[
J(x)=\int_0^\infty e^{-y}|(1-x)+(2x-1)y|\,dy,
\quad \int_0^\infty|K_0(x,y)|dy=4e^{-x}J(x).
\]
Now \(J(0)=2/e\) and \(J(1/2)=1/2\). For \(0\le x\le1/2\), convexity of \(J\) as an integral of absolute affine functions implies
\[
J(x)\le(1-2x)\,\frac2e+x\le\frac2e.
\]
Thus this interval contributes at most \(8/e\), attained at \(x=0\). For \(1/2\le x\le1\), the affine integrand is nonnegative, hence \(J(x)=x\), giving at most \(4/e\). For \(x\ge1\), the triangle inequality gives \(J(x)\le3x-2\), and
\[
4e^{-x}J(x)\le 12e^{-5/3}<8/e
\]
(the maximum of \(e^{-x}(3x-2)\) is at \(x=5/3\)). Therefore \(\Lambda_0=8/e\). This proves the first asymptotic. The true rank-one projector when \(b=0\) has kernel \(2e^{-x-y}\), and hence operator norm \(2\).

**4. High-frequency limit uniformly in evaluation.** Algebraically rewriting the same exact kernel gives
\[
K_r(x,y)=4e^{-x-y}\left[\cos(r(x-y))-
\frac1r\sin(r(x+y))+\frac2{r^2}\sin(rx)\sin(ry)\right].
\]
For \(r\ge1\), the row integral of the last two terms is at most \(e^{-x}(4/r+8/r^2)\). The continuous periodic function \(g(t)=|\cos t|-2/\pi\) has zero mean and a bounded periodic primitive \(F\). Integration by parts therefore implies, uniformly in the phase \(\theta\),
\[
\left|\int_0^\infty e^{-y}|\cos(\theta-ry)|\,dy-\frac2\pi\right|
\le\frac{2\|F\|_\infty}{r}.
\]
Consequently the original row integrals equal \(8e^{-x}/\pi+O(e^{-x}/r)\), with an absolute implicit constant uniform over \(x\ge0\). Taking the supremum gives \(\Lambda(r)\le8/\pi+O(1/r)\), and evaluating at \(x=0\) gives the reverse bound. This proves the second asymptotic.

## Verification
The Gram matrix is independently obtained by integrating elementary damped trigonometric products; its inverse multiplies it to the identity. The checker included with this result tests those identities, kernel idempotence at sample points, exact endpoint formula against sign-split integration, and representative limiting values. None of the numerical tests substitute for the uniform kernel estimates, convexity argument, or periodic-mean proof, all of which are analytic and apply to the stated continuum of parameters.

## Relationship to prior work
The problem is motivated by exponential-polynomial stability and spectral projections on half-lines. Protasov (2022, arXiv:2209.12250) studies sharp derivative inequalities for exponential polynomials, including complex exponents, but does not determine the \(L^\infty\)-operator norms of the real \(L^2\) least-squares projector onto a conjugate damped pair. Chen and Shen (2023, DOI 10.1137/21M1466840) analyze Laguerre and mapped log-orthogonal approximation on semi-infinite intervals; their projection approximation estimates neither assert nor imply the two-mode operator-norm limits proved here. A published two-mode Laguerre *carrier optimization* result instead varies a model frequency to minimize approximation error, which is a different extremal quantity. Results on first-harmonic least squares on finite arcs also use a different measure and projection range. No exact equivalent was found in the checked records; this is not a claim of exhaustive historical priority.

## Limitations
No exact closed formula for the *global* operator norm \(\Lambda(r)\) for arbitrary finite \(r\) is asserted, nor is monotonicity in \(r\). The explicit finite-frequency formula is only the norm of evaluation at the endpoint. The result does not concern weighted \(L^p\) projection for other measures, arbitrary dimension, complex-valued input/operator norms, or the uniform norm of derivative evaluation. Earlier specialist work on oscillatory least-squares conditioning might contain related estimates not indexed by the searches reported. Independent verification is not claimed.

## References
1. V. Yu. Protasov, *Generalized Markov-Bernstein inequalities and stability of dynamical systems*, first public 25 September 2022, arXiv:2209.12250, https://arxiv.org/abs/2209.12250 .
2. S. Chen and J. Shen, *Log Orthogonal Functions in Semi-Infinite Intervals: Approximation Results and Applications*, SIAM J. Numer. Anal. 61(1) (2023), 110–134, electronically published 23 February 2023, DOI 10.1137/21M1466840; author manuscript at https://www.math.purdue.edu/~shen7/pub/CS_SINUM23.pdf .
3. P. J. Davis and P. Rabinowitz, *Methods of Numerical Integration*, 2nd ed., Academic Press (1984), background on orthogonal projection and approximation norms (not a source for the new limits).

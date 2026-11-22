# Sharp entrywise stability of the two-by-two positive-definite matrix square root

## Finding

For real numbers \(0<a<b<\infty\), let \(\mathcal K_{a,b}\) be the real symmetric \(2\times2\) matrices with \(aI\preceq A\preceq bI\), and write \(\|X\|_{\max}=\max_{i,j}|X_{ij}|\). The *sharp global two-input* Lipschitz constant of the principal positive-definite square-root functional calculus is

\[
\sup_{\substack{A,B\in\mathcal K_{a,b}\\A\ne B}}
\frac{\|A^{1/2}-B^{1/2}\|_{\max}}{\|A-B\|_{\max}}
=\frac{3+2\sqrt2}{8\sqrt a}
-\frac{1}{2(\sqrt a+\sqrt b)}
+\frac{3-2\sqrt2}{8\sqrt b}.
\]

As \(b/a\to\infty\), its ratio to the scalar square-root Lipschitz constant \(1/(2\sqrt a)\) tends to \((3+2\sqrt2)/4\), strictly greater than one. The spectral orientation of a limiting extremizer is a rotation by \(\pi/8\), independent of \(a,b\). With no finite upper spectral bound, the sharp constant on \(A\succeq aI\) is \((3+2\sqrt2)/(8\sqrt a)\). The result is about the maximum *absolute entry* norm, not the induced matrix row-sum norm or Frobenius norm.

## Assumptions and scope

The matrices and all perturbations are **real symmetric**, the input spectral window is \([a,b]\) with \(0<a<b<\infty\), and square root denotes the unique real symmetric positive-definite square root. The coefficient is the supremum over distinct finite pairs and need not be attained by a pair. Dimension is exactly two; no statement is made for higher dimensions. The upper-bound-free statement concerns all real symmetric matrices satisfying \(A\succeq aI\).

## Proof

**1. Derivative and positive kernel.** For any such matrix \(A\), put \(S=A^{1/2}\). Differentiating \(S^2=A\), the Fréchet derivative \(X=D(A^{1/2})[H]\) uniquely solves the Lyapunov equation \(SX+XS=H\), whence

\[
D(A^{1/2})[H]=\int_0^\infty e^{-tS}He^{-tS}\,dt.
\]

A diagonal sign conjugation and a simultaneous coordinate permutation preserve both the spectral window and the maximum-entry norm. Therefore assume the off-diagonal entry of \(S\) is nonpositive and that the first component of its positive lowest-eigenvalue eigenvector is the larger one. There exist \(0<u\le v\) and \(0\le\theta\le\pi/4\), with \(c=\cos\theta\), \(s=\sin\theta\), such that

\[
S=\begin{pmatrix}c&-s\\s&c\end{pmatrix}
\begin{pmatrix}u&0\\0&v\end{pmatrix}
\begin{pmatrix}c&s\\-s&c\end{pmatrix}.
\]

Every entry of \(E_t=e^{-tS}\) is nonnegative: its off-diagonal entry is \(cs(e^{-ut}-e^{-vt})\), and its diagonal entries are nonnegative. Let \(R_i(t)\) be the sum of row \(i\) of \(E_t\). If \(\|H\|_{\max}\le1\), then

\[
|D(A^{1/2})[H]_{ij}|\le\int_0^\infty R_i(t)R_j(t)\,dt
\le \max_k\int_0^\infty R_k(t)^2\,dt.
\]

Both inequalities are sharp in the induced maximum-entry norm: choose \(H=\mathbf1\mathbf1^{\mathsf T}\) and a maximizing diagonal output. Moreover,

\[
R_1(t)-R_2(t)=(c^2-s^2)(e^{-ut}-e^{-vt})\ge0.
\]

Consequently the derivative norm is exactly \(\int_0^\infty R_1(t)^2dt\).

**2. Spectral endpoints.** Set \(x=\tan\theta\in[0,1]\). Directly,

\[
R_1(t)=\frac{1+x}{1+x^2}e^{-ut}
+\frac{x(x-1)}{1+x^2}e^{-vt}.
\]

Since the first coefficient is positive, the second is nonpositive, and \(R_1(t)\ge0\), the integral of \(R_1^2\) is nonincreasing in \(u\) and nondecreasing in \(v\). For eigenvalues of \(A\) in \([a,b]\), we have \(u\ge\sqrt a\), \(v\le\sqrt b\). Therefore the supremum of the derivative norm at each orientation occurs at \(u=\sqrt a\), \(v=\sqrt b\).

**3. Sharp rotation.** For fixed \(u\le v\), integration gives

\[
F_{u,v}(x)=\frac{(1+x)^2/(2u)+2(1+x)x(x-1)/(u+v)+x^2(x-1)^2/(2v)}{(1+x^2)^2}.
\]

An explicit derivative factorization is

\[
F'_{u,v}(x)=
\frac{(u-v)(x^2+2x-1)(ux^2-ux+vx+v)}{uv(u+v)(1+x^2)^3}.
\]

For \(v>u\) and \(x\in[0,1]\), the final parenthetic factor is strictly positive, since \(ux(x-1)\ge-u/4\) while \(v(x+1)\ge v\ge u\). Thus \(F_{u,v}\) increases to \(x=\sqrt2-1\) and decreases afterwards. Since \(\tan(\pi/8)=\sqrt2-1\), the unique maximizing rotation angle for distinct eigenvalues is \(\pi/8\). At this angle the two coefficients of the exponentials in \(R_1\) are \((1+\sqrt2)/2\) and \((1-\sqrt2)/2\). Therefore

\[
\max F_{u,v}=\frac{3+2\sqrt2}{8u}-\frac1{2(u+v)}+\frac{3-2\sqrt2}{8v}.
\]

**4. From derivatives to two-input sharpness.** For any \(A,B\in\mathcal K_{a,b}\), the convex segment \(A_t=A+t(B-A)\) stays in \(\mathcal K_{a,b}\). Integrating its derivative and applying the previous sharp uniform derivative bound yields the claimed global inequality. Conversely, fix \(0<\varepsilon<(b-a)/2\) and construct \(A_\varepsilon\) with eigenvalues \(a+\varepsilon,b-\varepsilon\) and low-eigenvector angle \(\pi/8\) in the preceding orientation. The matrix is in the interior of the spectral window, so the perturbation \(H=\mathbf1\mathbf1^{\mathsf T}\) is admissible for sufficiently small positive steps. Its largest output derivative attains the local expression above for these interior eigenvalues. First send the perturbation step to zero and then \(\varepsilon\downarrow0\); this proves sharpness of the two-input supremum. The upper-bound-free result follows by taking \(b\to\infty\), using inclusion for the upper bound and finite-window sharpness for the lower bound.

## Verification

The analytic certificate consists of the Lyapunov integral, positivity of the two-by-two semigroup entries, the row-sum reduction, monotonicity in the two spectral endpoints, the displayed exactly factored derivative, and the interior rank-one perturbation witness. These are finite symbolic arguments valid for all stated parameters.

The standalone file `check_square_root.py` uses Python's standard library to compute principal roots by the closed two-by-two formula, independently solve the derivative Sylvester equation, enumerate all eight sign vertices of the symmetric input maximum-norm ball, compare the derivative norm with the integrated semigroup row sums, and test finite-pair bounds and near-boundary sharpness. It runs as `python3 check_square_root.py`. Its 16,515 checks are supplementary evidence, not an infinite proof or a formal proof assistant certificate.

## Relationship to prior work

The smooth Fréchet derivative and its divided-difference representation are standard; see Carlsson (2018), especially the review of the Daleckii–Krein theorem. Higham–Relton (2014) obtain Hermitian square-root conditioning in **Frobenius norm**, where the local coefficient is \(1/(2\sqrt{\lambda_{\min}(A)})\), not the entrywise maximum-norm quantity here. Kandolf et al. (2020, 2021) develop low-rank approximations of general Fréchet derivatives, rather than optimizing this spectral-window entrywise constant. Schweitzer (2022) treats higher-order derivatives and level-two conditioning, again in a different norm and order. The new step is the sharp global two-ended spectral optimization and fixed \(\pi/8\) extremal orientation; the standard derivative alone does not state these constants.

## Limitations

No claim is made about larger matrix sizes, nonreal matrices, or entrywise *relative* errors. The coefficient is a supremum and is generally approached by interior perturbations near spectral endpoints. A computational literature search cannot establish historical uniqueness; earlier equivalent conditioning estimates under alternate terminology or unpublished proofs remain possible. Independent validation is not reported.

## References

1. Marcus Carlsson, *Perturbation theory for the matrix square root and matrix modulus*, initial public arXiv submission 2018-10-02, https://arxiv.org/abs/1810.01464 .
2. Nicholas J. Higham and Samuel D. Relton, *Higher Order Fréchet Derivatives of Matrix Functions and the Level-2 Condition Number*, SIAM J. Matrix Anal. Appl. 35 (2014), 1019–1037, https://doi.org/10.1137/130945259 .
3. Peter Kandolf, Antti Koskela, Samuel D. Relton and Marcel Schweitzer, *Computing low-rank approximations of the Fréchet derivative of a matrix function using Krylov subspace methods*, arXiv initial public submission 2020-08-29, https://arxiv.org/abs/2008.12926 .
4. Marcel Schweitzer, *Integral representations for higher-order Fréchet derivatives of matrix functions: Quadrature algorithms and new results on the level-2 condition number*, initial public arXiv submission 2022-03-08, https://arxiv.org/abs/2203.03930 .

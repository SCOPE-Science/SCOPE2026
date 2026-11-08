# Sharp sixth moments and spectral defects for real quadratic harmonics on the three-sphere

## Finding

Let \(\sigma\) be probability surface measure on \(\mathbb S^3\subset\mathbb R^4\). For every nonzero real symmetric trace-free \(4\times4\) matrix \(B\), write
\[
h_B(\omega)=\omega^{\mathsf T}B\omega,
\quad S=\operatorname{tr}(B^2)>0,
\quad T=\operatorname{tr}(B^3),
\quad D=\det B.
\]
Then the exact normalized sixth moment is
\[
\boxed{\frac{\|h_B\|_6^6}{\|h_B\|_2^6}
=\frac9{14}\left(15-144\frac{D}{S^2}+16\frac{T^2}{S^3}\right).}
\]
In particular, the complete sharp two-sided inequality is
\[
\boxed{\frac{27}{7}\le\frac{\|h_B\|_6^6}{\|h_B\|_2^6}\le15.}
\]
The left equality holds exactly when the eigenvalues of \(B\) are \((a,a,-a,-a)\) in some order, for a nonzero real \(a\). The right equality holds exactly when they are \((3a,-a,-a,-a)\) in some order. Orthogonal changes of variables do not affect the norms.

There are also **exact two-sided nonnegative spectral defect identities**:
\[
\boxed{\frac{\|h_B\|_6^6}{\|h_B\|_2^6}-\frac{27}{7}
=\frac9{14}\left[144\left(\frac1{16}-\frac{D}{S^2}\right)
+16\frac{T^2}{S^3}\right],}
\]
\[
\boxed{15-\frac{\|h_B\|_6^6}{\|h_B\|_2^6}
=\frac9{14}\left[144\left(\frac{D}{S^2}+\frac1{48}\right)
+16\left(\frac13-\frac{T^2}{S^3}\right)\right].}
\]
Every bracketed summand is separately nonnegative for trace-free real symmetric \(B\), and the displayed equality cases are complete.

The same two sharp constants govern the full nine-dimensional space of real matrix coefficients of the defining representation of \(\mathrm{SO}(3)\). If \(R\) is Haar uniform and \(F_A(R)=\operatorname{tr}(A^{\mathsf T}R)\), for any nonzero real \(3\times3\) matrix \(A\), then \(\|F_A\|_2^2=\|A\|_{\mathrm F}^2/3\) and
\[
\frac{27}{7}\le\frac{\|F_A\|_6^6}{\|F_A\|_2^6}\le15.
\]
The lower equality holds precisely for rank-one \(A\); the upper equality holds precisely when \(A\) is a nonzero scalar multiple of an orthogonal matrix. This is an equivalent realization of the same nine-dimensional harmonic norm problem, not a separate assertion of independent novelty.

## Assumptions and scope

All matrices and coefficient functions are real. All sphere and group measures are normalized probabilities. The sphere is \(\mathbb S^3\), not \(\mathbb S^2\); harmonic degree is exactly two, and the exponent is exactly six. Any real homogeneous quadratic polynomial with vanishing Euclidean Laplacian has the unique representation \(x^{\mathsf T}Bx\) with \(B\) real symmetric and trace-free. No positive definiteness is assumed. All scale-invariant fractions have \(S>0\). The group statement concerns Haar probability measure on \(\mathrm{SO}(3)\) and arbitrary real matrices \(A\ne0\).

## Proof

### 1. Exact spherical sixth moment

Let \(G\) be standard Gaussian in \(\mathbb R^4\), and write \(G=\rho\omega\), where \(\omega\) is uniform on \(\mathbb S^3\), independent of \(\rho\). The Gaussian quadratic form \(Z=G^{\mathsf T}BG\) is centered because \(\operatorname{tr}B=0\). Its cumulants are \(\kappa_r(Z)=2^{r-1}(r-1)!\operatorname{tr}(B^r)\) for integers \(r\ge2\). In particular,
\[
\mathbb EZ^2=2S,
\quad \mathbb EZ^6=120S^3+1440S\operatorname{tr}(B^4)
+640T^2+3840\operatorname{tr}(B^6).
\]
Since \(\mathbb E\rho^4=4\cdot6=24\) and \(\mathbb E\rho^{12}=4\cdot6\cdot8\cdot10\cdot12\cdot14=322560\),
\[
\|h_B\|_2^2=\frac S{12},
\qquad
\|h_B\|_6^6=\frac{120S^3+1440S\operatorname{tr}(B^4)+640T^2+3840\operatorname{tr}(B^6)}{322560}.
\]
Newton's identities for the four eigenvalues with zero sum give
\[
\operatorname{tr}(B^4)=\frac{S^2}{2}-4D,
\qquad
\operatorname{tr}(B^6)=\frac{S^3}{4}-3DS+\frac{T^2}{3}.
\]
Substitution yields \(\|h_B\|_6^6=(15S^3-144DS+16T^2)/2688\). Dividing by \((S/12)^3\) proves the exact normalized-moment identity.

### 2. Three elementary sharp spectral constraints

Let the four real eigenvalues be \(\lambda_1,\ldots,\lambda_4\), with \(\sum_i\lambda_i=0\) and \(S=\sum_i\lambda_i^2>0\). First, the arithmetic–geometric mean inequality applied to their squares gives
\[
D=\prod_i\lambda_i\le |D|\le\left(\frac S4\right)^2=\frac{S^2}{16}.
\]
Equality in the positive upper bound requires equal nonzero absolute values and, by zero sum, exactly two positive and two negative eigenvalues. This is precisely the \((a,a,-a,-a)\) orbit.

Second, \(D\ge-S^2/48\). It is trivial if \(D\ge0\). If \(D<0\), after replacing all eigenvalues by their negatives if needed, write the eigenvalues as \((a+b+c,-a,-b,-c)\) with \(a,b,c>0\). For \(t=a+b+c\), the elementary inequalities \(abc\le(t/3)^3\) and \(a^2+b^2+c^2\ge t^2/3\) give
\[
-D=tabc\le\frac{t^4}{27},
\qquad S=t^2+a^2+b^2+c^2\ge\frac{4t^2}{3},
\]
and therefore \(-D\le S^2/48\). Equality requires \(a=b=c\), giving \((3a,-a,-a,-a)\).

Third,
\[
0\le T^2\le\frac{S^3}{3}.
\]
To prove the upper bound normalize \(S=1\), and maximize \(\sum_i\lambda_i^3\) on the compact intersection \(\sum_i\lambda_i=0\), \(\sum_i\lambda_i^2=1\). At an extremum the two constraints have independent gradients; Lagrange multipliers yield \(3\lambda_i^2=\alpha+2\beta\lambda_i\). Hence all four eigenvalues take at most two distinct values. If one value has multiplicity \(k\in\{1,2,3\}\) and the other multiplicity \(4-k\), zero sum and unit squared sum give, up to an overall sign,
\[
\lambda_{1}=\cdots=\lambda_k=\sqrt{\frac{4-k}{4k}},
\quad
\lambda_{k+1}=\cdots=\lambda_4=-\sqrt{\frac{k}{4(4-k)}}.
\]
Substitution into \(T\) gives \(|T|=1/\sqrt3\) for \(k=1,3\) and \(T=0\) for \(k=2\). Both endpoints are attainable. Thus \(T^2\le S^3/3\), with equality exactly for the one-versus-three eigenvalue configuration.

### 3. Sharp inequalities, complete equality cases, and exact defects

Insert the three inequalities
\[
-\frac1{48}\le\frac D{S^2}\le\frac1{16},
\qquad0\le\frac{T^2}{S^3}\le\frac13
\]
into the exact sixth-moment identity. The largest possible moment is attained when \(D/S^2=-1/48\) and \(T^2/S^3=1/3\), simultaneously realized by \((3a,-a,-a,-a)\). The smallest is attained when \(D/S^2=1/16\) and \(T=0\), simultaneously realized by \((a,a,-a,-a)\). Arithmetic yields the constants \(15\) and \(27/7\). Rearranging the exact identity gives the two displayed sums of nonnegative spectral defects. The equality characterizations in the sharp spectral constraints prove that there are no additional extremizers.

### 4. Equivalent realization as rotation-group matrix coefficients

Write a unit quaternion \(q=(q_0,q_1,q_2,q_3)\in\mathbb S^3\); the standard quadratic quaternion map \(q\mapsto R(q)\) covers \(\mathrm{SO}(3)\) twice and pushes uniform sphere measure to Haar measure. Every entry of \(R(q)\) is a homogeneous traceless quadratic in the four quaternion coordinates, and the nine entries are linearly independent. Thus every real \(F_A(R(q))=\operatorname{tr}(A^{\mathsf T}R(q))\) equals a unique \(h_{B(A)}(q)\), with \(B(A)\) real symmetric and trace-free. The identities \(\operatorname{tr}(B(E_{ij})B(E_{kl}))=4\delta_{ik}\delta_{jl}\), checked from the explicit quaternion rotation formula, establish that the map is an isomorphism between two nine-dimensional Euclidean spaces and that \(\|F_A\|_2^2=\|A\|_{\mathrm F}^2/3\).

Left-right invariance of Haar measure and signed singular-value decomposition reduce classification to \(A=\operatorname{diag}(a,b,c)\). In that case the quadratic \(B(A)\) is diagonal with eigenvalues
\[
(a+b+c,\ a-b-c,\ -a+b-c,\ -a-b+c).
\]
Solving these four linear equations shows that the balanced eigenvalue orbit corresponds precisely to one nonzero diagonal entry of \(A\), and the one-versus-three orbit corresponds precisely to three equal absolute values of the diagonal entries. Undoing left-right rotations gives the stated rank-one and scaled-orthogonal equality families.

## Verification

The standalone script `verify_sixth_s3.py` uses SymPy exact rational arithmetic. It independently expands the degree-six Dirichlet moment of the squared coordinates of a uniform \(\mathbb S^3\) point, substitutes \(\lambda_4=-\lambda_1-\lambda_2-\lambda_3\), and compares every coefficient with the invariant formula. It checks both exact defect identities, the two sharp spectral endpoint values, finite rational examples, and the full nine-element quaternion matrix-coefficient isometry. It does not replace the continuous Lagrange-multiplier and AM–GM arguments; those prove sharpness and uniqueness for all real matrices.

Run `python verify_sixth_s3.py` from the directory containing this result and the script. Python 3 and SymPy are the only dependencies.

## Relationship to prior work

General distributions of quadratic forms on spheres are studied by Hillier (2001), whose article provides density formulas rather than this sharp normalized sixth-moment range and its equality families. Stanton and Weinstein (1981) treat a fourth-moment extremal question. Dai, Feng, and Tikhonov (arXiv:1408.1877, 2014) address sharp asymptotic *orders* of reverse Hölder constants as harmonic degree grows. The published work *Sharp L4/L2 norm and extremizers for degree-two spherical harmonics* (2026) determines a global fourth-moment norm and its extremizers for all sphere dimensions, including dimension four; its full theorem and proof concern exponent four, and neither the sixth-moment lower constant nor the two exact sixth-moment defects follows from that statement. The current assertion is strictly an exact fixed-degree, sixth-moment, real-coefficient theorem. The classical Gaussian cumulant and Newton identities are used as ingredients and are not claimed as discoveries.

## Limitations

The result is limited to real-valued degree-two harmonics on \(\mathbb S^3\) and their equivalent real \(\mathrm{SO}(3)\) matrix coefficients. It does not establish sharp sixth-moment inequalities on other sphere dimensions, for complex quadratic harmonics, or for arbitrary real exponents. The two exact defect identities control normalized spectral invariants, not a separately quantified distance to an extremal orbit. General reverse Hölder sources and older matrix-invariant literature could contain equivalent formulations; not every plausible paper could be inspected in full. Independent mathematical validation has not been performed.

## References

1. Grant Hillier, *The density of a quadratic form in a vector uniformly distributed on the n-sphere*, Econometric Theory 17 (2001), 1–28, DOI: 10.1017/S026646660117101X (online 2001-02-07).
2. Feng Dai, Han Feng, and Sergey Tikhonov, *Reverse Hölder's inequality for spherical harmonics*, arXiv:1408.1877, first submitted 2014-08-06, published Proc. Amer. Math. Soc. 144 (2016), 1041–1051.
3. Robert J. Stanton and Alan Weinstein, *On the L4 norm of spherical harmonics*, Math. Proc. Cambridge Philos. Soc. 89 (1981), 343–358, DOI: 10.1017/S0305004100058229.
4. *Sharp L4/L2 norm and extremizers for degree-two spherical harmonics*, published research result (2026-09-20), `https://github.com/published-finding corpus/2026/blob/main/2026/9/20/SCOPE-sharp-l4-degree-two-spherical-harmonics--d4106097159f/RESULT.md`.

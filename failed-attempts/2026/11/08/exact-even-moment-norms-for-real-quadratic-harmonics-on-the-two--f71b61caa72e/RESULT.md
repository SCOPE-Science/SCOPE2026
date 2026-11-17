# Exact even-moment norms for real quadratic harmonics on the two-sphere

## Finding
Let \(\sigma\) be normalized surface area on \(\mathbb S^2\), and let \(\mathcal H_{2,\mathbb R}\) be its five-dimensional real space of spherical harmonics of degree two. Every nonzero member is uniquely of the form
\[
h_A(\omega)=\omega^{\mathsf T}A\omega,\qquad A=A^{\mathsf T}\in\mathbb R^{3\times3},\quad \operatorname{tr}A=0,\quad A\ne0.
\]
For integers \(m\ge1\) define \(s_j=\operatorname{tr}(A^j)\) and the scale-free spectral discriminant
\[
d(A)=\frac{s_3^2}{s_2^3}\in[0,1/6].
\]
Write \((a)_k=a(a+1)\cdots(a+k-1)\), with \((a)_0=1\). Define, for \(0\le d\le1/6\),
\[
F_m(d)=\frac{(2m)!}{\prod_{j=0}^{2m-1}(3+2j)}\left(\frac{15}{2}\right)^m
\sum_{\ell=0}^{\lfloor m/3\rfloor}
\frac{(1/2)_{m-\ell}\,2^{m-3\ell}(8/3)^{2\ell}}{(m-3\ell)!\,(2\ell)!}\,d^\ell.
\]
Then **every real quadratic harmonic has the exact even-moment ratio**
\[
\boxed{\frac{\|h_A\|_{L^{2m}(\sigma)}^{2m}}{\|h_A\|_{L^2(\sigma)}^{2m}}=F_m(d(A)).}
\]
For \(m=1\) the ratio is \(1\), and for \(m=2\) it is the constant \(15/7\), independently of \(A\). For **every integer \(m\ge3\)**, the function \(F_m\) is strictly increasing on \([0,1/6]\), giving the sharp two-sided norm inequality
\[
\boxed{F_m(0)^{1/(2m)}\|h_A\|_2\le\|h_A\|_{2m}\le F_m(1/6)^{1/(2m)}\|h_A\|_2.}
\]
The lower equality cases are exactly those with eigenvalues proportional to \((1,0,-1)\); the upper equality cases are exactly those with eigenvalues proportional to \((2,-1,-1)\). All orthogonal conjugates and nonzero scalar multiples are included, and there are no others. In particular the first rigidity threshold is the sixth moment:
\[
\boxed{\frac{5625}{1001}\le\frac{\|h_A\|_6^6}{\|h_A\|_2^6}\le\frac{6625}{1001}.}
\]
Both endpoints are attained, and the foregoing two eigenvalue orbits characterize equality. This determines the entire interval of possible even-moment ratios as well as both sharp constants, since \(d(A)\) varies continuously across \([0,1/6]\).

## Assumptions and scope
The scalar field is real; \(\sigma\) is probability surface measure; \(m\) is an arbitrary positive integer. The matrix is real, symmetric and traceless, and nonzero. Spherical harmonics are defined as restrictions of homogeneous Euclidean harmonic polynomials. The norms use the same normalized measure. The moment formula makes no assertion about non-even exponents or arbitrary complex harmonics. By the degree-two harmonic identity \(\Delta(x^{\mathsf T}Ax)=2\operatorname{tr}A\), the matrix representation is exact.

## Proof
**1. Gaussian representation.** Write \(G=R\omega\), where \(G\) has three independent standard real Gaussian coordinates, \(R=\|G\|_2\), and \(\omega\) is independent of \(R\) and uniformly distributed under \(\sigma\). Since \(G^{\mathsf T}AG=R^2h_A(\omega)\),
\[
\mathbb E\,h_A(\omega)^{2m}=\frac{\mathbb E(G^{\mathsf T}AG)^{2m}}{\prod_{j=0}^{2m-1}(3+2j)},
\quad
\|h_A\|_2^2=\frac{2s_2}{15}.
\]
The first identity uses the \(4m\)-th moment of the Gaussian radius, not its \(2m\)-th moment.

**2. The exact cubic generating function.** Let \(\lambda_1,\lambda_2,\lambda_3\) be the real eigenvalues of \(A\). Because \(\sum\lambda_i=0\), Newton's identities give \(\sum_{i<j}\lambda_i\lambda_j=-s_2/2\) and \(\lambda_1\lambda_2\lambda_3=s_3/3\). Hence for \(z\) near zero,
\[
\mathbb E e^{zG^{\mathsf T}AG}=\det(I-2zA)^{-1/2}
=\left(1-2s_2z^2-\frac83s_3z^3\right)^{-1/2}.
\]
Use the absolutely convergent bivariate binomial series
\[
(1-X-Y)^{-1/2}=\sum_{j,k\ge0}\frac{(1/2)_{j+k}}{j!\,k!}X^jY^k.
\]
In the coefficient of \(z^{2m}\), the identity \(2j+3k=2m\) forces \(k=2\ell\) and \(j=m-3\ell\). Multiplication by \((2m)!\), followed by the radial normalization and division by \((2s_2/15)^m\), gives exactly \(F_m(d(A))\).

**3. Exact spectral range.** The characteristic polynomial of \(A\) is
\[
t^3-\frac{s_2}{2}t-\frac{s_3}{3}.
\]
It has three real roots (including multiplicity), so its discriminant \(s_2^3/2-3s_3^2\) is nonnegative. Thus \(0\le d(A)\le1/6\). Equality at the upper endpoint is equivalent to a repeated eigenvalue, necessarily proportional to \((2,-1,-1)\). At the lower endpoint \(s_3=0\), and zero trace implies zero determinant; hence the spectrum is proportional to \((1,0,-1)\). Conversely these patterns attain the stated endpoints. Their continuous interpolation within the connected normalized trace-zero eigenvalue circle attains all intermediate discriminants.

**4. Sharp monotonicity and equality.** For \(m=1,2\) only the index \(\ell=0\) occurs, so the ratio is independent of \(d\); the second and fourth moments are respectively \(1\) and \(15/7\) after normalization. For \(m\ge3\), all coefficients of \(F_m(d)\) are positive and, crucially, its coefficient at \(d\) is strictly positive. Hence \(F_m\) is strictly increasing for nonnegative \(d\). The spectral range of step 3 therefore proves both sharp bounds and the full equality classification. Substituting \(m=3\) into the explicit polynomial gives \(F_3(0)=5625/1001\) and \(F_3(1/6)=6625/1001\). No numerical or finite-dimensional enumeration is used to establish the quantified claims.

## Verification
The included standalone Python 3 program `artifacts/verify_even_spherical.py` reconstructs normalized sphere moments directly from the Dirichlet half-parameter monomial formula and independently from the cubic Gaussian generating function using exact rational arithmetic. It compares 640 moments across rational spectra and even powers through sixteen, independently checks both sixth-moment endpoints and fourth-moment constancy, confirms positivity of the discriminant coefficients for a finite range of orders, and compares extremal values for a rational grid of trace-zero matrices. Its finite tests corroborate, but do not replace, the analytical proof.

## Relationship to prior work
Stanton and Weinstein (1981) and Lu (1987) address the fourth-power extremal problem. A separately published exact degree-two \(L^4/L^2\) result establishes that the real quadratic harmonics on \(\mathbb S^2\) all have the same normalized fourth moment; this is the \(m=2\) boundary recovered here, **not a claimed novelty**. The present theorem begins at the next even moment and determines, simultaneously for every order \(2m\ge6\), both sharp constants and the complete opposite extremal eigenvalue families.

Sogge and Zelditch (first posted 2010-10-31), Han (first posted 2014-04-20), and Dai, Feng and Tikhonov (first posted 2014-08-06) study asymptotic norm-growth, orthonormal bases, and reverse Hölder orders as the harmonic degree tends to infinity; their inspected texts do not assert the fixed-degree-two exact hierarchy above. A known sharp three-point skewness–kurtosis inequality constrains the eigenvalue discriminant but does not state the even-moment formula or associated harmonic norm extremizers. Searches and comparisons did not locate an equivalent entire hierarchy, but non-indexed invariant-theory or spherical-quadratic-moment literature could contain one.

## Limitations
Only real degree-two harmonics on the two-sphere and integer even exponents are treated. The positive-coefficient argument does not compare arbitrary real \(p>4\), and no assertion is made about complex-coefficient harmonics or higher harmonic degrees. Prior results on quartic norms and spectral discriminants are explicitly retained as prior work. Independent external mathematical validation has not been performed.

## References
1. R. J. Stanton and A. Weinstein, “On the L4 norm of spherical harmonics,” *Mathematical Proceedings of the Cambridge Philosophical Society* **89** (1981), 343–358, DOI 10.1017/S0305004100058229.
2. J.-H. Lu, “A note on a theorem of Stanton-Weinstein on the L4-norm of spherical harmonics,” *Mathematical Proceedings of the Cambridge Philosophical Society* **102** (1987), 561–563, DOI 10.1017/S0305004100067591.
3. C. D. Sogge and S. Zelditch, “Concerning the L4 norms of typical eigenfunctions on compact surfaces,” arXiv:1011.0215v1, first posted 2010-10-31; https://arxiv.org/abs/1011.0215.
4. X. Han, “Spherical harmonics with maximal Lp (2<p<=6) norm growth,” arXiv:1404.5016v1, first posted 2014-04-20; https://arxiv.org/abs/1404.5016.
5. F. Dai, H. Feng and S. Tikhonov, “Reverse Hölder's inequality for spherical harmonics,” arXiv:1408.1877v1, first posted 2014-08-06; https://arxiv.org/abs/1408.1877.
6. “Sharp L4/L2 norm and extremizers for degree-two spherical harmonics,” publicly available 2026, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-sharp-l4-degree-two-spherical-harmonics--d4106097159f.

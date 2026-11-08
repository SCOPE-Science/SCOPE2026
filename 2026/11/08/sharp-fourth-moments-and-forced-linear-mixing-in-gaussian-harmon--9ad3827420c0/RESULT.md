# Sharp fourth moments and forced linear mixing in Gaussian harmonic quadratics

## Finding
Let \(n\ge2\) be an integer, \(G\sim N(0,I_n)\), \(A\) a real symmetric trace-free \(n\times n\) matrix, and \(b\in\mathbb R^n\). Put
\[
F_{A,b}(G)=G^{\mathsf T}AG+b\cdot G.
\]
For every \((A,b)\ne(0,0)\), the normalized fourth moment obeys the **sharp** bounds
\[
\boxed{3\le K_n(A,b):=\frac{\mathbb E F_{A,b}^4}{(\mathbb E F_{A,b}^2)^2}
\le 3+\frac{12(n-1)^3}{n(n^2-n-1)}=:C_n.}
\]
The lower equality cases are exactly \(A=0\) and \(b\ne0\). The upper equality cases are exactly
\[
A=t\left(ww^{\mathsf T}-\frac{I_n}{n}\right),\quad
\|w\|_2=1,\quad t\ne0,\quad
b\parallel w,\quad
\frac{\|b\|_2^2}{2\operatorname{tr}(A^2)}=\frac{n-2}{(n-1)^2}.
\]
In dimension two, the last ratio is zero, so \(b=0\); in every dimension at least three the upper extremizer necessarily mixes its first and second Gaussian chaos components. All values between the endpoints occur. For example, \(C_2=9\), \(C_3=47/5\), and \(C_n\to15\) as \(n\to\infty\).

For \(A\ne0\), write \(S=\operatorname{tr}(A^2)>0\), \(U=\operatorname{tr}(A^4)\), \(B=\|b\|_2^2\), and \(T=b^{\mathsf T}A^2b\). Define
\[
\rho=\frac{B}{2S},\qquad \nu=\frac{U}{S^2},\qquad
\gamma=\begin{cases}T/(SB),&B>0,\\0,&B=0,\end{cases}
\]
\[
\beta_n=\frac{n-1}{n},\qquad
u_n=\frac{n^2-3n+3}{n(n-1)},\qquad
\rho_n^*=\frac{n-2}{(n-1)^2},\qquad
c_n=\frac{\beta_n^2}{2\beta_n-\nu_n}.
\]
The **exact nonnegative upper deficit** is
\[
\boxed{C_n-K_n(A,b)=\frac{12}{(1+\rho)^2}
\left[ (\nu_n-\nu)+2\rho(\beta_n-\gamma)
+c_n(\rho-\rho_n^*)^2\right].}
\]
Each bracketed summand is nonnegative. In particular the identity separates spectral fourth-power concentration, directional alignment, and the energy allocation between the two degrees.

## Assumptions and scope
All coefficients and Gaussian variables are real. The Gaussian law is standard and isotropic, and the norm is \(\|F\|_p=(\mathbb E|F|^p)^{1/p}\). The trace-free condition makes the quadratic polynomial harmonic in the Euclidean variables and removes its constant Gaussian-chaos component. The first and second homogeneous Gaussian-chaos components are orthogonal in \(L^2\). The claim concerns the full direct sum of this harmonic quadratic space with the linear space, not a restriction to diagonal matrices or pure quadratics. The only excluded coefficient choice is the zero function. For \(A=0\), the upper-deficit parametrization is not used; the main bound is immediate by Gaussian fourth moments.

## Proof
**Step 1: exact Gaussian moments.** Orthogonally diagonalize \(A\), transforming \(b\) by the same orthogonal matrix. For a single standard Gaussian \(Z\) and real \(a,c\), direct expansion using \(\mathbb EZ^{2j}=(2j-1)!!\) gives
\[
\mathbb E[a(Z^2-1)+cZ]^2=2a^2+c^2,
\]
\[
\mathbb E[a(Z^2-1)+cZ]^4
=60a^4+60a^2c^2+3c^4.
\]
The centered independent coordinate summands have vanishing first moment, so multiplying out their fourth power yields
\[
\boxed{\mathbb E F_{A,b}^2=B+2S,\qquad
\mathbb E F_{A,b}^4=3(B+2S)^2+48(U+T).}\tag{1}
\]
In particular \(K_n\ge3\), with equality if and only if \(A=0\): if \(A\ne0\), then \(U>0\), while \(T=\|Ab\|_2^2\ge0\).

**Step 2: two sharp spectral inequalities.** If \(\lambda_1,\ldots,\lambda_n\) are real, zero-sum eigenvalues, then
\[
\max_i\lambda_i^2\le\beta_n\sum_i\lambda_i^2,
\quad\sum_i\lambda_i^4\le\nu_n\Big(\sum_i\lambda_i^2\Big)^2.\tag{2}
\]
The first inequality follows from \(\lambda_i=-\sum_{j\ne i}\lambda_j\) and Cauchy--Schwarz; equality holds precisely when the other \(n-1\) eigenvalues coincide.

For completeness, the second inequality and its maximizers follow from a constrained calculation. For \(n=2,3\), the zero-sum identity is \(\sum_i\lambda_i^4=\tfrac12(\sum_i\lambda_i^2)^2\), which equals \(\nu_n\) in these dimensions. Suppose \(n\ge4\), normalize \(\sum_i\lambda_i^2=1\), and maximize \(\sum_i\lambda_i^4\) under the zero-sum constraint. The two constraint gradients are independent. The Lagrange equations say that all coordinate values are roots of one cubic \(4x^3-2ux-v=0\), so at most three values occur. If three distinct values \(a<c<d\) occur, their sum is zero by the vanishing quadratic coefficient of the cubic. At its two extreme roots the second derivative of the Lagrangian is strictly positive, since it equals the derivative of \(4(x-a)(x-c)(x-d)\). Therefore neither extreme value may repeat: swapping \(+\varepsilon\) and \(-\varepsilon\) between two equal extreme coordinates would be tangent to both constraints and produce positive second variation, contradicting maximality. Consequently the middle value occurs \(n-2\) times. The constraints \(a+c+d=0\) and \(a+(n-2)c+d=0\) imply \(c=0\) and \(a=-d\), so the normalized fourth-power sum is \(1/2\), strictly below \(\nu_n\) for \(n\ge4\). Thus every maximizer has two distinct values. If one occurs \(k\) times, the other \(n-k\) times, direct substitution yields
\[
\frac{\sum_i\lambda_i^4}{(\sum_i\lambda_i^2)^2}
=\frac{n}{k(n-k)}-\frac3n.
\]
This is largest for \(k=1\) or \(k=n-1\), giving \(\nu_n\). Equality for \(n\ge4\) requires one outlier and \(n-1\) equal eigenvalues. In every dimension the maximum-square equality in the first inequality singles out that same spectral pattern.

**Step 3: directional inequality and scalar optimization.** For \(A\ne0\), the Rayleigh bound and (2) give \(0\le\gamma\le\beta_n\) when \(B>0\), and \(\nu\le\nu_n\). Equation (1) becomes
\[
K_n(A,b)=3+\frac{12(\nu+2\rho\gamma)}{(1+\rho)^2}
\le3+\frac{12(\nu_n+2\beta_n\rho)}{(1+\rho)^2}.\tag{3}
\]
For all \(\rho\ge0\), the rightmost function is maximized at
\[
\rho=1-\frac{\nu_n}{\beta_n}=\frac{n-2}{(n-1)^2}=\rho_n^*,
\]
including the endpoint \(\rho_n^*=0\) when \(n=2\). Its maximum is \(3+12c_n\), and algebra gives
\[
c_n=\frac{(n-1)^3}{n(n^2-n-1)}.
\]
The scalar optimization has the exact remainder identity
\[
c_n(1+\rho)^2-(\nu_n+2\beta_n\rho)
=c_n(\rho-\rho_n^*)^2.\tag{4}
\]
Subtract (1)--(3) and use (4) to obtain the displayed three-term upper deficit, proving sharpness and every claimed nonnegativity.

**Step 4: equality and full range.** Equality requires all three deficit terms to vanish. The scalar condition is \(\rho=\rho_n^*\), which is strictly positive for \(n\ge3\). Equality in the first spectral inequality and the directional Rayleigh inequality forces
\(A=t(ww^{\mathsf T}-I_n/n)\), \(b\parallel w\) with \(t\ne0\), and then the fourth-power inequality also saturates. For \(n=2\), \(\rho=0\), and every nonzero trace-free symmetric \(A\) is of the same displayed one-outlier form. Conversely, these configurations saturate every term. The normalized \(L^2\)-unit sphere of coefficient pairs is connected for \(n\ge2\), and the quotient is continuous, so every intermediate value is attained.

## Verification
Run `python3 verify.py` from the same directory. The program needs only the Python standard library. It independently expands fourth moments of non-diagonal Gaussian polynomials in exact rational arithmetic for 36 coefficient instances, compares those moments with (1), checks the exact upper deficit for each instance, verifies the endpoint algebra in every integer dimension from two through eighty, and checks the sharp spectral inequalities on small integer grids. These are diagnostics; the proof above, not finite tests, establishes the result for every admissible coefficient and dimension. The computation explicitly checks non-diagonal examples rather than assuming a diagonal-only claim.

## Relationship to prior work
Riener's symmetric-polynomial degree principles provide general context for two-level extremization; they neither involve Gaussian first--second chaos interactions nor give the sharp constant here. Sharma and collaborators investigate fourth-central-moment bounds for bounded distributions and corresponding eigenvalue spread inequalities, without the mixed Gaussian harmonic optimization. Pang's later pure-quadratic Gaussian moment theorem covers arbitrary symmetric matrices with \(b=0\); it cannot imply this sharp trace-free **mixed** bound, whose upper extremizers have \(b\ne0\) for \(n\ge3\). A published exact analysis of complex zero-sum \(\ell_4\) hyperplanes contains the real spectral inequality (2) as a lemma, but not the Gaussian mixed-component identity or the optimal allocation \(\rho_n^*\). Classical general bounds for moments of linear and quadratic forms, including Whittle's 1960 paper, are relevant background; its accessible abstract does not establish coverage of the sharp restricted inequality. The latter full-text comparison remains unresolved.

## Limitations
The result is restricted to real Gaussian polynomial coefficients, standard isotropic Gaussian measure, harmonic trace-free quadratic part, and exponent four. It does not settle sharp norms for non-Gaussian measures, higher Wiener chaoses, higher moments, or unrestricted nonzero-trace affine quadratics. The historical literature may contain an equivalent formulation under different terminology. The algebraic stability identity is exact but is not asserted to give an optimal metric-distance-to-extremizers constant. Independent external mathematical validation has not been performed.

## References
1. C. Riener, *On the degree and half degree principle for symmetric polynomials*, arXiv:1001.4464v1, first publicly submitted 2010-01-25, https://arxiv.org/abs/1001.4464. Full HTML of the paper examined (including Theorems 1.1 and 1.3 and the symmetric-optimization framework).
2. R. Sharma, R. Kumar, R. Saini and G. Kapoor, *Complementary upper bounds for fourth central moment with extensions and applications*, arXiv:1503.03786v1, first publicly submitted 2015-03-12, https://arxiv.org/abs/1503.03786. Full HTML examined, especially Sections 2 and 3.
3. Z. Pang, *A Gamma envelope and sharp moment inequalities for Gaussian quadratic forms*, arXiv:2609.05914v1, publicly submitted 2026-09-05, https://arxiv.org/abs/2609.05914. Inspected the introduction and exact pure-quadratic formulation, including Theorem 1.1 and Section 2.
4. *Exact complex Euclidean distortion of zero-sum \(\ell_4\) hyperplanes*, public research result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-complex-euclidean-distortion-of-zero-sum-ell-4-hyperplanes--f5d77d1ed7ff. Full RESULT.md examined, especially the proof of the real zero-sum fourth-moment lemma.
5. P. Whittle, *Bounds for the Moments of Linear and Quadratic Forms in Independent Variables*, Theory of Probability and Its Applications 5 (1960), 302--305, https://doi.org/10.1137/1105028. Abstract consulted; full text unavailable in this comparison.

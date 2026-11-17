# Determinant law and a critical-exponent reversal for the Cartesian radius of traceless two-by-two matrices

## Finding
For a nonzero complex \(2\times2\) matrix \(T\) with \(\operatorname{tr}T=0\), put \(F=\|T\|_{\mathrm F}=(\operatorname{tr}T^*T)^{1/2}\), \(\rho=2|\det T|/F^2\in[0,1]\), and, for each real \(1\le p<\infty\), define the Cartesian radius
\[
\omega_{\mathrm{Cart},p}(T)=\left(\frac1{2\pi}\int_0^{2\pi}\left\|\operatorname{Re}(e^{-i\theta}T)\right\|_{\mathrm{op}}^p\,d\theta\right)^{1/p}.
\]
Then its complete two-invariant formula is
\[
\boxed{\omega_{\mathrm{Cart},p}(T)=\frac F2\left[\frac1{2\pi}\int_0^{2\pi}(1+\rho\cos 2\theta)^{p/2}\,d\theta\right]^{1/p}}.
\]
Equivalently the bracketed integral equals \({}_2F_1(-p/4,(2-p)/4;1;\rho^2)\), with the endpoint interpreted by continuity. Write \(c_p=(\pi^{-1/2}\Gamma((p+1)/2)/\Gamma((p+2)/2))^{1/p}\). For \(1\le p<2\), the sharp bounds are
\[
\frac{c_p}{\sqrt2}F\le\omega_{\mathrm{Cart},p}(T)\le\frac F2,
\]
where the lower equality holds exactly for nonzero normal traceless matrices and the upper equality exactly for nonzero nilpotent traceless matrices. For \(p>2\) the inequalities reverse:
\[
\frac F2\le\omega_{\mathrm{Cart},p}(T)\le\frac{c_p}{\sqrt2}F,
\]
with lower equality exactly for nonzero nilpotents and upper equality exactly for nonzero normal traceless matrices. At the critical exponent \(p=2\), every such matrix satisfies \(\omega_{\mathrm{Cart},2}(T)=F/2\). For each fixed \(p\ne2\), the radius divided by \(F\) is strictly monotone in the determinant ratio \(\rho\), decreasing when \(p<2\) and increasing when \(p>2\). Its exact quadratic response near nilpotency is \(\omega_{\mathrm{Cart},p}(T)/(F/2)=1+(p-2)\rho^2/16+O_p(\rho^4)\).

## Assumptions and scope
All matrices act on the standard complex Hilbert plane; \(\operatorname{Re}S=(S+S^*)/2\), \(\|\cdot\|_{\mathrm{op}}\) is the spectral norm, and \(\|\cdot\|_{\mathrm F}\) the Frobenius norm. The exponent range is \(1\le p<\infty\). No assumption of normality, invertibility, or real entries is imposed. The zero matrix is excluded only to define \(\rho\); its Cartesian radius is zero. The determinant ratio is bounded by one because \(2|\det T|\le\operatorname{tr}(T^*T)\), with equality exactly for equal singular values. For a nonzero traceless two-by-two matrix, equal singular values are equivalent to normality, whereas vanishing determinant is equivalent to nilpotency.

## Proof
Write \(T=H+iK\), with \(H=H^*\) and \(K=K^*\). Both are traceless. Every traceless Hermitian \(2\times2\) matrix \(X\) satisfies \(X^2=\frac12\operatorname{tr}(X^2)I\) by Cayley--Hamilton; therefore \(\|X\|_{\mathrm{op}}^2=\frac12\operatorname{tr}(X^2)\). Set \(a=\frac12\operatorname{tr}(H^2)\), \(b=\frac12\operatorname{tr}(K^2)\), \(c=\frac12\operatorname{tr}(HK)\), all real. For \(A_\theta=H\cos\theta+K\sin\theta\),
\[
\|A_\theta\|_{\mathrm{op}}^2=a\cos^2\theta+b\sin^2\theta+2c\sin\theta\cos\theta
=\frac{a+b}2+\frac{a-b}2\cos2\theta+c\sin2\theta.
\]
The Frobenius identity is \(F^2=2(a+b)\). Also
\[
\operatorname{tr}(T^2)=2(a-b)+4ic=-2\det T,
\]
where the last equality uses \(\operatorname{tr}T=0\) and Cayley--Hamilton. Consequently \(\sqrt{(a-b)^2+4c^2}=|\det T|\). The oscillatory amplitude is \(|\det T|/2\), whereas the mean is \(F^2/4\). A shift of the angular variable therefore gives
\[
\|A_\theta\|_{\mathrm{op}}^2=\frac{F^2}4\bigl(1+\rho\cos(2\theta-\phi)\bigr)
\]
for some \(\phi\), proving the exact integral formula.

For \(|\rho|<1\), expand \((1+\rho\cos t)^{p/2}\) by the binomial series and integrate even powers. The identity \(\frac1{2\pi}\int_0^{2\pi}\cos^{2j}t\,dt=\binom{2j}j/4^j\) yields the stated hypergeometric series. Dominated convergence handles \(\rho=1\).

Let \(r=p/2\) and \(G_r(s)=\frac1{2\pi}\int_0^{2\pi}(1+s\cos t)^r\,dt\), \(0\le s\le1\). If \(r>1\), strict convexity of the scalar power shows \(G_r\) is strictly convex on \([0,1)\); if \(0<r<1\), it is strictly concave. Moreover \(G_r\) is even in \(s\), so is strictly increasing or decreasing, respectively, on \((0,1]\). At \(r=1\), \(G_1\equiv1\). The endpoints are \(G_r(0)=1\) and
\[
G_r(1)=\frac1{2\pi}\int_0^{2\pi}(2\cos^2(t/2))^r\,dt=2^{p/2}c_p^p.
\]
These give both optimal inequalities and strict equality characterizations. Expanding the even binomial series at \(\rho=0\) gives \(G_{p/2}(\rho)=1+p(p-2)\rho^2/16+O_p(\rho^4)\), and taking the \(p\)-th root yields the asserted quadratic response. Finally, \(\rho=0\) means \(\det T=0\), hence \(T^2=0\), and \(\rho=1\) means the two singular values coincide, hence \(T\) is a scalar multiple of a unitary; tracelessness then makes it unitarily diagonalizable with eigenvalues \(\lambda,-\lambda\). Both endpoints occur, for example for \(T=\begin{pmatrix}0&1\\0&0\end{pmatrix}\) and \(T=\operatorname{diag}(1,-1)\).

## Verification
The included `verify.py` is a standalone Python standard-library checker. It reconstructs the exact angular moments from a six-rational-parameter representation of all pairs of traceless Hermitian matrices and compares them with the determinant formula for \(p=2,4,6,8,10\). It also compares matrix-level rotational integrals and the invariant formula for \(p=1,3,5,7\) over deterministic samples. These checks supplement rather than prove the all-real-exponent theorem. In particular the strict monotonicity and the endpoint classifications follow from the analytical convexity and singular-value arguments above. As a sample exact specialization,
\[
\omega_{\mathrm{Cart},4}(T)^4=\frac{F^4}{16}+\frac{|\det T|^2}{8}.
\]

## Relationship to prior work
Audeh, Kittaneh, Moradi, and Sahoo introduced the \(L^p\)-Cartesian radius and obtained universal inequalities against the ordinary numerical radius; their Theorems 18 and 23 give general bounds and examples, but not this determinant classification, the complete fixed-Frobenius extremizers, or the critical exponent reversal. A related public research record derives the \(p=2\) radius of rank-one operators from their overlap; its nilpotent rank-one special case is contained here but neither implies the invertible traceless formula nor addresses all \(p\). Another published result studies finite-spectral unitaries for the \(L^2\) radius; its normal endpoint is compatible with, but does not imply, the nonnormal all-\(p\) classification. The proof uses classical Cayley--Hamilton, singular-value inequalities, and elementary angular averaging; these ingredients are not claimed as new.

## Limitations
The formula is specific to trace-zero complex two-by-two matrices; it is not an all-matrix inequality in larger dimensions. The exponent is finite with \(p\ge1\). The novelty assessment is a targeted comparison, not a mathematical proof of publication priority: earlier equivalent results under differing terminology remain possible. No independent external audit has been performed. All numerical checks are finite supporting diagnostics.

## References
1. W. Audeh, F. Kittaneh, H. R. Moradi, S. Sahoo, *The \(L^2\)-Cartesian Numerical Radii of Hilbert Space Operators*, arXiv:2610.04844v2 (first public version 4 October 2026), especially Definition (1.1), Theorem 18, Theorem 23 and Proposition 24. https://arxiv.org/abs/2610.04844
2. Public research record, *Exact rank-one overlap profile for the \(L^2\)-Cartesian numerical radius*, identifier 846b702b24b7 (2026), compared for the special rank-one case.
3. Public research record, *Exact projective spectral-gap formula and optimal finite spectra for the \(L^2\)-Cartesian radius of unitaries*, identifier f6644dc86b39 (2026), compared for the normal finite-spectrum case.

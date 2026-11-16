# Sharp quintic two-erasure stability for Chebyshev–Lobatto cosine sampling

## Finding

Fix an integer \(N\ge4\). Set \(x_j=\cos(j\pi/N)\) for \(0\le j\le N\), and set the endpoint-half weights \(w_0=w_N=1/2\) and \(w_j=1\) for \(1\le j\le N-1\). Let \(v_0=v_N=1/2\), \(v_k=1\) otherwise, and define the real orthogonal discrete-cosine matrix
\[
Q_{jk}=\sqrt{\frac{2w_jv_k}{N}}\cos\!\left(\frac{jk\pi}{N}\right),
\qquad 0\le j,k\le N.
\]

For any two *distinct* erased node indices \(0\le j<\ell\le N\), let \(A_{N;j,\ell}\) be the square \((N-1)\)-by-\((N-1)\) submatrix of \(Q\) obtained by removing rows \(j,\ell\) and retaining the polynomial-frequency columns \(0,\ldots,N-2\). Thus \(A_{N;j,\ell}\) represents quadrature-weighted, coefficient-orthonormal Chebyshev sampling of polynomials of degree at most \(N-2\) after exactly two observations are lost.

**Complete spectrum.** Put \(t_{j\ell}=w_j(x_j^2+1/2)+w_\ell(x_\ell^2+1/2)\). Then the squared singular values of \(A_{N;j,\ell}\), counted with multiplicity, are
\[
\underbrace{1,\ldots,1}_{N-3\ \mathrm{copies}},\qquad
\mu_{j\ell}^{\pm}=\frac{t_{j\ell}\pm\sqrt{t_{j\ell}^2-2w_jw_\ell(x_j-x_\ell)^2}}{N}.
\]
Both nontrivial eigenvalues are positive, so **every** two-erasure pattern remains exactly reconstructible.

**Sharp extremizers.** Among all unordered pairs of erased nodes, the unique minimizing patterns, up to the reflection \(j\mapsto N-j\), are \(\{0,1\}\) and \(\{N-1,N\}\). Writing \(c_N=\cos(\pi/N)\), \(\delta_N=1-c_N\), and \(t_N=5/4+c_N^2\), the exact worst squared singular-value floor is
\[
\alpha_N=\frac{t_N-\sqrt{t_N^2-\delta_N^2}}{N}
=\frac{\delta_N^2}{N\bigl(t_N+\sqrt{t_N^2-\delta_N^2}\bigr)}.
\]
The squared-analysis condition ratio (largest divided by smallest squared singular value) has the exact sharp value
\[
\kappa_N=\frac{N\bigl(t_N+\sqrt{t_N^2-\delta_N^2}\bigr)}{\delta_N^2},
\qquad
\lim_{N\to\infty}\frac{\kappa_N}{N^5}=\frac{18}{\pi^4}.
\]
In particular, the limiting least singular-value constant is
\[
\lim_{N\to\infty}N^5\alpha_N=\frac{\pi^4}{18}.
\]
The exponent five is for the explicitly weighted, orthonormal Chebyshev–Lobatto model defined above, not for unweighted nodal data or a uniform-norm Lebesgue constant.

## Assumptions and scope

All matrices are exact real matrices. The coefficient basis consists of \(\sqrt{v_k}T_k\), where \(T_k(x)=\cos(k\arccos x)\), with the sampling normalization \(\sqrt{2w_j/N}\). The underlying discrete norm is quadrature-weighted, including the endpoint-half factors. The matrix has \(N+1\) original rows, \(N-1\) retained frequency columns, exactly two erased rows, and \(N-1\) surviving observations. Both erasures are known, distinct, and arbitrary. The condition number here is the ratio of squared singular values; its square root is the standard spectral two-norm condition number.

## Proof

**1. Orthogonality and the complementary-minor reduction.** The elementary discrete cosine identity
\[
\sum_{j=0}^{N}w_j\cos(jk\pi/N)\cos(jm\pi/N)
=\begin{cases}N/(2v_k),&k=m,\\0,&k\ne m,\end{cases}
\]
for \(0\le k,m\le N\) proves \(Q^TQ=I\). Partition \(Q\) by the retained/deleted rows and the retained/highest two columns:
\[
Q=\begin{pmatrix}A&C\\D&B\end{pmatrix},\qquad B=Q[\{j,\ell\},\{N-1,N\}].
\]
The identity \(AA^T+CC^T=I_{N-1}\), together with \(C^TC=I_2-B^TB\), implies that the spectrum of \(AA^T\) consists of \(N-3\) ones and the two eigenvalues of \(B^TB\). The latter claim includes multiplicities, even when the two eigenvalues coincide.

**2. Explicit two-dimensional spectrum.** Since
\[
\cos\!\left(\frac{(N-1)j\pi}{N}\right)=(-1)^j x_j,
\qquad \cos(j\pi)=(-1)^j,
\]
we have row \(j\) of \(B\) equal to \((-1)^j\sqrt{2w_j/N}\,(x_j,1/\sqrt2)\), and similarly for row \(\ell\). The trace and determinant of \(B^TB\) are
\[
\operatorname{tr}(B^TB)=\frac{2t_{j\ell}}{N},\qquad
\det(B^TB)=\frac{2w_jw_\ell(x_j-x_\ell)^2}{N^2}.
\]
Taking the characteristic roots gives \(\mu^{\pm}_{j\ell}\) as claimed. Because \(x_j\ne x_\ell\) and both quadrature weights are positive, the determinant is strictly positive. The full sampling matrix \(A\) is therefore invertible. As a contraction submatrix of an orthogonal matrix, its squared singular values are at most one. For \(N\ge4\), the \(N-3\) copies of one show that its largest squared singular value is exactly one.

**3. A uniform comparison for all erased pairs.** Write \(\Delta=|x_j-x_\ell|\) and \(u_i=(x_i,1/\sqrt2)\). The smaller eigenvalue obeys \(\mu^-_{j\ell}\ge\det(B^TB)/\operatorname{tr}(B^TB)\); the inequality follows from \(\mu^+\le\operatorname{tr}\). As \(x_i^2+1/2\le3/2\), this gives the explicit bound
\[
\mu^-_{j\ell}\ge
\frac{2w_jw_\ell}{3N(w_j+w_\ell)}\Delta^2.
\tag{1}
\]
For the candidate erased pair \(\{0,1\}\), use the unit vector orthogonal to \((1,1/\sqrt2)\), namely \((-1/\sqrt2,1)/\sqrt{3/2}\), in the Rayleigh quotient of \(B^TB\). It yields
\[
\mu^-_{01}\le\frac{2\delta_N^2}{3N}.
\tag{2}
\]
Now put \(\theta=\pi/N\). The nodal separation between any two distinct *interior* nodes is at least
\[
\cos\theta-\cos2\theta=(1+2\cos\theta)\delta_N>2\delta_N
\]
for \(N\ge4\), because the adjacent spacings of the cosine grid increase toward its center. With both weights one, (1) gives \(\mu^-_{j\ell}>4\delta_N^2/(3N)\), strictly exceeding (2).

If precisely one erased node is an endpoint but is *not* paired with its nearest neighbor, its separation is at least
\[
1-\cos2\theta=2(1+\cos\theta)\delta_N>3\delta_N.
\]
The weights are \(1/2\) and \(1\); (1) now gives \(\mu^-_{j\ell}>2\delta_N^2/N\), again strictly exceeding (2). If the two erased nodes are the two endpoints, their separation is two and both weights are \(1/2\), so (1) gives \(\mu^-_{0N}\ge 2/(3N)>2\delta_N^2/(3N)\), using \(0<\delta_N<1\). The only remaining pairs are \(\{0,1\}\) and \(\{N-1,N\}\). Reflection \(x\mapsto-x\) makes their eigenvalues identical. Thus these, and only these, are the global worst patterns for every \(N\ge4\).

**4. Exact sharp value and asymptotics.** For \(\{0,1\}\), the trace parameter is \(t_N=5/4+c_N^2\), and the square-root discriminant is \(t_N^2-\delta_N^2\). The displayed formula for \(\alpha_N\) follows by rationalization. Since \(\delta_N=\pi^2/(2N^2)+O(N^{-4})\) and \(t_N=9/4+O(N^{-2})\),
\[
\alpha_N=\frac{\pi^4}{18N^5}\bigl(1+O(N^{-2})\bigr),\qquad
\kappa_N=\frac{18N^5}{\pi^4}\bigl(1+O(N^{-2})\bigr).
\]
The exact largest squared singular value is one by step 2, completing the proof.

## Verification

The standalone file `check_dct1.py` implements the full orthogonal DCT-I matrix independently of the complementary-minor formula. For every \(4\le N\le52\) and every erased pair, it compares the two complementary singular values with the closed expressions; for \(4\le N\le20\), it also constructs the surviving matrix and compares its spectrum directly. It checks that the reflected endpoint-neighbor patterns, and no others, minimize the least squared singular value. High-degree evaluations check convergence to the analytically proved constant. It passed 52,800 deterministic assertions. To reproduce, run `python3 check_dct1.py` with Python and NumPy installed. Finite checks do not establish any of the all-order inequalities or historical priority.

## Relationship to prior work

The discrete cosine transform of type I and the Chebyshev–Lobatto weights are standard. Weisbrich, Malissiovas and Neitzel (2021, DOI below) explain high-order Chebyshev point-cloud interpolation on precisely the Lobatto nodes and analyze accuracy under noise, but their full open-access text does not provide two-erasure singular spectra or optimal failure patterns. Goren and Zamir (2021, DOI below) motivate erasure sensitivity in DCT-based coding, but their abstract does not determine this DCT-I theorem; their full article was unavailable for thorough inspection.

The published study *Single-erasure boundary layers for Chebyshev–Lobatto interpolation* (2026, published-finding corpus identifier `a3c5beff381f`) treats the \(L^\infty\) Lebesgue norm after one deletion and polynomial degree reduction by one, not the \(\ell^2\) weighted sampling spectrum after two deletions and degree reduction by two. A separate previous Gauss–Chebyshev DCT-II two-erasure result determines a different half-shifted grid and has a seventh-power, rather than fifth-power, worst conditioning law. Neither statement implies the present exact DCT-I spectrum or its minimizer classification. General complementary-minor identities are explicitly used as established tools, not claimed as new.

## Limitations

The theorem is tied to exact orthonormal DCT-I normalization with endpoint-half observation weights. It does not assert identical stability for unweighted observations, floating-point interpolation, unknown erasure locations, more than two erasures, or uniform-norm Lebesgue amplification. Neither numerical testing nor negative literature searches establish historical priority. A plausible DCT coding source was not readable in full, and older equivalent calculations might exist.

## References

1. S. Weisbrich, G. Malissiovas and F. Neitzel, “On the fast approximation of point clouds using Chebyshev polynomials,” *Journal of Applied Geodesy* 15 (2021), 305–317, DOI: `10.1515/jag-2021-0010`. First verified online publication: 2021-06-23. Full open-access HTML text inspected, especially sections 2–5.
2. M. Goren and R. Zamir, “Diversity Image Coding Using Irregular Interpolation,” *IEEE Transactions on Image Processing* 30 (2021), 5665–5677, DOI: `10.1109/TIP.2021.3087404`. Public record dated 2021-06-18; abstract inspected; complete paper access unsuccessful.
3. SciPy documentation, `scipy.fft.dct`, type-I definition and orthonormalization, https://docs.scipy.org/doc/scipy/reference/generated/scipy.fft.dct.html (technical baseline).
4. “Single-erasure boundary layers for Chebyshev–Lobatto interpolation,” published mathematical record (2026), identifier `a3c5beff381f`. The full publicly available result statement and proof were inspected to compare operators and norms.

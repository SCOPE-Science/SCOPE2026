# Laguerre boundary matrices and sharp Schatten laws for polyanalytic Bergman Toeplitz operators

## Finding
For every integer \(n\ge2\), real \(\alpha>-1\), and \(\sigma>0\), a bounded radial symbol whose boundary expansion begins with \(b(1-|z|^2)^\sigma\), \(b\ne0\), generates a compact Toeplitz operator with a sharp singular-value law determined by a finite Laguerre moment pencil. Define
\[
B_{jk}=\Gamma(\alpha+j+k+1),\qquad A_{jk}=\Gamma(\alpha+\sigma+j+k+1),\qquad 0\le j,k<n.
\]
Let \(\mu_1,\ldots,\mu_n>0\) be the generalized eigenvalues \(Av=\mu Bv\), including multiplicity, and put \(S=\sum_{i=1}^n\mu_i^{1/\sigma}\). The singular values in decreasing order, with multiplicity, obey
\[
\lim_{k\to\infty}k^\sigma s_k(T_a)=|b|S^\sigma,
\quad N(t;|T_a|)\sim |b|^{1/\sigma} S\,t^{-1/\sigma}\quad(t\downarrow0).
\]
In particular, for every \(p>0\), \(T_a\in\mathcal S_p\) if and only if \(p>1/\sigma\); it is weak-Schatten at the critical exponent and not in the strong endpoint. The logarithmic eigenvalue sum has the ordinary (non-generalized-limit) value
\[
\lim_{K\to\infty}{1\over\log K}\sum_{k=1}^K s_k(|T_a|^{1/\sigma})=|b|^{1/\sigma}S.
\]
For \(\sigma=1\), \(\mu_i\) are the \(n\) positive zeros of the generalized Laguerre polynomial \(L_n^{(\alpha)}\); hence \(S=n(n+\alpha)\). For \(n=2\) and \(\alpha=0\), a strict first-order Toeplitz-power anomaly occurs:
\[
\lim_{k\to\infty}k^2s_k(T_{(1-|z|^2)^2})=16+4\sqrt3
\ne16=\lim_{k\to\infty}k^2s_k(T_{1-|z|^2}^{\,2}).
\]

## Assumptions and scope
Work on the complex unit disk \(\mathbb D\) with probability measure \(d\nu_\alpha=(\alpha+1)(1-|z|^2)^\alpha dA(z)/\pi\). Let \(\mathcal A^2_{n,\alpha}\) denote all \(L^2(d\nu_\alpha)\) functions satisfying \(\partial_{\bar z}^{\,n}f=0\) in distributions. Let \(P_{n,\alpha}\) be orthogonal projection onto this closed space and \(T_a=P_{n,\alpha}M_a\) restricted to it. Assume \(a\) is essentially bounded, radial, and
\[
\lim_{y\downarrow0}\frac{a(\sqrt{1-y})}{y^\sigma}=b\ne0
\]
in the essential radial sense. Neither \(a\) nor \(b\) needs to be real. The positive matrices \(A,B\) are strictly positive definite because their quadratic forms are moments of \(|p(x)|^2 x^{\alpha+\sigma}e^{-x}\) and \(|p(x)|^2x^\alpha e^{-x}\). The singular counting function \(N(t;|T_a|)\) counts singular values strictly greater than \(t>0\). All stated limits hold for fixed \(n,\alpha,\sigma\), with no uniformity claimed when these parameters vary.

## Proof
**Angular sectors.** The space admits the orthogonal rotation decomposition into frequencies \(\xi=-n+1,-n+2,\ldots\). For each \(\xi\ge0\), the sector has dimension exactly \(n\) and consists of
\[
 f(re^{i\theta})=e^{i\xi\theta}r^\xi p(r^2),\qquad \deg p\le n-1.
\]
Indeed, its spanning monomials are \(z^{\xi+j}\bar z^j\), \(0\le j<n\). The finitely many negative-frequency sectors contribute only finitely many singular values and have no effect on any asymptotic or endpoint condition. Radial Toeplitz operators preserve each sector.

**Boundary scaling.** Write \(t=r^2\), \(y=1-t\), and \(x=\xi y\). The sector inner product is a fixed common positive multiple of
\[
\int_0^1 |p(t)|^2t^\xi(1-t)^\alpha\,dt.
\]
Under the invertible polynomial coordinate change \(p(t)=q(\xi(1-t))\), the basis \(1,x,\ldots,x^{n-1}\) has a Gram matrix, after cancelling the common factor \(\xi^{-\alpha-1}\), with entries
\[
G_{\xi,jk}=\int_0^\xi x^{\alpha+j+k}(1-x/\xi)^\xi\,dx.
\]
The radial-symbol matrix, after additionally removing \(\xi^{-\sigma}\), has entries
\[
H_{\xi,jk}=\int_0^\xi x^{\alpha+j+k+\sigma}(1-x/\xi)^\xi
\frac{a(\sqrt{1-x/\xi})}{(x/\xi)^\sigma}\,dx.
\]
By \((1-x/\xi)^\xi\le e^{-x}\), \(G_\xi\to B\) entrywise. For \(H_\xi\), fix \(0<\delta<1\) and split the integral at \(\delta\xi\). On the first interval, the boundary quotient is bounded and converges pointwise to \(b\), so dominated convergence applies with dominating function \(C x^{\alpha+j+k+\sigma}e^{-x}\). On the second interval, boundedness of \(a\) gives a bound \(C\xi^\sigma x^{\alpha+j+k}e^{-x}\), whose integral tends to zero. Therefore \(H_\xi\to bA\). All limiting matrices are finite-dimensional and \(B\) is positive definite.

**Sector asymptotics.** The sector operator has, in an orthonormal basis, matrix
\[
T_{a,\xi}=\xi^{-\sigma}G_\xi^{-1/2}H_\xi G_\xi^{-1/2}.
\]
Consequently \(\xi^\sigma T_{a,\xi}\to b B^{-1/2}AB^{-1/2}\) in matrix norm. Continuity of singular values yields, for each \(1\le i\le n\),
\[
s_i(T_{a,\xi})=\bigl(|b|\mu_i+o(1)\bigr)\xi^{-\sigma}
\quad(\xi\to\infty).
\]
No normality assumption on \(T_a\) is needed.

**Rearrangement and endpoint.** For every \(\varepsilon>0\), all sufficiently large \(\xi\) have sector singular values trapped between \((|b|\mu_i-\varepsilon)\xi^{-\sigma}\) and \((|b|\mu_i+\varepsilon)\xi^{-\sigma}\); choose \(\varepsilon<|b|\min_i\mu_i\). Counting the integer frequencies above threshold gives
\[
N(t;|T_a|)=\left(\sum_{i=1}^n(|b|\mu_i)^{1/\sigma}\right)t^{-1/\sigma}+o(t^{-1/\sigma}).
\]
Finite exceptional blocks add only \(O(1)\). Monotone inversion of this counting asymptotic gives the claimed \(s_k\) asymptotic. Since \(s_k(T_a)^p\sim (|b|S^\sigma)^p k^{-\sigma p}\), ordinary comparison with the harmonic series proves the strong Schatten criterion and exclusion at equality. The asymptotic \(s_k(|T_a|^{1/\sigma})\sim |b|^{1/\sigma}S/k\) proves the logarithmic limit by summation; its boundedness also proves weak-endpoint membership.

**Exact Laguerre values and power defect.** When \(\sigma=1\), the pencil \((A,B)\) represents the compression of multiplication by \(x\) on polynomials of degree less than \(n\) in \(L^2(x^\alpha e^{-x}dx)\). In the orthonormal generalized-Laguerre basis this is the standard Jacobi tridiagonal matrix, whose eigenvalues are the zeros of \(L_n^{(\alpha)}\); the sum of diagonal recurrence coefficients \(\alpha+1,\alpha+3,\ldots,\alpha+2n-1\) equals \(n(n+\alpha)\). For \(n=2,\alpha=0,\sigma=2\), in the orthonormal basis \(1,1-x\), multiplication by \(x^2\) has compression
\[
\begin{pmatrix}2&-4\\-4&14\end{pmatrix},
\qquad \mu_\pm=8\pm2\sqrt{13}.
\]
Thus \((\sqrt{\mu_+}+\sqrt{\mu_-})^2=16+4\sqrt3\). For \(\sigma=1\), \(\mu_++\mu_-=4\) and so \(s_k(T_{1-|z|^2})\sim4/k\). This positive operator has \(s_k(T_{1-|z|^2}^{\,2})\sim16/k^2\), proving the asserted leading discrepancy.

## Verification
The standalone `CHECK.py` computes exact beta moments for finite angular frequencies and independently evaluates the limiting two-dimensional Laguerre pencils at exponents \(\sigma=1,2\). It checks convergence from the actual finite-sector generalized eigenvalues at four large indices. These finite tests corroborate but do not replace the preceding infinite-dimensional dominated-convergence and rearrangement arguments. Run `python CHECK.py` with the standard Python library.

## Relationship to prior work
Barrera-Castelán, Maximenko, and Ramos-Vazquez (2020, arXiv:2009.14301; 2023, arXiv:2306.06231) establish rotation-sector representations of radial Toeplitz operators on full weighted polyanalytic Bergman spaces and qualitative scalar-limit structure for bounded radial symbols with boundary limits. Their published qualitative limit does not supply the renormalized \(\xi^\sigma\) matrix limit, a universal Laguerre moment pencil, or the sharp rearranged singular-value constant derived here. Pushnitski (arXiv:1710.02652) proves spectral asymptotics for ordinary analytic Bergman Toeplitz operators, which motivates comparison but does not entail the finite-multiplicity polyanalytic matrix pencil. Rozenblum and Vasilevski (arXiv:1907.06878) analyze upper-half-plane polyanalytic Toeplitz operators with singular symbols using reduction techniques; the present disk boundary-symbol and exact matrix-valued constants are not supplied by the inspected material.

## Limitations
Novelty is asserted only relative to the accessible works inspected, not as a guarantee against unindexed or inaccessible earlier results. The theorem concerns radial symbols on the full fixed-order polyanalytic disk space. The boundary hypothesis is stronger than a generic finite limit; no uniform estimate in increasing polyanalytic order is established. The spectral coefficient is asymptotic, not an exact formula for every finite sector. Independent external proof assessment has not been performed.

## References
1. R. M. Barrera-Castelán, E. A. Maximenko, G. Ramos-Vazquez, *Radial operators on polyanalytic weighted Bergman spaces* (2020), arXiv:2009.14301.
2. R. M. Barrera-Castelán, E. A. Maximenko, G. Ramos-Vazquez, *C*-algebras generated by radial Toeplitz operators on polyanalytic weighted Bergman spaces* (2023), arXiv:2306.06231v1 (first public: 2023-06-09).
3. A. Pushnitski, *Spectral asymptotics for a class of Toeplitz operators on the Bergman space* (2017), arXiv:1710.02652.
4. G. Rozenblum, N. Vasilevski, *Toeplitz operators with singular symbols in polyanalytic Bergman spaces on the half-plane* (2019), arXiv:1907.06878.

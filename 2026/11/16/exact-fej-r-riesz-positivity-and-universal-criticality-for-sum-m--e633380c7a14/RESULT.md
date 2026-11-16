# Exact Fejér–Riesz positivity and universal criticality for sum-modulated circle heat kernels

## Finding
For \(0<q<1\), integer \(M\ge1\), and real \(a_1,\ldots,a_M\), define on the circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\)
\[
H_q(t)=\sum_{n\in\mathbb Z}q^{n^2}e^{int},\qquad
K_{q,\boldsymbol a}(x,y)=H_q(x-y)\left(1+\sum_{j=1}^M a_j\cos(j(x+y))\right).
\]
Let \(m\) be normalized Haar measure and set
\[
w_{q,\boldsymbol a}(z)=1+\sum_{j=1}^M a_jq^{-j^2}\cos(2jz).
\]
**Classification:** \(K_{q,\boldsymbol a}\) is positive semidefinite on every finite subset of \(\mathbb T\) exactly when \(w_{q,\boldsymbol a}\ge0\) everywhere. On the full admissible parameter region, including its boundary, \(K_{q,\boldsymbol a}\) is strictly positive definite for every finite set of distinct sites and its RKHS is dense in \(C(\mathbb T)\).

For \(M=1\) this is the sharp interval \(|a_1|\le q\). For \(M=2\), write \(A=a_1/q\), \(B=a_2/q^4\). The sharp admissibility condition is
\[
\begin{cases}
1+B\ge |A|, & B\le0\text{ or }(B>0,\ |A|\ge4B),\
1-B-\dfrac{A^2}{8B}\ge0, & B>0,\ |A|\le4B.
\end{cases}
\]
The two branches coincide at their common boundary. The second branch is a curved frontier, rather than a finite affine polygon. At \(a_1=q,a_j=0\) for \(j\ge2\), \(w(z)=1+\cos(2z)\) has two zeros, but the kernel remains universal.

## Assumptions and scope
All coefficients are real; \(M\) is finite and at least one. The heat multiplier convention is \(q^{n^2}\), not a geodesic-distance Gaussian. Complex test vectors and arbitrary distinct circle sites are allowed. Positive semidefiniteness is required for every finite configuration. The condition \(w\ge0\) is pointwise, including zeros; no strictly positive lower bound is assumed.

## Proof
Fourier multiplication gives the exact double coefficients of the kernel:
\[
\widehat K(n,m)=q^{n^2}\mathbf1_{n=m}
+\sum_{j=1}^M\frac{a_j}{2}\,q^{((n+m)/2)^2}
\left(\mathbf1_{n-m=2j}+\mathbf1_{m-n=2j}\right).
\]
For \(n-m=2j\), the identity
\[
q^{((n+m)/2)^2}=q^{(n^2+m^2)/2}q^{-j^2}
\]
shows, term by term, that the double Fourier series is exactly
\[
\boxed{K(x,y)=\int_{\mathbb T}H_{\sqrt q}(x-z)\,w_{q,\boldsymbol a}(z)\,H_{\sqrt q}(z-y)\,dm(z).}
\]
All series converge absolutely and uniformly, so coefficient matching is legitimate. Hence positivity of \(w\) suffices.

Conversely, if the continuous \(w\) is negative on an arc, choose a nonzero trigonometric polynomial \(g\) for which \(\int w|g|^2dm<0\); trigonometric polynomials approximate a function supported in that arc in \(L^2\). Because every Fourier multiplier \(q^{n^2/2}\) is nonzero, write \(g=H_{\sqrt q}*f\) with another trigonometric polynomial \(f\). The integral operator with kernel \(K\) then has negative quadratic form on \(f\). If every finite evaluation Gram matrix were positive semidefinite, approximation of the integral by Riemann sums would make every such operator quadratic form nonnegative, a contradiction. Thus pointwise nonnegativity is necessary.

Now suppose \(w\ge0\). Its constant Fourier coefficient is one, so it is a nonzero trigonometric polynomial and has at most finitely many zeros on \(\mathbb T\). For any nonzero finite complex Borel measure \(\nu\), the analytic function \(F(z)=\int_{\mathbb T}H_{\sqrt q}(x-z)\,d\nu(x)\) is not identically zero: its Fourier coefficients are the nonvanishing Gaussian multipliers times the Fourier–Stieltjes coefficients of \(\nu\), which determine the measure. Therefore
\[
\iint K(x,y)\,d\nu(x)\,d\overline{\nu}(y)
=\int w(z)|F(z)|^2dm(z)>0.
\]
The same inequality for nonzero atomic \(\nu\) proves finite-site strict positive definiteness. For any nonzero finite signed/complex measure it proves uniform density of the kernel's RKHS in \(C(\mathbb T)\) by Hahn–Banach and the Riesz representation theorem.

For \(M=2\), write \(u=\cos(2z)\in[-1,1]\). Then \(w=1-B+Au+2Bu^2\). If \(B\le0\), the minimum is at an endpoint and equals \(1+B-|A|\). If \(B>0\), the minimum occurs at \(u=-A/(4B)\) when \(|A|\le4B\), giving \(1-B-A^2/(8B)\); otherwise it occurs at an endpoint, giving \(1+B-|A|\). This proves the complete two-harmonic conditions.

For an exact inadmissibility witness, choose \(q=1/2\), \(M=1\), \(a_1=11/20\). Then \(w(z)=1+(11/10)\cos(2z)\) and \(g(z)=\sum_{k=0}^{11}(-1)^k e^{2ikz}\) satisfies \(\int w|g|^2dm=12-(11/10)11=-1/10\). Pulling back its finitely supported Fourier coefficients by the invertible Gaussian multipliers yields a negative quadratic form of the specified kernel.

## Verification
The accompanying self-contained Python script `check_gaussian_sum_modulation.py` uses rational arithmetic to verify the Fourier factorization for \(q\in\{1/2,2/3,3/5\}\), several sign-changing and boundary coefficient choices, and all \(n,m\in[-11,11]\); it separately checks the exact quadratic minimization over a rational parameter grid. It reports 9,206 passed exact identities/tests. The universal theorem rests on the analytic proof above, not finite testing.

## Relationship to prior work
The classical Fejér–Riesz theorem represents nonnegative trigonometric polynomials as polynomial modulus squares; it is used as context, not claimed as new. The nonstationary spectral representation and factorization viewpoint occurs in Jawaid–Karatas–Seewig (2026). Their inspected method constructs finite-rank approximations for harmonizable covariance kernels, whereas this theorem gives an exact positivity criterion, all-coefficient classification, and boundary universality for the explicit periodic sum-modulated heat family. A related published circle-Poisson result treats a single sum-coordinate harmonic, with a different threshold and possible finite-site singularities; the present heat family has a full arbitrary-degree polynomial criterion and universal boundary.

## Limitations
This concerns finite trigonometric sum-coordinate modulations of the genuine periodic heat kernel, not arbitrary nonstationary kernels or the Gaussian of squared geodesic distance. There is no uniform inverse/coercivity estimate at polynomial zeros, and no general classification of infinite Fourier modulations. Older equivalent cases in harmonizable-kernel or Toeplitz literature may exist; general spectral-factorization theory predates this work. Independent mathematical verification and publication priority determination have not been performed.

## References
1. A. Jawaid, A. Karatas, J. Seewig, *Regular Fourier Features for Nonstationary Gaussian Processes*, arXiv:2602.23006 (first public version February 26, 2026), https://arxiv.org/html/2602.23006.
2. T. T. Georgiou and A. Lindquist, *On a Fejér–Riesz factorization of generalized trigonometric polynomials*, arXiv:2005.11920, https://arxiv.org/abs/2005.11920.
3. *Sharp harmonic modulation cutoff and polygonal singularities for circle Poisson covariances*, published mathematical summary, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-harmonic-modulation-cutoff-and-polygonal-singularities-for--0f4219b7a6a9. Full text was not accessible at review.

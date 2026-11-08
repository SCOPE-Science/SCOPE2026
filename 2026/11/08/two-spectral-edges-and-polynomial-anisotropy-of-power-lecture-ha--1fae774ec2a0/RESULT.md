# Two spectral edges and polynomial anisotropy of power lecture-hall simplices

## Finding
Fix an integer \(p\geq0\). For every integer \(n\geq2\), consider the Euclidean lecture-hall simplex
\[
P_{n,p}=\{x\in\mathbb R^n:0\leq x_1/1^p\leq x_2/2^p\leq\cdots\leq x_n/n^p\leq1\}.
\]
Let \(X_{n,p}\) be uniformly distributed on its \(n+1\) distinct vertices, and let \(C_{n,p}=\operatorname{Cov}(X_{n,p})\), computed using the inherited Euclidean inner product. Write its eigenvalues in nonincreasing order as \(\lambda_{n,p,1}\geq\cdots\geq\lambda_{n,p,n}>0\). Put \(N=n+1\). For \(1\leq i,j\leq n\),
\[
(C_{n,p})_{ij}=i^pj^p\left(\frac{\min(i,j)}N-\frac{ij}{N^2}\right),\qquad
C_{n,p}^{-1}=N D_{n,p}^{-1}L_nD_{n,p}^{-1},
\]
where \(D_{n,p}=\operatorname{diag}(1^p,\ldots,n^p)\) and \(L_n\) is the tridiagonal Dirichlet matrix with diagonal \(2\) and neighboring entries \(-1\).

Set \(\nu_p=1/(2p+2)\), and let \(j_{\nu_p,k}\) be the \(k\)-th positive zero of the ordinary Bessel function \(J_{\nu_p}\). For every fixed positive integer \(k\),
\[
\boxed{\lim_{n\to\infty}\frac{\lambda_{n,p,k}}{n^{2p+1}}
=\kappa_{p,k}:=\frac1{(p+1)^2j_{\nu_p,k}^2}.}
\]
For \(p\geq1\), introduce the positive compact operator \(A_p\) on \(\ell^2(\mathbb N)\) with matrix entries
\[
(A_p)_{ij}=\frac{2}{i^{2p}}\mathbf1_{i=j}
-\frac1{i^pj^p}\mathbf1_{|i-j|=1}.
\]
Write its positive eigenvalues in nonincreasing order as \(\mu_{p,1}\geq\mu_{p,2}\geq\cdots>0\), and let \(\rho_p=\mu_{p,1}=\|A_p\|\). Then for every fixed positive integer \(r\),
\[
\boxed{\lim_{n\to\infty}n\lambda_{n,p,n-r+1}=\frac1{\mu_{p,r}}.}
\]
The entire two-ended asymptotic spectrum therefore gives the sharp Euclidean covariance condition-number law
\[
\boxed{\lim_{n\to\infty}\frac{\lambda_{n,p,1}/\lambda_{n,p,n}}{n^{2p+2}}
=\frac{\rho_p}{(p+1)^2j_{\nu_p,1}^2},\quad p\geq1.}
\]
The exponent can be any even integer at least four while the face lattice remains that of an \(n\)-simplex. For \(p=1\), the coefficient is approximately \(0.06958856836\); here \(\rho_1\approx2.152607271998\) and \(j_{1/4,1}\approx2.780887723995\).

At the unweighted endpoint \(p=0\), there is instead the exact elementary spectrum
\[
\lambda_{n,0,k}=\frac1{4(n+1)\sin^2(k\pi/[2(n+1)])},\quad1\leq k\leq n,
\]
so \(n\lambda_{n,0,n-r+1}\to1/4\) for every fixed \(r\), and the condition-number limit is \(4/\pi^2\) after division by \(n^2\). In particular, the hard-edge discrete hierarchy for positive powers collapses to a single level at zero power.

Finally, for every fixed \(p\geq0\),
\[
\lim_{n\to\infty}\frac{\operatorname{tr} C_{n,p}}{n^{2p+1}}
=\frac1{(2p+2)(2p+3)}
=\sum_{k=1}^{\infty}\kappa_{p,k}.
\]

## Assumptions and scope
The integer \(p\) is fixed as \(n\to\infty\); powers are not permitted to increase with dimension. The vertex measure is uniform on exactly \(n+1\) distinct vertices, **not** Lebesgue-uniform in the simplex and not a Gaussian law. The Euclidean metric is inherited from \(\mathbb R^n\), not transformed by normalization of the inequalities. The highest and lowest \(k\) eigenvalues are considered for each fixed \(k\); no uniform-in-index spectral approximation is claimed. The case \(p=0\) is included as a classical comparison; the new geometric content is the two-ended spectral splitting and anisotropy classification for \(p\geq1\).

## Proof
**1. Exact finite covariance.** The \(n+1\) vertices are the zero vector and the suffix vectors \(v^{(k)}\), where \(1\leq k\leq n\) and \(v_i^{(k)}=i^p\mathbf1_{k\leq i}\). Equivalently, choose \(J\) uniformly from \(\{1,\ldots,n+1\}\), and set \(X_i=i^p\mathbf1_{J\leq i}\). Then
\[
\mathbb E X_i=i^p i/N,\qquad
\mathbb E(X_iX_j)=i^pj^p\min(i,j)/N,
\]
which gives the displayed covariance exactly. Put \(B_{ij}=\min(i,j)-ij/N\). The matrix \(B\) is the inverse of the discrete Dirichlet second-difference matrix \(L_n\): applying its three-point difference to the piecewise affine function of the row index \(i\) yields the coordinate basis vector, with boundary values zero at \(i=0,N\). Thus \(C_{n,p}=D_{n,p}BD_{n,p}/N\) and the inverse formula follows. Both matrices are positive definite.

**2. The compact discrete hard edge.** Let \(A_{p,n}=D_{n,p}^{-1}L_nD_{n,p}^{-1}\), the leading principal \(n\)-by-\(n\) compression of \(A_p\). For \(p\geq1\), its matrix is tridiagonal, with absolute entries \(O(i^{-2p})\) in rows of index \(i\). The operator-norm difference between \(A_p\) and the zero-extended \(A_{p,n}\) tends to zero by a uniform tail row-sum bound; hence \(A_p\) is compact. It is positive and injective: for finitely supported \(u\), the quadratic form is the sum of squares of successive differences of \(u_i/i^p\), with zero boundary at index zero, and its closure vanishes only at zero. Therefore its positive eigenvalues \(\mu_{p,r}\) exist at every fixed index \(r\), and the corresponding \(r\)-th largest eigenvalue of \(A_{p,n}\) tends to \(\mu_{p,r}\) by norm convergence and the min-max principle. The \(r\)-th smallest eigenvalue of \(C_{n,p}\) is \(1/[N\mu_{p,n,r}]\), where \(\mu_{p,n,r}\) denotes that \(r\)-th largest eigenvalue. Multiplying by \(n\) proves the hard-edge limit.

**3. The continuum large-eigenvalue edge.** Divide \(C_{n,p}\) by \(n^{2p+1}\) and embed the coordinate space isometrically in \(L^2(0,1)\) as functions constant on the \(n\) intervals of length \(1/n\). The resulting step-kernel operator has kernel
\[
K_{n,p}(s,t)=\left(\frac{\lceil ns\rceil}{n}\right)^p
\left(\frac{\lceil nt\rceil}{n}\right)^p
\left[\frac{\min(\lceil ns\rceil,\lceil nt\rceil)}{n+1}
-\frac{\lceil ns\rceil\lceil nt\rceil}{(n+1)^2}\right].
\]
It converges uniformly (hence in Hilbert-Schmidt and operator norm) to
\[
K_p(s,t)=s^pt^p(\min(s,t)-st).
\]
For the resulting integral operator \(T_p\), let \(T_pf=\lambda f\) with \(\lambda>0\) and put \(g(t)=f(t)/t^p\) on \((0,1]\). Since \(\min(s,t)-st\) is the Dirichlet Green kernel for \(-d^2/dt^2\), the eigenvalue equation is equivalent to
\[
-\lambda g''(t)=t^{2p}g(t),\qquad g(0)=g(1)=0.
\]
The boundary condition at zero selects the solution \(g(t)=c\sqrt t\,J_{\nu_p}(t^{p+1}/[(p+1)\sqrt\lambda])\); the independent \(J_{-\nu_p}\) solution is nonzero at zero. The boundary value at one gives exactly \(\lambda=1/[(p+1)^2j_{\nu_p,k}^2]\). Sturm-Liouville theory proves that these are all the positive simple eigenvalues, in decreasing order. Norm convergence of the step operators proves the claimed fixed-index limits.

**4. Condition numbers, trace, and the endpoint.** Combining steps 2 and 3 gives the power \(n^{2p+2}\) and its strictly positive coefficient. Direct summation of diagonal entries gives
\[
\operatorname{tr}C_{n,p}=\frac1{N^2}\sum_{i=1}^{n} i^{2p+1}(N-i),
\]
whose Riemann-sum limit is \(\int_0^1t^{2p+1}(1-t)\,dt\). The equality with the Bessel-zero sum follows from the standard Rayleigh identity \(\sum_{k\geq1}j_{\nu,k}^{-2}=1/[4(\nu+1)]\). For \(p=0\), diagonalization of \(L_n\) by the sine basis gives its eigenvalues \(4\sin^2(k\pi/[2N])\). Inverting and reversing order yields the stated finite spectrum, the common \(1/4\) lower-edge limit, and the quadratic condition-number law.

## Verification
The standalone script `checks/verify_power_lecture_hall.py` uses exact rational enumeration of vertices and matrix inverses for the powers \(p=0,1,2,3\) and dimensions up to six. It compares the unweighted covariance spectrum with exact sine eigenvalues, independently computes the first two Bessel-zero limits and compact-Jacobi edge approximations, and evaluates positive-power examples at dimensions 80 and 160. The completed run returned `POWER_LECTURE_HALL_TWO_EDGE_SPECTRUM_CHECKS_PASSED`. These calculations support but do not replace the all-dimensional arguments above.

## Relationship to prior work
Kohl and Olsen (arXiv:1710.10892; first public version October 30, 2017) study the defining lecture-hall simplices, Gorenstein properties and level algebras. Brändén and Solus (arXiv:1911.12459) develop integer decomposition and triangulation properties of the same family. Neither inspected primary source contains the uniform-vertex covariance anisotropy statement or its discrete hard-edge spectrum. The inradius of general lecture-hall order polytopes is treated in a separately indexed result titled *Euclidean inradius of every lecture-hall order polytope is a weighted critical-path reciprocal*; an inradius theorem does not determine vertex-covariance eigenvalues.

**The weighted-Brownian-bridge Bessel spectrum itself is not new.** It is a special case of Deheuvels and Martynov's 2003 Karhunen-Loève expansions, also recorded explicitly in Deheuvels (2006, arXiv:math/0612693, Fact 1.2). The new claim here is the simultaneous identification of both spectral edges for this discrete geometric vertex measure, including the compact Jacobi limit and sharp condition-number exponent and coefficient. Related 2024 work by Pycke on discrete Brownian bridges and Hahn polynomials concerns a hypergeometric family with different weights; no inference of this two-edge lecture-hall theorem was identified. Historical priority remains subject to independent literature review.

## Limitations
The result does not assert originality of the continuous Bessel spectral identity, quantitative convergence rates, uniform spectral asymptotics for indices increasing with dimension, or properties of the uniform interior measure. The constants \(\rho_p\) are defined as norms of explicitly specified compact Jacobi operators rather than claimed elementary closed forms. Computational checks are finite and cannot certify an infinite-dimensional limit. An older equivalent treatment of these specific weighted discrete covariance matrices could affect historical priority. No independent mathematical audit has been performed.

## References
1. F. Kohl and M. Olsen, *Level algebras and s-lecture hall polytopes*, arXiv:1710.10892 (first version 2017-10-30); Electronic Journal of Combinatorics 27 (2020), P3.50; DOI 10.37236/8626.
2. P. Brändén and L. Solus, *Some algebraic properties of lecture hall polytopes*, arXiv:1911.12459 (first version 2019-11-27).
3. P. Deheuvels and G. Martynov, *Karhunen-Loève expansions for weighted Wiener processes and Brownian bridges via Bessel functions*, in *High Dimensional Probability III* (2003), pp. 57–93, DOI 10.1007/978-3-0348-8059-6_4.
4. P. Deheuvels, *Karhunen-Loève expansions of mean-centered Wiener processes*, IMS Lecture Notes–Monograph Series 51 (2006), 62–76, arXiv:math/0612693, DOI 10.1214/074921706000000761.
5. J.-R. Pycke, *A discrete Cramér–Von Mises statistic related to Hahn polynomials with application to goodness-of-fit testing for hypergeometric distributions*, Axioms 13 (2024), 369, DOI 10.3390/axioms13060369.

# Three competing second-jet Bergman radii and a weight-driven Gamma peak reversal

## Finding
Let \(\beta>1\), let \(n\ge3\) be an integer, and let \(A^2_\beta\) denote the analytic disk reproducing-kernel Hilbert space with \(K_\beta(z,w)=(1-z\overline w)^{-\beta}\). Write \(c_n=(\beta)_n/n!\) and \(e_n(z)=\sqrt{c_n}\,z^n\). For each \(w\in\mathbb D\), let \(J_w^{(2)}\) be the span of the function-value, first-derivative and second-derivative representers at \(w\), and let \(P_{n,\beta}(x)=\|\operatorname{Proj}_{J_w^{(2)}}e_n\|^2\), where \(x=|w|^2\).

Define the polynomials
\[
\begin{aligned}
Q_1(x)&=(n+\beta)x-n,\\
Q_2(x)&=n(n-1)-2n(n+\beta)x+(n+\beta)(n+\beta+1)x^2,\\
Q_3(x)&=-n(n-1)(n-2)+3n(n-1)(n+\beta)x\\
&\quad-3n(n+\beta)(n+\beta+1)x^2
 +(n+\beta)(n+\beta+1)(n+\beta+2)x^3.
\end{aligned}
\]
Then
\[
P_{n,\beta}(x)=c_n x^{n-2}(1-x)^\beta
\left[x^2+\frac{xQ_1(x)^2}{\beta}+\frac{Q_2(x)^2}{2\beta(\beta+1)}\right]
\qquad (0<x<1).
\]
There are **exactly three strict local maxima** of \(P_{n,\beta}\), at the three roots of \(Q_3\) in \((0,1)\), and **exactly two strict local minima**, at the interlacing roots of \(Q_2\). Consequently the exact best captured squared norm is the maximum of three explicitly defined algebraic-radius candidate values, with no other maximizing radii.

For each fixed \(\beta>1\), let \(0<t_1(\beta)<t_2(\beta)<t_3(\beta)\) be the three positive roots of the generalized Laguerre polynomial \(L_3^{(\beta-1)}\). Define
\[
H_\beta(t)=\frac{e^{-t}t^\beta}{\Gamma(\beta)}
\left[1+\frac{(\beta-t)^2}{\beta}
+\frac{\big(t^2-2(\beta+1)t+\beta(\beta+1)\big)^2}{2\beta(\beta+1)}\right].
\]
Then the sharp high-degree limit and all limiting candidate radii are
\[
\lim_{n\to\infty}n\max_{0\le x<1}P_{n,\beta}(x)
=\max_{j=1,2,3}H_\beta(t_j(\beta)),\qquad
n(1-x_{j,n})\longrightarrow t_j(\beta),
\]
where \(x_{j,n}\) is the root of \(Q_3\) corresponding to \(t_j\) in decreasing order of \(x\).

At \(\beta=2\), the **largest** Laguerre root \(t_3\) uniquely maximizes the limiting capture. For all sufficiently large fixed \(\beta\), the **middle** root \(t_2\) uniquely maximizes it. Hence at least one intermediate weight has two or more equally optimal limiting radial peaks; and for all sufficiently large \(n\), varying \(\beta\) produces at least one tie between distinct exact finite-degree optimal radii.

## Assumptions and scope
The disk weight corresponding to the kernel is \((\beta-1)(1-|z|^2)^{\beta-2}\,dA(z)/\pi\), so \(\beta>1\) is precisely the standard integrable positive area-weight range. The convention \((\beta)_n=\beta(\beta+1)\cdots(\beta+n-1)\) is used. The projection uses the entire three-dimensional same-site jet span, not a single isolated second-derivative representer. All radius extrema are within \(0<x<1\); angular rotations of \(w\) are equivalent. The assertion of a transition does not assert a unique transition weight or a formula for its location.

## Proof
**Exact projection formula.** For real \(w=r\in(0,1)\), the weighted disk-automorphism unitary
\[
(U_rf)(z)=(1-r^2)^{\beta/2}(1-rz)^{-\beta}
 f\left(\frac{r-z}{1-rz}\right)
\]
interchanges the jet span at \(r\) with the span of \(1,z,z^2\) at the origin. This follows because the automorphism is involutive and its nonvanishing multiplier transforms the three Taylor functionals by an invertible triangular matrix. The Taylor coefficient of \(U_re_n\) at degree \(j=0,1,2\) equals
\[
\sqrt{c_n}\,(1-r^2)^{\beta/2} r^{n-j}\frac{Q_j(r^2)}{j!},\qquad Q_0=1.
\]
The monomial squared norm is \(\|z^j\|^2=j!/(\beta)_j\). Orthogonal summation of these three Taylor modes therefore yields the stated formula.

**All critical points.** Differentiating the displayed rational-power expression and collecting terms gives the exact factorization
\[
P_{n,\beta}'(x)
=-\frac{c_n}{2\beta(\beta+1)}
 x^{n-3}(1-x)^{\beta-1}Q_2(x)Q_3(x).
\]
The standard shifted-Jacobi Rodrigues formula identifies
\[
Q_j(x)=(-1)^j j! P_j^{(n-j,\,\beta-1)}(1-2x),\qquad j=2,3.
\]
Thus \(Q_3\) has three simple roots in \((0,1)\) and \(Q_2\) has two. To see strict interlacing, put \(v(x)=x^{n-3}(1-x)^{\beta-1}\). The degree-three polynomial \(Q_3\) is orthogonal for \(v\), whereas \(Q_2\) is orthogonal for \(xv\). The elementary Christoffel-transform interlacing theorem at the endpoint \(x=0\) places the two roots of \(Q_2\) strictly between the three roots of \(Q_3\). It also follows directly by expressing the degree-two orthogonal polynomial for \(xv\) as the divided difference at zero of the degree-three and degree-two polynomials for \(v\), whose zeros strictly interlace. At \(x\downarrow0\), \(Q_2>0\), \(Q_3<0\) and \(P'>0\). The alternating simple zeros therefore give maxima at \(Q_3=0\), minima at \(Q_2=0\). Since \(n\ge3\) and \(\beta>1\), the endpoint values both vanish, so every global maximum lies at a root of \(Q_3\).

**The Gamma boundary limit.** Put \(t=n(1-x)\). For each fixed positive \(t\), the binomial Taylor coefficients satisfy
\[
Q_j(1-t/n)\longrightarrow j!L_j^{(\beta-1)}(t),\qquad j=0,1,2,3,
\]
while \(c_n\sim n^{\beta-1}/\Gamma(\beta)\), \(x^{n-j}\to e^{-t}\), and \((1-x)^\beta=(t/n)^\beta\). The formula gives \(nP_{n,\beta}(1-t/n)\to H_\beta(t)\), locally uniformly in \(t>0\). Because \(L_3^{(\beta-1)}\) has three simple positive zeros, the three zeros of \(Q_3\) correspond in the stated order and converge under this rescaling. Evaluating the three candidate heights proves convergence of the **global** maximum, without assuming that numerical or finite-interval scans exhaust the disk.

**Weight reversal.** At \(\beta=2\), the three roots of \(L_3^{(1)}\) lie respectively in \((0.935,0.937)\), \((3.305,3.306)\), \((7.758,7.760)\). Exact rational endpoint sign tests for \(24-36t+12t^2-t^3\), together with rational Taylor-remainder enclosures for \(e^{-t}\), give the disjoint bounds
\[
0.58<H_2(t_1)<0.59,\qquad
1.02<H_2(t_2)<1.03,\qquad
1.27<H_2(t_3)<1.29.
\]
The supplied exact-arithmetic checker reproduces these interval certificates using only rational operations.

Now send \(\beta\to\infty\) and write \(t=\beta+\sqrt\beta\,y\). Stirling's formula and the fixed-degree Laguerre-to-Hermite limit give, uniformly for \(y\) in compact sets,
\[
\frac{H_\beta(\beta+\sqrt\beta\,y)}{\sqrt\beta}
\longrightarrow \frac{e^{-y^2/2}}{\sqrt{2\pi}}
\left(1+y^2+\frac{(y^2-1)^2}{2}\right).
\]
The rescaled three Laguerre roots tend to \(-\sqrt3,0,\sqrt3\). The limiting peak at zero has height \(3/(2\sqrt{2\pi})\), versus \(6e^{-3/2}/\sqrt{2\pi}\) at each outer peak. The former is strictly larger because \(e^{3/2}>4\). Therefore, for sufficiently large \(\beta\), \(t_2\) is uniquely preferred. The three peak values depend continuously on \(\beta>1\), and the preferred label differs at the two parameter ends, so some intermediate weight has a tied global maximum. For sufficiently large integer \(n\), the same strict preferences persist at fixed \(\beta=2\) and at one fixed sufficiently large \(\beta\), and continuity of the exact finite-degree peak values forces a finite-degree tie as well.

## Verification
The standalone `checker.py` uses exact fractions to check the derivative polynomial identity for 44 integer-degree/weight pairs and independently reconstruct the three-jet Gram projection for 45 rational-node cases. It also certifies the three \(\beta=2\) Laguerre-root intervals and their disjoint Gamma-height bounds using an explicit order-80 Maclaurin remainder. The program reports 98 successful assertions. These finite checks supplement, rather than replace, the all-degree algebraic, Jacobi and asymptotic arguments above.

## Relationship to prior work
Qu and Dang (first public 27 May 2019) study adaptive reproducing-kernel approximation in weighted Bergman spaces, including repeated kernels. Qu, Qian and Deng (2020) prove general existence of best multiple-kernel approximants. Escudero, Haimi and Romero (2021) investigate multiple sampling and interpolation densities in weighted Fock spaces, a different domain and objective. Classical Jacobi and Laguerre orthogonality provides the necessary polynomial tools but does not itself specify the above three-site radial preference and its Gamma weight reversal. The result differs from previously reported first-jet Bergman capture (two maxima and no second derivative) and Gaussian-Fock single-site jet asymptotics (a bulk Hermite rather than a disk-boundary Gamma regime). The particular second-jet global peak-switch claim was not located in the accessible compared statements.

## Limitations
No complete classification or uniqueness of the intermediate transition parameter is claimed. The result does not optimize over multiple spatially distinct sites, over more than two derivatives, or over general non-monomial targets. The full 2019 Qu–Dang article was inaccessible through the attempted lawful channels; it remains a historical-priority risk. A general older Laguerre weighted-Christoffel extremum result not surfaced by the searches could contain an equivalent version. The numerical diagnostics are not proof of the infinite statements.

## References
1. W. Qu and P. Dang, *Reproducing kernel approximation in weighted Bergman spaces: Algorithm and applications*, Mathematical Methods in the Applied Sciences 42 (2019), 4292–4304, first published 27 May 2019, https://doi.org/10.1002/mma.5648.
2. W. Qu, T. Qian and G.-T. Deng, *A sufficient condition for n-Best Kernel Approximation in Reproducing Kernel Hilbert Spaces*, arXiv:2006.03290, first submitted 5 June 2020, https://arxiv.org/html/2006.03290v3.
3. L. A. Escudero, A. Haimi and J. L. Romero, *Multiple Sampling and Interpolation in Weighted Fock Spaces of Entire Functions*, Complex Analysis and Operator Theory 15 (2021), article 35, published 16 February 2021, https://doi.org/10.1007/s11785-020-01065-4.
4. NIST Digital Library of Mathematical Functions, Chapters 18 (classical orthogonal polynomials) and 3.5 (Gaussian quadrature), https://dlmf.nist.gov/18 and https://dlmf.nist.gov/3.5.

# Optimal positive circular convolution kernels and the killed-Cauchy spectral limit

## Finding

For an integer \(n\geq1\), let \(\mathcal K_n\) consist of nonnegative real trigonometric polynomials \(K\) of degree at most \(n\), normalized by \(\frac1{2\pi}\int_{-\pi}^{\pi}K(t)\,dt=1\). The convolution operator \(S_K f(x)=\frac1{2\pi}\int_{-\pi}^{\pi}K(t)f(x-t)\,dt\) is positivity preserving and fixes constants. Its worst uniform approximation error on all circular one-Lipschitz functions is \(E(K)=\frac1{2\pi}\int_{-\pi}^{\pi}|t|K(t)\,dt\).

**Theorem.** The minimum \(C_n=\min_{K\in\mathcal K_n}E(K)\) is the smallest eigenvalue of the explicit real symmetric \((n+1)\)-by-\((n+1)\) Toeplitz matrix \(T_n=(t_{j-k})_{j,k=0}^{n}\), where
\[
 t_0=\frac\pi2,\qquad t_m=\frac{(-1)^m-1}{\pi m^2}\quad(m\neq0).
\]
For every \(n\geq1\), the minimum is attained by **exactly one kernel**
\[
 K_n(t)=\left|\sum_{j=0}^{n}v_j e^{ijt}\right|^2,
\]
where \(v=(v_0,\ldots,v_n)\) is the unique unit-norm, entrywise positive eigenvector of \(T_n\) at \(C_n\). Moreover \(v_j=v_{n-j}\).

The optimal constants satisfy the nontrivial continuum limit
\[
 \lim_{n\to\infty}(n+1)C_n=\Lambda,
 \qquad \Lambda=\inf_{\substack{0\ne u\in C_c^\infty(0,1)}}
 \frac{\frac1{2\pi}\int_{\mathbb R}|\xi|\,|\widehat u(\xi)|^2\,d\xi}
 {\int_0^1|u(x)|^2\,dx}.
\]
Here \(\widehat u(\xi)=\int_{\mathbb R}u(x)e^{-i\xi x}\,dx\), with zero extension outside \((0,1)\). Thus \(\Lambda\) is the first eigenvalue of the **restricted (zero-exterior)** one-dimensional half-Laplacian on \((0,1)\). It is twice the first restricted-Cauchy eigenvalue on \((-1,1)\), which is already studied in spectral theory. It obeys the strict, explicitly evaluated bound
\[
 0<\Lambda<2\operatorname{Si}(\pi)-\frac4\pi
 =2.4306345592297687\ldots,
 \qquad \operatorname{Si}(x)=\int_0^x\frac{\sin t}{t}\,dt.
\]
This strict inequality improves the asymptotic positive-convolution error coefficient of the Rivlin-type construction analyzed in the motivating paper. The new claim concerns the entire class of positive trigonometric convolution kernels, **not** unrestricted best approximation by arbitrary polynomials.

## Assumptions and scope

All functions in the Lipschitz error definition are real or complex \(2\pi\)-periodic functions with Lipschitz constant at most one for the geodesic distance on the circle, and error is measured in uniform norm. Fourier degree is at most \(n\); convolution kernels are pointwise nonnegative with integral mass one. Eigenvectors are normalized in Euclidean \(\ell^2\). The half-Laplacian is the **restricted** Fourier multiplier \(|\xi|\) acting on zero-extended functions, not the spectral square root of a Dirichlet ordinary Laplacian. All limits are as positive integer \(n\to\infty\).

## Proof

**1. Worst-case error and a Toeplitz minimum.** If \(f\) is one-Lipschitz, positivity and unit mass give \(|S_Kf(x)-f(x)|\leq(2\pi)^{-1}\int|t|K(t)\,dt\). Equality occurs at the evaluation point \(x=0\) for the periodic distance function \(f(x)=\operatorname{dist}_{\mathbb T}(x,0)\), up to sign. Hence the objective is exactly the stated first geodesic moment. By Fejér–Riesz factorization, every \(K\in\mathcal K_n\) is \(|P(e^{it})|^2\), with \(P(z)=\sum_{j=0}^{n}a_jz^j\) and \(\sum|a_j|^2=1\). Direct integration of the Fourier coefficients of \(|t|\) gives \(t_0=\pi/2\) and \(t_m=((-1)^m-1)/(\pi m^2)\). Therefore \(E(K)=a^*T_na\), and the minimum equals \(\lambda_{\min}(T_n)\).

**2. Uniqueness of the optimal nonnegative kernel.** Set \(B_n=(\pi/2)I-T_n\). Its entries are \((B_n)_{jk}=2/(\pi|j-k|^2)\) whenever \(|j-k|\) is odd, and zero otherwise. In particular, the positive offdiagonal edge connecting each pair of consecutive indices makes its nonnegative graph connected. Perron–Frobenius yields a simple largest eigenvalue with a unique unit positive eigenvector \(v\). Since \(T_n=\pi I/2-B_n\), every minimizing coefficient vector is a constant phase multiple of \(v\), proving uniqueness of \(K_n\). Index reversal commutes with \(B_n\) and preserves positivity, so \(v_j=v_{n-j}\).

**3. Continuum lower bound.** Write \(L=n+1\), \(h=1/L\). For a norm-one vector \(a\in\mathbb C^L\), form the step function \(u_h(x)=a_j/\sqrt h\) on \([jh,(j+1)h)\), zero elsewhere. Then \(\|u_h\|_2=1\). Its Fourier transform obeys
\[
 \widehat u_h(\xi)=\sqrt h\,e^{-ih\xi/2}\operatorname{sinc}(h\xi/2)
 \sum_{j=0}^{L-1}a_j e^{-ijh\xi},
 \qquad\operatorname{sinc}(y)=\frac{\sin y}{y}.
\]
Consequently, with \(Q_h=h^{-1}a^*T_na\),
\[
 Q_h=\frac1{2\pi}\int_{-\pi/h}^{\pi/h}
 \frac{|\xi|\,|\widehat u_h(\xi)|^2}
 {\operatorname{sinc}^2(h\xi/2)}\,d\xi.
\]
Consider minimizing vectors along any sequence for which \(Q_h\) is bounded. On the principal interval, the \(L^2\)-Fourier mass at \(|\xi|>R\) is at most \(Q_h/R\), since \(\operatorname{sinc}^2\leq1\). Outside it, decompose into translates by \(2\pi k/h\). The Fourier transform's alias ratio at base frequency \(\eta\in[-\pi/h,\pi/h]\) is \(\big|\eta/(\eta+2\pi k/h)\big|\); summing squares over \(k\ne0\) gives at most \(C h^2\eta^2\). Since \(\int_{-\pi/h}^{\pi/h}\eta^2|\widehat u_h(\eta)|^2d\eta\leq(\pi/h)\,2\pi Q_h\), the total alias mass is \(O(hQ_h)\). Thus Fourier tails vanish uniformly, while every \(u_h\) has support in \([0,1]\). Fourier tightness plus fixed spatial support implies precompactness in \(L^2(\mathbb R)\) (the Fourier form of the Kolmogorov–Riesz criterion). Any subsequence has a further strongly convergent subsequence with limit \(u\), supported in \([0,1]\) and \(\|u\|_2=1\). For each bounded Fourier interval, the displayed exact identity and \(\operatorname{sinc}^{-2}(h\xi/2)\to1\), followed by weak lower semicontinuity and monotone exhaustion, give
\[
 \liminf_{h\downarrow0}Q_h\geq \frac1{2\pi}\int_{\mathbb R}|\xi|\,|\widehat u(\xi)|^2d\xi\geq\Lambda.
\]
The last inequality follows from the form-domain characterization as the closure of smooth functions compactly supported in \((0,1)\); for an interval, this density follows by inwardly dilating any zero-extended finite-energy function to compact support in the interval (dilations are continuous in the Fourier energy norm), then mollifying. This proves the lower asymptotic bound.

**4. Continuum upper bound.** For any \(u\in C_c^\infty(0,1)\), take \(a_j=\sqrt h\,u(jh)\), then normalize by \((\sum|a_j|^2)^{1/2}\to\|u\|_2\). On the principal band \(|\xi|\leq\pi/h\), the corresponding finite sum \(h\sum_j u(jh)e^{-ijh\xi}\) converges at each fixed \(\xi\) to \(\widehat u(\xi)\). Repeated discrete summation by parts (using the zero padding near both endpoints) bounds it uniformly by \(C_N(1+|\xi|)^{-N}\) for each fixed positive integer \(N\). Dominated convergence in the exact principal-band formula yields \(Q_h\to(2\pi)^{-1}\int|\xi||\widehat u|^2/\|u\|_2^2\). Taking the infimum over such tests gives \(\limsup (n+1)C_n\leq\Lambda\), completing the limit proof.

**5. Strict improvement.** Use the unit-norm zero-extended test \(u_0(x)=\sqrt2\sin(\pi x)\) on \((0,1)\). A direct Fourier integration yields
\[
 \frac1{2\pi}\int_{\mathbb R}|\xi|\,|\widehat u_0(\xi)|^2d\xi
 =2\operatorname{Si}(\pi)-\frac4\pi.
\]
This upper bound is strict. Indeed, \(u_0\) cannot minimize the restricted-Cauchy Rayleigh quotient: for \(x\downarrow0\), the principal-value formula
\[
 (|D|u_0)(x)=\frac1\pi\operatorname{PV}\!\int_{\mathbb R}
 \frac{u_0(x)-u_0(y)}{(x-y)^2}\,dy
 \]
has the asymptotic \((|D|u_0)(x)=\sqrt2\log x+O(1)\), while any eigenfunction relation \(|D|u_0=\lambda u_0\) would have a bounded right side tending to zero. To see the logarithm directly, write \(u_0(y)=\sqrt2\pi y+O(y^3)\) on \((0,\delta)\); its linear term contributes \(\sqrt2\,\operatorname{PV}\int_0^\delta(x-y)^{-1}dy=\sqrt2\log x+O(1)\); the remaining pieces contribute bounded terms. A positive smooth perturbation supported where this Euler–Lagrange residual is negative strictly lowers the Rayleigh quotient. Therefore \(\Lambda\) is strictly below the displayed test value.

## Verification

`CHECK.py` recomputes the Toeplitz matrix, eigenpairs, strictly positive and symmetric minimizing vectors, direct angular-moment integrals, and variational competitors for degrees one through thirty-two. Further checks cover degrees sixty-four, one hundred twenty-eight, two hundred fifty-six and five hundred twelve. Run `python CHECK.py` after installing the packages in `requirements.txt`. The checker is finite numerical corroboration only; it cannot establish the operator limit, strict asymptotic inequality or novelty. The algebraic Fourier coefficient calculation, Perron–Frobenius argument and compactness proof provide the infinite-dimensional justification. The normalization and zero-exterior boundary convention are essential.

## Relationship to prior work

Shah, Urschel and West (2026, arXiv:2607.23375, initially public July 25, 2026) analyzed asymptotic constants for two explicitly prescribed Jackson/Rivlin-type positive convolution constructions and proved the first-moment characterization of Lipschitz error. Here the optimization instead runs over *every* positive, normalized trigonometric kernel of each degree; the unique exact finite-degree solution and its continuum spectral limit are the additional assertions. Kwaśnicki (2010, arXiv:1012.1133) established restricted fractional-Laplacian spectral theory and numerical bounds; Zhang (2026, arXiv:2608.23457) advanced interval fractional spectral estimates. Neither spectral paper, by its stated objects and inspected results, derives a positive trigonometric approximation optimality principle. An older paper by Goldstein and McDonald (1984), entitled “An Extremal Problem for Non-Negative Trigonometric Polynomials,” is a priority-risk source whose full contents could not be compared in this review; no conclusion of noncoverage is asserted for that paper.

## Limitations

The result concerns normalized *positive convolution operators* and uniform error on the circular Lipschitz unit ball. It is not a sharp unconstrained Jackson approximation theorem. The limiting constant is identified exactly as a pre-existing restricted-Cauchy eigenvalue, rather than given in elementary closed form. The finite numerical checks do not prove convergence. Prior-publication equivalence under older extremal-polynomial terminology remains a residual risk. No independent validation or publication-priority audit is claimed.

## References

- R. Shah, J. Urschel, N. West, “What is Jackson's constant?”, arXiv:2607.23375 (first version July 25, 2026), https://arxiv.org/abs/2607.23375.
- M. Kwaśnicki, “Eigenvalues of the fractional Laplace operator in the interval”, arXiv:1012.1133 (2010), https://arxiv.org/abs/1012.1133.
- C. Zhang, “Eigenvalue asymptotics and uniform eigenfunction bounds for the fractional Laplacian in the interval”, arXiv:2608.23457 (first version August 24, 2026), https://arxiv.org/abs/2608.23457.
- M. Goldstein, J. N. McDonald, “An Extremal Problem for Non-Negative Trigonometric Polynomials”, Journal of the London Mathematical Society (1984), doi:10.1112/jlms/s2-29.1.81 (full text unavailable for comparison).

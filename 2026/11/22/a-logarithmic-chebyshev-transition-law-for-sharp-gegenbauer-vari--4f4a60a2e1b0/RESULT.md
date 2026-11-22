# A logarithmic Chebyshev-transition law for sharp Gegenbauer variation coefficients

## Finding
For each real number \(\tau\), let \(\lambda_n=\tau/\log n\) for integers \(n\ge3\); restrict to sufficiently large \(n\) so that \(\lambda_n>-1/2\). Let \(p_n^{(\lambda)}\) be the Gegenbauer polynomial of degree \(n\) normalized by \(p_n^{(\lambda)}(1)=1\), continuously extended at \(\lambda=0\) as the first-kind Chebyshev polynomial \(T_n\). Define
\[
w_\lambda(x)=(1-x^2)^{\lambda-1/2},\quad G_{n,\lambda}(x)=\int_{-1}^{x}p_n^{(\lambda)}(t)w_\lambda(t)\,dt,\quad M_{n,\lambda}=\max_{-1\le x\le1}|G_{n,\lambda}(x)|,
\]
\[
h_{n,\lambda}=\int_{-1}^{1}p_n^{(\lambda)}(x)^2w_\lambda(x)\,dx,\quad K_{n,\lambda}=M_{n,\lambda}/h_{n,\lambda}.
\]
The exact sharp operator norm of the coefficient functional \(f\mapsto h_{n,\lambda}^{-1}\int f p_n^{(\lambda)}w_\lambda\) over real bounded-variation functions with total variation at most one is \(K_{n,\lambda}\). Its **critical moving-parameter limit**, and that of its primitive, are
\[
\lim_{n\to\infty}nM_{n,\lambda_n}=\begin{cases}e^{-2\tau},&\tau<0,\\1,&\tau=0,\\e^{-\tau},&\tau>0,\end{cases}
\qquad \lim_{n\to\infty}nK_{n,\lambda_n}=\frac2\pi\begin{cases}1,&\tau\le0,\\e^\tau,&\tau\ge0.\end{cases}
\]
More generally both limits hold whenever \(\lambda_n\to0\) and \(\lambda_n\log n\to\tau\). For every finite \(n\), the maximizing locations of \(|G_{n,\lambda}|\) are the two outermost Gegenbauer zeros if \(\lambda<0\), the zero(s) nearest the origin if \(\lambda>0\), and all polynomial zeros if \(\lambda=0\). The location assertion is known; the logarithmic-window limit is the new result.

## Assumptions and scope
Throughout, \(n\ge3\), \(-1/2<\lambda\) and \(|\lambda|<1/4\) for sufficiently large \(n\). At \(\lambda=0\) use \(p_n^{(0)}=T_n\). Every \(h_{n,\lambda}\) is strictly positive. The coefficient functional is understood on real \(BV[-1,1]\), modulo additive constants, with \(V(f)\le1\). Limits are pointwise for each finite real \(\tau\), not asserted uniformly for unbounded \(\tau\). The positive/negative sides can be followed along arbitrary sequences approaching zero.

## Proof
**1. Exact primitive, maximizing zeros.** Write \(p=p_n^{(\lambda)}\), \(N=n(n+2\lambda)\) and \(y=(1-x^2)^{\lambda+1/2}p'(x)\). The normalized Gegenbauer ODE gives \(y'=-Nw_\lambda p\), with \(y(\pm1)=0\). Hence \(G_{n,\lambda}(x)=-y(x)/N\), including the endpoints. All interior extrema of \(G\) occur at zeros of \(p\). The identity
\[
E(x)=y(x)^2+N(1-x^2)^{2\lambda}p(x)^2,\qquad E'(x)=-4\lambda N x(1-x^2)^{2\lambda-1}p(x)^2
\]
shows that \(E\) decreases strictly between nonnegative roots for \(\lambda>0\) and increases strictly for \(\lambda<0\). At any zero of \(p\), \(E=y^2\); symmetry handles the negative side. Consequently the innermost zero(s) maximize for positive \(\lambda\), the outermost pair for negative \(\lambda\), and all zeros tie for zero parameter. This finite-degree extremum ordering also follows from Wang (2023, Theorem 4.1(iv)); it is included here only as a premise.

**2. Central regime.** Put \(m=\lfloor n/2\rfloor\) and
\[
 a_{m,\lambda}=\frac{(1/2)_m}{(\lambda+1/2)_m}
 =\frac{\Gamma(m+1/2)\Gamma(\lambda+1/2)}{\sqrt\pi\,\Gamma(m+\lambda+1/2)}.
\]
Direct evaluation of the hypergeometric Gegenbauer polynomial gives \(p_{2m}^{(\lambda)}(0)=(-1)^ma_{m,\lambda}\), and \((p_{2m+1}^{(\lambda)})'(0)=(-1)^m(2m+1)a_{m,\lambda}\). Uniform gamma-ratio asymptotics for \(|\lambda|\le1/4\) give
\[
 a_{m,\lambda}=\frac{2^\lambda\Gamma(\lambda+1/2)}{\sqrt\pi}\,n^{-\lambda}(1+O(1/n)),\quad n\in\{2m,2m+1\}.
\]
For odd \(n\), the central zero is exactly zero and \(M_{n,\lambda}=a_{m,\lambda}/(n+2\lambda)\). For even \(n\), set \(x=\sin(z/n)\), \(u_n(z)=(-1)^m p_n^{(\lambda)}(\sin(z/n))/a_{m,\lambda}\). It satisfies
\[
 u_n''(z)-\frac{2\lambda}{n}\tan(z/n)u_n'(z)+(1+2\lambda/n)u_n(z)=0,\quad u_n(0)=1,\quad u_n'(0)=0.
\]
On every compact \(z\)-interval the coefficients converge uniformly to those of \(u''+u=0\), uniformly for \(\lambda\to0\), so \(u_n\to\cos z\) with first derivatives. Its first positive zero tends to \(\pi/2\). At that zero the exact primitive formula becomes \(|G|=a_{m,\lambda}|\cos(z/n)^{2\lambda}u_n'(z)|/(n+2\lambda)\), hence \(nM_{n,\lambda}\sim a_{m,\lambda}\) whenever \(\lambda\ge0\) tends to zero. With \(\lambda\log n\to\tau\ge0\), this tends to \(e^{-\tau}\). If \(\lambda=0\) identically, \(M_{n,0}=1/n\), consistent with the limit.

**3. Endpoint regime.** For \(\lambda<0\) use the outermost positive zero \(x_n\), and write \(x_n=\cos(z_n/n)\), with \(z_n>0\). The hypergeometric representation is
\[
 H_n(z)=p_n^{(\lambda)}(\cos(z/n))={}_2F_1\bigl(-n,n+2\lambda;\lambda+\tfrac12;(1-\cos(z/n))/2\bigr).
\]
For \(|\lambda|\le1/4\), each coefficient of this terminating series, and its differentiated series, is bounded on compact \(z\)-sets by a constant times \((2z^2)^k/((1/4)_k k!)\). Dominated convergence as \(\lambda\to0\) yields \(H_n(z)\to{}_0F_1(;1/2;-z^2/4)=\cos z\) in \(C^1\) on compact sets. Positivity up to \(\pi/2-\varepsilon\), and a simple sign-changing zero near \(\pi/2\), imply \(z_n\to\pi/2\), \(|H_n'(z_n)|\to1\), and this is indeed the first zero from the endpoint. The exact derivative identity gives
\[
 nM_{n,\lambda}=\frac{n}{n+2\lambda}\bigl(\sin(z_n/n)\bigr)^{2\lambda}|H_n'(z_n)|.
\]
As \(z_n\to\pi/2\), \(\log\sin(z_n/n)=-\log n+O(1)\). Thus \(nM_{n,\lambda}\to e^{-2\tau}\) if \(\lambda<0\) and \(\lambda\log n\to\tau\le0\). Subsequences of either sign with \(\tau=0\) agree and therefore cover sign-changing sequences.

**4. Sharp coefficient norm.** The Gegenbauer squared norm for this endpoint normalization is exactly
\[
 h_{n,\lambda}=2^{2\lambda-1}\Gamma(\lambda+1/2)^2\frac{\Gamma(n+1)}{(n+\lambda)\Gamma(n+2\lambda)}
\]
(including its continuous \(\lambda=0\) limit \(\pi/2\)). Uniform gamma-ratio estimates for \(\lambda\to0\) give \(h_{n,\lambda}\to(\pi/2)e^{-2\tau}\) when \(\lambda\log n\to\tau\). Dividing the primitive asymptotics by this norm proves the second displayed law. The sharp BV inequality is classical integration by parts: since \(G(-1)=G(1)=0\), \(|\int fpw|=|\int G\,df|\le V(f)M\), with equality for a unit jump at a maximum of \(|G|\).

## Verification
The standalone `check_crossover.py` verifies independent Gauss-quadrature versions of the normalization at 32 small parameter-degree combinations, checks positive maxima, and numerically observes convergence of the moving-window constants at three values of \(\tau\) and three increasing degrees; 76 supplementary assertions pass. Numerical checks do not prove the infinite limit. The proof is analytic and supplies the uniform-in-moving-parameter arguments required for that limit.

## Relationship to prior work
Sluchak (2026) introduces the motivating sharp BV weighted-primitive framework and tabulates estimates for Chebyshev, Gegenbauer, Legendre, and Jacobi families, without the present moving-parameter logarithmic-window limit. Wang (2023, Theorem 4.1(iv)) already proves the finite-degree Gegenbauer extremum ordering and fixed-parameter bounds; that known ordering is not claimed as new here. Xiang and Liu (2020) give the weighted Jacobi BV primitive inequality and fixed-parameter estimates. Dunster (2022) develops uniform Gegenbauer asymptotics but does not state this sharp BV crossover. The result concerns **competition between different zero locations when the Gegenbauer parameter itself tends to zero at a degree-dependent logarithmic rate**, yielding distinct one-sided exponential laws and a kink in the sharp coefficient constant.

## Limitations
The theorem is limited to the Gegenbauer-to-Chebyshev critical window \(\lambda_n\to0\) with bounded convergent \(\lambda_n\log n\); no full global phase diagram for arbitrary moving parameters is asserted. The crossing of the left/right derivative at \(\tau=0\) is an asymptotic effect. A prior general moving-parameter Jacobi asymptotic could potentially subsume parts of the proof, and unlocated older equivalent formulations remain a bibliographic risk. Independent mathematical validation has not been performed.

## References
1. V. Sluchak, *Bounds for Orthogonal Expansion Coefficients via Weighted Primitives*, arXiv:2611.04067 (first public 2026-11-02), sections 3, 6, 7.
2. H. Wang, *New error bounds for Legendre approximations of differentiable functions*, arXiv:2111.03833v2 (2023), Theorem 4.1.
3. S. Xiang and D. Liu, Jacobi coefficient estimates for functions of bounded variation, *Numerische Mathematik* (2020), https://doi.org/10.1007/s00211-020-01113-3.
4. T. M. Dunster, *Uniform asymptotic expansions for Gegenbauer polynomials*, arXiv:2209.10716 (2022).

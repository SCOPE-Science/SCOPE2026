# Sharp Laplace repair and an unbounded spectral staircase for a geodesic Matérn mixture on the circle

## Finding
Let \(d(z,w)\in[0,\pi]\) denote shortest-arc distance on the unit circle, and fix \(a>0\). The geodesic Matérn-\(5/2\) profile \((1+a d+(a d)^2/3)e^{-a d}\) fails positive definiteness. Consider its normalized nonnegative mixture with the geodesic Matérn-\(1/2\) (Laplace) profile:
\[
K_{a,b}(z,w)=\frac{e^{-a d(z,w)}}{1+b}
 \left(1+a d(z,w)+\frac{a^2d(z,w)^2}{3}+b\right),\qquad b\ge0.
\]
Set \(Q=e^{\pi a}-1\), and
\[
L=\frac{\pi a(1+\pi a)}{3Q},\qquad
c=\frac{4\pi a^3}{3Q},\qquad
h=\frac{8a^4}{3},\qquad
x_m=\frac{1}{a^2+4m^2}\quad(m\ge1).
\]
The **exact least admissible mixing ratio** is
\[
\boxed{\ b_*(a)=\max_{m\ge1}\bigl(L+c x_m-h x_m^2\bigr)>L>0,\qquad
 K_{a,b}\succeq0\ \Longleftrightarrow\ b\ge b_*(a).\ }
\]
The maximum is finite and attained; it can be evaluated by at most the two consecutive indices that bracket the positive solution of \(x_m=x_*=\pi/(4aQ)\). If the solution lies below the first index, the maximizer is \(m=1\).

There is a unique strictly increasing unbounded sequence of transition parameters \(0<a_1<a_2<\cdots\), characterized by
\[
\boxed{\ \frac{\pi}{2a_m(e^{\pi a_m}-1)}
=\frac{1}{a_m^2+4m^2}+\frac{1}{a_m^2+4(m+1)^2}.\ }
\]
With \(a_0=0\), exactly the Fourier harmonics \(n=\pm2m\) have zero covariance weight at \(b=b_*(a)\) for \(a_{m-1}<a<a_m\); at \(a=a_m\), precisely \(n=\pm2m,\pm2(m+1)\) vanish. Every successive even harmonic becomes uniquely critical on a nonempty interval: none is skipped. All other Fourier coefficients are strictly positive.

At the threshold the kernel is **strictly positive definite on every finite distinct-site configuration but is not universal on \(C(S^1)\)**. For \(b>b_*(a)\), all Fourier coefficients are positive and the kernel is universal. If \(m_*(a)\) denotes either active positive index, then
\[
m_*(a)=\sqrt{\frac{a}{\pi}}e^{\pi a/2}(1+o(1)),\qquad a\to\infty.
\]
The exact high-frequency endpoint inequality \(b\ge L\) is always strictly insufficient: a finite Fourier notch forces \(b_*>L\). Quantitatively,
\[
 b_*(a)=\frac13+\frac{\pi a}{6}+O(a^2)\quad(a\downarrow0),
\]
\[
\boxed{\ b_*(a)=L+\frac{\pi^2a^2}{6Q^2}+O(aQ^{-3})\quad(a\to\infty).\ }
\]
The corresponding least Laplace mixture fraction (out of total variance) is \(b_*(a)/(1+b_*(a))\).

## Assumptions and scope
All statements are for one-dimensional unit-circle geodesic distance \(d\in[0,\pi]\), every \(a>0\), and every nonnegative real \(b\). The profile is continuous, real, even, translation invariant, and normalized to unit diagonal. Positive semidefiniteness means every finite Gram matrix, including repeated sites, is positive semidefinite; strict positive definiteness concerns finite distinct sites. Universality means density of the RKHS in the continuous complex-valued functions on the circle under the uniform norm. No positive-definiteness assertion is made for higher spheres or for signed \(b<0\). The Fourier transform uses \(\widehat f(n)=(2\pi)^{-1}\int_{-\pi}^{\pi}f(\theta)e^{-in\theta}\,d\theta\).

## Proof
**1. Fourier coefficient identity.** Write \(E=e^{-\pi a}\) and \(D_n=a^2+n^2\). For \(n\in\mathbb Z\), the Laplace profile has strictly positive coefficient
\[
 I_n=\frac1\pi\int_0^\pi e^{-a\theta}\cos(n\theta)\,d\theta
 =\frac{a[1-(-1)^nE]}{\pi D_n}.
\]
Differentiate under the integral sign: the coefficient of the unnormalized Matérn-\(5/2\) profile is \(J_n=I_n-a\partial_a I_n+(a^2/3)\partial_a^2I_n\). Put \(s=(-1)^n\), \(A=1-sE\), \(B=s\pi E\), \(C=-s\pi^2E\), so that \(A'=B\), \(A''=C\). Exact differentiation of \(I_n=aA/(\pi D_n)\) yields
\[
\frac{J_n}{I_n}=\frac{-aB+a^2C}{3A}
 -\frac{4a^3B}{3AD_n}+\frac{8a^4}{3D_n^2}.
\]
For odd \(n\), both \(-B\) and \(C\) are positive; thus \(J_n>0\). For even \(n\), the ratio simplifies exactly to
\[
\frac{J_n}{I_n}=-L-\frac{c}{D_n}+\frac{h}{D_n^2}.
\]
The full normalized kernel has coefficient \((J_n+bI_n)/(1+b)\). By the circle Fourier/Herglotz criterion it is positive semidefinite exactly when these coefficients are all nonnegative. For \(n=0\), positivity follows from the positive integrand; for odd \(n\) it follows from the displayed identity. At even nonzero indices \(n=2m\), it is equivalent to \(b\ge L+c x_m-h x_m^2\), giving the stated supremum.

**2. A genuine finite spectral notch.** Let \(x_*=c/(2h)=\pi/(4aQ)>0\). Completing the square gives
\[
L+c x_m-hx_m^2=L+hx_*^2-h(x_m-x_*)^2.
\]
The strictly decreasing sequence \(x_m=(a^2+4m^2)^{-1}\) tends to zero. For every \(x_*>0\) some \(m\) satisfies \(0<x_m<2x_*\); that index makes \(cx_m-hx_m^2>0\). Consequently \(b_*>L\), and the maximum cannot be attained at the limiting index \(m=\infty\). The closest point(s) of the discrete monotone sequence to \(x_*\) are either \(x_1\) or the two consecutive sequence elements bracketing \(x_*\). Strict monotonicity rules out triple ties.

**3. Exactly one crossing per pair, in order.** For consecutive indices the sign of
\[
(L+cx_m-hx_m^2)-(L+cx_{m+1}-hx_{m+1}^2)
=h(x_m-x_{m+1})(2x_*-x_m-x_{m+1})
\]
is the sign of \(2x_*-x_m-x_{m+1}\). Define \(R_m(a)=2x_*/(x_m+x_{m+1})\). Now
\[
\frac{d}{da}\log x_*=-\frac1a-\frac{\pi e^{\pi a}}{e^{\pi a}-1}< -\frac2a,
\]
where the strict inequality uses \(te^t/(e^t-1)>1\) for \(t>0\). Meanwhile
\[
0<-\frac{d}{da}\log(x_m+x_{m+1})
=2a\frac{x_m^2+x_{m+1}^2}{x_m+x_{m+1}}<\frac2a.
\]
Hence \(R_m\) strictly decreases from \(+\infty\) as \(a\downarrow0\) to \(0\) as \(a\to\infty\), so it equals one at exactly one parameter \(a_m\). For each fixed \(a\), \(R_m(a)\) strictly increases in \(m\), because \(x_m+x_{m+1}\) strictly decreases. Therefore \(a_m<a_{m+1}\). The maximum-of-a-concave-quadratic two-candidate principle makes the active indices exactly \(m\) in \((a_{m-1},a_m)\) and \(m,m+1\) at \(a_m\). Since \(x_m+x_{m+1}\to0\) for fixed \(a\), the crossing parameters diverge to infinity. This proves the all-parameter, no-skips staircase.

**4. Finite-site strictness and universality.** At \(b=b_*\) precisely the one or two active positive even indices, together with their negatives, have zero Fourier coefficient, and all other coefficients are positive. In particular every sufficiently large consecutive integer frequency has positive coefficient. If a quadratic form on distinct points \(z_j=e^{i\theta_j}\) vanished with complex weights \(u_j\), positivity of the Fourier series would force \(\sum_j u_j z_j^n=0\) for all sufficiently large integers \(n\). Any consecutive block of as many equations as sites has an invertible Vandermonde matrix; thus all \(u_j=0\). This proves strict finite-site positive definiteness. At equality the RKHS is orthogonal, in \(L^2(S^1)\), to the absent Fourier characters, precluding \(C\)-universality. Above the threshold every character belongs to the RKHS, so the trigonometric polynomials give universality.

**5. Boundary asymptotics.** The continuous optimal point solves \(a^2+4m^2=4aQ/\pi\). Since the discrete maximizing index lies adjacent to this root for large \(a\),
\[
 m_*(a)=\frac12\sqrt{\frac{4aQ}{\pi}-a^2}+O(1)
=\sqrt{a/\pi}\,e^{\pi a/2}(1+o(1)).
\]
Near that root, neighboring \(x_m\) differ by \(O((aQ)^{-3/2})\). Therefore \(\min_m(x_m-x_*)^2=O((aQ)^{-3})\), giving
\[
 b_*=L+h x_*^2+O(aQ^{-3})=L+\frac{\pi^2a^2}{6Q^2}+O(aQ^{-3}).
\]
At small \(a\), the first index is optimal, and Taylor expansion of \(L+c/(a^2+4)-h/(a^2+4)^2\) gives \(1/3+\pi a/6+O(a^2)\). All error statements hold with the one parameter tending to the stated endpoint, not uniformly over changes in sphere dimension.

## Verification
The included standalone `checker.py` uses symbolic differentiation, independent high-precision quadrature of the cosine integrals, positivity/sharpness checks near active harmonics, and numerical solution of 39 consecutive transition equations. It passed **500 finite diagnostics**; these are not exhaustive checks of infinitely many modes. The proof's explicit rational Fourier expression, monotonic crossing inequality, finite-candidate reduction, and Vandermonde argument establish the infinite claims.

## Relationship to prior work
Huang–Li (2022, arXiv:2201.12856) explain why directly using ordinary Euclidean Matérn profiles with geodesic circle distance may fail positive definiteness and construct a different, SPDE-based circular Matérn covariance. Alegría–Cuevas-Pacheco–Diggle–Porcu (2021, arXiv:2101.05394) develop a different always-admissible spherical hypergeometric family. Those constructions do not imply the exact smallest nonnegative Laplace mixing coefficient for the ordinary geodesic Matérn-\(5/2\) profile, nor its unbounded critical-frequency staircase. A published geodesic-exponential second-harmonic modulation classification has an every-mode staircase but changes **angular Fourier frequencies by multiplication with \(\cos(2\theta)\)** rather than taking a distance-polynomial Matérn mixture; it neither gives the exponentially growing active mode nor the weight threshold here. Generic Fourier coefficient positivity characterizations supply the premise, not the explicitly optimized answer.

## Limitations
The repaired mixture has a nonzero cusp derivative at coincident sites, so it does **not** recover the mean-square smoothness of a genuine Matérn-\(5/2\) process on the circle. It is a sharp positive-semidefinite repair within one specific two-component, equal-scale mixture class, not a universal optimum among all valid circular covariances. Historical priority against older circle-model literature, especially alternate formulations of sharp signed mixture criteria, has not been independently settled. No claims for dimensions at least two are made.

## References
1. C. Huang and A. Li, *The Circular Matérn Covariance Function and its Link to Markov Random Fields on the Circle*, arXiv:2201.12856, first posted 2022-01-30, https://arxiv.org/abs/2201.12856 .
2. A. Alegría, F. Cuevas-Pacheco, P. Diggle, E. Porcu, *The F-family of covariance functions: A Matérn analogue for modeling random fields on spheres*, arXiv:2101.05394, first posted 2021-01-13, https://arxiv.org/abs/2101.05394 .
3. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077, first posted 2011-11-30, https://arxiv.org/abs/1111.7077 .
4. *Exact every-mode staircase for even-harmonic geodesic-exponential circle covariances*, public mathematical finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-exact-every-mode-staircase-for-even-harmonic-geodesic-exponentia--027cc81ac50f .
5. *Sharp circle-covariance modulation threshold and an unbounded Fourier-mode staircase*, public mathematical finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-circle-covariance-modulation-threshold-and-an-unbounded-fo--3df14ed06eed .

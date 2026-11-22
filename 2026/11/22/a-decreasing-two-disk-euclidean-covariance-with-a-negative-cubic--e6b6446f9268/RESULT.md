# A decreasing two-disk Euclidean covariance with a negative cubic spherical coefficient

## Finding

Let \(B_R=\{x\in\mathbb R^2:|x|\le R\}\), and form the positive two-disk seed
\[
g(x)=3\mathbf 1_{B_{1/2}}(x)+2\mathbf 1_{B_{3/2}}(x).
\]
Set \(F=g*g\) and \(\varphi(r)=F(re_1)/F(0)\). This is a continuous, nonnegative, radially nonincreasing, strictly positive-definite Euclidean covariance on \(\mathbb R^2\), with \(\varphi(0)=1\) and exact support \([0,3]\subset[0,\pi)\). Nevertheless, the unchanged geodesic covariance \(\varphi(\arccos(u\cdot v))\) on \(\mathbb S^2\) is not positive definite: its degree-three Legendre coefficient is strictly negative, whereas its coefficients of degrees zero, one, and two are strictly positive. In fact,
\[
\int_0^\pi\varphi(r)P_3(\cos r)\sin r\,dr<-\frac1{5700}.
\]
This identifies failure within the nonnegative *monotone* subclass, beyond the general even-dimensional transfer counterexamples.

## Assumptions and scope

All convolutions are on planar Lebesgue space. The seed is real, even, radial, and compactly supported. Positive definite refers to every finite complex quadratic form, with strictness for distinct sampling points. The sphere is the unit two-sphere with intrinsic great-circle distance \(\theta=\arccos(u\cdot v)\in[0,\pi]\). The support endpoint is exactly \(3\), which is less than \(\pi\). The normalized degree-\(\ell\) coefficient has the same sign as
\[
I_\ell=\int_0^\pi\varphi(r)P_\ell(\cos r)\sin r\,dr.
\]
Only the first four coefficients are classified; no claim is made concerning later degrees.

## Proof

**Euclidean geometry and positivity.** The seed equals \(5\) on \(B_{1/2}\), \(2\) on \(B_{3/2}\setminus B_{1/2}\), and zero outside. Direct integration gives \(F(0)=\|g\|_2^2=57\pi/4\). Its autocorrelation is continuous and \(\widehat F=|\widehat g|^2\ge0\). Since \(\widehat g(0)=\int g>0\), this density is positive near the origin, so its quadratic form is strictly positive for distinct points: a nonzero exponential polynomial cannot vanish on an open set. Also \(F\) is a positive combination of overlapping-disk areas \(|B_R\cap(B_S+x)|\), each nonincreasing in \(|x|\). Thus \(F\) is nonnegative and radially nonincreasing. Positivity of the seed on the open disk of radius \(3/2\) implies \(F(x)>0\) whenever \(|x|<3\), and \(F(x)=0\) at \(|x|\ge3\).

**Reduction to an Abel integral.** Use \(\widehat h(\xi)=\int h(x)e^{-ix\cdot\xi}\,dx\) and define
\[
G(t)=\frac{3(1/2)J_1(t/2)+2(3/2)J_1(3t/2)}{t},\quad
A_a=\int_0^{\pi/2}G(a\sin u)^2\sin u\,du.
\]
The continuous value \(G(0)=21/8\) is understood. Disk Fourier transformation gives \(\widehat g(t)=2\pi G(t)\). Radial Fourier inversion, followed by the Abel-regularized Bessel sine integral
\[
\lim_{\varepsilon\downarrow0}\int_0^\infty e^{-\varepsilon r}J_0(\rho r)\sin(ar)\,dr
=\frac{\mathbf1_{\rho<a}}{\sqrt{a^2-\rho^2}}
\]
under an integrable endpoint limit, yields
\[
\int_0^\infty F(re_1)\sin(ar)\,dr=2\pi a A_a.
\]
The trigonometric Legendre identities
\[
\sin rP_2(\cos r)=\frac{-\sin r+3\sin3r}{8},\qquad
\sin rP_3(\cos r)=\frac{-2\sin2r+5\sin4r}{16}
\]
therefore give
\[
I_0=\frac8{57}A_1,\quad I_1=\frac4{57}A_2,\quad
I_2=\frac{9A_3-A_1}{57},\quad I_3=\frac{2(5A_4-A_2)}{57}.
\]

**Exact cubic sign certificate.** The Bessel series defines positive rational coefficients
\[
b_k=\frac{3(1/2)^{2k+2}+2(3/2)^{2k+2}}{2^{2k+1}k!(k+1)!},\quad
c_m=\sum_{k=0}^m b_kb_{m-k},\quad
h_m=\frac{4^m(m!)^2}{(2m+1)!}.
\]
Absolute convergence and the beta integral imply
\[
A_a=\sum_{m=0}^\infty(-1)^m a^{2m}c_mh_m.
\]
Here \(b_0=21/8\), \(h_m\le1\), and Vandermonde's identity gives
\[
0\le c_m\le\left(\frac{21}{8}\right)^2
\frac{(9/4)^m}{(m!)^2}.
\]
Write \(A_a^{[28]}=\sum_{m=0}^{27}(-1)^m a^{2m}c_mh_m\). For \(a\in\{1,2,3,4\}\), its rigorous absolute truncation error is bounded by
\[
E_{a,28}=\left(\frac{21}{8}\right)^2
\frac{(9a^2/4)^{28}}{(28!)^2\,[1-(9a^2/4)/29^2]}.
\]
The accompanying `certificate.py` computes these exact rational values (not floating-point quadrature) and verifies
\[
5A_4^{[28]}-A_2^{[28]}+5E_{4,28}+E_{2,28}< -\frac1{200},
\]
\[
9A_3^{[28]}-A_1^{[28]}-9E_{3,28}-E_{1,28}>1,
\]
and \(A_1^{[28]}>E_{1,28}\), \(A_2^{[28]}>E_{2,28}\). Thus \(I_0,I_1,I_2>0\), while \(I_3<-1/5700<0\). Schoenberg's nonnegative-Legendre-coefficient criterion forbids spherical positive definiteness, proving the claim.

## Verification

Run `python3 certificate.py` with the Python standard library. The program uses exact fractions and factorials, checks all four required sign bounds and prints the truncated cubic expression and its rigorous tail bound. The computed central value is approximately \(-0.005618338733205308\) for \(5A_4-A_2\), with absolute error less than \(1.5\times10^{-14}\); these decimals are descriptive only, not proof. The inequalities above are exact rational comparisons. No numerical sampling is used to establish the global positive-definiteness claims.

## Relationship to prior work

Ge (2026, arXiv:2608.22173), Section 3 and its appendix, proves a dimension-two failure with a **signed three-disk seed** and a negative *degree-two* coefficient; its general theorem supplies counterexamples with arbitrarily small support but does not establish this positive, decreasing two-disk subclass. The Abel/Bessel method and Schoenberg criterion are established tools, not claimed as new. Huang and Zhang (2026, arXiv:2608.25639) construct exact-support smooth Euclidean examples by differential filtering, likewise without the stated monotone nonnegative two-disk conclusion. Gneiting (2013, arXiv:1111.7077) describes the odd-dimensional transfer mechanism and the motivating spherical covariance question. The present assertion concerns a stronger shape restriction but does not improve the known general counterexample theorem.

## Limitations

This gives one explicit example in planar Euclidean and spherical dimension two, at support radius exactly three; it is not a classification or an arbitrarily-small-support theorem for monotone kernels. The profile need not be convex or infinitely differentiable. Only the first four spherical coefficients are determined. Priority against unindexed examples in Euclid-hat or covariance-mixture literature remains a bibliographic risk; no independent mathematical audit has been performed.

## References

- Yan Ge, *Isotropic Positive Definite Functions on Spheres: Even-Dimensional Gneiting's Problem*, first posted August 23, 2026, https://arxiv.org/abs/2608.22173.
- Wentao Huang and Haizhang Zhang, *Exact-Support Counterexamples to Euclidean-to-Spherical Transfer of Positive Definiteness in Even Dimensions*, first posted August 26, 2026, https://arxiv.org/abs/2608.25639.
- Tilmann Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077, https://arxiv.org/abs/1111.7077.
- I. J. Schoenberg, *Positive definite functions on spheres*, Duke Mathematical Journal 9 (1942), 96–108.

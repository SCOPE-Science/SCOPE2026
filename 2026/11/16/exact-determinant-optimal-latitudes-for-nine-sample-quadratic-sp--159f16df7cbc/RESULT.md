# Exact determinant-optimal latitudes for nine-sample quadratic spherical harmonics

## Finding

Let \(\mathcal H_{\leq 2}\) be the nine-dimensional space of complex spherical harmonics of degrees \(0,1,2\) on the unit sphere \(\mathbb S^2\), with the standard orthonormal basis \(Y_\ell^m\) for surface-area measure. Fix the south pole as one sample. Place three further samples at constant height \(x\in(-1,1)\), equally spaced in longitude, and five samples at height \(y\in(-1,1)\), equally spaced in longitude. Assume \(x\ne y\); the two angular offsets are arbitrary. Let \(M(x,y)\) be the square matrix evaluating the nine basis functions at these nine sites.

The **exact determinant** is independent of the two angular offsets and satisfies

\[
|\det M(x,y)|^2=\frac{5189853515625}{1073741824\pi^9}
(1+x)^4(1-x)^2(1+y)^8(1-y)^6(y-x)^6.
\]

Among all permitted heights, the determinant has a **unique global maximum**, at

\[
x_*=\frac{11+\sqrt{2305}}{78}=0.756543788931\ldots,\qquad
 y_*=\frac{3}{26}-\frac{\sqrt{2305}}{130}=-0.253926273359\ldots.
\]

Every choice of the two angular offsets attains the same optimum. In particular, the samples determine every element of \(\mathcal H_{\leq 2}\) uniquely whenever \(-1<x,y<1\) and \(x\ne y\).

The conventional equiangular latitude choice \(x=\cos(\pi/5)\), \(y=\cos(3\pi/5)\) has a squared determinant lower by a factor \(1.12357901135\ldots\); the proposed heights increase the squared determinant by about \(12.36\%\). This is a determinant-optimality (information-volume) comparison, **not** a claim about the minimum singular value or worst-case condition number.

## Assumptions and scope

Write the spherical coordinates of a point as \((z,\phi)\), where \(z=\cos\theta\in[-1,1]\) is height and \(\phi\) is longitude. The nine locations, including the south pole, are

\[
\{(-1,0)\}\cup\{(x,\alpha+2\pi j/3):0\le j<3\}
\cup\{(y,\beta+2\pi k/5):0\le k<5\},
\]

with \(x,y\in(-1,1)\), \(x\ne y\) and \(\alpha,\beta\in\mathbb R\). Here the south-pole longitude is immaterial. The basis consists of the usual complex harmonics, orthonormal for total surface area \(4\pi\), ordered in any fixed way. Absolute determinants do not depend on that ordering or on the conventional harmonic phases.

No claim is made for arbitrary nine-point configurations, unequal longitude spacings, quadrature exactness, or optimal conditioning under other objectives. The optimization domain is specifically this minimal \(1+3+5\) iso-latitude architecture.

## Proof

**Step 1: exact factorization.** For each ring apply the unitary discrete Fourier transform to its sample rows. This changes neither the absolute determinant nor any Gram determinant. The two outer-ring channels with azimuthal orders \(\pm2\) isolate the degree-two harmonics \(Y_2^{\pm2}\), with radial factor \(1-y^2\). Eliminating their contributions from the other rows leaves the \(\pm1\) channels, one each from both rings. For each sign, the two remaining harmonic columns have radial factors proportional to

\[
\sqrt{1-z^2},\qquad z\sqrt{1-z^2}.
\]

The corresponding two-by-two determinant is therefore proportional to \(\sqrt{(1-x^2)(1-y^2)}(y-x)\). After these four columns are eliminated, the remaining three columns have azimuthal order zero and polynomial height dependence \(1,z,3z^2-1\). Their three-point evaluation determinant at heights \((-1,x,y)\) is proportional to the Vandermonde product \((1+x)(1+y)(y-x)\). Offset phases contribute only unit-modulus factors to the isolated Fourier channels. Combining the normalization constants

\[
\begin{aligned}
|Y_0^0|&=1/\sqrt{4\pi},\quad
|Y_1^0/z|=\sqrt{3/(4\pi)},\quad
|Y_2^0/(3z^2-1)|=\sqrt{5/(16\pi)},\\
|Y_1^1/(\sqrt{1-z^2}e^{i\phi})|&=\sqrt{3/(8\pi)},\\
|Y_2^1/(z\sqrt{1-z^2}e^{i\phi})|&=\sqrt{15/(8\pi)},\\
|Y_2^2/((1-z^2)e^{2i\phi})|&=\sqrt{15/(32\pi)}
\end{aligned}
\]

gives the unsquared identity

\[
|\det M|=\frac{2278125}{32768\pi^{9/2}}
(1-y^2)^3(1-x^2)(1+x)(1+y)|y-x|^3.
\]

Squaring and regrouping yields the displayed exact formula. Every displayed factor is positive in the stipulated domain, hence the interpolation matrix is invertible there.

**Step 2: strict concavity and candidate roots.** Removing the positive constant, define

\[
F(x,y)=(1+x)^4(1-x)^2(1+y)^8(1-y)^6(y-x)^6.
\]

On each open chamber \(-1<x<y<1\) and \(-1<y<x<1\), the logarithm \(\log F\) is strictly concave: it is a sum of positive multiples of logarithms of positive affine functions, and its pure \(x\)- and pure \(y\)-curvatures are both strictly negative. Furthermore \(F\to0\) on every chamber boundary. Thus each chamber has one and only one interior maximizer, determined by the stationary equations. Clearing their nonzero denominators produces

\[
6x^2-3xy-x+y-3=0,\qquad
7xy-x-10y^2+y+3=0.
\]

Eliminating \(y\) gives, apart from noninterior endpoint roots, the polynomial \(39x^2-11x-14\). The two interior stationary pairs are

\[
\left(\frac{11+\sqrt{2305}}{78},\frac3{26}-\frac{\sqrt{2305}}{130}\right)
\quad\text{and}\quad
\left(\frac{11-\sqrt{2305}}{78},\frac3{26}+\frac{\sqrt{2305}}{130}\right).
\]

The first pair is in the chamber \(y<x\), and the second is in \(x<y\). Each therefore uniquely optimizes its chamber.

**Step 3: compare the two chambers without floating-point assumptions.** For the second pair, the rigorous rational bounds \(-0.475<x<-0.474\) and \(0.484<y<0.485\) imply

\[
F(x,y)<(0.53)^4(1.48)^2(1.49)^8(0.52)^6(0.97)^6<\frac1{10}.
\]

Meanwhile the rational test pair \((3/4,-1/4)\) is in the first chamber and satisfies

\[
F(3/4,-1/4)=\frac{246140015625}{1099511627776}>\frac15.
\]

Hence the first stationary pair is the unique global maximizer. No boundary configuration attains a positive maximum, and the entire claim follows.

## Verification

The accompanying stand-alone script `check.py` constructs all nine normalized degree-at-most-two spherical harmonics directly, evaluates the complex determinant by Gaussian elimination for independently rotated three- and five-point rings, and compares it with the closed form at specified interior and critical configurations. It verifies the exact algebraic critical-point equations to numerical tolerance, and checks the improvement against the equiangular reference. These finite comparisons check the normalization and arithmetic independently; the proof of global optimality is the analytic strict-concavity argument above.

## Relationship to prior work

Earlier work on odd-point spherical latitude interpolation, summarized by zu Castell, Laín Fernández and Xu (2004), already establishes broad unisolvence for many choices of odd-population regular rings; unisolvence by itself is not claimed as new. Khalid, Kennedy and McEwen introduced the \(L^2\)-sample, \(1+3+\cdots+(2L-1)\) iso-latitude architecture in 2014. For \(L=3\) it has nine points as here, but their ring placement is chosen from an equiangular candidate set with numerical conditioning considerations. Nafees et al. (2017) likewise optimize selected ring latitudes for the condition numbers of separated-order matrices, using a finite equiangular candidate set rather than optimizing the global evaluation determinant continuously. Haines (first published December 2024) considers optimal exact designs in spherical harmonic regression, especially spherical designs, under a different design class. An and Zhuang (first public January 2026) survey extremal determinant-based spherical designs and interpolation. The present statement is the exact continuous-height, minimal nine-sample determinant optimum within the \(1+3+5\) architecture. It is not an unrestricted Fekete-point theorem and does not follow merely from the earlier conditioning procedures.

## Limitations

The optimization is for the square collocation determinant and may select heights different from those optimizing the smallest singular value or numerical stability of a specific spherical harmonic transform. The sample scheme uses a fixed south pole, fixed populations \(1,3,5\), and regular azimuthal spacings. The proof establishes no global optimality over other nine-point geometries. Priority risk remains that an older equivalent Fekete/optimal-design calculation might subsume this constrained algebraic optimum; an independent literature audit has not been conducted.

## References

1. W. zu Castell, N. Laín Fernández and Y. Xu, *Polynomial Interpolation on the Unit Sphere II*, 2004, https://arxiv.org/abs/math/0407448.
2. Z. Khalid, R. A. Kennedy and J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, 2014, https://arxiv.org/abs/1403.4661.
3. W. Nafees, Z. Khalid, R. A. Kennedy and J. D. McEwen, *Optimal-Dimensionality Sampling on the Sphere: Improvements and Variations*, 2017, https://arxiv.org/abs/1709.02497.
4. L. M. Haines, *Optimal designs for spherical harmonic regression*, first published 9 December 2024, https://doi.org/10.1007/s00362-024-01630-5.
5. C. An and X. Zhuang, *A Survey on Spherical Designs: Existence, Numerical Constructions, and Applications*, first public 17 January 2026, https://arxiv.org/abs/2601.11963.

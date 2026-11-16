# A sharp four-site onset and universal sign reversal for cyclic Poisson-kernel precision

## Finding
Let \(0<r<1\), let \(n\ge2\) be an integer, and let
\[
P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}
=\sum_{k\in\mathbb Z}r^{|k|}e^{ik\theta}.
\]
At the regular \(n\)-gon \(\theta_j=2\pi j/n\), put \(\Sigma_{ij}=P_r(\theta_i-\theta_j)\), \(Q=\Sigma^{-1}\), and \(q_d=Q_{0d}\). The matrix is strictly positive definite for every \(n,r\). Its exact Fourier eigenvalues are
\[
\lambda_j=\frac{n(r^j+r^{n-j})}{1-r^n},\quad 0\le j<n,
\qquad q_d=\frac1n\sum_{j=0}^{n-1}\frac{\cos(2\pi jd/n)}{\lambda_j}.
\]
For \(1\le d\le\lfloor n/2\rfloor\) the following sharp endpoint laws hold. Writing \(h=\lfloor n/2\rfloor\),
\[
q_d\sim\begin{cases}
\displaystyle\frac{(-1)^d}{2n^2}\,r^{-h},&n=2h,\\[3pt]
\displaystyle\frac{2(-1)^d\cos(\pi d/n)}{n^2}\,r^{-h},&n=2h+1,
\end{cases}\quad(r\downarrow0),
\]
and
\[
q_d=-\frac{(1-r)^3}{4[1-\cos(2\pi d/n)]}+O_n((1-r)^4)
\quad(r\uparrow1).
\]
For \(n\le3\), every off-diagonal precision entry is strictly negative for every \(r\). Beginning sharply at \(n=4\), **every even cyclic distance** \(2\le d\le\lfloor n/2\rfloor\) has a positive precision entry at sufficiently small \(r\) and a negative one near \(r=1\); therefore it has at least one intermediate zero, an exact conditional-independence configuration.

For the first two nontrivial sizes the transition is unique. Put
\[
U_4=1+\sqrt5,\quad
r_4=\frac{U_4-\sqrt{U_4^2-4}}2=0.3460143392\ldots,
\]
\[
U_5=\frac{3+\sqrt5+\sqrt{(3+\sqrt5)^2+16}}4,\quad
r_5=\frac{U_5-\sqrt{U_5^2-4}}2=0.3896071423\ldots.
\]
At \(n=4\) or \(5\), \(q_1<0\) always and \(q_2\) is positive for \(r<r_n\), zero exactly at \(r=r_n\), and negative for \(r>r_n\). Consequently the Gaussian conditional-independence graph is the cycle \(C_n\) exactly at this unique critical radius and the complete graph otherwise. No uniqueness or full sign classification is claimed for \(n\ge6\).

## Assumptions and scope
The circle is \(\mathbb R/(2\pi\mathbb Z)\); sample points are distinct and equispaced. The covariance is the *classical Poisson kernel*, not the circular Matérn, heat, geodesic exponential, or squared-distance Gaussian kernel. There is no observation nugget. For a nonsingular Gaussian vector, \(Q_{ij}=0\) for distinct sites is equivalent to conditional independence given all remaining sites; the partial-correlation sign is the negative of the precision-entry sign. The normalization \(P_r(0)=(1+r)/(1-r)\) is used throughout. A common positive rescaling of the covariance changes magnitudes, not signs or zero sets.

## Proof
**Strict positivity and aliasing.** All Fourier weights \(r^{|k|}\) are positive. For a nonzero vector \(c\),
\[
c^*\Sigma c=\sum_{k\in\mathbb Z}r^{|k|}\left|\sum_{j=0}^{n-1}c_je^{-ik\theta_j}\right|^2>0,
\]
because the first \(n\) Fourier sums form an invertible discrete Fourier transform. Summing the absolutely convergent weights over residues modulo \(n\) yields
\[
\sum_{\ell\in\mathbb Z}r^{|j+n\ell|}
=\frac{r^j+r^{n-j}}{1-r^n},\quad 0\le j<n.
\]
The discrete Fourier transform diagonalizes \(\Sigma\), proving the eigenvalue and inverse-entry formulas in the finding, including the \(j=0\) convention.

**Small-radius asymptotics.** If \(n=2h\), the unique reciprocal eigenvalue of dominant order is at \(j=h\):
\[
\lambda_h^{-1}=\frac{1-r^n}{2nr^h},
\qquad
\lambda_j^{-1}=O_n(r^{-(h-1)})\quad(j\ne h).
\]
Inserting its Fourier character \(\cos(\pi d)=(-1)^d\) gives the even case. For \(n=2h+1\) the two dominant terms lie at \(j=h,h+1\), each asymptotic to \((nr^h)^{-1}\). Their combined character is \(2(-1)^d\cos(\pi d/n)\), giving the odd case. The cosine is strictly positive for all shortest nonzero distances \(d\le h\); hence these asymptotics determine the signs without cancellations.

**Near-boundary asymptotics.** Set \(\delta=1-r\) and \(a=P_r(0)=(2-\delta)/\delta\). For a fixed nonzero sampled angle \(\vartheta\),
\[
P_r(\vartheta)=\frac{\delta}{1-\cos\vartheta}+O_n(\delta^2).
\]
Thus \(\Sigma=aI+E\), where \(E\) has zero diagonal and off-diagonal entries of order \(\delta\). The convergent Neumann expansion gives \(\Sigma^{-1}=a^{-1}I-a^{-2}E+O_n(\delta^5)\) in off-diagonal entries, with the \(O_n(\delta^4)\) correction from expanding \(a^{-2}E\). This proves the negative cubic law. For even \(d\ge2\), the two endpoints have opposite strict signs. Continuity of \(Q\) on \((0,1)\) and the intermediate-value theorem prove at least one zero. For \(n=2,3\), all distinct points are adjacent and the covariance has the compound-symmetry form \((a-b)I+b\mathbf1\mathbf1^T\), with \(a>b>0\). Its inverse has every off-diagonal entry \(-b/[(a-b)(a+(n-1)b)]<0\).

**Exact quadrilateral transition.** Elementary inversion of the four Fourier eigenvalues gives
\[
q_1=\frac{(r-1)^3(r+1)^3(r^2+1)}{32r^2(r^4+1)}<0,
\]
\[
q_2=\frac{(1-r)^3(1+r)(r^4-2r^3-2r^2-2r+1)}{32r^2(r^4+1)}.
\]
With \(u=r+r^{-1}\), the last numerator's quartic factor equals \(r^2(u^2-2u-4)\). The parameter \(u\) decreases strictly from infinity to \(2\) as \(r\) rises from zero to one. The unique root in \(u>2\) is \(U_4=1+\sqrt5\), proving the first exact classification.

**Exact pentagon transition.** Let \(s=\sqrt5\), \(D=(1+r^5)(r+r^4)(r^2+r^3)>0\), \(B=(1-r^5)/25>0\), and \(F=r(1-r)^2(1+r)^2/(2D)>0\). Pairing the two conjugate Fourier eigenvalue classes, using \(\cos(2\pi/5)=(s-1)/4\) and \(\cos(4\pi/5)=-(s+1)/4\), yields
\[
q_1=-B(1+s)F\,H_1(r),\qquad q_2=B(s-1)F\,H_2(r),
\]
\[
H_1(r)=r^4+r^2+1-\frac{3-s}{2}(r^3+r),\quad
H_2(r)=r^4+r^2+1-\frac{3+s}{2}(r^3+r).
\]
Since \(r^4+1\ge r^3+r\) on \((0,1)\) and \((3-s)/2<1\), \(H_1(r)>0\). Writing again \(u=r+r^{-1}\),
\[
H_2(r)=\frac{r^2}{2}\bigl[2u^2-(3+s)u-2\bigr].
\]
The bracket has exactly one root on \(u>2\), namely \(U_5\), and is positive above it and negative below it. The strictly decreasing correspondence \(r\mapsto u\) gives the unique pentagonal zero and its signs. The only distinct-site distances for these polygons are one and two, so their conditional-independence graph is precisely the respective cycle at the critical radius and complete elsewhere.

## Verification
The standalone standard-library script `CHECKER.py` checks the exact Fourier formula against separately formed spatial covariances and independent Gauss–Jordan inverses for sample sizes \(2\) through \(12\) and four values of \(r\). It separately checks the factored quadrilateral and pentagon formulas, their root signs, and endpoint asymptotics on larger cycles. Run `python3 CHECKER.py`; the expected output begins `PASS: 3084`. All universal statements above are proved analytically; finite checks are not used as infinite proofs.

## Relationship to prior work
Borovitskiy, Terenin, Mostowsky and Deisenroth (2020, arXiv:2006.10160) establish spectral constructions of Gaussian-process kernels on compact manifolds and explicit Fourier series for circular Matérn and squared-exponential covariances. Huang and Li (2022, arXiv:2201.12856) derive circular Matérn covariance/conditional-autoregression connections, with exact order-one structure. Barnett, Greengard and Rachh (2023, arXiv:2305.11065) develop Fourier-grid covariance approximations, aliasing bounds and matrix conditioning. Those sources motivate the distinction between a kernel's Fourier eigenvalues and the sign structure of its *finite-sample inverse*; they do not supply the classical Poisson-kernel sign-reversal theorem above.

A separately published result on nonstationary Poisson-kernel modulation determines when its Gram matrices become singular, rather than describing inverse signs of the unmodulated stationary kernel. Fourier diagonalization and the Poisson expansion are classical and are not claimed as novel. The assessed contribution is the uniform-in-size alternating-to-attractive sign change, its sharp minimum sample size, and the complete exact four-/five-sample boundaries.

## Limitations
The theorem makes no uniqueness claim for the zero of \(q_d\) for general \(n\ge6\), nor any global odd-distance sign claim there. Endpoint statements are asymptotic, not exact equalities at \(r=0\) or \(r=1\), where the covariance scaling becomes singular. Irregular sampling, observation noise, and other circular covariances are outside scope. Historical novelty is assessed against selected full texts, mathematical-record searches and accessible related claims; an unindexed general inversion theorem could contain an equivalent result. No independent mathematical audit has been performed.

## References
1. V. Borovitskiy, A. Terenin, P. Mostowsky and M. P. Deisenroth, *Matérn Gaussian processes on Riemannian manifolds*, arXiv:2006.10160, first public 2020-06-17, https://arxiv.org/abs/2006.10160.
2. C. Huang and A. Li, *The Circular Matérn Covariance Function and its Link to Markov Random Fields on the Circle*, arXiv:2201.12856, first public 2022-01-30, https://arxiv.org/abs/2201.12856.
3. A. Barnett, P. Greengard and M. Rachh, *Uniform approximation of common Gaussian process kernels using equispaced Fourier grids*, arXiv:2305.11065, first public 2023-05-18, https://arxiv.org/abs/2305.11065.

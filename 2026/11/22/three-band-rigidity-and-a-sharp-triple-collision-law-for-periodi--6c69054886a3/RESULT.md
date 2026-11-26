# Exact singular bands and a quarter-grid crossing in three-periodic Fourier interpolation

## Finding

Let \(m\ge1\) be an integer, \(N=3m\), and \(0\le\varepsilon<1\). For \(0\le j<m\), set
\[
x_{3j}=\frac{3j+\varepsilon}{N},\qquad x_{3j+1}=\frac{3j+1}{N},\qquad
x_{3j+2}=\frac{3j+2-\varepsilon}{N}.
\]
The normalized Fourier interpolation matrix has entries \((F_{\varepsilon,N})_{\ell,k}=N^{-1/2}\exp(2\pi i k x_\ell)\), for \(0\le\ell,k<N\). Put
\[
\theta=\frac{2\pi(1-\varepsilon)}3,\qquad
a=\frac{1+2\cos\theta}{3},\qquad b=\frac{1+2\cos(2\theta)}{3},\qquad
\Delta=\sqrt{b^2/4+2a^2}.
\]
Then the complete squared singular spectrum is the multiset obtained by repeating each of
\[
\lambda_-=1+b/2-\Delta,\qquad
\lambda_{\mathrm{odd}}=1-b,\qquad
\lambda_+=1+b/2+\Delta
\]
exactly \(m\) times. For \(0<\varepsilon<1\), \(\lambda_-\) is the least level. The largest is \(\lambda_{\mathrm{odd}}\) for \(0<\varepsilon<1/4\) and \(\lambda_+\) for \(1/4<\varepsilon<1\). The only interior degeneracy is at \(\varepsilon=1/4\), where the levels are \(1/3,4/3,4/3\). Thus the exact Euclidean condition number at all displacements before coalescence is \(\sqrt{\max(\lambda_{\mathrm{odd}},\lambda_+)/\lambda_-}\), independent of \(m\) (and equal to 1 at \(\varepsilon=0\)). At \(\varepsilon=1\), the formula for the same matrix with repeated nodes gives rank \(m\) and squared singular levels \(0,0,3\), each repeated \(m\) times.

## Assumptions and scope

The Fourier frequencies are the consecutive integers \(0,\ldots,N-1\), all sampling weights are \(1/N\), and the sample positions have the specified symmetric three-periodic pattern. There is no assertion for arbitrary jitter, other frequencies, or weighted least squares. The endpoint \(\varepsilon=1\) uses the displayed nodes with repetitions retained.

## Proof

**Repeated blocks.** Write \(k=q+sm\), with \(0\le q<m\), \(s=0,1,2\), and set \((y_0,y_1,y_2)=(\varepsilon,1,2-\varepsilon)\). Since \(x_{3j+r}=(3j+y_r)/N\),
\[
(F_{\varepsilon,N})_{3j+r,q+sm}
=m^{-1/2}e^{2\pi i qj/m}\,e^{2\pi i qy_r/N}\,3^{-1/2}e^{2\pi i s y_r/3}.
\]
For each \(r\), a unitary length-\(m\) forward DFT in \(j\) selects the index \(q\). After reordering and absorbing the row phase \(e^{2\pi i qy_r/N}\), the matrix is unitarily equivalent to \(m\) identical copies of \(B_{r,s}=3^{-1/2}e^{2\pi i s y_r/3}\).

**Parity decomposition.** Subtracting 1 from the frequency index \(s\) in each row amounts to a row phase. Summing over the centered indices \(-1,0,1\) makes the Gram matrix real, with adjacent entry \(a\), endpoint entry \(b\), and diagonal 1. The odd vector \((1,0,-1)\) has eigenvalue \(1-b\), and the even subspace with basis \((1,0,1)/\sqrt2,(0,1,0)\) has matrix
\[
\begin{pmatrix}1+b&\sqrt2a\\\sqrt2a&1\end{pmatrix}.
\]
This gives the two quadratic roots. The original block is a square Vandermonde matrix on three distinct points of the unit circle for \(\varepsilon<1\), so the Gram levels are positive. At \(\varepsilon=0\) the Gram matrix is the identity, and at \(\varepsilon=1\) its entries are all 1.

**Ordering.** In the open range set \(c=\cos\theta\), so \(-1/2<c<1\), \(a>0\), \(a-b=2(1-c)(1+2c)/3>0\). The even levels are distinct. The difference \(\lambda_{\mathrm{odd}}-\lambda_-=\Delta-3b/2\) is positive if \(b\le0\), and if \(b>0\) the inequality \(a>b\) gives \(\Delta>3b/2\). For the upper levels their difference \(\lambda_+-\lambda_{\mathrm{odd}}=\Delta+3b/2\) is positive if \(b\ge0\). For \(b<0\), its sign is the sign of \(\Delta^2-9b^2/4=2(a-b)(a+b)\). Now \(a+b=2ac\); if \(c\le0\) then \(b=2ac-a<0\). Thus the sign of the upper-level difference is precisely the sign of \(c\) throughout the open interval. At the crossing \(\theta=\pi/2\) we have \(a=1/3,\ b=-1/3\), giving the stated levels.

## Collision check and relation to the known leading law

The band formula also recovers the known quadratic coalescence of a symmetric Fourier triple. The Vandermonde determinant gives the product of the three squared singular levels of one block as
\[
\frac{(2\sin(\theta/2))^4(2\sin\theta)^2}{27}
=\frac{4\theta^6}{27}\bigl(1+O(\theta^2)\bigr).
\]
Since \(\lambda_{\mathrm{odd}}=4\theta^2/3+O(\theta^4)\) and \(\lambda_+=3+O(\theta^2)\), division gives \(\lambda_-=\theta^4/27\,(1+O(\theta^2))\). In terms of \(t=1-\varepsilon\),
\[
\sigma_{\min}(F_{\varepsilon,N})=\frac{4\pi^2}{27\sqrt3}\,t^2(1+O(t^2)),\qquad
\kappa_2(F_{\varepsilon,N})=\frac{81}{4\pi^2}\,t^{-2}(1+O(t^2)).
\]
The remainders are independent of \(m\) because the block is exactly repeated. The leading constants already follow from the midpoint theorem in [1]: center the source positions, shift the frequency indices to \(-1,0,1\), then transpose the block. It is the aperture of [1] with three equal weights, normalized source positions \((-1,0,1)\), and separation parameter \(\delta=\theta\). Its least-singular-value coefficient in \(\theta\) is \(1/(3\sqrt3)\), and its condition-number coefficient is 9. This check is not a new claim of either leading constant.

## Verification

The accompanying `checker.py` uses the Python 3 standard library only. It constructs the full matrices for sizes \(3,6,9,12,15,18,24,36\), compares the first three Gram spectral power sums at eleven displacements per size, and checks the quarter-step degeneracy and near-collision scalings. These finite numerical checks supplement, but do not replace, the block reduction and analytic ordering proof.

## Relationship to other prior work and limitations

Periodic multichannel Fourier reduction is a standard technique; the contribution here is the explicit complete spectrum, with the exact interior crossing and identification of the top branch for every displacement. Chen–Lin–Zhang [2] give general periodic-interpolation estimates, including clustered-node bounds in a rectangular oversampled regime; the bounds do not state the exact square three-period spectrum. Strohmer–Tanner [3] treat reconstruction from periodic nonuniform samples, and general perturbed interpolation is studied by Austin–Trefethen [4]. Earlier three-coset or polyphase calculations could contain an equivalent formula; no exhaustive historical priority claim is made. Arbitrary perturbations need not have the repeated-block structure used here.

## References

1. *Universal midpoint optimality and a sharp three-source Fourier superresolution constant*, 2026-11-08. https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-universal-midpoint-optimality-and-a-sharp-three-source-fourier-s--0602ba6c6c22
2. L. Chen, R. Lin and H. Zhang, *Smallest Singular Value Estimates for Nonuniform Fourier Matrices via Periodic Nonuniform Sampling*, arXiv:2608.21960. https://arxiv.org/abs/2608.21960
3. T. Strohmer and J. Tanner, *Fast Reconstruction Methods for Bandlimited Functions from Periodic Nonuniform Sampling*, SIAM J. Numer. Anal. 44 (2006), 1073–1094. https://doi.org/10.1137/040609586
4. A. P. Austin and L. N. Trefethen, *Trigonometric interpolation and quadrature in perturbed points*, SIAM J. Numer. Anal. 55 (2017), 2113–2122. https://doi.org/10.1137/16M1106287

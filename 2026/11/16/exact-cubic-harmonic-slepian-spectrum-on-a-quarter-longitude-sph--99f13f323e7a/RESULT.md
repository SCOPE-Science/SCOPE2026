# Exact cubic-harmonic Slepian spectrum on a quarter-longitude spherical lune

## Finding
Let \(\Omega=\{(x,y,z)\in\mathbb S^2:x\ge0,\ y\ge0\}\), the spherical lune of longitude aperture \(\pi/2\). The concentration operator on the seven-dimensional complex space \(\mathcal H_3\) of pure degree-three spherical harmonics has exactly seven simple eigenvalues:
\[
\frac14,\quad \frac14\pm\frac{\sqrt{15}}{10\pi},\quad
\frac14\pm\frac{\sqrt{115}-5}{30\pi},\quad
\frac14\pm\frac{\sqrt{115}+5}{30\pi}.
\]
Consequently every nonzero \(f\in\mathcal H_3\) obeys the **sharp**, two-sided localization inequality
\[
\frac14-\frac{5+\sqrt{115}}{30\pi}\ \le\
\frac{\int_\Omega|f|^2\,d\sigma}{\int_{\mathbb S^2}|f|^2\,d\sigma}\ \le\
\frac14+\frac{5+\sqrt{115}}{30\pi}.
\]
The two bounds have one-dimensional complex equality spaces. The seven values occur in three symmetric pairs around the area fraction \(1/4\), plus one central eigenvalue.

## Assumptions and scope
Surface area \(d\sigma\) is the ordinary, unnormalized measure (the ratio and concentration operator are unchanged by common normalization). Write \(\mathcal H_3\) for the restrictions of complex-valued homogeneous harmonic cubics in \(\mathbb R^3\). The boundary of \(\Omega\) has surface measure zero; all membership inequalities may be weak. The result concerns a *single exact degree*, not the full degree-through-three band, and the precise ninety-degree longitude lune.

## Proof
Introduce the seven real orthogonal cubic spherical harmonics, restricted to \(\mathbb S^2\), in the following order:
\[
\begin{aligned}
p_0&=z(5z^2-3),&p_1&=z(x^2-y^2),&p_2&=2xyz,\\
p_3&=x(5z^2-1),&p_4&=y(5z^2-1),\\
p_5&=x(x^2-3y^2),&p_6&=y(3x^2-y^2).
\end{aligned}
\]
Each is the restriction of a homogeneous harmonic cubic (replace the constant \(1\) by \(x^2+y^2+z^2\) when homogenizing). Their squared full-sphere norms, in the same order, are
\[
\left(\frac{16\pi}7,\frac{16\pi}{105},\frac{16\pi}{105},
\frac{32\pi}{21},\frac{32\pi}{21},\frac{32\pi}{35},\frac{32\pi}{35}\right).
\]
Let \(e_j=p_j/\|p_j\|_{L^2(\mathbb S^2)}\). The Hermitian regional Gram matrix \(C_{ij}=\int_\Omega e_i e_j\,d\sigma\) is exactly
\[
C=\frac14 I_7+\frac1\pi\begin{pmatrix}
0&0&-\sqrt{15}/10&0&0&0&0\\
0&0&0&0&0&0&0\\
-\sqrt{15}/10&0&0&0&0&0&0\\
0&0&0&0&1/2&0&-\sqrt{15}/30\\
0&0&0&1/2&0&\sqrt{15}/30&0\\
0&0&0&0&\sqrt{15}/30&0&1/6\\
0&0&0&-\sqrt{15}/30&0&1/6&0
\end{pmatrix}.
\]
For completeness, to evaluate any monomial, parameterize \((x,y,z)=(\sqrt{1-z^2}\cos\phi,\sqrt{1-z^2}\sin\phi,z)\) with \(-1\le z\le1\) and \(0\le\phi\le\pi/2\). When the exponent \(c\) is even,
\[
\int_\Omega x^a y^b z^c\,d\sigma=
\frac{\Gamma((a+1)/2)\Gamma((b+1)/2)\Gamma((c+1)/2)}{2\Gamma((a+b+c+3)/2)};
\]
when \(c\) is odd the integral is zero. Expanding the products \(p_i p_j\) and using this identity yields \(C\), including its zero blocks, with no numerical approximation.

The first three coordinates form a block with eigenvalues \(1/4\) and \(1/4\pm\sqrt{15}/(10\pi)\). The remaining four coordinates form a block whose centered matrix has eigenvalues \(\pm(5+\sqrt{115})/(30\pi)\) and \(\pm(\sqrt{115}-5)/(30\pi)\). These seven values are distinct because
\[
0<\frac{\sqrt{115}-5}{30\pi}<\frac{\sqrt{15}}{10\pi}<\frac{\sqrt{115}+5}{30\pi}<\frac14.
\]
The spectral theorem gives both sharp energy inequalities and the claimed one-dimensional equality spaces: specifically they are the unique eigenlines of the displayed lower-right four-by-four block at its largest and smallest eigenvalues.

## Verification
Run `python verify_exact.py` with SymPy to reconstruct the seven orthogonal norms, the full regional matrix, and its exact characteristic polynomial. Independently, run `python verify_numeric.py` with NumPy: one hundred Gauss–Legendre nodes in each of the latitude and longitude directions reproduce all seven eigenvalues to an absolute error less than \(10^{-12}\). The latter is a numerical cross-check, not a substitute for the moment proof.

## Relationship to prior work
Simons, Dahlen and Wieczorek (2004) formulate the general spherical spatial-spectral concentration eigenproblem for arbitrary regions and focus on a polar cap and numerical approaches. Roddy and McEwen (first public February 12, 2023) develop Slepian wavelets on general manifolds and incomplete regions; neither work states the evaluated pure-cubic ninety-degree lune spectrum above. Related quadratic spherical-lune and quarter-wedge spectra treat a different harmonic degree. The present result is the complete closed radical spectrum and extremal stability constants of this canonical region-degree pair, not a new general Slepian principle.

## Limitations
Only the quarter-longitude lune and pure degree-three harmonics are covered. No general aperture formula, multidegree claim, or independent expert validation is asserted. A specialized unindexed table or computation of the same seven constants remains a potential priority overlap.

## References
1. P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on Manifolds*, arXiv:2302.06006 (first public 2023-02-12), https://arxiv.org/abs/2302.06006 .
2. F. J. Simons, F. A. Dahlen and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424 (2004), https://arxiv.org/abs/math/0408424 .

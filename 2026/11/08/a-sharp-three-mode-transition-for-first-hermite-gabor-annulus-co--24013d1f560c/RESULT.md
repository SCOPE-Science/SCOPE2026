# A sharp three-mode transition for first-Hermite Gabor annulus concentration

## Finding
Let \(h_j\) denote the normalized one-dimensional Hermite functions, \(h_0(t)=2^{1/4}e^{-\pi t^2}\), and \(h_1(t)=2\sqrt\pi\,t h_0(t)\). For each fixed \(b>0\) and integer \(n>b^2\), consider the radial phase-space annulus
\[
 E_{n,b}=\{(x,\xi)\in\mathbb R^2:n-b\sqrt n\le\pi(x^2+\xi^2)\le n+b\sqrt n\}
\]
and the positive short-time-Fourier localization operator
\[
 T_{n,b}=V_{h_1}^{*}\mathbf1_{E_{n,b}}V_{h_1}\quad\text{on }L^2(\mathbb R),
 \qquad V_gf(x,\xi)=\int_{\mathbb R}f(t)\overline{g(t-x)}e^{-2\pi i\xi t}\,dt.
\]
Its complete Hermite eigenvalue sequence is
\[
 T_{n,b}h_j=\lambda_{j,n}(b)h_j,\qquad
 \lambda_{j,n}(b)=\int_{n-b\sqrt n}^{n+b\sqrt n}
       \frac{(j-s)^2}{s}\frac{e^{-s}s^j}{j!}\,ds,\quad j\ge0.
\]
Define the standard normal density \(\varphi(y)=(2\pi)^{-1/2}e^{-y^2/2}\), cumulative distribution \(\Phi(y)=\int_{-\infty}^y\varphi(v)\,dv\), and
\[
 F_b(u)=\int_{u-b}^{u+b}y^2\varphi(y)\,dy.
\]
For every \(b>0\), there exists a unique \(U_b>b\) solving
\[
 \log\frac{U_b+b}{U_b-b}=bU_b.
\]
There is a unique threshold \(b_*\in(\sqrt2,2)\) characterized by
\[
 F_{b_*}(0)=F_{b_*}(U_{b_*}),\qquad
 b_*=1.524046518925874\ldots,\quad U_{b_*}=1.751131023931451\ldots.
\]
The global maximizers of \(F_b\) are precisely \(\{-U_b,U_b\}\) if \(0<b<b_*\), precisely \(\{-U_b,0,U_b\}\) if \(b=b_*\), and precisely \(\{0\}\) if \(b>b_*\). In particular,
\[
 \lim_{n\to\infty}\|T_{n,b}\|=\max\{F_b(0),F_b(U_b)\}.
\]
Every maximizing Hermite index \(j_n\) satisfies \((j_n-n)/\sqrt n=O_b(1)\), and its subsequential limits are contained in the stated maximizer set. Consequently \(\lvert j_n-n\rvert/\sqrt n\to U_b\) for \(b<b_*\), while \((j_n-n)/\sqrt n\to0\) for \(b>b_*\). At the threshold only subsequential containment in the three-point set is asserted, not an exact finite-\(n\) tie.

## Assumptions and scope
The time-frequency measure is planar Lebesgue measure, so that \(s=\pi(x^2+\xi^2)\) is the area coordinate, and \(\|h_1\|_2=1\). The parameter \(b\) is fixed and positive while the integer \(n\to\infty\); the inner radius is positive for \(n>b^2\). There is no truncation of the Hermite input space: the norm is the full \(L^2\) operator norm. The limit claim allows arbitrary choices among maximizing indices at each \(n\).

## Proof
**Exact diagonalization.** Rotation of the phase-space plane is implemented by the fractional Fourier transform, under which \(h_j\) are eigenvectors. Since the region and the analysis window \(h_1\) have definite rotation character, the radial localization operator is diagonal in the Hermite basis. More concretely, the normalized first-Hermite STFT identity gives (up to unit-modulus angular phase)
\[
 |V_{h_1}h_j(x,\xi)|^2
 =e^{-s}\frac{s^{j-1}(j-s)^2}{j!},\qquad s=\pi(x^2+\xi^2),
\]
including \(j=0\), when the expression is \(s e^{-s}\). Integration in \(d x\,d\xi=d s\,d\theta/(2\pi)\) yields the eigenvalue formula. It is normalized: for \(j\ge1\), if \(S\) has gamma distribution with shape \(j+1\), then \(\mathbb E(j-S)^2/S=j^2/j-2j+(j+1)=1\); for \(j=0\), \(\int_0^\infty se^{-s}\,ds=1\). Therefore all eigenvalues are in \([0,1]\) and the norm is their supremum. Since each fixed \(n\) has bounded annular support, eigenvalues decay as \(j\to\infty\), so the supremum is attained.

**Central-limit profile.** Put \(j=n+\lfloor u\sqrt n\rfloor\), \(s=n+v\sqrt n\) for bounded real \(u,v\). Uniform Stirling expansion of the Poisson mass gives
\[
 \frac{e^{-s}s^j}{j!}=\frac{\varphi(u-v)+o(1)}{\sqrt n},
 \qquad\frac{(j-s)^2}{s}=(u-v)^2+o(1),
\]
uniformly on compact \((u,v)\)-sets. Thus \(\lambda_{j,n}(b)\to\int_{-b}^b (u-v)^2\varphi(u-v)\,dv=F_b(u)\), locally uniformly in \(u\). By Stirling's inequality, for \(s\in[n-b\sqrt n,n+b\sqrt n]\) and \(j\ge0\), the Poisson point probabilities decay exponentially in the Poisson rate \(j\log(j/s)-j+s\). In the central range \(j\in[n/2,2n]\), the rate is bounded below by a constant times \((j-s)^2/n\), up to a harmless adjustment of the constant; polynomial factors from \((j-s)^2/s\) do not defeat this Gaussian tail. Beyond that range, the Poisson rate is linear in \(j\) or in \(n\), and dominates the same polynomial prefactor. Consequently
\[
 \lim_{R\to\infty}\limsup_{n\to\infty}\sup_{|j-n|\ge R\sqrt n}\lambda_{j,n}(b)=0.
\]
Since \(\max_uF_b(u)>0\), all maximizing indices are in the central range \(j=n+O_b(\sqrt n)\). Local uniform convergence and the preceding tail bound imply convergence of global maxima and containment of all limiting maximizing offsets in the argmax of \(F_b\).

**Classification of profile maximizers.** Set \(h(y)=y^2\varphi(y)\). Then \(F_b\) is even and
\[
 F'_b(u)=h(u+b)-h(u-b),\qquad
 F''_b(0)=2b(2-b^2)\varphi(b).
\]
For \(u>b\), the critical-point equation is exactly \(\log((u+b)/(u-b))=bu\). Its left side strictly decreases from infinity to zero as \(u\downarrow b\) then \(u\to\infty\), while the right side strictly increases; hence the unique root \(U_b>b\) is a strict outer maximum. For \(0<u<b\), the sign of \(F'_b(u)\) is that of
\[
 2\operatorname{artanh}(u/b)-bu.
\]
If \(b\le\sqrt2\), it is strictly positive for \(u>0\), so the only maxima are \(\pm U_b\). If \(b>\sqrt2\), the function above is strictly convex, starts at zero with negative slope, and tends to infinity at \(u\uparrow b\). It has exactly one additional positive root, a strict local minimum, while the center is a strict local maximum. Therefore every global maximizer lies in \(\{0,\pm U_b\}\).

**One and only one exchange of dominance.** Define \(D(b)=F_b(0)-F_b(U_b)\). For \(b=\sqrt2\), the function increases strictly from zero up to \(U_b\), hence \(D(\sqrt2)<0\). For \(b\to\infty\), \(F_b(0)\to\int_{\mathbb R}h=1\), whereas \(U_b>b\) implies \(F_b(U_b)\le\int_0^\infty h=1/2\), so eventually \(D(b)>0\). Smooth dependence of \(U_b\) follows from the nonzero derivative of its defining equation. Since \(U_b\) is stationary for \(F_b\), the envelope rule and equality \(h(U_b+b)=h(U_b-b)\) give
\[
 D'(b)=2\bigl(h(b)-h(U_b+b)\bigr)>0\qquad(b>\sqrt2).
\]
The strict inequality follows because \(h\) is strictly decreasing on \((\sqrt2,\infty)\) and \(U_b+b>b\). Hence exactly one crossing \(b_*\in(\sqrt2,\infty)\) exists. The interval \((\sqrt2,2)\) is rigorous: the Gaussian Mills bound \(1-\Phi(2)<\varphi(2)/2\) gives \(F_2(0)>1-5\varphi(2)>1/2\), while \(F_2(U_2)\le1/2\); hence \(D(2)>0\). The numerical values stated above are approximations, not mathematical exact definitions. This completes the proof.

## Verification
Run `python3 check.py` with Python 3, NumPy and SciPy. It computes the exact annular integrals from the Hermite formula, solves the scalar threshold equation, checks derivative and global-profile inequalities, and compares dominant Hermite indices at increasing radii. The included execution returned `FIRST_HERMITE_ANNULUS_CHECKS_PASS 471`. These numerical tests corroborate, but do not replace, the infinite-dimensional tail argument or the uniqueness proof.

## Relationship to prior work
Daubechies' classical radial Gaussian-window localization diagonalizes in Hermite functions. Knutsen studies Gaussian-window ring and Cantor-type regions and gives a unimodal Poisson-weight spectral comparison. Keller and Luef describe Hermite-window STFTs and polyanalytic Toeplitz calculus, including the Laguerre/Hermite overlap identity. Abreu explicitly presents the first-Hermite-window spectrogram expansion. None of the cited inspected statements supplies the annular central-limit profile's global three-way mode transition, the unique exchange threshold, or maximizing-index asymptotics. The eigenvalue kernel itself is a known formula and is not claimed new. An unlocated earlier derivation of the transition in Landau-level or displacement-number-statistics literature remains possible.

## Limitations
The observation domains are symmetric annuli of radial-area center \(n\) and width \(2b\sqrt n\); the window is exactly the first excited Hermite function. No claim is made for higher window order, nonsymmetric radial shells, general planar sets, finite radius mode ties, or uniformity when \(b\) varies with \(n\). The result is analytic but has not been independently audited. Numerical constants are not used to establish existence or uniqueness.

## References
1. J. Keller and F. Luef, *Polyanalytic Toeplitz Operators: Isomorphisms, Symbolic Calculus and Approximation of Weyl Operators*, arXiv:1905.07741 (first public 2019-05-19); J. Fourier Anal. Appl. 27 (2021), article 47, https://doi.org/10.1007/s00041-021-09843-0.
2. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets I*, arXiv:1907.00848 (first public 2019-07-01); J. Fourier Anal. Appl. 26 (2020), article 47, https://doi.org/10.1007/s00041-020-09751-9.
3. L. D. Abreu, *Local Maxima of White Noise Spectrograms and Gaussian Entire Functions*, arXiv:2210.06721 (first public 2022-10-13); J. Fourier Anal. Appl. 28 (2022), article 88, https://doi.org/10.1007/s00041-022-09979-7.
4. I. Daubechies, *Time-frequency localization operators: a geometric phase space approach*, IEEE Trans. Inf. Theory 34 (1988), 605–612, https://doi.org/10.1109/18.9761.
5. N. Faustino, *Localization and Toeplitz Operators on Polyanalytic Fock Spaces*, arXiv:1107.4680 (2011).

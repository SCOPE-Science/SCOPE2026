# The lower-shoulder selection law for thin first-Hermite localization annuli

## Finding
Fix an arbitrary annular area \(L>0\). For \(s\ge0\), write
\[
 E_{s,L}=\{(x,\xi)\in\mathbb R^2:s\le\pi(x^2+\xi^2)\le s+L\},\qquad
 T_{s,L}=V_{h_1}^{*}\mathbf1_{E_{s,L}}V_{h_1},
\]
where \(h_1(t)=2\sqrt\pi\,t\,2^{1/4}e^{-\pi t^2}\) is normalized, and the short-time Fourier transform has convention
\(V_gf(x,\xi)=\int f(t)\overline{g(t-x)}e^{-2\pi i\xi t}\,dt\).
Set \(R=s+L/2\). In the Hermite basis, \(T_{s,L}h_n=\lambda_n(s,L)h_n\), with
\[
 \lambda_n(s,L)=\int_s^{s+L} e^{-u}\frac{u^{n-1}(u-n)^2}{n!}\,du
 \quad(n\in\mathbb Z_{\ge0}),
\]
where the integrand at \(n=0\) is \(ue^{-u}\). Define \(M_-(s,L)=\max_{0\le n<R}\lambda_n(s,L)\) and \(M_+(s,L)=\max_{n>R}\lambda_n(s,L)\). As \(s\to\infty\) with \(L\) fixed,
\[
 M_-(s,L)=\frac{2L}{e\sqrt{2\pi R}}\left(1+\frac{\sqrt2}{6\sqrt R}+O_L(R^{-1})\right),\qquad
 M_+(s,L)=\frac{2L}{e\sqrt{2\pi R}}\left(1-\frac{\sqrt2}{6\sqrt R}+O_L(R^{-1})\right).
\]
In particular,
\[
 \boxed{M_-(s,L)-M_+(s,L)=\frac{2L}{3e\sqrt\pi\,R}+O_L(R^{-3/2})>0}
\]
for all sufficiently large \(s\). Every globally maximizing Hermite index obeys \(n=R-\sqrt{2R}+O_L(1)\). The discrete eigenvalue sequence has a second, suboptimal local maximum near \(R+\sqrt{2R}\). Thus its two leading spectral shoulders are *not* asymptotically tied at the first nonvanishing correction. The norm is \(M_-\) for sufficiently large \(s\), and relative to the analogous Gaussian-window annulus of the same area its norm ratio tends to \(2/e\).

## Assumptions and scope
The area \(L>0\) is fixed independently of \(s\). All asymptotic constants may depend on \(L\), and \(s\) must tend to infinity. The operator acts on the full complex Hilbert space \(L^2(\mathbb R)\), not a finite Hermite truncation. Local maximum of a discrete eigenvalue sequence means \(\lambda_n\ge\lambda_{n-1}\) and \(\lambda_n\ge\lambda_{n+1}\). No assertion of a unique discrete maximizing index is made; integer rounding can produce ties.

## Proof
**Hermite diagonalization and normalization.** Rotational invariance of the annular mask diagonalizes the localization operator in the orthonormal Hermite basis. The standard first-Hermite STFT/Laguerre overlap identity gives
\[
 |V_{h_1}h_n(x,\xi)|^2=e^{-u}\frac{u^{n-1}(u-n)^2}{n!},\qquad u=\pi(x^2+\xi^2).
\]
Integration in polar area coordinates proves the eigenvalue formula. With \(X\sim\operatorname{Poisson}(u)\), its radial density is \(p_n(u)=\Pr(X=n)(u-n)^2/u\), including \(n=0\). The Poisson variance identity gives \(\sum_{n\ge0}p_n(u)=1\) and thus \(\sum_n\lambda_n(s,L)=L\); this also establishes compactness and existence of spectral maxima.

**A two-term local estimate.** Write \(n=R+x\sqrt R\), where \(n\) is an integer and \(x\) lies in any fixed bounded interval. Stirling's formula with a remainder uniform on that interval yields
\[
 e^{-R}\frac{R^n}{n!}=\frac{e^{-x^2/2}}{\sqrt{2\pi R}}
 \left[1+\frac{x^3-3x}{6\sqrt R}+O_B(R^{-1})\right].
\]
For the central radial density, \(p_n(R)=\Pr(\operatorname{Poisson}(R)=n)x^2\). For \(|t|\le L/2\), direct differentiation of the smooth expression \(p_n(R+t)\) shows \(\sup_{|t|\le L/2}|\partial_u^2p_n(R+t)|=O_{B,L}(R^{-3/2})\), including the case where \(R+t=n\). Symmetric integration cancels the first derivative, so
\[
 \lambda_n(s,L)=Lp_n(R)+O_{B,L}(R^{-3/2})
 =\frac{L}{\sqrt{2\pi R}}\left[f(x)+R^{-1/2}g(x)+O_{B,L}(R^{-1})\right],
\]
where \(f(x)=x^2e^{-x^2/2}\) and \(g(x)=f(x)(x^3-3x)/6\). Differentiating the gamma-function interpolation in real \(n\) and applying differentiable Stirling remainders also gives the corresponding uniform \(C^1\) expansion near the two peaks.

**No remote maximizing indices.** Standard Stirling/Chernoff estimates applied to \(p_n(u)\) imply that, for any \(\varepsilon>0\), a sufficiently large constant \(B\) makes
\(\sup_{|n-R|\ge B\sqrt R}\sqrt R\lambda_n(s,L)/L<\varepsilon\) uniformly for all sufficiently large \(R\). To see this directly, in \(|n-u|\le u/2\) use the Poisson entropy exponent \(n\log(n/u)-n+u\ge c(n-u)^2/u\), plus the polynomial factor \((u-n)^2/u\); outside that range the entropy gives exponentially decaying tails. The leading function \(f\) has exactly two global maxima, at \(x=-\sqrt2\) and \(x=+\sqrt2\), both of value \(2/e\); its other stationary point \(x=0\) is a strict minimum. Therefore every one-sided maximizing index approaches the respective peak in scaled coordinates.

**The asymmetric selection.** At the two peaks,
\[
 g(-\sqrt2)=\frac{2}{e}\frac{\sqrt2}{6},\qquad
 g(+\sqrt2)=-\frac{2}{e}\frac{\sqrt2}{6},\qquad
 f''(\pm\sqrt2)=-\frac4e<0.
\]
For any smooth \(f,g\) with a strict nondegenerate maximum at \(x_0\), maximizing \(f(x)+R^{-1/2}g(x)+O(R^{-1})\) over an \(R^{-1/2}\)-spaced grid yields \(f(x_0)+R^{-1/2}g(x_0)+O(R^{-1})\): the upper bound follows by the negative quadratic curvature and the Lipschitz bound on \(g\), while the lower bound uses the nearest grid point to \(x_0\). Apply this to each peak to obtain the two displayed one-sided asymptotics. Subtracting gives the positive gap \(2L/(3e\sqrt\pi\,R)+O_L(R^{-3/2})\). The same quadratic estimate localizes any global maximizing index within \(O_L(R^{-1/2})\) in the scaled \(x\)-coordinate, hence within \(O_L(1)\) in its Hermite index, of \(R-\sqrt{2R}\).

**The surviving secondary shoulder.** Fix \(0<\delta<\sqrt2/4\). The leading value of \(f\) at the two endpoints of \([\sqrt2-\delta,\sqrt2+\delta]\) is strictly below its value at \(\sqrt2\). Consequently the maximum of the discrete eigenvalues whose scaled indices lie in this interval occurs strictly in the interior for all sufficiently large \(s\), and is a discrete local maximum. It is inferior to the lower-index shoulder by the positive gap. For the Gaussian window, \(\widetilde\lambda_n=\int_s^{s+L}\Pr(\operatorname{Poisson}(u)=n)du\) and the local central limit theorem gives \(\max_n\widetilde\lambda_n=L/\sqrt{2\pi R}(1+o(1))\). Dividing yields the limiting norm ratio \(2/e\). This completes the proof.

## Verification
The accompanying `check.py` evaluates the radial integral by composite Simpson quadrature using logarithmic factorials, compares two spectral shoulders for several fixed widths and large inner radii, and tests the normalization \(\sum_n p_n(u)=1\). It prints the dimensionless gap divided by its predicted leading coefficient. The code is an independent numerical sanity check of the algebraic normalization and asymptotic signs; the infinite-dimensional limit is proved above rather than inferred from finite tests.

## Relationship to prior work
Keller and Luef (arXiv:1905.07741, first public 2019-05-19; 2021 journal version) give the polyanalytic/Hermite localization framework and Hermite–Laguerre overlaps, not this fixed-area distant-annulus norm and its signed correction. Knutsen (2020), Section 3.1, treats a unit-area annulus with a **Gaussian** window: it has a single central Poisson peak and a different norm coefficient, so its conclusion does not imply two first-Hermite shoulders. Abreu (2022) concerns critical points of random Gaussian spectrograms and explains their connection to first higher Landau levels, rather than deterministic annular spectral maxima. The \(\sqrt R\)-wide first-Hermite annulus regime produces a symmetric leading pair of possible shoulders but does not by itself select the lower branch for the *fixed-area* regime or determine the order-\(R^{-1}\) gap. No claim is made that a failed literature search proves priority.

## Limitations
Only the first excited Hermite window and fixed strictly positive annular area are addressed. The onset radius above which the lower branch wins is not explicit. Adjacent Hermite indices can be nearly tied; uniqueness of the top eigenfunction is not asserted. Higher Hermite windows, growing widths, and exact finite-radius spectral collision sets are not classified. Priority against an unidentified earlier thin-annulus asymptotic remains unverified by an independent audit.

## References
1. J. Keller and F. Luef, *Polyanalytic Toeplitz operators: isomorphisms, symbolic calculus and approximation of Weyl operators*, arXiv:1905.07741 (2019), J. Fourier Anal. Appl. 27, 47 (2021), https://arxiv.org/abs/1905.07741 and https://doi.org/10.1007/s00041-021-09843-0.
2. H. Knutsen, *Daubechies' Time–Frequency Localization Operator on Cantor Type Sets I*, J. Fourier Anal. Appl. 26, 47 (2020), especially Section 3.1, https://doi.org/10.1007/s00041-020-09751-9.
3. L. D. Abreu, *Local Maxima of White Noise Spectrograms and Gaussian Entire Functions*, J. Fourier Anal. Appl. 28, 88 (2022), https://doi.org/10.1007/s00041-022-09979-7.

# Quantized singular spectra and sharp stability of two-tone Paley–Wiener multipliers

## Finding

For every pair of positive bandwidths \(\sigma,\eta>0\) and every amplitude \(r>0\), let \(B_\sigma^2\) be the Hilbert Paley–Wiener space with Fourier support in \([-\sigma,\sigma]\), and consider the bounded multiplication map
\[
T_{\sigma,\eta,r}:B_\sigma^2\longrightarrow B_{\sigma+\eta}^2,
\qquad (T_{\sigma,\eta,r}f)(z)=\bigl(e^{i\eta z}+r e^{-i\eta z}\bigr)f(z).
\]
Put \(q=\sigma/\eta\), \(k=\lfloor q\rfloor\), \(\vartheta=q-k\), \(m=\lceil q\rceil\), and
\[
\mathcal N(q)=
\begin{cases}
\{k\},&\vartheta=0,\\
\{k,k+1\}\setminus\{0\},&0<\vartheta<1.
\end{cases}
\]
The **complete spectrum of the positive Gram operator** is exactly
\[
\operatorname{spec}(T_{\sigma,\eta,r}^*T_{\sigma,\eta,r})=
\bigcup_{n\in\mathcal N(q)}
\left\{1+r^2+2r\cos\frac{j\pi}{n+1}:1\le j\le n\right\}.
\]
Every listed number is an eigenvalue of countably infinite multiplicity and belongs to the essential spectrum; there is no other spectrum. Different listed fractions give distinct eigenvalues. Thus the spectrum has \(m\) distinct points for integral \(q\), and \(2m-1\) for nonintegral \(q\). Both sharp bounds below are **attained by nonzero functions**, and each extremizer space is infinite dimensional:
\[
\boxed{\quad
\biggl(1+r^2-2r\cos\frac{\pi}{m+1}\biggr)\|f\|_2^2
\le\|T_{\sigma,\eta,r}f\|_2^2
\le\biggl(1+r^2+2r\cos\frac{\pi}{m+1}\biggr)\|f\|_2^2.
\quad}
\]
In particular the multiplication map has a closed range and a bounded inverse on its range, although its equal-amplitude symbol \(2\cos(\eta x)\) vanishes infinitely often on the real line. In that equal-amplitude case the exact sharp inequality is
\[
4\sin^2\frac{\pi}{2(m+1)}\,\|f\|_2^2
\le\|2\cos(\eta\cdot)f\|_2^2
\le4\cos^2\frac{\pi}{2(m+1)}\,\|f\|_2^2,
\]
with exact condition number \(\cot(\pi/[2(m+1)])\). As \(\eta\downarrow0\) with \(\sigma\) fixed, its least gain is asymptotic to \(\pi\eta/\sigma\), while its largest gain tends to \(2\). For each positive integer \(h\), the two sharp gains jump as \(\eta\) increases through \(\sigma/h\) from below: at equality the longest fibers have length \(h\), whereas immediately below the threshold they have length \(h+1\).

## Assumptions and scope

The Fourier transform is normalized unitarily: \(\widehat f(\xi)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-ix\xi}\,dx\), extended from dense subspaces to \(L^2(\mathbb R)\). The space \(B_\sigma^2\) comprises exactly those \(L^2\) functions whose transforms vanish almost everywhere outside \([-\sigma,\sigma]\), with the inherited \(L^2\)-norm and canonical entire representatives. The codomain has bandwidth \(\sigma+\eta\); no projection is applied to the output. The amplitude \(r\) is strictly positive and real. A complex relative phase is reducible by translation and unitary gauges, but is not needed for the statement. The operator \(T^*T\) acts on the input space \(B_\sigma^2\), not on the output space.

## Proof

**1. Exact Gram identity.** Fourier transformation identifies the input with \(L^2(I)\) for \(I=[-\sigma,\sigma]\). The output spectrum is \(\widehat{Tf}(\xi)=g(\xi-\eta)+r g(\xi+\eta)\), where \(g=\widehat f\) is extended by zero. Write \(h=2\eta\), and let \(S_h\) be the truncated right translation on \(L^2(I)\): \((S_hg)(\xi)=g(\xi-h)\) when both arguments belong to \(I\), and zero otherwise. Plancherel and expansion of the square give the exact operator identity
\[
\widehat{T^*T}=(1+r^2)I+r(S_h+S_h^*).
\]
No asymptotic approximation or finite cutoff enters this identity.

**2. Unitary fiber decomposition.** Write \(L=2\sigma\), so that \(L/h=q=k+\vartheta\). Modulo endpoint null sets, each \(\xi\in I\) can be written uniquely as \(\xi=-\sigma+t+jh\), with \(0\le t<h\) and a nonnegative integer \(j\). The unitary reindexing
\[
L^2(I)\simeq\int_{[0,h)}^{\oplus}\mathbb C^{n(t)}\,dt
\]
uses the number \(n(t)\) of points in \(I\) in the residue fiber, omitting zero-dimensional fibers. If \(\vartheta=0\), this number equals \(k\) almost everywhere. If \(0<\vartheta<1\), it equals \(k+1\) for \(0<t<\vartheta h\), and \(k\) for \(\vartheta h<t<h\). Every positive length that occurs therefore occurs on a set of positive measure.

**3. Finite path spectra.** On each nonempty fiber of length \(n\), the truncated shift is the nilpotent forward shift on \(\mathbb C^n\), and its sum with its adjoint is the adjacency matrix of the path on \(n\) vertices. For \(1\le j\le n\), the vector whose \(\ell\)-th component is
\[
\sqrt{\frac{2}{n+1}}\sin\frac{\ell j\pi}{n+1},\qquad1\le\ell\le n,
\]
is an eigenvector with eigenvalue \(2\cos(j\pi/(n+1))\); the boundary identities use the zero values at \(\ell=0,n+1\). These vectors form an orthonormal basis, giving all spectral values. Because each positive-dimensional fiber size occupies positive Lebesgue measure, multiplication by a fixed finite matrix on that fiber interval has an infinite-dimensional eigenspace for each matrix eigenvalue. For consecutive lengths \(n,n+1\), equality between two cosine eigenvalues would require \(j/(n+1)=a/(n+2)\), impossible with allowed positive interior indices because consecutive denominators are coprime. This proves the complete finite pure-point and essential spectra and the distinct-point count.

**4. Sharp gains and transition.** The cosine is strictly decreasing on \((0,\pi)\); the outermost eigenvalues occur in the longest length \(m=\lceil q\rceil\), and the longest-fiber set has positive measure even when \(q\) is integral. Choosing a measurable scalar multiple of the corresponding path eigenvector on a positive-measure fiber interval proves equality attainment (not merely approximation). The smallest value is strictly positive, since \(\cos(\pi/(m+1))<1\). At \(r=1\), the half-angle identities yield the stated sine/cosine gains. Since \(m\sim\sigma/\eta\) as \(\eta\downarrow0\), the lower gain is \(2\sin(\pi/[2(m+1)])\sim\pi\eta/\sigma\). When \(\eta=\sigma/h\), the ratio \(q\) is the integer \(h\). Approaching that point from smaller \(\eta\) makes \(q>h\) and \(m=h+1\), giving the asserted one-sided jump. All assertions follow.

## Verification

The standalone standard-library script `two_tone_check.py` checks exact rational Gram-matrix identities \(B^*B=(1+r^2)I+rA_n\) for path sizes up to 32 and three positive rational amplitudes, checks the sine-vector spectral formula, and independently enumerates residue fiber sizes at 48 bandwidth pairs. It prints `TWO_TONE_PALEY_WIENER_CHECK_OK 40704` when these diagnostics pass. The written Fourier identity, fiber unitary, and eigenvector proof—not the finite checks—establish the assertions for arbitrary real parameters and infinite-dimensional spaces.

## Relationship to prior work

Álvarez and Severiano, arXiv:2508.19975 (first publicly posted 27 August 2025), classify spectra and dynamical properties of **unweighted composition self-operators** of Paley–Wiener Hilbert spaces; their spectral statements do not give the Gram spectrum of a two-tone multiplication map between different bandwidths. Mukherjee, Jafari and McInroy, arXiv:1006.2793 (2010), describe bandwidth and Fourier support for weighted composition operators, but no sharp lower/upper gain or quantized Gram spectrum of this family. Hai, Huy and Tien, arXiv:2611.21261 (first posted 16 November 2026), provide general boundedness/compactness classifications and norm comparisons for multipliers; their Theorem 3.15 gives bounds up to unspecified constants, not this exact spectrum or its sharp inverse bound. Standard Fourier shift identities and path eigenvectors are used as tools, not asserted to be new.

## Limitations

The classification is for the Hilbert exponent \(2\), a contiguous symmetric input frequency interval, a precisely two-term exponential weight with nonzero frequency separation, and codomain bandwidth at least the required \(\sigma+\eta\). It does not treat variable frequency supports, more than two tones, non-Hilbert exponents, or the limit \(\eta=0\), at which the finite-fiber decomposition changes. The operator is not compact; its finitely many positive singular levels all have infinite multiplicity. The proof is mathematical rather than externally certified; identifying no matching theorem in the checked literature is not a universal novelty guarantee.

## References

1. C. F. Álvarez and O. R. Severiano, *Expansivity and shadowing for composition operators on Paley–Wiener spaces*, arXiv:2508.19975, first version dated 27 August 2025, https://arxiv.org/abs/2508.19975.
2. S. Mukherjee, F. Jafari and J. E. McInroy, *On the range of composition operators on spaces of entire functions*, arXiv:1006.2793, 2010, https://arxiv.org/abs/1006.2793.
3. P. V. Hai, V. N. Huy and P. T. Tien, *Analytic tools and weighted composition operators on Paley–Wiener spaces*, arXiv:2611.21261, first version dated 16 November 2026, https://arxiv.org/abs/2611.21261.

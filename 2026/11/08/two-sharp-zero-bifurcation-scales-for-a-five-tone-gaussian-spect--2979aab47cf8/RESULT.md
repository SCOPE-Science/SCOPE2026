# Two sharp zero-bifurcation scales for a five-tone Gaussian spectrogram

## Finding
Let \(\sigma>0\), \(\Omega>0\), and take the equal-amplitude five-frequency signal
\[
f(s)=\sum_{k=-2}^{2}e^{ik\Omega s},\qquad
h_\sigma(s)=e^{-s^2/(2\sigma^2)}.
\]
Define its Gaussian short-time Fourier transform by the absolutely convergent integral
\[
V(t,\xi)=\int_{\mathbb R} f(s)h_\sigma(s-t)e^{-i\xi s}\,ds.
\]
Set \(r=e^{\sigma^2\Omega^2}>1\) and view time modulo the period \(2\pi/\Omega\). **There are exactly four zeros of \(V\) per time-frequency cylinder, counted with multiplicity.** They have the following complete classification, with **precisely two transition values**:
\[
\boxed{r_1=2,\qquad r_2=1+\sqrt5.}
\]
Equivalently, the sharp critical dimensionless frequency gaps are \(\sigma\Omega=\sqrt{\log2}\) and \(\sigma\Omega=\sqrt{\log(1+\sqrt5)}\).

Write
\[
\Delta(r)=(r-2)(r^2-2r-4),\qquad
 y_\pm(r)=\frac{-r^{3/2}\pm\sqrt{\Delta(r)}}{2},\qquad
 z=\sigma^2\Omega\xi+i\Omega t.
\]
The zeros are exactly the solutions \(2\cosh z=y_\pm(r)\) (including multiplicities), and their regimes are:

- **Central-frequency regime**, \(1<r<2\): both \(y_\pm\) are distinct and belong to \((-2,2)\). With \(\theta_\pm=\arccos(y_\pm/2)\), all four zeros are at \(\xi=0\) and \(\Omega t=\pm\theta_\pm\pmod{2\pi}\).
- **First collision**, \(r=2\): precisely two double zeros occur, at \(\xi=0\) and \(\Omega t=\pm3\pi/4\pmod{2\pi}\).
- **Off-axis regime**, \(2<r<1+\sqrt5\): the \(y_\pm\) are nonreal conjugates. Choose \(z_*=x+i\theta\) with \(x>0\), \(0<\theta<\pi\), and \(2\cosh z_*=y_+\) with positive imaginary part. The four simple zeros are \(z\in\{\pm z_*,\pm\overline{z_*}\}\pmod{2\pi i}\), so both time and frequency coordinates split.
- **Second collision**, \(r=1+\sqrt5\): precisely two double zeros occur at \(\Omega t=\pi\pmod{2\pi}\) and \(\sigma^2\Omega\xi=\pm\operatorname{arcosh}(r^{3/2}/4)\).
- **Alternating-time regime**, \(r>1+\sqrt5\): both \(y_\pm<-2\) are distinct. All four simple zeros have \(\Omega t=\pi\pmod{2\pi}\), with \(\sigma^2\Omega\xi=\pm\operatorname{arcosh}(-y_\pm/2)\).

Here double means multiplicity two as a zero of the holomorphic factor in the displayed complex coordinate, not merely a zero of the squared spectrogram.

## Assumptions and scope
All five coefficients are exactly one; both \(\sigma\) and \(\Omega\) range over all positive reals. Although \(f\) is bounded rather than square-integrable on \(\mathbb R\), the Gaussian-weighted STFT integral converges absolutely. Frequencies \(\xi\) range over all real numbers; time \(t\) ranges over one full period modulo \(2\pi/\Omega\). No finite sampling or discretization is assumed. The window is the *unnormalized* real Gaussian specified above; multiplying it by any positive constant leaves the zero set unchanged.

## Proof
Put \(\alpha=\sigma^2\Omega^2/2\), so \(r=e^{2\alpha}\). Integrating each exponential against the translated Gaussian gives, without approximation,
\[
 V(t,\xi)=\sqrt{2\pi}\sigma\,e^{-i\xi t}e^{-\sigma^2\xi^2/2}
 \left(1+2e^{-\alpha}\cosh z+2e^{-4\alpha}\cosh(2z)\right),
 \quad z=\sigma^2\Omega\xi+i\Omega t.
\]
The prefactor never vanishes. With \(y=2\cosh z\) and \(2\cosh(2z)=y^2-2\), multiplying the remaining factor by \(e^{4\alpha}\) yields
\[
 Q_r(y)=y^2+r^{3/2}y+r^2-2.
\]
Its discriminant is
\[
(r^{3/2})^2-4(r^2-2)=r^3-4r^2+8=(r-2)(r^2-2r-4).
\]
On \(r>1\), the only zeros of this discriminant are \(2\) and \(1+\sqrt5\); its sign is positive, negative, positive on the three intervening open intervals.

The map \(z\mapsto 2\cosh z\) has critical values only \(\pm2\). Neither can be a root of \(Q_r\):
\[
 Q_r(2)=r^2+2r^{3/2}+2>0,
 \quad Q_r(-2)=u^4-2u^3+2,\quad u=\sqrt r\ge1.
\]
The last polynomial has derivative \(2u^2(2u-3)\), and its minimum on \([1,\infty)\) is \(5/16>0\), attained at \(u=3/2\). Thus \(2\cosh z\) is locally invertible at *every* zero, and all zero multiplicities arise solely from repeated roots of \(Q_r\).

At \(r=1\), the roots are \((-1\pm\sqrt5)/2\), both in \((-2,2)\). They cannot cross \(\pm2\), so for \(1<r<2\) they remain there. Hence each gives precisely two imaginary \(z\)-values per period, establishing the first regime. At \(r=2\), \(Q_r\) has the repeated root \(-\sqrt2\), whose preimages are \(\pm3\pi i/4\), establishing the first pair of double zeros.

For \(2<r<1+\sqrt5\), the two roots of \(Q_r\) are nonreal conjugates. Since \(\cosh(x+i\theta)=\cosh x\cos\theta+i\sinh x\sin\theta\), each nonreal root has two preimages modulo \(2\pi i\), producing exactly the four displayed off-axis simple zeros. At \(r=1+\sqrt5\), the repeated value is \(-r^{3/2}/2<-2\), because \(r>3\) implies \(r^{3/2}>4\). Its preimages are \(\pm\operatorname{arcosh}(r^{3/2}/4)+\pi i\), each double. For larger \(r\), continuity and the impossibility of crossing \(-2\) imply both distinct real roots remain below \(-2\), establishing the last regime.

Finally, setting \(w=e^z\ne0\), the same nonvanishing factor becomes, after multiplication by \(w^2\), the reciprocal quartic
\[
 e^{-4\alpha}(w^4+1)+e^{-\alpha}(w^3+w)+w^2.
\]
Its leading and constant coefficients are nonzero. Thus it has exactly four roots in \(\mathbb C^\times\), counted with multiplicity, each representing exactly one \(z\) modulo \(2\pi i\). This proves completeness and the zero-count assertion.

## Verification
The standalone `CHECK.py` uses only Python's standard library. Run `python3 CHECK.py` in the same folder. It checks the exact discriminant factorization with integer polynomial multiplication, the exact \(5/16\) boundary value with rational arithmetic, the two predicted double roots and nonzero second derivatives, the quartic identity, every predicted zero in sample cases of each regime, and independent numerical quadrature of the original STFT integral against its closed form. It prints `ALL_FIVE_TONE_CHECKS_PASSED` when the checks succeed. The proof above, not finite samples or floating-point tolerance, establishes the universal statement.

## Relationship to prior work
Chand, Nolen and Wu (arXiv:2601.10910, first public January 15, 2026) study Gaussian STFT spectral interference with a two-component harmonic model and a sharp resolution transition; the present result concerns the exact zero geometry and two collision thresholds of the **equal-amplitude five-component** model. The full text of that 76-page source was not available for comparison, so possible unindexed appendices or more general formulas remain an originality risk. Abreu's open-access study of Gaussian spectrogram zeros treats random entire-function models and critical-point statistics, not this deterministic five-tone phase diagram. The general Gaussian STFT/Bargmann analyticity and phase singularity principles are established prior art; the polynomial reduction is standard in spirit. The specific two algebraic thresholds, five-regime classification and double-zero locations are the assertions examined here.

## Limitations
The model uses exactly five equally spaced, equal-phase, equal-amplitude harmonics and a Gaussian window; unequal amplitudes or frequency offsets may alter the collision structure. The statement classifies *zeros* of the complete continuous STFT, not ridges, local maxima, noisy estimators, synchrosqueezing reconstruction quality or perturbation stability. The non-square-integrability of the pure-tone signal is accommodated only by the absolutely convergent windowed transform. The claim has received self-review only; no independent audit or publication-priority certification was performed.

## References
1. S. Chand, J. Nolen, H.-T. Wu, *On spectral interference of the short-time Fourier transform and its nonlinear variations*, arXiv:2601.10910 (first posted 2026-01-15), https://arxiv.org/abs/2601.10910; subsequently *Applied and Computational Harmonic Analysis* 85 (2026), 101889, doi:10.1016/j.acha.2026.101889.
2. L. D. Abreu, *Local Maxima of White Noise Spectrograms and Gaussian Entire Functions*, *Journal of Fourier Analysis and Applications* 28 (2022), 88, doi:10.1007/s00041-022-09979-7, https://link.springer.com/article/10.1007/s00041-022-09979-7.
3. P. Balazs, D. Bayer, F. Jaillet, P. Søndergaard, *The pole behavior of the phase derivative of the short-time Fourier transform*, *Applied and Computational Harmonic Analysis* 40 (2016), 610–621, https://arxiv.org/abs/1103.0409.
4. L. A. Escudero, G. Koliander, J. L. Romero, *Zeros of the Spectrogram of Colored Noise*, arXiv:2609.18689 (2026-09-16), https://arxiv.org/abs/2609.18689.

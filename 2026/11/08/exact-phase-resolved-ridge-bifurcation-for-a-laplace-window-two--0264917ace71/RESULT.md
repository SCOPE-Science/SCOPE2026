# Exact phase-resolved ridge bifurcation for a Laplace-window two-tone spectrogram

## Finding
For any \(a>0\), \(\omega>0\), and \(x\in\mathbb R\), take the even Laplace window \(g_a(s)=e^{-a|s|}\), the equal-amplitude two-tone signal \(f(s)=e^{i\omega s}+e^{-i\omega s}\), and its angular-frequency short-time Fourier transform
\[
V_{g_a}f(x,\xi)=\int_{\mathbb R}f(s)g_a(s-x)e^{-i\xi s}\,ds.
\]
The frequency profile \(\xi\mapsto |V_{g_a}f(x,\xi)|^2\) has **either one frequency maximum at the midpoint** or **exactly two symmetric frequency maxima**; it can never have three maxima. Put
\[
q=(\omega/a)^2,\qquad c=\cos(2\omega x),\qquad q_*(c)=\frac{1+c}{5+c}.
\]
If \(0<q<q_*(c)\), the midpoint \(\xi=0\) is the unique strict global maximum. If \(q=q_*(c)\), the midpoint remains the unique global maximum but is quartically flat. If \(q>q_*(c)\), the midpoint is a strict local minimum and the two unique global maxima occur at \(\xi=\pm a\sqrt{t_*}\), where \(t_*>0\) is the unique positive root of the explicit polynomial in the proof below. The borderline \(c=-1\) has \(q_*(-1)=0\), so all positive gaps give two maxima there.

For \(0<q<1/3\), the fraction of any full beat period \(\pi/\omega\) at which the frequency profile has two distinct maxima is exactly
\[
\mathcal D(q)=1-\frac1\pi\arccos\!\left(\frac{5q-1}{1-q}\right).
\]
For \(q\ge1/3\), this fraction equals \(1\) (at equality the aligned phase is a single quartically flat exceptional instant). As \(\omega/a\downarrow0\),
\[
\mathcal D((\omega/a)^2)\sim\frac{2\sqrt2}{\pi}\frac\omega a.
\]
Thus \(\omega/a=1/\sqrt3\) is the exact critical separation above which phase-dependent single-ridge windows disappear, up to the isolated equality phase.

## Assumptions and scope
All frequencies are *angular* frequencies (there is no \(2\pi\) in the Fourier exponent). The two tones have equal positive amplitude, with zero relative phase at \(s=0\); an arbitrary relative phase merely shifts \(x\). The window is exactly \(e^{-a|s|}\) with \(a>0\). The signal is bounded rather than square integrable, but the STFT integral is absolutely convergent for every \((x,\xi)\). A ridge is a local maximum of the **squared magnitude** along the entire real frequency axis at fixed time. The statement is exact, noise-free, and concerns the linear STFT without reassignment.

## Proof
The elementary transform \(\int_{\mathbb R}e^{-a|u|}e^{-i\eta u}\,du=2a/(a^2+\eta^2)\) gives
\[
V_{g_a}f(x,\xi)=2a e^{-i\xi x}\left[\frac{e^{i\omega x}}{a^2+(\xi-\omega)^2}+\frac{e^{-i\omega x}}{a^2+(\xi+\omega)^2}\right].
\]
Put \(y=\xi/a\), \(t=y^2\ge0\), \(q=(\omega/a)^2>0\), \(c=\cos(2\omega x)\), and
\[
U=t+1+q,\quad D=U^2-4qt=\bigl(1+(y-\sqrt q)^2\bigr)\bigl(1+(y+\sqrt q)^2\bigr)>0,
\]
\[
N=(1+c)U^2+4(1-c)qt.
\]
The complete frequency profile is the even rational function
\[
P(y):=|V_{g_a}f(x,ay)|^2=\frac8{a^2}\frac{N(t)}{D(t)^2}.
\]
In particular \(P(y)\to0\) as \(|y|\to\infty\). Differentiation in \(t\) shows that the sign of \(dP/dt\) is the sign of \(H(t)=N'(t)D(t)-2N(t)D'(t)\) because \(D>0\). Direct expansion gives
\[
\begin{aligned}
H(t)={}&-2(1+c)t^3+6\bigl((c-3)q-(c+1)\bigr)t^2\\
&-2\bigl(3cq^2-2cq+3c-5q^2+6q+3\bigr)t\\
&+2(1+q)^2\bigl((5+c)q-(1+c)\bigr).
\end{aligned}
\]
The cubic coefficient is nonpositive, and the quadratic coefficient is strictly negative for every \(q>0\), \(-1\le c\le1\). Set \(B=3cq^2-2cq+3c-5q^2+6q+3\). For \(0<q\le q_*(c)\le1/3\), the coefficient of \(c\) in \(B\) is \(3q^2-2q+3>0\), so
\[
B\ge B|_{c=-1}=8q(1-q)>0.
\]
In this range \(H(0)\le0\), and every nonzero coefficient of \(H\) is nonpositive while the \(t^2\) coefficient is strictly negative. Thus \(H(t)<0\) for all \(t>0\), proving the unique central maximum for \(q\le q_*(c)\).

For \(q>q_*(c)\), the constant term of \(H\) is strictly positive, the quadratic coefficient is strictly negative, and the leading coefficient is nonpositive. Regardless of the sign of the linear coefficient, the nonzero coefficient sequence in descending powers has exactly one sign change. Descartes' rule of signs therefore gives *at most one positive root counted with multiplicity*. Since \(H(0)>0\) and \(H(t)\to-\infty\) as \(t\to\infty\) (the negative quadratic term handles \(c=-1\)), there is exactly one simple positive root \(t_*\). The derivative changes sign from positive to negative at that root. Under \(t=y^2\) this gives one central minimum and precisely two symmetric strict global maxima. No other stationary points or hidden sidelobes are possible.

At the transition \(q=q_*(c)>0\), one has \(c>-1\), and
\[
B(q_*(c),c)=\frac{4(1+c)(c^2+6c+25)}{(5+c)^2}>0.
\]
Hence \(H(0)=0\), \(H'(0)=-2B<0\), so \(P(y)=P(0)-C y^4+O(y^6)\) for a constant \(C>0\). For any fixed \(-1<c\le1\), the new pair of maxima is born continuously with
\[
t_* = \frac{(c+3)^2(c+5)}{(c+1)(c^2+6c+25)}\,(q-q_*(c)) + O_c((q-q_*(c))^2)\quad(q\downarrow q_*(c)\text{ from above}).
\]
Indeed this is the implicit-function expansion \(t_*=-H(0)/H'(0)+O((q-q_*)^2)\), using the displayed exact value of \(B\).

For every \(0<q<1/3\), the strict two-ridge condition rearranges to \(\cos(2\omega x)<(5q-1)/(1-q)\). Uniform phase \(2\omega x\in[0,2\pi)\) yields the stated fraction \(\mathcal D(q)\). The small-gap expansion follows from \((5q-1)/(1-q)=-1+4q+O(q^2)\) and the square-root expansion of \(\arccos\) near \(-1\). For \(q>1/3\), \(q>q_*(c)\) for every phase. At \(q=1/3\), only \(c=1\) is critical, a measure-zero set of times.

For reference, in the coherent aligned case \(c=1\), when \(q>1/3\),
\[
t_*=2\sqrt{q(1+q)}-(1+q).
\]
In the destructive anti-aligned case \(c=-1\), at every \(q>0\),
\[
t_*=\frac{q-1+2\sqrt{q^2+q+1}}3.
\]
Both are positive exactly on their claimed domains and agree with the unique-root characterization.

## Verification
The self-contained `CHECK.py` symbolically reconstructs the complete rational STFT intensity and the derivative polynomial, verifies the transition-slope and local-bifurcation identities, compares the original absolutely convergent STFT integral by numerical quadrature at independently chosen parameters, and checks positive roots, maxima, explicit aligned/anti-aligned peak locations and beat-phase fractions on extensive sampled parameters. Run with `python CHECK.py` after installing the packages listed in `requirements.txt`.

Numerical tests are *not* substituted for Descartes' rule, positivity of the coefficients, or the analytical arguments establishing the universal quantifiers. The checker prints `LAPLACE_STFT_CHECKS_PASSED 6051` with the listed dependency families.

## Relationship to prior work
Chand, Nolen and Wu (arXiv:2601.10910, initially submitted January 15, 2026) investigate two-tone spectral interference and ridge bifurcations for the *Gaussian* STFT window, including time-frequency bubbles and reassignment. The present theorem instead gives the complete **non-Gaussian Laplace-window**, phase-resolved global ridge classification, a sharp rational transition curve, explicit peak positions at extreme beat phases, and the exact phase occupancy of the split-ridge regime. These statements do not follow by rescaling the Gaussian Fourier multiplier: its spectral profile is exponential, whereas the Laplace window has a rational Lorentzian spectral profile.

Iatsenko, McClintock and Stefanovska (2016) discuss methods of extracting time-frequency ridges, rather than this exact Laplace-window bifurcation. General facts about overlapping Lorentzian lines explain the limiting aligned/incoherent comparisons but do not by themselves give the phase-dependent two-tone STFT profile or its beat-time duty cycle. Searches of mathematical records for the Laplace/Cauchy-window phase-resolved formula and alias terminology did not identify a published statement with the entire classification. Failure to find an indexed match does not establish publication priority.

## Limitations
The result does not cover unequal tone amplitudes, chirped signals, generic even windows, noisy ridges or synchrosqueezed/reassigned transforms. The source on Gaussian-window spectral interference was accessible through public abstract and publisher metadata, but its full 76-page preprint could not be inspected through the available routes; an unadvertised general-window result therein is a residual priority risk. There may also be related older calculations in coherent Lorentzian line-shape literature not indexed with STFT terminology. Neither independent review nor publication-priority certification has been performed.

## References
1. Shrikant Chand, James Nolen, Hau-Tieng Wu, *On spectral interference of the short-time Fourier transform and its nonlinear variations*, arXiv:2601.10910 (first submitted January 15, 2026); Applied and Computational Harmonic Analysis **85** (2026), 101889, doi:10.1016/j.acha.2026.101889.
2. D. Iatsenko, P. V. E. McClintock, A. Stefanovska, *Extraction of instantaneous frequencies from ridges in time-frequency representations of signals*, Signal Processing **125** (2016), 290–303, doi:10.1016/j.sigpro.2016.01.024. Author-accepted abstract and record: https://eprints.lancs.ac.uk/id/eprint/78088/.
3. *Spectral line shape*, background account of Lorentzian spectral profiles (consulted 2026): https://en.wikipedia.org/wiki/Spectral_line_shape. This is background terminology, not novelty evidence.

# A tricritical frequency-ridge transition for two coherently chirped tones

## Finding

For the central-frequency slice of the Gaussian-window short-time Fourier transform of two equal-amplitude tones with a **common linear chirp**, the onset of two resolved local spectral maxima changes its bifurcation type at the exact ratio
\[
 r_*=\sqrt{2}-1
\]
of chirp rate to Gaussian window parameter. Below this ratio the side peaks emerge with a square-root law; at the ratio their distance follows a fourth-root law; just above it an interval of central/satellite peak coexistence is bounded by a saddle-node curve with an explicitly determined quadratic leading coefficient.

Define the dimensionless Gaussian intensity profile
\[
H_{r,\varepsilon}(z)=e^{-z^2}\left[\cosh\!\left(2\sqrt{\frac{1+\varepsilon}{1-r^2}}\,z\right)+\cos\!\left(2r\sqrt{\frac{1+\varepsilon}{1-r^2}}\,z\right)\right],
\quad 0\le r<1,\quad\varepsilon>-1.
\]
All extrema below are **local**, near \(z=0\); no statement is made about the global number of ridges over all frequencies.

1. For each fixed \(0\le r<r_*\), at \(\varepsilon=0\) the origin is a strict quartic local maximum. For sufficiently small \(\varepsilon>0\), the origin is a strict local minimum and there is a unique pair of nearby nonzero local maxima with
\[
 z_\pm=\pm\left(-\frac{\varepsilon}{q(r)}\right)^{1/2}(1+o(1)),\qquad q(r)=\frac{-1+6r^2-r^4}{3(1-r^2)^2}<0.
\]
2. At \(r=r_*\) and \(\varepsilon=0\), the origin is a **sixth-order** strict local maximum; for sufficiently small \(\varepsilon>0\), the two nearby local maxima satisfy
\[
 z_\pm=\pm\left(\frac{15\varepsilon}{4}\right)^{1/4}(1+o(1)).
\]
3. For \(r=r_*+\delta\) with sufficiently small \(\delta>0\), there is a smooth saddle-node threshold \(\varepsilon_{\rm fold}(r)<0\) such that every \(\varepsilon_{\rm fold}(r)<\varepsilon<0\) has exactly three local maxima (one central, two outer) and two intervening local minima in a fixed sufficiently small neighborhood of the origin. The threshold has the sharp asymptotic expansion
\[
\varepsilon_{\rm fold}(r_*+\delta)=-\left(\frac52+\frac{5\sqrt2}{3}\right)\delta^2+O(\delta^3).
\]
At the fold, the two positive-frequency critical points coalesce, and their squared dimensionless frequency is
\[
 z_{\rm fold}^{2}=\frac{15}{8}\,\frac{4+2\sqrt2}{3}\,\delta+O(\delta^2).
\]
The negative-frequency fold is its reflection. At \(\varepsilon=0\) and \(\delta>0\), the central point is a degenerate local minimum, while the nonzero maxima have squared frequencies \(z_\pm^2=\frac{15}{4}\frac{4+2\sqrt2}{3}\delta+O(\delta^2)\).

## Assumptions and scope

Let \(a>0\), \(c\in\mathbb R\) with \(|c|<a\), and \(\omega>0\). Use the Gaussian analysis window \(g_a(t)=e^{-\pi a t^2}\) and the bounded, non-square-integrable chirped two-tone signal
\[
f_{c,\omega}(t)=e^{\pi i c t^2}\left(e^{2\pi i\omega t}+e^{-2\pi i\omega t}\right).
\]
Its central STFT is the absolutely convergent integral
\[
V(0,\xi)=\int_{\mathbb R}f_{c,\omega}(t)g_a(t)e^{-2\pi i\xi t}\,dt.
\]
Let \(D=a^2+c^2\), \(u=2\pi a/D\), \(r=|c|/a\), and
\[
\omega_c^2=\frac{aD}{2\pi(a^2-c^2)},\qquad
\varepsilon=\frac{\omega^2}{\omega_c^2}-1,\qquad z=\sqrt{u}\,\xi.
\]
Then the observed intensity is an everywhere-positive constant multiple of \(H_{r,\varepsilon}(z)\); in particular, the signs and orders of extrema agree. The order of limits is as specified: item 1 fixes \(r\), while item 3 sends \(\delta\downarrow0\). These are not uniform claims over all \(r\in[0,1)\) or over the entire frequency axis.

## Proof

The complex Gaussian integral, valid since \(a>0\), yields
\[
V(0,\xi)=\frac{1}{\sqrt{a-ic}}\left[\exp\left(-\frac{\pi(\xi-\omega)^2}{a-ic}\right)+\exp\left(-\frac{\pi(\xi+\omega)^2}{a-ic}\right)\right].
\]
Taking the absolute square and using \(1/(a-ic)=(a+ic)/D\) gives the **exact normalization**
\[
|V(0,\xi)|^2=\frac{2}{\sqrt D}e^{-u(\xi^2+\omega^2)}\left[\cosh\left(\frac{4\pi a\omega}{D}\xi\right)+\cos\left(\frac{4\pi c\omega}{D}\xi\right)\right].
\]
Substitution of the definitions of \(\omega_c,\varepsilon,z\) gives the stated \(H_{r,\varepsilon}\) multiplied by \(2e^{-u\omega^2}/\sqrt D>0\).

The even analytic function has Taylor expansion near \((r,\varepsilon,z)=(r_*,0,0)\)
\[
H_{r,\varepsilon}(z)=2+2\varepsilon z^2+q(r)z^4+v(r)z^6+O\bigl(|\varepsilon|z^4+|\varepsilon|z^6+z^8\bigr),
\]
where the displayed \(q(r)\) is the coefficient at \(\varepsilon=0\) and
\[
v(r)=\frac{4(r^2-4r+1)(r^2+4r+1)}{45(1-r^2)^2}.
\]
Direct substitution and differentiation establish
\[
q(r_*)=0,\quad q'(r_*)=Q:=\frac{4+2\sqrt2}{3}>0,\quad v(r_*)=-\frac8{45}<0.
\]
For each fixed \(r<r_*\), the polynomial \(-1+6r^2-r^4\) is negative, so the origin is a quartic maximum at \(\varepsilon=0\). For \(\varepsilon>0\), the quadratic term makes the origin a minimum. Divide the odd derivative \(\partial_zH\) by \(2z\) and write \(y=z^2\). Its analytic continuation \(G(r,\varepsilon,y)\) satisfies
\[
G(r,\varepsilon,y)=2\varepsilon+2q(r)y+3v(r)y^2+O(|\varepsilon|y+|\varepsilon|y^2+y^3).
\]
For fixed \(r<r_*\), \(\partial_yG(r,0,0)=2q(r)<0\). The analytic implicit-function theorem gives one small positive stationary root \(y=-\varepsilon/q(r)+O(\varepsilon^2)\). Its derivative sign changes from positive to negative, so the two reflected critical points are local maxima. This proves item 1.

At \(r=r_*\), the first nonconstant term at \(\varepsilon=0\) is \(-8z^6/45\), so the origin is a sixth-order maximum. At \(\varepsilon>0\), balancing \(2\varepsilon+3v(r_*)y^2=0\) yields \(y=\sqrt{15\varepsilon/4}(1+o(1))\) and hence the fourth-root law in item 2. The negative derivative of \(G\) at this root determines the maximum type; the positive quadratic term makes the central point a minimum.

For item 3, write \(r=r_*+\delta\) and use the scaling \(y=\delta Y\), \(\varepsilon=\delta^2E\). The quotient \(\delta^{-2}G(r_*+\delta,\delta^2E,\delta Y)\) extends analytically to \(\delta=0\) and equals there
\[
F(E,Y)=2E+2QY-\frac8{15}Y^2.
\]
The nondegenerate double-root equations \(F=\partial_YF=0\) give
\[
Y_f=\frac{15Q}{8},\qquad E_f=-\frac{15Q^2}{16}=-\left(\frac52+\frac{5\sqrt2}{3}\right).
\]
The Jacobian of \((F,\partial_YF)\) with respect to \((E,Y)\) is nonzero at this point, so the implicit-function theorem produces unique analytic positive fold branches \(Y_f(\delta)\), \(E_f(\delta)\), and the claimed expansions. Since \(\partial_{yy}G(r_*,0,0)=6v(r_*)<0\), \(G\) is strictly concave as a function of \(y\ge0\) within a fixed sufficiently small neighborhood for all nearby parameters. For \(\varepsilon_{\rm fold}<\varepsilon<0\), it is negative at \(y=0\), has a positive maximum, and has exactly two positive zeros in that neighborhood. The sign pattern of \(\partial_z H=2zG\) is then negative / positive / negative for successive positive \(z\): a central maximum, a positive-side minimum, and a positive-side maximum. Reflection gives exactly three maxima and two minima. Setting \(\varepsilon=0\), the nonzero root of \(F(0,Y)\) is \(Y=15Q/4\), proving the stated satellite expansion. All conclusions are local; the argument neither counts nor excludes remote critical points.

## Verification

The standalone `CHECK.py` verifies the complex Gaussian integral numerically against its closed form and the exact intensity factor, independently differentiates the normalized profile symbolically to recover the quartic and sextic coefficients, verifies the exact critical ratio and fold coefficient, and checks nearby stationary-point classifications with high-precision root finding. Run `python CHECK.py` with Python 3, SymPy, and mpmath. These finite checks corroborate, but do not replace, the analytic argument for the quantified local statements.

## Relationship to prior work

Chand, Nolen, and Wu [1] study spectral interference and frequency-ridge bifurcations for a two-component **harmonic** (nonchirped) model, including refinements by reassignment. The present claim concerns the extra common-chirp degree of freedom, a change of local bifurcation type at a calculable positive ratio, and a subcritical coexistence interval. Li and coauthors [2] derive Gaussian STFT formulas for linear frequency-modulated signals and sufficient nonoverlap conditions for multicomponent separation, including the two-component case. Their conditions concern approximate support zones, not the exact local critical-point multiplicity, sixth-order degeneracy, or saddle-node coefficient obtained here. The accessible abstract of [1] is insufficient to exclude every result buried in its unavailable full text, so priority remains subject to that comparison.

## Limitations

The result is restricted to equal-amplitude, coherent, in-phase components sharing a common chirp, to the central time slice, and to a Gaussian analysis window. The signal is bounded but not in \(L^2(\mathbb R)\); the STFT integral nonetheless converges absolutely. Local critical-point statements do not prove global ridge counts, finite-sample resolution, or stability under noise. They do not extend automatically to unequal amplitudes, different chirp rates, shifted analysis times, or chirp ratio \(r\ge1\). The strongest recent related full text could not be inspected, leaving a residual literature-priority risk; no independent audit is asserted.

## References

[1] S. Chand, J. Nolen, H.-T. Wu, *On spectral interference of the short-time Fourier transform and its nonlinear variations*, first publicly available January 15, 2026, arXiv:2601.10910, https://arxiv.org/abs/2601.10910; *Applied and Computational Harmonic Analysis* 85 (2026), doi:10.1016/j.acha.2026.101889.

[2] L. Li, H. Cai, H. Han, Q. Jiang, H. Ji, *Adaptive Short-time Fourier Transform and Synchrosqueezing Transform for Non-stationary Signal Separation*, first publicly available December 29, 2018, arXiv:1812.11292, https://arxiv.org/abs/1812.11292; *Signal Processing* 166 (2020).

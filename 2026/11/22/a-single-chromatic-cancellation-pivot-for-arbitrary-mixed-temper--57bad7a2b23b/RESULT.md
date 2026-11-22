# A single chromatic cancellation pivot for arbitrary mixed-temperature blackbody photospheres

## Finding
Let the visible stellar disk be an arbitrary probability mixture of blackbody temperatures on a compact interval of positive temperatures, and let an unobscured reference transit chord radiate as a blackbody at temperature \(T_0\). Assume that a positive area fraction is cooler than \(T_0\) and another positive fraction is hotter. Write \(\bar B_\lambda\) for the disk-averaged Planck spectrum and \(B_\lambda(T_0)\) for the chord spectrum. Then:

1. The continuum spectral contrast \(\bar B_\lambda-B_\lambda(T_0)\) has a finite positive-wavelength zero **if and only if** the area-mean temperature \(\overline T\) is strictly less than \(T_0\).
2. That zero, when it exists, is **unique**: the disk is brighter than the reference chord on its short-wavelength side and fainter on its long-wavelength side. When \(\overline T\ge T_0\), the disk is brighter for **every** finite wavelength, even at equality of the mean temperatures.
3. If the mixture is nondegenerate and **bolometrically neutral** relative to its chord, meaning \(\int T^4\,d\mu(T)=T_0^4\), the unique chromatic crossover necessarily exists.

Under the uniform-chord, no-limb-darkening transit model, a positive intrinsic transit depth is multiplied by \(B_\lambda(T_0)/\bar B_\lambda\). Hence in the one-pivot case the apparent depth is suppressed on the blue side and enhanced on the red side relative to the intrinsic depth. This theorem is restricted to ideal Planck continua; it does not assert a crossover bound for realistic stellar atmosphere spectra with lines or wavelength-dependent limb darkening.

## Assumptions and scope
Let \(0<T_{\min}<T_0<T_{\max}<\infty\). Let \(\mu\) be any Borel probability measure supported on \([T_{\min},T_{\max}]\), including discrete, continuous, and mixed temperature distributions, such that \(\mu([T_{\min},T_0))>0\) and \(\mu((T_0,T_{\max}])>0\). Atoms at the temperature endpoints are allowed; atoms at \(T_0\) contribute no contrast. Define the Planck spectral radiance per unit wavelength by
\[
B_\lambda(T)=\frac{2hc^2}{\lambda^5}\frac{1}{\exp(hc/(\lambda k_{\rm B}T))-1}, \quad \lambda>0,
\]
and \(\bar B_\lambda=\int B_\lambda(T)\,d\mu(T)\), \(\overline T=\int T\,d\mu(T)\). All temperatures are absolute. Uniform effective projected-area weights and a strictly positive intrinsic transit depth are assumed only for the transit-depth interpretation, not for the continuum crossing theorem.

## Proof
Put \(x=hc/(\lambda k_{\rm B})>0\), and \(b(T,x)=1/(e^{x/T}-1)\). The positive wavelength-dependent Planck prefactor cancels from spectral comparisons. Introduce
\[
K(T,x)=\partial_T b(T,x)=\frac{x}{4T^2}\operatorname{csch}^2\!\left(\frac{x}{2T}\right)>0.
\]
For \(y=x/(2T)>0\), direct differentiation gives
\[
\partial_T\partial_x\log K(T,x)=\frac{\coth y-y\operatorname{csch}^2y}{T^2}>0.
\]
Indeed the numerator equals \((\sinh y\cosh y-y)/\sinh^2y\), which is positive since \(\sinh(2y)>2y\) for \(y>0\). Thus for every \(T_h>T_c>0\) and \(x_2>x_1>0\),
\[
K(T_h,x_2)K(T_c,x_1)>K(T_h,x_1)K(T_c,x_2). \tag{1}
\]

Separate the strictly positive warm and cool contributions:
\[
H(x)=\int_{T>T_0}[b(T,x)-b(T_0,x)]\,d\mu(T),\qquad
C(x)=\int_{T<T_0}[b(T_0,x)-b(T,x)]\,d\mu(T).
\]
By the fundamental theorem of calculus and Tonelli's theorem, \(H\) is a positive mixture of \(K(u,x)\) over \(u>T_0\), while \(C\) is a positive mixture of the same kernel over \(u<T_0\). Integrating the strictly positive determinant (1) over the product of these two positive measures yields
\[
H(x_2)C(x_1)>H(x_1)C(x_2),
\]
so \(R(x)=H(x)/C(x)\) is strictly increasing on \((0,\infty)\).

The Rayleigh–Jeans expansion \(b(T,x)=T/x-1/2+O(x)\), uniform on the compact temperature support, gives
\[
\lim_{x\downarrow0}R(x)=\frac{\int_{T>T_0}(T-T_0)\,d\mu}{\int_{T<T_0}(T_0-T)\,d\mu}=\frac{M_+}{M_-}.
\]
Here \(M_+-M_-=\overline T-T_0\). The warm positive-mass assumption supplies a \(\delta>0\) for which \(\mu([T_0+\delta,T_{\max}])>0\). As \(x\to\infty\), the warm contribution has a lower bound proportional to \(b(T_0+\delta,x)-b(T_0,x)\), whereas \(C(x)\le b(T_0,x)\); therefore \(R(x)\to\infty\). Since \(R\) is continuous and strictly increasing, the equation \(H(x)=C(x)\) has exactly one positive solution precisely when \(M_+<M_-\). If \(M_+\ge M_-\), strict monotonicity makes \(H(x)>C(x)\) at every finite positive \(x\). As \(x\) decreases with wavelength, the hot contribution dominates on the short-wavelength side of a crossing and the cool contribution on the long-wavelength side. This proves assertions 1 and 2.

Finally, \(T\mapsto T^4\) is strictly convex on positive temperatures. If \(\mu\) has nonzero temperature variance and \(\int T^4\,d\mu=T_0^4\), strict Jensen yields \((\overline T)^4<T_0^4\), hence \(\overline T<T_0\), establishing assertion 3. The stated transit-depth sign follows immediately because \(D_{\rm obs}/D_{\rm intrinsic}=B_\lambda(T_0)/\bar B_\lambda\) and both factors are positive.

## Verification
A concrete three-temperature disk has spot, quiet, and facular temperatures \(4000\), \(5000\), and \(6000\) K, with projected fractions \(0.2\), \(0.7\), and \(0.1\). With \(T_0=5000\) K its area-mean temperature is \(4900\) K. Numerical evaluation of the exact Planck formula gives the unique crossing near \(0.530284339425\) micrometres. The excess is positive at \(0.4\) micrometres and negative at \(0.6\) micrometres. The companion standard-library script `verify.py` reproduces this bracketing, a bolometrically neutral mixed-temperature example, and 17,515 supplementary deterministic and randomized numerical assertions, while the preceding proof—not finite tests—establishes all-wavelength uniqueness and the arbitrary-measure result. Run using `python3 verify.py`.

## Relationship to prior work
Rackham, Apai and Giampapa (2017) derive the astrophysical spot-plus-facula spectral contamination formula and simulate stellar heterogeneity with atmosphere-model spectra. Rackham, Apai and Giampapa (2018) extend the empirical modeling to FGK stars. Thompson and collaborators (2023) study the retrieval consequences of spot-contaminated stellar spectra. Désert (2022) describes blackbody temperature mixtures using derivatives and a moment expansion in a different astronomical context. These known mixing and contamination frameworks supply motivation and general context, not the claimed all-distributions, one-crossover classification from the mean temperature. The proof here identifies the precise determinant inequality needed to obtain that classification; it does not claim new Planck's law, Stefan–Boltzmann law, or general theory of totally positive kernels.

## Limitations
The unique-crossover conclusion can fail when spectral components depart from exact blackbodies, with wavelength-dependent spot/facula contrast, spectral absorption bands, nonuniform limb darkening, variable chord intensities, or wavelength-dependent weighting. A crossover can lie outside an instrument's observed band, and an approximate empirical bolometric flux balance cannot substitute for the exact fourth-moment assumption. The theorem describes continuum sign, not the identifiability of physical temperatures from finite noisy measurements. The priority assessment is based on identified and inspected sources, not an exhaustive historical classification, and no independent external audit has occurred.

## References
- B. V. Rackham, D. Apai and M. S. Giampapa, *The Transit Light Source Effect: False Spectral Features and Incorrect Densities for M-dwarf Transiting Planets*, originally public 2017-11-15, https://arxiv.org/abs/1711.05691 (especially the stellar contamination equation and Sections II–IV).
- B. V. Rackham, D. Apai and M. S. Giampapa, *The Transit Light Source Effect II: The Impact of Stellar Heterogeneity on Transmission Spectra of Planets Orbiting Broadly Sun-like Stars*, originally public 2018-12-14, https://arxiv.org/abs/1812.06184.
- A. Thompson et al., *Correcting Exoplanet Transmission Spectra for Stellar Activity with an Optimised Retrieval Framework*, originally public 2023-02-09, https://arxiv.org/abs/2302.04574.
- F.-X. Désert, *The interstellar dust emission spectrum: Going beyond the single-temperature grey body*, 2022, https://doi.org/10.1051/0004-6361/202142617 (temperature-mixing formalism and moment expansion).
- Planck's spectral law and the Stefan–Boltzmann integral are classical physical inputs; no new derivation of either is claimed.

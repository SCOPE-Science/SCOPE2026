# Three-channel Planck inversion of cool-starspot transit contamination

## Finding

**Theorem (exact three-channel identification and sharp data feasibility).** Fix a known stellar photospheric temperature \(T_\star>0\) and a monochromatic wavelength \(\lambda>0\). Under the two-temperature unocculted cool-spot model below, three exact simultaneous transit depths at \(\lambda,2\lambda,4\lambda\) uniquely identify an unknown cool-spot temperature \(T_c\), filling fraction \(f\), and achromatic intrinsic planet depth \(\delta\). There is an explicit inverse, and the inequalities below are necessary *and sufficient* for any positive depth triple to be physically realizable. Two wavelengths never locally identify all three parameters in the strictly interior model.

Let \(Y_j=1/D_j\), with \(D_1,D_2,D_3\) the measured depths at \(\lambda,2\lambda,4\lambda\). Define
\[
s=\exp\!\left(\frac{hc}{4\lambda k_B T_\star}\right)>1,\qquad
R=\frac{Y_2-Y_1}{Y_3-Y_2},\qquad R_{\max}=\frac{2s(s+1)}{s^2+1}.
\]
Then there is an interior cool-spot solution **if and only if** \(0<D_j<\infty\), \(Y_1<Y_2<Y_3\), \(0<R<R_{\max}\), and the recovered \(\alpha>1\) as defined below. The unique solution is
\[
t=\frac{s+1+\sqrt{(s+1)^2+4R[s(s+1)-R]}}{2R},\qquad
T_c=\frac{hc}{4\lambda k_B\log t},
\]
\[
r_2=\frac{s^2-1}{t^2-1},\quad r_3=\frac{s-1}{t-1},\quad
\beta=\frac{Y_3-Y_2}{r_3-r_2},\quad
\alpha=Y_2-\beta r_2,
\]
\[
\boxed{\quad f=\frac{\beta}{\alpha+\beta},\qquad
\delta=\frac1{\alpha+\beta}.\quad}
\]
The ordering inequalities ensure \(\beta>0\) automatically. With \(\alpha>1\), one obtains \(0<T_c<T_\star\), \(0<f<1\), and \(0<\delta<1-f\). Conversely every such physical triple produces these inequalities.

**Sharp band-count obstruction.** Any pair of the three depths from an interior solution is shared by a nontrivial open one-parameter family of physically admissible \((T_c,f,\delta)\) values. If \(f=0\) or \(T_c=T_\star\), all the measured depths are achromatic and the spot parameters cannot be inferred even from the idealized three-band observation.

## Assumptions and scope

The photosphere is an ideal blackbody at known \(T_\star\). The visible but unocculted cool component is one ideal blackbody with unknown \(0<T_c<T_\star\) occupying fraction \(0<f<1\) of the stellar disk. The transiting body occults only photospheric area and has wavelength-independent intrinsic area ratio \(\delta\), constrained to \(0<\delta<1-f\). Ignore limb darkening, emission, atmospheric planetary spectral features, overlapping spots, faculae, and bandpass averaging. Wavelengths are exactly \(\lambda,2\lambda,4\lambda\) and all three measurements share the same filling fraction. Planck's spectral radiance \(B_\lambda(T)\) is used consistently in wavelength units; the monochromatic wavelength-dependent prefactor cancels within each temperature ratio. \(h,c,k_B\) denote Planck's constant, speed of light and Boltzmann's constant. These are theoretical exact-data statements, not noise-robust estimation guarantees.

The measured transit model is
\[
D_j=\frac{\delta}{(1-f)+f r_j},\qquad
r_j=\frac{B_{\lambda_j}(T_c)}{B_{\lambda_j}(T_\star)},\qquad
(\lambda_1,\lambda_2,\lambda_3)=(\lambda,2\lambda,4\lambda).
\]

## Proof

**Step 1: linearization.** By Planck's law and the definitions \(s=\exp(hc/(4\lambda k_BT_\star))\) and \(t=\exp(hc/(4\lambda k_BT_c))\), the temperature assumption is exactly \(1<s<t\). The intensity contrasts are
\[
r_1=\frac{s^4-1}{t^4-1},\quad
r_2=\frac{s^2-1}{t^2-1},\quad
r_3=\frac{s-1}{t-1},
\]
with \(0<r_1<r_2<r_3<1\). Taking reciprocals gives \(Y_j=\alpha+\beta r_j\), where \(\alpha=(1-f)/\delta>1\) and \(\beta=f/\delta>0\). Hence \(Y_1<Y_2<Y_3\).

**Step 2: a monotone contrast ratio.** Direct subtraction and factorization yield
\[
r_3-r_2=\frac{(s-1)(t-s)}{t^2-1},\qquad
r_2-r_1=\frac{(s-1)(s+1)(t-s)(s+t)}{(t^2-1)(t^2+1)}.
\]
Thus the nuisance constants \(\alpha,\beta\) cancel from the data ratio:
\[
R=\frac{Y_2-Y_1}{Y_3-Y_2}
=\frac{r_2-r_1}{r_3-r_2}
=F_s(t):=\frac{(s+1)(s+t)}{1+t^2}.
\]
For all \(t>s>1\),
\[
F'_s(t)=\frac{(s+1)(1-t^2-2st)}{(1+t^2)^2}<0.
\]
The endpoint limits are \(F_s(s)=2s(s+1)/(1+s^2)=R_{\max}\) and \(F_s(t)\to0\) as \(t\to\infty\). Consequently \(F_s\) is a bijection from \((s,\infty)\) onto \((0,R_{\max})\). Solving the resulting quadratic \(Rt^2-(s+1)t+[R-s(s+1)]=0\) gives exactly the displayed positive root. No second root lies in the physical interval \((s,\infty)\).

**Step 3: complete physical inversion.** With recovered \(t\), the strictly positive difference \(r_3-r_2\) determines \(\beta>0\), then \(\alpha\) follows uniquely. The formulas for \(f,\delta\) are forced because \(\alpha+\beta=1/\delta\). The condition \(\alpha>1\) is equivalent to the unspotted-photosphere area constraint \(\delta<1-f\), and positivity of \(\beta\) implies \(0<f<1\). This proves sufficiency, and Step 1 proves necessity. Uniqueness follows from the strictly monotone ratio and linear inversion. If any condition fails, no interior solution exists in this model.

**Step 4: why two bands cannot identify.** Fix any physical interior solution and choose any two distinct wavelengths from the three above. Each candidate \(t'>s\) near the true \(t\) has distinct contrasts \(r_i(t')\ne r_j(t')\). The two measured reciprocals have the unique corresponding affine coefficients \(\beta(t')=(Y_j-Y_i)/(r_j(t')-r_i(t'))\) and \(\alpha(t')=Y_i-\beta(t')r_i(t')\). These coefficients vary continuously with \(t'\); strict inequalities \(\alpha>1\), \(\beta>0\) persist on an open neighborhood. Inverting the affine coefficients produces infinitely many distinct physical triples with *exactly the same two measurements*. Thus no two-channel local identification is possible. At \(f=0\) or \(t=s\), all contrasts are respectively irrelevant or unity and no chromatic information remains.

## Verification

An exact rational witness takes \(s=2\), \(t=3\), \(f=1/4\), \(\delta=1/100\), corresponding to \(T_c/T_\star=\log 2/\log3\). It has \((r_1,r_2,r_3)=(3/16,3/8,1/2)\), \((Y_1,Y_2,Y_3)=(1275/16,675/8,175/2)\), measured \((D_1,D_2,D_3)=(16/1275,8/675,2/175)\) and \(R=3/2\). The inverse gives \(\alpha=75\), \(\beta=25\), recovering the exact input. The standalone `checker.py` reproduces these rational identities and checks a further fixed-seed sample of synthetic interior triples. The symbolic factorization and derivative sign above, not the finite checks, prove the infinite-domain assertions.

## Relationship to prior work

Rackham, Apai and Giampapa (2018; preprint 2017) formulate the stellar transit-light-source contamination factor under heterogeneous photospheres; this familiar *forward* formula is the starting point, not claimed as new. Saba et al. (2024 preprint) investigate real multiband contamination and Bayesian retrieval, documenting challenges caused by stellar heterogeneity. Thompson et al. (2023 preprint) and Chakraborty et al. (2023 preprint) address more realistic numerical inference including additional stellar/instrument effects. The theorem here claims only the special, sharply identifiable inverse under an exact two-blackbody, achromatic, three-monochromatic-channel model; general multi-component or wide-bandpass inversions are not covered. Rosich et al. (2020) explicitly propose three-band identifiability for a different observable—rotational photometric amplitudes with modulating and constant spot components—and illustrate two-band ambiguities; the general principle that a third colour helps is therefore known. What is claimed here is the specific global, exact, harmonic-wavelength inverse and necessary-and-sufficient data-feasibility region for three single-epoch *transit depths*, with an achromatic planet and one unknown cool-spot fraction. The algebraic factorization and complete if-and-only-if criterion were not located as stated in the inspected sources. This is a best-knowledge comparison, not proof of historical priority.

## Limitations

The result is an exact, simplified identification benchmark, not an estimator for noisy data. Temperature or filling fraction differences approaching zero make wavelength differences small and inversion poorly conditioned; at the boundary they are unidentifiable. Planetary atmospheric colour, unknown photospheric temperature, limb darkening, hot faculae, multiple spot temperatures, changing epochs and finite passbands can reintroduce ambiguities. The three special wavelengths may not be available on an actual instrument. No claim of independent verification, astrophysical calibration or universal three-band identification is made.

## References

1. Saba, A. et al., *A Population Analysis of 20 Exoplanets Observed from the Optical to the Near-infrared Wavelengths with HST: Evidence for Widespread Stellar Contamination*, arXiv:2404.15505, version 1 publicly submitted 2024-04-23. https://arxiv.org/abs/2404.15505
2. Rackham, B. V., Apai, D., and Giampapa, M. S., *The Transit Light Source Effect: False Spectral Features and Incorrect Densities for M-dwarf Transiting Planets*, arXiv:1711.05691, publicly submitted 2017-11-15. https://arxiv.org/abs/1711.05691
3. Thompson, A. et al., *Correcting Exoplanet Transmission Spectra for Stellar Activity with an Optimised Retrieval Framework*, arXiv:2302.04574, publicly submitted 2023-02-09. https://arxiv.org/abs/2302.04574
4. Chakraborty, R. et al., *SAGE: A tool to constrain impacts of stellar activity on transmission spectroscopy*, arXiv:2311.16864, publicly submitted 2023-11-28. https://arxiv.org/abs/2311.16864

5. Rosich, A. et al., *Correcting for chromatic stellar activity effects in transits with multiband photometric monitoring: Application to WASP-52*, arXiv:2007.00573, publicly submitted 2020-07-01. https://arxiv.org/abs/2007.00573

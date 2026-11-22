# A sharp bath-contrast ceiling for irreversible cross-spectral coherence in a Brownian gyrator

## Finding

For a two-temperature overdamped harmonic gyrator, the normalized imaginary component of the complex coordinate cross-spectrum has a unique optimal positive analysis frequency for each fixed nonzero stable coupling. More strikingly, its maximum over all stable couplings and frequencies obeys a sharp temperature-contrast-only ceiling:

\[
\sup_{0<k<a,\,\omega\in\mathbb R}\frac{[\operatorname{Im}S_{xy}(\omega)]^2}{S_{xx}(\omega)S_{yy}(\omega)}=\frac{(\sqrt{T_x}-\sqrt{T_y})^2}{T_x+T_y}.
\]

For unequal bath strengths this supremum is not attained by any strictly stable trap; it is attained only as a limit at the soft-mode stability boundary. Unlike the ordinary squared magnitude of cross-spectral coherence, this imaginary-part statistic vanishes at thermal equilibrium despite nonzero elastic coupling. It therefore isolates the time-antisymmetric component of the spectrum rather than general linear dependence.

## Assumptions and scope

Take \(a>0\), \(0<k<a\), \(T_x,T_y>0\). The unique stationary real Gaussian diffusion is

\[
\begin{aligned}
dX_t&=(-aX_t-kY_t)\,dt+\sqrt{2T_x}\,dW_{x,t},\\
dY_t&=(-kX_t-aY_t)\,dt+\sqrt{2T_y}\,dW_{y,t},
\end{aligned}
\]

where the Brownian motions are independent. Let \(K=\begin{psmallmatrix}a&k\\k&a\end{psmallmatrix}\) and \(D=\operatorname{diag}(T_x,T_y)\). With the two-sided spectral convention \(S(\omega)=2(K+i\omega I)^{-1}D(K-i\omega I)^{-1}\), define

\[
\mathcal I(\omega)=\frac{[\operatorname{Im}S_{xy}(\omega)]^2}{S_{xx}(\omega)S_{yy}(\omega)}\,.
\]

Both diagonal spectra are strictly positive. Reversing the Fourier sign convention reverses the sign of the imaginary cross-spectrum but leaves \(\mathcal I\) unchanged. The result concerns stationary population spectra, not finite-window estimation variance. The labels \(x\) and \(y\) may be swapped without changing the claims.

## Proof

**Exact cross-spectrum.** Directly multiplying the two resolvent matrices gives, with \(\Delta_\omega=[(a-k)^2+\omega^2][(a+k)^2+\omega^2]>0\),

\[
\begin{aligned}
S_{xx}(\omega)&=\frac{2[(a^2+\omega^2)T_x+k^2T_y]}{\Delta_\omega},\\
S_{yy}(\omega)&=\frac{2[(a^2+\omega^2)T_y+k^2T_x]}{\Delta_\omega},\\
S_{xy}(\omega)&=-\frac{2k[a(T_x+T_y)+i\omega(T_x-T_y)]}{\Delta_\omega}.
\end{aligned}
\]

Thus \(\mathcal I\ge0\), it vanishes identically for \(T_x=T_y\), and when temperatures differ it is strictly positive at all nonzero frequencies. It decays to zero at zero frequency and infinity.

**Reduction to two dimensionless controls.** Define \(v=(k/a)^2\in(0,1)\), \(z=(\omega/a)^2\ge0\), and \(\tau=T_y/T_x>0\). Cancelling the positive common spectral denominator yields

\[
\mathcal I=\frac{v z(\tau-1)^2}{(1+z+v\tau)[\tau(1+z)+v]}.
\tag{1}
\]

For \(\tau\ne1\), differentiating (1) with respect to \(z\) and removing positive factors shows the sign of the derivative is that of

\[
(1+v\tau)(1+v/\tau)-z^2.
\]

Consequently the only critical point on positive frequencies is the unique strict global maximum at

\[
z_*(v,\tau)=\sqrt{(1+v\tau)(1+v/\tau)},\quad
\omega_*=a[(1+v\tau)(1+v/\tau)]^{1/4}.
\]

The only other maximizing real frequency is \(-\omega_*\); at \(\omega=0\) the value vanishes.

**Monotonicity in coupling.** For fixed \(z>0\), put \(A=1+z\). Up to the positive factor \(z(\tau-1)^2\), equation (1) is \(v/[(A+v\tau)(\tau A+v)]\), whose derivative is exactly

\[
\frac{\tau(A^2-v^2)}{(A+v\tau)^2(\tau A+v)^2}>0
\]

for \(A\ge1\) and \(0<v<1\). Hence the frequency-optimized coherence is strictly increasing in coupling, and the global supremum is approached as \(v\uparrow1\), not attained in the stable domain.

**Sharp contrast ceiling and maximizing sequence.** At \(v=1\) the positive-frequency optimizer becomes \(z_*(1,\tau)=(1+\tau)/\sqrt\tau\). Substituting these limiting values into (1) simplifies to

\[
\mathcal I_{\rm sup}=\frac{(\sqrt\tau-1)^2}{1+\tau}
=\frac{(\sqrt{T_x}-\sqrt{T_y})^2}{T_x+T_y}.
\]

Choosing any sequence of positive couplings \(k_m<a\) increasing to \(a\) and \(\omega_m=a[(1+v_m\tau)(1+v_m/\tau)]^{1/4}\) attains this value in the limit. Conversely, to approach the ceiling, the strict monotonicity in \(v\) enforces \(v\to1\), and the unique limiting positive-frequency maximum enforces \(z\to(1+\tau)/\sqrt\tau\). For equal temperatures the statistic is identically zero at all frequencies and the zero ceiling is attained everywhere: no uniqueness or boundary statement is claimed in that case.

## Verification

The supplied standalone \(checker.py\) recomputes the full complex spectral matrix from the independent matrix-resolvent definition; symbolically verifies all four entries against the displayed formulas, both derivative identities, and the sharp boundary expression; and tests 144 exact-rational temperature/coupling/frequency comparisons with high-precision evaluation. The proof above, rather than the finite parameter tests, establishes the statements for all permitted real parameters. To reproduce: \(\texttt{python checker.py}\) with Python 3 and SymPy installed.

## Relationship to prior work

Cerasoli, Ciliberto, Marinari, Oshanin, Peliti and Rondoni (2022) derive spectral fingerprints of the Brownian gyrator, particularly a Pearson correlation of *single-trajectory auto-spectral powers* and its low-frequency behavior. Its Pearson coefficient concerns the entire magnitude correlation and is not the time-antisymmetric imaginary component used here. Their explicit general Langevin/spectral framework is prior background and can facilitate algebraic reductions, but the inspected main results and appendices do not state this positive-frequency optimizer or the global thermal-only boundary and nonattainment theorem. Henkel (2021) gives cross-correlation spectra for two quantum oscillators with separate baths, a broader physical setting with inertial/quantum dynamics, but not this stable overdamped optimum. Ordinary spectral positive-semidefiniteness gives the weaker generic bound \(\mathcal I\le1\), not the bath-contrast-only sharp ceiling. The present result is a closed-form *optimization of a specific irreversible part of a population cross-spectrum*, not a new general spectral framework.

## Limitations

The theorem assumes equal positive trap diagonal relaxations, reciprocal positive coupling smaller than the relaxation, independent white-noise baths of strictly positive strengths, and stationary spectra. A bath at exactly zero temperature is excluded; the thermal-contrast limit can nevertheless tend to one. The stability-edge equality is a supremum only because the stationary law ceases to exist at \(k=a\). The theorem does not optimize finite-sample detectability, estimation variance, measurement cost, general nonsymmetric traps, fractional baths, or entropy production. Prior general resolvent formulas might contain the calculation implicitly; the literature comparison does not establish formal publication priority or independent certification.

## References

1. S. Cerasoli, S. Ciliberto, E. Marinari, G. Oshanin, L. Peliti, L. Rondoni, *Spectral fingerprints of nonequilibrium dynamics: The case of a Brownian gyrator*, Phys. Rev. E **106**, 014137 (2022), DOI: 10.1103/PhysRevE.106.014137, https://arxiv.org/abs/2201.04903 (first public version 2022-01-13); open complete manuscript: https://www.smri.it/Publications/Phys_Rev_E_Gyrator_Spectra.pdf.
2. C. Henkel, *Heat Transfer and Entanglement–Non-Equilibrium Correlation Spectra of Two Quantum Oscillators*, Annalen der Physik **533**, 2100089 (2021), DOI: 10.1002/andp.202100089, https://onlinelibrary.wiley.com/doi/full/10.1002/andp.202100089.

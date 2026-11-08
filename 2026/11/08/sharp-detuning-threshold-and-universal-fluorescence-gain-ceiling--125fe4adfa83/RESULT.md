# Sharp detuning threshold and universal fluorescence-gain ceiling under ground-state Poisson resetting

## Finding
For a coherently driven, radiatively decaying two-level emitter, complete Poisson resets to its ground state *increase* the stationary spontaneous-emission rate exactly when the laser detuning obeys \(4\Delta^2>3\gamma^2\) and the resetting rate lies in an explicit finite interval. There is a unique globally optimal positive resetting rate, independent of the Rabi coupling, and resetting can enhance emission by **strictly less than a factor of two**; this constant is globally sharp.

Precisely, for \(\gamma>0\), \(\Omega>0\), \(\Delta\in\mathbb R\), and \(r\ge0\), the stationary emission flux is
\[
J(r)=\frac{\gamma\Omega^2(\gamma+2r)}{B(r)},\qquad
B(r)=\gamma^3+2\gamma\Omega^2+4\gamma\Delta^2
 +(5\gamma^2+4\Omega^2+4\Delta^2)r+8\gamma r^2+4r^3.
\]
Its unreset value is \(J(0)=\gamma\Omega^2/(\gamma^2+2\Omega^2+4\Delta^2)>0\). If \(4\Delta^2\le3\gamma^2\), then \(J(r)<J(0)\) for every \(r>0\). If \(4\Delta^2>3\gamma^2\), then \(J\) has one strict global maximum at the unique positive root of
\[
16r^3+28\gamma r^2+16\gamma^2r+3\gamma^3-4\gamma\Delta^2=0.
\]
This maximizer \(r_*\) is independent of \(\Omega\); moreover \(J(r)>J(0)\) holds exactly for
\[
0<r<r_c,\qquad r_c=\frac{\sqrt{\gamma^2+4\Delta^2}-2\gamma}{2},\qquad 0<r_*<r_c.
\]
In every regime \(J(r)<2J(0)\) for all finite \(r\ge0\), and \(\max_{r\ge0}J(r)/J(0)\to2\) as \(|\Delta|\to\infty\) for any fixed \(\gamma,\Omega>0\).

## Assumptions and scope
Take the two-dimensional Hilbert space spanned by normalized \(|g\rangle\) and \(|e\rangle\). In units \(\hbar=1\), the Hamiltonian is \(H=\frac{\Omega}{2}(|g\rangle\langle e|+|e\rangle\langle g|)+\Delta |e\rangle\langle e|\). Spontaneous photon emissions are represented by the Lindblad operator \(L=\sqrt\gamma |g\rangle\langle e|\). Independently, a Poisson clock of rate \(r\) instantaneously maps the entire density matrix to \(\rho_g=|g\rangle\langle g|\); reset events are *not* counted as photon emissions. The density matrix solves
\[
\dot\rho=-i[H,\rho]+\gamma\left(L_0\rho L_0^\dagger-\frac12\{L_0^\dagger L_0,\rho\}\right)+r(\rho_g-\rho),\quad L_0=|g\rangle\langle e|.
\]
Equivalently use the radiative Lindblad operator \(L\) and omit the explicit prefactor \(\gamma\). For every \(\gamma>0\) the dynamics has a unique stationary state. \(J=\gamma\langle e|\rho_*|e\rangle\) counts only radiative emission. No unmodelled dephasing, pure thermal excitation, dead-time, or finite-duration reset is asserted.

## Proof
Set \(p=\rho_{ee}\), \(u=\operatorname{Re}\rho_{ge}\), \(v=\operatorname{Im}\rho_{ge}\), and \(h=\gamma/2+r\). In the stationary state the optical Bloch equations read
\[
0=\Omega v-(\gamma+r)p,\qquad0=-hu-\Delta v,\qquad0=\Delta u-hv+\tfrac{\Omega}{2}(1-2p).
\]
Eliminating \(u,v\) and using \(h>0\) gives
\[
p=\frac{\Omega^2h}{2(\gamma+r)(h^2+\Delta^2)+2\Omega^2h}
=\frac{\Omega^2(\gamma+2r)}{B(r)}.
\]
All coefficients of \(B\) are strictly positive, proving denominator positivity over the stated domain. Differentiation and exact factorization give
\[
J'(r)=-\frac{\gamma\Omega^2}{B(r)^2}P(r),\quad
P(r)=16r^3+28\gamma r^2+16\gamma^2r+3\gamma^3-4\gamma\Delta^2.
\]
Here \(P'(r)=48r^2+56\gamma r+16\gamma^2>0\) for all \(r\ge0\). If \(4\Delta^2\le3\gamma^2\), then \(P(r)>0\) for all \(r>0\), so the flux decreases strictly. Otherwise \(P(0)<0\), \(P(r)\to\infty\), and strict monotonicity implies exactly one root \(r_*>0\), with positive derivative before and negative derivative after it. Since \(J(r)\to0\), it is the global maximum.

Subtracting the unreset value and factoring exactly yields
\[
J(r)-J(0)=\frac{-\gamma\Omega^2r(3\gamma^2+8\gamma r+4r^2-4\Delta^2)}{(\gamma^2+2\Omega^2+4\Delta^2)B(r)}.
\]
For \(4\Delta^2>3\gamma^2\), the quadratic factor has precisely one positive root \(r_c=(\sqrt{\gamma^2+4\Delta^2}-2\gamma)/2\). Therefore the enhancing rates are exactly \((0,r_c)\); since \(J(r_c)=J(0)\) and \(J\) increases initially, the unique maximizer lies inside this interval.

Finally, the exact positive identity
\[
2J(0)-J(r)=\frac{\gamma\Omega^2[\gamma^3+2\gamma\Omega^2+4\gamma\Delta^2+(8\gamma^2+4\Omega^2)r+16\gamma r^2+8r^3]}{(\gamma^2+2\Omega^2+4\Delta^2)B(r)}>0
\]
proves the universal strict bound. For fixed \(\gamma,\Omega>0\) with \(|\Delta|\to\infty\), the unique cubic root satisfies \(r_*\sim(\gamma\Delta^2/4)^{1/3}\), so \(r_*/|\Delta|\to0\). Substitution in the rational formula shows \(J(r_*)/J(0)\to2\). This proves optimal sharpness without an equality case.

## Verification
The self-contained standard-Python/SymPy script `verify.py` symbolically reproduces the stationary Bloch expression, its derivative, the enhancement factorization, and the sharp strict-bound identity. It also reconstructs the same photon intensity independently through the inverse no-photon generator and a renewal count, and checks eight independently solved exact-rational steady-state linear systems and seven cubic root-count examples. Run `python verify.py`; the run reported 30 passing checks. The analytic monotonicity arguments, not a finite parameter grid, prove the universal quantifiers. For \(\gamma=\Omega=1\) and \(\Delta=2\), numerical values are \(J(0)=1/19\), \(r_*\approx0.4232277299\), \(r_c\approx1.0615528128\), and \(J(r_*)/J(0)\approx1.1202465509\).

## Relationship to prior work
Perfetto, Carollo and Lesanovsky (2021), arXiv:2112.05078, analyze the photon-emission statistics of a resonantly driven open quantum two-level system subject to stochastic resetting and show resetting suppresses activity in their ground-resetting resonant example. The present theorem instead resolves the **detuned** regime, including the unique flux-maximizing reset rate and sharp factor-two envelope. Reynaud (2022), arXiv:2212.11137, gives the exact detuned, *unreset* resonance-fluorescence waiting-time formula, and its older spectral conclusions are not claimed anew. Carollo, Lesanovsky and Garrahan (2023), arXiv:2310.06981, analyze reset-conditioned quantum jump statistics; neither their general formalism nor earlier optical Bloch calculations is claimed as new. The rational stationary expression is a consequence of standard Bloch equations, so the substantive assertion is the all-parameter **reset-enhancement phase classification**, rate-independent optimizer, and sharp gain ceiling. Those conclusions might be implicitly obtainable from more general earlier formulae and independent publication-priority review is still needed.

## Limitations
This is an ideal Markovian two-level model with instantaneous, state-preparing Poisson resets independent of spontaneous emission. Reset cost, finite reset fidelity, detector efficiency, extra dephasing, thermal excitations, and multilevel structure are not modeled. The result is stationary and makes no universal claims about finite-time photon counting, optimum energetic efficiency, or experimental advantage. No claim is made that the foundational Bloch or renewal machinery is original. The comparison to other conceivable detuned reset models cannot exclude unidentified prior publications; independent validation has not occurred.

## References
- G. Perfetto, F. Carollo, and I. Lesanovsky, *Thermodynamics of quantum-jump trajectories of open quantum systems subject to stochastic resetting*, arXiv:2112.05078 (first publicly posted 2021-12-09). https://arxiv.org/abs/2112.05078
- S. Reynaud, *The resonance fluorescence cascade of a laser-excited two-level atom*, arXiv:2212.11137 (first publicly posted 2022-12-21). https://arxiv.org/abs/2212.11137
- F. Carollo, I. Lesanovsky, and J. P. Garrahan, *Universal and nonuniversal probability laws in Markovian open quantum dynamics subject to generalized reset processes*, arXiv:2310.06981 (first publicly posted 2023-10-10). https://arxiv.org/abs/2310.06981

# An inverse-square-root spectral-edge threshold for quantum-memory purity

## Finding

For the uniform-history quantum-resetting channel of de Mauro, Kulkarni and Majumdar, the long-time purity of a pure state supported on an absolutely continuous energy band has a sharp transition at a square-root spectral edge. Explicitly, let \(r>0\) and \(0\leq\alpha<1\). On \(\mathcal H=L^2((0,1),dE)\), let \(H\) be multiplication by \(E\), and initialize the density matrix in the rank-one state associated with the normalized wavefunction \(\psi_\alpha(E)=\sqrt{1-\alpha}\,E^{-\alpha/2}\). Write \(P_\alpha(t)=\operatorname{Tr}(\rho_\alpha(t)^2)\) and \(L=\log(rt)\). As \(t\to\infty\),
\[
P_\alpha(t)\sim
\begin{cases}
\displaystyle\frac{(1-\alpha)^2}{1-2\alpha}\frac{r\sqrt\pi}{\sqrt{2L}}, & 0\le\alpha<\frac12,\\[4pt]
\displaystyle\frac{r\sqrt\pi}{8\sqrt{2L}}\log L, & \alpha=\frac12,\\[4pt]
\displaystyle (1-\alpha)^2B(1-\alpha,2\alpha-1)\Gamma(1-\alpha)\left(\frac{r^2}{2L}\right)^{1-\alpha}, & \frac12<\alpha<1.
\end{cases}
\]
The middle line gives a genuine \(\log\log(rt)/\sqrt{\log(rt)}\) enhancement at the critical inverse-square-root edge, and the last line gives continuously varying non-Gaussian logarithmic exponents. The critical and supercritical assertions are not covered by the earlier bounded-energy-density purity theorem.

## Assumptions and scope

The channel acts on a trace-one positive trace-class operator, with natural units \(\hbar=1\), according to
\[
\frac{d\rho(t)}{dt}=-i[H,\rho(t)]-r\rho(t)+\frac rt\int_0^t\rho(s)\,ds.
\]
This is an equation in the mild/trace-class sense. A memory reset samples a time uniformly from the entire preceding interval; it does not reset to one fixed initial state. All exponents \(\alpha\) are fixed when \(t\to\infty\); the theorem does not assert uniformity if \(\alpha\) itself approaches \(1/2\) with time. The Hamiltonian and the initial wavefunction are precisely as defined above. Positivity and normalization of the initial state follow from \(\int_0^1(1-\alpha)E^{-\alpha}\,dE=1\).

## Proof

**Exact scalar reduction.** Let \(\omega=E-E'\). The known scalar response is
\[
f_r(\omega,t)={}_1F_1\!\left(\frac{i\omega}{r+i\omega};1;-(r+i\omega)t\right).
\]
It gives the exact energy-basis density kernel \(\rho_\alpha(E,E',t)=\psi_\alpha(E)\overline{\psi_\alpha(E')}f_r(E-E',t)\). Consequently, with \(w_\alpha(E)=(1-\alpha)E^{-\alpha}\) on \((0,1)\),
\[
P_\alpha(t)=\int_0^1\int_0^1 w_\alpha(E)w_\alpha(E')|f_r(E-E',t)|^2\,dE\,dE'
=2\int_0^1G_\alpha(\delta)|f_r(\delta,t)|^2\,d\delta,
\]
where for \(0<\delta<1\),
\[
G_\alpha(\delta)=(1-\alpha)^2\int_0^{1-\delta}u^{-\alpha}(u+\delta)^{-\alpha}\,du.
\]
The complex-conjugation symmetry of the response ensures the last reduction. All integrals are finite for every \(t\), since \(|f_r|\le1\) and \(w_\alpha\in L^1\).

**Singular autocorrelation lemma.** Direct integration or a positive dominated limit gives the following three exact near-zero behaviors:
\[
G_\alpha(\delta)\longrightarrow \frac{(1-\alpha)^2}{1-2\alpha} \quad(\alpha<1/2);
\]
\[
G_{1/2}(\delta)=\frac12\operatorname{arsinh}\sqrt{\frac{1-\delta}{\delta}}=\frac14\log(1/\delta)+O(1);
\]
\[
G_\alpha(\delta)\sim (1-\alpha)^2 B(1-\alpha,2\alpha-1)\,\delta^{1-2\alpha}\quad(\alpha>1/2).
\]
For the last line substitute \(u=\delta v\); its rescaled integrand converges by monotone convergence to \(v^{-\alpha}(1+v)^{-\alpha}\) on \((0,\infty)\), which is integrable exactly when \(\alpha>1/2\). The integral is the displayed beta function. The critical line follows by evaluating \(\int du/\sqrt{u(u+\delta)}\) explicitly. The subcritical line follows from dominated convergence after extending the integrand to \([0,1]\); near zero it is bounded by \(u^{-2\alpha}\).

**Frequency localization.** The Kummer large-argument expansion, uniform on the compact real frequency interval \([-1,1]\) and in particular near zero, gives
\[
f_r(\omega,t)=\frac{[(r+i\omega)t]^{-a(\omega)}}{\Gamma(1-a(\omega))}(1+o(1)),\qquad a(\omega)=\frac{i\omega}{r+i\omega},
\]
with an exponentially small discarded branch. The asymptotic is understood with the continuous logarithm chosen on the right half-plane, so \(\operatorname{Re}a(\omega)=\omega^2/(r^2+\omega^2)\). For \(\sigma=r/\sqrt{2L}\), uniformly for bounded real \(y\),
\[
|f_r(\sigma y,t)|^2\longrightarrow e^{-y^2}.
\]
The same uniform asymptotic with the fact that the gamma factor is bounded away from zero on this compact parameter family supplies constants \(C,c>0\), depending on fixed \(r\), such that \(|f_r(\omega,t)|^2\le C e^{-cL\omega^2}\) for \(0\le\omega\le1\) at sufficiently large \(t\) (an exponentially small term is harmless). This provides an integrable majorant after rescaling and also makes frequencies \(\delta\gg\sigma\) negligible, including when the autocorrelation has its integrable singularity. Thus replacing the kernel by the Gaussian profile inside the asymptotically shrinking frequency window is justified, not merely heuristic.

**Evaluation of all three regimes.** For \(\alpha<1/2\), substitute \(\delta=\sigma y\) in the purity integral and use the finite limit of \(G_\alpha\). One obtains \(2G_\alpha(0)\sigma\int_0^\infty e^{-y^2}dy=G_\alpha(0)\sigma\sqrt\pi\). For \(\alpha=1/2\), since \(\log(1/(\sigma y))=\tfrac12\log L+O(1+|\log y|)\) for fixed \(y>0\), the critical autocorrelation contributes \(2(1/4)(1/2\log L)\sigma\int_0^\infty e^{-y^2}dy=\sigma\sqrt\pi\log L/8\). The terms containing \(|\log y|\) are integrable near zero and infinity, validating the coefficient. For \(\alpha>1/2\), insert the power-law autocorrelation to obtain
\[
P_\alpha(t)\sim 2(1-\alpha)^2B(1-\alpha,2\alpha-1)\sigma^{2-2\alpha}\int_0^\infty y^{1-2\alpha}e^{-y^2}dy.
\]
The final integral equals \(\Gamma(1-\alpha)/2\). These are precisely the three formulas stated in the finding.

## Verification

The included standalone `check.py` evaluates the exact confluent-hypergeometric response, independently expands its defining series, checks the beta-integral autocorrelation against an independent regularizing substitution, verifies its exact critical square-root formula, checks the stated Kummer leading branch at finite times, and evaluates Gaussian-kernel proxy integrals as an asymptotic diagnostic. It passes 34 finite deterministic assertions with Python and mpmath. The Gaussian proxy converges particularly slowly at the critical point because its omitted correction is relatively of order \(1/\log L\); finite ratios are not asserted to be proofs of the asymptotic. The asymptotic equivalents themselves follow analytically from the three steps above.

## Relationship to prior work

De Mauro, Kulkarni and Majumdar (2026), *Quantum resetting with memory* (arXiv:2608.02297v1), establish the full-memory master equation, scalar Kummer response and decay at fixed nonzero energy gaps. Those ingredients are credited, not claimed new. The prior result *A Schatten threshold and a logarithmic purity law for quantum resetting with memory* (2026) establishes \(P(t)\sim r\sqrt{\pi/(2\log(rt))}\int w(E)^2dE\) for an initially pure state with **bounded** energy density \(w\). That identity explains the subcritical branch after an elementary extension to square-integrable unbounded weights, but its hypothesis fails exactly at and above \(\alpha=1/2\): the integral \(\int w_\alpha^2\) diverges. Neither the finite coefficient nor the exponent at that singular boundary follows by substituting into the previous formula. The present proof derives the critical \(\log\log\) factor and supercritical beta/gamma coefficient by a distinct singular-autocorrelation analysis.

## Limitations

Only the fixed family of power-law energy densities on a single bounded band and positive fixed reset rate is treated. An actual lattice van Hove edge often has a smooth varying prefactor or a second band edge; while the inverse-square-root motivation is physical, no universality for arbitrary density-of-states prefactors is asserted. The result concerns ensemble purity, not trajectory purity, entanglement or the rate of trace-norm convergence. The critical \(\log\log\) term has unusually slow relative convergence. The literature search and inspected portions of relevant primary text do not establish exhaustive priority; equivalent unindexed results remain possible, and independent review is pending.

## References

- G. de Mauro, M. Kulkarni and S. N. Majumdar, *Quantum resetting with memory*, arXiv:2608.02297v1, publicly posted August 3, 2026. https://arxiv.org/abs/2608.02297
- *A Schatten threshold and a logarithmic purity law for quantum resetting with memory*, October 25, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-schatten-threshold-and-a-logarithmic-purity-law-for-quantum-re--1493090d05f9
- NIST Digital Library of Mathematical Functions, Chapter 13, §13.7, *Asymptotic Expansions for Large Argument*. https://dlmf.nist.gov/13.7

# Sharp accumulated-coherence trichotomy for power-biased quantum memory resetting

## Finding

Let a finite-dimensional quantum state undergo unitary evolution with a fixed Hamiltonian between Poisson resetting events of intensity \(r>0\). At each reset at time \(t>0\), the past state to be restored is sampled from the history with density
\[
K_\beta(s,t)=\frac{\beta s^{\beta-1}}{t^\beta},\qquad 0<s<t,\quad\beta>0.
\]
Denote the averaged density matrix by \(\rho_\beta(t)\), its energy-dephased limit by \(\rho_\infty\), and the accumulated deviation by
\[
S_\beta(T)=\int_0^T[\rho_\beta(t)-\rho_\infty]dt.
\]
Write \(H=\sum_E E P_E\) in units \(\hbar=1\). If \([H,\rho_0]\ne0\), let the **least active Bohr gap** and its associated threshold be
\[
\Delta=\min\{|E-F|:E\ne F,\ P_E\rho_0P_F\ne0\}>0,
\qquad
\beta_* = 1+\left(\frac r\Delta\right)^2.
\]
The following trichotomy is sharp.

**(i) Growing accumulated coherence.** For \(0<\beta<\beta_*\), put
\[
\alpha=\frac{\beta\Delta^2}{r^2+\Delta^2}<1,
\quad\gamma=\frac{\beta r\Delta}{r^2+\Delta^2},
\quad a=\alpha+i\gamma,
\]
and define
\[
B=\frac{\Gamma(\beta)}{\Gamma(\beta-a)}(r+i\Delta)^{-a},
\quad
A=\frac{B}{1-a}\sum_{E-F=\Delta}P_E\rho_0P_F.
\]
The complex power uses the principal logarithm; \(A\ne0\). In Hilbert–Schmidt norm,
\[
S_\beta(T)=T^{1-\alpha}\left(e^{-i\gamma\log T}A+e^{i\gamma\log T}A^\dagger\right)+o(T^{1-\alpha}),
\qquad
\lim_{T\to\infty}\frac{\|S_\beta(T)\|_2}{T^{1-\alpha}}=\sqrt2\,\|A\|_2>0.
\]

**(ii) Bounded, nonconvergent critical coherence.** At \(\beta=\beta_*\), use the same \(B,A\) with \(a=1+ir/\Delta\) and \(\gamma=r/\Delta\). There is a fixed Hermitian matrix \(C\) such that
\[
S_{\beta_*}(T)=C+e^{-i\gamma\log T}A+e^{i\gamma\log T}A^\dagger+o(1).
\]
Its exact accumulation set is the nondegenerate circle
\[
\left\{C+e^{-i\theta}A+e^{i\theta}A^\dagger:\theta\in[0,2\pi)\right\},
\]
of Hilbert–Schmidt radius \(\sqrt2\|A\|_2\) about \(C\). Its period in \(\log T\) is \(2\pi\Delta/r\). Thus the accumulated operator is bounded but has no limit.

**(iii) Absolutely convergent accumulated coherence.** For \(\beta>\beta_*\), \(\int_0^\infty\|\rho_\beta(t)-\rho_\infty\|_2dt<\infty\), and the limit has the exact spectral-block expression
\[
\boxed{\displaystyle
S_\beta(\infty)=\sum_{E\ne F}
\frac{\beta-1}{-r+i(\beta-1)(E-F)}P_E\rho_0P_F.}
\]
It obeys the **strict integrated coherence sign law**
\[
\boxed{\displaystyle
\operatorname{tr}[(\rho_0-\rho_\infty)S_\beta(\infty)]
=-2r(\beta-1)\sum_{E>F}\frac{\|P_E\rho_0P_F\|_2^2}
{r^2+(\beta-1)^2(E-F)^2}<0.}
\]
If \([H,\rho_0]=0\), then \(\rho_\beta(t)=\rho_0=\rho_\infty\) and \(S_\beta(T)=0\) for all \(\beta,T\); no threshold is asserted in this stationary case.

## Assumptions and scope

The Hilbert space has finite dimension at least two. \(H\) is time-independent and Hermitian, with arbitrary finite real spectrum, including possible degeneracies. The initial density operator \(\rho_0\) is positive semidefinite, trace one, and Hermitian. The scalar intensity \(r\) and power-history parameter \(\beta\) are strictly positive. The reset process is understood in the same ensemble-history sense as quantum preferential relocation: the selected past state belongs to the system's realized history, and the past-time sampling law is independent of the state given \(t\). The resulting linear ensemble equation is
\[
\frac{d\rho_\beta}{dt}=-i[H,\rho_\beta(t)]-r\rho_\beta(t)+r\int_0^t K_\beta(s,t)\rho_\beta(s)\,ds,
\qquad \rho_\beta(0)=\rho_0.
\]
Finite-dimensionality, a time-independent Hamiltonian, and this exact history-sampling rule are essential. No claim is made about arbitrary nonlinear quantum feedback or infinite-dimensional gapless spectra. All norms \(\|\cdot\|_2\) are Hilbert–Schmidt norms.

## Proof

**1. Spectral reduction and exact scalar solution.** For any ordered pair of distinct energies, define \(\omega=E-F\) and let \(f_\beta(\omega,t)\) multiply the matrix block \(P_E\rho_0P_F\). The evolution equation gives
\[
f'(t)=-(r+i\omega)f(t)+r\beta t^{-\beta}\int_0^t s^{\beta-1}f(s)\,ds,
\qquad f(0)=1.
\]
Since the history kernel integrates to one, \(f'(0)=-i\omega\). Differentiating after multiplication by \(t^\beta\) yields
\[
t f''(t)+[\beta+(r+i\omega)t]f'(t)+i\beta\omega f(t)=0.
\]
Setting \(z_\omega=r+i\omega\) and \(a_\omega=i\beta\omega/z_\omega\), the unique solution analytic at zero is
\[
f_\beta(\omega,t)={}_1F_1(a_\omega;\beta;-z_\omega t).
\]
The frequency-zero blocks are constant; hence \(\rho_\infty=\sum_E P_E\rho_0P_E\). The Kummer scalar formula is a complex-mode extension of the classical preferential-relocation formula of Boyer, Evans and Majumdar (2025), Section 5.1, and is **used here as a prior-work-derived lemma**, not claimed as the new discovery.

**2. Precise complex-power asymptotics.** For every nonzero \(\omega\),
\[
\operatorname{Re}a_\omega=\frac{\beta\omega^2}{r^2+\omega^2}>0,
\qquad \operatorname{Re}(\beta-a_\omega)=\frac{\beta r^2}{r^2+\omega^2}>0.
\]
Therefore Euler's integral is valid without analytic continuation of an improper integral:
\[
f_\beta(\omega,t)=\frac{\Gamma(\beta)}{\Gamma(a_\omega)\Gamma(\beta-a_\omega)}
\int_0^1e^{-z_\omega tu}u^{a_\omega-1}(1-u)^{\beta-a_\omega-1}du.
\]
As \(t\to\infty\), the endpoint \(u=0\) is the dominant contribution because \(\operatorname{Re}z_\omega=r>0\). Scaling \(u\) by \(t\), expanding the smooth factor near zero, and bounding the complementary endpoint exponentially gives
\[
f_\beta(\omega,t)=B_\omega t^{-a_\omega}+O(t^{-\operatorname{Re}a_\omega-1})+O(e^{-rt/2}),
\quad B_\omega=\frac{\Gamma(\beta)}{\Gamma(\beta-a_\omega)}z_\omega^{-a_\omega}.
\]
The gamma function has no zero, and its denominator here has positive real part, so \(B_\omega\ne0\). In a finite-dimensional spectral expansion, the remainder estimates can be summed over all active frequencies. The decay exponents \(\operatorname{Re}a_\omega\) increase strictly with \(|\omega|\), so the smallest active gap \(\Delta\) alone governs the leading accumulated coherence.

**3. Subcritical growth.** With \(\alpha=\operatorname{Re}a_\Delta<1\), integration of the leading term gives \(B_\Delta T^{1-a_\Delta}/(1-a_\Delta)\) plus a lower-order term. Contributions from all larger active gaps are \(o(T^{1-\alpha})\), even if some are themselves slowly decaying, and conjugate negative-gap blocks combine into the Hermitian expression in (i). Let \(M=\sum_{E-F=\Delta}P_E\rho_0P_F\). Ordering the energy eigenspaces shows that \(M\) (and therefore \(A\)) is strictly triangular; in particular, \(\operatorname{tr}(A^2)=0\). Consequently, for every real \(\theta\),
\[
\|e^{-i\theta}A+e^{i\theta}A^\dagger\|_2^2
=2\|A\|_2^2+2\operatorname{Re}(e^{-2i\theta}\operatorname{tr}A^2)=2\|A\|_2^2.
\]
This proves the nonzero, phase-independent norm coefficient.

**4. Critical cluster circle.** At \(\beta=\beta_*\), \(a_\Delta=1+i\gamma\), \(\gamma=r/\Delta>0\). The leading integral \(\int_1^T t^{-1-i\gamma}dt=(T^{-i\gamma}-1)/(-i\gamma)\) remains bounded and rotates forever. The error in step 2 is absolutely integrable, as are the contributions from every larger active gap, whose real exponent is strictly greater than one. All nonoscillatory pieces therefore converge to one fixed Hermitian \(C\). The strictly triangular geometry from step 3 makes the phase curve a circle of radius \(\sqrt2\|A\|_2\), not a generic ellipse. Every angle is approached along \(T_n=\exp[(\theta+2\pi n)/\gamma]\) after adjusting the phase sign, and no other accumulation points occur. Since \(A\ne0\), convergence is impossible.

**5. Supercritical integral and sign law.** If \(\beta>\beta_*\), every active frequency has \(\operatorname{Re}a_\omega>1\). The finite sum of scalar decays is absolutely integrable in Hilbert–Schmidt norm. Apply Fubini to the Euler representation: \(\int_0^\infty e^{-z_\omega tu}dt=(z_\omega u)^{-1}\). The remaining beta integral converges because \(\operatorname{Re}a_\omega>1\). Thus
\[
\begin{aligned}
\int_0^\infty f_\beta(\omega,t)dt
&=\frac{\Gamma(\beta)}{z_\omega\Gamma(a_\omega)\Gamma(\beta-a_\omega)}
B(a_\omega-1,\beta-a_\omega)\\
&=\frac{\beta-1}{z_\omega(a_\omega-1)}
=\frac{\beta-1}{-r+i(\beta-1)\omega}.
\end{aligned}
\]
Collecting spectral blocks proves the rational sum rule. Pairing \(\omega\) with \(-\omega\) and taking the real part proves the negative quadratic response: each term is strictly negative and at least one active block is nonzero. This completes the trichotomy.

## Verification

The standalone `verify.py` uses `mpmath` 1.3.0 at 48 decimal digits to check the scalar ODE and initial derivative, Euler versus Kummer representations, complex conjugacy, the convergent beta-integral identity, the decay exponent and critical phase, leading asymptotics, one direct infinite-time integral, and the exact three-level matrix circle. Running `python verify.py` with the accompanying `requirements.txt` completed **151 deterministic checks** without an exception. Such finite computations corroborate formulas but do not establish asymptotic or universal claims; steps 1–5 above carry the proof.

## Relationship to prior work

The 2026 quantum-memory-reset paper by de Mauro, Kulkarni and Majumdar derives the full finite-dimensional eigenbasis dynamics for **uniform past-time selection** (the special case \(\beta=1\)) and its algebraic/log-periodic relaxation. Its discussion explicitly leaves nonuniform memory kernels open. Boyer, Evans and Majumdar's 2025 **classical** confining-diffusion paper already derives the scalar Kummer mode with a power-law history integral and a **real positive** relaxation eigenvalue. Substituting a purely imaginary quantum frequency into that scalar solution is straightforward and is **not** an originality claim here. The additional mathematical statement concerns the observable time-integrated **Hermitian quantum coherence operator**: its sharp state-dependent threshold, critical nonconvergent circle, exact convergent operator sum, and universal negative accumulated self-overlap. The older classical real-spectrum results do not assert these complex spectral and operator features. Earlier works on diffusive preferential relocation and non-Markovian quantum reset dynamics give surrounding context but no identified full implication to this operator trichotomy. Publication priority is not guaranteed by a finite literature search, and general complex-mode continuation results remain a residual risk.

## Limitations

This is a theorem only for a fixed finite-dimensional Hamiltonian and the specified history distribution, with strictly positive \(r\) and \(\beta\). A state without active energy coherences has the trivial zero response. The threshold depends on the smallest **initially active** energy difference, not necessarily the Hamiltonian's absolute smallest spacing. It is not a classification for continuous spectra, nonlinear feedback, time-dependent Hamiltonians, or an experimentally verified reset implementation. The phase is logarithmic in time and its fitted offset is not claimed to be independent of the initial state. Search comparisons provide qualified originality rather than proof of publication priority. No independent audit has been performed.

## References

1. G. de Mauro, M. Kulkarni, S. N. Majumdar, *Quantum resetting with memory*, arXiv:2608.02297 (first posted 2026-08-03). https://arxiv.org/abs/2608.02297
2. D. Boyer, M. R. Evans, S. N. Majumdar, *Diffusion with preferential relocation in a confining potential*, arXiv:2411.00641 (first posted 2024-11-01), especially Section 5.1, equations (44)–(50). https://arxiv.org/html/2411.00641
3. D. Boyer, M. R. Evans, S. N. Majumdar, *Long time scaling behaviour for diffusion with resetting and memory*, arXiv:1611.06743 (2016). https://arxiv.org/abs/1611.06743
4. F. Carollo, S. Wald, *Stochastic resetting induces quantum non-Markovianity*, arXiv:2601.13367 (2026). https://arxiv.org/abs/2601.13367

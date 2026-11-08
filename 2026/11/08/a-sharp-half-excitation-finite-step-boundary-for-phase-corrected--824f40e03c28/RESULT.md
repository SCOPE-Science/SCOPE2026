# A sharp half-excitation finite-step boundary for phase-corrected collisional quantum charging

## Finding
Consider sequential exchange collisions between a fixed pure charger qubit and a pure battery qubit. In addition to adaptive rank-one measurement of the spent charger, permit outcome-conditioned rotations of the battery **about its energy axis**. These rotations commute with its bare Hamiltonian, preserve its instantaneous expected energy, and align the phases of the two conditional pure states. This produces identical battery states, not merely identical energies, across all measurement histories.

Theorem. Let the charger excitation be \(\beta\in(0,1)\), and let the fixed exchange-collision probability be \(\eta\in(0,1)\), as defined below. Every next battery excitation probability in the closed interval
\[
F_-(e)\le e'\le F_+(e),\qquad
F_\pm(e)=(1-\eta)e+\eta\beta\pm2\sqrt{\eta(1-\eta)\beta(1-\beta)e(1-e)}
\]
is exactly realizable by a phase choice, an adaptive projective measurement, and conditional energy-axis rotations. The battery conditional mean energy equals \(\omega_b e'\) on every branch.

Write \(s=\sqrt{1-\eta}\). The full interval of excitation probabilities that can be **held constant at every collision** using these controls is exactly
\[
\boxed{\quad e\in[p_-,p_+],\qquad
p_\pm=\frac{\beta(1\pm s)}{1\pm s(2\beta-1)}.\quad}
\]
In particular, \(p_+>\beta\) is the largest sustainable deterministic population. Beginning with an empty battery, \(e_0=0\), there exists a zero-trajectory-dispersion protocol that attains and thereafter holds \(p_+\) in a **finite** number of collisions if and only if \(\beta>1/2\). For \(\beta\le1/2\), \(p_+\) is approachable but is not attained in finitely many collisions by any protocol with the stated controls and fixed collision parameters.

A constructive policy sets
\[
e_{n+1}=\min\{F_+(e_n),p_+\}.
\]
For \(0<\beta<1/2\), its strictly positive errors \(\delta_n=p_+-e_n\) have the asymptotic law
\[
\delta_{n+1}=s(1-2\beta)\delta_n+O(\delta_n^2).
\]
At the critical charger excitation \(\beta=1/2\), convergence is instead quadratic:
\[
\delta_{n+1}=\frac{s}{\eta}\delta_n^2+O(\delta_n^3).
\]
For \(1/2<\beta<1\), the same policy reaches \(p_+\) exactly after finitely many collisions. Thus the sharp threshold is independent of detuning and interaction duration once \(0<\eta<1\) is fixed.

## Assumptions and scope
Let \(\omega_a,\omega_b,g,\tau>0\), \(\Delta=\omega_b-\omega_a\), and
\[
H=\omega_a|1\rangle\langle1|_a+\omega_b|1\rangle\langle1|_b+g(\sigma_a^-\sigma_b^++\sigma_a^+\sigma_b^-),
\quad \Omega=\sqrt{g^2+(\Delta/2)^2},\quad
\eta=\frac{g^2}{\Omega^2}\sin^2(\Omega\tau).
\]
Assume \(0<\eta<1\). Each fresh charger has the same pure state \(\sqrt{1-\beta}|0\rangle+\sqrt\beta|1\rangle\), with \(0<\beta<1\). The battery begins in the pure ground state for the reachability conclusion. After each collision of duration \(\tau\), the charger is projectively measured in an adaptively chosen orthonormal basis. The outcome is known and the battery may be rotated by an outcome-dependent diagonal unitary \(\operatorname{diag}(1,e^{i\varphi})\). Its phase may likewise be chosen before the next collision. No population-changing battery gate, varying charger state, post-selection, or changing collision time is allowed. The statements concern variance across **conditional mean stored energies**, not the intrinsic variance of a subsequent projective battery-energy measurement. They do not include the energetic cost of measurement, record processing, or switching interactions.

## Proof
**1. Energy-equalizing measurement and phase alignment.** Following a collision the joint charger–battery state \(|\Psi\rangle\) is pure. Let \(\rho_a=\operatorname{Tr}_b|\Psi\rangle\langle\Psi|\), and let \(A_a=\operatorname{Tr}_b[(I_a\otimes |1\rangle\langle1|_b)|\Psi\rangle\langle\Psi|]\). Put \(p=\operatorname{Tr}(A_a)\). Then \(T=A_a-p\rho_a\) is a traceless Hermitian two-by-two matrix. There is a real orthonormal basis \(\{|k_0\rangle,|k_1\rangle\}\) in which its diagonal vanishes: writing the Bloch vector of \(T\) as \((t_x,t_y,t_z)\), select a measurement axis in the real \(xz\)-meridian orthogonal to \((t_x,t_z)\); if both components vanish, any real axis works. Therefore, for each outcome \(j\) of nonzero probability \(q_j=\langle k_j|\rho_a|k_j\rangle\), the normalized battery state has excitation
\[
\frac{\langle k_j|A_a|k_j\rangle}{q_j}=p.
\]
Because a rank-one measurement on one side of a pure two-qubit state yields a pure conditional state, both battery branches have the form \(\sqrt{1-p}|0\rangle+e^{i\alpha_j}\sqrt p|1\rangle\) up to global phase. Outcome-conditioned diagonal battery unitaries align these phases to any predetermined target phase, including the trivial cases \(p=0\) or \(1\) where the phase is immaterial. Thus both branches become the same state. Repeating this operation removes all trajectory dispersion of the conditional battery state and its mean energy.

**2. Exactly attainable population interval.** Write the battery state before collision as \(\sqrt{1-e}|0\rangle+e^{i\alpha}\sqrt e|1\rangle\). The \(|01\rangle,|10\rangle\) block of the Hamiltonian has half-splitting \(\Delta/2\) and off-diagonal coupling \(g\). Direct evolution and partial trace give
\[
\begin{split}
p={}&(1-\eta)e+\eta\beta\\
&+2\frac g\Omega\sin(\Omega\tau)\sqrt{\beta(1-\beta)e(1-e)}\left[\frac{\Delta}{2\Omega}\sin(\Omega\tau)\cos\alpha-\cos(\Omega\tau)\sin\alpha\right].
\end{split}
\]
The bracket has maximum absolute magnitude \(\sqrt{1-\eta}\), since \(\cos^2(\Omega\tau)+[\Delta\sin(\Omega\tau)/(2\Omega)]^2=1-\eta\). Varying \(\alpha\) therefore yields precisely the interval \([F_-(e),F_+(e)]\), including its endpoints. Step 1 then equalizes both outcomes and resets the phase for the next collision. This proves sufficiency and necessity of the interval for the allowed controls.

**3. Exact sustainable-population endpoints.** Maintaining \(e'=e\) is possible exactly if
\[
\left|\eta(e-\beta)\right|\le 2\sqrt{\eta(1-\eta)\beta(1-\beta)e(1-e)}.
\]
Squaring, using \(0<\eta,\beta<1\), and solving the resulting quadratic gives the two roots \(p_-=\beta(1-s)/[1-s(2\beta-1)]\) and \(p_+=\beta(1+s)/[1+s(2\beta-1)]\). The denominators are strictly positive. The nonnegative quadratic inequality holds precisely on \([p_-,p_+]\). Moreover \(p_-<\beta<p_+<1\). The upper endpoint is thus sharp: at every \(e>p_+\), even the best available phase gives \(F_+(e)<e\), ruling out a higher fixed population. This statement is about a sustainable constant population, not an upper bound on every transient overshoot.

**4. Finite attainment and its threshold.** On \([0,p_+)\), one has \(F_+(e)>e\), and \(F_-(e)\le (1-\eta)e+\eta\beta<p_+\) for \(e\le p_+\). Thus every step of the clipped policy is physically attainable and strictly increases the excitation until the target is reached. If no step reaches \(p_+\), the increasing bounded sequence converges to a fixed point of \(F_+\), whose only root in \([0,1]\) is \(p_+\). Writing \(k=\sqrt{\eta(1-\eta)\beta(1-\beta)}\) gives
\[
F'_+(e)=1-\eta+k\frac{1-2e}{\sqrt{e(1-e)}},\qquad
F''_+(e)=-\frac{k}{2[e(1-e)]^{3/2}}<0.
\]
Substituting \(p_+\), and \(p_+(1-p_+)=\eta\beta(1-\beta)/[1+s(2\beta-1)]^2\), yields the key exact identity
\[
\boxed{F'_+(p_+)=s(1-2\beta).}
\]
If \(\beta>1/2\), this derivative is negative, so \(F_+(e)>p_+\) for all \(e<p_+\) sufficiently close to \(p_+\). Any increasing sequence tending to \(p_+\) must enter that neighborhood and hence reaches \(p_+\) at the next clipped step, a contradiction to nonattainment. Conversely, if \(\beta\le1/2\), strict concavity and \(F'_+(p_+)\ge0\) make \(F_+\) strictly increasing on \([0,p_+]\). Hence \(F_+(e)<p_+\) whenever \(e<p_+\). No allowed phase choice can attain \(p_+\) in finitely many steps from \(e_0=0\). For \(\beta<1/2\), Taylor expansion at the endpoint gives the stated linear error rate. At \(\beta=1/2\), the linear term vanishes, and the second derivative above gives \(-F''_+(p_+)/2=s/\eta\), proving the quadratic error law.

## Verification
An included standalone Python program checks the exact fixed-point and derivative identities for 56 rational Pythagorean parameter pairs (168 exact-rational checks); it also compares the excitation formula with 450 independently built resonant two-qubit unitaries and verifies energy equalization for both measured charger outcomes. Another 250 nonresonant unitary calculations independently reproduce the interference formula. A constructive example, \(\beta=4/5\) and \(\eta=1/2\), reaches its exact sustainable ceiling in three collisions under the clipped policy. All checks pass. The global quantifiers and sharp threshold follow from the proof, not from finite tests.

To reproduce: install Python 3 and NumPy, then run `python check.py` in the directory containing this document and the verifier. No network access is required.

## Relationship to prior work
Gong, Zhang and Li (arXiv:2610.01332, first submitted October 1, 2026) established the adaptive charger measurement, phase-dependent one-step excitation formula and zero trajectory-energy dispersion for *excited-state* chargers. They observed remaining phase-driven dispersion with superposition chargers under their measurement-only protocol. The additional outcome-conditioned diagonal battery feedback considered here is a distinct allowed operation; it collapses the phase branches. The new sharp constant-population interval and the universal \(\beta=1/2\) finite-attainment boundary follow from solving the resulting controlled dynamics, not from an assertion that the published measurement-only result is incorrect.

The same authors' arXiv:2610.31242 concerns a two-qubit charger and classifications of phase-blind charger states under adaptive measurement; it does not supply the one-qubit phase-corrected reachability boundary considered here. Mitchison, Goold and Prior (arXiv:2012.00350) analyze continuous homodyne feedback to a driven-dissipative charger rather than discrete outcome-conditioned energy-axis rotations of a pure battery. Li and collaborators (Phys. Rev. A 113, 052437, 2026) study fixed coherent ancilla phases and ergotropy in a multilevel model; that article was only accessible at abstract level in this comparison. General measurement/feedback and coherence-control theory provide conceptual precedents, and the precise publication-priority claim remains provisional.

## Limitations
Only pure fixed chargers, pure conditional battery states, ideal rank-one charger readout, perfectly known outcomes, and unrestricted instantaneous diagonal phase gates are included. The result does not hold without the phase-feedback resource in general, and it makes no claim for mixed chargers, noisy feedback, unobserved outcomes, varying collision strengths, or many-level batteries. The mathematical zero-dispersion statement refers to trajectories of **conditional mean energy**; intrinsic projective energy-readout randomness persists for \(0<e<1\). A diagonal battery gate preserves its bare expected energy but measurement, feedback electronics, charger preparation, and interaction switching may incur thermodynamic costs. The ceiling \(p_+\) bounds sustainable constant excitation, not arbitrary one-step overshoots. The case \(\eta=0\) or \(\eta=1\) and exactly \(\beta=0\) or \(1\) is excluded. Independent scientific validation and complete publication-priority certification have not been performed.

## References
1. L. Gong, J. Zhang and Y. Li, *Achieving Identical Stored Energy in Cascaded Collisional Quantum Battery Charging: Analytical Results*, arXiv:2610.01332 (2026), https://arxiv.org/html/2610.01332.
2. L. Gong, J. Zhang and Y. Li, *Fluctuation-free Quantum Battery Charging Enabled by Bell-like Entangled and Separable Charger States*, arXiv:2610.31242 (2026), https://arxiv.org/abs/2610.31242.
3. M. T. Mitchison, J. Goold and J. Prior, *Charging a quantum battery with linear feedback control*, Quantum 5, 500 (2021), https://arxiv.org/html/2012.00350v3.
4. H. Li, X. Chen, W. Yu and Y. Hao, *Charging optimization of quantum battery via phase-controlled coherent ancillae*, Phys. Rev. A 113, 052437 (2026), https://doi.org/10.1103/39yj-zgwf.
5. A. H. A. Malavazi, B. Ahmadi, P. Horodecki and P. R. Dieguez, *Charge-Preserving Operations in Quantum Batteries*, arXiv:2510.25549 (2025), https://arxiv.org/abs/2510.25549.

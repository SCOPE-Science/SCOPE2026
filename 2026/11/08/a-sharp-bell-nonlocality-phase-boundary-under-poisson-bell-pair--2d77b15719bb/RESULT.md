# A sharp Bell-nonlocality phase boundary under Poisson Bell-pair reinitialization and local decoherence

## Finding

A pair of qubits undergoes independent zero-temperature amplitude damping, independent local pure dephasing, and simultaneous Poisson reinitialization into the Bell state \(\lvert\Phi^+\rangle=(\lvert00\rangle+\lvert11\rangle)/\sqrt2\). Although the system is not driven by a Hamiltonian between resets, a unique positive reset-rate threshold separates its Bell-local and CHSH-violating stationary states. The optimal CHSH witness changes type at an exactly defined positive dephasing-to-relaxation ratio. At strong dephasing, the smallest rate permitting CHSH violation scales as the two-thirds power of the dephasing strength.

Let \(\gamma>0\) be the identical amplitude-damping rate at each site, \(\kappa\ge0\) the coefficient of each dissipator \(\kappa(Z_j\rho Z_j-\rho)\), and \(r>0\) the global Poisson reinitialization rate. Set
\[
 x=\frac r\gamma,\qquad b=1+\frac{4\kappa}{\gamma}\ge1,\qquad
 u=\frac{x}{x+b},\qquad v=\frac{x^2+x+2}{(x+1)(x+2)}.
\]
The unique stationary state has maximized CHSH value
\[
 S_{\max}(x,b)=2\sqrt{u^2+\max\{u^2,v^2\}}.
\]
Define
\[
 P_b(x)=x^5+2x^4+(5-8b)x^3+(4-4b^2-16b)x^2
 +(4-8b^2-16b)x-8b^2.
\]
For each \(b\ge1\), this polynomial has exactly one positive root \(\xi_b\). The CHSH threshold is
\[
 X(b)=\min\big\{(1+\sqrt2)b,\xi_b\big\},\qquad
 S_{\max}(x,b)>2\ \Longleftrightarrow\ x>X(b).
\]
For \(0<x<X(b)\), one has \(S_{\max}<2\), and \(S_{\max}=2\) exactly at the positive threshold.

The two mechanisms for reaching the threshold exchange dominance once. Let \(z_0\) be the unique solution greater than \(\sqrt2\) of
\[
 \frac{z_0^2+z_0+2}{(z_0+1)(z_0+2)}=\frac1{\sqrt2};
 \qquad z_0=3.20425757804585\ldots
\]
and let \(b_c=z_0/(1+\sqrt2)=1.327246946163\ldots\). Then
\[
 X(b)=\begin{cases}(1+\sqrt2)b,&1\le b\le b_c,\\
 \xi_b,&b\ge b_c.
 \end{cases}
\]
The two branches agree at \(b=b_c\). In particular \(X(1)=1+\sqrt2\), and
\[
 \lim_{b\to\infty}\frac{X(b)}{b^{2/3}}=4^{1/3}.
\]
Equivalently, in the limit \(\kappa/\gamma\to\infty\), the physical threshold satisfies \(r_{\mathrm{CHSH}}\sim4\gamma^{1/3}\kappa^{2/3}\).

For comparison, Wootters concurrence of the *same stationary state* is
\[
 C(x,b)=\frac{x\,[x^2+2x+2-b]_+}{(x+b)(x+1)(x+2)},
 \qquad [y]_+=\max\{0,y\}.
\]
It is positive for all \(x>0\) if \(1\le b\le2\), and for \(x>\sqrt{b-1}-1\) if \(b>2\). The CHSH condition is strictly stronger than the entanglement condition. For large \(b\), the entanglement-onset rate grows as \(b^{1/2}\), whereas the CHSH-onset rate grows as \(b^{2/3}\).

## Assumptions and scope

The two-qubit density operator is written in the computational basis \((\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle)\). Between resets it evolves under the Markovian generator
\[
 \mathcal L_0(\rho)=\sum_{j=1}^2\gamma\left(\sigma_-^{(j)}\rho\sigma_+^{(j)}
 -\tfrac12\{\sigma_+^{(j)}\sigma_-^{(j)},\rho\}\right)
 +\sum_{j=1}^2\kappa(Z_j\rho Z_j-\rho).
\]
The two reservoirs are independent, both amplitude-damping rates equal \(\gamma>0\), both dephasing coefficients equal \(\kappa\ge0\), and there is no Hamiltonian or thermal upward jump. At rate \(r>0\), both qubits are jointly and instantaneously replaced by \(\rho_0=\lvert\Phi^+\rangle\langle\Phi^+\rvert\), independent of their pre-reset state and the environment. The reported CHSH maximum optimizes over local dichotomic projective observables on a single copy of the unconditional stationary density matrix, with no filtering or postselection. Time and all rate parameters have consistent units.

## Proof

**1. Stationary state.** Regeneration at Poisson events gives the unique unconditional stationary state
\[
 \bar\rho=r\int_0^\infty e^{-rt}e^{t\mathcal L_0}(\rho_0)\,dt.
\]
For the unreset evolution, writing \(q_t=\rho_{01,01}(t)=\rho_{10,10}(t)\), \(w_t=\rho_{11,11}(t)\), and \(c_t=\rho_{00,11}(t)\), the Lindblad equations give
\[
 q_t=\tfrac12(e^{-\gamma t}-e^{-2\gamma t}),\quad
 w_t=\tfrac12 e^{-2\gamma t},\quad
 c_t=\tfrac12e^{-(\gamma+4\kappa)t}.
\]
All other off-diagonal entries vanish. Performing the positive exponential integrals yields the X-state
\[
 \bar\rho=\begin{pmatrix}
 1-2q-w&0&0&c\\0&q&0&0\\0&0&q&0\\c&0&0&w
 \end{pmatrix},\qquad
 q=\frac{x}{2(x+1)(x+2)},\quad
 w=\frac{x}{2(x+2)},\quad c=\frac{x}{2(x+b)}.
\]
This is positive and trace-one because it is the integral of physical density matrices. Uniqueness follows from complete reinitialization at a positive rate (the contribution of any initial state without a reset is bounded by \(e^{-rt}\) in trace norm).

**2. Exact CHSH criterion.** The real Pauli-correlation matrix of \(\bar\rho\) is diagonal, with diagonal entries \((2c,-2c,1-4q)=(u,-u,v)\). By the necessary-and-sufficient two-qubit CHSH criterion of Horodecki et al., the maximum CHSH value is twice the square root of the sum of the two largest eigenvalues of \(T^{\mathsf T}T\), proving the displayed \(S_{\max}\). Both \(u\) and \(v\) lie strictly between zero and one for \(x>0\). Therefore the CHSH inequality is violated exactly when
\[
 2u^2>1\quad\text{or}\quad u^2+v^2>1.
\]
The first inequality is equivalent to \(x>(1+\sqrt2)b\). Direct expansion of the second gives the exact identity
\[
 1-u^2-v^2=-\frac{x P_b(x)}{(x+b)^2(x+1)^2(x+2)^2}.
\]
For every \(b\ge1\), the coefficients of \(P_b\) in descending order have signs \((+,+,-,-,-,-)\); the third coefficient is \(5-8b\le-3\), and the remaining negative coefficients are strictly negative as well. Descartes' rule permits at most one positive root counting multiplicities. Since \(P_b(0)=-8b^2<0\) and \(P_b(x)\to+\infty\), the root exists, is simple, and is unique. Consequently \(u^2+v^2>1\) if and only if \(x>\xi_b\). Taking the union of the two strict half-lines proves the unique threshold and the strict inequality below it.

**3. Switching of the controlling witness.** Differentiate \(v\) to obtain
\[
 \frac{dv}{dx}=\frac{2(x^2-2)}{(x+1)^2(x+2)^2}.
\]
The first candidate threshold \(x_1=(1+\sqrt2)b\) is at least \(1+\sqrt2>\sqrt2\), where \(v\) is strictly increasing. At \(x_1\), \(u=1/\sqrt2\); hence the second CHSH branch already violates exactly when \(v(x_1)>1/\sqrt2\). The strictly increasing function \(v\) on \([1+\sqrt2,\infty)\) crosses \(1/\sqrt2\) once at \(z_0\), which exists because its value at \(1+\sqrt2\) is less than \(1/\sqrt2\) while its limit is one. This gives the stated sharp \(b_c\) and the two cases. Equivalently, \(z_0\) is the larger positive root of \(z^4-2z^3-3z^2-4z+4=0\).

**4. Strong-dephasing asymptotic.** For \(b>b_c\), the threshold is the unique positive root of \(P_b\). Substitute \(x=b^{2/3}y\) and divide the polynomial by \(b^{10/3}\). For each fixed \(y>0\), its limit is \(y^5-4y^2\). This is negative below \(y=4^{1/3}\) and positive above it. The uniqueness of the positive root of \(P_b\) and the intermediate-value theorem squeeze \(\xi_b/b^{2/3}\) to \(4^{1/3}\). The physical-rate form follows from \(b=1+4\kappa/\gamma\).

**5. Comparison with entanglement.** The standard X-state evaluation of Wootters concurrence gives \(C=2[c-\sqrt{\rho_{01,01}\rho_{10,10}}]_+=2[c-q]_+\), since the other X-state concurrence candidate is nonpositive. Substituting the stationary entries gives the displayed formula and the unique positive entanglement onset (when it exists). CHSH violation implies entanglement by the Bell inequality criterion. To establish a strict gap for \(b>2\), at its positive concurrence-onset point \(c=q\) put \(u=2c=2q\in(0,1/2)\), so \(v=1-2u\). Then \(2u^2<1\) and \(u^2+v^2=1-4u+5u^2<1\), proving strict CHSH locality at entanglement onset. For \(b\le2\), concurrence is positive at every positive reset rate while the CHSH threshold remains strictly positive. The strong-dephasing entanglement threshold is \(\sqrt{b-1}-1\sim b^{1/2}\), strictly smaller in order than \(X(b)\sim4^{1/3}b^{2/3}\).

## Verification

Run `python checker.py` with SymPy, NumPy and SciPy. The standalone program checks exact symbolic factorizations, independently solves the full 16-dimensional stationary Lindblad equation (including three exact-rational generator inversions), computes concurrence from the spin-flip eigenvalues, computes the optimized CHSH value from the eigenvalues of the real Pauli-correlation matrix, and checks threshold branches and asymptotic witnesses. The packaged checker passed **491 assertions**. The continuum uniqueness, global parameter bounds and asymptotic statements are analytic consequences of the proof; finite parameter tests alone would not establish them.

For example, at \(b=1\), \(X(1)=1+\sqrt2=2.41421356237\ldots\). At \(b=2\), \(X(2)=\xi_2=4.15077024316\ldots\), and the witness branch switches at \(b_c=1.32724694616\ldots\).

## Relationship to prior work

Kulkarni and Majumdar (2023) develop Poisson resetting and stationary entanglement for an interacting **closed** two-spin Hamiltonian; their setup resets to a product state and calculates concurrence, not a CHSH phase diagram under local dissipative loss. Carollo, Lesanovsky and Garrahan (2023) establish a general **open**-system reset generator and study universal ordering statistics of trajectories, rather than optimized Bell inequalities. Wald et al. (2024, first posted 15 October 2024) analyze discrete-time reset-induced correlations under unitary gates, not continuous Lindblad amplitude damping and dephasing. Murauer et al. (2026) treat a discrete-time transverse-field Ising reset system and simulated depolarizing noise; their model and observables do not produce the present all-parameter CHSH threshold. The classical Horodecki two-qubit CHSH theorem and Wootters concurrence formula are used, not claimed as new. General Lindblad reset resolvents plus these standard criteria could indirectly support a derivation of these formulas; the contribution assessed here is the **sharp complete global classification, change of active CHSH witness, and strong-dephasing \(2/3\)-power law** for the explicitly specified open Bell-reset model.

## Limitations

The theorem assumes exactly symmetric local damping and dephasing, zero-temperature amplitude damping, ideal global Bell reinitialization, and a memoryless reset clock. It does not classify general Hamiltonian couplings, asymmetric decay, finite-temperature baths, local-only resets, non-Poisson interarrival distributions, filtered hidden nonlocality, loophole-free experimental tests, or measurement noise. It does not claim the underlying stationary-reset formula, CHSH criterion, or concurrence formula as new. No independent validation or publication-priority certification has been performed; an implicit derivation from existing general channel methods remains possible.

## References

- M. Kulkarni and S. N. Majumdar, *Generating Entanglement by Quantum Resetting*, arXiv:2307.07485, first public 2023-07-14, https://arxiv.org/abs/2307.07485.
- F. Carollo, I. Lesanovsky and J. P. Garrahan, *Universal and nonuniversal probability laws in Markovian open quantum dynamics subject to generalized reset processes*, arXiv:2310.06981, first public 2023-10-10, https://arxiv.org/html/2310.06981v2.
- S. Wald et al., *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497, first public 2024-10-15, https://arxiv.org/abs/2410.11497.
- J. Murauer et al., *Entanglement diagnostics of stochastic-resetting steady states: theory and measurement on superconducting qubits*, arXiv:2610.40638, first public 2026-10-29, https://arxiv.org/abs/2610.40638.
- R. Horodecki, P. Horodecki and M. Horodecki, *Violating Bell inequality by mixed spin-1/2 states: necessary and sufficient condition*, Phys. Lett. A 200 (1995), https://doi.org/10.1016/0375-9601(95)00214-N.
- W. K. Wootters, *Entanglement of Formation of an Arbitrary State of Two Qubits*, Phys. Rev. Lett. 80 (1998), https://doi.org/10.1103/PhysRevLett.80.2245.

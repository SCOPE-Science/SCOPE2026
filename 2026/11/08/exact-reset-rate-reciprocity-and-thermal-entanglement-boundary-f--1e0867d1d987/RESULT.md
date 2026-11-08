# Exact reset-rate reciprocity and thermal entanglement boundary for a dephased qubit pair

## Finding
Consider two qubits coupled only by coherent pair conversion and independently subject to local dephasing. A Poisson event at rate \(r>0\) replaces their **joint** density matrix by the same fixed, diagonal separable preparation. Let \(J>0\) be the pair-conversion matrix element, let \(\gamma_1,\gamma_2\ge0\) be the dephasing coefficients defined below, and let the preparation probabilities \(a,b,c,d\ge0\) sum to one. Put
\[
\Gamma=2(\gamma_1+\gamma_2),\qquad \Delta=a-d,\qquad h=\sqrt{bc},\qquad D_r=r(r+\Gamma)+4J^2.
\]
The system has a unique stationary density matrix, whose exact Wootters concurrence is
\[
\boxed{C(r)=2\left[\frac{J|\Delta|r}{D_r}-h\right]_+,\qquad [x]_+=\max(x,0).}
\]
Its complete entanglement phase diagram and reset-rate optimum are as follows.

1. If \(h>0\), entanglement occurs at some positive reset rate **if and only if** \(J|\Delta|>h(4J+\Gamma)\). In this case it occurs on exactly one open interval \((r_-,r_+)\), where
\[
\boxed{r_\pm=\frac{J|\Delta|-\Gamma h\pm\sqrt{(J|\Delta|-\Gamma h)^2-16J^2h^2}}{2h},\qquad r_-r_+=4J^2.}
\]
At both endpoints concurrence vanishes. If the strict inequality fails, concurrence is identically zero; equality gives only a tangential zero of its unclipped expression at \(r=2J\).

2. If \(h=0\) and \(\Delta\ne0\), concurrence is positive for every \(r>0\), tends to zero in both endpoint limits \(r\downarrow0\) and \(r\to\infty\), and has a unique positive-rate maximum. If \(\Delta=0\), concurrence is zero for all rates, for either value of \(h\).

3. Whenever positive concurrence is attainable, its **unique** maximizer is \(r_{\mathrm{opt}}=2J\), unaffected by the preparation probabilities or either dephasing coefficient. Its sharp maximum and universal ceiling are
\[
\boxed{\max_{r>0}C(r)=2\left[\frac{J|\Delta|}{4J+\Gamma}-h\right]_+\le\frac12.}
\]
The ceiling is attained precisely by dephasing-free resetting to the pure preparation \(\lvert00\rangle\langle00\rvert\) or \(\lvert11\rangle\langle11\rvert\). The assertion of a unique maximizer is **not** made when concurrence is identically zero.

4. In the natural identical local thermal-preparation family \(a=(1-s)^2\), \(b=c=s(1-s)\), \(d=s^2\), \(0\le s\le 1/2\), define \(\eta=\Gamma/J\). For \(0<s\le1/2\), some positive reset rate creates stationary entanglement **if and only if**
\[
\boxed{s<s_c(\eta),\qquad
s_c(\eta)=\frac{6+\eta-\sqrt{\eta^2+8\eta+20}}{2(4+\eta)}.}
\]
At \(s=0\), entanglement occurs at every positive rate. In particular the zero-dephasing critical population is \(s_c(0)=(3-\sqrt5)/4\). If each qubit is prepared in a Gibbs state with excitation gap \(\epsilon>0\), then \(s=(1+e^{\beta\epsilon})^{-1}\); the equivalent inverse-temperature boundary is \(\beta\epsilon>\log((1-s_c)/s_c)\).

## Assumptions and scope
Work with \(\hbar=1\) and computational basis \(\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle\). The Hamiltonian and full Markovian equation are
\[
H=J(\lvert00\rangle\langle11\rvert+\lvert11\rangle\langle00\rvert),\qquad
\dot\rho=-i[H,\rho]+\sum_{j=1}^{2}\gamma_j(Z_j\rho Z_j-\rho)+r(\rho_* -\rho),
\]
where \(Z_j\) is Pauli \(Z\) acting on qubit \(j\), and \(\rho_*=\operatorname{diag}(a,b,c,d)\) is physically re-prepared at each joint reset. Equivalently, the reset contribution on arbitrary operators is \(r(\operatorname{tr}(\rho)\rho_*-\rho)\). The coefficients \(\gamma_j\) use the convention displayed here: the \(\lvert00\rangle\langle11\rvert\) coherence decays at rate \(\Gamma=2(\gamma_1+\gamma_2)\) before counting resets. There is no qubit-frequency detuning, amplitude damping, transverse single-qubit drive, or independent one-qubit resetting. All statements hold for every \(J>0\), \(r>0\), \(\gamma_j\ge0\) and all diagonal preparation probability vectors, including boundary values.

## Proof
**Existence and uniqueness.** Let \(\mathcal L_0\) denote the Hamiltonian plus dephasing generator, without resetting. It generates a completely positive, trace-preserving contraction semigroup. For every \(r>0\),
\[
\rho_r=r\int_0^\infty e^{-rt}e^{t\mathcal L_0}(\rho_*)\,dt
\]
is a normalized positive stationary state. Two normalized solutions differ by \(e^{-rt}e^{t\mathcal L_0}\) applied to their initial traceless difference, so trace-norm contraction ensures uniqueness and convergence.

**Exact stationary matrix.** The odd-parity populations are stationary at \(\rho_{01,01}=b\) and \(\rho_{10,10}=c\); all other off-diagonals except \(w=\rho_{00,11}\) decay homogeneously, since neither the Hamiltonian nor the diagonal reset drives them. Put \(z=\rho_{00,00}-\rho_{11,11}\), \(y=\operatorname{Im}w\), and \(S=a+d\). The nontrivial stationary equations are
\[
0=-4Jy+r(\Delta-z),\qquad 0=Jz-(r+\Gamma)y,\qquad \operatorname{Re}w=0.
\]
They have the unique solution
\[
z=\frac{r(r+\Gamma)\Delta}{D_r},\qquad
w=i\frac{Jr\Delta}{D_r},\qquad
\rho_r=\begin{pmatrix}
(S+z)/2&0&0&w\\
0&b&0&0\\
0&0&c&0\\
\overline w&0&0&(S-z)/2
\end{pmatrix}.
\]
The matrix is automatically positive because it is the convergent integral of completely positive evolutions of the reset preparation.

**Concurrence.** For this \(X\)-state the Wootters spin-flip eigenvalue formula reduces to \(C=2\max\{0,|w|-\sqrt{bc},-\sqrt{\rho_{00,00}\rho_{11,11}}\}\). The last entry is nonpositive and the displayed formula for \(C(r)\) follows. In particular a finite positive reset rate creates entanglement exactly when the stationary even-parity coherence exceeds the geometric mean of the two spectator populations.

**Optimization and sharp interval.** For \(\Delta\ne0\), differentiation gives
\[
\frac{d}{dr}\left(\frac{J|\Delta|r}{D_r}\right)
=\frac{J|\Delta|(4J^2-r^2)}{D_r^2}.
\]
It is strictly positive below \(2J\), zero at \(2J\) and strictly negative above, independently of \(\Gamma\). Its maximum is \(J|\Delta|/(4J+\Gamma)\). For \(h>0\), the strict coherence condition is equivalent to the quadratic inequality
\[
h r^2+(h\Gamma-J|\Delta|)r+4hJ^2<0.
\]
A negative interval exists precisely when \(J|\Delta|>h(4J+\Gamma)\). Its roots are the stated \(r_\pm\), and Vieta's product is \(4J^2\); thus their geometric mean coincides with the unique coherence optimum. Equality is a repeated root \(2J\) with zero concurrence. When \(h=0\), the coherence is strictly positive at every positive rate unless \(\Delta=0\). Since \(|\Delta|\le1\), \(\Gamma\ge0\) and \(h\ge0\), the concurrence maximum is at most \(2J/(4J)=1/2\), with equality exactly as specified.

**Thermal-preparation boundary.** For identical product preparations, \(|\Delta|=1-2s\) and \(h=s(1-s)\) on \(0\le s\le1/2\). The strict entanglement inequality becomes \(1-2s>(4+\eta)s(1-s)\). The left side strictly decreases in \(s\), while the right side strictly increases on \([0,1/2)\). Thus there is exactly one threshold inside \((0,1/2)\). Solving the resulting quadratic and selecting the smaller root yields \(s_c(\eta)\). Direct substitution verifies \(s_c(0)=(3-\sqrt5)/4\); the Gibbs expression follows by inversion of \(s=(1+e^{\beta\epsilon})^{-1}\).

## Verification
The associated standalone \(CHECK.py\) checks the stationary Bloch equations and rate optimization symbolically, the preparation threshold algebraically, and the resulting formula against independently assembled and solved \(16\times16\) full Liouvillian systems. It additionally calculates concurrence from the complete Wootters spin-flip spectrum rather than reusing the two-by-two formula. In one reproducible run, \(273\) assertions passed. These finite diagnostics corroborate, rather than replace, the unrestricted proof above.

A concrete strictly mixed example is \(J=1\), \(\gamma_1=0.2\), \(\gamma_2=0.3\), \(s=0.1\): then \(\Gamma=1\), \(r_-\approx0.5446441598235\), \(r_+\approx7.3442447290654\), \(r_-r_+=4\), and the unique maximum at \(r=2\) is \(C=0.14\).

## Relationship to prior work
Kulkarni and Majumdar [1] introduced the general Poisson quantum-reset entanglement framework and solved a **pure-reset, coherent transverse-field Ising pair**, observing nonmonotone concurrence. Rose, Touchette, Lesanovsky and Garrahan [2] established the general stationary spectral/resolvent law for stochastic resets, including open quantum systems; the renewal stationary-state representation here is an application of that established principle, **not a new general renewal theorem**. Hartmann, Dür and Briegel [3] established that **individual local** reset operations combined with decoherence and qubit interactions can create entangled stationary states, and already reported that imperfect mixed reset states can restrict entanglement to a finite reset-rate window. Those broad qualitative phenomena are **not** claimed as new. The asserted specific addition is the complete exact classification of **joint Poisson resetting to arbitrary diagonal separable states under pair conversion and separate local dephasing**, including reciprocal interval boundaries, a dephasing-independent unique optimum and the sharp locally thermal preparation threshold. Murauer and collaborators [4] subsequently studied **discrete-time, unitary-step** reset correlations and concurrence for the transverse-field Ising model; those discrete-time resonance results do not state the present Markovian mixed-preparation phase diagram.

## Limitations
The proof does not address independent per-qubit resets, coherent initial reset superpositions, finite detuning, amplitude damping, non-Poisson renewal resets, more than two qubits or time-dependent noise. The thermal interpretation refers to the **preparation** being a product Gibbs state of separate noninteracting qubits, not to a thermal stationary state of the interacting Hamiltonian. The exact finite window phenomenon in the broader literature is established already; the claimed contribution is its sharp new formula and design classification for this specific joint-reset pair-conversion model. Originality comparisons are necessarily bounded by inspected published sources and searchable records, so unnoticed exact prior specialization remains a publication-priority risk. No independent review or experimental validation is asserted.

## References
[1] M. Kulkarni and S. N. Majumdar, *Generating Entanglement by Quantum Resetting* (first public arXiv submission 2023-07-14), https://arxiv.org/abs/2307.07485.

[2] D. C. Rose, H. Touchette, I. Lesanovsky and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes* (2018), https://arxiv.org/abs/1806.01298.

[3] L. Hartmann, W. Dür and H.-J. Briegel, *Entanglement and its dynamics in open, dissipative systems* (2007), https://arxiv.org/abs/quant-ph/0703138.

[4] J. Murauer, S. Tornow, M. Kulkarni, E. Barkai, S. N. Majumdar and M. Singh Roy, *Entanglement diagnostics of stochastic-resetting steady states: theory and measurement on superconducting qubits* (first public submission 2026-10-29), https://arxiv.org/abs/2610.40638.

[5] W. K. Wootters, *Entanglement of Formation of an Arbitrary State of Two Qubits* (1998), https://arxiv.org/abs/quant-ph/9709029.

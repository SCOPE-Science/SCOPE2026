# Unique joint-sensing reset optimum for a dephased qubit

## Finding

The reset rate maximizing the **determinant of the stationary symmetric-logarithmic-derivative quantum Fisher information matrix** for *jointly* estimating a qubit's Hamiltonian frequency \(\omega\) and dephasing rate \(\gamma\) is uniquely determined at every \(\gamma>0\) and \(\omega\in\mathbb R\). This is a local, per-preparation, two-parameter \(D\)-optimality criterion, not Fisher information per unit time.

For Poisson full-state preparation at rate \(r>0\), set \(A=\gamma^2+\omega^2\). The determinant is
\[
\det Q(r;\gamma,\omega)=
\frac{r^4}{(\gamma^2+2\gamma r+\omega^2)\big((r+\gamma)^2+\omega^2\big)^3}.
\]
Its unique global maximizer \(r_*(\gamma,\omega)>0\) is the unique positive zero of
\[
P(r)=2A^2+4\gamma Ar-Ar^2-3\gamma r^3.
\]
It obeys the strict, parameter-uniform bounds
\[
\sqrt A<r_*<\sqrt{2A},
\]
and the stronger normalized result
\[
\frac{1+\sqrt 7}{3}\leq\frac{r_*}{\sqrt A}<\sqrt 2,
\]
with equality in the lower bound precisely when \(\omega=0\). The ratio \(r_*/\sqrt A\) is strictly increasing in \(|\omega|/\gamma\), with \(r_*(\gamma,0)=(1+\sqrt7)\gamma/3\). In the far-detuned limit,
\[
\frac{r_*}{|\omega|}\longrightarrow\sqrt2,
\qquad
\omega^4\max_{r>0}\det Q(r;\gamma,\omega)\longrightarrow\frac4{27}
\quad(|\omega|/\gamma\to\infty).
\]
The symmetric-logarithmic derivatives are operator-incompatible but weakly commute in the stationary state. Thus the determinant is an asymptotically collective-measurement-compatible information benchmark, not a universally achievable single-copy measurement performance.

## Assumptions and scope

Use \(\hbar=1\). Between resets the density matrix follows a qubit Markovian master equation with Hamiltonian \(H=\omega\sigma_z/2\) and pure phase damping \((\gamma/2)(\sigma_z\rho\sigma_z-\rho)\), with \(\gamma>0\). At events of an independent Poisson clock of *known* positive rate \(r\), the entire state is replaced by \(|+\rangle\langle+|\), where \(|+\rangle=(|0\rangle+|1\rangle)/\sqrt2\). Stationary states are measured with neither event times nor resetting records available. The jointly unknown parameters are \((\gamma,\omega)\); all other settings are known. The information matrix uses two-sided smooth parameter derivatives at every \(\gamma>0\) and \(\omega\in\mathbb R\). There is no unknown reset-rate nuisance parameter and no charge for re-preparation time. The \(D\)-criterion is the determinant of the *quantum* Fisher matrix, not that of a fixed single-copy POVM.

## Proof

**Stationary state.** By the memoryless-reset renewal law, the stationary off-diagonal coherence equals the exponentially age-weighted coherence after a fresh preparation:
\[
 c=r\int_0^\infty e^{-(r+\gamma+i\omega)t}\,dt
 =\frac r{r+\gamma+i\omega}.
\]
Therefore \(\rho=\tfrac12\begin{pmatrix}1&c\\\bar c&1\end{pmatrix}\). Its Bloch vector is
\[
 v=\frac r{(r+\gamma)^2+\omega^2}(r+\gamma,\omega,0).
\]
As \(\gamma>0\), \(|v|<1\), so the state is full rank for every finite \(r>0\).

**Quantum information and determinant.** Put \(h=(r+\gamma)^2+\omega^2\), \(m=|v|=r/\sqrt h\), and \(\varphi=\arctan(\omega/(r+\gamma))\). For a full-rank equatorial Bloch vector the SLD information line element is
\[
 ds_Q^2=\frac{dm^2}{1-m^2}+m^2d\varphi^2.
\]
Direct differentiation gives
\[
\det\frac{\partial(m,\varphi)}{\partial(\gamma,\omega)}
=-\frac r{h^{3/2}}.
\]
Multiplying the determinant of the polar metric by the *square* of the Jacobian yields \(\det Q=r^4/[h^3(h-r^2)]\). Since \(h-r^2=\gamma^2+2\gamma r+\omega^2\), this is the stated formula, strictly positive.

**Uniqueness and sharp location.** Differentiating the rational determinant, without dropping any positive denominator, yields
\[
\frac{d}{dr}\det Q=
\frac{2r^3P(r)}{(\gamma^2+2\gamma r+\omega^2)^2h^4}.
\]
From low to high degree the coefficient signs of \(P\) are \(+,+,-,-\). Descartes' rule gives at most one strictly positive zero, and \(P(0)=2A^2>0\), whereas \(P(r)\to-\infty\). The positive zero is therefore unique. The determinant tends to zero as \(r\downarrow0\) and as \(r\to\infty\); its derivative changes from positive to negative at that zero, proving strict global optimality. Direct substitution gives
\[
P(\sqrt A)=A^2+\gamma A^{3/2}>0,\qquad
P(\sqrt{2A})=-2\sqrt2\gamma A^{3/2}<0.
\]
This gives the first interval. To sharpen and establish monotonicity, put \(t=\gamma/\sqrt A\in(0,1]\), \(y=r_*/\sqrt A\in(1,\sqrt2)\). Its equation becomes
\[
F(y,t)=2+4ty-y^2-3ty^3=0.
\]
At \(y=2/\sqrt3\), \(F=2/3>0\); hence its unique positive root satisfies \(y>2/\sqrt3\). Consequently \(\partial_t F=y(4-3y^2)<0\) and \(\partial_yF=-2y+t(4-9y^2)<0\), so implicit differentiation gives \(dy/dt<0\). Because \(t\) strictly decreases with \(|\omega|/\gamma\), \(y\) strictly increases. At \(t=1\), \(F(y,1)=(y+1)(2+2y-3y^2)\), giving \(y=(1+\sqrt7)/3\); at \(t\downarrow0\), the unique positive root tends to \(\sqrt2\).

**Large detuning.** For fixed positive \(\gamma\), the preceding limit implies \(r_*/|\omega|\to\sqrt2\). Inserting \(r\sim\sqrt2|\omega|\) into the determinant gives \(\omega^4\det Q(r_*)\to 4/27\).

**Compatibility qualifier.** SLD Pauli-vector parts for the two parameters lie in the equatorial plane, so their commutator is proportional to \(\sigma_z\) and its expectation in the equatorial state vanishes. The Jacobian computed above is nonzero, so the two SLDs do not commute as operators. Thus single-copy measurements cannot in general saturate the entire SLD information matrix, while the vanishing mean commutator is the standard local asymptotic compatibility condition for collective measurements. This does not construct such measurements or address finite sample sizes.

## Verification

Run \(\texttt{python check_joint_qfim.py}\) with Python 3, NumPy and SymPy. The standalone script recomputes the SLD information matrix from the Bloch metric symbolically, factors the exact determinant and its derivative, verifies both sharp bracket substitutions, and then independently computes the information matrix from finite-difference derivatives of the two-by-two density matrix using an eigenbasis SLD formula. It compares 60 quantum-matrix numerical parameter triples (including negative, positive, and zero frequencies) and brackets 12 optimization roots. All 72 parameter cases passed, alongside exact symbolic identities. These finite checks supplement—not replace—the algebraic all-parameter proof above.

## Relationship to prior work

The full-rank equatorial-qubit QFIM and weak-commutativity/measurement tradeoff are classical ingredients of joint phase/diffusion estimation; in particular, Vidrighin et al. (2014) provide the geometric measurement context. The renewal-to-stationary-state construction for qubits appears in Sevilla and Valdés-Hernández (2022). Le, Nguyen and Ho (2023) develop multiparameter sensing under dephasing with variational probes and measurements. None of those inspected discussions formulates the joint unknown *frequency and damping* stationary Poisson-repreparation \(D\)-optimal reset-rate problem or proves the cubic unique optimizer and sharp normalization interval. A distinct published result for discrete-time phase-only reset sensing optimizes one QFI entry; it does not optimize the determinant for two unknown parameters. Li, Tong and Bao (2026, v1) derive a general *scalar* reset-QFI response identity and list multiparameter estimation as a future direction; their later conditional-reset study also emphasizes a no-go for comparing blind-reset performance against the best transient no-reset protocol, which is a different benchmark from the present stationary determinant criterion. The present claim does **not** re-label the standard two-parameter QFIM as new; the proposed contribution is the global reset-design theorem, its sharp bounds, and its physically constrained attainment interpretation.

## Limitations

The conclusion concerns a single stationary reset-to-\(|+\rangle\) Markov model with known Poisson rate and exactly two unknown parameters. The quantum information determinant is a local volume criterion, not an experimentally demonstrated estimator, a finite-sample precision guarantee, or precision per unit time. Weak commutativity does not make the two SLD operators commute or provide a single-shot optimal POVM. An arbitrary fixed measurement, an unknown reset-rate nuisance parameter, amplitude damping, non-Markovian decoherence, and preparation costs fall outside the theorem. The general equatorial QFIM makes the determinant algebraically accessible; the novelty assessment is about the specific unique global optimization and its sharp inequalities, not a newly invented information geometry. Independent literature-priority review has not been performed.

## References

- M. D. Vidrighin et al., *Joint estimation of phase and phase diffusion for quantum metrology*, Nature Communications **5**, 3532 (2014), https://arxiv.org/abs/1410.5353 (equatorial qubit joint-Fisher geometry and compatibility).
- F. J. Sevilla and A. Valdés-Hernández, *Dynamics of closed quantum systems under stochastic resetting*, Journal of Physics A (2023), https://arxiv.org/abs/2209.05643 (first public version 2022-09-12; quantum renewal framework).
- T. K. Le, H. Q. Nguyen and L. B. Ho, *Variational quantum metrology for multiparameter estimation under dephasing noise*, Scientific Reports **13**, 17775 (2023), https://arxiv.org/abs/2305.08289 (first public version 2023-05-15; motivating multiparameter dephasing problem).
- S. Li, Q. Tong and R. Bao, *Reset-Enhanced Dissipative Quantum Metrology* (arXiv v1, 2026-10-22), https://arxiv.org/abs/2610.31249v1 (scalar reset-QFI response and frequency-sensing results; substantially revised v2 2026-11-15).

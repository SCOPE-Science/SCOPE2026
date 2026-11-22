# A sharp entanglement-death frontier for one-sided resetting of a coupled qubit pair

## Finding

Consider two interacting qubits with Hamiltonian \(H=J(X\otimes X)+h(Z\otimes I+I\otimes Z)\), where \(J,h>0\). At independent Poisson times of rate \(r>0\), **only the first qubit** is re-prepared in \(|0\rangle\), leaving the second-qubit marginal unchanged. The resulting state has a unique faithful stationary density matrix and exactly the concurrence
\[
\boxed{C(r)=\frac{J}{Q}\Big[\sqrt{r^2+16h^2}-\sqrt{2r^2+4J^2}\Big]_+,\qquad Q=r^2+4J^2+8h^2.}
\]
Here \([a]_+=\max\{a,0\}\). In particular, stationary entanglement is present **if and only if**
\[
\boxed{h>\frac J2\quad\text{and}\quad0<r<2\sqrt{4h^2-J^2}.}
\]
Thus the sharp field threshold is \(h=J/2\). Above it, increasing the local-reset rate across \(r_c=2\sqrt{4h^2-J^2}\) causes exactly one entangled-to-separable transition. Below or at the field threshold, no strictly positive reset rate produces stationary entanglement. For example, \(h=J=1\) gives \(r_c=2\sqrt3\).

## Assumptions and scope

Use \(X,Y,Z\) for Pauli matrices, \(I\) for the two-dimensional identity, and the \(Z\) eigenbasis \(|0\rangle,|1\rangle\), ordered as \(|00\rangle,|01\rangle,|10\rangle,|11\rangle\). Set \(\hbar=1\). For every real \(J,h,r>0\), the unconditional density matrix obeys the completely positive, trace-preserving continuous-time equation
\[
\frac{d\rho}{dt}=\mathcal L(\rho)=-i[H,\rho]+r\big(|0\rangle\langle0|\otimes\operatorname{tr}_1\rho-\rho\big).
\]
The physical reset is a local replacement quantum channel, not postselection, local dephasing, a global reset of both qubits, or an instantaneous reset of the unobserved second-qubit state. Entanglement refers to stationary two-qubit concurrence (equivalently nonpositive partial transpose for this bipartite dimension). No restriction is imposed on the initial density matrix.

## Proof

**1. Exact stationary solution.** For \(Q=r^2+4J^2+8h^2\), set
\[
A=\frac{r^2+2J^2+16h^2}{2Q},\quad B=\frac{r^2+2J^2}{2Q},\quad T=\frac{J^2}{Q},
\]
\[
w=\frac{J(2h+ir/2)}{Q},\qquad z=\frac{iJr}{2Q}.
\]
Then
\[
\boxed{\rho_*=\begin{pmatrix}A&0&0&w\\0&B&z&0\\0&\bar z&T&0\\\bar w&0&0&T\end{pmatrix}.}
\]
Direct matrix multiplication gives \(\operatorname{tr}\rho_*=1\) and \(-i[H,\rho_*]+r(|0\rangle\langle0|\otimes\operatorname{tr}_1\rho_*-\rho_*)=0\). This is also independently checked entry by entry by the accompanying symbolic program. Reordering the basis into the \((00,11)\) and \((01,10)\) pairs yields two Hermitian \(2\times2\) blocks with positive diagonal entries and strictly positive determinants
\[
AT-|w|^2=\frac{J^2(r^2+4J^2+16h^2)}{4Q^2}>0,
\]
\[
BT-|z|^2=\frac{J^2(r^2+4J^2)}{4Q^2}>0.
\]
Hence \(\rho_*\) is strictly positive definite.

**2. Uniqueness in the full state space.** The reset channel admits jump operators \(L_0=\sqrt r\,|0\rangle\langle0|\otimes I\) and \(L_1=\sqrt r\,|0\rangle\langle1|\otimes I\), with \(\sum_jL_j^\dagger L_j=rI\otimes I\). For any adjoint-generator fixed operator \(F\), the dissipation identity gives
\[
\mathcal L^\dagger(F^\dagger F)-\mathcal L^\dagger(F^\dagger)F-F^\dagger\mathcal L^\dagger(F)=\sum_{j=0}^1[L_j,F]^\dagger[L_j,F].
\]
Taking expectation in the faithful stationary \(\rho_*\), the left side vanishes, so \([L_j,F]=0\). Repeating with \(F^\dagger\) gives \([L_j^\dagger,F]=0\). The joint commutant of those first-qubit matrix units is \(F=I\otimes G\). The remaining Hamiltonian commutator is \(JX\otimes[X,G]+hI\otimes[Z,G]\), forcing \([X,G]=[Z,G]=0\) and hence \(G\) scalar since \(J,h>0\). The adjoint fixed space is one-dimensional; rank-nullity implies the Schrödinger stationary kernel is likewise one-dimensional. Therefore \(\rho_*\) is the unique stationary density matrix.

**3. Exact concurrence and sharp frontier.** The standard two-qubit \(X\)-state concurrence is
\[
C=2\max\{0,|w|-\sqrt{BT},|z|-\sqrt{AT}\}.
\]
The second candidate is strictly negative because
\[
|z|^2-AT=-\frac{J^2(r^2+4J^2+32h^2)}{4Q^2}<0.
\]
The first candidate has sign equal to
\[
|w|^2-BT=\frac{J^2(16h^2-4J^2-r^2)}{4Q^2}.
\]
Since both square-root arguments are positive and \(J>0\), the positive branch is exactly the displayed concurrence and can change sign at most once as \(r\) grows. Its positivity is equivalent to \(16h^2-4J^2-r^2>0\). This is possible for some positive \(r\) precisely if \(h>J/2\), in which case the unique crossing is \(r_c=2\sqrt{4h^2-J^2}\). At equality and above, the density matrix is PPT and hence separable by the two-qubit PPT criterion.

## Verification

Run `python checker.py` with Python 3.10+, NumPy and SymPy. The checker verifies the full symbolic master equation and block determinants, tests both partial-transpose branch inequalities, and independently assembles and solves the complete \(16\times16\) complex Liouvillian for 72 positive-parameter triples. It compares the resulting density matrices and independently evaluates concurrence via the Wootters spin-flip eigenvalue formula. The current checker completes 442 assertions. Numerical checks illustrate and corroborate the exact algebraic proof; they are not a substitute for its universal quantifiers.

## Relationship to prior work

Kulkarni and Majumdar [1] solve a pair of interacting spins subjected to **joint full-system** Poisson resetting, not marginal-preserving resetting of the first spin alone. Magoni and colleagues [2] treat globally reset noninteracting qubit ensembles. Wald and colleagues [3] study discrete-time gates with full-state resets, so their resonant stationary mixtures do not supply this continuous-time local-replacement threshold. An existing exact one-sided-resetting Ising-dimer classification [4] resets the first qubit in an eigenstate of its Ising coupling \(Z\), with local drives transverse to that coupling, and finds stationary separability. After the same single-qubit Hadamard rotation on both sites, **the present protocol instead resets the first qubit in an eigenstate of the transverse drive**, perpendicular to its Ising coupling. This is a different physical channel, not a basis re-expression of [4]; the strictly positive concurrence regime supplies a sharp contrast. The standard Wootters formula and two-qubit PPT criterion are used without claiming them as new.

## Limitations

The classification assumes one locally reset qubit, an exactly prepared pure \(|0\rangle\) state, no additional dissipation, identical positive fields on both qubits, and strictly positive \(J,h,r\). It makes no assertion about finite-time transient concurrence, imperfect or thermal reset states, or many-body scalability. The \(r\downarrow0\) expression describes the limit through strictly positive reset rates, not uniqueness at exactly zero resetting. Independent assessment of literature coverage and publication priority remains necessary; checked databases cannot certify absolute novelty.

## References

[1] M. Kulkarni and S. N. Majumdar, *Generating Entanglement by Quantum Resetting*, arXiv:2307.07485, first submitted 2023-07-14, https://arxiv.org/abs/2307.07485.

[2] M. Magoni, F. Carollo, G. Perfetto and I. Lesanovsky, *Emergent quantum correlations and collective behavior in non-interacting quantum systems subject to stochastic resetting*, arXiv:2202.12655, https://arxiv.org/abs/2202.12655.

[3] S. Wald, L. H. Yao, T. Platini, C. Hooley and F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497, https://arxiv.org/abs/2410.11497.

[4] *One-sided quantum resets enforce separability but strictly directional discord in an Ising dimer*, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-one-sided-quantum-resets-enforce-separability-but-strictly-direc--1d75ced6406d.
